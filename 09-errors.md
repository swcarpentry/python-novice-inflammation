---
title: Errors and Exceptions
teaching: 30
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

- To be able to read a traceback, and determine where the error took place and what type it is.
- To be able to describe the types of situations in which syntax errors, indentation errors, name errors, index errors, and missing file errors occur.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How does Python report errors?
- How can I handle errors in Python programs?

::::::::::::::::::::::::::::::::::::::::::::::::::

Every programmer encounters errors,
both those who are just beginning,
and those who have been programming for years.
Encountering errors and exceptions can be very frustrating at times,
and can make coding feel like a hopeless endeavour.
However,
understanding what the different types of errors are
and when you are likely to encounter them can help a lot.
Once you know *why* you get certain types of errors,
they become much easier to fix.

Errors in Python have a very specific form,
called a [traceback](../learners/reference.md#traceback).
Let's examine one:

```python
# This code has an intentional error. You can type it directly or
# use it for reference to understand the error message below.
def favorite_ice_cream():
    ice_creams = [
        'chocolate',
        'vanilla',
        'strawberry'
    ]
    print(ice_creams[3])

favorite_ice_cream()
```

```error
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-1-70bd89baa4df> in <module>()
      9     print(ice_creams[3])
      10
----> 11 favorite_ice_cream()

<ipython-input-1-70bd89baa4df> in favorite_ice_cream()
      7         'strawberry'
      8     ]
----> 9     print(ice_creams[3])
      10
      11 favorite_ice_cream()

IndexError: list index out of range
```

This particular traceback has two levels.
You can determine the number of levels by looking for the number of arrows on the left hand side.
In this case:

1. The first shows code from the cell above,
  with an arrow pointing to Line 11 (which is `favorite_ice_cream()`).

2. The second shows some code in the function `favorite_ice_cream`,
  with an arrow pointing to Line 9 (which is `print(ice_creams[3])`).

The last level is the actual place where the error occurred.
The other level(s) show what function the program executed to get to the next level down.
So, in this case, the program first performed a
[function call](../learners/reference.md#function-call) to the function `favorite_ice_cream`.
Inside this function,
the program encountered an error on Line 6, when it tried to run the code `print(ice_creams[3])`.

:::::::::::::::::::::::::::::::::::::::::  callout

## Long Tracebacks

Sometimes, you might see a traceback that is very long
\-- sometimes they might even be 20 levels deep!
This can make it seem like something horrible happened,
but the length of the error message does not reflect severity, rather,
it indicates that your program called many functions before it encountered the error.
Most of the time, the actual place where the error occurred is at the bottom-most level,
so you can skip down the traceback to the bottom.


::::::::::::::::::::::::::::::::::::::::::::::::::

So what error did the program actually encounter?
In the last line of the traceback,
Python helpfully tells us the category or type of error (in this case, it is an `IndexError`)
and a more detailed error message (in this case, it says "list index out of range").

If you encounter an error and don't know what it means,
it is still important to read the traceback closely.
That way,
if you fix the error,
but encounter a new one,
you can tell that the error changed.
Additionally,
sometimes knowing *where* the error occurred is enough to fix it,
even if you don't entirely understand the message.

If you do encounter an error you don't recognize,
try looking at the
[official documentation on errors](https://docs.python.org/3/library/exceptions.html).
However,
note that you may not always be able to find the error there,
as it is possible to create custom errors.
In that case,
hopefully the custom error message is informative enough to help you figure out what went wrong.

:::::::::::::::::::::::::::::::::::::::  challenge

## Reading Error Messages

Read the Python code and the resulting traceback below, and answer the following questions:

1. How many levels does the traceback have?
2. What is the function name where the error occurred?
3. On which line number in this function did the error occur?
4. What is the type of error?
5. What is the error message?

```python
# This code has an intentional error. Do not type it directly;
# use it for reference to understand the error message below.
def print_message(day):
    messages = [
        'Hello, world!',
        'Today is Tuesday!',
        'It is the middle of the week.',
        'Today is Donnerstag in German!',
        'Last day of the week!',
        'Hooray for the weekend!',
        'Aw, the weekend is almost over.'
    ]
    print(messages[day])

def print_sunday_message():
    print_message(7)

print_sunday_message()
```

```error
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-7-3ad455d81842> in <module>
     16     print_message(7)
     17 
---> 18 print_sunday_message()
     19 

<ipython-input-7-3ad455d81842> in print_sunday_message()
     14 
     15 def print_sunday_message():
---> 16     print_message(7)
     17 
     18 print_sunday_message()

<ipython-input-7-3ad455d81842> in print_message(day)
     11         'Aw, the weekend is almost over.'
     12     ]
---> 13     print(messages[day])
     14 
     15 def print_sunday_message():

IndexError: list index out of range
```

:::::::::::::::  solution

## Solution

1. 3 levels
2. `print_message`
3. 13
4. `IndexError`
5. `list index out of range` You can then infer that
  `7` is not the right index to use with `messages`.
  
  

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Better errors on newer Pythons

Newer versions of Python have improved error printouts.  If you are debugging errors, it is often
helpful to use the latest Python version, even if you support older versions of Python.


::::::::::::::::::::::::::::::::::::::::::::::::::

## Syntax Errors

When you forget a colon at the end of a line,
accidentally add one space too many when indenting under an `if` statement,
or forget a parenthesis,
you will encounter a [syntax error](../learners/reference.md#syntax-error).
This means that Python couldn't figure out how to read your program.
This is similar to forgetting punctuation in English:
for example,
this text is difficult to read there is no punctuation there is also no capitalization
why is this hard because you have to figure out where each sentence ends
you also have to figure out where each sentence begins
to some extent it might be ambiguous if there should be a sentence break or not

People can typically figure out what is meant by text with no punctuation,
but people are much smarter than computers.
If Python doesn't know how to read the program,
it will give up and inform you with an error.
For example:

```python
def some_function()
    msg = 'hello, world!'
    print(msg)
     return msg
```

```error
  File "<ipython-input-3-6bb841ea1423>", line 1
    def some_function()
                       ^
SyntaxError: invalid syntax
```

Here, Python tells us that there is a `SyntaxError` on line 1,
and even puts a little arrow in the place where there is an issue.
In this case the problem is that the function definition is missing a colon at the end.

Actually, the function above has *two* issues with syntax.
If we fix the problem with the colon,
we see that there is *also* an `IndentationError`,
which means that the lines in the function definition do not all have the same indentation:

```python
def some_function():
    msg = 'hello, world!'
    print(msg)
     return msg
```

```error
  File "<ipython-input-4-ae290e7659cb>", line 4
    return msg
    ^
IndentationError: unexpected indent
```

Both `SyntaxError` and `IndentationError` indicate a problem with the syntax of your program,
but an `IndentationError` is more specific:
it *always* means that there is a problem with how your code is indented.

:::::::::::::::::::::::::::::::::::::::::  callout

## Tabs and Spaces

Some indentation errors are harder to spot than others.
In particular, mixing spaces and tabs can be difficult to spot
because they are both [whitespace](../learners/reference.md#whitespace).
In the example below, the first two lines in the body of the function
`some_function` are indented with tabs, while the third line — with spaces.
If you're working in a Jupyter notebook, be sure to copy and paste this example
rather than trying to type it in manually because Jupyter automatically replaces
tabs with spaces.

```python
def some_function():
	msg = 'hello, world!'
	print(msg)
        return msg
```

Visually it is impossible to spot the error.
Fortunately, Python does not allow you to mix tabs and spaces.

```error
  File "<ipython-input-5-653b36fbcd41>", line 4
    return msg
              ^
TabError: inconsistent use of tabs and spaces in indentation
```

::::::::::::::::::::::::::::::::::::::::::::::::::

## Variable Name Errors

Another very common type of error is called a `NameError`,
and occurs when you try to use a variable that does not exist.
For example:

```python
print(a)
```

```error
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-9d7b17ad5387> in <module>()
----> 1 print(a)

NameError: name 'a' is not defined
```

Variable name errors come with some of the most informative error messages,
which are usually of the form "name 'the\_variable\_name' is not defined".

Why does this error message occur?
That's a harder question to answer,
because it depends on what your code is supposed to do.
However,
there are a few very common reasons why you might have an undefined variable.
The first is that you meant to use a
[string](../learners/reference.md#string), but forgot to put quotes around it:

```python
print(hello)
```

```error
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-9553ee03b645> in <module>()
----> 1 print(hello)

NameError: name 'hello' is not defined
```

The second reason is that you might be trying to use a variable that does not yet exist.
In the following example,
`count` should have been defined (e.g., with `count = 0`) before the for loop:

```python
for number in range(10):
    count = count + number
print('The count is:', count)
```

```error
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-9-dd6a12d7ca5c> in <module>()
      1 for number in range(10):
----> 2     count = count + number
      3 print('The count is:', count)

NameError: name 'count' is not defined
```

Finally, the third possibility is that you made a typo when you were writing your code.
Let's say we fixed the error above by adding the line `Count = 0` before the for loop.
Frustratingly, this actually does not fix the error.
Remember that variables are [case-sensitive](../learners/reference.md#case-sensitive),
so the variable `count` is different from `Count`. We still get the same error,
because we still have not defined `count`:

```python
Count = 0
for number in range(10):
    count = count + number
print('The count is:', count)
```

```error
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-10-d77d40059aea> in <module>()
      1 Count = 0
      2 for number in range(10):
----> 3     count = count + number
      4 print('The count is:', count)

NameError: name 'count' is not defined
```

## Index Errors

Next up are errors having to do with containers (like lists and strings) and the items within them.
If you try to access an item in a list or a string that does not exist,
then you will get an error.
This makes sense:
if you asked someone what day they would like to get coffee,
and they answered "caturday",
you might be a bit annoyed.
Python gets similarly annoyed if you try to ask it for an item that doesn't exist:

```python
letters = ['a', 'b', 'c']
print('Letter #1 is', letters[0])
print('Letter #2 is', letters[1])
print('Letter #3 is', letters[2])
print('Letter #4 is', letters[3])
```

```output
Letter #1 is a
Letter #2 is b
Letter #3 is c
```

```error
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-11-d817f55b7d6c> in <module>()
      3 print('Letter #2 is', letters[1])
      4 print('Letter #3 is', letters[2])
----> 5 print('Letter #4 is', letters[3])

IndexError: list index out of range
```

Here,
Python is telling us that there is an `IndexError` in our code,
meaning we tried to access a list index that did not exist.

## File Errors

The last type of error we'll cover today
are those associated with reading and writing files: `FileNotFoundError`.
If you try to read a file that does not exist,
you will receive a `FileNotFoundError` telling you so.
If you attempt to write to a file that was opened read-only, Python 3
returns an `UnsupportedOperationError`.
More generally, problems with input and output manifest as
`OSError`s, which may show up as a more specific subclass; you can see
[the list in the Python docs](https://docs.python.org/3/library/exceptions.html#os-exceptions).
They all have a unique UNIX `errno`, which is you can see in the error message.

```python
file_handle = open('myfile.txt', 'r')
```

```error
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-14-f6e1ac4aee96> in <module>()
----> 1 file_handle = open('myfile.txt', 'r')

FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
```

One reason for receiving this error is that you specified an incorrect path to the file.
For example,
if I am currently in a folder called `myproject`,
and I have a file in `myproject/writing/myfile.txt`,
but I try to open `myfile.txt`,
this will fail.
The correct path would be `writing/myfile.txt`.
It is also possible that the file name or its path contains a typo.

A related issue can occur if you use the "read" flag instead of the "write" flag.
Python will not give you an error if you try to open a file for writing
when the file does not exist.
However,
if you meant to open a file for reading,
but accidentally opened it for writing,
and then try to read from it,
you will get an `UnsupportedOperation` error
telling you that the file was not opened for reading:

```python
file_handle = open('myfile.txt', 'w')
file_handle.read()
```

```error
---------------------------------------------------------------------------
UnsupportedOperation                      Traceback (most recent call last)
<ipython-input-15-b846479bc61f> in <module>()
      1 file_handle = open('myfile.txt', 'w')
----> 2 file_handle.read()

UnsupportedOperation: not readable
```

These are the most common errors with files,
though many others exist.
If you get an error that you've never seen before,
searching the Internet for that error type
often reveals common reasons why you might get that error.

:::::::::::::::::::::::::::::::::::::::  challenge

## Identifying Syntax Errors

1. Read the code below, and (without running it) try to identify what the errors are.
2. Run the code, and read the error message. Is it a `SyntaxError` or an `IndentationError`?
3. Fix the error.
4. Repeat steps 2 and 3, until you have fixed all the errors.

```python
def another_function
  print('Syntax errors are annoying.')
   print('But at least Python tells us about them!')
  print('So they are usually not too hard to fix.')
```

:::::::::::::::  solution

## Solution

`SyntaxError` for missing `():` at end of first line,
`IndentationError` for mismatch between second and third lines.
A fixed version is:

```python
def another_function():
    print('Syntax errors are annoying.')
    print('But at least Python tells us about them!')
    print('So they are usually not too hard to fix.')
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Identifying Variable Name Errors

1. Read the code below, and (without running it) try to identify what the errors are.
2. Run the code, and read the error message.
  What type of `NameError` do you think this is?
  In other words, is it a string with no quotes,
  a misspelled variable,
  or a variable that should have been defined but was not?
3. Fix the error.
4. Repeat steps 2 and 3, until you have fixed all the errors.

```python
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (Number % 3) == 0:
        message = message + a
    else:
        message = message + 'b'
print(message)
```

:::::::::::::::  solution

## Solution

3 `NameError`s for `number` being misspelled, for `message` not defined,
and for `a` not being in quotes.

Fixed version:

```python
message = ''
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + 'a'
    else:
        message = message + 'b'
print(message)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Identifying Index Errors

1. Read the code below, and (without running it) try to identify what the errors are.
2. Run the code, and read the error message. What type of error is it?
3. Fix the error.

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[4])
```

:::::::::::::::  solution

## Solution

`IndexError`; the last entry is `seasons[3]`, so `seasons[4]` doesn't make sense.
A fixed version is:

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[-1])
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::



:::::::::::::::::::::::::::::::::::::::: keypoints

- Tracebacks can look intimidating, but they give us a lot of useful information about what went wrong in our program, including where the error occurred and what type of error it was.
- An error having to do with the 'grammar' or syntax of the program is called a `SyntaxError`. If the issue has to do with how the code is indented, then it will be called an `IndentationError`.
- A `NameError` will occur when trying to use a variable that does not exist. Possible causes are that a variable definition is missing, a variable reference differs from its definition in spelling or capitalization, or the code contains a string that is missing quotes around it.
- Containers like lists and strings will generate errors if you try to access items in them that do not exist. This type of error is called an `IndexError`.
- Trying to read a file that does not exist will give you an `FileNotFoundError`. Trying to read a file that is open for writing, or writing to a file that is open for reading, will give you an `IOError`.

::::::::::::::::::::::::::::::::::::::::::::::::::


