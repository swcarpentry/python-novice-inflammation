#!/usr/bin/env python
import sys

count = 0
for line in sys.stdin:
    count += 1

print(f'{count} lines in standard input')
