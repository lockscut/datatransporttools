from transport import *
from odbc import ODBCTransport
from batchedodbc import BatchedODBCTransport

class SharedPostgreSQL(object):

    def __get_quoted_table(self):
        if self.schema:
            return '"%s"."%s"' % (self.schema, self.table)
        else:
            return '"%s"' % self.table

    @classmethod
    def make_connstr(self, **kwargs):
        return ';'.join(map(lambda k,v: "k=v" % (k,v)))

    @classmethod
    def by_value(cls, **kwargs):
        if any(map(lambda k: k in kwargs, ('driver', 'username', 'password', 'database'))):
            raise Exception("must specify username, password, and database")
        if 'server' not in kwargs:
            kwargs['server'] = 'localhost'
        if 'port' not in kwargs:
            kwargs['port'] = 5432
        return cls(cls.make_connstr(kwargs))

    @classmethod
    def by_value_ansi(cls, **kwargs):
        kwargs['driver'] = '{PostgreSQL ANSI}'
        return cls.by_value(**kwargs)

    @classmethod
    def by_value_unicode(cls, **kwargs):
        kwargs['driver'] = '{PostgreSQL Unicode}'
        return cls.by_value(**kwargs)


class PostgreSQLTable(SharedPostgreSQL, BatchedODBCTransport):
    pass
    
class PostgreSQLTableNoBatching(SharedPostgreSQL, ODBCTransport):
    pass
