---
title: Repeating Actions with Loops
teaching: 30
exercises: 0
questions:
- "How can I do the same operations on many different values?"
objectives:
- "Explain what a for loop does."
- "Correctly write for loops to repeat simple calculations."
- "Trace changes to a loop variable as the loop runs."
- "Trace changes to other variables as they are updated by a for loop."
keypoints:
- "Use `for variable in sequence` to process the elements of a sequence one at a time."
- "The body of a for loop must be indented."
- "Use `len(thing)` to determine the length of something that contains other values."
---

In the last lesson,
we wrote some code that plots some values of interest from our first inflammation dataset,
and reveals some suspicious features in it, such as from `inflammation-01.csv`

![Analysis of inflammation-01.csv](../fig/03-loop_2_0.png)

We have a dozen data sets right now, though, and more on the way.
We want to create plots for all of our data sets with a single statement.
To do that, we'll have to teach the computer how to repeat things.

So far, we've seen how to create variables that hold a single value.  For example, we can create a variable, "a", that holds the integer value 10.

~~~
a = 10
~~~
{: .python}

We've also shown how to use these variables to create new variables.  For instance, we can create a new variable, "b", that holds the value of the first variable multiplied by ten.

~~~
b = a * 10
print(b)
100
~~~
{: .python}

However, there will often be occasions when you need a way to store multiple values in a group.  For example, you might want to store daily temperature readings for a week.  You could try using a separate variable for each element.

~~~
daily_temp_1 = 63
daily_temp_2 = 62
daily_temp_3 = 60
daily_temp_4 = 66
~~~
{: .python}

With a large number of observations, this approach becomes unmanageable.  What you really need is a way to store a series of values in a single variable.  Python provides a number of different formats, or data structures, to store collections of variables.  The most basic data structure to store multiple values is a list.  Here's one way can store daily temperature readings in a list.

~~~
daily_temps = [63, 62, 60, 66, 58, 58, 60]
print(daily_temps)
[63, 62, 60, 66, 58, 58, 61]
~~~
{: .python}

You can access the value for each element of a list by its index.  The index is the position of the element in a list, starting at zero.  For instance, to access the first temperature reading, you would print the value of the variable at index 0.

~~~
print(daily_temps[0])
63
~~~
{: .python}

Note that you can't access an element that doesn't exist.  If you try to access element 7 of this list, python will reply that this index is out of range.  Remember, you start counting from 0, so daily_temps[6] represents the seventh value in this list.

~~~
print(daily_temps[6])
60
print(daily_temps[7]
...
IndexError: list index out of range
~~~
{: .python}

You add, multiply, or perform other operations on the elements of a list in the same way you use stand alone variables.  

~~~
print(print(daily_temps[0] + daily_temps[1])
125
~~~
{: .python}

We could find the average temperature reading for this week this way, by adding each element separately and dividing by the number of observations. This would reduce the usefulness of our list, though, since we'd still have to type out each individual element.  What we need is a way to go through each element of the list, one by one.  

Python provides this ability with a loop, a method that allows you to step (or iterate) through the elements of a list.  

~~~
for daily_temp in daily_temps:
    print(daily_temp)
63
62
60
66
58
58
60
~~~
{: .python}

This loop steps through each temperature reading in the list, assigns it to the variable daily_temp, and then prints the value of the daily_temp in the body of the loop.  You can also access and set variables defined outside the loop. For example, here's a loop to find the average temperature for the week.

~~~
sum_temp = 0
count = 0
for daily_temp in daily_temps:
    sum_temp = sum_temp + daily_temp
    count = count + 1
print(sum_temp / count)
~~~
{: .python}

We create two variables prior to entering the loop - a running sum of the observed temperatures, and a count of the number of observations.  For each observation in the list, we increase the sum by the value of each new temperature reading, and we increase the count by one.  Once we exit the loop, we divide the sum of the temperature observations by the number of observations to get the average.

As you use different methods and data types, you'll find that python often uses a list to store values, even if it isn't immediately apparant.  In the example above, we explicitely defined a list of numbers.  It turns out that Python also treats words this way as well.  A string, or word, is in fact a list of characters.  For example, the word "lead" is a list composed of 'l', 'e', 'a', 'd'.  

Try it out!

~~~
word = 'lead'
~~~
{: .python}

We can access a character in a string using its index. For example, we can get the first
character of the word 'lead', by using word[0]. One way to print each character is to use
four `print` statements:

~~~
print(word[0])
print(word[1])
print(word[2])
print(word[3])
~~~
{: .python}

~~~
l
e
a
d
~~~
{: .output}

As with our explicit list of integers, this is a bad approach for two reasons:

1.  It doesn't scale:
    if we want to print the characters in a string that's hundreds of letters long,
    we'd be better off just typing them in.

1.  It's fragile:
    if we give it a longer string,
    it only prints part of the data,
    and if we give it a shorter one,
    it produces an error because we're asking for characters that don't exist.

~~~
word = 'tin'
print(word[0])
print(word[1])
print(word[2])
print(word[3])

~~~
{: .python}

~~~
t
i
n
~~~
{: .output}

~~~
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-3-7974b6cdaf14> in <module>()
      3 print(word[1])
      4 print(word[2])
----> 5 print(word[3])

IndexError: string index out of range
~~~
{: .error}

Here's a better approach:

~~~
word = 'lead'
for char in word:
    print(char)

~~~
{: .python}

~~~
l
e
a
d
~~~
{: .output}

This is shorter---certainly shorter than something that prints every character in a hundred-letter string---and
more robust as well:

~~~
word = 'oxygen'
for char in word:
    print(char)
~~~
{: .python}

~~~
o
x
y
g
e
n
~~~
{: .output}

The improved version uses a [for loop]({{ page.root }}/reference/#for-loop)
to repeat an operation---in this case, printing---once for each thing in a sequence.
The general form of a loop is:

~~~
for element in variable:
    do things with element
~~~
{: .python}

Using the oxygen example above, the loop might look like this:

![loop_image](../fig/loops_image.png)

where each character (`char`) in the variable `word` is looped through and printed one character after another.
The numbers in the diagram denote which loop cycle the character was printed in (1 being the first loop, and 6 being the final loop).

We can call the [loop variable]({{ page.root }}/reference/#loop-variable) anything we like,
but there must be a colon at the end of the line starting the loop,
and we must indent anything we want to run inside the loop. Unlike many other languages, there is no
command to signify the end of the loop body (e.g. end for); what is indented after the for statement belongs to the loop.

Here's another loop that repeatedly updates a variable:

~~~
length = 0
for vowel in 'aeiou':
    length = length + 1
print('There are', length, 'vowels')
~~~
{: .python}

~~~
There are 5 vowels
~~~
{: .output}

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

~~~
letter = 'z'
for letter in 'abc':
    print(letter)
print('after the loop, letter is', letter)
~~~
{: .python}

~~~
a
b
c
after the loop, letter is c
~~~
{: .output}

Note also that finding the length of a string is such a common operation
that Python actually has a built-in function to do it called `len`:

~~~
print(len('aeiou'))
~~~
{: .python}

~~~
5
~~~
{: .output}

`len` is much faster than any function we could write ourselves,
and much easier to read than a two-line loop;
it will also give us the length of many other things that we haven't met yet,
so we should always use it when we can.

> ## From 1 to N
>
> Python has a built-in function called `range` that creates a sequence of numbers. Range can
> accept 1-3 parameters. If one parameter is input, range creates an array of that length,
> starting at zero and incrementing by 1. If 2 parameters are input, range starts at
> the first and ends just before the second, incrementing by one. If range is passed 3 parameters,
> it starts at the first one, ends just before the second one, and increments by the third one. For
> example,
> `range(3)` produces the numbers 0, 1, 2, while `range(2, 5)` produces 2, 3, 4,
> and `range(3, 10, 3)` produces 3, 6, 9.
> Using `range`,
> write a loop that uses `range` to print the first 3 natural numbers:
>
> ~~~
> 1
> 2
> 3
> ~~~
> {: .python}
>
> > ## Solution
> > ~~~
> > for i in range(1, 4):
> >    print(i)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Computing Powers With Loops
>
> Exponentiation is built into Python:
>
> ~~~
> print(5 ** 3)
> ~~~
> {: .python}
>
> ~~~
> 125
> ~~~
> {: .output}
>
> Write a loop that calculates the same result as `5 ** 3` using
> multiplication (and without exponentiation).
>
> > ## Solution
> > ~~~
> > result = 1
> > for i in range(0, 3):
> >    result = result * 5
> > print(result)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Reverse a String
>
> Write a loop that takes a string,
> and produces a new string with the characters in reverse order,
> so `'Newton'` becomes `'notweN'`.
>
> > ## Solution
> > ~~~
> > newstring = ''
> > oldstring = 'Newton'
> > for char in oldstring:
> >    newstring = char + newstring
> > print(newstring)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Computing the Value of a Polynomial
>
> The built-in function `enumerate` takes a sequence (e.g. a list) and generates a
> new sequence of the same length. Each element of the new sequence contains the index
> (0,1,2,...) and the value from the original sequence:
>
> ~~~
> for i, x in enumerate(xs):
>     # Do something with i and x
> ~~~
> {: .python}
>
> The loop above assigns the index to `i` and the value to `x`.
>
> Suppose you have encoded a polynomial as a list of coefficients in
> the following way: the first element is the constant term, the
> second element is the coefficient of the linear term, the third is the
> coefficient of the quadratic term, etc.
>
> ~~~
> x = 5
> cc = [2, 4, 3]
> ~~~
> {: .python}
>
> ~~~
> y = cc[0] * x**0 + cc[1] * x**1 + cc[2] * x**2
> y = 97
> ~~~
> {: .output}
>
> Write a loop using `enumerate(cc)` which computes the value `y` of any
> polynomial, given `x` and `cc`.
>
> > ## Solution
> > ~~~
> > y = 0
> > for i, c in enumerate(cc):
> >     y = y + x**i * c
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}
