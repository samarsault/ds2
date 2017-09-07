import csvmapper
from csvmapper import FieldMapper, CSVParser

from shared import conf

class Key(object):
    def __init__(self):
        parser = CSVParser(conf['keys'], hasHeader = True )
        try:
            self.data = parser.buildDict()
        except:
            self.data = [] # empty file

    def get_hashed_key(self, name):
        for item in self.data:
            if item['name'] == name:
                return item['hash']

    def add_db_key(self, name, hsh):
        self.data.append({ 'name': name, 'hash': hsh })

    def remove_db_key(self, name):
        for item in self.data:
            if item['name'] == name:
                self.data.remove(item)
                break

    def save(self):
        writer = csvmapper.CSVWriter(self.data)
        writer.write(conf['keys'])
