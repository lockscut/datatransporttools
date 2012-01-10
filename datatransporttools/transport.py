import sys

class UnavailableHeadersException(Exception):
    """import does not have any headers or import type does not support headers"""
    pass
    
class ReadOnlyTransportException(Exception):
    """the particular datasource that was used as an export only supports being used as a import."""

class DataTransport(object):
    _reader = None
    _writer = None

    def prep_read(self): pass
    def prep_write(self): pass
    def close(self): pass