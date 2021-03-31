#!/usr/bin/env python
import sys
import numpy


def main():
    if len(sys.argv) == 1:  # no arguments, so print help message
        print(f'''Usage: python {sys.argv[0]} action filenames
              action must be one of --min --mean --max
              if filenames is blank, input is taken from stdin;
              otherwise, each filename in the list of arguments
              is processed in turn''')
        return None

    action = sys.argv[1]
    filenames = sys.argv[2:]

    action_list = ['--min', '--mean', '--max']
    assert action in action_list, f'''Action is not one
    of {''.join(f'{act}, ' for act in action_list)[:-2]}: {action}'''

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
