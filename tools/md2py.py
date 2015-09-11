#! /usr/bin/env python
"""
Check lessons for PEP8 compatibility using the `pep8` script. This is designed
to be run from the lesson root directory.
"""
import os
import shutil
import subprocess


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


def check_lesson(fname):
    """
    Convert a lesson and check it for PEP8 compliance. Does not work right now.
    """
    fname_py = fname.replace(".md", ".py")
    fpath_py = os.path.join("temp", fname_py)
    # Convert the lesson to Python
    md2py(fname, fname_py)
    # Run the pep8 script on the newly generated Python file
    results = subprocess.check_output(["pep8", fpath_py], shell=True,
                                      stderr=subprocess.STDOUT)
    print(results)


if __name__ == "__main__":
    # test_md2py(rm_temp=True)
    # check_lesson("01-numpy.md")
    pages = ["01-numpy.md", "02-loop.md", "03-lists.md", "04-files.md",
             "05-cond.md", "06-func.md", "07-errors.md", "08-defensive.md",
             "09-debugging.md", "10-cmdline.md"]
    for page in pages:
        fname_py = page.replace(".md", ".py")
        print("Converting {} to {}".format(page, fname_py))
        md2py(page, fname_py)
