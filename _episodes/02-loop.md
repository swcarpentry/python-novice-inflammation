---
title: Repeating Actions with Loops
teaching: 30
exercises: 0
questions:
- "How can I do the same operations on many different values?"
objectives:
- "Explain what a for loop does."
- "Correctly write for loops to repeat simple operations."
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
We may want to create plots for all of our data sets with a single statement instead of
writing each plot command separately. Alternatively, we may want to process each dataset
in some way and accumulate an aggregate result. As yet another idea we may want to take
a single representative dataset and systematically perturb or modify it in some way so as
to produce child datasets.

To do any of those specific cases or any other alternative scenario where repetitive but
systematic work is required, we'll have to teach the computer how to repeat things.

Let's first look at a fairly abstract scenario where we can disregard any complexities
associated with a specific domain of application. Later we will apply the loop construct
to a series of specific domain-relevant scenarios to help make the idea concrete.

Therefore, the example task that we will consider is the goal of printing each character in a
word on a line of its own.

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

This is a bad approach for two reasons:

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


> ## What's in a name?
>
> In the example above, the loop variable was given the name `char`
> as a mnemonic; it is short for 'character'.
> 'Char' is not a keyword in Python that pulls the characters
> from words or strings.
> In fact when a similar loop is run over a list rather than a word,
> the output would be each member of that list printed in order,
> rather than the characters.
>
> ~~~
> list = ['oxygen','nitrogen','argon']
> for char in list:
>    print(char)
> ~~~
> {: .python}
>
> ~~~
> oxygen
> nitrogen
> argon
> ~~~
> {: .output}
>
> We can choose any name we want for variables.
> We might just as easily have chosen the name `banana`
> for the loop variable,
> as long as we use the same name when we invoke the variable inside the loop:
>
> ~~~
> word = 'oxygen'
> for banana in word:
>     print(banana)
> ~~~
> {: .python}
>
> ~~~
> o
> x
> y
> g
> e
> n
> ~~~
> {: .output}
>
> It is a good idea to choose variable names
> that are meaningful so that it is easier
> to understand what the loop is doing.
{: .callout}

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

> ## Modifying a Dataset With Loops
>
> In the previous lesson on Analyzing Patient Data we used a numpy array to hold
> patient information. Let's imagine that we would like to subtract the average
> value of the data from each element in the array:
>
> First, we will need to create a dataset to play with.
> ~~~
> import numpy as np
> patient_data = np.array([0.0, 0.0, 1.0, 1.0, 5.0, 4.0, 3.0, 6.0, 7.0, 3.0, 2.0, 1.0, 2.0, 0.0, 0.0])
> ~~~
> {: .python}
>
> Then, we will need to compute the average value.
> ~~~
> average = np.average(patient_data)
> ~~~
> {: .output}
>
> Now, we can pursue our goal. Your assignment is to write a loop that will subtract the average
> value from each element of the patient_data array. You may want to print the array contents both
> before and after to make sure that the result is correct.
>
> > ## Solution
> > There are multiple ways to solve this problem and number of interesting general programming
> > and Python specific things that the solutions to this exercise can illustrate.
> >
> > Here is one fairly explicit solution that follows a traditional programming paradigm.
> > ~~~
> > import numpy as np
> > patient_data = np.array([0.0, 0.0, 1.0, 1.0, 5.0, 4.0, 3.0, 6.0, 7.0, 3.0, 2.0, 1.0, 2.0, 0.0, 0.0])
> > print(patient_data)
> > average = np.average(patient_data)
> > print(average)
> > for i in range(0, np.size(patient_data)):
> >    patient_data[i] = patient_data[i] - average
> > print(patient_data)
> > ~~~
> > {: .python}
> >
> > Here is another solution that makes use of the -= operator.
> > ~~~
> > import numpy as np
> > patient_data = np.array([0.0, 0.0, 1.0, 1.0, 5.0, 4.0, 3.0, 6.0, 7.0, 3.0, 2.0, 1.0, 2.0, 0.0, 0.0])
> > print(patient_data)
> > average = np.average(patient_data)
> > print(average)
> > for i in range(0, np.size(patient_data)):
> >    patient_data[i] -= average
> > print(patient_data)
> > ~~~
> > {: .python}
> > By using the -= operation we only need to write the name of the variable to be modified once.
> > This is particularly useful for any kind of modification and you may use it with other operations
> > such as addition (+=), multiplication (*=), and division (/=).
> {: .solution}
{: .challenge}

> ## List Comprehensions as a Loop Construct
> An important concept that applies to Python (as well as many other high-level languages) is that
> the language often offers special syntax to the programmer to carry out very common types of
> operations. If the programmer uses the special syntax, then the operations may be carried out
> by the computer much faster than if a traditional (usually very explicit) form were used.
> 
> Loops over arrays are extremely common and so Python has a special syntax called a
> List Comprehension for performing array operations. A List Comprehension takes the following
> form: new_list = [<operation on item> for <item> in current list]
>
> Try to solve the same problem as the previous exercise, except this time use a List
> Comprehension.
> > ## Solution
> > ~~~
> > import numpy as np
> > patient_data = np.array([0.0, 0.0, 1.0, 1.0, 5.0, 4.0, 3.0, 6.0, 7.0, 3.0, 2.0, 1.0, 2.0, 0.0, 0.0])
> > print(patient_data)
> > average = np.average(patient_data)
> > print(average)
> > patient_data = np.array([datum-average for datum in patient_data])
> > print(patient_data)
> > ~~~
> > {: .python}
> >
> > It is not important that you master List Comprehensions at this time, but it is important that
> > you are aware that they exist. The reason is that the speed with which Python is able to perform
> > operations using a List Comprehension form of an loop is much faster
> {: .solution}
{: .challenge}

> ## Nesting Loops
>
> Another extremely important concept in programming is the idea that one block of operations can
> be embedded within another block. Loops can be embedded within loops, if-then-else statements
> (which you will see in another lesson) can be embedded within other if-then-else statement.
> Loops can be embedded within if-then-else statements and vice-versa, etc. This concept of
> embedding allows fairly complicated actions to be performed. In this assignment your goal is to
> embed a loop within a loop to deal with the scenario that instead of having one array holding
> data for one patient, we now have an array of arrays that holds patient data for many patients.
>
> We can load the sample data that was used in the previous lesson:
> ~~~
> patients_data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
> print(patients_data)
> ~~~
> {: .python}
>
> As you formulate your solution, keep in mind that you when using the traditional loop constructs
> you will need to have a different index variable for each loop. Perhaps 'i' for the first loop
> and 'j' for the second. Also, you will need to compute the average separately for each patient.
> Thus, average is computed after the start of the outer loop but before the start of the inner
> loop. There are two other bits of technical complication: (1) To access an element of a multi-
> dimensional array, use the form: "array[i,j]"; and (2) To compute the number of elements in a
> particular dimension (dim) of a multidimensional array, use the form: "np.size(array,dim)".
>
> > ## Solution
> > ~~~
> > import numpy as np
> > patients_data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
> > print(patients_data)
> > for i in range(0, np.size(patients_data,0)):
> >    average = np.average(patients_data[i])
> >    for j in range (0, np.size(patients_data,1)):
> >       patients_data[i,j] -= average
> > print(patients_data)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}
