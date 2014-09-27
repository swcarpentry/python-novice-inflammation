---
layout: lesson
root: ../..
---

## Command-Line Programs


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

1. If no filename is given on the command line, read data from [standard input](../../gloss.html#standard-input).
2. If one or more filenames are given, read data from them and report statistics for each file separately.
3. Use the `--min`, `--mean`, or `--max` flag to determine what statistic to print.

To make this work,
we need to know how to handle command-line arguments in a program,
and how to get at standard input.
We'll tackle these questions in turn below.


<div class="objectives" markdown="1">
#### Objectives

*   Use the values of command-line arguments in a program.
*   Handle flags and files separately in a command-line program.
*   Read data from standard input in a program so that it can be used in a pipeline.
</div>

### Command-Line Arguments


Using the text editor of your choice,
save the following in a text file:


<pre class="in"><code>!cat sys-version.py</code></pre>

<div class="out"><pre class='out'><code>import sys
print &#39;version is&#39;, sys.version
</code></pre></div>


The first line imports a library called `sys`,
which is short for "system".
It defines values such as `sys.version`,
which describes which version of Python we are running.
We can run this script from within the IPython Notebook like this:


<pre class="in"><code>%run sys-version.py</code></pre>

<div class="out"><pre class='out'><code>version is 2.7.5 |Anaconda 1.8.0 (x86_64)| (default, Oct 24 2013, 07:02:20) 
[GCC 4.0.1 (Apple Inc. build 5493)]
</code></pre></div>


or like this:


<pre class="in"><code>!ipython sys-version.py</code></pre>

<div class="out"><pre class='out'><code>version is 2.7.5 |Anaconda 1.8.0 (x86_64)| (default, Oct 24 2013, 07:02:20) 
[GCC 4.0.1 (Apple Inc. build 5493)]
</code></pre></div>


The first method, `%run`,
uses a special command in the IPython Notebook to run a program in a `.py` file.
The second method is more general:
the exclamation mark `!` tells the Notebook to run a shell command,
and it just so happens that the command we run is `ipython` with the name of the script.


Here's another script that does something more interesting:


<pre class="in"><code>!cat argv-list.py</code></pre>

<div class="out"><pre class='out'><code>import sys
print &#39;sys.argv is&#39;, sys.argv
</code></pre></div>


The strange name `argv` stands for "argument values".
Whenever Python runs a program,
it takes all of the values given on the command line
and puts them in the list `sys.argv`
so that the program can determine what they were.
If we run this program with no arguments:


<pre class="in"><code>!ipython argv-list.py</code></pre>

<div class="out"><pre class='out'><code>sys.argv is [&#39;/Users/gwilson/s/bc/python/novice/argv-list.py&#39;]
</code></pre></div>


the only thing in the list is the full path to our script,
which is always `sys.argv[0]`.
If we run it with a few arguments, however:


<pre class="in"><code>!ipython argv-list.py first second third</code></pre>

<div class="out"><pre class='out'><code>sys.argv is [&#39;/Users/gwilson/s/bc/python/novice/argv-list.py&#39;, &#39;first&#39;, &#39;second&#39;, &#39;third&#39;]
</code></pre></div>


then Python adds each of those arguments to that magic list.


With this in hand,
let's build a version of `readings.py` that always prints the per-patient mean of a single data file.
The first step is to write a function that outlines our implementation,
and a placeholder for the function that does the actual work.
By convention this function is usually called `main`,
though we can call it whatever we want:


<pre class="in"><code>!cat readings-01.py</code></pre>

<div class="out"><pre class='out'><code>import sys
import numpy as np

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = np.loadtxt(filename, delimiter=&#39;,&#39;)
    for m in data.mean(axis=1):
        print m
</code></pre></div>


This function gets the name of the script from `sys.argv[0]`,
because that's where it's always put,
and the name of the file to process from `sys.argv[1]`.
Here's a simple test:


<pre class="in"><code>%run readings-01.py inflammation-01.csv</code></pre>


There is no output because we have defined a function,
but haven't actually called it.
Let's add a call to `main`:


<pre class="in"><code>!cat readings-02.py</code></pre>

<div class="out"><pre class='out'><code>import sys
import numpy as np

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = np.loadtxt(filename, delimiter=&#39;,&#39;)
    for m in data.mean(axis=1):
        print m

main()
</code></pre></div>


and run that:


<pre class="in"><code>%run readings-02.py inflammation-01.csv</code></pre>

<div class="out"><pre class='out'><code>5.45
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
</code></pre></div>


> #### The Right Way to Do It
>
> If our programs can take complex parameters or multiple filenames,
> we shouldn't handle `sys.argv` directly.
> Instead,
> we should use Python's `argparse` library,
> which handles common cases in a systematic way,
> and also makes it easy for us to provide sensible error messages for our users.


<div class="challenges" markdown="1">
#### Challenges

1.  Write a command-line program that does addition and subtraction:

    ~~~
    $ python arith.py 1 + 2
    3
    $ python arith.py 3 - 4
    -1
    ~~~

    What goes wrong if you try to add multiplication using '*' to the program?

2.  Using the `glob` module introduced [03-loop.ipynb](earlier),
    write a simple version of `ls` that shows files in the current directory with a particular suffix:
    
    ~~~
    $ python my_ls.py py
    left.py
    right.py
    zero.py
    ~~~
</div>

### Handling Multiple Files


The next step is to teach our program how to handle multiple files.
Since 60 lines of output per file is a lot to page through,
we'll start by creating three smaller files,
each of which has three days of data for two patients:


<pre class="in"><code>!ls small-*.csv</code></pre>

<div class="out"><pre class='out'><code>small-01.csv small-02.csv small-03.csv
</code></pre></div>


<pre class="in"><code>!cat small-01.csv</code></pre>

<div class="out"><pre class='out'><code>0,0,1
0,1,2
</code></pre></div>


<pre class="in"><code>%run readings-02.py small-01.csv</code></pre>

<div class="out"><pre class='out'><code>0.333333333333
1.0
</code></pre></div>


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
Here's our changed program:


<pre class="in"><code>!cat readings-03.py</code></pre>

<div class="out"><pre class='out'><code>import sys
import numpy as np

def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        data = np.loadtxt(filename, delimiter=&#39;,&#39;)
        for m in data.mean(axis=1):
            print m

main()
</code></pre></div>


and here it is in action:


<pre class="in"><code>%run readings-03.py small-01.csv small-02.csv</code></pre>

<div class="out"><pre class='out'><code>0.333333333333
1.0
13.6666666667
11.0
</code></pre></div>


Note:
at this point,
we have created three versions of our script called `readings-01.py`,
`readings-02.py`, and `readings-03.py`.
We wouldn't do this in real life:
instead,
we would have one file called `readings.py` that we committed to version control
every time we got an enhancement working.
For teaching,
though,
we need all the successive versions side by side.


<div class="challenges" markdown="1">
#### Challenges

1.  Write a program called `check.py` that takes the names of one or more inflammation data files as arguments
    and checks that all the files have the same number of rows and columns.
    What is the best way to test your program?
</div>

### Handling Command-Line Flags


The next step is to teach our program to pay attention to the `--min`, `--mean`, and `--max` flags.
These always appear before the names of the files,
so we could just do this:


<pre class="in"><code>!cat readings-04.py</code></pre>

<div class="out"><pre class='out'><code>import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for f in filenames:
        data = np.loadtxt(f, delimiter=&#39;,&#39;)

        if action == &#39;--min&#39;:
            values = data.min(axis=1)
        elif action == &#39;--mean&#39;:
            values = data.mean(axis=1)
        elif action == &#39;--max&#39;:
            values = data.max(axis=1)

        for m in values:
            print m

main()
</code></pre></div>


This works:


<pre class="in"><code>%run readings-04.py --max small-01.csv</code></pre>

<div class="out"><pre class='out'><code>1.0
2.0
</code></pre></div>


but there are seveal things wrong with it:

1.  `main` is too large to read comfortably.

2.  If `action` isn't one of the three recognized flags,
    the program loads each file but does nothing with it
    (because none of the branches in the conditional match).
    [Silent failures](../../gloss.html#silent-failure) like this
    are always hard to debug.

This version pulls the processing of each file out of the loop into a function of its own.
It also checks that `action` is one of the allowed flags
before doing any processing,
so that the program fails fast:


<pre class="in"><code>!cat readings-05.py</code></pre>

<div class="out"><pre class='out'><code>import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in [&#39;--min&#39;, &#39;--mean&#39;, &#39;--max&#39;], \
           &#39;Action is not one of --min, --mean, or --max: &#39; + action
    for f in filenames:
        process(f, action)

def process(filename, action):
    data = np.loadtxt(filename, delimiter=&#39;,&#39;)

    if action == &#39;--min&#39;:
        values = data.min(axis=1)
    elif action == &#39;--mean&#39;:
        values = data.mean(axis=1)
    elif action == &#39;--max&#39;:
        values = data.max(axis=1)

    for m in values:
        print m

main()
</code></pre></div>


This is four lines longer than its predecessor,
but broken into more digestible chunks of 8 and 12 lines.


Python has a module named [argparse](http://docs.python.org/dev/library/argparse.html)
that helps handle complex command-line flags. We will not cover this module in this lesson
but you can go to Tshepang Lekhonkhobe's [Argparse tutorial](http://docs.python.org/dev/howto/argparse.html)
that is part of Python's Official Documentation.


<div class="challenges" markdown="1">
#### Challenges

1.  Rewrite this program so that it uses `-n`, `-m`, and `-x` instead of `--min`, `--mean`, and `--max` respectively.
    Is the code easier to read?
    Is the program easier to understand?

2.  Separately,
    modify the program so that if no parameters are given
    (i.e., no action is specified and no filenames are given),
    it prints a message explaining how it should be used.

3.  Separately,
    modify the program so that if no action is given
    it displays the means of the data.
</div>

### Handling Standard Input


The next thing our program has to do is read data from standard input if no filenames are given
so that we can put it in a pipeline,
redirect input to it,
and so on.
Let's experiment in another script:


<pre class="in"><code>!cat count-stdin.py</code></pre>

<div class="out"><pre class='out'><code>import sys

count = 0
for line in sys.stdin:
    count += 1

print count, &#39;lines in standard input&#39;
</code></pre></div>


This little program reads lines from a special "file" called `sys.stdin`,
which is automatically connected to the program's standard input.
We don't have to open it&mdash;Python and the operating system
take care of that when the program starts up&mdash;
but we can do almost anything with it that we could do to a regular file.
Let's try running it as if it were a regular command-line program:


<pre class="in"><code>!ipython count-stdin.py &lt; small-01.csv</code></pre>

<div class="out"><pre class='out'><code>2 lines in standard input
</code></pre></div>


What if we run it using `%run`?


<pre class="in"><code>%run count-stdin.py &lt; small-01.csv</code></pre>

<div class="out"><pre class='out'><code>0 lines in standard input
</code></pre></div>


As you can see,
`%run` doesn't understand file redirection:
that's a shell thing.

A common mistake is to try to run something that reads from standard input like this:

~~~
!ipython count_stdin.py small-01.csv
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


~~~
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


Let's try it out
(we'll see in a moment why we send the output through `head`):


<pre class="in"><code>!ipython readings-06.py --mean &lt; small-01.csv | head -10</code></pre>

<div class="out"><pre class='out'><code>[TerminalIPythonApp] CRITICAL | Bad config encountered during initialization:
[TerminalIPythonApp] CRITICAL | Unrecognized flag: &#39;--mean&#39;
=========
 IPython
=========

Tools for Interactive Computing in Python
=========================================

    A Python shell with automatic history (input and output), dynamic object
    introspection, easier configuration, command completion, access to the
    system shell and more.  IPython can also be embedded in running programs.
</code></pre></div>


Whoops:
why are we getting IPython's help rather than the line-by-line average of our data?
The answer is that IPython has a hard time telling
which command-line arguments are meant for it,
and which are meant for the program it's running.
To make our meaning clear,
we have to use `--` (a double dash)
to separate the two:


<pre class="in"><code>!ipython readings-06.py -- --mean &lt; small-01.csv</code></pre>

<div class="out"><pre class='out'><code>0.333333333333
1.0
</code></pre></div>


That's better.
In fact,
that's done:
the program now does everything we set out to do.


<div class="challenges" markdown="1">
#### Challenges

1.  Write a program called `line-count.py` that works like the Unix `wc` command:
    *   If no filenames are given, it reports the number of lines in standard input.
    *   If one or more filenames are given, it reports the number of lines in each, followed by the total number of lines.
</div>


<div class="keypoints" markdown="1">
#### Key Points

*   The `sys` library connects a Python program to the system it is running on.
*   The list `sys.argv` contains the command-line arguments that a program was run with.
*   Avoid silent failures.
*   The "file" `sys.stdin` connects to a program's standard input.
*   The "file" `sys.stdout` connects to a program's standard output.
</div>
