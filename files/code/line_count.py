import sys


def main():
    """
    print each input filename and the number of lines in it,
    and print the sum of the number of lines
    """
    filenames = sys.argv[1:]
    sum_nlines = 0  # initialize counting variable

    if len(filenames) == 0:  # no filenames, just stdin
        sum_nlines = count_file_like(sys.stdin)
        print('stdin: %d' % sum_nlines)
    else:
        for filename in filenames:
            nlines = count_file(filename)
            print('%s %d' % (filename, nlines))
            sum_nlines += nlines
        print('total: %d' % sum_nlines)


def count_file(filename):
    """count the number of lines in a file"""
    f = open(filename, 'r')
    nlines = len(f.readlines())
    f.close()
    return(nlines)


def count_file_like(file_like):
    """count the number of lines in a file-like object (eg stdin)"""
    n = 0
    for line in file_like:
        n = n+1
    return n


if __name__ == '__main__':
    main()
