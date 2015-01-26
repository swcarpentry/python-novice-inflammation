---
layout: page
title: Programming with Python
subtitle: Command-Line Programs
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Use the values of command-line arguments in a program.
> *   Handle flags and files separately in a command-line program.
> *   Read data from standard input in a program so that it can be used in a pipeline.

The IPython Notebook and other interactive tools are great for prototyping code and exploring data,
but sooner or later we will want to use our program in a pipeline
or run it in a shell script to process thousands of data files.
In order to do that,
we need to make our programs work like other Unix command-line tools.
For example,
we may want a program that reads a data set
and prints the average inflammation per patient:

~~~
$ python readings.py --mean inflammation-01.csv
5.45
5.425
6.1
...
6.4
7.05
5.9
~~~

but we might also want to look at the minimum of the first four lines

~~~
$ head -4 inflammation-01.csv | python readings.py --min
~~~

or the maximum inflammations in several files one after another:

~~~
$ python readings.py --max inflammation-*.csv
~~~

Our overall requirements are:

1. If no filename is given on the command line, read data from **standard input**.
2. If one or more filenames are given, read data from them and report statistics for each file separately.
3. Use the `--min`, `--mean`, or `--max` flag to determine what statistic to print.

To make this work,
we need to know how to handle command-line arguments in a program,
and how to get at standard input.
We'll tackle these questions in turn below.

### Command-Line Arguments

Using the text editor of your choice,
save the following in a text file called `sys-version.py`:

~~~ {.python}
import sys
print 'version is', sys.version
~~~

The first line imports a library called `sys`,
which is short for "system".
It defines values such as `sys.version`,
which describes which version of Python we are running.
We can run this script from within the IPython Notebook like this:

<pre class="in"><code>%run sys-version.py</code></pre>

~~~ {.output}
version is 2.7.5 |Anaconda 1.8.0 (x86_64)| (default, Oct 24 2013, 07:02:20) 
[GCC 4.0.1 (Apple Inc. build 5493)]
~~~

or like this:

<pre class="in"><code>!ipython sys-version.py</code></pre>

~~~ {.output}
version is 2.7.5 |Anaconda 1.8.0 (x86_64)| (default, Oct 24 2013, 07:02:20) 
[GCC 4.0.1 (Apple Inc. build 5493)]
~~~

The first method, `%run`,
uses a special command in the IPython Notebook to run a program in a `.py` file.
The second method is more general:
the exclamation mark `!` tells the Notebook to run a shell command,
and it just so happens that the command we run is `ipython` with the name of the script.

Here's another script called `argv-list.py` that does something more interesting:

~~~ {.python}
import sys
print 'sys.argv is', sys.argv
~~~

The strange name `argv` stands for "argument values".
Whenever Python runs a program,
it takes all of the values given on the command line
and puts them in the list `sys.argv`
so that the program can determine what they were.
If we run this program with no arguments:

<pre class="in"><code>!ipython argv-list.py</code></pre>

~~~ {.output}
sys.argv is ['/Users/gwilson/s/bc/python/novice/argv-list.py']
~~~

the only thing in the list is the full path to our script,
which is always `sys.argv[0]`.
If we run it with a few arguments, however:

~~~ {.input}
$ argv-list.py first second third
~~~
~~~ {.output}
sys.argv is ['/Users/gwilson/s/bc/python/novice/argv-list.py', 'first', 'second', 'third']
~~~

then Python adds each of those arguments to that magic list.

With this in hand,
let's build a version of `readings.py` that always prints the per-patient mean of a single data file.
The first step is to write a function that outlines our implementation,
and a placeholder for the function that does the actual work.
By convention this function is usually called `main`,
though we can call it whatever we want:

<pre class="in"><code>!cat readings-01.py</code></pre>

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = np.loadtxt(filename, delimiter=',')
    for m in data.mean(axis=1):
        print m
~~~

This function gets the name of the script from `sys.argv[0]`,
because that's where it's always put,
and the name of the file to process from `sys.argv[1]`.
Here's a simple test:

<pre class="in"><code>%run readings-01.py inflammation-01.csv</code></pre>

There is no output because we have defined a function,
but haven't actually called it.
Let's add a call to `main`:

<pre class="in"><code>!cat readings-02.py</code></pre>

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = np.loadtxt(filename, delimiter=',')
    for m in data.mean(axis=1):
        print m

main()
~~~

and run that:

<pre class="in"><code>%run readings-02.py inflammation-01.csv</code></pre>

~~~ {.output}
5.45
5.425
6.1
5.9
5.55
6.225
5.975
6.65
6.625
6.525
6.775
5.8
6.225
5.75
5.225
6.3
6.55
5.7
5.85
6.55
5.775
5.825
6.175
6.1
5.8
6.425
6.05
6.025
6.175
6.55
6.175
6.35
6.725
6.125
7.075
5.725
5.925
6.15
6.075
5.75
5.975
5.725
6.3
5.9
6.75
5.925
7.225
6.15
5.95
6.275
5.7
6.1
6.825
5.975
6.725
5.7
6.25
6.4
7.05
5.9
~~~

> ## The Right Way to Do It {.callout}
>
> If our programs can take complex parameters or multiple filenames,
> we shouldn't handle `sys.argv` directly.
> Instead,
> we should use Python's `argparse` library,
> which handles common cases in a systematic way,
> and also makes it easy for us to provide sensible error messages for our users.

## Handling Multiple Files

The next step is to teach our program how to handle multiple files.
Since 60 lines of output per file is a lot to page through,
we'll start by creating three smaller files,
each of which has three days of data for two patients:

~~~ {.input}
$ ls small-*.csv
~~~
~~~ {.output}
small-01.csv small-02.csv small-03.csv
~~~

~~~ {.input}
$ cat small-01.csv
~~~
~~~ {.output}
0,0,1
0,1,2
~~~

~~~ {.input}
$ python readings-02.py small-01.csv
~~~
~~~ {.output}
0.333333333333
1.0
~~~

Using small data files as input also allows us to check our results more easily:
here,
for example,
we can see that our program is calculating the mean correctly for each line,
whereas we were really taking it on faith before.
This is yet another rule of programming:
"[test the simple things first](../../rules.html#test-simple-first)".

We want our program to process each file separately,
so we need a loop that executes once for each filename.
If we specify the files on the command line,
the filenames will be in `sys.argv`,
but we need to be careful:
`sys.argv[0]` will always be the name of our script,
rather than the name of a file.
We also need to handle an unknown number of filenames,
since our program could be run for any number of files.

The solution to both problems is to loop over the contents of `sys.argv[1:]`.
The '1' tells Python to start the slice at location 1,
so the program's name isn't included;
since we've left off the upper bound,
the slice runs to the end of the list,
and includes all the filenames.
Here's our changed program
`readings-03.py`:

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        data = np.loadtxt(filename, delimiter=',')
        for m in data.mean(axis=1):
            print m

main()
~~~

and here it is in action:

~~~ {.input}
$ python readings-03.py small-01.csv small-02.csv
~~~
~~~ {.output}
0.333333333333
1.0
13.6666666667
11.0
~~~

> ## The Right Way to Do It {.callout}
>
> At this point,
> we have created three versions of our script called `readings-01.py`,
> `readings-02.py`, and `readings-03.py`.
> We wouldn't do this in real life:
> instead,
> we would have one file called `readings.py` that we committed to version control
> every time we got an enhancement working.
> For teaching,
> though,
> we need all the successive versions side by side.

## Handling Command-Line Flags

The next step is to teach our program to pay attention to the `--min`, `--mean`, and `--max` flags.
These always appear before the names of the files,
so we could just do this:

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for f in filenames:
        data = np.loadtxt(f, delimiter=',')

        if action == '--min':
            values = data.min(axis=1)
        elif action == '--mean':
            values = data.mean(axis=1)
        elif action == '--max':
            values = data.max(axis=1)

        for m in values:
            print m

main()
~~~

This works:

~~~ {.input}
$ python readings-04.py --max small-01.csv
~~~
~~~ {.output}
1.0
2.0
~~~

but there are several things wrong with it:

1.  `main` is too large to read comfortably.

2.  If `action` isn't one of the three recognized flags,
    the program loads each file but does nothing with it
    (because none of the branches in the conditional match).
    **Silent failures** like this
    are always hard to debug.

This version pulls the processing of each file out of the loop into a function of its own.
It also checks that `action` is one of the allowed flags
before doing any processing,
so that the program fails fast:

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    for f in filenames:
        process(f, action)

def process(filename, action):
    data = np.loadtxt(filename, delimiter=',')

    if action == '--min':
        values = data.min(axis=1)
    elif action == '--mean':
        values = data.mean(axis=1)
    elif action == '--max':
        values = data.max(axis=1)

    for m in values:
        print m

main()
~~~

This is four lines longer than its predecessor,
but broken into more digestible chunks of 8 and 12 lines.

Python has a module named [argparse](http://docs.python.org/dev/library/argparse.html)
that helps handle complex command-line flags. We will not cover this module in this lesson
but you can go to Tshepang Lekhonkhobe's [Argparse tutorial](http://docs.python.org/dev/howto/argparse.html)
that is part of Python's Official Documentation.

## Handling Standard Input

The next thing our program has to do is read data from standard input if no filenames are given
so that we can put it in a pipeline,
redirect input to it,
and so on.
Let's experiment in another script called `count-stdin.py`:

~~~ {.python}
import sys

count = 0
for line in sys.stdin:
    count += 1

print count, 'lines in standard input'
~~~

This little program reads lines from a special "file" called `sys.stdin`,
which is automatically connected to the program's standard input.
We don't have to open it --- Python and the operating system
take care of that when the program starts up --- 
but we can do almost anything with it that we could do to a regular file.
Let's try running it as if it were a regular command-line program:

~~~ {.input}
$ python count-stdin.py < small-01.csv
~~~
~~~ {.output}
2 lines in standard input
~~~

A common mistake is to try to run something that reads from standard input like this:

~~~ {.input}
$ count_stdin.py small-01.csv
~~~

i.e., to forget the `<` character that redirect the file to standard input.
In this case,
there's nothing in standard input,
so the program waits at the start of the loop for someone to type something on the keyboard.
Since there's no way for us to do this,
our program is stuck,
and we have to halt it using the `Interrupt` option from the `Kernel` menu in the Notebook.

We now need to rewrite the program so that it loads data from `sys.stdin` if no filenames are provided.
Luckily,
`numpy.loadtxt` can handle either a filename or an open file as its first parameter,
so we don't actually need to change `process`.
That leaves `main`:

~~~ {.python}
def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for f in filenames:
            process(f, action)
~~~

Let's try it out:

~~~ {.python}
0.333333333333
1.0
~~~

That's better.
In fact,
that's done:
the program now does everything we set out to do.

> ## FIXME {.challenge}
> 
> Write a command-line program that does addition and subtraction:
> 
> ~~~ {.python}
> $ python arith.py 1 + 2
> ~~~
> ~~~ {.output}
> 3
> ~~~
> $ python arith.py 3 - 4
> ~~~
> ~~~ {.output}
> -1
> ~~~
> 
> What goes wrong if you try to add multiplication using '*' to the program?

> ## FIXME {.challenge}
>
> Using the `glob` module introduced [03-loop.ipynb](earlier),
> write a simple version of `ls` that shows files in the current directory with a particular suffix:
>     
> ~~~ {.python}
> $ python my_ls.py py
> ~~~
> ~~~ {.output}
> left.py
> right.py
> zero.py
> ~~~

> ## FIXME {.challenge}
> 
> Rewrite this program so that it uses `-n`, `-m`, and `-x` instead of `--min`, `--mean`, and `--max` respectively.
> Is the code easier to read?
> Is the program easier to understand?

> ## FIXME {.challenge}
> 
> Separately,
> modify the program so that if no parameters are given
> (i.e., no action is specified and no filenames are given),
> it prints a message explaining how it should be used.

> ## FIXME {.challenge}
> 
> Separately,
> modify the program so that if no action is given
> it displays the means of the data.

> ## FIXME {.challenge}
> 
> Write a program called `check.py` that takes the names of one or more inflammation data files as arguments
> and checks that all the files have the same number of rows and columns.
> What is the best way to test your program?

> ## FIXME {.challenge}
> 
> Write a program called `line-count.py` that works like the Unix `wc` command:
> 
> *   If no filenames are given, it reports the number of lines in standard input.
> *   If one or more filenames are given, it reports the number of lines in each, followed by the total number of lines.
