from odbc import *

class BatchedODBCTransport(ODBCTransport):
    DEFAULT_BATCH_SIZE = 10000

    def prep_write(self, *args, **kwargs):
        super(BatchedODBCTransport, self).prep_write(*args, **kwargs)
        self.__cache = []
        self.__batch_size = kwargs.get('batch_size', self.DEFAULT_BATCH_SIZE)
        
    def __flush(self):  
        self._writer.executemany(self.get_insert_str(data), self.__cache)
        self.__cache = []
        
    def close(self):
        self.__flush()
        super(BatchedODBCTransport, self).close()
        
    def put_record(self, data):
        self.prep_write()
        self.__cache.append(data)
        if len(self.__cache) >= self.__batch_size:
            self.__flush()