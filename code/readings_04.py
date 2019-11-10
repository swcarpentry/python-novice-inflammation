import sys
import numpy


def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for filename in filenames:
        data = numpy.loadtxt(filename, delimiter=',')

        if action == '--min':
            values = data.min(axis=1)
        elif action == '--mean':
            values = data.mean(axis=1)
        elif action == '--max':
            values = data.max(axis=1)

        for val in values:
            print(val)


if __name__ == '__main__':
    main()
