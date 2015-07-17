from __future__ import print_function

import sys

count = 0
for line in sys.stdin:
    count += 1

print(count, 'lines in standard input')
