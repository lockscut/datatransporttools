import os
import xlrd
from transport import *

class ExcelFile(DataTransport):
    def __init__(self, file_name, has_header=True, sheet_name=None, begin_column=0, end_column=None):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.begin_column=begin_column
        self.end_column=end_column
        self.has_header = has_header
        
    def prep_read(self):
        assert os.path.exists(self.file_name)
        workbook = xlrd.open_workbook(self.file_name)
        if self.sheet_name:
            self._reader = workbook.sheet_by_name(self.sheet_name)
        else:
            self._reader = workbook.sheet_by_index(0)
        if not self.end_column:
            self.end_column = self._reader.ncols

    def get_record(self):
        start_row = 0 
        if self.has_header:
            start_row = 1
            
        for i in range(start_row, self._reader.nrows):
            yield map(lambda x: x.value.lstrip().rstrip() if x.ctype==1 else x.value, self._reader.row(i))[self.begin_column:self.end_column]
        
    def get_headers(self):
        if self.has_header:
            return map(lambda x: x.value, self._reader.row(0))[self.begin_column:self.end_column]
        else:
            raise UnavailableHeadersException
            
    def close(self):
        pass
    