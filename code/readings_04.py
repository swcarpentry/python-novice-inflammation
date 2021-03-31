#!/usr/bin/env python
import sys
import numpy


def main():
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for filename in filenames:
        data = numpy.loadtxt(filename)

        if action == '--min':
            values = numpy.min(data, axis=1)
        elif action == '--mean':
            values = numpy.mean(data, axis=1)
        elif action == '--max':
            values = numpy.max(data, axis=1)
        else:
            values = None

        if values is None:
            print('Incorrect flag has been provided, no data is printed.')
        else:
            for val in values:
                print(val)
    return None


if __name__ == '__main__':
    main()
