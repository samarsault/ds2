#
# Interactive shell for the cli
#

from cmd import Cmd
import ds2

db = None

class DbShell(Cmd):
    def do_add(self, args):
        """
            Adds a file to database
            Syntax: add file_name
        """
        if len(args) == 0:
            print('No File Specified')
            return
        else:
            if db.add_file(args):
                print('Success')
            else:
                print('Error: File not found')

    def do_ls(self, args):
        """ Lists the Files in the Database"""
        for item in db.meta_data.data:
            print('(%s) %s' %(item['id'], item['name']))

    def do_rm(self, args):
        """
            Delete File from Database
            Syntax: rm file_id
        """
        k = 0
        try:
            k = int(args)
            print(k)
            if db.rm_file(k):
                print('Success')
            else:
                print('Error: not a valid id')
        except:
            print('Not a valid File Id')

    def do_extract(self, args):
        """ 
            Extracts File with ID to location
            Syntax: extract file_id
        """
        j= args.split(' ')
        if len(j) < 1:
             print ('Not enough arguments')
        else:
            res = None
            if len(j)==1:
                res = db.get_file(int( j[0] ))
            else:
                res =db.get_file(int( j[0] ), j[1])
            if res == -1:
                print ('Error, invalid ID')
            else:
                print ('Success!')

    def do_quit(self, args):
        """Quits the shell."""
        print ('Quitting.')
        raise SystemExit

def start_shell(db_name):
    global db
    db = ds2.Db(db_name)
    prompt = DbShell()
    prompt.prompt = '> '
    prompt.cmdloop('Initialized Database %s' %db_name)
