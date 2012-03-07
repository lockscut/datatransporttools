from transport import *
from odbc import ODBCTransport

class MySQLTable(ODBCTransport):
    insert_str = None
    
    def get_insert_str(self, data):
        if not self.insert_str:
            insert_str = 'INSERT INTO %s VALUES(' % self.table
            for i in range (0, len(data)):
                insert_str = insert_str + '?, '
            insert_str = insert_str.rstrip(', ') + ')'
            self.insert_str = insert_str
        return self.insert_str
    
    def put_record(self, data):
        self._writer.execute(self.get_insert_str(data), data)
