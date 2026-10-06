import glob
import sys


def main():
    """prints names of all files with sys.argv as suffix"""
    assert len(sys.argv) >= 2, "Argument list cannot be empty"
    # NB: behaviour is not as you'd expect if sys.argv[1] is *
    suffix = sys.argv[1]
    glob_input = '*.' + suffix  # construct the input
    glob_output = glob.glob(glob_input)  # call the glob function
    for item in glob_output:  # print the output
        print(item)
    return


if __name__ == '__main__':
    main()
