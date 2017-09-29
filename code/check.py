import sys
import numpy


def main():
    script = sys.argv[0]
    filenames = sys.argv[1:]
    if len(filenames) <= 1:  # nothing to check
        print('Only 1 file specified on input')
    else:
        nrow0, ncol0 = row_col_count(filenames[0])
        print('First file %s: %d rows and %d columns' % (
            filenames[0], nrow0, ncol0))
        for f in filenames[1:]:
            nrow, ncol = row_col_count(f)
            if nrow != nrow0 or ncol != ncol0:
                print('File %s does not check: %d rows and %d columns'
                      % (f, nrow, ncol))
            else:
                print('File %s checks' % f)
        return


def row_col_count(filename):
    try:
        nrow, ncol = numpy.loadtxt(filename, delimiter=',').shape
    except ValueError:
        # This occurs if the file doesn't have same number of rows and columns,
        # or if it has non-numeric content
        nrow, ncol = (0, 0)
    return nrow, ncol


if __name__ == '__main__':
    main()
