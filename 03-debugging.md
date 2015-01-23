---
layout: page
title: Programming with Python
subtitle: Debugging a Function
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Test and debug a function.

Let's convert the boiling point of water from Fahrenheit to Kelvin. 

~~~ {.python}
print 'boiling point of water:', fahr_to_kelvin(212)
~~~
~~~ {.output}
boiling point of water: 273.15
~~~

Unfortunately, the value returned doesn't look right.
What went wrong?

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
