import sys

def transfer(inputobj, outputobj, include_headers=False):
    inputobj.prep_read()
    outputobj.prep_write()
    if include_headers:
        print 'dump headers...',
        outputobj.put_record(inputobj.get_headers())
        print 'ok'
    print 'start transfer',
    for record in inputobj.get_record():
        sys.stdout.write('.')
        outputobj.put_record(record)
    print ' ok'
    inputobj.close()
    outputobj.close()
