import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['-n', '-m', '-x'], (
        'Action is not one of -n, -m, or -x: ' + action)
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for filename in filenames:
            process(filename, action)

def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=',')

    if action == '-n':
        values = numpy.min(data, axis=1)
    elif action == '-m':
        values = numpy.mean(data, axis=1)
    elif action == '-x':
        values = numpy.max(data, axis=1)

    for val in values:
        print(val)

if __name__ == '__main__':
    main()
