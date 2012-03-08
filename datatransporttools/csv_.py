import csv
from transport import *

class CSVFile(DataTransport):
    def __init__(self, file_name, has_header=True, **kwargs):
        DataTransport.__init__(self)
        if 'lineterminator' not in kwargs: 
            kwargs['lineterminator'] = '\n'
        self.kwargs = kwargs
        self.file_name = file_name
        self.has_header = has_header

    def prep_read(self):
        self._file = open(self.file_name, 'r')
        if not self._reader:
            self._reader = csv.reader(self._file, **self.kwargs)

    def prep_write(self):
        self._file = open(self.file_name, 'w')
        if not self._writer:
            self._writer = csv.writer(self._file, **self.kwargs)

    def put_record(self, data):
        self._writer.writerow(data)

    def get_record(self):
        if self.has_header:
            self._reader.next()
        for row in self._reader:
            yield row

    def close(self):
        self._file.close()
