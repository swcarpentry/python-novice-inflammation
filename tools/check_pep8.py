#! /usr/bin/env python
"""
Convert lesson pages to Python to check for PEP8 compatibility using the `pep8`
script. This is designed to be run from the lesson root directory.
"""
import os
import subprocess

def comment_line(line):
    """Comment a line."""
    return "# " + line


def md2py(fpath_md):
    """
    Convert Markdown file to Python, commenting everything except code blocks.
    Output file is in the same directory with `.md` replacing `.py`.
    """
    py_text = ""
    fpath_py = fpath_md.replace(".md", ".py")
    inblock = False
    with open(fpath_md) as f:
        for line in f:
            if line.strip()[:13] == "~~~ {.python}":
                py_text += comment_line(line)
                inblock = True
            elif line.strip() == "~~~":
                py_text += comment_line(line)
                inblock = False
            elif inblock:
                py_text += line
            else:
                py_text += comment_line(line)
    with open(fpath_py, "w") as f:
        f.write(py_text)


def test_md2py(rm=True):
    """Test the md2py function on known input."""
    fpath_md = "tools/test/test_md_to_py.md"
    fpath_py_ref = "tools/test/test_md_to_py_ref.py"
    fpath_py = "tools/test/test_md_to_py.py"
    md2py(fpath_md)
    with open(fpath_py_ref) as f:
        py_ref = f.read()
    with open(fpath_py) as f:
        py = f.read()
    if rm:
        os.remove(fpath_py)
    assert py == py_ref


def check_page(fpath, rm=True, ignore=["E501", "W291", "E402", "E302"]):
    """
    Convert a lesson page from Markdown to Python and check it for PEP8
    compliance.
    """
    fpath_py = fpath.replace(".md", ".py")
    # Convert the lesson to Python
    md2py(fpath)
    # Run the pep8 script on the newly generated Python file
    subprocess.call(["pep8", fpath_py, "--ignore", ",".join(ignore)])
    if rm:
        os.remove(fpath_py)


if __name__ == "__main__":
    # test_md2py(rm=True)
    pages = ["01-numpy.md", "02-loop.md", "03-lists.md", "04-files.md",
             "05-cond.md", "06-func.md", "07-errors.md", "08-defensive.md",
             "09-debugging.md", "10-cmdline.md"]
    for page in pages:
        check_page(page, rm=True)
