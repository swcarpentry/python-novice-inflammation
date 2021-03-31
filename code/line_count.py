#!/usr/bin/env python
import sys


def main():
    """
    print each input filename and the number of lines in it,
    and print the sum of the number of lines
    """
    filenames = sys.argv[1:]
    sum_nlines = 0  # initialize counting variable

    if not len(filenames):  # no filenames, just stdin
        sum_nlines = count_file_like(sys.stdin)
        print(f'stdin: {sum_nlines}')
    else:
        for filename in filenames:
            nlines = count_file(filename)
            print(f'{filename} {nlines}')
            sum_nlines += nlines
        print(f'total: {sum_nlines}')

    return None


def count_file(filename):
    """count the number of lines in a file"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        nlines = len(input_file.readlines())
    return nlines


def count_file_like(file_like):
    """count the number of lines in a file-like object (eg stdin)"""
    n = 0
    for _ in file_like:
        n += 1
    return n


if __name__ == '__main__':
    main()
