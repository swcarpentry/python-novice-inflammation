import sys
import numpy


def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = numpy.loadtxt(filename, delimiter=',')
    for row_mean in numpy.mean(data, axis=1):
        print(row_mean)
