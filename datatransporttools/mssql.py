from transport import *
from odbc import ODBCTransport

class MSSQLTable(ODBCTransport):
    def prep_read(self):
        if not self._reader:
            self._reader = self.conn.cursor()
            self._reader.execute("SELECT * FROM [%s].[%s]" % (self.schema, self.table))
            
    def prep_write(self, truncate=False):
        if not self._writer:
            self._writer = self.conn.cursor()
        if self.truncate:
            # not amazing to use string interpolation instead of database level string interpolation, but won't work
            # since DBI layer interpolation will attempt to quote and then die miserably. not like someone will sql inject it. 
            self._writer.execute("TRUNCATE TABLE [%s].[%s]" % (self.schema, self.table))
    
    def put_record(self, data):
        insert_str = 'INSERT INTO [%s].[%s] VALUES(' % (self.schema, self.table)
        for i in range (0, len(data)):
            insert_str = insert_str + '?, '
        insert_str = insert_str.rstrip(', ') + ')'
        try:
            self._writer.execute(insert_str, data)
        except Exception, e:
            print insert_str, data
            raise e