#!/usr/bin/env python
import sys
import numpy


def main():
    for filename in sys.argv[1:]:
        data = numpy.loadtxt(filename)
        for row_mean in numpy.mean(data, axis=1):
            print(row_mean)
    return None


if __name__ == '__main__':
    main()
