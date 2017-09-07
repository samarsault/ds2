from tempfile import NamedTemporaryFile
from shared import encode_key, meta_loc
import bson, os
from crypt import *

""" Database Metadata """
class Meta(object):
    """ Meta(database name, database password) """
    def __init__(self, name, key):
       self.name = name
       self.key = encode_key(key)

       fs = open(meta_loc(name), mode='rb')
       cont = fs.read()
       if cont == '':
            self.broot = { 'data':[] }
            self.data = self.broot['data']
            return
       ps = fdecrypt(cont, self.key)
       self.broot = bson.loads(ps)
       self.data = self.broot['data']

    def assign_id(self):
        mx = len(self.data)
        is_assigned = [ False ] * (mx + 1)
        for item in self.data:
            is_assigned[item['id']] = True
        for x in range(0, mx+1):
            if is_assigned[x] == False:
                return x

    # add file to metadata
    def add_file(self, fpath, key, iv, fid):
        self.data.append({'name': fpath, 'key': key, 'iv': iv, 'id': fid})

    # remove file from metadata
    def remove_file(self, file_id):
        for item in self.data:
            if item['id'] == file_id:
                self.data.remove(item)

    def get_key(self, file_id):
        return self.get_meta(file_id)['key']

    # -1 => not found
    def get_meta(self, file_id):
        for item in self.data:
            if item['id'] == file_id:
                return item
        return -1

    def destroy(self):
        os.remove( meta_loc(self.name) )

    def save(self):
        with open(meta_loc(self.name), mode='wb') as stream:
            stream.write(fencrypt(bson.dumps(self.broot), self.key))
