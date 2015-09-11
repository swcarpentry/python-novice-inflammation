#! /usr/bin/env python
"""
Check lessons for PEP8 compatibility using the `pep8` script. This is designed
to be run from the lesson root directory.
"""
import os
import shutil

def comment_line(line):
    """Comment a line."""
    return "# " + line

def md2py(fpath_md, fname_out=None):
    """
    Convert Markdown file to Python, commenting everything except code blocks.
    Returns text unless an ouput file name is provided.
    """
    py_text = ""
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
    if fname_out is None:
        return py_text
    else:
        if not os.path.isdir("temp"):
            os.mkdir("temp")
        with open(os.path.join("temp", fname_out), "w") as f:
            f.write(py_text)

def test_md2py(rm_temp=True):
    """Test the md2py function on known input."""
    fpath_md = "tools/test/test_md_to_py.md"
    fpath_py_ref = "tools/test/test_md_to_py.py"
    fname_py = "test.py"
    md2py(fpath_md, fname_py)
    with open(fpath_py_ref) as f:
        py_ref = f.read()
    with open(os.path.join("temp", fname_py)) as f:
        py = f.read()
    if rm_temp:
        shutil.rmtree("./temp")
    assert py == py_ref

if __name__ == "__main__":
    test_md2py(rm_temp=True)
