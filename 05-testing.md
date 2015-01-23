---
layout: page
title: Programming with Python
subtitle: Testing and Documenting Functions
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Test and debug a function.


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

> ## FIXME {.challenge}
>
> Write a function `rescale` that takes an array as input
> and returns a corresponding array of values scaled to lie in the range 0.0 to 1.0.
> (If $L$ and $H$ are the lowest and highest values in the original array,
> then the replacement for a value $v$ should be $(v-L) / (H-L)$.)
> Be sure to give the function a docstring.

> ## FIXME {.challenge}
>
> Run the commands `help(numpy.arange)` and `help(numpy.linspace)`
> to see how to use these functions to generate regularly-spaced values,
> then use those values to test your `rescale` function.
