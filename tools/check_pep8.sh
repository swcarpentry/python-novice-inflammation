#!/usr/bin/env sh
# This script runs a PEP8 check on all lessons defined in md2py.py.
# It should be run from the project root directory.

# Convert all lessons to Python and store these in `./temp`
python tools/md2py.py

# Run PEP8 check, ignoring long lines (E501), trailing whitespace (W291),
# module level imports not at top of file (E402), and insufficient blank lines
# before function definitions (E302)
pep8 --ignore E501,W291,E402,E302 temp

# Remove temporary files
rm -rf temp
