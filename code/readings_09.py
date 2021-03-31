#!/usr/bin/env python
import sys
import numpy


def main():
    action = sys.argv[1]
    if action not in ['--min', '--mean', '--max']:  # if no action given
        action = '--mean'  # set a default action, that being mean
        # start the filenames one place earlier in the argv list
        print(f'No action has been provided, using default flag {action}.')
        filenames = sys.argv[1:]
    else:
        filenames = sys.argv[2:]

    if not len(filenames):
        process(sys.stdin, action)
    else:
        for filename in filenames:
            process(filename, action)
    return None


def process(filename, action):
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
