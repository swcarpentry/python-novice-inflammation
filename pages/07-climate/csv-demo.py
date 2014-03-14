import cStringIO
import csv

data = 'first\nsecond\nthird\n'
reader = cStringIO.StringIO(data)
wrapper = csv.reader(reader)
for record in wrapper:
    print record
