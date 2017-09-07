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
from shared import init_dir_struct, conf
from db import Db
from keys import Key
import shell
