from transport import *

class Iterable(DataTransport):
    def __init__(self, iterable):
        DataTransport.__init__(self)
        assert hasattr(iterable, '__iter__')   
        self.iterable = iterable

    def put_record(self, data):
        self._writer.writerow(data)
        
    def get_record(self):
        for r in self.iterable:
            yield r

    def prep_write(self):
        self.cache = []

    def put_record(self, r):
        self.cache.append(r)
