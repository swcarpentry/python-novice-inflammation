#!/usr/bin/env python

"""
Generate pseudo-random patient inflammation data for use in Python lessons.
"""

import random

random.seed(1)

n_patients = 60
n_days = 40
n_range = 20

middle = n_days / 2

for p in range(n_patients):
    upper_vals = [max(n_range - abs(d - middle), 0) for d in range(n_days)]
    vals = [random.randint(int(upper / 4), int(upper)) for upper in upper_vals]

    print(f'''{''.join(f'{value},' for value in vals)}'''[:-1])
