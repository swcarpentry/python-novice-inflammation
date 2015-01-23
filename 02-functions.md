---
layout: topic
title: Programming with Python
subtitle: Creating Functions
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Define a function that takes parameters.
> *   Return a value from a function.
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

~~~ {.python}
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
~~~
~~~ {.output}
freezing point of water: 273.15
~~~

We've successfully called the function that we defined,
and we have access to the value that we returned.


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
We could write out the formula again,
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
then combine them in ever-larger chunks to get the effect we want.
Real-life functions will usually be larger than the ones shown here --- typically half a dozen to a few dozen lines --- but
they shouldn't ever be much longer than that,
or the next person who reads it won't be able to understand what's going on.


> ## FIXME {.challenge}
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

> ## FIXME {.challenge}
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
