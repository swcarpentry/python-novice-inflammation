---
title: Creating Functions
teaching: 30
exercises: 0
questions:
- "How can I define new functions?"
- "What's the difference between defining and calling a function?"
- "What happens when I call a function?"
objectives:
- "Define a function that takes parameters."
- "Return a value from a function."
- "Test and debug a function."
- "Set default values for function parameters."
- "Explain why we should divide programs into small, single-purpose functions."
keypoints:
- "Define a function using `def name(...params...)`."
- "The body of a function must be indented."
- "Call a function using `name(...values...)`."
- "Numbers are stored as integers or floating-point numbers."
- "Integer division produces the whole part of the answer (not the fractional part)."
- "Each time a function is called, a new stack frame is created on the **call stack** to hold its parameters and local variables."
- "Python looks for variables in the current stack frame before looking for them at the top level."
- "Use `help(thing)` to view help for something."
- "Put docstrings in functions to provide help for that function."
- "Specify default values for parameters when defining a function using `name=value` in the parameter list."
- "Parameters can be passed by matching based on name, by position, or by omitting them (in which case the default value is used)."
---

At this point,
we've written code to draw some interesting features in our inflammation data,
loop over all our data files to quickly draw these plots for each of them,
and have Python make decisions based on what it sees in our data.
But, our code is getting pretty long and complicated;
what if we had thousands of datasets,
and didn't want to generate a figure for every single one?
Commenting out the figure-drawing code is a nuisance.
Also, what if we want to use that code again,
on a different dataset or at a different point in our program?
Cutting and pasting it is going to make our code get very long and very repetitive,
very quickly.
We'd like a way to package our code so that it is easier to reuse,
and Python provides for this by letting us define things called 'functions' -
a shorthand way of re-executing longer pieces of code.

Let's start by defining a function `fahr_to_kelvin` that converts temperatures from Fahrenheit to Kelvin:

~~~
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15
~~~
{: .python}

![The Blueprint for a Python Function](../fig/python-function.svg)

<!--- see https://gist.github.com/wd15/2b4ffbe5ce0d0ddb8a5b to
regenerate the above figure --->

The function definition opens with the keyword `def` followed by the
name of the function and a parenthesized list of parameter names. The
[body]({{ page.root }}/reference/#function-body) of the function --- the
statements that are executed when it runs --- is indented below the
definition line.

When we call the function,
the values we pass to it are assigned to those variables
so that we can use them inside the function.
Inside the function,
we use a [return statement]({{ page.root }}/reference/#return-statement) to send a result back to whoever asked for it.

Let's try running our function.

~~~
fahr_to_kelvin(32)
~~~

This command should call our function, using "32" as the input and return the function value.

In fact, calling our own function is no different from calling any other function:
~~~
print('freezing point of water:', fahr_to_kelvin(32))
print('boiling point of water:', fahr_to_kelvin(212))
~~~
{: .python}

~~~
freezing point of water: 273.15
boiling point of water: 373.15
~~~
{: .output}

We've successfully called the function that we defined,
and we have access to the value that we returned.

> ## Integer Division
>
> We are using Python 3, where division always returns a floating point number:
>
> ~~~
> $ python3 -c "print(5/9)"
> ~~~
> {: .python}
>
> ~~~
> 0.5555555555555556
> ~~~
> {: .output}
>
> Unfortunately, this wasn't the case in Python 2:
>
> ~~~
> 5/9
> ~~~
> {: .python}
>
> ~~~
> 0
> ~~~
> {: .output}
>
> If you are using Python 2 and want to keep the fractional part of division
> you need to convert one or the other number to floating point:
>
> ~~~
> float(5)/9
> ~~~
> {: .python}
>
> ~~~
> 0.555555555556
> ~~~
> {: .output}
>
> ~~~
> 5/float(9)
> ~~~
> {: .python}
>
> ~~~
> 0.555555555556
> ~~~
> {: .output}
>
> ~~~
> 5.0/9
> ~~~
> {: .python}
>
> ~~~
> 0.555555555556
> ~~~
> {: .output}
> ~~~
> 5/9.0
> ~~~
> {: .python}
>
> ~~~
> 0.555555555556
> ~~~
> {: .output}
>
> And if you want an integer result from division in Python 3,
> use a double-slash:
>
> ~~~
> 4//2
> ~~~
> {: .python}
>
> ~~~
> 2
> ~~~
> {: .output}
>
> ~~~
> 3//2
> ~~~
> {: .python}
>
> ~~~
> 1
> ~~~
> {: .output}
{: .callout}

## Composing Functions

Now that we've seen how to turn Fahrenheit into Kelvin,
it's easy to turn Kelvin into Celsius:

~~~
def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

print('absolute zero in Celsius:', kelvin_to_celsius(0.0))
~~~
{: .python}

~~~
absolute zero in Celsius: -273.15
~~~
{: .output}

What about converting Fahrenheit to Celsius?
We could write out the formula,
but we don't need to.
Instead,
we can [compose]({{ page.root }}/reference/#compose) the two functions we have already created:

~~~
def fahr_to_celsius(temp_f):
    temp_k = fahr_to_kelvin(temp_f)
    result = kelvin_to_celsius(temp_k)
    return result

print('freezing point of water in Celsius:', fahr_to_celsius(32.0))
~~~
{: .python}

~~~
freezing point of water in Celsius: 0.0
~~~
{: .output}

This is our first taste of how larger programs are built:
we define basic operations,
then combine them in ever-large chunks to get the effect we want.
Real-life functions will usually be larger than the ones shown here --- typically half a dozen to a few dozen lines --- but
they shouldn't ever be much longer than that,
or the next person who reads it won't be able to understand what's going on.

## Tidying up

Now that we know how to wrap bits of code up in functions,
we can make our inflammation analysis easier to read and easier to reuse.
First, let's make an `analyze` function that generates our plots:

~~~
def analyze(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()
~~~
{: .python}

and another function called `detect_problems` that checks for those systematics
we noticed:

~~~
def detect_problems(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')
~~~
{: .python}

Notice that rather than jumbling this code together in one giant `for` loop,
we can now read and reuse both ideas separately.
We can reproduce the previous analysis with a much simpler `for` loop:

~~~
for f in filenames[:3]:
    print(f)
    analyze(f)
    detect_problems(f)
~~~
{: .python}

By giving our functions human-readable names,
we can more easily read and understand what is happening in the `for` loop.
Even better, if at some later date we want to use either of those pieces of code again,
we can do so in a single line.

## Testing and Documenting

Once we start putting things in functions so that we can re-use them,
we need to start testing that those functions are working correctly.
To see how to do this,
let's write a function to center a dataset around a particular value:

~~~
def center(data, desired):
    return (data - numpy.mean(data)) + desired
~~~
{: .python}

We could test this on our actual data,
but since we don't know what the values ought to be,
it will be hard to tell if the result was correct.
Instead,
let's use NumPy to create a matrix of 0's
and then center that around 3:

~~~
z = numpy.zeros((2,2))
print(center(z, 3))
~~~
{: .python}

~~~
[[ 3.  3.]
 [ 3.  3.]]
~~~
{: .output}

That looks right,
so let's try `center` on our real data:

~~~
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print(center(data, 0))
~~~
{: .python}

~~~
[[-6.14875 -6.14875 -5.14875 ..., -3.14875 -6.14875 -6.14875]
 [-6.14875 -5.14875 -4.14875 ..., -5.14875 -6.14875 -5.14875]
 [-6.14875 -5.14875 -5.14875 ..., -4.14875 -5.14875 -5.14875]
 ...,
 [-6.14875 -5.14875 -5.14875 ..., -5.14875 -5.14875 -5.14875]
 [-6.14875 -6.14875 -6.14875 ..., -6.14875 -4.14875 -6.14875]
 [-6.14875 -6.14875 -5.14875 ..., -5.14875 -5.14875 -6.14875]]
~~~
{: .output}

It's hard to tell from the default output whether the result is correct,
but there are a few simple tests that will reassure us:

~~~
print('original min, mean, and max are:', numpy.min(data), numpy.mean(data), numpy.max(data))
centered = center(data, 0)
print('min, mean, and max of centered data are:', numpy.min(centered), numpy.mean(centered), numpy.max(centered))
~~~
{: .python}

~~~
original min, mean, and max are: 0.0 6.14875 20.0
min, mean, and and max of centered data are: -6.14875 2.84217094304e-16 13.85125
~~~
{: .output}

That seems almost right:
the original mean was about 6.1,
so the lower bound from zero is now about -6.1.
The mean of the centered data isn't quite zero --- we'll explore why not in the challenges --- but it's pretty close.
We can even go further and check that the standard deviation hasn't changed:

~~~
print('std dev before and after:', numpy.std(data), numpy.std(centered))
~~~
{: .python}

~~~
std dev before and after: 4.61383319712 4.61383319712
~~~
{: .output}

Those values look the same,
but we probably wouldn't notice if they were different in the sixth decimal place.
Let's do this instead:

~~~
print('difference in standard deviations before and after:', numpy.std(data) - numpy.std(centered))
~~~
{: .python}

~~~
difference in standard deviations before and after: -3.5527136788e-15
~~~
{: .output}

Again,
the difference is very small.
It's still possible that our function is wrong,
but it seems unlikely enough that we should probably get back to doing our analysis.
We have one more task first, though:
we should write some [documentation]({{ page.root }}/reference/#documentation) for our function
to remind ourselves later what it's for and how to use it.

The usual way to put documentation in software is to add [comments]({{ page.root }}/reference/#comment) like this:

~~~
# center(data, desired): return a new array containing the original data centered around the desired value.
def center(data, desired):
    return (data - numpy.mean(data)) + desired
~~~
{: .python}

There's a better way, though.
If the first thing in a function is a string that isn't assigned to a variable,
that string is attached to the function as its documentation:

~~~
def center(data, desired):
    '''Return a new array containing the original data centered around the desired value.'''
    return (data - numpy.mean(data)) + desired
~~~
{: .python}

This is better because we can now ask Python's built-in help system to show us the documentation for the function:

~~~
help(center)
~~~
{: .python}

~~~
Help on function center in module __main__:

center(data, desired)
    Return a new array containing the original data centered around the desired value.
~~~
{: .output}

A string like this is called a [docstring]({{ page.root }}/reference/#docstring).
We don't need to use triple quotes when we write one,
but if we do,
we can break the string across multiple lines:

~~~
def center(data, desired):
    '''Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - numpy.mean(data)) + desired

help(center)
~~~
{: .python}

~~~
Help on function center in module __main__:

center(data, desired)
    Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) => [-1, 0, 1]
~~~
{: .output}

## Defining Defaults

We have passed parameters to functions in two ways:
directly, as in `type(data)`,
and by name, as in `numpy.loadtxt(fname='something.csv', delimiter=',')`.
In fact,
we can pass the filename to `loadtxt` without the `fname=`:

~~~
numpy.loadtxt('inflammation-01.csv', delimiter=',')
~~~
{: .python}

~~~
array([[ 0.,  0.,  1., ...,  3.,  0.,  0.],
       [ 0.,  1.,  2., ...,  1.,  0.,  1.],
       [ 0.,  1.,  1., ...,  2.,  1.,  1.],
       ...,
       [ 0.,  1.,  1., ...,  1.,  1.,  1.],
       [ 0.,  0.,  0., ...,  0.,  2.,  0.],
       [ 0.,  0.,  1., ...,  1.,  1.,  0.]])
~~~
{: .output}

but we still need to say `delimiter=`:

~~~
numpy.loadtxt('inflammation-01.csv', ',')
~~~
{: .python}

~~~
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
{: .error}

To understand what's going on,
and make our own functions easier to use,
let's re-define our `center` function like this:

~~~
def center(data, desired=0.0):
    '''Return a new array containing the original data centered around the desired value (0 by default).
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - numpy.mean(data)) + desired
~~~
{: .python}

The key change is that the second parameter is now written `desired=0.0` instead of just `desired`.
If we call the function with two arguments,
it works as it did before:

~~~
test_data = numpy.zeros((2, 2))
print(center(test_data, 3))
~~~
{: .python}

~~~
[[ 3.  3.]
 [ 3.  3.]]
~~~
{: .output}

But we can also now call it with just one parameter,
in which case `desired` is automatically assigned the [default value]({{ page.root }}/reference/#default-value) of 0.0:

~~~
more_data = 5 + numpy.zeros((2, 2))
print('data before centering:')
print(more_data)
print('centered data:')
print(center(more_data))
~~~
{: .python}

~~~
data before centering:
[[ 5.  5.]
 [ 5.  5.]]
centered data:
[[ 0.  0.]
 [ 0.  0.]]
~~~
{: .output}

This is handy:
if we usually want a function to work one way,
but occasionally need it to do something else,
we can allow people to pass a parameter when they need to
but provide a default to make the normal case easier.
The example below shows how Python matches values to parameters:

~~~
def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)

print('no parameters:')
display()
print('one parameter:')
display(55)
print('two parameters:')
display(55, 66)
~~~
{: .python}

~~~
no parameters:
a: 1 b: 2 c: 3
one parameter:
a: 55 b: 2 c: 3
two parameters:
a: 55 b: 66 c: 3
~~~
{: .output}

As this example shows,
parameters are matched up from left to right,
and any that haven't been given a value explicitly get their default value.
We can override this behavior by naming the value as we pass it in:

~~~
print('only setting the value of c')
display(c=77)
~~~
{: .python}

~~~
only setting the value of c
a: 1 b: 2 c: 77
~~~
{: .output}

With that in hand,
let's look at the help for `numpy.loadtxt`:

~~~
help(numpy.loadtxt)
~~~
{: .python}

~~~
Help on function loadtxt in module numpy.lib.npyio:

loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
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
{: .output}

There's a lot of information here,
but the most important part is the first couple of lines:

~~~
loadtxt(fname, dtype=<type 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None,
        unpack=False, ndmin=0)
~~~
{: .output}

This tells us that `loadtxt` has one parameter called `fname` that doesn't have a default value,
and eight others that do.
If we call the function like this:

~~~
numpy.loadtxt('inflammation-01.csv', ',')
~~~
{: .python}

then the filename is assigned to `fname` (which is what we want),
but the delimiter string `','` is assigned to `dtype` rather than `delimiter`,
because `dtype` is the second parameter in the list. However ',' isn't a known `dtype` so
our code produced an error message when we tried to run it.
When we call `loadtxt` we don't have to provide `fname=` for the filename because it's the
first item in the list, but if we want the ',' to be assigned to the variable `delimiter`,
we *do* have to provide `delimiter=` for the second parameter since `delimiter` is not
the second parameter in the list.

## Readable functions

Consider these two functions:

~~~
def s(p):
    a = 0
    for v in p:
        a += v
    m = a / len(p)
    d = 0
    for v in p:
        d += (v - m) * (v - m)
    return numpy.sqrt(d / (len(p) - 1))

def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return numpy.sqrt(sum_squared_devs / (len(sample) - 1))
~~~
{: .python}

The functions `s` and `std_dev` are computationally equivalent (they
both calculate the sample standard deviation), but to a human reader,
they look very different. You probably found `std_dev` much easier to
read and understand than `s`.

As this example illustrates, both documentation and a programmer's
_coding style_ combine to determine how easy it is for others to read
and understand the programmer's code. Choosing meaningful variable
names and using blank spaces to break the code into logical "chunks"
are helpful techniques for producing _readable code_. This is useful
not only for sharing code with others, but also for the original
programmer. If you need to revisit code that you wrote months ago and
haven't thought about since then, you will appreciate the value of
readable code!

> ## Combining Strings
>
> "Adding" two strings produces their concatenation:
> `'a' + 'b'` is `'ab'`.
> Write a function called `fence` that takes two parameters called `original` and `wrapper`
> and returns a new string that has the wrapper character at the beginning and end of the original.
> A call to your function should look like this:
>
> ~~~
> print(fence('name', '*'))
> ~~~
> {: .python}
>
> ~~~
> *name*
> ~~~
> {: .output}
>
> > ## Solution
> > ~~~
> > def fence(original, wrapper):
> >     return wrapper + original + wrapper
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Selecting Characters From Strings
>
> If the variable `s` refers to a string,
> then `s[0]` is the string's first character
> and `s[-1]` is its last.
> Write a function called `outer`
> that returns a string made up of just the first and last characters of its input.
> A call to your function should look like this:
>
> ~~~
> print(outer('helium'))
> ~~~
> {: .python}
>
> ~~~
> hm
> ~~~
> {: .output}
>
> > ## Solution
> > ~~~
> > def outer(input_string):
> >     return input_string[0] + input_string[-1]
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Rescaling an Array
>
> Write a function `rescale` that takes an array as input
> and returns a corresponding array of values scaled to lie in the range 0.0 to 1.0.
> (Hint: If $L$ and $H$ are the lowest and highest values in the original array,
> then the replacement for a value $v$ should be $(v-L) / (H-L)$.)
>
> > ## Challenge
> > ~~~
> > def rescale(input_array):
> >     L = numpy.min(input_array)
> >     H = numpy.max(input_array)
> >     output_array = (input_array - L) / (H - L)
> >     return output_array
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Testing and Documenting Your Function
>
> Run the commands `help(numpy.arange)` and `help(numpy.linspace)`
> to see how to use these functions to generate regularly-spaced values,
> then use those values to test your `rescale` function.
> Once you've successfully tested your function,
> add a docstring that explains what it does.
>
> > ## Solution
> > ~~~
> > '''Takes an array as input, and returns a corresponding array scaled so
> > that 0 corresponds to the minimum and 1 to the maximum value of the input array.
> >
> > Examples:
> > >>> rescale(numpy.arange(10.0))
> > array([ 0.        ,  0.11111111,  0.22222222,  0.33333333,  0.44444444,
> >        0.55555556,  0.66666667,  0.77777778,  0.88888889,  1.        ])
> > >>> rescale(numpy.linspace(0, 100, 5))
> > array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
> > '''
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Defining Defaults
>
> Rewrite the `rescale` function so that it scales data to lie between 0.0 and 1.0 by default,
> but will allow the caller to specify lower and upper bounds if they want.
> Compare your implementation to your neighbor's:
> do the two functions always behave the same way?
>
> > ## Solution
> > ~~~
> > def rescale(input_array, low_val=0.0, high_val=1.0):
> >     '''rescales input array values to lie between low_val and high_val'''
> >     L = numpy.min(input_array)
> >     H = numpy.max(input_array)
> >     intermed_array = (input_array - L) / (H - L)
> >     output_array = intermed_array * (high_val - low_val) + low_val
> >     return output_array
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Variables Inside and Outside Functions
>
> What does the following piece of code display when run - and why?
>
> ~~~
> f = 0
> k = 0
>
> def f2k(f):
>   k = ((f-32)*(5.0/9.0)) + 273.15
>   return k
>
> f2k(8)
> f2k(41)
> f2k(32)
>
> print(k)
> ~~~
> {: .python}
>
> > ## Solution
> >
> > ~~~
> > 259.81666666666666
> > 287.15
> > 273.15
> > 0
> > ~~~
> > {: .output}
> > `k` is 0 because the `k` inside the function `f2k` doesn't know about the `k` defined outside the function.
> {: .solution}
{: .challenge}

> ## Mixing Default and Non-Default Parameters
>
> Given the following code:
>
> ~~~
> def numbers(one, two=2, three, four=4):
>     n = str(one) + str(two) + str(three) + str(four)
>     return n
>
> print(numbers(1, three=3))
> ~~~
> {: .python}
>
> what do you expect will be printed?  What is actually printed?
> What rule do you think Python is following?
>
> 1.  `1234`
> 2.  `one2three4`
> 3.  `1239`
> 4.  `SyntaxError`
>
> Given that, what does the following piece of code display when run?
>
> ~~~
> def func(a, b=3, c=6):
>   print('a: ', a, 'b: ', b, 'c:', c)
>
> func(-1, 2)
> ~~~
> {: .python}
>
> 1. `a: b: 3 c: 6`
> 2. `a: -1 b: 3 c: 6`
> 3. `a: -1 b: 2 c: 6`
> 4. `a: b: -1 c: 2`
>
> > ## Solution
> > Attempting to define the `numbers` function results in `4. SyntaxError`.
> > The defined parameters `two` and `four` are given default values. Because
> > `one` and `three` are not given default values, they are required to be 
> > included as arguments when the function is called and must be placed
> > before any parameters that have default values in the function definition.
> > 
> > The given call to `func` displays `a: -1 b: 2 c: 6`. -1 is assigned to
> > the first parameter `a`, 2 is assigned to the next parameter `b`, and `c` is
> > not passed a value, so it uses its default value 6.
> {: .solution}
{: .challenge}

> ## The Old Switcheroo
>
> Which of the following would be printed if you were to run this code? Why did you pick this answer?
>
> 1. `7 3`
> 2. `3 7`
> 3. `3 3`
> 4. `7 7`
>
> ~~~
> a = 3
> b = 7
>
> def swap(a, b):
>     temp = a
>     a = b
>     b = temp
>
> swap(a, b)
>
> print(a, b)
> ~~~
> {: .python}
> > ## Solution
> > `3, 7` is correct. Initially `a` has a value of 3 and `b` has a value of 7.
> > When the swap function is called, it creates local variables (also called
> > `a` and `b` in this case) and trades their values. The function does not
> > return any values and does not alter `a` or `b` outside of its local copy.
> > Therefore the original values of `a` and `b` remain unchanged.
> {: .solution}
{: .challenge}

> ## Readable Code
>
> Revise a function you wrote for one of the previous exercises to try to make
> the code more readable. Then, collaborate with one of your neighbors
> to critique each other's functions and discuss how your function implementations
> could be further improved to make them more readable.
{: .challenge}
