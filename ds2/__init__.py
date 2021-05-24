"""

    Structure:
        .keys file -> * Contains (Hashed) Passwords for all Database
         (Unecrypted) * CSV Document with Fields (name, hash)
                      * Access using Keys Object

        .store/${db_name} -> * Encrypted using key in keys file, contains metadata of the db
                             * CSV Document with Fields (id, name, key)
        data/${db_name} -> * File Encrypted with key found in ./store/${db_name}[id=file_name]
"""

""" Import Modules """
from ds2.shared import init_dir_struct, conf
from ds2.db import Db
from ds2.keys import Key
import ds2.shell
