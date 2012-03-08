import sys

class UnavailableHeadersException(Exception):
    """import does not have any headers or import type does not support headers"""
    pass
    
class ReadOnlyTransportException(Exception):
    """the particular datasource that was used as an export only supports being used as a import."""

class DataTransport(object):

    def prep_read(self):
        print("WARNING: prep read is not defined for this transport (%s).") % self.__class__.__name__ 
        
    def prep_write(self): 
        print("WARNING: prep_write is not defined for this transport (%s).") % self.__class__.__name__               
        
    def close(self):
        print("WARNING: close is not defined for this transport (%s).") % self.__class__.__name__     
        
    def get_record(self):
        raise Exception("Transport must define get_record to facilitate iterator")

    def __init__(self):
        self.completed = 0     
        self._reader = None
        self._writer = None
        
    __iter__ = get_record