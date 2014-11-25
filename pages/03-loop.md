---
layout: lesson
root: ../..
---

## Analyzing Multiple Data Sets


We have created a function called `analyze` that creates graphs of the minimum, average, and maximum daily inflammation rates
for a single data set:


<pre class="in"><code>%matplotlib inline

import numpy as np
from matplotlib import pyplot as plt

def analyze(filename):
    data = np.loadtxt(fname=filename, delimiter=&#39;,&#39;)
    
    plt.figure(figsize=(10.0, 3.0))
    
    plt.subplot(1, 3, 1)
    plt.ylabel(&#39;average&#39;)
    plt.plot(data.mean(0))
    
    plt.subplot(1, 3, 2)
    plt.ylabel(&#39;max&#39;)
    plt.plot(data.max(0))
    
    plt.subplot(1, 3, 3)
    plt.ylabel(&#39;min&#39;)
    plt.plot(data.min(0))
    
    plt.tight_layout()
    plt.show()

analyze(&#39;inflammation-01.csv&#39;)</code></pre>

<div class="out">
<img src="../../novice/python/03-loop_files/novice/python/03-loop_2_0.png">
</div>


We can use it to analyze other data sets one by one:


<pre class="in"><code>analyze(&#39;inflammation-02.csv&#39;)</code></pre>

<div class="out">
<img src="../../novice/python/03-loop_files/novice/python/03-loop_4_0.png">
</div>


but we have a dozen data sets right now and more on the way.
We want to create plots for all our data sets with a single statement.
To do that,
we'll have to teach the computer how to repeat things.


<div class="objectives" markdown="1">
#### Objectives

*   Explain what a for loop does.
*   Correctly write for loops to repeat simple calculations.
*   Trace changes to a loop variable as the loop runs.
*   Trace changes to other variables as they are updated by a for loop.
*   Explain what a list is.
*   Create and index lists of simple values.
*   Use a library function to get a list of filenames that match a simple wildcard pattern.
*   Use a for loop to process multiple files.
</div>

### For Loops


Suppose we want to print each character in the word "lead" on a line of its own.
One way is to use four `print` statements:


<pre class="in"><code>def print_characters(element):
    print element[0]
    print element[1]
    print element[2]
    print element[3]

print_characters(&#39;lead&#39;)</code></pre>

<div class="out"><pre class='out'><code>l
e
a
d
</code></pre></div>


but that's a bad approach for two reasons:

1.  It doesn't scale:
    if we want to print the characters in a string that's hundreds of letters long,
    we'd be better off just typing them in.

1.  It's fragile:
    if we give it a longer string,
    it only prints part of the data,
    and if we give it a shorter one,
    it produces an error because we're asking for characters that don't exist.


<pre class="in"><code>print_characters(&#39;tin&#39;)</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
&lt;ipython-input-13-5bc7311e0bf3&gt; in &lt;module&gt;()
----&gt; 1 print_characters(&#39;tin&#39;)

&lt;ipython-input-12-11460561ea56&gt; in print_characters(element)
      3     print element[1]
      4     print element[2]
----&gt; 5     print element[3]
      6 
      7 print_characters(&#39;lead&#39;)

IndexError: string index out of range</code></pre><pre class='out'><code>t
i
n
</code></pre></div>


Here's a better approach:


<pre class="in"><code>def print_characters(element):
    for char in element:
        print char

print_characters(&#39;lead&#39;)</code></pre>


This is shorter---certainly shorter than something that prints every character in a hundred-letter string---and
more robust as well:


<pre class="in"><code>print_characters(&#39;oxygen&#39;)</code></pre>


The improved version of `print_characters` uses a [for loop](../../gloss.html#for-loop)
to repeat an operation---in this case, printing---once for each thing in a collection.
The general form of a loop is:

<pre>
<strong>for</strong> <em>variable</em> <strong>in</strong> <em>collection</em><strong>:</strong>
    <em>do things with variable</em>
</pre>


We can call the [loop variable](../../gloss.html#loop-variable) anything we like,
but there must be a colon at the end of the line starting the loop,
and we must indent the body of the loop.

Here's another loop that repeatedly updates a variable:


<pre class="in"><code>length = 0
for vowel in &#39;aeiou&#39;:
    length = length + 1
print &#39;There are&#39;, length, &#39;vowels&#39;</code></pre>


It's worth tracing the execution of this little program step by step.
Since there are five characters in `'aeiou'`,
the statement on line 3 will be executed five times.
The first time around,
`length` is zero (the value assigned to it on line 1)
and `vowel` is `'a'`.
The statement adds 1 to the old value of `length`,
producing 1,
and updates `length` to refer to that new value.
The next time around,
`vowel` is `'e'` and `length` is 1,
so `length` is updated to be 2.
After three more updates,
`length` is 5;
since there is nothing left in `'aeiou'` for Python to process,
the loop finishes
and the `print` statement on line 4 tells us our final answer.

Note that a loop variable is just a variable that's being used to record progress in a loop.
It still exists after the loop is over,
and we can re-use variables previously defined as loop variables as well:


<pre class="in"><code>letter = &#39;z&#39;
for letter in &#39;abc&#39;:
    print letter
print &#39;after the loop, letter is&#39;, letter</code></pre>


Note also that finding the length of a string is such a common operation
that Python actually has a built-in function to do it called `len`:


<pre class="in"><code>print len(&#39;aeiou&#39;)</code></pre>


`len` is much faster than any function we could write ourselves,
and much easier to read than a two-line loop;
it will also give us the length of many other things that we haven't met yet,
so we should always use it when we can.


<div class="challenges" markdown="1">
#### Challenges

1.  Python has a built-in function called `range` that creates a list of numbers:
    `range(3)` produces `[0, 1, 2]`, `range(2, 5)` produces `[2, 3, 4]`.
    Using `range`,
    write a function that prints the $N$ natural numbers:
    
    ~~~python
    print_N(3)
    1
    2
    3
    ~~~

1.  Exponentiation is built into Python:

    ~~~python
    print 5**3
    125
    ~~~
    
    It also has a function called `pow` that calculates the same value.
    Write a function called `expo` that uses a loop to calculate the same result.

1.  Write a function called `rev` that takes a string as input, and produces a new string with the characters in reverse order:
    
    ~~~python
    print rev('Newton')
    notweN
    ~~~
    
    As always, be sure to include a docstring.
</div>

### Lists


Just as a `for` loop is a way to do operations many times,
a list is a way to store many values.
Unlike NumPy arrays,
there are built into the language.
We create a list by putting values inside square brackets:


<pre class="in"><code>odds = [1, 3, 5, 7]
print &#39;odds are:&#39;, odds</code></pre>


We select individual elements from lists by indexing them:


<pre class="in"><code>print &#39;first and last:&#39;, odds[0], odds[-1]</code></pre>


and if we loop over a list,
the loop variable is assigned elements one at a time:


<pre class="in"><code>for number in odds:
    print number</code></pre>


There is one important difference between lists and strings:
we can change the values in a list,
but we cannot change the characters in a string.
For example:


<pre class="in"><code>names = [&#39;Newton&#39;, &#39;Darwing&#39;, &#39;Turing&#39;] # typo in Darwin&#39;s name
print &#39;names is originally:&#39;, names
names[1] = &#39;Darwin&#39; # correct the name
print &#39;final value of names:&#39;, names</code></pre>


works, but:


<pre class="in"><code>name = &#39;Bell&#39;
name[0] = &#39;b&#39;</code></pre>


does not.

> #### Ch-Ch-Ch-Changes
>
> Data that can be changed is called [mutable](../../gloss.html#mutable),
> while data that cannot be is called [immutable](../../gloss.html#immutable).
> Like strings,
> numbers are immutable:
> there's no way to make the number 0 have the value 1 or vice versa
> (at least, not in Python&mdash;there actually *are* languages that will let people do this,
> with predictably confusing results).
> Lists and arrays,
> on the other hand,
> are mutable:
> both can be modified after they have been created.
>
> Programs that modify data in place can be harder to understand than ones that don't
> because readers may have to mentally sum up many lines of code
> in order to figure out what the value of something actually is.
> On the other hand,
> programs that modify data in place instead of creating copies that are almost identical to the original
> every time they want to make a small change
> are much more efficient.

There are many ways to change the contents of in lists besides assigning to elements:


<pre class="in"><code>odds.append(11)
print &#39;odds after adding a value:&#39;, odds</code></pre>


<pre class="in"><code>del odds[0]
print &#39;odds after removing the first element:&#39;, odds</code></pre>


<pre class="in"><code>odds.reverse()
print &#39;odds after reversing:&#39;, odds</code></pre>


<div class="challenges" markdown="1">
#### Challenges

1.  Write a function called `total` that calculates the sum of the values in a list.
    (Python has a built-in function called `sum` that does this for you.
    Please don't use it for this exercise.)
</div>

### Processing Multiple Files


We now have almost everything we need to process all our data files.
The only thing that's missing is a library with a rather unpleasant name:


<pre class="in"><code>import glob</code></pre>


The `glob` library contains a single function, also called `glob`,
that finds files whose names match a pattern.
We provide those patterns as strings:
the character `*` matches zero or more characters,
while `?` matches any one character.
We can use this to get the names of all the IPython Notebooks we have created so far:


<pre class="in"><code>print glob.glob(&#39;*.ipynb&#39;)</code></pre>

<div class="out"><pre class='out'><code>[&#39;01-numpy.ipynb&#39;, &#39;02-func.ipynb&#39;, &#39;03-loop.ipynb&#39;, &#39;04-cond.ipynb&#39;, &#39;05-defensive.ipynb&#39;, &#39;06-cmdline.ipynb&#39;, &#39;spatial-intro.ipynb&#39;]
</code></pre></div>


or to get the names of all our CSV data files:


<pre class="in"><code>print glob.glob(&#39;*.csv&#39;)</code></pre>

<div class="out"><pre class='out'><code>[&#39;inflammation-01.csv&#39;, &#39;inflammation-02.csv&#39;, &#39;inflammation-03.csv&#39;, &#39;inflammation-04.csv&#39;, &#39;inflammation-05.csv&#39;, &#39;inflammation-06.csv&#39;, &#39;inflammation-07.csv&#39;, &#39;inflammation-08.csv&#39;, &#39;inflammation-09.csv&#39;, &#39;inflammation-10.csv&#39;, &#39;inflammation-11.csv&#39;, &#39;inflammation-12.csv&#39;, &#39;small-01.csv&#39;, &#39;small-02.csv&#39;, &#39;small-03.csv&#39;, &#39;swc_bc_coords.csv&#39;]
</code></pre></div>


As these examples show,
`glob.glob`'s result is a list of strings,
which means we can loop over it
to do something with each filename in turn.
In our case,
the "something" we want is our `analyze` function.
Let's test it by analyzing the first three files in the list:


<pre class="in"><code>filenames = glob.glob(&#39;*.csv&#39;)
filenames = filenames[0:3]
for f in filenames:
    print f
    analyze(f)</code></pre>

<div class="out"><pre class='out'><code>inflammation-01.csv
</code></pre>
<img src="../../novice/python/03-loop_files/novice/python/03-loop_49_1.png">
<pre class='out'><code>inflammation-02.csv
</code></pre>
<img src="../../novice/python/03-loop_files/novice/python/03-loop_49_3.png">
<pre class='out'><code>inflammation-03.csv
</code></pre>
<img src="../../novice/python/03-loop_files/novice/python/03-loop_49_5.png">
</div>


Sure enough,
the maxima of these data sets show exactly the same ramp as the first,
and their minima show the same staircase structure.


<div class="challenges" markdown="1">
#### Challenges

1.  Write a function called `analyze_all` that takes a filename pattern as its sole argument
    and runs `analyze` for each file whose name matches the pattern.
</div>


#### Key Points

*   Use `for variable in collection` to process the elements of a collection one at a time.
*   The body of a for loop must be indented.
*   Use `len(thing)` to determine the length of something that contains other values.
*   `[value1, value2, value3, ...]` creates a list.
*   Lists are indexed and sliced in the same way as strings and arrays.
*   Lists are mutable (i.e., their values can be changed in place).
*   Strings are immutable (i.e., the characters in them cannot be changed).
*   Use `glob.glob(pattern)` to create a list of files whose names match a pattern.
*   Use `*` in a pattern to match zero or more characters, and `?` to match any single character.


#### Next Steps

We have now solved our original problem:
we can analyze any number of data files with a single command.
More importantly,
we have met two of the most important ideas in programming:

1.  Use functions to make code easier to re-use and easier to understand.
1.  Use lists and arrays to store related values, and loops to repeat operations on them.

We have one more big idea to introduce,
and then we will be able to go back and create a heat map
like the one we initially used to display our first data set.
