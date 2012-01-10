from transport import *

class SQLAlchemyQuery(DataTransport):
    def __init__(self, query_obj, attributes=[]):
        DataTransport.__init__(self)
        self._reader = query_obj
        self.attributes = attributes
        
    def get_headers(self):
        return self.attributes
            
    def get_record(self):
        for obj in self._reader.all():
            yield map(lambda attrib: getattr(obj, attrib), self.attributes)