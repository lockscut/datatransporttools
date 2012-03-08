import os.path
from transport import *
from odbc import ODBCTransport

class AccessTable(ODBCTransport):
    def __init__(self, file_path, *args, **kwargs):
        connstr = "Driver={Microsoft Access Driver (*.mdb)};Dbq=%s" % file_path
        ODBCTransport.__init__(self, conn=connstr, *args, **kwargs)
        
    def prep_read(self):
        if not self._reader:
            self._reader = self.conn.cursor()
            self._reader.execute("SELECT * FROM [%s]" % self.table)

class AccessQuery(ODBCTransport):
    def __init__(self, file_path, query):
        assert os.path.exists(file_path)
        connstr = "Driver={Microsoft Access Driver (*.mdb)};Dbq=%s" % file_path
        ODBCTransport.__init__(self, conn=connstr, table=None)
        self.query = query
        
    def prep_read(self):
        if not self._reader:
            self._reader = self.conn.cursor()
            self._reader.execute(self.query)