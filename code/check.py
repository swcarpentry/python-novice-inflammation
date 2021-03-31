#!/usr/bin/env python
import sys
import numpy


def main():
    filenames = sys.argv[1:]
    total_files = len(filenames)
    if total_files <= 1:  # nothing to check
        print(f'''{'Only one file' if total_files else 'None files'} specified
        on input''')
    else:
        nrow0, ncol0 = row_col_count(filenames[0])
        print(f'''First file {filenames[0]}: {nrow0} rows and {ncol0}
        columns''')
        for filename in filenames[1:]:
            nrow, ncol = row_col_count(filename)
            if nrow != nrow0 or ncol != ncol0:
                print(f'''File {filename} does not check: {nrow} rows
                and {ncol} columns''')
            else:
                print(f'File {filename} checks')

    return None


def row_col_count(filename):
    try:
        nrow, ncol = numpy.loadtxt(filename).shape
    except ValueError as val:
        # This occurs if the file does contain rows
        # with inconsistent number of elements or if it has non-numeric content
        print(val)
        nrow, ncol = (0, 0)
    return nrow, ncol


if __name__ == '__main__':
    main()
