import cStringIO

data = 'first\nsecond\nthird\n'
reader = cStringIO.StringIO(data)
for line in reader:
    print line
