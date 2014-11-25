#!/usr/bin/env python

'''Generate pseudo-random patient inflammation data for use in Python lessons.'''

import sys
import random

n_patients = 60
n_days = 40
n_range = 20

middle = n_days / 2

for p in range(n_patients):
    vals = []
    for d in range(n_days):
        upper = max(n_range - abs(d - middle), 0)
        vals.append(random.randint(upper/4, upper))
    print ','.join([str(v) for v in vals])
