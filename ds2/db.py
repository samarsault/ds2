import os
import shutil
from metadata import Meta
from keys import Key
from shared import conf, meta_loc, create_pass, ask_pass
from crypt import *
import sys

class Db(object):
    def __init__(self, name):
        self.name = name
        self.key_store = Key()
        self.dr = conf['home'] + '/data/' + self.name # file storage location
        if os.path.exists(meta_loc(name)): # database exists
            pwd = ask_pass(self.key_store.get_hashed_key(name))
            if pwd == -1:
                sys.exit(1) # TODO: Something better
            self.meta_data = Meta(name, pwd) # auth success

    def count(self):
        return len(self.meta_data.data)

    def create(self):
        if not os.path.exists(self.dr):
            os.makedirs(self.dr)
        pwd, hsh = create_pass() # (password, hash)
        self.key_store.add_db_key(self.name, hsh)
        self.key_store.save()
        open(meta_loc(self.name), 'w').close()
        self.meta_data = Meta(self.name, pwd)

    def add_file(self, source):
        if not os.path.exists(source):
            return False
        con = ''
        with open(source, 'rb') as fs:
            con = fs.read()
        key = os.urandom(32)
        iv = os.urandom(16)
        file_id = self.meta_data.assign_id()

        with open(self.dr + '/' + str(file_id), mode='wb') as fl:
            fl.write(encrypt(con, key, iv))

        self.meta_data.add_file(source, key, iv, file_id)
        self.meta_data.save()
        return True

    def rm_file(self, file_id):
        path = self.dr + '/' + str( file_id )
        if os.path.isfile(path):
            os.remove(path)
            self.meta_data.remove_file(file_id)
            self.meta_data.save()
            return True
        return False

    def get_file(self, file_id, dest=None):
        m = self.meta_data.get_meta(file_id)
        if m == -1:
            return -1 # error
        if dest is None:
            dest = os.path.basename(m['name'])
        with open(self.dr + '/' + str(file_id), mode='rb') as fs:
            s = decrypt(fs.read(), m['key'], m['iv'])
            with open(dest, mode='wb') as ws:
                ws.write(s)

    # Destroy database
    def destroy(self):
        shutil.rmtree(self.dr)
        self.key_store.remove_db_key(self.name)
        self.meta_data.destroy()
        # save changes
        self.key_store.save()
