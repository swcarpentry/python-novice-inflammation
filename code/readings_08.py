import sys
import numpy

def main():
    script = sys.argv[0]
    if len(sys.argv) == 1:  # no arguments, so print help message
        print('Usage: python readings_08.py action filenames\n'
              'action must be one of --min --mean --max\n'
              'if filenames is blank, input is taken from stdin;\n'
              'otherwise, each filename in the list of arguments\n'
              'is processed in turn')
        return

    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], (
        'Action is not one of --min, --mean, or --max: ' + action)
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for filename in filenames:
            process(filename, action)

def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=',')

    if action == '--min':
        values = numpy.min(data, axis=1)
    elif action == '--mean':
        values = numpy.mean(data, axis=1)
    elif action == '--max':
        values = numpy.max(data, axis=1)

    for val in values:
        print(val)

if __name__ == '__main__':
    main()
