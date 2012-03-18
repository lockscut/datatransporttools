from transport import *
from odbc import ODBCTransport
from batchedodbc import BatchedODBCTransport

class SharedMySQL(object):

    def get_quoted_table(self):
        if self.schema:
            raise Exception("MySQL does not support schemas?")
        return "`%s`" % self.table

    @classmethod
    def __from_values(cls, server, database, username, password, table, truncate=False, *args, **kwargs):
        c = 'DRIVER=mysql;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (server, database, username, password)   
        # ODBCTransport def => def __init__(self, conn, table, schema='dbo', truncate=False, *args, **kwargs): 
        return cls(c, table=table, schema=None, truncate=truncate, *args, **kwargs) 
    

class MySQLTable(SharedMySQL, BatchedODBCTransport):
    pass
    
class MySQLTableNoBatching(SharedMySQL, ODBCTransport):
    pass
