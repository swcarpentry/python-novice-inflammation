---
layout: lesson
root: ../..
---

## Creating Functions


<div class="">
<p>If we only had one data set to analyze, it would probably be faster to load the file into a spreadsheet and use that to plot some simple statistics. But we have twelve files to check, and may have more in future. In this lesson, we'll learn how to write a function so that we can repeat several operations with a single command.</p>
</div>


<div class="objectives">
<h4 id="objectives">Objectives</h4>
<ul>
<li>Define a function that takes parameters.</li>
<li>Return a value from a function.</li>
<li>Test and debug a function.</li>
<li>Explain what a call stack is, and trace changes to the call stack as functions are called.</li>
<li>Set default values for function parameters.</li>
<li>Explain why we should divide programs into small, single-purpose functions.</li>
</ul>
</div>

### Defining a Function


<div class="">
<p>Let's start by defining a function <code>fahr_to_kelvin</code> that converts temperatures from Fahrenheit to Kelvin:</p>
</div>


<div class="in">
<pre>def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15</pre>
</div>


<div class="">
<p>The definition opens with the word <code>def</code>, which is followed by the name of the function and a parenthesized list of parameter names. The <a href="../../gloss.html#function-body">body</a> of the function—the statements that are executed when it runs—is indented below the definition line, typically by four spaces.</p>
<p>When we call the function, the values we pass to it are assigned to those variables so that we can use them inside the function. Inside the function, we use a <a href="../../gloss.html#return-statement">return statement</a> to send a result back to whoever asked for it.</p>
<p>Let's try running our function. Calling our own function is no different from calling any other function:</p>
</div>


<div class="in">
<pre>print &#39;freezing point of water:&#39;, fahr_to_kelvin(32)
print &#39;boiling point of water:&#39;, fahr_to_kelvin(212)</pre>
</div>

<div class="out">
<pre>freezing point of water: 273.15
boiling point of water: 273.15
</pre>
</div>


<div>
<p>We've successfully called the function that we defined, and we have access to the value that we returned. Unfortunately, the value returned doesn't look right. What went wrong?</p>
</div>

### Debugging a Function


<div>
<p><em>Debugging</em> is when we fix a piece of code that we know is working incorrectly. In this case, we know that <code>fahr_to_kelvin</code> is giving us the wrong answer, so let's find out why.</p>
<p>For big pieces of code, there are tools called <em>debuggers</em> that aid in this process.</p>
<p>We just have a short function, so we'll debug by choosing some parameter value, breaking our function into small parts, and printing out the value of each part.</p>
</div>


<div class="in">
<pre># We&#39;ll use temp = 212, the boiling point of water, which was incorrect
print &#34;212 - 32:&#34;, 212 - 32</pre>
</div>

<div class="out">
<pre>212 - 32: 180
</pre>
</div>


<div class="in">
<pre>print &#34;(212 - 32) * (5/9):&#34;, (212 - 32) * (5/9)</pre>
</div>

<div class="out">
<pre>(212 - 32) * (5/9): 0
</pre>
</div>


<div>
<p>Aha! The problem comes when we multiply by <code>5/9</code>. This is because <code>5/9</code> is actually 0.</p>
</div>


<div class="in">
<pre>5/9</pre>
</div>

<div class="out">
<pre>0</pre>
</div>


<div class="">
<p>Computers store numbers in one of two ways: as <a href="../../gloss.html#integer">integers</a> or as <a href="../../gloss.html#float">floating-point numbers</a> (or floats). The first are the numbers we usually count with; the second have fractional parts. Addition, subtraction and multiplication work on both as we'd expect, but division works differently. If we divide one integer by another, we get the quotient without the remainder:</p>
</div>


<div class="in">
<pre>print &#39;10/3 is:&#39;, 10/3</pre>
</div>

<div class="out">
<pre>10/3 is: 3
</pre>
</div>


<div class="">
<p>If either part of the division is a float, on the other hand, the computer creates a floating-point answer:</p>
</div>


<div class="in">
<pre>print &#39;10.0/3 is:&#39;, 10.0/3</pre>
</div>

<div class="out">
<pre>10.0/3 is: 3.33333333333
</pre>
</div>


<div class="">
<p>The computer does this for historical reasons: integer operations were much faster on early machines, and this behavior is actually useful in a lot of situations. It's still confusing, though, so Python 3 produces a floating-point answer when dividing integers if it needs to. We're still using Python 2.7 in this class, though, so if we want <code>5/9</code> to give us the right answer, we have to write it as <code>5.0/9</code>, <code>5/9.0</code>, or some other variation.</p>
</div>


<div>
<p>Let's fix our <code>fahr_to_kelvin</code> function with this new knowledge.</p>
</div>


<div class="in">
<pre>def fahr_to_kelvin(temp):
    return ((temp - 32) * (5.0/9.0)) + 273.15

print &#39;freezing point of water:&#39;, fahr_to_kelvin(32)
print &#39;boiling point of water:&#39;, fahr_to_kelvin(212)</pre>
</div>

<div class="out">
<pre>freezing point of water: 273.15
boiling point of water: 373.15
</pre>
</div>


<div class="">
<p>It works!</p>
</div>

### Composing Functions


<div>
<p>Now that we've seen how to turn Fahrenheit into Kelvin, it's easy to turn Kelvin into Celsius:</p>
</div>


<div class="in">
<pre>def kelvin_to_celsius(temp):
    return temp - 273.15

print &#39;absolute zero in Celsius:&#39;, kelvin_to_celsius(0.0)</pre>
</div>

<div class="out">
<pre>absolute zero in Celsius: -273.15
</pre>
</div>


<div class="">
<p>What about converting Fahrenheit to Celsius? We could write out the formula, but we don't need to. Instead, we can <a href="../../gloss.html#function-composition">compose</a> the two functions we have already created:</p>
</div>


<div class="in">
<pre>def fahr_to_celsius(temp):
    temp_k = fahr_to_kelvin(temp)
    result = kelvin_to_celsius(temp_k)
    return result

print &#39;freezing point of water in Celsius:&#39;, fahr_to_celsius(32.0)</pre>
</div>

<div class="out">
<pre>freezing point of water in Celsius: 0.0
</pre>
</div>


<div class="">
<p>This is our first taste of how larger programs are built: we define basic operations, then combine them in ever-large chunks to get the effect we want. Real-life functions will usually be larger than the ones shown here—typically half a dozen to a few dozen lines—but they shouldn't ever be much longer than that, or the next person who reads it won't be able to understand what's going on.</p>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol style="list-style-type: decimal">
<li><p>&quot;Adding&quot; two strings produces their concatention: <code>'a' + 'b'</code> is <code>'ab'</code>. Write a function called <code>fence</code> that takes two parameters called <code>original</code> and <code>wrapper</code> and returns a new string that has the wrapper character at the beginning and end of the original:</p>
<pre class="sourceCode python"><code class="sourceCode python"><span class="kw">print</span> fence(<span class="st">&#39;name&#39;</span>, <span class="st">&#39;*&#39;</span>)
*name*</code></pre></li>
<li><p>If the variable <code>s</code> refers to a string, then <code>s[0]</code> is the string's first character and <code>s[-1]</code> is its last. Write a function called <code>outer</code> that returns a string made up of just the first and last characters of its input:</p>
<pre class="sourceCode python"><code class="sourceCode python"><span class="kw">print</span> outer(<span class="st">&#39;helium&#39;</span>)
hm</code></pre></li>
</ol>
</div>

### The Call Stack


<div class="">
<p>Let's take a closer look at what happens when we call <code>fahr_to_celsius(32.0)</code>. To make things clearer, we'll start by putting the initial value 32.0 in a variable and store the final result in one as well:</p>
</div>


<div class="in">
<pre>original = 32.0
final = fahr_to_celsius(original)</pre>
</div>


<div class="">
<p>The diagram below shows what memory looks like after the first line has been executed:</p>
</div>


<div class="">
<p><img src="img/python-call-stack-01.svg" alt="Call Stack (Initial State)" /></p>
</div>


<div class="">
<p>When we call <code>fahr_to_celsius</code>, Python <em>doesn't</em> create the variable <code>temp</code> right away. Instead, it creates something called a <a href="../../gloss.html#stack-frame">stack frame</a> to keep track of the variables defined by <code>fahr_to_kelvin</code>. Initially, this stack frame only holds the value of <code>temp</code>:</p>
</div>


<div class="">
<p><img src="img/python-call-stack-02.svg" alt="Call Stack Immediately After First Function Call" /></p>
</div>


<div class="">
<p>When we call <code>fahr_to_kelvin</code> inside <code>fahr_to_celsius</code>, Python creates another stack frame to hold <code>fahr_to_kelvin</code>'s variables:</p>
</div>


<div class="">
<p><img src="img/python-call-stack-03.svg" alt="Call Stack During First Nested Function Call" /></p>
</div>


<div class="">
<p>It does this because there are now two variables in play called <code>temp</code>: the parameter to <code>fahr_to_celsius</code>, and the parameter to <code>fahr_to_kelvin</code>. Having two variables with the same name in the same part of the program would be ambiguous, so Python (and every other modern programming language) creates a new stack frame for each function call to keep that function's variables separate from those defined by other functions.</p>
<p>When the call to <code>fahr_to_kelvin</code> returns a value, Python throws away <code>fahr_to_kelvin</code>'s stack frame and creates a new variable in the stack frame for <code>fahr_to_celsius</code> to hold the temperature in Kelvin:</p>
</div>


<div class="">
<p><img src="img/python-call-stack-04.svg" alt="Call Stack After Return From First Nested Function Call" /></p>
</div>


<div class="">
<p>It then calls <code>kelvin_to_celsius</code>, which means it creates a stack frame to hold that function's variables:</p>
</div>


<div class="">
<p><img src="img/python-call-stack-05.svg" alt="Call Stack During Call to Second Nested Function" /></p>
</div>


<div class="">
<p>Once again, Python throws away that stack frame when <code>kelvin_to_celsius</code> is done and creates the variable <code>result</code> in the stack frame for <code>fahr_to_celsius</code>:</p>
</div>


<div class="">
<p><img src="img/python-call-stack-06.svg" alt="Call Stack After Second Nested Function Returns" /></p>
</div>


<div class="">
<p>Finally, when <code>fahr_to_celsius</code> is done, Python throws away <em>its</em> stack frame and puts its result in a new variable called <code>final</code> that lives in the stack frame we started with:</p>
</div>


<div class="">
<p><img src="img/python-call-stack-07.svg" alt="Call Stack After All Functions Have Finished" /></p>
</div>


<div class="">
<p>This final stack frame is always there; it holds the variables we defined outside the functions in our code. What it <em>doesn't</em> hold is the variables that were in the various stack frames. If we try to get the value of <code>temp</code> after our functions have finished running, Python tells us that there's no such thing:</p>
</div>


<div class="in">
<pre>print &#39;final value of temp after all function calls:&#39;, temp</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-12-ffd9b4dbd5f1&gt; in &lt;module&gt;()
----&gt; 1 print &#39;final value of temp after all function calls:&#39;, temp

NameError: name &#39;temp&#39; is not definedfinal value of temp after all function calls:</pre>
</div>


<div class="">
<p>Why go to all this trouble? Well, here's a function called <code>span</code> that calculates the difference between the mininum and maximum values in an array:</p>
</div>


<div class="in">
<pre>import numpy

def span(a):
    diff = a.max() - a.min()
    return diff

data = numpy.loadtxt(fname=&#39;inflammation-01.csv&#39;, delimiter=&#39;,&#39;)
print &#39;span of data&#39;, span(data)</pre>
</div>

<div class="out">
<pre> span of data 20.0
</pre>
</div>


<div class="">
<p>Notice that <code>span</code> assigns a value to a variable called <code>diff</code>. We might very well use a variable with the same name to hold data:</p>
</div>


<div class="in">
<pre>diff = numpy.loadtxt(fname=&#39;inflammation-01.csv&#39;, delimiter=&#39;,&#39;)
print &#39;span of data:&#39;, span(diff)</pre>
</div>

<div class="out">
<pre>span of data: 20.0
</pre>
</div>


<div class="">
<p>We don't expect <code>diff</code> to have the value 20.0 after this function call, so the name <code>diff</code> cannot refer to the same thing inside <code>span</code> as it does in the main body of our program. And yes, we could probably choose a different name than <code>diff</code> in our main program in this case, but we don't want to have to read every line of NumPy to see what variable names its functions use before calling any of those functions, just in case they change the values of our variables.</p>
</div>


<div class="">
<p>The big idea here is <a href="../../gloss.html#encapsulation">encapsulation</a>, and it's the key to writing correct, comprehensible programs. A function's job is to turn several operations into one so that we can think about a single function call instead of a dozen or a hundred statements each time we want to do something. That only works if functions don't interfere with each other; if they do, we have to pay attention to the details once again, which quickly overloads our short-term memory.</p>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol style="list-style-type: decimal">
<li>We previously wrote functions called <code>fence</code> and <code>outer</code>. Draw a diagram showing how the call stack changes when we run the following: <sub>~</sub>python print outer(fence('carbon', '+')) <sub>~</sub></li>
</ol>
</div>

### Testing and Documenting


<div class="">
<p>Once we start putting things in functions so that we can re-use them, we need to start testing that those functions are working correctly. To see how to do this, let's write a function to center a dataset around a particular value:</p>
</div>


<div class="in">
<pre>def center(data, desired):
    return (data - data.mean()) + desired</pre>
</div>


<div class="">
<p>We could test this on our actual data, but since we don't know what the values ought to be, it will be hard to tell if the result was correct. Instead, let's use NumPy to create a matrix of 0's and then center that around 3:</p>
</div>


<div class="in">
<pre>z = numpy.zeros((2,2))
print center(z, 3)</pre>
</div>

<div class="out">
<pre>[[ 3.  3.]
 [ 3.  3.]]
</pre>
</div>


<div class="">
<p>That looks right, so let's try <code>center</code> on our real data:</p>
</div>


<div class="in">
<pre>data = numpy.loadtxt(fname=&#39;inflammation-01.csv&#39;, delimiter=&#39;,&#39;)
print center(data, 0)</pre>
</div>

<div class="out">
<pre>[[-6.14875 -6.14875 -5.14875 ..., -3.14875 -6.14875 -6.14875]
 [-6.14875 -5.14875 -4.14875 ..., -5.14875 -6.14875 -5.14875]
 [-6.14875 -5.14875 -5.14875 ..., -4.14875 -5.14875 -5.14875]
 ..., 
 [-6.14875 -5.14875 -5.14875 ..., -5.14875 -5.14875 -5.14875]
 [-6.14875 -6.14875 -6.14875 ..., -6.14875 -4.14875 -6.14875]
 [-6.14875 -6.14875 -5.14875 ..., -5.14875 -5.14875 -6.14875]]
</pre>
</div>


<div class="">
<p>It's hard to tell from the default output whether the result is correct, but there are a few simple tests that will reassure us:</p>
</div>


<div class="in">
<pre>print &#39;original min, mean, and max are:&#39;, data.min(), data.mean(), data.max()
centered = center(data, 0)
print &#39;min, mean, and and max of centered data are:&#39;, centered.min(), centered.mean(), centered.max()</pre>
</div>

<div class="out">
<pre>original min, mean, and max are: 0.0 6.14875 20.0
min, mean, and and max of centered data are: -6.14875 -3.49054118942e-15 13.85125
</pre>
</div>


<div class="">
<p>That seems almost right: the original mean was about 6.1, so the lower bound from zero is how about -6.1. The mean of the centered data isn't quite zero—we'll explore why not in the challenges—but it's pretty close. We can even go further and check that the standard deviation hasn't changed:</p>
</div>


<div class="in">
<pre>print &#39;std dev before and after:&#39;, data.std(), centered.std()</pre>
</div>

<div class="out">
<pre>std dev before and after: 4.61383319712 4.61383319712
</pre>
</div>


<div class="">
<p>Those values look the same, but we probably wouldn't notice if they were different in the sixth decimal place. Let's do this instead:</p>
</div>


<div class="in">
<pre>print &#39;difference in standard deviations before and after:&#39;, data.std() - centered.std()</pre>
</div>

<div class="out">
<pre>difference in standard deviations before and after: -3.5527136788e-15
</pre>
</div>


<div class="">
<p>Again, the difference is very small. It's still possible that our function is wrong, but it seems unlikely enough that we should probably get back to doing our analysis. We have one more task first, though: we should write some <a href="../../gloss.html#documentation">documentation</a> for our function to remind ourselves later what it's for and how to use it.</p>
<p>The usual way to put documentation in software is to add <a href="../../gloss.html#comment">comments</a> like this:</p>
</div>


<div class="in">
<pre># center(data, desired): return a new array containing the original data centered around the desired value.
def center(data, desired):
    return (data - data.mean()) + desired</pre>
</div>


<div class="">
<p>There's a better way, though. If the first thing in a function is a string that isn't assigned to a variable, that string is attached to the function as its documentation:</p>
</div>


<div class="in">
<pre>def center(data, desired):
    &#39;&#39;&#39;Return a new array containing the original data centered around the desired value.&#39;&#39;&#39;
    return (data - data.mean()) + desired</pre>
</div>


<div class="">
<p>This is better because we can now ask Python's built-in help system to show us the documentation for the function:</p>
</div>


<div class="in">
<pre>help(center)</pre>
</div>

<div class="out">
<pre>Help on function center in module __main__:

center(data, desired)
    Return a new array containing the original data centered around the desired value.

</pre>
</div>


<div class="">
<p>A string like this is called a <a href="../../gloss.html#docstring">docstring</a>. We don't need to use triple quotes when we write one, but if we do, we can break the string across multiple lines:</p>
</div>


<div class="in">
<pre>def center(data, desired):
    &#39;&#39;&#39;Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) =&gt; [-1, 0, 1]&#39;&#39;&#39;
    return (data - data.mean()) + desired

help(center)</pre>
</div>

<div class="out">
<pre>Help on function center in module __main__:

center(data, desired)
    Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) =&gt; [-1, 0, 1]

</pre>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol style="list-style-type: decimal">
<li><p>Write a function called <code>analyze</code> that takes a filename as a parameter and displays the three graphs produced in the <a href="01-numpy.ipynb">previous lesson</a>, i.e., <code>analyze('inflammation-01.csv')</code> should produce the graphs already shown, while <code>analyze('inflammation-02.csv')</code> should produce corresponding graphs for the second data set. Be sure to give your function a docstring.</p></li>
<li><p>Write a function <code>rescale</code> that takes an array as input and returns a corresponding array of values scaled to lie in the range 0.0 to 1.0. (If <span class="math">\(L\)</span> and <span class="math">\(H\)</span> are the lowest and highest values in the original array, then the replacement for a value <span class="math">\(v\)</span> should be <span class="math">\((v-L) / (H-L)\)</span>.) Be sure to give the function a docstring.</p></li>
<li><p>Run the commands <code>help(numpy.arange)</code> and <code>help(numpy.linspace)</code> to see how to use these functions to generate regularly-spaced values, then use those values to test your <code>rescale</code> function.</p></li>
</ol>
</div>

### Defining Defaults


<div class="">
<p>We have passed parameters to functions in two ways: directly, as in <code>span(data)</code>, and by name, as in <code>numpy.loadtxt(fname='something.csv', delimiter=',')</code>. In fact, we can pass the filename to <code>loadtxt</code> without the <code>fname=</code>:</p>
</div>


<div class="in">
<pre>numpy.loadtxt(&#39;inflammation-01.csv&#39;, delimiter=&#39;,&#39;)</pre>
</div>

<div class="out">
<pre>array([[ 0.,  0.,  1., ...,  3.,  0.,  0.],
       [ 0.,  1.,  2., ...,  1.,  0.,  1.],
       [ 0.,  1.,  1., ...,  2.,  1.,  1.],
       ..., 
       [ 0.,  1.,  1., ...,  1.,  1.,  1.],
       [ 0.,  0.,  0., ...,  0.,  2.,  0.],
       [ 0.,  0.,  1., ...,  1.,  1.,  0.]])</pre>
</div>


<div class="">
<p>but we still need to say <code>delimiter=</code>:</p>
</div>


<div class="in">
<pre>numpy.loadtxt(&#39;inflammation-01.csv&#39;, &#39;,&#39;)</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
&lt;ipython-input-26-e3bc6cf4fd6a&gt; in &lt;module&gt;()
----&gt; 1 numpy.loadtxt(&#39;inflammation-01.csv&#39;, &#39;,&#39;)

/Users/gwilson/anaconda/lib/python2.7/site-packages/numpy/lib/npyio.pyc in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin)
    775     try:
    776         # Make sure we&#39;re dealing with a proper dtype
--&gt; 777         dtype = np.dtype(dtype)
    778         defconv = _getconv(dtype)
    779 

TypeError: data type &#34;,&#34; not understood</pre>
</div>


<div class="">
<p>To understand what's going on, and make our own functions easier to use, let's re-define our <code>center</code> function like this:</p>
</div>


<div class="in">
<pre>def center(data, desired=0.0):
    &#39;&#39;&#39;Return a new array containing the original data centered around the desired value (0 by default).
    Example: center([1, 2, 3], 0) =&gt; [-1, 0, 1]&#39;&#39;&#39;
    return (data - data.mean()) + desired</pre>
</div>


<div class="">
<p>The key change is that the second parameter is now written <code>desired=0.0</code> instead of just <code>desired</code>. If we call the function with two arguments, it works as it did before:</p>
</div>


<div class="in">
<pre>test_data = numpy.zeros((2, 2))
print center(test_data, 3)</pre>
</div>

<div class="out">
<pre>[[ 3.  3.]
 [ 3.  3.]]
</pre>
</div>


<div class="">
<p>But we can also now call it with just one parameter, in which case <code>desired</code> is automatically assigned the <a href="../../gloss.html#default-parameter-value">default value</a> of 0.0:</p>
</div>


<div class="in">
<pre>more_data = 5 + numpy.zeros((2, 2))
print &#39;data before centering:&#39;, more_data
print &#39;centered data:&#39;, center(more_data)</pre>
</div>

<div class="out">
<pre>data before centering: [[ 5.  5.]
 [ 5.  5.]]
centered data: [[ 0.  0.]
 [ 0.  0.]]
</pre>
</div>


<div class="">
<p>This is handy: if we usually want a function to work one way, but occasionally need it to do something else, we can allow people to pass a parameter when they need to but provide a default to make the normal case easier. The example below shows how Python matches values to parameters:</p>
</div>


<div class="in">
<pre>def display(a=1, b=2, c=3):
    print &#39;a:&#39;, a, &#39;b:&#39;, b, &#39;c:&#39;, c

print &#39;no parameters:&#39;
display()
print &#39;one parameter:&#39;
display(55)
print &#39;two parameters:&#39;
display(55, 66)</pre>
</div>

<div class="out">
<pre>no parameters:
a: 1 b: 2 c: 3
one parameter:
a: 55 b: 2 c: 3
two parameters:
a: 55 b: 66 c: 3
</pre>
</div>


<div class="">
<p>As this example shows, parameters are matched up from left to right, and any that haven't been given a value explicitly get their default value. We can override this behavior by naming the value as we pass it in:</p>
</div>


<div class="in">
<pre>print &#39;only setting the value of c&#39;
display(c=77)</pre>
</div>

<div class="out">
<pre>only setting the value of c
a: 1 b: 2 c: 77
</pre>
</div>


<div class="">
<p>With that in hand, let's look at the help for <code>numpy.loadtxt</code>:</p>
</div>


<div class="in">
<pre>help(numpy.loadtxt)</pre>
</div>

<div class="out">
<pre>Help on function loadtxt in module numpy.lib.npyio:

loadtxt(fname, dtype=&lt;type &#39;float&#39;&gt;, comments=&#39;#&#39;, delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
    Load data from a text file.
    
    Each row in the text file must have the same number of values.
    
    Parameters
    ----------
    fname : file or str
        File, filename, or generator to read.  If the filename extension is
        ``.gz`` or ``.bz2``, the file is first decompressed. Note that
        generators should return byte strings for Python 3k.
    dtype : data-type, optional
        Data-type of the resulting array; default: float.  If this is a
        record data-type, the resulting array will be 1-dimensional, and
        each row will be interpreted as an element of the array.  In this
        case, the number of columns used must match the number of fields in
        the data-type.
    comments : str, optional
        The character used to indicate the start of a comment;
        default: &#39;#&#39;.
    delimiter : str, optional
        The string used to separate values.  By default, this is any
        whitespace.
    converters : dict, optional
        A dictionary mapping column number to a function that will convert
        that column to a float.  E.g., if column 0 is a date string:
        ``converters = {0: datestr2num}``.  Converters can also be used to
        provide a default value for missing data (but see also `genfromtxt`):
        ``converters = {3: lambda s: float(s.strip() or 0)}``.  Default: None.
    skiprows : int, optional
        Skip the first `skiprows` lines; default: 0.
    usecols : sequence, optional
        Which columns to read, with 0 being the first.  For example,
        ``usecols = (1,4,5)`` will extract the 2nd, 5th and 6th columns.
        The default, None, results in all columns being read.
    unpack : bool, optional
        If True, the returned array is transposed, so that arguments may be
        unpacked using ``x, y, z = loadtxt(...)``.  When used with a record
        data-type, arrays are returned for each field.  Default is False.
    ndmin : int, optional
        The returned array will have at least `ndmin` dimensions.
        Otherwise mono-dimensional axes will be squeezed.
        Legal values: 0 (default), 1 or 2.
        .. versionadded:: 1.6.0
    
    Returns
    -------
    out : ndarray
        Data read from the text file.
    
    See Also
    --------
    load, fromstring, fromregex
    genfromtxt : Load data with missing values handled as specified.
    scipy.io.loadmat : reads MATLAB data files
    
    Notes
    -----
    This function aims to be a fast reader for simply formatted files.  The
    `genfromtxt` function provides more sophisticated handling of, e.g.,
    lines with missing values.
    
    Examples
    --------
    &gt;&gt;&gt; from StringIO import StringIO   # StringIO behaves like a file object
    &gt;&gt;&gt; c = StringIO(&#34;0 1\n2 3&#34;)
    &gt;&gt;&gt; np.loadtxt(c)
    array([[ 0.,  1.],
           [ 2.,  3.]])
    
    &gt;&gt;&gt; d = StringIO(&#34;M 21 72\nF 35 58&#34;)
    &gt;&gt;&gt; np.loadtxt(d, dtype={&#39;names&#39;: (&#39;gender&#39;, &#39;age&#39;, &#39;weight&#39;),
    ...                      &#39;formats&#39;: (&#39;S1&#39;, &#39;i4&#39;, &#39;f4&#39;)})
    array([(&#39;M&#39;, 21, 72.0), (&#39;F&#39;, 35, 58.0)],
          dtype=[(&#39;gender&#39;, &#39;|S1&#39;), (&#39;age&#39;, &#39;&lt;i4&#39;), (&#39;weight&#39;, &#39;&lt;f4&#39;)])
    
    &gt;&gt;&gt; c = StringIO(&#34;1,0,2\n3,0,4&#34;)
    &gt;&gt;&gt; x, y = np.loadtxt(c, delimiter=&#39;,&#39;, usecols=(0, 2), unpack=True)
    &gt;&gt;&gt; x
    array([ 1.,  3.])
    &gt;&gt;&gt; y
    array([ 2.,  4.])

</pre>
</div>


<div class="">
<p>There's a lot of information here, but the most important part is the first couple of lines:</p>
<pre class="sourceCode python"><code class="sourceCode python">loadtxt(fname, dtype=&lt;<span class="dt">type</span> <span class="st">&#39;float&#39;</span>&gt;, comments=<span class="st">&#39;#&#39;</span>, delimiter=<span class="ot">None</span>, converters=<span class="ot">None</span>, skiprows=<span class="dv">0</span>, usecols=<span class="ot">None</span>,
        unpack=<span class="ot">False</span>, ndmin=<span class="dv">0</span>)</code></pre>
<p>This tells us that <code>loadtxt</code> has one parameter called <code>fname</code> that doesn't have a default value, and eight others that do. If we call the function like this:</p>
<pre class="sourceCode python"><code class="sourceCode python">numpy.loadtxt(<span class="st">&#39;inflammation-01.csv&#39;</span>, <span class="st">&#39;,&#39;</span>)</code></pre>
<p>then the filename is assigned to <code>fname</code> (which is what we want), but the delimiter string <code>','</code> is assigned to <code>dtype</code> rather than <code>delimiter</code>, because <code>dtype</code> is the second parameter in the list. That's why we don't have to provide <code>fname=</code> for the filename, but <em>do</em> have to provide <code>delimiter=</code> for the second parameter.</p>
</div>


<div class="challenges">
<h4 id="challenges">Challenges</h4>
<ol style="list-style-type: decimal">
<li>Rewrite the <code>normalize</code> function so that it scales data to lie between 0.0 and 1.0 by default, but will allow the caller to specify lower and upper bounds if they want. Compare your implementation to your neighbor's: do the two functions always behave the same way?</li>
</ol>
</div>


<div class="keypoints">
<h4 id="key-points">Key Points</h4>
<ul>
<li>Define a function using <code>def name(...params...)</code>.</li>
<li>The body of a function must be indented.</li>
<li>Call a function using <code>name(...values...)</code>.</li>
<li>Numbers are stored as integers or floating-point numbers.</li>
<li>Integer division produces the whole part of the answer (not the fractional part).</li>
<li>Each time a function is called, a new stack frame is created on the <a href="../../gloss.html#call-stack">call stack</a> to hold its parameters and local variables.</li>
<li>Python looks for variables in the current stack frame before looking for them at the top level.</li>
<li>Use <code>help(thing)</code> to view help for something.</li>
<li>Put docstrings in functions to provide help for that function.</li>
<li>Specify default values for parameters when defining a function using <code>name=value</code> in the parameter list.</li>
<li>Parameters can be passed by matching based on name, by position, or by omitting them (in which case the default value is used).</li>
</ul>
</div>


<div class="">
<h4 id="next-steps">Next Steps</h4>
<p>We now have a function called <code>analyze</code> to visualize a single data set. We could use it to explore all 12 of our current data sets like this:</p>
<pre class="sourceCode python"><code class="sourceCode python">analyze(<span class="st">&#39;inflammation-01.csv&#39;</span>)
analyze(<span class="st">&#39;inflammation-02.csv&#39;</span>)
...
analyze(<span class="st">&#39;inflammation-12.csv&#39;</span>)</code></pre>
<p>but the chances of us typing all 12 filenames correctly aren't great, and we'll be even worse off if we get another hundred files. What we need is a way to tell Python to do something once for each file, and that will be the subject of the next lesson.</p>
</div>
