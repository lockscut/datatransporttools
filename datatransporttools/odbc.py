import pyodbc
from transport import *

class ODBCTransport(DataTransport):
    def __init__(self, conn, table, schema='dbo', truncate=False):
        DataTransport.__init__(self)
        if type(conn) == str:
            self.conn = pyodbc.connect(conn)
            self.close_conn = True
            self.commit = True
        else:
            self.conn = conn
            self.close_conn = False
            self.commit = False
        self.schema = schema
        self.table = table
        self.truncate = truncate
        
    def prep_write(self):
         if not self._writer:
            self._writer = self.conn.cursor()

    def close(self):
        if self._reader: 
            self._reader.close()
        if self._writer:
            self._writer.close()
        if self.commit: 
            self.conn.commit()
        if self.close_conn: 
            self.conn.close()
        
    def get_record(self):
        self.prep_read()
        for row in self._reader.fetchall():
            yield row
    
    def get_headers(self):
        self.prep_read()
        return map(lambda x: x[0], self._reader.description)