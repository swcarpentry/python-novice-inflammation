---
layout: lesson
root: ../..
---

## Python errors and exceptions


Every programmer encounters errors, both those who are just beginning, and those who have been programming for years. Encountering errors and exceptions can be very frustrating at times, and can make coding feel like a hopeless endeavour. However, understanding what the **different types of errors** are and when you are likely to encounter them can help a lot! Once you know *why* you get certain types of errors, they become much easier to fix.


<div class="objectives" markdown="1">
#### Objectives

*   To be able to read a traceback, and determine the following relevant pieces of information:
    * The file, function, and line number on which the error occurred
    * The type of the error
    * The error message
*   To be able to describe the types of situations in which the following errors occur:
    * `SyntaxError` and `IndentationError`
    * `NameError`
    * `KeyError` and `IndexError`
    * `IOError`
</div>

### The anatomy of an error


Errors in Python have a very specific form, called a [traceback](../../gloss.html#traceback). Let's examine one:


<pre class="in"><code>from errors_01 import favorite_ice_cream
favorite_ice_cream()</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
&lt;ipython-input-1-9d0462a5b07c&gt; in &lt;module&gt;()
      1 from errors_01 import favorite_ice_cream
----&gt; 2 favorite_ice_cream()

/Users/jhamrick/project/swc/novice/python/errors_01.pyc in favorite_ice_cream()
      5         &#34;strawberry&#34;
      6     ]
----&gt; 7     print ice_creams[3]

IndexError: list index out of range</code></pre></div>


This particular traceback has two levels. You can determine the number of levels by looking for the number of arrows on the left hand side. In this case:

1. The first shows code from the cell above, with an arrow pointing to Line 2 (which is `favorite_ice_cream()`).
2. The second shows some code in another function (`favorite_ice_cream`, located in the file `errors_01.py`), with an arrow pointing to Line 7 (which is `print ice_creams[3]`).

The last level is the actual place where the error occurred. The other level(s) show what function the program executed to get to the next level down. So, in this case, the program first performed a [function call](../../gloss.html#function-call) to the function `favorite_ice_cream`. Inside this function, the program encountered an error on Line 7, when it tried to run the code `print ice_creams[3]`.

> #### Long tracebacks
> Sometimes, you might see a traceback that is very long -- sometimes they might even be 20 levels deep! This can make it seem like something horrible happened, but really it just means that your program called many functions before it ran into the error. Most of the time, you can just pay attention to the bottom-most level, which is the actual place where the error occurred.

So what error did the program actually encounter? In the last line of the traceback, Python helpfully tells us the category or **type of error** (in this case, it is an `IndexError`) and a more detailed **error message** (in this case, it says "list index out of range"). 

If you encounter an error and don't know what it means, it is still important to read the traceback closely. That way, if you fix the error, but encounter a new one, you can tell that the error changed! Additionally, sometimes just knowing *where* the error occurred is enough to fix it, even if you don't entirely understand the message.

If you do encounter an error you don't recognize, try looking at the [official documentation on errors](http://docs.python.org/2/library/exceptions.html). However, note that you may not always be able to find the error there, as it is possible to create custom errors. In that case, hopefully the custom error message is informative enough to help you figure out what went wrong!


<div class="challenges" markdown="1">
#### Challenge: reading error messages

Read the traceback below, and identify the following pieces of information about it:

1.  How many **levels** does the traceback have?
2.  What is the **file name** where the error occurred?
3.  What is the **function name** where the error occurred?
4.  On which **line number** in this function did the error occurr?
5.  What is the **type of error**?
6.  What is the **error message**?
</div>


<pre class="in"><code>from errors_02 import print_friday_message
print_friday_message()</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
&lt;ipython-input-2-e4c4cbafeeb5&gt; in &lt;module&gt;()
      1 from errors_02 import print_friday_message
----&gt; 2 print_friday_message()

/Users/jhamrick/project/swc/novice/python/errors_02.py in print_friday_message()
     13 
     14 def print_friday_message():
---&gt; 15     print_message(&#34;Friday&#34;)

/Users/jhamrick/project/swc/novice/python/errors_02.py in print_message(day)
      9         &#34;sunday&#34;: &#34;Aw, the weekend is almost over.&#34;
     10     }
---&gt; 11     print messages[day]
     12 
     13 

KeyError: &#39;Friday&#39;</code></pre></div>

### Syntax errors


When you forget a colon at the end of a line, accidentally add one space too many when indenting under an `if` statement, or forget a parentheses, you will encounter a **syntax error**. This means that Python couldn't figure out how to read your program. This is similar to forgetting punctuation in English:

> this text is difficult to read there is no punctuation there is also no capitalization why is this hard because you have to figure out where each sentence ends you also have to figure out where each sentence begins to some extent it might be ambiguous if there should be a sentence break or not

People can typically figure out what is meant by text with no punctuation, but people are much smarter than computers! If Python doesn't know how to read the program, it will just give up, and inform you with an error. For example:


<pre class="in"><code>def some_function()
    msg = &#34;hello, world!&#34;
    print msg
     return msg</code></pre>

<div class="out"><pre class='err'><code>  File &#34;&lt;ipython-input-3-6bb841ea1423&gt;&#34;, line 1
    def some_function()
                       ^
SyntaxError: invalid syntax
</code></pre></div>


Here, Python tells us that there is a `SyntaxError` on line 1, and even puts a little arrow in the place where there is an issue. In this case, the problem is that the function definition is missing a colon at the end.

Actually, the function above has *two* issues with syntax. If we fix the problem with the colon, we see that there is *also* an `IndentationError`, which means that the lines in the function definition do not all have the same indentation:


<pre class="in"><code>def some_function():
    msg = &#34;hello, world!&#34;
    print msg
     return msg</code></pre>

<div class="out"><pre class='err'><code>  File &#34;&lt;ipython-input-4-ae290e7659cb&gt;&#34;, line 4
    return msg
    ^
IndentationError: unexpected indent
</code></pre></div>


Both `SyntaxError` and `IndentationError` indicate a problem with the syntax of your program, but an `IndentationError` is more specific: it *always* means that there is a problem with how your code is indented.


#### Whitespace: tabs and spaces

A quick note on indentation errors: they can sometimes be insidious, especially if you are mixing spaces and tabs. Because they are both "whitespace", it is difficult to visually tell the difference! The IPython notebook actually gives us a bit of a hint, but not all Python editors will do that. In the following example, the first two lines are using a tab for indentation, while the third line uses four spaces.


<pre class="in"><code>def some_function():
	msg = &#34;hello, world!&#34;
	print msg
    return msg</code></pre>

<div class="out"><pre class='err'><code>  File &#34;&lt;ipython-input-5-653b36fbcd41&gt;&#34;, line 4
    return msg
              ^
IndentationError: unindent does not match any outer indentation level
</code></pre></div>


By default, one tab is equivalent to eight spaces, so the only way to mix tabs and spaces is to make it look like this! In general, is is better to just **never use tabs** and **always use spaces**, because it can make things very confusing.


<pre class="in"><code>def some_function():
	msg = &#34;hello, world!&#34;
	print msg
        return msg</code></pre>


<div class="challenges" markdown="1">
#### Challenge: identifying syntax errors

1. Read the code below, and (without running it) try to identify what the errors are.
2. Run the cell, and read the error message. Is it a `SyntaxError` or an `IndentationError`?
3. Fix the error.
4. Repeat steps 2 and 3, until you have fixed all the errors.
</div>


<pre class="in"><code>def another_function
  print &#34;Syntax errors are annoying.&#34;
   print &#34;But at least python tells us about them!&#34;
  print &#34;So they are usually not too hard to fix.&#34;</code></pre>

### Variable name errors


Another very common type of error is called a `NameError`, and occurs when you try to use a variable that does not exist. For example:


<pre class="in"><code>print a</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-7-9d7b17ad5387&gt; in &lt;module&gt;()
----&gt; 1 print a

NameError: name &#39;a&#39; is not defined</code></pre></div>


Variable name errors come with some of the most informative error messages, which are usually of the form "name 'the_variable_name' is not defined".

*Why* does this error message occur? That's harder question to answer, because it depends on what your code is supposed to do. However, there are a few very common reasons why you might have an undefined variable. The first is that you meant to use a [string](../../gloss.html#string), but forgot to put quotes around it:


<pre class="in"><code>print hello</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-8-9553ee03b645&gt; in &lt;module&gt;()
----&gt; 1 print hello

NameError: name &#39;hello&#39; is not defined</code></pre></div>


The second is that you just forgot to create the variable before using it. In the following example, `count` should have been defined (e.g., with `count = 0`) before the for loop:


<pre class="in"><code>for number in range(10):
    count = count + number
print &#34;The count is: &#34; + str(count)</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-9-dd6a12d7ca5c&gt; in &lt;module&gt;()
      1 for number in range(10):
----&gt; 2     count = count + number
      3 print &#34;The count is: &#34; + str(count)

NameError: name &#39;count&#39; is not defined</code></pre></div>


Finally, the third possibility is that you made a typo when you were writing your code. Let's say we fixed the error above by adding the line `Count = 0` before the for loop. Frustratingly, this actually does not fix the error! Remember that variables are [case-sensitive](../../gloss.html#case-sensitive), so the variable `count` is different from `Count`. We still get the same error, because we still have not defined `count`:


<pre class="in"><code>Count = 0
for number in range(10):
    count = count + number
print &#34;The count is: &#34; + str(count)</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-10-d77d40059aea&gt; in &lt;module&gt;()
      1 Count = 0
      2 for number in range(10):
----&gt; 3     count = count + number
      4 print &#34;The count is: &#34; + str(count)

NameError: name &#39;count&#39; is not defined</code></pre></div>


<div class="challenges" markdown="1">
#### Challenge: identifying variable name errors

1. Read the code below, and (without running it) try to identify what the errors are.
2. Run the cell, and read the error message. What type of `NameError` do you think this is? In other words, is it a string with no quotes, a misspelled variable, or a variable that should have been defined but was not?
3. Fix the error.
4. Repeat steps 2 and 3, until you have fixed all the errors.
</div>


<pre class="in"><code>for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (Number % 3) == 0:
        message = message + a
    else:
        message = message + &#34;b&#34;
print message</code></pre>

### Item errors


Next up are errors having to do with containers (like lists and dictionaries) and the items within them. If you try to access an item in a list or a dictionary that does not exist, then you will get an error! This makes sense. Think about a real life example: if you asked someone what day they would like to get coffee, and they answered "caturday", you might be a bit annoyed (though, perhaps after being amused that someone thought of the idea of caturday). Python gets similarly annoyed if you try to ask it for an item that doesn't exist:


<pre class="in"><code>letters = [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]
print &#34;Letter #1 is &#34; + letters[0]
print &#34;Letter #2 is &#34; + letters[1]
print &#34;Letter #3 is &#34; + letters[2]
print &#34;Letter #4 is &#34; + letters[3]</code></pre>

<div class="out"><pre class='out'><code>Letter #1 is a
Letter #2 is b
Letter #3 is c
</code></pre><pre class='err'><code>---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
&lt;ipython-input-11-d817f55b7d6c&gt; in &lt;module&gt;()
      3 print &#34;Letter #2 is &#34; + letters[1]
      4 print &#34;Letter #3 is &#34; + letters[2]
----&gt; 5 print &#34;Letter #4 is &#34; + letters[3]

IndexError: list index out of range</code></pre></div>


Here, Python is telling us that there is an `IndexError` in our code, meaning we tried to access a *list index* that did not exist.

We get a similar error in the case of dictionaries:


<pre class="in"><code>us_state_capitals = {
    &#39;california&#39;: &#39;sacramento&#39;,
    &#39;virginia&#39;: &#39;richmond&#39;,
    &#39;new york&#39;: &#39;albany&#39;,
    &#39;massachusetts&#39;: &#39;boston&#39;
}

print &#34;The capital of Oregon is: &#34; + us_state_capitals[&#39;oregon&#39;]</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
&lt;ipython-input-12-27fa113dd73c&gt; in &lt;module&gt;()
      6 }
      7 
----&gt; 8 print &#34;The capital of Oregon is: &#34; + us_state_capitals[&#39;oregon&#39;]

KeyError: &#39;oregon&#39;</code></pre></div>


In this case, we get a `KeyError`, which means that the key we requested (`'oregon'`, as the error message tells us) is not present in the dictionary. This might be because it genuinely does not exist in the dictionary, but it could *also* be due to a typo. This is similar to the case we discussed above, where you can sometimes receive a `NameError` due to a typo. For example:


<pre class="in"><code>us_state_capitals = {
    &#39;california&#39;: &#39;sacramento&#39;,
    &#39;virginia&#39;: &#39;richmond&#39;,
    &#39;new york&#39;: &#39;albany&#39;,
    &#39;massachusetts&#39;: &#39;boston&#39;
}

print &#34;The capital of Massachusetts is: &#34; + us_state_capitals[&#39;massachussetts&#39;]</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
&lt;ipython-input-13-ae1dac4c6a45&gt; in &lt;module&gt;()
      6 }
      7 
----&gt; 8 print &#34;The capital of Massachusetts is: &#34; + us_state_capitals[&#39;massachussetts&#39;]

KeyError: &#39;massachussetts&#39;</code></pre></div>


<div class="challenges" markdown="1">
#### Challenge: identifying item errors

1. Read the code below, and (without running it) try to identify what the errors are.
2. Run the cell, and read the error message. Is it an `IndexError` or a `KeyError`?
3. Fix the error.
4. Repeat steps 2 and 3, until you have fixed all the errors.
</div>


<pre class="in"><code>seasons = {
    &#39;spring&#39;: [&#39;march&#39;, &#39;april&#39;, &#39;may&#39;],
    &#39;summer&#39;: [&#39;june&#39;, &#39;july&#39;, &#39;august&#39;],
    &#39;fall&#39;: [&#39;september&#39;, &#39;october&#39;, &#39;november&#39;],
    &#39;winter&#39;: [&#39;december&#39;, &#39;january&#39;, &#39;february&#39;]
}

print &#34;The first month in spring is: &#34; + seasons[&#39;spring&#39;][0]
print &#34;The third month in summer is: &#34; + seasons[&#39;summer&#39;][3]
print &#34;The third month in fall is: &#34; + seasons[&#39;fal&#39;][3]
print &#34;The second month in winter is: &#34; + seasons[&#39;Winter&#39;][1]</code></pre>

### File errors


The last type of error we'll cover today are those associated with reading and writing files: `IOError`. The "IO" in `IOError` stands for "input/output", which is just a fancy way of saying "writing/reading".

If you try to read a file that does not exist, you will recieve an `IOError` telling you so. This is the most common reason why you would receive `IOError`, and if the error messages says "no such file or directory", then you know you have just tried to access a file that does not exist:


<pre class="in"><code>file_handle = open(&#39;myfile.txt&#39;, &#39;r&#39;)</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
IOError                                   Traceback (most recent call last)
&lt;ipython-input-14-f6e1ac4aee96&gt; in &lt;module&gt;()
----&gt; 1 file_handle = open(&#39;myfile.txt&#39;, &#39;r&#39;)

IOError: [Errno 2] No such file or directory: &#39;myfile.txt&#39;</code></pre></div>


One reason for receiving this error is that you specified an incorrect path to the file. For example, if I am currently in a folder called `myproject`, and I have a file in `myproject/writing/myfile.txt`, but I try to just open `myfile.txt`, this will fail. The correct path would be `writing/myfile.txt`. It is also possible (like with `NameError` and `KeyError`) that you just made a typo.


Another issue could be that you used the "read" flag instead of the "write" flag. Python will not give you an error if you try to open a file for writing when the file does not exist. However, if you meant to open a file for reading, but accidentally opened it for writing, and then try to read from it, you will get an error telling you that the file was not opened for reading:


<pre class="in"><code>file_handle = open(&#39;myfile.txt&#39;, &#39;w&#39;)
file_handle.read()</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
IOError                                   Traceback (most recent call last)
&lt;ipython-input-15-b846479bc61f&gt; in &lt;module&gt;()
      1 file_handle = open(&#39;myfile.txt&#39;, &#39;w&#39;)
----&gt; 2 file_handle.read()

IOError: File not open for reading</code></pre></div>


<div class="keypoints" markdown="1">
#### Key Points

*   Tracebacks can look intimidating, but they give us a lot of useful information about what went wrong in our program, including where the error occurred and what type of error it was.
*   An error having to do with the "grammar" or syntax of the program is called a `SyntaxError`. If the issue has to do with how the code is indented, then it will be called an `IndentationError`.
*   A `NameError` will occur if you use a variable that has not been defined (either because you meant to use quotes around a string, you forgot to define the variable, or you just made a typo).
*   Containers like lists and dictionaries will generate errors if you try to access items in them that do not exist. For lists, this type of error is called an `IndexError`; for dictionaries, it is called a `KeyError`.
*   Trying to read a file that does not exist will give you an `IOError`. Trying to read a file that is open for writing, or writing to a file that is open for reading, will also give you an `IOError`.
</div>
