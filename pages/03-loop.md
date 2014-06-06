---
layout: lesson
root: ../..
---

## Analyzing Multiple Data Sets


<div class="">
<p>We have created a function called <code>analyze</code> that creates graphs of the minimum, average, and maximum daily inflammation rates for a single data set:</p>
</div>


<div class="in">
<pre>%matplotlib inline

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

analyze(&#39;inflammation-01.csv&#39;)</pre>
</div>

<div class="out">
<pre>
<img src="../../novice/python/03-loop_files/novice/python/03-loop_2_0.png">
</pre>
</div>


<div class="">
<p>We can use it to analyze other data sets one by one:</p>
</div>


<div class="in">
<pre>analyze(&#39;inflammation-02.csv&#39;)</pre>
</div>

<div class="out">
<pre>
<img src="../../novice/python/03-loop_files/novice/python/03-loop_4_0.png">
</pre>
</div>


<div class="">
<p>but we have a dozen data sets right now and more on the way. We want to create plots for all our data sets with a single statement. To do that, we'll have to teach the computer how to repeat things.</p>
</div>


<div class="objectives">
<h4 id="objectives">Objectives</h4>
<ul>
<li>Explain what a for loop does.</li>
<li>Correctly write for loops to repeat simple calculations.</li>
<li>Trace changes to a loop variable as the loop runs.</li>
<li>Trace changes to other variables as they are updated by a for loop.</li>
<li>Explain what a list is.</li>
<li>Create and index lists of simple values.</li>
<li>Use a library function to get a list of filenames that match a simple wildcard pattern.</li>
<li>Use a for loop to process multiple files.</li>
</ul>
</div>

### For Loops


<div class="">
<p>Suppose we want to print each character in the word &quot;lead&quot; on a line of its own. One way is to use four <code>print</code> statements:</p>
</div>


<div class="in">
<pre>def print_characters(element):
    print element[0]
    print element[1]
    print element[2]
    print element[3]

print_characters(&#39;lead&#39;)</pre>
</div>

<div class="out">
<pre>l
e
a
d
</pre>
</div>


<div class="">
<p>but that's a bad approach for two reasons:</p>
<ol style="list-style-type: decimal">
<li><p>It doesn't scale: if we want to print the characters in a string that's hundreds of letters long, we'd be better off just typing them in.</p></li>
<li><p>It's fragile: if we give it a longer string, it only prints part of the data, and if we give it a shorter one, it produces an error because we're asking for characters that don't exist.</p></li>
</ol>
</div>


<div class="in">
<pre>print_characters(&#39;tin&#39;)</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
&lt;ipython-input-13-5bc7311e0bf3&gt; in &lt;module&gt;()
----&gt; 1 print_characters(&#39;tin&#39;)

&lt;ipython-input-12-11460561ea56&gt; in print_characters(element)
      3     print element[1]
      4     print element[2]
----&gt; 5     print element[3]
      6 
      7 print_characters(&#39;lead&#39;)

IndexError: string index out of ranget
i
n
</pre>
</div>


<div>
<p>Here's a better approach:</p>
</div>


<div class="in">
<pre>def print_characters(element):
    for char in element:
        print char

print_characters(&#39;lead&#39;)</pre>
</div>


<div class="">
<p>This is shorter---certainly shorter than something that prints every character in a hundred-letter string---and more robust as well:</p>
</div>


<div class="in">
<pre>print_characters(&#39;oxygen&#39;)</pre>
</div>


<div class="">
<p>The improved version of <code>print_characters</code> uses a <a href="../../gloss.html#for-loop">for loop</a> to repeat an operation---in this case, printing---once for each thing in a collection. The general form of a loop is:</p>
<pre>
<strong>for</strong> <em>variable</em> <strong>in</strong> <em>collection</em><strong>:</strong>
    <em>do things with variable</em>
</pre>

</div>


<div class="">
<p>We can call the <a href="../../gloss.html#loop-variable">loop variable</a> anything we like, but there must be a colon at the end of the line starting the loop, and we must indent the body of the loop.</p>
<p>Here's another loop that repeatedly updates a variable:</p>
</div>


<div class="in">
<pre>length = 0
for vowel in &#39;aeiou&#39;:
    length = length + 1
print &#39;There are&#39;, length, &#39;vowels&#39;</pre>
</div>


<div class="">
<p>It's worth tracing the execution of this little program step by step. Since there are five characters in <code>'aeiou'</code>, the statement on line 3 will be executed five times. The first time around, <code>length</code> is zero (the value assigned to it on line 1) and <code>vowel</code> is <code>'a'</code>. The statement adds 1 to the old value of <code>length</code>, producing 1, and updates <code>length</code> to refer to that new value. The next time around, <code>vowel</code> is <code>'e'</code> and <code>length</code> is 1, so <code>length</code> is updated to be 2. After three more updates, <code>length</code> is 5; since there is nothing left in <code>'aeiou'</code> for Python to process, the loop finishes and the <code>print</code> statement on line 4 tells us our final answer.</p>
<p>Note that a loop variable is just a variable that's being used to record progress in a loop. It still exists after the loop is over, and we can re-use variables previously defined as loop variables as well:</p>
</div>


<div class="in">
<pre>letter = &#39;z&#39;
for letter in &#39;abc&#39;:
    print letter
print &#39;after the loop, letter is&#39;, letter</pre>
</div>


<div class="">
<p>Note also that finding the length of a string is such a common operation that Python actually has a built-in function to do it called <code>len</code>:</p>
</div>


<div class="in">
<pre>print len(&#39;aeiou&#39;)</pre>
</div>


<div class="">
<p><code>len</code> is much faster than any function we could write ourselves, and much easier to read than a two-line loop; it will also give us the length of many other things that we haven't met yet, so we should always use it when we can.</p>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol>
<li><p>Python has a built-in function called <code>range</code> that creates a list of numbers:
<code>range(3)</code> produces <code>[0, 1, 2]</code>, <code>range(2, 5)</code> produces <code>[2, 3, 4]</code>, and <code>range(2, 10, 3)</code> produces <code>[2, 5, 8]</code>.
Using <code>range</code>,
write a function that prints the $N$ natural numbers:</p>
<pre><code class="language-python">print_N(<span class="number">3</span>)
<span class="number">1</span>
<span class="number">2</span>
<span class="number">3</span>
</code></pre>
</li>
<li><p>Exponentiation is built into Python:</p>
<pre><code class="language-python"><span class="keyword">print</span> <span class="number">2</span>**<span class="number">4</span>
<span class="number">16</span>
</code></pre>
<p>It also has a function called <code>pow</code> that calculates the same value.
Write a function called <code>expo</code> that uses a loop to calculate the same result.</p>
</li>
<li><p>Write a function called <code>rev</code> that takes a string as input, and produces a new string with the characters in reverse order:</p>
<pre><code class="language-python"><span class="keyword">print</span> rev(<span class="string">'Newton'</span>)
notweN
</code></pre>
<p>As always, be sure to include a docstring.</p>
</li>
</ol>
</div>

### Lists


<div class="">
<p>Just as a <code>for</code> loop is a way to do operations many times, a list is a way to store many values. Unlike NumPy arrays, there are built into the language. We create a list by putting values inside square brackets:</p>
</div>


<div class="in">
<pre>odds = [1, 3, 5, 7]
print &#39;odds are:&#39;, odds</pre>
</div>


<div class="">
<p>We select individual elements from lists by indexing them:</p>
</div>


<div class="in">
<pre>print &#39;first and last:&#39;, odds[0], odds[-1]</pre>
</div>


<div class="">
<p>and if we loop over a list, the loop variable is assigned elements one at a time:</p>
</div>


<div class="in">
<pre>for number in odds:
    print number</pre>
</div>


<div class="">
<p>There is one important difference between lists and strings: we can change the values in a list, but we cannot change the characters in a string. For example:</p>
</div>


<div class="in">
<pre>names = [&#39;Newton&#39;, &#39;Darwing&#39;, &#39;Turing&#39;] # typo in Darwin&#39;s name
print &#39;names is originally:&#39;, names
names[1] = &#39;Darwin&#39; # correct the name
print &#39;final value of names:&#39;, names</pre>
</div>


<div class="">
<p>works, but:</p>
</div>


<div class="in">
<pre>name = &#39;Bell&#39;
name[0] = &#39;b&#39;</pre>
</div>


<div class="">
<p>does not.</p>
<blockquote>
<h4>Ch-Ch-Ch-Changes</h4>
<p>Data that can be changed is called <a href="../../gloss.html#mutable">mutable</a>, while data that cannot be is called <a href="../../gloss.html#immutable">immutable</a>. Like strings, numbers are immutable: there's no way to make the number 0 have the value 1 or vice versa (at least, not in Python—there actually <em>are</em> languages that will let people do this, with predictably confusing results). Lists and arrays, on the other hand, are mutable: both can be modified after they have been created.</p>
<p>Programs that modify data in place can be harder to understand than ones that don't because readers may have to mentally sum up many lines of code in order to figure out what the value of something actually is. On the other hand, programs that modify data in place instead of creating copies that are almost identical to the original every time they want to make a small change are much more efficient.</p>
</blockquote>
<p>There are many ways to change the contents of in lists besides assigning to elements:</p>
</div>


<div class="in">
<pre>odds.append(11)
print &#39;odds after adding a value:&#39;, odds</pre>
</div>


<div class="in">
<pre>del odds[0]
print &#39;odds after removing the first element:&#39;, odds</pre>
</div>


<div class="in">
<pre>odds.reverse()
print &#39;odds after reversing:&#39;, odds</pre>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol style="list-style-type: decimal">
<li>Write a function called <code>total</code> that calculates the sum of the values in a list. (Python has a built-in function called <code>sum</code> that does this for you. Please don't use it for this exercise.)</li>
</ol>
</div>

### Processing Multiple Files


<div class="">
<p>We now have almost everything we need to process all our data files. The only thing that's missing is a library with a rather unpleasant name:</p>
</div>


<div class="in">
<pre>import glob</pre>
</div>


<div class="">
<p>The <code>glob</code> library contains a single function, also called <code>glob</code>, that finds files whose names match a pattern. We provide those patterns as strings: the character <code>*</code> matches zero or more characters, while <code>?</code> matches any one character. We can use this to get the names of all the IPython Notebooks we have created so far:</p>
</div>


<div class="in">
<pre>print glob.glob(&#39;*.ipynb&#39;)</pre>
</div>

<div class="out">
<pre>[&#39;01-numpy.ipynb&#39;, &#39;02-func.ipynb&#39;, &#39;03-loop.ipynb&#39;, &#39;04-cond.ipynb&#39;, &#39;05-defensive.ipynb&#39;, &#39;06-cmdline.ipynb&#39;, &#39;spatial-intro.ipynb&#39;]
</pre>
</div>


<div class="">
<p>or to get the names of all our CSV data files:</p>
</div>


<div class="in">
<pre>print glob.glob(&#39;*.csv&#39;)</pre>
</div>

<div class="out">
<pre>[&#39;inflammation-01.csv&#39;, &#39;inflammation-02.csv&#39;, &#39;inflammation-03.csv&#39;, &#39;inflammation-04.csv&#39;, &#39;inflammation-05.csv&#39;, &#39;inflammation-06.csv&#39;, &#39;inflammation-07.csv&#39;, &#39;inflammation-08.csv&#39;, &#39;inflammation-09.csv&#39;, &#39;inflammation-10.csv&#39;, &#39;inflammation-11.csv&#39;, &#39;inflammation-12.csv&#39;, &#39;small-01.csv&#39;, &#39;small-02.csv&#39;, &#39;small-03.csv&#39;, &#39;swc_bc_coords.csv&#39;]
</pre>
</div>


<div class="">
<p>As these examples show, <code>glob.glob</code>'s result is a list of strings, which means we can loop over it to do something with each filename in turn. In our case, the &quot;something&quot; we want is our <code>analyze</code> function. Let's test it by analyzing the first three files in the list:</p>
</div>


<div class="in">
<pre>filenames = glob.glob(&#39;*.csv&#39;)
filenames = filenames[0:3]
for f in filenames:
    print f
    analyze(f)</pre>
</div>

<div class="out">
<pre>inflammation-01.csv

<img src="../../novice/python/03-loop_files/novice/python/03-loop_49_1.png">
inflammation-02.csv

<img src="../../novice/python/03-loop_files/novice/python/03-loop_49_3.png">
inflammation-03.csv

<img src="../../novice/python/03-loop_files/novice/python/03-loop_49_5.png">
</pre>
</div>


<div class="">
<p>Sure enough, the maxima of these data sets show exactly the same ramp as the first, and their minima show the same staircase structure.</p>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol style="list-style-type: decimal">
<li>Write a function called <code>analyze_all</code> that takes a filename pattern as its sole argument and runs <code>analyze</code> for each file whose name matches the pattern.</li>
</ol>
</div>


<div class="">
<h4 id="key-points">Key Points</h4>
<ul>
<li>Use <code>for variable in collection</code> to process the elements of a collection one at a time.</li>
<li>The body of a for loop must be indented.</li>
<li>Use <code>len(thing)</code> to determine the length of something that contains other values.</li>
<li><code>[value1, value2, value3, ...]</code> creates a list.</li>
<li>Lists are indexed and sliced in the same way as strings and arrays.</li>
<li>Lists are mutable (i.e., their values can be changed in place).</li>
<li>Strings are immutable (i.e., the characters in them cannot be changed).</li>
<li>Use <code>glob.glob(pattern)</code> to create a list of files whose names match a pattern.</li>
<li>Use <code>*</code> in a pattern to match zero or more characters, and <code>?</code> to match any single character.</li>
</ul>
</div>


<div class="">
<h4 id="next-steps">Next Steps</h4>
<p>We have now solved our original problem: we can analyze any number of data files with a single command. More importantly, we have met two of the most important ideas in programming:</p>
<ol style="list-style-type: decimal">
<li>Use functions to make code easier to re-use and easier to understand.</li>
<li>Use lists and arrays to store related values, and loops to repeat operations on them.</li>
</ol>
<p>We have one more big idea to introduce, and then we will be able to go back and create a heat map like the one we initially used to display our first data set.</p>
</div>
