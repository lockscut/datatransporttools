from transport import *
from odbc import ODBCTransport
from batchedodbc import BatchedODBCTransport 

class SharedMSSQL(object):

    def get_quoted_table(self):
        return "[%s].[%s]" % (self.schema, self.table)

    def prep_write(self):
        if self.truncate:
            self._writer.execute("TRUNCATE TABLE %s" % self.get_quoted_table())
            self.truncate = False
        super(MSSQLTable, self).prep_write()
        
 
class MSSQLTable(SharedMSSQL, BatchedODBCTransport):
    pass
    
class MSSQLTableNoBatching(SharedMSSQL, ODBCTransport):
    pass