import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    if action not in ['--min', '--mean', '--max']:  # if no action given
        action = '--mean'  # set a default action, that being mean
        # start the filenames one place earlier in the argv list
        filenames = sys.argv[1:]
    else:
        filenames = sys.argv[2:]

    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for filename in filenames:
            process(filename, action)

def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=',')

    if action == '--min':
        values = numpy.amin(data, axis=1)
    elif action == '--mean':
        values = numpy.mean(data, axis=1)
    elif action == '--max':
        values = numpy.amax(data, axis=1)

    for val in values:
        print(val)

if __name__ == '__main__':
    main()
