Data Transport Tools
####################

A lightweight Python toolkit designed to allow for easy, transactional conversion of data between common data storage mediums. Currently supports:

 * ODBC Tables, Queries (batching supported)
 
   * MySQL
   * PostgreSQL
   * Microsoft SQL Server
   * Microsoft Access

 * Delimited Files (python csv library)
 * Microsoft Excel
 * Python Iterators
 * SQLAlchemy Constructions

Example::

    import datatransporttools
    from datatransporttools.mysql import MySQLTable
    from datatransporttools.csv_ import CSVFile

    src = MySQLTable.from_values(server='localhost', username='zakir', password='password', table='users')
    dst = CSVFile('users_dump.csv')
    datatransporttools.transfer(src, dst)
