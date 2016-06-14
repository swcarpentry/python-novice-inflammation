---
layout: page
title: Programming with Python
subtitle: Making Choices
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Write conditional statements including `if`, `elif`, and `else` branches.
> *   Correctly evaluate expressions containing `and` and `or`.

In our last lesson, we discovered something suspicious was going on
in our inflammation data by drawing some plots.
How can we use Python to automatically recognize the different features we saw,
and take a different action for each? In this lesson, we'll learn how to write code that
runs only when certain conditions are true.

## Conditionals

We can ask Python to take different actions, depending on a condition, with an `if` statement:

~~~ {.python}
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')
~~~
~~~ {.output}
not greater
done

~~~

The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows the `if` statement is true,
the body of the `if`
(i.e., the lines indented underneath it) are executed.
If the test is false,
the body of the `else` is executed instead.
Only one or the other is ever executed:

![Executing a Conditional](fig/python-flowchart-conditional.png)\

Conditional statements don't have to include an `else`.
If there isn't one,
Python simply does nothing if the test is false:

~~~ {.python}
num = 53
print('before conditional...')
if num > 100:
    print('53 is greater than 100')
print('...after conditional')
~~~
~~~ {.output}
before conditional...
...after conditional
~~~

We can also chain several tests together using `elif`,
which is short for "else if".
The following Python code uses `elif` to print the sign of a number.

~~~ {.python}
num = -3

if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative")
~~~
~~~ {.output}
"-3 is negative"
~~~

One important thing to notice in the code above is that we use a double equals sign `==` to test for equality
rather than a single equals sign
because the latter is used to mean assignment.

We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:

~~~ {.python}
if (1 > 0) and (-1 > 0):
    print('both parts are true')
else:
    print('at least one part is false')
~~~
~~~ {.output}
at least one part is false
~~~

while `or` is true if at least one part is true:

~~~ {.python}
if (1 < 0) or (-1 < 0):
    print('at least one test is true')
~~~
~~~ {.output}
at least one test is true
~~~

## Checking our Data

Now that we've seen how conditionals work,
we can use them to check for the suspicious features we saw in our inflammation data.
In the first couple of plots, the maximum inflammation per day
seemed to rise like a straight line, one unit per day.
We can check for this inside the `for` loop we wrote with the following conditional:

~~~ {.python}
if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
    print('Suspicious looking maxima!')
~~~

We also saw a different problem in the third dataset;
the minima per day were all zero (looks like a healthy person snuck into our study).
We can also check for this with an `elif` condition:

~~~{.python}
elif data.min(axis=0).sum() == 0:
    print('Minima add up to zero!')
~~~

And if neither of these conditions are true, we can use `else` to give the all-clear:

~~~ {.python}
else:
    print('Seems OK!')
~~~

Let's test that out:

~~~ {.python}
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
    print('Suspicious looking maxima!')
elif data.min(axis=0).sum() == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')
~~~

~~~ {.output}
Suspicious looking maxima!
~~~

~~~ {.python}
data = numpy.loadtxt(fname='inflammation-03.csv', delimiter=',')
if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
    print('Suspicious looking maxima!')
elif data.min(axis=0).sum() == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')
~~~

~~~ {.output}
Minima add up to zero!
~~~

In this way,
we have asked Python to do something different depending on the condition of our data.
Here we printed messages in all cases,
but we could also imagine not using the `else` catch-all
so that messages are only printed when something is wrong,
freeing us from having to manually examine every plot for features we've seen before.

> ## How many paths? {.challenge}
>
> Which of the following would be printed if you were to run this code? Why did you pick this answer?
>
> 1.  A
> 2.  B
> 3.  C
> 4.  B and C
>
> ~~~ {.python}
> if 4 > 5:
>     print('A')
> elif 4 == 5:
>     print('B')
> elif 4 < 5:
>     print('C')
> ~~~

> ## What is truth? {.challenge}
>
> `True` and `False` are special words in Python called `booleans` which represent true
and false statements. However, they aren't the only values in Python that are true and false.
> In fact, *any* value can be used in an `if` or `elif`.
> After reading and running the code below,
> explain what the rule is for which values are considered true and which are considered false.
>
> ~~~ {.python}
> if '':
>     print('empty string is true')
> if 'word':
>     print('word is true')
> if []:
>     print('empty list is true')
> if [1, 2, 3]:
>     print('non-empty list is true')
> if 0:
>     print('zero is true')
> if 1:
>     print('one is true')
> ~~~

> ## not not True is True {.challenge}
>
> Sometimes it is useful to check whether some condition is not true.
> The special word `not` can do this explicitly.
> After reading and running the code below,
> write some conditions that use `not` to test the rule you formulated in the previous challenge.
>
> ~~~ {.python}
> if not '':
>     print('empty string is not true')
> if not 'word':
>     print('word is not true')
> if not not True:
>     print('not not True is true')
> ~~~
 

> ## Close enough {.challenge}
>
> Write some conditions that print `True` if the variable `a` is within 10% of the variable `b`
> and `False` otherwise.
> Compare your implementation with your partner's:
> do you get the same answer for all possible pairs of numbers?

> ## New Question, combining concepts {.challenge}
> 
> Now that you have learned about conditions and loops we can combine these concepts to look
> at another type of loop: while loops. The structure is exactly like an if state the only difference
> being that it will repeat what is within your loop until your condition becomes false. 
> Try the following:
> * Create a list that contains the following five numbers: [2,3,5,6,9]
> * Create a variable and set it equal to zero, we will use this to point at the numbers in your list
> * Create a condition that checks if the current value we are pointing to in your list is less than 6, 
> and place it as if you were writing an if state except that instead of 'if' use the word 'while'
> * Print the number that is being compared inside the loop
> * Lastly, remember to iterate your variable otherwise you will end up with an infinite loop
> 
> This type of loop is useful in cases where you do not know exactly how many times you need to repeat your
> loop contents.


> ## In-place operators {.challenge}
>
> Python (and most other languages in the C family) provides [in-place operators](reference.html#in-place-operators)
> that work like this:
>
> ~~~ {.python}
> x = 1  # original value
> x += 1 # add one to x, assigning result back to x
> x *= 3 # multiply x by 3
> print(x)
> ~~~
> ~~~ {.output}
> 6
> ~~~
>
> Write some code that sums the positive and negative numbers in a list separately,
> using in-place operators.
> Do you think the result is more or less readable than writing the same without in-place operators?

> ## Tuples and Exchanges {.challenge}
>
> Explain what the overall effect of this code is:
>
> ~~~ {.python}
> left = 'L'
> right = 'R'
>
> temp = left
> left = right
> right = temp
> ~~~
>
> Compare it to:
>
> ~~~ {.python}
> left, right = right, left
> ~~~
>
> Do they always do the same thing?
> Which do you find easier to read?

> ## Sorting a List Into Buckets {.challenge}
>
> The folder containing our data files has large data sets whose names start with
> "inflammation-", small ones whose names with "small-", and possibly other files
> whose sizes we don't know.  Our goal is to sort those files into three lists
> called `large_files`, `small_files`, and `other_files` respectively.  Add code
> to the template below to do this.  Note that the string method
> [`startswith`](https://docs.python.org/3.5/library/stdtypes.html#str.startswith)
> returns `True` if and only if the string it is called on starts with the string
> passed as an argument.
>
> ~~~ {.python}
> files = ['inflammation-01.csv', 'myscript.py', 'inflammation-02.csv', 'small-01.csv', 'small-02.csv']
> large_files = []
> small_files = []
> other_files = []
> ~~~
>
> Your solution should:
>
> 1.  loop over the names of the files
> 2.  figure out which group each filename belongs
> 3.  append the filename to that list
>
> In the end the three lists should be:
>
> ~~~ {.python}
> large_files = ['inflammation-01.csv', 'inflammation-02.csv']
> small_files = ['small-01.csv', 'small-02.csv']
> other_files = ['myscript.py']
> ~~~

> ## Counting Vowels {.challenge}
>
> 1.  Write a loop that counts the number of vowels in a character string.
>
> 2. Test it on a few individual words and full sentences.
>
> 3. Once you are done, compare your solution to your neighbor's.
>    Did you make the same decisions about how to handle the letter 'y'
>    (which some people think is a vowel, and some do not)?
