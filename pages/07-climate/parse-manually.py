input_data = '1901,12.3\n1902,45.6\n1903,78.9\n'
print 'input data is:'
print input_data

as_lines = input_data.split('\n')
print 'as lines:'
print as_lines

for line in as_lines:
    fields = line.split(',')
    year = int(fields[0])
    value = float(fields[1])
    print year, ':', value
