import sys
import numpy


def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for filename in filenames:
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
