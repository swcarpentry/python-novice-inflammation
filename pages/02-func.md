---
layout: lesson
root: ../..
---

## Creating Functions


If we only had one data set to analyze,
it would probably be faster to load the file into a spreadsheet
and use that to plot some simple statistics.
But we have twelve files to check,
and may have more in future.
In this lesson,
we'll learn how to write a function
so that we can repeat several operations with a single command.


<div class="objectives" markdown="1">
#### Objectives

*   Define a function that takes parameters.
*   Return a value from a function.
*   Test and debug a function.
*   Explain what a call stack is, and trace changes to the call stack as functions are called.
*   Set default values for function parameters.
*   Explain why we should divide programs into small, single-purpose functions.
</div>

### Defining a Function


Let's start by defining a function `fahr_to_kelvin` that converts temperatures from Fahrenheit to Kelvin:


<pre class="in"><code>def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15</code></pre>


The definition opens with the word `def`,
which is followed by the name of the function
and a parenthesized list of parameter names.
The [body](../../gloss.html#function-body) of the function&mdash;the
statements that are executed when it runs&mdash;is indented below the definition line,
typically by four spaces.

When we call the function,
the values we pass to it are assigned to those variables
so that we can use them inside the function.
Inside the function,
we use a [return statement](../../gloss.html#return-statement) to send a result back to whoever asked for it.

Let's try running our function.
Calling our own function is no different from calling any other function:


<pre class="in"><code>print &#39;freezing point of water:&#39;, fahr_to_kelvin(32)
print &#39;boiling point of water:&#39;, fahr_to_kelvin(212)</code></pre>

<div class="out"><pre class='out'><code>freezing point of water: 273.15
boiling point of water: 273.15
</code></pre></div>


We've successfully called the function that we defined,
and we have access to the value that we returned.
Unfortunately, the value returned doesn't look right.
What went wrong?

### Debugging a Function


*Debugging* is when we fix a piece of code
that we know is working incorrectly.
In this case, we know that `fahr_to_kelvin`
is giving us the wrong answer,
so let's find out why.

For big pieces of code,
there are tools called *debuggers* that aid in this process.

We just have a short function,
so we'll debug by choosing some parameter value,
breaking our function into small parts,
and printing out the value of each part.


<pre class="in"><code># We&#39;ll use temp = 212, the boiling point of water, which was incorrect
print &#34;212 - 32:&#34;, 212 - 32</code></pre>

<div class="out"><pre class='out'><code>212 - 32: 180
</code></pre></div>


<pre class="in"><code>print &#34;(212 - 32) * (5/9):&#34;, (212 - 32) * (5/9)</code></pre>

<div class="out"><pre class='out'><code>(212 - 32) * (5/9): 0
</code></pre></div>


Aha! The problem comes when we multiply by `5/9`.
This is because `5/9` is actually 0.


<pre class="in"><code>5/9</code></pre>

<div class="out"><pre class='out'><code>0</code></pre></div>


Computers store numbers in one of two ways:
as [integers](../../gloss.html#integer)
or as [floating-point numbers](../../gloss.html#float-point-number) (or floats).
The first are the numbers we usually count with;
the second have fractional parts.
Addition, subtraction and multiplication work on both as we'd expect,
but division works differently.
If we divide one integer by another,
we get the quotient without the remainder:


<pre class="in"><code>print &#39;10/3 is:&#39;, 10/3</code></pre>

<div class="out"><pre class='out'><code>10/3 is: 3
</code></pre></div>


If either part of the division is a float,
on the other hand,
the computer creates a floating-point answer:


<pre class="in"><code>print &#39;10.0/3 is:&#39;, 10.0/3</code></pre>

<div class="out"><pre class='out'><code>10.0/3 is: 3.33333333333
</code></pre></div>


The computer does this for historical reasons:
integer operations were much faster on early machines,
and this behavior is actually useful in a lot of situations.
It's still confusing,
though,
so Python 3 produces a floating-point answer when dividing integers if it needs to.
We're still using Python 2.7 in this class,
though,
so if we want `5/9` to give us the right answer,
we have to write it as `5.0/9`, `5/9.0`, or some other variation.

Another way to create a floating-point answer is to explicitly tell the computer that you desire one. This is achieved by casting one of the numbers:


<pre class="in"><code>print &#39;float(10)/3 is:&#39;, float(10)/3</code></pre>

<div class="out"><pre class='out'><code>float(10)/3 is: 3.33333333333
</code></pre></div>


The advantage to this method is it can be used with existing variables. Let's take a look:


<pre class="in"><code>a = 10
b = 3
print &#39;a/b is:&#39;, a/b
print &#39;float(a)/b is:&#39;, float(a)/b</code></pre>

<div class="out"><pre class='out'><code>a/b is: 3
float(a)/b is: 3.33333333333
</code></pre></div>


See that was much easier than redefining `a` or `b`!

Let's fix our `fahr_to_kelvin` function with this new knowledge.


<pre class="in"><code>def fahr_to_kelvin(temp):
    return ((temp - 32) * (5.0/9.0)) + 273.15

print &#39;freezing point of water:&#39;, fahr_to_kelvin(32)
print &#39;boiling point of water:&#39;, fahr_to_kelvin(212)</code></pre>

<div class="out"><pre class='out'><code>freezing point of water: 273.15
boiling point of water: 373.15
</code></pre></div>


It works!

### Composing Functions


Now that we've seen how to turn Fahrenheit into Kelvin,
it's easy to turn Kelvin into Celsius:


<pre class="in"><code>def kelvin_to_celsius(temp):
    return temp - 273.15

print &#39;absolute zero in Celsius:&#39;, kelvin_to_celsius(0.0)</code></pre>

<div class="out"><pre class='out'><code>absolute zero in Celsius: -273.15
</code></pre></div>


What about converting Fahrenheit to Celsius?
We could write out the formula,
but we don't need to.
Instead,
we can [compose](../../gloss.html#function-composition) the two functions we have already created:


<pre class="in"><code>def fahr_to_celsius(temp):
    temp_k = fahr_to_kelvin(temp)
    result = kelvin_to_celsius(temp_k)
    return result

print &#39;freezing point of water in Celsius:&#39;, fahr_to_celsius(32.0)</code></pre>

<div class="out"><pre class='out'><code>freezing point of water in Celsius: 0.0
</code></pre></div>


This is our first taste of how larger programs are built:
we define basic operations,
then combine them in ever-large chunks to get the effect we want.
Real-life functions will usually be larger than the ones shown here&mdash;typically half a dozen to a few dozen lines&mdash;but
they shouldn't ever be much longer than that,
or the next person who reads it won't be able to understand what's going on.


<div class="challenges" markdown="1">
#### Challenges

1.  "Adding" two strings produces their concatention:
    `'a' + 'b'` is `'ab'`.
    Write a function called `fence` that takes two parameters called `original` and `wrapper`
    and returns a new string that has the wrapper character at the beginning and end of the original:

    ~~~python
    print fence('name', '*')
    *name*
    ~~~

1.  If the variable `s` refers to a string,
    then `s[0]` is the string's first character
    and `s[-1]` is its last.
    Write a function called `outer`
    that returns a string made up of just the first and last characters of its input:

    ~~~python
    print outer('helium')
    hm
    ~~~
</div>

### The Call Stack


Let's take a closer look at what happens when we call `fahr_to_celsius(32.0)`.
To make things clearer,
we'll start by putting the initial value 32.0 in a variable
and store the final result in one as well:


<pre class="in"><code>original = 32.0
final = fahr_to_celsius(original)</code></pre>


The diagram below shows what memory looks like after the first line has been executed:


<img src="img/python-call-stack-01.svg" alt="Call Stack (Initial State)" />


When we call `fahr_to_celsius`,
Python *doesn't* create the variable `temp` right away.
Instead,
it creates something called a [stack frame](../../gloss.html#stack-frame)
to keep track of the variables defined by `fahr_to_kelvin`.
Initially,
this stack frame only holds the value of `temp`:


<img src="img/python-call-stack-02.svg" alt="Call Stack Immediately After First Function Call" />


When we call `fahr_to_kelvin` inside `fahr_to_celsius`,
Python creates another stack frame to hold `fahr_to_kelvin`'s variables:


<img src="img/python-call-stack-03.svg" alt="Call Stack During First Nested Function Call" />


It does this because there are now two variables in play called `temp`:
the parameter to `fahr_to_celsius`,
and the parameter to `fahr_to_kelvin`.
Having two variables with the same name in the same part of the program would be ambiguous,
so Python (and every other modern programming language) creates a new stack frame for each function call
to keep that function's variables separate from those defined by other functions.

When the call to `fahr_to_kelvin` returns a value,
Python throws away `fahr_to_kelvin`'s stack frame
and creates a new variable in the stack frame for `fahr_to_celsius` to hold the temperature in Kelvin:


<img src="img/python-call-stack-04.svg" alt="Call Stack After Return From First Nested Function Call" />


It then calls `kelvin_to_celsius`,
which means it creates a stack frame to hold that function's variables:


<img src="img/python-call-stack-05.svg" alt="Call Stack During Call to Second Nested Function" />


Once again,
Python throws away that stack frame when `kelvin_to_celsius` is done
and creates the variable `result` in the stack frame for `fahr_to_celsius`:


<img src="img/python-call-stack-06.svg" alt="Call Stack After Second Nested Function Returns" />


Finally,
when `fahr_to_celsius` is done,
Python throws away *its* stack frame
and puts its result in a new variable called `final`
that lives in the stack frame we started with:


<img src="img/python-call-stack-07.svg" alt="Call Stack After All Functions Have Finished" />


This final stack frame is always there;
it holds the variables we defined outside the functions in our code.
What it *doesn't* hold is the variables that were in the various stack frames.
If we try to get the value of `temp` after our functions have finished running,
Python tells us that there's no such thing:


<pre class="in"><code>print &#39;final value of temp after all function calls:&#39;, temp</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-12-ffd9b4dbd5f1&gt; in &lt;module&gt;()
----&gt; 1 print &#39;final value of temp after all function calls:&#39;, temp

NameError: name &#39;temp&#39; is not defined</code></pre><pre class='out'><code>final value of temp after all function calls:</code></pre></div>


Why go to all this trouble?
Well,
here's a function called `span` that calculates the difference between
the mininum and maximum values in an array:


<pre class="in"><code>import numpy

def span(a):
    diff = a.max() - a.min()
    return diff

data = numpy.loadtxt(fname=&#39;inflammation-01.csv&#39;, delimiter=&#39;,&#39;)
print &#39;span of data&#39;, span(data)</code></pre>

<div class="out"><pre class='out'><code> span of data 20.0
</code></pre></div>


Notice that `span` assigns a value to a variable called `diff`.
We might very well use a variable with the same name to hold data:


<pre class="in"><code>diff = numpy.loadtxt(fname=&#39;inflammation-01.csv&#39;, delimiter=&#39;,&#39;)
print &#39;span of data:&#39;, span(diff)</code></pre>

<div class="out"><pre class='out'><code>span of data: 20.0
</code></pre></div>


We don't expect `diff` to have the value 20.0 after this function call,
so the name `diff` cannot refer to the same thing inside `span` as it does in the main body of our program.
And yes,
we could probably choose a different name than `diff` in our main program in this case,
but we don't want to have to read every line of NumPy to see what variable names its functions use
before calling any of those functions,
just in case they change the values of our variables.


The big idea here is [encapsulation](../../gloss.html#encapsulation),
and it's the key to writing correct, comprehensible programs.
A function's job is to turn several operations into one
so that we can think about a single function call
instead of a dozen or a hundred statements
each time we want to do something.
That only works if functions don't interfere with each other;
if they do,
we have to pay attention to the details once again,
which quickly overloads our short-term memory.


<div class="challenges" markdown="1">
#### Challenges

1.  We previously wrote functions called `fence` and `outer`.
    Draw a diagram showing how the call stack changes when we run the following:
    
    ~~~python
    print outer(fence('carbon', '+'))
    ~~~
</div>

### Testing and Documenting


Once we start putting things in functions so that we can re-use them,
we need to start testing that those functions are working correctly.
To see how to do this,
let's write a function to center a dataset around a particular value:


<pre class="in"><code>def center(data, desired):
    return (data - data.mean()) + desired</code></pre>


We could test this on our actual data,
but since we don't know what the values ought to be,
it will be hard to tell if the result was correct.
Instead,
let's use NumPy to create a matrix of 0's
and then center that around 3:


<pre class="in"><code>z = numpy.zeros((2,2))
print center(z, 3)</code></pre>

<div class="out"><pre class='out'><code>[[ 3.  3.]
 [ 3.  3.]]
</code></pre></div>


That looks right,
so let's try `center` on our real data:


<pre class="in"><code>data = numpy.loadtxt(fname=&#39;inflammation-01.csv&#39;, delimiter=&#39;,&#39;)
print center(data, 0)</code></pre>

<div class="out"><pre class='out'><code>[[-6.14875 -6.14875 -5.14875 ..., -3.14875 -6.14875 -6.14875]
 [-6.14875 -5.14875 -4.14875 ..., -5.14875 -6.14875 -5.14875]
 [-6.14875 -5.14875 -5.14875 ..., -4.14875 -5.14875 -5.14875]
 ..., 
 [-6.14875 -5.14875 -5.14875 ..., -5.14875 -5.14875 -5.14875]
 [-6.14875 -6.14875 -6.14875 ..., -6.14875 -4.14875 -6.14875]
 [-6.14875 -6.14875 -5.14875 ..., -5.14875 -5.14875 -6.14875]]
</code></pre></div>


It's hard to tell from the default output whether the result is correct,
but there are a few simple tests that will reassure us:


<pre class="in"><code>print &#39;original min, mean, and max are:&#39;, data.min(), data.mean(), data.max()
centered = center(data, 0)
print &#39;min, mean, and and max of centered data are:&#39;, centered.min(), centered.mean(), centered.max()</code></pre>

<div class="out"><pre class='out'><code>original min, mean, and max are: 0.0 6.14875 20.0
min, mean, and and max of centered data are: -6.14875 -3.49054118942e-15 13.85125
</code></pre></div>


That seems almost right:
the original mean was about 6.1,
so the lower bound from zero is how about -6.1.
The mean of the centered data isn't quite zero&mdash;we'll explore why not in the challenges&mdash;but it's pretty close.
We can even go further and check that the standard deviation hasn't changed:


<pre class="in"><code>print &#39;std dev before and after:&#39;, data.std(), centered.std()</code></pre>

<div class="out"><pre class='out'><code>std dev before and after: 4.61383319712 4.61383319712
</code></pre></div>


Those values look the same,
but we probably wouldn't notice if they were different in the sixth decimal place.
Let's do this instead:


<pre class="in"><code>print &#39;difference in standard deviations before and after:&#39;, data.std() - centered.std()</code></pre>

<div class="out"><pre class='out'><code>difference in standard deviations before and after: -3.5527136788e-15
</code></pre></div>


Again,
the difference is very small.
It's still possible that our function is wrong,
but it seems unlikely enough that we should probably get back to doing our analysis.
We have one more task first, though:
we should write some [documentation](../../gloss.html#documentation) for our function
to remind ourselves later what it's for and how to use it.

The usual way to put documentation in software is to add [comments](../../gloss.html#comment) like this:


<pre class="in"><code># center(data, desired): return a new array containing the original data centered around the desired value.
def center(data, desired):
    return (data - data.mean()) + desired</code></pre>


There's a better way, though.
If the first thing in a function is a string that isn't assigned to a variable,
that string is attached to the function as its documentation:


<pre class="in"><code>def center(data, desired):
    &#39;&#39;&#39;Return a new array containing the original data centered around the desired value.&#39;&#39;&#39;
    return (data - data.mean()) + desired</code></pre>


This is better because we can now ask Python's built-in help system to show us the documentation for the function:


<pre class="in"><code>help(center)</code></pre>

<div class="out"><pre class='out'><code>Help on function center in module __main__:

center(data, desired)
    Return a new array containing the original data centered around the desired value.

</code></pre></div>


A string like this is called a [docstring](../../gloss.html#docstring).
We don't need to use triple quotes when we write one,
but if we do,
we can break the string across multiple lines:


<pre class="in"><code>def center(data, desired):
    &#39;&#39;&#39;Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) =&gt; [-1, 0, 1]&#39;&#39;&#39;
    return (data - data.mean()) + desired

help(center)</code></pre>

<div class="out"><pre class='out'><code>Help on function center in module __main__:

center(data, desired)
    Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) =&gt; [-1, 0, 1]

</code></pre></div>


<div class="challenges" markdown="1">
#### Challenges

1.  Write a function called `analyze` that takes a filename as a parameter
    and displays the three graphs produced in the [previous lesson](01-numpy.ipynb),
    i.e.,
    `analyze('inflammation-01.csv')` should produce the graphs already shown,
    while `analyze('inflammation-02.csv')` should produce corresponding graphs for the second data set.
    Be sure to give your function a docstring.

2.  Write a function `rescale` that takes an array as input
    and returns a corresponding array of values scaled to lie in the range 0.0 to 1.0.
    (If $L$ and $H$ are the lowest and highest values in the original array,
    then the replacement for a value $v$ should be $(v-L) / (H-L)$.)
    Be sure to give the function a docstring.

3.  Run the commands `help(numpy.arange)` and `help(numpy.linspace)`
    to see how to use these functions to generate regularly-spaced values,
    then use those values to test your `rescale` function.
</div>

### Defining Defaults


We have passed parameters to functions in two ways:
directly, as in `span(data)`,
and by name, as in `numpy.loadtxt(fname='something.csv', delimiter=',')`.
In fact,
we can pass the filename to `loadtxt` without the `fname=`:


<pre class="in"><code>numpy.loadtxt(&#39;inflammation-01.csv&#39;, delimiter=&#39;,&#39;)</code></pre>

<div class="out"><pre class='out'><code>array([[ 0.,  0.,  1., ...,  3.,  0.,  0.],
       [ 0.,  1.,  2., ...,  1.,  0.,  1.],
       [ 0.,  1.,  1., ...,  2.,  1.,  1.],
       ..., 
       [ 0.,  1.,  1., ...,  1.,  1.,  1.],
       [ 0.,  0.,  0., ...,  0.,  2.,  0.],
       [ 0.,  0.,  1., ...,  1.,  1.,  0.]])</code></pre></div>


but we still need to say `delimiter=`:


<pre class="in"><code>numpy.loadtxt(&#39;inflammation-01.csv&#39;, &#39;,&#39;)</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
&lt;ipython-input-26-e3bc6cf4fd6a&gt; in &lt;module&gt;()
----&gt; 1 numpy.loadtxt(&#39;inflammation-01.csv&#39;, &#39;,&#39;)

/Users/gwilson/anaconda/lib/python2.7/site-packages/numpy/lib/npyio.pyc in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin)
    775     try:
    776         # Make sure we&#39;re dealing with a proper dtype
--&gt; 777         dtype = np.dtype(dtype)
    778         defconv = _getconv(dtype)
    779 

TypeError: data type &#34;,&#34; not understood</code></pre></div>


To understand what's going on,
and make our own functions easier to use,
let's re-define our `center` function like this:


<pre class="in"><code>def center(data, desired=0.0):
    &#39;&#39;&#39;Return a new array containing the original data centered around the desired value (0 by default).
    Example: center([1, 2, 3], 0) =&gt; [-1, 0, 1]&#39;&#39;&#39;
    return (data - data.mean()) + desired</code></pre>


The key change is that the second parameter is now written `desired=0.0` instead of just `desired`.
If we call the function with two arguments,
it works as it did before:


<pre class="in"><code>test_data = numpy.zeros((2, 2))
print center(test_data, 3)</code></pre>

<div class="out"><pre class='out'><code>[[ 3.  3.]
 [ 3.  3.]]
</code></pre></div>


But we can also now call it with just one parameter,
in which case `desired` is automatically assigned the [default value](../../gloss.html#default-parameter-value) of 0.0:


<pre class="in"><code>more_data = 5 + numpy.zeros((2, 2))
print &#39;data before centering:&#39;, more_data
print &#39;centered data:&#39;, center(more_data)</code></pre>

<div class="out"><pre class='out'><code>data before centering: [[ 5.  5.]
 [ 5.  5.]]
centered data: [[ 0.  0.]
 [ 0.  0.]]
</code></pre></div>


This is handy:
if we usually want a function to work one way,
but occasionally need it to do something else,
we can allow people to pass a parameter when they need to
but provide a default to make the normal case easier.
The example below shows how Python matches values to parameters:


<pre class="in"><code>def display(a=1, b=2, c=3):
    print &#39;a:&#39;, a, &#39;b:&#39;, b, &#39;c:&#39;, c

print &#39;no parameters:&#39;
display()
print &#39;one parameter:&#39;
display(55)
print &#39;two parameters:&#39;
display(55, 66)</code></pre>

<div class="out"><pre class='out'><code>no parameters:
a: 1 b: 2 c: 3
one parameter:
a: 55 b: 2 c: 3
two parameters:
a: 55 b: 66 c: 3
</code></pre></div>


As this example shows,
parameters are matched up from left to right,
and any that haven't been given a value explicitly get their default value.
We can override this behavior by naming the value as we pass it in:


<pre class="in"><code>print &#39;only setting the value of c&#39;
display(c=77)</code></pre>

<div class="out"><pre class='out'><code>only setting the value of c
a: 1 b: 2 c: 77
</code></pre></div>


With that in hand,
let's look at the help for `numpy.loadtxt`:


<pre class="in"><code>help(numpy.loadtxt)</code></pre>

<div class="out"><pre class='out'><code>Help on function loadtxt in module numpy.lib.npyio:

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

</code></pre></div>


There's a lot of information here,
but the most important part is the first couple of lines:

~~~python
loadtxt(fname, dtype=<type 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None,
        unpack=False, ndmin=0)
~~~

This tells us that `loadtxt` has one parameter called `fname` that doesn't have a default value,
and eight others that do.
If we call the function like this:

~~~python
numpy.loadtxt('inflammation-01.csv', ',')
~~~

then the filename is assigned to `fname` (which is what we want),
but the delimiter string `','` is assigned to `dtype` rather than `delimiter`,
because `dtype` is the second parameter in the list.
That's why we don't have to provide `fname=` for the filename,
but *do* have to provide `delimiter=` for the second parameter.


<div class="challenges" markdown="1">
#### Challenges

1.  Rewrite the `rescale` function so that it scales data to lie between 0.0 and 1.0 by default,
    but will allow the caller to specify lower and upper bounds if they want.
    Compare your implementation to your neighbor's:
    do the two functions always behave the same way?
</div>


<div class="keypoints" markdown="1">
#### Key Points

*   Define a function using `def name(...params...)`.
*   The body of a function must be indented.
*   Call a function using `name(...values...)`.
*   Numbers are stored as integers or floating-point numbers.
*   Integer division produces the whole part of the answer (not the fractional part).
*   Each time a function is called, a new stack frame is created on the [call stack](../../gloss.html#call-stack) to hold its parameters and local variables.
*   Python looks for variables in the current stack frame before looking for them at the top level.
*   Use `help(thing)` to view help for something.
*   Put docstrings in functions to provide help for that function.
*   Specify default values for parameters when defining a function using `name=value` in the parameter list.
*   Parameters can be passed by matching based on name, by position, or by omitting them (in which case the default value is used).
</div>


#### Next Steps

We now have a function called `analyze` to visualize a single data set.
We could use it to explore all 12 of our current data sets like this:

~~~python
analyze('inflammation-01.csv')
analyze('inflammation-02.csv')
...
analyze('inflammation-12.csv')
~~~

but the chances of us typing all 12 filenames correctly aren't great,
and we'll be even worse off if we get another hundred files.
What we need is a way to tell Python to do something once for each file,
and that will be the subject of the next lesson.
