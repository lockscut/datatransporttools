from transport import *
from odbc import ODBCTransport
from batchedodbc import BatchedODBCTransport

class SharedPostgreSQL(object):

    def get_quoted_table(self):
        if self.schema:
            return '"%s"."%s"' % (self.schema, self.table)
        else:
            return '"%s"' % self.table

    @classmethod
    def make_connstr(self, **kwargs):
        return ';'.join(map(lambda (k,v): "%s=%s" % (str(k),str(v)), kwargs.iteritems()))

    @classmethod
    def by_value(cls, table, driver, **kwargs):
        if any(map(lambda k: k not in kwargs, ('username', 'password', 'database'))):
            raise Exception("must specify username, password, and database")
        if 'server' not in kwargs:
            kwargs['server'] = 'localhost'
        if 'port' not in kwargs:
            kwargs['port'] = 5432
        s = "Driver=%s;%s" % (driver, cls.make_connstr(**kwargs))
        print s
        return cls(cls.make_connstr(**kwargs), table)

    @classmethod
    def by_value_ansi(cls, table, **kwargs):
        return cls.by_value(table, '{PostgreSQL ANSI}', **kwargs)

    @classmethod
    def by_value_unicode(cls, table, **kwargs):
        return cls.by_value(tabl, '{PostgreSQL Unicode}', **kwargs)


class PostgreSQLTable(SharedPostgreSQL, BatchedODBCTransport):
    pass
    
class PostgreSQLTableNoBatching(SharedPostgreSQL, ODBCTransport):
    pass
