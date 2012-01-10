from transport import *
from odbc import ODBCTransport

class AccessTable(ODBCTransport):
    def __init__(self, file_path, table, truncate=False):
        connstr = "Driver={Microsoft Access Driver (*.mdb)};Dbq=%s" % file_path
        ODBCTransport.__init__(self, conn=connstr, table=table, truncate=truncate)
        
    def prep_read(self):
        if not self._reader:
            self._reader = self.conn.cursor()
            self._reader.execute("SELECT * FROM [%s]" % self.table)

class AccessQuery(ODBCTransport):
    def __init__(self, file_path, query):
        connstr = "Driver={Microsoft Access Driver (*.mdb)};Dbq=%s" % file_path
        ODBCTransport.__init__(self, conn=connstr, table=None)
        self.query = query
        
    def prep_read(self):
        if not self._reader:
            self._reader = self.conn.cursor()
            self._reader.execute(self.query)

    def get_record(self):
        for row in self._reader.fetchall():
            yield tuple(row)