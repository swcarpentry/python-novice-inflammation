---
layout: page
title: Programming with Python
subtitle: Creating Functions
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Define a function that takes parameters.
> *   Return a value from a function.
> *   Test and debug a function.
> *   Explain what a call stack is, and trace changes to the call stack as functions are called.
> *   Set default values for function parameters.
> *   Explain why we should divide programs into small, single-purpose functions.

If we only had one data set to analyze,
it would probably be faster to load the file into a spreadsheet
and use that to plot some simple statistics.
But we have twelve files to check,
and may have more in future.
In this lesson,
we'll learn how to write a function
so that we can repeat several operations with a single command.

Let's start by defining a function `fahr_to_kelvin` that converts temperatures from Fahrenheit to Kelvin:

def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15
~~~

The definition opens with the word `def`,
which is followed by the name of the function
and a parenthesized list of parameter names.
The **body** of the function --- the
statements that are executed when it runs --- is indented below the definition line,
typically by four spaces.

When we call the function,
the values we pass to it are assigned to those variables
so that we can use them inside the function.
Inside the function,
we use a **return statement** to send a result back to whoever asked for it.

Let's try running our function.
Calling our own function is no different from calling any other function:

~~~ {.python}
print 'freezing point of water:', fahr_to_kelvin(32)
print 'boiling point of water:', fahr_to_kelvin(212)
~~~
~~~ {.output}
freezing point of water: 273.15
boiling point of water: 273.15
~~~

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
Since we just have a short function,
we'll debug by choosing some parameter value,
breaking our function into small parts,
and printing out the value of each part.

~~~ {.python}
# We'll use temp = 212, the boiling point of water, which was incorrect
print "212 - 32:", 212 - 32
~~~
~~~ {.output}
212 - 32: 180
~~~

~~~ {.python}
print "(212 - 32) * (5/9):", (212 - 32) * (5/9)
~~~
~~~ {.output}
(212 - 32) * (5/9): 0
~~~

Aha! The problem comes when we multiply by `5/9`.
This is because `5/9` is actually 0.

~~~ {.python}
5/9
~~~
~~~ {.output}
0
~~~

Computers store numbers in one of two ways:
as **integers**
or as **floating-point numbers** (or floats).
The first are the numbers we usually count with;
the second have fractional parts.
Addition, subtraction and multiplication work on both as we'd expect,
but division works differently.
If we divide one integer by another,
we get the quotient without the remainder:

~~~ {.python}
print '10/3 is:', 10/3
~~~
~~~ {.output}
10/3 is: 3
~~~

If either part of the division is a float,
on the other hand,
the computer creates a floating-point answer:

~~~ {.python}
print '10.0/3 is:', 10.0/3
~~~
~~~ {.output}
10.0/3 is: 3.33333333333
~~~

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

Another way to create a floating-point answer
is to explicitly tell the computer that you desire one.
This is achieved by **casting** one of the numbers:

~~~ {.python}
print 'float(10)/3 is:', float(10)/3
~~~
~~~ {.output}
float(10)/3 is: 3.33333333333
~~~

The advantage to this method is it can be used with existing variables.
Let's take a look:

~~~ {.python}
a = 10
b = 3
print 'a/b is:', a/b
print 'float(a)/b is:', float(a)/b
~~~
~~~ {.output}
a/b is: 3
float(a)/b is: 3.33333333333
~~~

Let's fix our `fahr_to_kelvin` function with this new knowledge:

~~~ {.python}
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5.0/9.0)) + 273.15

print 'freezing point of water:', fahr_to_kelvin(32)
print 'boiling point of water:', fahr_to_kelvin(212)
~~~
~~~ {.output}
freezing point of water: 273.15
boiling point of water: 373.15
~~~

## Composing Functions

Now that we've seen how to turn Fahrenheit into Kelvin,
it's easy to turn Kelvin into Celsius:

~~~ {.python}
def kelvin_to_celsius(temp):
    return temp - 273.15

print 'absolute zero in Celsius:', kelvin_to_celsius(0.0)
~~~
~~~ {.output}
absolute zero in Celsius: -273.15
~~~

What about converting Fahrenheit to Celsius?
We could write out the formula,
but we don't need to.
Instead,
we can **compose** the two functions we have already created:

~~~ {.python}
def fahr_to_celsius(temp):
    temp_k = fahr_to_kelvin(temp)
    result = kelvin_to_celsius(temp_k)
    return result

print 'freezing point of water in Celsius:', fahr_to_celsius(32.0)
~~~
~~~ {.output}
freezing point of water in Celsius: 0.0
~~~

This is our first taste of how larger programs are built:
we define basic operations,
then combine them in ever-large chunks to get the effect we want.
Real-life functions will usually be larger than the ones shown here --- typically half a dozen to a few dozen lines --- but
they shouldn't ever be much longer than that,
or the next person who reads it won't be able to understand what's going on.

## The Call Stack

Let's take a closer look at what happens when we call `fahr_to_celsius(32.0)`.
To make things clearer,
we'll start by putting the initial value 32.0 in a variable
and store the final result in one as well:

~~~ {.python}
original = 32.0
final = fahr_to_celsius(original)
~~~

The diagram below shows what memory looks like after the first line has been executed:

<img src="img/python-call-stack-01.svg" alt="Call Stack (Initial State)" />

When we call `fahr_to_celsius`,
Python *doesn't* create the variable `temp` right away.
Instead,
it creates something called a **stack frame**
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

~~~ {.python}
print 'final value of temp after all function calls:', temp
~~~
~~~ {.error}
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-12-ffd9b4dbd5f1> in <module>()
----> 1 print 'final value of temp after all function calls:', temp

NameError: name 'temp' is not defined
~~~
~~~ {.output}
final value of temp after all function calls:
~~~

Why go to all this trouble?
Well,
here's a function called `span` that calculates the difference between
the mininum and maximum values in an array:

~~~ {.python}
import numpy

def span(a):
    diff = a.max() - a.min()
    return diff

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print 'span of data', span(data)
~~~
~~~ {.output}
 span of data 20.0
~~~

Notice that `span` assigns a value to a variable called `diff`.
We might very well use a variable with the same name to hold data:

~~~ {.python}
diff = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print 'span of data:', span(diff)
~~~
~~~ {.output}
span of data: 20.0
~~~

We don't expect `diff` to have the value 20.0 after this function call,
so the name `diff` cannot refer to the same thing inside `span` as it does in the main body of our program.
And yes,
we could probably choose a different name than `diff` in our main program in this case,
but we don't want to have to read every line of NumPy to see what variable names its functions use
before calling any of those functions,
just in case they change the values of our variables.

The big idea here is **encapsulation**,
and it's the key to writing correct, comprehensible programs.
A function's job is to turn several operations into one
so that we can think about a single function call
instead of a dozen or a hundred statements
each time we want to do something.
That only works if functions don't interfere with each other;
if they do,
we have to pay attention to the details once again,
which quickly overloads our short-term memory.

## Testing and Documenting

Once we start putting things in functions so that we can re-use them,
we need to start testing that those functions are working correctly.
To see how to do this,
let's write a function to center a dataset around a particular value:

~~~ {.python}
def center(data, desired):
    return (data - data.mean()) + desired
~~~

We could test this on our actual data,
but since we don't know what the values ought to be,
it will be hard to tell if the result was correct.
Instead,
let's use NumPy to create a matrix of 0's
and then center that around 3:

~~~ {.python}
z = numpy.zeros((2,2))
print center(z, 3)
~~~
~~~ {.output}
[[ 3.  3.]
 [ 3.  3.]]
~~~

That looks right,
so let's try `center` on our real data:

~~~ {.python}
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print center(data, 0)
~~~
~~~ {.output}
[[-6.14875 -6.14875 -5.14875 ..., -3.14875 -6.14875 -6.14875]
 [-6.14875 -5.14875 -4.14875 ..., -5.14875 -6.14875 -5.14875]
 [-6.14875 -5.14875 -5.14875 ..., -4.14875 -5.14875 -5.14875]
 ..., 
 [-6.14875 -5.14875 -5.14875 ..., -5.14875 -5.14875 -5.14875]
 [-6.14875 -6.14875 -6.14875 ..., -6.14875 -4.14875 -6.14875]
 [-6.14875 -6.14875 -5.14875 ..., -5.14875 -5.14875 -6.14875]]
~~~

It's hard to tell from the default output whether the result is correct,
but there are a few simple tests that will reassure us:

~~~ {.python}
print 'original min, mean, and max are:', data.min(), data.mean(), data.max()
centered = center(data, 0)
print 'min, mean, and and max of centered data are:', centered.min(), centered.mean(), centered.max()
~~~
~~~ {.output}
original min, mean, and max are: 0.0 6.14875 20.0
min, mean, and and max of centered data are: -6.14875 -3.49054118942e-15 13.85125
~~~

That seems almost right:
the original mean was about 6.1,
so the lower bound from zero is how about -6.1.
The mean of the centered data isn't quite zero --- we'll explore why not in the challenges --- but it's pretty close.
We can even go further and check that the standard deviation hasn't changed:

~~~ {.python}
print 'std dev before and after:', data.std(), centered.std()
~~~
~~~ {.output}
std dev before and after: 4.61383319712 4.61383319712
~~~

Those values look the same,
but we probably wouldn't notice if they were different in the sixth decimal place.
Let's do this instead:

~~~ {.python}
print 'difference in standard deviations before and after:', data.std() - centered.std()
~~~
~~~ {.output}
difference in standard deviations before and after: -3.5527136788e-15
~~~

Again,
the difference is very small.
It's still possible that our function is wrong,
but it seems unlikely enough that we should probably get back to doing our analysis.
We have one more task first, though:
we should write some **documentation** for our function
to remind ourselves later what it's for and how to use it.

The usual way to put documentation in software is to add **comments** like this:

~~~ {.python}
# center(data, desired): return a new array containing the original data centered around the desired value.
def center(data, desired):
    return (data - data.mean()) + desired
~~~

There's a better way, though.
If the first thing in a function is a string that isn't assigned to a variable,
that string is attached to the function as its documentation:

~~~ {.python}
def center(data, desired):
    '''Return a new array containing the original data centered around the desired value.'''
    return (data - data.mean()) + desired
~~~

This is better because we can now ask Python's built-in help system to show us the documentation for the function:

~~~ {.python}
help(center)
~~~
~~~ {.output}
Help on function center in module __main__:

center(data, desired)
    Return a new array containing the original data centered around the desired value.

~~~

A string like this is called a **docstring**.
We don't need to use triple quotes when we write one,
but if we do,
we can break the string across multiple lines:

~~~ {.python}
def center(data, desired):
    '''Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - data.mean()) + desired

help(center)
~~~
~~~ {.output}
Help on function center in module __main__:

center(data, desired)
    Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) => [-1, 0, 1]

~~~

## Defining Defaults

We have passed parameters to functions in two ways:
directly, as in `span(data)`,
and by name, as in `numpy.loadtxt(fname='something.csv', delimiter=',')`.
In fact,
we can pass the filename to `loadtxt` without the `fname=`:

~~~ {.python}
numpy.loadtxt('inflammation-01.csv', delimiter=',')
~~~
~~~ {.output}
array([[ 0.,  0.,  1., ...,  3.,  0.,  0.],
       [ 0.,  1.,  2., ...,  1.,  0.,  1.],
       [ 0.,  1.,  1., ...,  2.,  1.,  1.],
       ..., 
       [ 0.,  1.,  1., ...,  1.,  1.,  1.],
       [ 0.,  0.,  0., ...,  0.,  2.,  0.],
       [ 0.,  0.,  1., ...,  1.,  1.,  0.]])~~~

but we still need to say `delimiter=`:

~~~ {.python}
numpy.loadtxt('inflammation-01.csv', ',')
~~~
~~~ {.error}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-26-e3bc6cf4fd6a> in <module>()
----> 1 numpy.loadtxt('inflammation-01.csv', ',')

/Users/gwilson/anaconda/lib/python2.7/site-packages/numpy/lib/npyio.pyc in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin)
    775     try:
    776         # Make sure we're dealing with a proper dtype
--> 777         dtype = np.dtype(dtype)
    778         defconv = _getconv(dtype)
    779 

TypeError: data type "," not understood
~~~

To understand what's going on,
and make our own functions easier to use,
let's re-define our `center` function like this:

~~~ {.python}
def center(data, desired=0.0):
    '''Return a new array containing the original data centered around the desired value (0 by default).
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - data.mean()) + desired
~~~

The key change is that the second parameter is now written `desired=0.0` instead of just `desired`.
If we call the function with two arguments,
it works as it did before:

~~~ {.python}
test_data = numpy.zeros((2, 2))
print center(test_data, 3)
~~~
~~~ {.output}
[[ 3.  3.]
 [ 3.  3.]]
~~~

But we can also now call it with just one parameter,
in which case `desired` is automatically assigned the **default value** of 0.0:

~~~ {.python}
more_data = 5 + numpy.zeros((2, 2))
print 'data before centering:', more_data
print 'centered data:', center(more_data)
~~~
~~~ {.output}
data before centering: [[ 5.  5.]
 [ 5.  5.]]
centered data: [[ 0.  0.]
 [ 0.  0.]]
~~~

This is handy:
if we usually want a function to work one way,
but occasionally need it to do something else,
we can allow people to pass a parameter when they need to
but provide a default to make the normal case easier.
The example below shows how Python matches values to parameters:

~~~ {.python}
def display(a=1, b=2, c=3):
    print 'a:', a, 'b:', b, 'c:', c

print 'no parameters:'
display()
print 'one parameter:'
display(55)
print 'two parameters:'
display(55, 66)
~~~
~~~ {.output}
no parameters:
a: 1 b: 2 c: 3
one parameter:
a: 55 b: 2 c: 3
two parameters:
a: 55 b: 66 c: 3
~~~

As this example shows,
parameters are matched up from left to right,
and any that haven't been given a value explicitly get their default value.
We can override this behavior by naming the value as we pass it in:

~~~ {.python}
print 'only setting the value of c'
display(c=77)
~~~
~~~ {.output}
only setting the value of c
a: 1 b: 2 c: 77
~~~

With that in hand,
let's look at the help for `numpy.loadtxt`:

~~~ {.python}
help(numpy.loadtxt)
~~~
~~~ {.output}
Help on function loadtxt in module numpy.lib.npyio:

loadtxt(fname, dtype=<type 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
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
        default: '#'.
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
    >>> from StringIO import StringIO   # StringIO behaves like a file object
    >>> c = StringIO("0 1\n2 3")
    >>> np.loadtxt(c)
    array([[ 0.,  1.],
           [ 2.,  3.]])
    
    >>> d = StringIO("M 21 72\nF 35 58")
    >>> np.loadtxt(d, dtype={'names': ('gender', 'age', 'weight'),
    ...                      'formats': ('S1', 'i4', 'f4')})
    array([('M', 21, 72.0), ('F', 35, 58.0)],
          dtype=[('gender', '|S1'), ('age', '<i4'), ('weight', '<f4')])
    
    >>> c = StringIO("1,0,2\n3,0,4")
    >>> x, y = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True)
    >>> x
    array([ 1.,  3.])
    >>> y
    array([ 2.,  4.])

~~~

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

> ## Combining strings {.challenge}
>
> "Adding" two strings produces their concatention:
> `'a' + 'b'` is `'ab'`.
> Write a function called `fence` that takes two parameters called `original` and `wrapper`
> and returns a new string that has the wrapper character at the beginning and end of the original:
> 
> ~~~ {.python}
> print fence('name', '*')
> *name*
> ~~~

> ## Selecting characters from strings {.challenge}
>
> If the variable `s` refers to a string,
> then `s[0]` is the string's first character
> and `s[-1]` is its last.
> Write a function called `outer`
> that returns a string made up of just the first and last characters of its input:
> 
> ~~~ {.python}
> print outer('helium')
> hm
> ~~~

> ## Following the call stack {.challenge}
>
> We previously wrote functions called `fence` and `outer`.
> Draw a diagram showing how the call stack changes when we run the following:
>     
> ~~~ {.python}
> print outer(fence('carbon', '+'))
> ~~~

> ## Rescaling, with parameters {.challenge}
>
> Rewrite the `rescale` function so that it scales data to lie between 0.0 and 1.0 by default,
> but will allow the caller to specify lower and upper bounds if they want.
> Compare your implementation to your neighbor's:
> do the two functions always behave the same way?

> ## Automatic plots {.challenge}
>
> Write a function called `analyze` that takes a filename as a parameter
> and displays the three graphs produced in the [previous lesson](01-numpy.ipynb),
> i.e.,
> `analyze('inflammation-01.csv')` should produce the graphs already shown,
> while `analyze('inflammation-02.csv')` should produce corresponding graphs for the second data set.
> Be sure to give your function a docstring.

> ## Rescaling an array {.challenge}
>
> Write a function `rescale` that takes an array as input
> and returns a corresponding array of values scaled to lie in the range 0.0 to 1.0.
> (If $L$ and $H$ are the lowest and highest values in the original array,
> then the replacement for a value $v$ should be $(v-L) / (H-L)$.)
> Be sure to give the function a docstring.

> ## Testing your function {.challenge}
>
> Run the commands `help(numpy.arange)` and `help(numpy.linspace)`
> to see how to use these functions to generate regularly-spaced values,
> then use those values to test your `rescale` function.
