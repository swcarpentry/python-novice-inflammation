---
layout: lesson
root: ../..
---

## Command-Line Programs


<div class="">
<p>The IPython Notebook and other interactive tools are great for prototyping code and exploring data, but sooner or later we will want to use our program in a pipeline or run it in a shell script to process thousands of data files. In order to do that, we need to make our programs work like other Unix command-line tools. For example, we may want a program that reads a data set and prints the average inflammation per patient:</p>
<pre><code>$ python readings.py --mean inflammation-01.csv
5.45
5.425
6.1
...
6.4
7.05
5.9</code></pre>
<p>but we might also want to look at the minimum of the first four lines</p>
<pre><code>$ head -4 inflammation-01.csv | python readings.py --min</code></pre>
<p>or the maximum inflammations in several files one after another:</p>
<pre><code>$ python readings.py --max inflammation-*.csv</code></pre>
<p>Our overall requirements are:</p>
<ol style="list-style-type: decimal">
<li>If no filename is given on the command line, read data from <a href="../../gloss.html#standard-input">standard input</a>.</li>
<li>If one or more filenames are given, read data from them and report statistics for each file separately.</li>
<li>Use the <code>--min</code>, <code>--mean</code>, or <code>--max</code> flag to determine what statistic to print.</li>
</ol>
<p>To make this work, we need to know how to handle command-line arguments in a program, and how to get at standard input. We'll tackle these questions in turn below.</p>
</div>


<div class="objectives">
<h4 id="objectives">Objectives</h4>
<ul>
<li>Use the values of command-line arguments in a program.</li>
<li>Handle flags and files separately in a command-line program.</li>
<li>Read data from standard input in a program so that it can be used in a pipeline.</li>
</ul>
</div>

### Command-Line Arguments


<div class="">
<p>Using the text editor of your choice, save the following in a text file:</p>
</div>


<div class="in">
<pre>!cat sys-version.py</pre>
</div>

<div class="out">
<pre>import sys
print &#39;version is&#39;, sys.version
</pre>
</div>


<div class="">
<p>The first line imports a library called <code>sys</code>, which is short for &quot;system&quot;. It defines values such as <code>sys.version</code>, which describes which version of Python we are running. We can run this script from within the IPython Notebook like this:</p>
</div>


<div class="in">
<pre>%run sys-version.py</pre>
</div>

<div class="out">
<pre>version is 2.7.5 |Anaconda 1.8.0 (x86_64)| (default, Oct 24 2013, 07:02:20) 
[GCC 4.0.1 (Apple Inc. build 5493)]
</pre>
</div>


<div class="">
<p>or like this:</p>
</div>


<div class="in">
<pre>!ipython sys-version.py</pre>
</div>

<div class="out">
<pre>version is 2.7.5 |Anaconda 1.8.0 (x86_64)| (default, Oct 24 2013, 07:02:20) 
[GCC 4.0.1 (Apple Inc. build 5493)]
</pre>
</div>


<div class="">
<p>The first method, <code>%run</code>, uses a special command in the IPython Notebook to run a program in a <code>.py</code> file. The second method is more general: the exclamation mark <code>!</code> tells the Notebook to run a shell command, and it just so happens that the command we run is <code>ipython</code> with the name of the script.</p>
</div>


<div class="">
<p>Here's another script that does something more interesting:</p>
</div>


<div class="in">
<pre>!cat argv-list.py</pre>
</div>

<div class="out">
<pre>import sys
print &#39;sys.argv is&#39;, sys.argv
</pre>
</div>


<div class="">
<p>The strange name <code>argv</code> stands for &quot;argument values&quot;. Whenever Python runs a program, it takes all of the values given on the command line and puts them in the list <code>sys.argv</code> so that the program can determine what they were. If we run this program with no arguments:</p>
</div>


<div class="in">
<pre>!ipython argv-list.py</pre>
</div>

<div class="out">
<pre>sys.argv is [&#39;/Users/gwilson/s/bc/python/novice/argv-list.py&#39;]
</pre>
</div>


<div class="">
<p>the only thing in the list is the full path to our script, which is always <code>sys.argv[0]</code>. If we run it with a few arguments, however:</p>
</div>


<div class="in">
<pre>!ipython argv-list.py first second third</pre>
</div>

<div class="out">
<pre>sys.argv is [&#39;/Users/gwilson/s/bc/python/novice/argv-list.py&#39;, &#39;first&#39;, &#39;second&#39;, &#39;third&#39;]
</pre>
</div>


<div class="">
<p>then Python adds each of those arguments to that magic list.</p>
</div>


<div class="">
<p>With this in hand, let's build a version of <code>readings.py</code> that always prints the per-patient mean of a single data file. The first step is to write a function that outlines our implementation, and a placeholder for the function that does the actual work. By convention this function is usually called <code>main</code>, though we can call it whatever we want:</p>
</div>


<div class="in">
<pre>!cat readings-01.py</pre>
</div>

<div class="out">
<pre>import sys
import numpy as np

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = np.loadtxt(filename, delimiter=&#39;,&#39;)
    for m in data.mean(axis=1):
        print m
</pre>
</div>


<div class="">
<p>This function gets the name of the script from <code>sys.argv[0]</code>, because that's where it's always put, and the name of the file to process from <code>sys.argv[1]</code>. Here's a simple test:</p>
</div>


<div class="in">
<pre>%run readings-01.py inflammation-01.csv</pre>
</div>


<div class="">
<p>There is no output because we have defined a function, but haven't actually called it. Let's add a call to <code>main</code>:</p>
</div>


<div class="in">
<pre>!cat readings-02.py</pre>
</div>

<div class="out">
<pre>import sys
import numpy as np

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = np.loadtxt(filename, delimiter=&#39;,&#39;)
    for m in data.mean(axis=1):
        print m

main()
</pre>
</div>


<div class="">
<p>and run that:</p>
</div>


<div class="in">
<pre>%run readings-02.py inflammation-01.csv</pre>
</div>

<div class="out">
<pre>5.45
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
</pre>
</div>


<div>
<blockquote>
<h4 id="the-right-way-to-do-it">The Right Way to Do It</h4>
<p>If our programs can take complex parameters or multiple filenames,
we shouldn&#39;t handle <code>sys.argv</code> directly.
Instead,
we should use Python&#39;s <code>argparse</code> library,
which handles common cases in a systematic way,
and also makes it easy for us to provide sensible error messages for our users.</p>
</blockquote>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol>
<li><p>Write a command-line program that does addition and subtraction:</p>
<pre><code>$ python arith.py 1 + 2
3
</code></pre><pre><code>$ python arith.py 3 - 4
-1
</code></pre><p>What goes wrong if you try to add multiplication using &#39;*&#39; to the program?</p>
</li>
<li><p>Using the <code>glob</code> module introduced <a href="earlier">03-loop.ipynb</a>,
write a simple version of <code>ls</code> that shows files in the current directory with a particular suffix:</p>
<pre><code>$ python my_ls.py py
left.py
right.py
zero.py
</code></pre></li>
</ol>
</div>

### Handling Multiple Files


<div class="">
<p>The next step is to teach our program how to handle multiple files. Since 60 lines of output per file is a lot to page through, we'll start by creating three smaller files, each of which has three days of data for two patients:</p>
</div>


<div class="in">
<pre>!ls small-*.csv</pre>
</div>

<div class="out">
<pre>small-01.csv small-02.csv small-03.csv
</pre>
</div>


<div class="in">
<pre>!cat small-01.csv</pre>
</div>

<div class="out">
<pre>0,0,1
0,1,2
</pre>
</div>


<div class="in">
<pre>%run readings-02.py small-01.csv</pre>
</div>

<div class="out">
<pre>0.333333333333
1.0
</pre>
</div>


<div class="">
<p>Using small data files as input also allows us to check our results more easily: here, for example, we can see that our program is calculating the mean correctly for each line, whereas we were really taking it on faith before. This is yet another rule of programming: &quot;<a href="../../rules.html#test-simple-first">test the simple things first</a>&quot;.</p>
<p>We want our program to process each file separately, so we need a looop that executes once for each filename. If we specify the files on the command line, the filenames will be in <code>sys.argv</code>, but we need to be careful: <code>sys.argv[0]</code> will always be the name of our script, rather than the name of a file. We also need to handle an unknown number of filenames, since our program could be run for any number of files.</p>
<p>The solution to both problems is to loop over the contents of <code>sys.argv[1:]</code>. The '1' tells Python to start the slice at location 1, so the program's name isn't included; since we've left off the upper bound, the slice runs to the end of the list, and includes all the filenames. Here's our changed program:</p>
</div>


<div class="in">
<pre>!cat readings-03.py</pre>
</div>

<div class="out">
<pre>import sys
import numpy as np

def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        data = np.loadtxt(filename, delimiter=&#39;,&#39;)
        for m in data.mean(axis=1):
            print m

main()
</pre>
</div>


<div class="">
<p>and here it is in action:</p>
</div>


<div class="in">
<pre>%run readings-03.py small-01.csv small-02.csv</pre>
</div>

<div class="out">
<pre>0.333333333333
1.0
13.6666666667
11.0
</pre>
</div>


<div class="">
<p>Note: at this point, we have created three versions of our script called <code>readings-01.py</code>, <code>readings-02.py</code>, and <code>readings-03.py</code>. We wouldn't do this in real life: instead, we would have one file called <code>readings.py</code> that we committed to version control every time we got an enhancement working. For teaching, though, we need all the successive versions side by side.</p>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol style="list-style-type: decimal">
<li>Write a program called <code>check.py</code> that takes the names of one or more inflammation data files as arguments and checks that all the files have the same number of rows and columns. What is the best way to test your program?</li>
</ol>
</div>

### Handling Command-Line Flags


<div class="">
<p>The next step is to teach our program to pay attention to the <code>--min</code>, <code>--mean</code>, and <code>--max</code> flags. These always appear before the names of the files, so we could just do this:</p>
</div>


<div class="in">
<pre>!cat readings-04.py</pre>
</div>

<div class="out">
<pre>import sys
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
</pre>
</div>


<div class="">
<p>This works:</p>
</div>


<div class="in">
<pre>%run readings-04.py --max small-01.csv</pre>
</div>

<div class="out">
<pre>1.0
2.0
</pre>
</div>


<div class="">
<p>but there are seveal things wrong with it:</p>
<ol style="list-style-type: decimal">
<li><p><code>main</code> is too large to read comfortably.</p></li>
<li><p>If <code>action</code> isn't one of the three recognized flags, the program loads each file but does nothing with it (because none of the branches in the conditional match). <a href="../../gloss.html#silent-failure">Silent failures</a> like this are always hard to debug.</p></li>
</ol>
<p>This version pulls the processing of each file out of the loop into a function of its own. It also checks that <code>action</code> is one of the allowed flags before doing any processing, so that the program fails fast:</p>
</div>


<div class="in">
<pre>!cat readings-05.py</pre>
</div>

<div class="out">
<pre>import sys
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
</pre>
</div>


<div class="">
<p>This is four lines longer than its predecessor, but broken into more digestible chunks of 8 and 12 lines.</p>
</div>


<div>
<p>Python has a module named <a href="http://docs.python.org/dev/library/argparse.html">argparse</a> that helps handle complex command-line flags. We will not cover this module in this lesson but you can go to Tshepang Lekhonkhobe's <a href="http://docs.python.org/dev/howto/argparse.html">Argparse tutorial</a> that is part of Python's Official Documentation.</p>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol style="list-style-type: decimal">
<li><p>Rewrite this program so that it uses <code>-n</code>, <code>-m</code>, and <code>-x</code> instead of <code>--min</code>, <code>--mean</code>, and <code>--max</code> respectively. Is the code easier to read? Is the program easier to understand?</p></li>
<li><p>Separately, modify the program so that if no parameters are given (i.e., no action is specified and no filenames are given), it prints a message explaining how it should be used.</p></li>
<li><p>Separately, modify the program so that if no action is given it displays the means of the data.</p></li>
</ol>
</div>

### Handling Standard Input


<div class="">
<p>The next thing our program has to do is read data from standard input if no filenames are given so that we can put it in a pipeline, redirect input to it, and so on. Let's experiment in another script:</p>
</div>


<div class="in">
<pre>!cat count-stdin.py</pre>
</div>

<div class="out">
<pre>import sys

count = 0
for line in sys.stdin:
    count += 1

print count, &#39;lines in standard input&#39;
</pre>
</div>


<div class="">
<p>This little program reads lines from a special &quot;file&quot; called <code>sys.stdin</code>, which is automatically connected to the program's standard input. We don't have to open it—Python and the operating system take care of that when the program starts up— but we can do almost anything with it that we could do to a regular file. Let's try running it as if it were a regular command-line program:</p>
</div>


<div class="in">
<pre>!ipython count-stdin.py &lt; small-01.csv</pre>
</div>

<div class="out">
<pre>2 lines in standard input
</pre>
</div>


<div class="">
<p>What if we run it using <code>%run</code>?</p>
</div>


<div class="in">
<pre>%run count-stdin.py &lt; small-01.csv</pre>
</div>

<div class="out">
<pre>0 lines in standard input
</pre>
</div>


<div class="">
<p>As you can see, <code>%run</code> doesn't understand file redirection: that's a shell thing.</p>
<p>A common mistake is to try to run something that reads from standard input like this:</p>
<pre><code>!ipython count_stdin.py small-01.csv</code></pre>
<p>i.e., to forget the <code>&lt;</code> character that redirect the file to standard input. In this case, there's nothing in standard input, so the program waits at the start of the loop for someone to type something on the keyboard. Since there's no way for us to do this, our program is stuck, and we have to halt it using the <code>Interrupt</code> option from the <code>Kernel</code> menu in the Notebook.</p>
<p>We now need to rewrite the program so that it loads data from <code>sys.stdin</code> if no filenames are provided. Luckily, <code>numpy.loadtxt</code> can handle either a filename or an open file as its first parameter, so we don't actually need to change <code>process</code>. That leaves <code>main</code>:</p>
</div>


<div class="">
<pre><code>def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in [&#39;--min&#39;, &#39;--mean&#39;, &#39;--max&#39;], \
           &#39;Action is not one of --min, --mean, or --max: &#39; + action
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for f in filenames:
            process(f, action)</code></pre>
</div>


<div class="">
<p>Let's try it out (we'll see in a moment why we send the output through <code>head</code>):</p>
</div>


<div class="in">
<pre>!ipython readings-06.py --mean &lt; small-01.csv | head -10</pre>
</div>

<div class="out">
<pre>[TerminalIPythonApp] CRITICAL | Bad config encountered during initialization:
[TerminalIPythonApp] CRITICAL | Unrecognized flag: &#39;--mean&#39;
=========
 IPython
=========

Tools for Interactive Computing in Python
=========================================

    A Python shell with automatic history (input and output), dynamic object
    introspection, easier configuration, command completion, access to the
    system shell and more.  IPython can also be embedded in running programs.
</pre>
</div>


<div class="">
<p>Whoops: why are we getting IPython's help rather than the line-by-line average of our data? The answer is that IPython has a hard time telling which command-line arguments are meant for it, and which are meant for the program it's running. To make our meaning clear, we have to use <code>--</code> (a double dash) to separate the two:</p>
</div>


<div class="in">
<pre>!ipython readings-06.py -- --mean &lt; small-01.csv</pre>
</div>

<div class="out">
<pre>0.333333333333
1.0
</pre>
</div>


<div class="">
<p>That's better. In fact, that's done: the program now does everything we set out to do.</p>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol style="list-style-type: decimal">
<li>Write a program called <code>line-count.py</code> that works like the Unix <code>wc</code> command:
<ul>
<li>If no filenames are given, it reports the number of lines in standard input.</li>
<li>If one or more filenames are given, it reports the number of lines in each, followed by the total number of lines.</li>
</ul></li>
</ol>
</div>


<div class="keypoints">
<h4 id="key-points">Key Points</h4>
<ul>
<li>The <code>sys</code> library connects a Python program to the system it is running on.</li>
<li>The list <code>sys.argv</code> contains the command-line arguments that a program was run with.</li>
<li>Avoid silent failures.</li>
<li>The &quot;file&quot; <code>sys.stdin</code> connects to a program's standard input.</li>
<li>The &quot;file&quot; <code>sys.stdout</code> connects to a program's standard output.</li>
</ul>
</div>
