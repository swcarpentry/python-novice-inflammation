---
layout: page
title: Programming with Python
subtitle: Instructor's Guide
---
## Legend

We are using a dataset with records on inflammation from patients following an
arthritis treatment.

We make reference in the lesson that this data is somehow strange. It is strange
because it is fabricated! The script used to generate the inflammation data
is included as [`tools/gen_inflammation.py`](tools/gen_inflammation.py).

## Overall

This lesson is written as an introduction to Python,
but its real purpose is to introduce the single most important idea in programming:
how to solve problems by building functions,
each of which can fit in a programmer's working memory.
In order to teach that,
we must teach people a little about
the mechanics of manipulating data with lists and file I/O
so that their functions can do things they actually care about.
Our teaching order tries to show practical uses of every idea as soon as it is introduced;
instructors should resist the temptation to explain
the "other 90%" of the language
as well.

The final example asks them to build a command-line tool
that works with the Unix pipe-and-filter model.
We do this because it is a useful skill
and because it helps learners see that the software they use isn't magical.
Tools like `grep` might be more sophisticated than
the programs our learners can write at this point in their careers,
but it's crucial they realize this is a difference of scale rather than kind.

Explain that we use Python because:

*   It's free.
*   It has a lot of scientific libraries, and more are constantly being added.
*   It has a large scientific user community.
*   It's easier for novices to learn than most of the mature alternatives.
    (Software Carpentry originally used Perl;
    when we switched,
    we found that we could cover as much material in two days in Python
    as we'd covered in three days in Perl,
    and that retention was higher.)

We do *not* include instructions on running the IPython Notebook in the tutorial
because we want to focus on the language rather than the tools.
Instructors should, however, walk learners through some basic operations:
*   Launch from the command line with `ipython notebook`.
*   Create a new notebook.
*   Enter code or data in a cell and execute it.
*   Explain the difference between `In[#]` and `Out[#]`.

Watching the instructor grow programs step by step
is as helpful to learners as anything to do with Python.
Resist the urge to update a single cell repeatedly
(which is what you'd probably do in real life).
Instead,
clone the previous cell and write the update in the new copy
so that learners have a complete record of how the program grew.
Once you've done this,
you can say,
"Now why don't we just breaks things into small functions right from the start?"

The discussion of command-line scripts
assumes that students understand standard I/O and building filters,
which are covered in the lesson on the shell.

## Frequently Argued Issues (FAI)

*   `import ... as ...` syntax.

    This syntax is commonly used in the scientific Python community;
    it is explicitly recommended in documentation to `import numpy as np`
    and `import matplotlib.pyplot as plt`. Despite that, we have decided
    not to introduce aliasing imports in this novice lesson due to the
    additional cognitive load it puts on students, despite the typing that
    it saves. A good summary of arguments for and against can be found in
    [PR #61](https://github.com/swcarpentry/python-novice-inflammation/pull/61).

    It is up to you as an individual instructor whether you want to introduce
    these aliases when you teach this lesson, but we encourage you to please
    read those arguments thoroughly before deciding one way or the other.

## [Analyzing Patient Data](01-numpy.html)

## [Repeating Actions with Loops](02-loop.html)

## [Storing Multiple Values in Lists](03-lists.html)

## [Analyzing Data from Multiple Files](04-files.html)

## [Making Choices](05-cond.html)

## [Creating Functions](06-func.html)

## [Errors and Exceptions](07-errors.html)

## [Defensive Programming](08-defensive.html)

## [Debugging](09-debugging.html)

## [Command-Line Programs](10-cmdline.html)

Solutions to exercises:

> ## Arithmetic on the command line {.challenge}
>
> Write a command-line program that does addition and subtraction:
>
> ~~~ {.python}
> $ python arith.py add 1 2
> ~~~
> ~~~ {.output}
> 3
> ~~~
> ~~~ {.python}
> $ python arith.py subtract 3 4
> ~~~
> ~~~ {.output}
> -1
> ~~~
>

> ~~~ {.output}
> # this is code/arith.py
>import sys
>
>def main():
>    assert len(sys.argv) == 4, 'Need exactly 3 arguments'
>
>    operator = sys.argv[1]
>    assert operator in ['add', 'subtract', 'multiply', 'divide'], \
>           'Operator is not one of add, subtract, multiply, or divide: bailing out' 
>    try:
>        operand1, operand2 = float(sys.argv[2]), float(sys.argv[3])
>    except ValueError:
>        print 'cannot convert input to a number: bailing out'
>        return
>        
>    do_arithmetic(operand1, operator, operand2)
>
>def do_arithmetic(operand1, operator, operand2):
>
>    if operator == 'add':
>        value = operand1 + operand2
>    elif operator == 'subtract':
>        value = operand1 - operand2
>    elif operator == 'multiply':
>        value = operand1 * operand2
>    elif operator == 'divide':
>        value = operand1 / operand2
>    print value
>
>main()
> ~~~

> ## Finding particular files {.challenge}
>
> Using the `glob` module introduced [earlier](04-files.html),
> write a simple version of `ls` that shows files in the current directory with a particular suffix.
> A call to this script should look like this:
>
> ~~~ {.python}
> $ python my_ls.py py
> ~~~
> ~~~ {.output}
> left.py
> right.py
> zero.py
> ~~~

> ~~~ {.output}
> # this is code/my_ls.py
>import sys
>import glob
>
>def main():
>    '''prints names of all files with sys.argv as suffix'''
>    assert len(sys.argv) >= 2, 'Argument list cannot be empty'
>    suffix = sys.argv[1] # NB: behaviour is not as you'd expect if sys.argv[1] is *
>    glob_input = '*.' + suffix # construct the input
>    glob_output = glob.glob(glob_input) # call the glob function
>    for item in glob_output: # print the output
>        print item
>    return
>
>main()
> ~~~


> ## Changing flags {.challenge}
>
> Rewrite `readings.py` so that it uses `-n`, `-m`, and `-x` instead of `--min`, `--mean`, and `--max` respectively.
> Is the code easier to read?
> Is the program easier to understand?

> ~~~ {.output}
> # this is code/readings-07.py
>import sys
>import numpy
>
>def main():
>    script = sys.argv[0]
>    action = sys.argv[1]
>    filenames = sys.argv[2:]
>    assert action in ['-n', '-m', '-x'], \
>           'Action is not one of -n, -m, or -x: ' + action
>    if len(filenames) == 0:
>        process(sys.stdin, action)
>    else:
>        for f in filenames:
>            process(f, action)
>
>def process(filename, action):
>    data = numpy.loadtxt(filename, delimiter=',')
>
>    if action == '-n':
>        values = data.min(axis=1)
>    elif action == '-m':
>        values = data.mean(axis=1)
>    elif action == '-x':
>        values = data.max(axis=1)
>
>    for m in values:
>        print m
>
>main()
> ~~~


> ## Adding a help message {.challenge}
>
> Separately,
> modify `readings.py` so that if no parameters are given
> (i.e., no action is specified and no filenames are given),
> it prints a message explaining how it should be used.

> ~~~ {.output}
> # this is code/readings-08.py
>import sys
>import numpy
>
>def main():
>    script = sys.argv[0]
>    if len(sys.argv) == 1: # no arguments, so print help message
>        print 'Usage: python readings-08.py action filenames\n \
>               action must be one of --min --mean --max\n \
>               if filenames is blank, input is taken from stdin;\n \
>               otherwise, each filename in the list of arguments is processed in turn'
>        return
>
>    action = sys.argv[1]
>    filenames = sys.argv[2:]
>    assert action in ['--min', '--mean', '--max'], \
>           'Action is not one of --min, --mean, or --max: ' + action
>    if len(filenames) == 0:
>        process(sys.stdin, action)
>    else:
>        for f in filenames:
>            process(f, action)
>
>def process(filename, action):
>    data = numpy.loadtxt(filename, delimiter=',')
>
>    if action == '--min':
>        values = data.min(axis=1)
>    elif action == '--mean':
>        values = data.mean(axis=1)
>    elif action == '--max':
>        values = data.max(axis=1)
>
>    for m in values:
>        print m
>
>main()
> ~~~

> ## Adding a default action {.challenge}
>
> Separately,
> modify `readings.py` so that if no action is given
> it displays the means of the data.

> ~~~ {.output}
># this is code/readings-09.py
>import sys
>import numpy
>
>def main():
>    script = sys.argv[0]
>    action = sys.argv[1]
>    if action not in ['--min', '--mean', '--max']: # if no action given
>        action = '--mean'    # set a default action, that being mean
>        filenames = sys.argv[1:] # start the filenames one place earlier in the argv list
>    else:
>        filenames = sys.argv[2:]
>
>    if len(filenames) == 0:
>        process(sys.stdin, action)
>    else:
>        for f in filenames:
>            process(f, action)
>
>def process(filename, action):
>    data = numpy.loadtxt(filename, delimiter=',')
>
>    if action == '--min':
>        values = data.min(axis=1)
>    elif action == '--mean':
>        values = data.mean(axis=1)
>    elif action == '--max':
>        values = data.max(axis=1)
>
>    for m in values:
>        print m
>
>main()
> ~~~

> ## A file-checker {.challenge}
>
> Write a program called `check.py` that takes the names of one or more inflammation data files as arguments
> and checks that all the files have the same number of rows and columns.
> What is the best way to test your program?

> ~~~ {.output}
> # this is code/check.py
>import sys
>import numpy 
>
>def main():
>    script = sys.argv[0]
>    filenames = sys.argv[1:]
>    if len(filenames) <=1: #nothing to check
>        print 'Only 1 file specified on input'
>    else:
>        nrow0, ncol0 = row_col_count(filenames[0])
>        print 'First file %s: %d rows and %d columns' % (filenames[0], nrow0, ncol0)
>        for f in filenames[1:]:
>            nrow, ncol = row_col_count(f)
>            if nrow != nrow0 or ncol != ncol0:
>                print 'File %s does not check: %d rows and %d columns' % (f, nrow, ncol)
>            else:
>                print 'File %s checks' % f
>        return
>
>def row_col_count(filename):
>    try:
>        nrow, ncol = numpy.loadtxt(filename, delimiter=',').shape
>    except ValueError: #get this if file doesn't have same number of rows and columns, or if it has non-numeric content
>        nrow, ncol = (0, 0)
>    return nrow, ncol
>
>main()
> ~~~

> ## Counting lines {.challenge}
>
> Write a program called `line-count.py` that works like the Unix `wc` command:
>
> *   If no filenames are given, it reports the number of lines in standard input.
> *   If one or more filenames are given, it reports the number of lines in each, followed by the total number of lines.
> ~~~ {.output}
> # this is code/line-count.py
>import sys
>
>def main():
>    '''print each input filename and the number of lines in it, 
>       and print the sum of the number of lines'''
>    filenames = sys.argv[1:]
>    sum_nlines = 0 #initialize counting variable
>
>    if len(filenames) == 0: # no filenames, just stdin
>        sum_nlines = count_file_like(sys.stdin)
>        print 'stdin: %d' % sum_nlines
>    else:
>        for f in filenames:
>            n = count_file(f)
>            print '%s %d' % (f, n)
>            sum_nlines += n
>        print 'total: %d' % sum_nlines
>
>def count_file(filename):
>    '''count the number of lines in a file'''
>    f = open(filename,'r')
>    nlines = len(f.readlines())
>    f.close()
>    return(nlines)
>
>def count_file_like(file_like):
>    '''count the number of lines in a file-like object (eg stdin)'''
>    n = 0
>    for line in file_like:
>        n = n+1
>    return n
>
>main()
>
> ~~~
