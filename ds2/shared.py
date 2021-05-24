import os
import bcrypt
import base64

from getpass import getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

conf = { }
if 'DS2_DIR' in os.environ:
    conf['home'] = os.path.expandvars('${DS2_DIR}');
else:
    conf['home'] = ''

conf['keys'] = conf['home'] + '/.keys'
conf['store'] = conf['home'] + '/.store/'

def init_dir_struct():
    if not os.path.isdir(conf['home']):
        os.makedirs(conf['home'])
    if not os.path.isfile(conf['keys']):
        open(conf['keys'], 'a').close()
    if not os.path.isdir(conf['home'] + '/data'):
        os.makedirs(conf['home'] + '/data')
    if not os.path.isdir(conf['store']):
        os.makedirs(conf['store'])


def meta_loc(name):
    return conf['store']+ name

def check_pass(pwd, hsh):
    return bcrypt.checkpw(pwd.encode(), hsh.encode())

def ask_pass(hsh):
    pwd = ''
    tries = 1
    while tries <= 3:
        pwd = getpass('Enter Password:')
        if check_pass(pwd, hsh):
            break
        print ('Incorrect, Please Try Again.')
        tries+=1

    if tries > 3:
        print ('No. of Tries Exceeded Limit, exiting...')
        return -1
    return pwd


# returns hashed password
def create_pass():
    pwd = getpass('Enter Password:')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd.encode(), salt);
    return pwd, hashed


def encode_key(password):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password.encode())
    return base64.urlsafe_b64encode(digest.finalize())
