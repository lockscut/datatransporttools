import pyodbc
from transport import *

class ODBCTransport(DataTransport):
    def __init__(self, conn, table, schema='dbo', truncate=False, *args, **kwargs):
        DataTransport.__init__(self, *args, **kwargs)
        if type(conn) == str:
            self.conn = pyodbc.connect(conn)
            self.close_conn = True
            self.commit = True
        else:
            assert(hasattr(self, 'cursor'))
            self.conn = conn
            self.close_conn = False
            self.commit = False
        self.schema = schema
        self.table = table
        self.truncate = truncate

    def get_insert_str(self, data):
        insert_str = 'INSERT INTO %s VALUES(' % self.get_quoted_table()
        for i in range (0, len(data)):
            insert_str = insert_str + '?, '
        insert_str = insert_str.rstrip(', ') + ')'
        return insert_str      

    def prep_read(self):
        if not self._reader:
            self._reader = self.conn.cursor()
            self._reader.execute("SELECT * FROM %s" % self.get_quoted_table())              

    def prep_write(self):        
        if not self._writer:
            self._writer = self.conn.cursor()
            if not hasattr(self, 'get_insert_str'):
                raise Exception("Subclasses of ODBCTransport must define get_insert_str method.")
            self.insert_str = self.get_insert_str()  
            if self.truncate:
                sql_s = "DELETE FROM %s" % self.get_quoted_table()
                self._writer.execute(sql_s)

    def close(self):
        if self.commit: 
            self.conn.commit()
        if self._reader: 
            self._reader.close()
        if self._writer:
            self._writer.close()
        if self.close_conn: 
            self.conn.close()

    def get_record(self):
        self.prep_read()
        for row in self._reader:
            yield row

    def put_record(self, data):
        self.prep_write()
        self._writer.execute(self.get_insert_str(data), data)

    def get_headers(self):
        self.prep_read()
        return map(lambda x: x[0], self._reader.description)
