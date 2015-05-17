---
layout: page
title: Programming with Python
subtitle: Instructor's Guide
---
## Legend

We are using a dataset with records on inflammation from patients following an
arthritis treatment.

We make reference in the lesson that this data is somehow strange. It is strange
because it is fabricated! The script used to generate the inflammation data
is included as [`tools/gen_inflammation.py`](tools/gen_inflammation.py).

## Overall

This lesson is written as an introduction to Python,
but its real purpose is to introduce the single most important idea in programming:
how to solve problems by building functions,
each of which can fit in a programmer's working memory.
In order to teach that,
we must teach people a little about
the mechanics of manipulating data with lists and file I/O
so that their functions can do things they actually care about.
Our teaching order tries to show practical uses of every idea as soon as it is introduced;
instructors should resist the temptation to explain
the "other 90%" of the language
as well.

The final example asks them to build a command-line tool
that works with the Unix pipe-and-filter model.
We do this because it is a useful skill
and because it helps learners see that the software they use isn't magical.
Tools like `grep` might be more sophisticated than
the programs our learners can write at this point in their careers,
but it's crucial they realize this is a difference of scale rather than kind.

Explain that we use Python because:

*   It's free.
*   It has a lot of scientific libraries, and more are constantly being added.
*   It has a large scientific user community.
*   It's easier for novices to learn than most of the mature alternatives.
    (Software Carpentry originally used Perl;
    when we switched,
    we found that we could cover as much material in two days in Python
    as we'd covered in three days in Perl,
    and that retention was higher.)

We do *not* include instructions on running the IPython Notebook in the tutorial
because we want to focus on the language rather than the tools.
Instructors should, however, walk learners through some basic operations:
*   Launch from the command line with `ipython notebook`.
*   Create a new notebook.
*   Enter code or data in a cell and execute it.
*   Explain the difference between `In[#]` and `Out[#]`.

Watching the instructor grow programs step by step
is as helpful to learners as anything to do with Python.
Resist the urge to update a single cell repeatedly
(which is what you'd probably do in real life).
Instead,
clone the previous cell and write the update in the new copy
so that learners have a complete record of how the program grew.
Once you've done this,
you can say,
"Now why don't we just break things into small functions right from the start?"

The discussion of command-line scripts
assumes that students understand standard I/O and building filters,
which are covered in the lesson on the shell.

## Frequently Argued Issues (FAI)

*   `import ... as ...` syntax.

    This syntax is commonly used in the scientific Python community;
    it is explicitly recommended in documentation to `import numpy as np`
    and `import matplotlib.pyplot as plt`. Despite that, we have decided
    not to introduce aliasing imports in this novice lesson due to the
    additional cognitive load it puts on students, despite the typing that
    it saves. A good summary of arguments for and against can be found in
    [PR #61](https://github.com/swcarpentry/python-novice-inflammation/pull/61).

    It is up to you as an individual instructor whether you want to introduce
    these aliases when you teach this lesson, but we encourage you to please
    read those arguments thoroughly before deciding one way or the other.

## [Analyzing Patient Data](01-numpy.html)

## [Repeating Actions with Loops](02-loop.html)

Solutions to exercises:

> ## From 1 to N {.challenge}
> Using `range`,
> write a loop that uses `range` to print the first 3 natural numbers:
>
> ~~~ {.python}
> for i in range(1,4):
>    print i
> 1
> 2
> 3
> ~~~

> ## Computing powers with loops {.challenge}
> Write a loop to calculate 5**3.
> ~~~ {.python}
> result = 1
> for i in range(0,3):
>    result = result*5
> print result
> 125
> ~~~

> ## Reverse a string {.challenge}
>
> Write a loop that takes a string,
> and produces a new string with the characters in reverse order.
> ~~~ {.python}
> newstring = ""
> oldstring = "Newton"
> for c in range(len(oldstring)-1,-1,-1):
>    newstring = newstring + oldstring[c]
> print result
> "notweN"
> ~~~

After discussing these challenges could be a good time to introduce the `b*=2` syntax.

## [Storing Multiple Values in Lists](03-lists.html)

## [Analyzing Data from Multiple Files](04-files.html)

## [Making Choices](05-cond.html)
> ## How many paths? {.challenge}
>
> Which of the following would be printed if you were to run this code? Why did you pick this answer?
>
> ~~~ {.python}
> if 4 > 5:
>     print 'A'
> elif 4 == 5:
>     print 'B'
> elif 4 < 5:
>     print 'C'
> C
> ~~~

> ## What is truth? {.challenge}
>
> After reading and running the code below,
> explain the rules for which values are considered true and which are considered false.
> (Note that if the body of a conditional is a single statement, we can write it on the same line as the `if`.)
>
> ~~~ {.python}
> if '': print 'empty string is true'
> 
> if 'word': print 'word is true'
> word is true
> if []: print 'empty list is true'
> 
> if [1, 2, 3]: print 'non-empty list is true'
> non-empty list is true
> if 0: print 'zero is true'
>
> if 1: print 'one is true'
>
> ~~~
> False values: 0, empty string, empty list. True values: 1, non-empty lists or strings.

> ## Close enough {.challenge}
>
> Write some conditions that print `True` if the variable `a` is within 10% of the variable `b`
> and `False` otherwise.
> ~~~ {.python}
> a = 5
> b = 5.1
>
> if abs(a-b) < 0.1*abs(b):
>     print 'True'
> else:
>     print 'False'
> ~~~
> Another possible solution:
> ~~~ {.python}
> print abs(a-b) < 0.1*abs(b)
> ~~~
> This works because the Boolean objects `True` and `False` have string representations which can be `print`ed.


> ## In-place operators {.challenge}
>
> Write some code that sums the positive and negative numbers in a list separately,
> using in-place operators.
> ~~~ {.python}
> positive_sum = 0
> negative_sum = 0
> test_list = [3,4,6,1,-1,-5,0,7,-8]
> for num in test_list:
>     if num > 0:
>         positive_sum += num
>     elif num == 0:
>         pass
>     else:
>         negative_sum += num
> print positive_sum, negative_sum
> 21 -14
> ~~~ 
> Here `pass` means "don't do anything". In this particular case, it's not actually needed, since if `num==0` neither 
> sum needs to change, but it illustrates the use of `elif`.

> ## Tuples and exchanges {.challenge}
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
> Answer: swaps contents of variables right and left.
> Compare it to:
>
> ~~~ {.python}
> left, right = right, left
> ~~~
>
> Do they always do the same thing?
> Answer: Yes, although it's possible the internal implementation is different.
> Which do you find easier to read?
> Answers may vary..

## [Creating Functions](06-func.html)

> ## Combining strings {.challenge}
>
> Write a function called `fence` that takes two parameters called `original` and `wrapper`
> and returns a new string that has the wrapper character at the beginning and end of the original.
>
> ~~~ {.python}
> def fence(original, wrapper):
>     return wrapper + original + wrapper
> ~~~

> ## Selecting characters from strings {.challenge}
>
> Write a function called `outer`
> that returns a string made up of just the first and last characters of its input.
>
> ~~~ {.python}
> def outer(input_string):
>     return input_string[0] + input_string[-1]
> ~~~

> ## Rescaling, with parameters {.challenge}
>
> Rewrite the `rescale` function so that it scales data to lie between 0.0 and 1.0 by default,
> but will allow the caller to specify lower and upper bounds if they want.
> FIXME: looks like the rescale function is no longer in the lesson? FIXME

> ## Testing your function {.challenge}
>
> Run the commands `help(numpy.arange)` and `help(numpy.linspace)`
> to see how to use these functions to generate regularly-spaced values,
> then use those values to test your `rescale` function.
> FIXME: looks like the rescale function is no longer in the lesson? FIXME

> ## Variables inside and outside functions {.challenge}
>
> What does the following piece of code display when run - and why?
>
> ~~~ {.python}
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
> print k
> 0
> ~~~
> 
> Answer: displays 0 because the `k` inside the function `f2k` doesn't know about the `k` defined outside the function.


## [Errors and Exceptions](07-errors.html)

> ## Reading Error Messages {.challenge}
>
> Read the traceback below, and identify the following pieces of information about it:
>
> 1.  How many levels does the traceback have?
> 2.  What is the file name where the error occurred?
> 3.  What is the function name where the error occurred?
> 4.  On which line number in this function did the error occurr?
> 5.  What is the type of error?
> 6.  What is the error message?
>
> ~~~ {.python}
> import errors_02
> errors_02.print_friday_message()
> ~~~
> ~~~ {.error}
> ---------------------------------------------------------------------------
> KeyError                                  Traceback (most recent call last)
> <ipython-input-2-e4c4cbafeeb5> in <module>()
>       1 import errors_02
> ----> 2 errors_02.print_friday_message()
>
> /Users/jhamrick/project/swc/novice/python/errors_02.py in print_friday_message()
>      13
>      14 def print_friday_message():
> ---> 15     print_message("Friday")
>
> /Users/jhamrick/project/swc/novice/python/errors_02.py in print_message(day)
>       9         "sunday": "Aw, the weekend is almost over."
>      10     }
> ---> 11     print messages[day]
>      12
>      13
>
> KeyError: 'Friday'
> ~~~
> Answer:
>
> 1. 3 levels
> 2. `errors_02.py`
> 3. `print_message`
> 4. 11
> 5. `KeyError`
> 6. There isn't much of a message; you're supposed to infer that `Friday` is not a key in `messages`.



> ## Identifying Syntax Errors {.challenge}
>
> 1. Read the code below, and (without running it) try to identify what the errors are.
> 2. Run the code, and read the error message. Is it a `SyntaxError` or an `IndentationError`?
> 3. Fix the error.
> 4. Repeat steps 2 and 3, until you have fixed all the errors.
>
> ~~~ {.python}
> def another_function
>   print "Syntax errors are annoying."
>    print "But at least python tells us about them!"
>   print "So they are usually not too hard to fix."
> ~~~
> Answer: `SyntaxError` for missing `:()` at end of first line, `IndentationError` for mismatch between second and third lines.
> ~~~ {.python}
> def another_function():
>   print "Syntax errors are annoying."
>   print "But at least python tells us about them!"
>   print "So they are usually not too hard to fix."
> ~~~

> ## Identifying Variable Name Errors {.challenge}
>
> 1. Read the code below, and (without running it) try to identify what the errors are.
> 2. Run the code, and read the error message. What type of `NameError` do you think this is? In other words, is it a string with no quotes, a misspelled variable, or a variable that should have been defined but was not?
> 3. Fix the error.
> 4. Repeat steps 2 and 3, until you have fixed all the errors.
>
> ~~~ {.python}
> for number in range(10):
>     # use a if the number is a multiple of 3, otherwise use b
>     if (Number % 3) == 0:
>         message = message + a
>     else:
>         message = message + "b"
> print message
> ~~~
> Answer: 3 `NameError`s for `number` being misspelled, for `message` not defined, and for `a` not being in quotes.  
> ~~~ {.python}
> message = ""
> for number in range(10):
>     # use a if the number is a multiple of 3, otherwise use b
>     if (Number % 3) == 0:
>         message = message + "a"
>     else:
>         message = message + "b"
> print message
> abbabbabba

> ## Identifying Item Errors {.challenge}
>
> 1. Read the code below, and (without running it) try to identify what the errors are.
> 2. Run the code, and read the error message. What type of error is it?
> 3. Fix the error.
>
> ~~~ {.python}
> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
> print 'My favorite season is ', seasons[4]
> ~~~
> Answer: IndexError; the last entry is `seasons[3]`, so `seasons[4]` doesn't make sense.
> ~~~ {.python}
> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
> print 'My favorite season is ', seasons[-1]
> ~~~

## [Defensive Programming](08-defensive.html)

## [Debugging](09-debugging.html)

## [Command-Line Programs](10-cmdline.html)
