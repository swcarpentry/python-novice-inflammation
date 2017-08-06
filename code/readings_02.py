import sys
import numpy

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = numpy.genfromtxt(filename, delimiter=',')
    for m in data.mean(axis=1):
        print(m)

if __name__ == '__main__':
    main()
