---
layout: page
title: Programming with Python
subtitle: Analyzing Multiple Data Sets
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Explain what a for loop does.
> *   Correctly write for loops to repeat simple calculations.
> *   Trace changes to a loop variable as the loop runs.
> *   Trace changes to other variables as they are updated by a for loop.
> *   Explain what a list is.
> *   Create and index lists of simple values.
> *   Use a library function to get a list of filenames that match a simple wildcard pattern.
> *   Use a for loop to process multiple files.

In the last lesson,
we wrote some code that plots some values of interest from our first inflammation dataset,
and reveals some suspicious features in it, such as from `inflammation-01.csv`

![Analysis of inflammation-01.csv](fig/03-loop_2_0.png)\

but we have a dozen data sets right now and more on the way.
We want to create plots for all our data sets with a single statement.
To do that,
we'll have to teach the computer how to repeat things.

## For Loops

Suppose we want to print each character in the word "lead" on a line of its own.
One way is to use four `print` statements:

~~~ {.python}
def print_characters(element):
    print element[0]
    print element[1]
    print element[2]
    print element[3]

print_characters('lead')
~~~
~~~ {.output}
l
e
a
d
~~~

but that's a bad approach for two reasons:

1.  It doesn't scale:
    if we want to print the characters in a string that's hundreds of letters long,
    we'd be better off just typing them in.

1.  It's fragile:
    if we give it a longer string,
    it only prints part of the data,
    and if we give it a shorter one,
    it produces an error because we're asking for characters that don't exist.

~~~ {.python}
print_characters('tin')
~~~
~~~ {.error}
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-13-5bc7311e0bf3> in <module>()
----> 1 print_characters('tin')

<ipython-input-12-11460561ea56> in print_characters(element)
      3     print element[1]
      4     print element[2]
----> 5     print element[3]
      6
      7 print_characters('lead')

IndexError: string index out of range
~~~ {.output}
t
i
n
~~~

Here's a better approach:

~~~ {.python}
def print_characters(element):
    for char in element:
        print char

print_characters('lead')
~~~

This is shorter---certainly shorter than something that prints every character in a hundred-letter string---and
more robust as well:

~~~ {.python}
print_characters('oxygen')
~~~

The improved version of `print_characters` uses a **for loop**
to repeat an operation---in this case, printing---once for each thing in a collection.
The general form of a loop is:

~~~ {.python}
for variable in collection:
    do things with variable
~~~

We can call the **loop variable** anything we like,
but there must be a colon at the end of the line starting the loop,
and we must indent the body of the loop.

Here's another loop that repeatedly updates a variable:

~~~ {.python}
length = 0
for vowel in 'aeiou':
    length = length + 1
print 'There are', length, 'vowels'
~~~

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

~~~ {.python}
letter = 'z'
for letter in 'abc':
    print letter
print 'after the loop, letter is', letter
~~~

Note also that finding the length of a string is such a common operation
that Python actually has a built-in function to do it called `len`:

~~~ {.python}
print len('aeiou')
~~~

`len` is much faster than any function we could write ourselves,
and much easier to read than a two-line loop;
it will also give us the length of many other things that we haven't met yet,
so we should always use it when we can.

## Lists

Just as a `for` loop is a way to do operations many times,
a list is a way to store many values.
Unlike NumPy arrays,
there are built into the language.
We create a list by putting values inside square brackets:

~~~ {.python}
odds = [1, 3, 5, 7]
print 'odds are:', odds
~~~

We select individual elements from lists by indexing them:

~~~ {.python}
print 'first and last:', odds[0], odds[-1]
~~~

and if we loop over a list,
the loop variable is assigned elements one at a time:

~~~ {.python}
for number in odds:
    print number
~~~

There is one important difference between lists and strings:
we can change the values in a list,
but we cannot change the characters in a string.
For example:

~~~ {.python}
names = ['Newton', 'Darwing', 'Turing'] # typo in Darwin's name
print 'names is originally:', names
names[1] = 'Darwin' # correct the name
print 'final value of names:', names
~~~

works, but:

~~~ {.python}
name = 'Bell'
name[0] = 'b'
~~~

does not.

> ## Ch-Ch-Ch-Changes {.callout}
>
> Data that can be changed is called **mutable**,
> while data that cannot be is called **immutable**.
> Like strings,
> numbers are immutable:
> there's no way to make the number 0 have the value 1 or vice versa
> (at least, not in Python --- there actually *are* languages that will let people do this,
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

~~~ {.python}
odds.append(11)
print 'odds after adding a value:', odds
~~~

FIXME: output

~~~ {.python}
del odds[0]
print 'odds after removing the first element:', odds
~~~

FIXME: output

~~~ {.python}
odds.reverse()
print 'odds after reversing:', odds
~~~

FIXME: output

## Processing Multiple Files

We now have almost everything we need to process all our data files.
The only thing that's missing is a library with a rather unpleasant name:

~~~ {.python}
import glob
~~~

The `glob` library contains a single function, also called `glob`,
that finds files whose names match a pattern.
We provide those patterns as strings:
the character `*` matches zero or more characters,
while `?` matches any one character.
We can use this to get the names of all the IPython Notebooks we have created so far:

~~~ {.python}
print glob.glob('*.ipynb')
~~~

~~~ {.output}
['01-numpy.ipynb', '02-func.ipynb', '03-loop.ipynb', '04-cond.ipynb', '05-defensive.ipynb', '06-cmdline.ipynb', 'spatial-intro.ipynb']
~~~

or to get the names of all our CSV data files:

~~~ {.python}
print glob.glob('*.csv')
~~~

~~~ {.output}
['inflammation-01.csv', 'inflammation-02.csv', 'inflammation-03.csv', 'inflammation-04.csv', 'inflammation-05.csv', 'inflammation-06.csv', 'inflammation-07.csv', 'inflammation-08.csv', 'inflammation-09.csv', 'inflammation-10.csv', 'inflammation-11.csv', 'inflammation-12.csv', 'small-01.csv', 'small-02.csv', 'small-03.csv']
~~~

As these examples show,
`glob.glob`'s result is a list of strings,
which means we can loop over it
to do something with each filename in turn.
In our case,
the "something" we want is the code that generates those plots of our inflammation data.
Let's test it by analyzing the first three files in the list:

~~~ {.python}
filenames = glob.glob('*.csv')
filenames = filenames[0:3]
for f in filenames:
    print f

    data = numpy.loadtxt(fname=f, delimiter=',')

    pyplot.figure(figsize=(10.0, 3.0))

    pyplot.subplot(1, 3, 1)
    pyplot.ylabel('average')
    pyplot.plot(data.mean(axis=0))

    pyplot.subplot(1, 3, 2)
    pyplot.ylabel('max')
    pyplot.plot(data.max(axis=0))

    pyplot.subplot(1, 3, 3)
    pyplot.ylabel('min')
    pyplot.plot(data.min(axis=0))

    pyplot.tight_layout()
    pyplot.show()
~~~

~~~ {.output}
inflammation-01.csv
~~~

![Analysis of inflammation-01.csv](fig/03-loop_49_1.png)\


~~~ {.output}
inflammation-02.csv
~~~

![Analysis of inflammation-02.csv](fig/03-loop_49_3.png)\


~~~ {.output}
inflammation-03.csv
~~~

![Analysis of inflammation-03.csv](fig/03-loop_49_5.png)\

Sure enough,
the maxima of the first two data sets show exactly the same ramp as the first,
and their minima show the same staircase structure;
a different situation has been revealed in the third dataset,
where the maxima are a bit less regular, but the minima are consistently zero.

> ## FIXME {.challenge}
>
> Python has a built-in function called `range` that creates a list of numbers:
> `range(3)` produces `[0, 1, 2]`, `range(2, 5)` produces `[2, 3, 4]`.
> Using `range`,
> write a loop that uses `range` to print the first 3 natural numbers:
>
> ~~~ {.python}
> 1
> 2
> 3
> ~~~

> ## FIXME {.challenge}
>
> Exponentiation is built into Python:
>
>~~~ {.python}
> print 5**3
> 125
> ~~~
>
> It also has a function called `pow` that calculates the same value.
> Write a loop to calculate the same result.

> ## FIXME {.challenge}
>
> Write a loop that takes a string,
> and produces a new string with the characters in reverse order,
> so `'Newton'` becomes `'notweN'`.

> ## FIXME {.challenge}
>
> Write a loop calculates the sum of the values in a list.
> (Python has a built-in function called `sum` that does this for you.
> Please don't use it for this exercise.)
