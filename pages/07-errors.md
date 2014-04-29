---
layout: lesson
root: ../..
---

## Python errors and exceptions


<div>
<p>Every programmer encounters errors, both those who are just beginning, and those who have been programming for years. Encountering errors and exceptions can be very frustrating at times, and can make coding feel like a hopeless endeavour. However, understanding what the <strong>different types of errors</strong> are and when you are likely to encounter them can help a lot! Once you know <em>why</em> you get certain types of errors, they become much easier to fix.</p>
</div>


<div class="objectives">
<h4 id="objectives">Objectives</h4>
<ul>
<li>To be able to read a traceback, and determine the following relevant pieces of information:<ul>
<li>The file, function, and line number on which the error occurred</li>
<li>The type of the error</li>
<li>The error message</li>
</ul>
</li>
<li>To be able to describe the types of situations in which the following errors occur:<ul>
<li><code>SyntaxError</code> and <code>IndentationError</code></li>
<li><code>NameError</code></li>
<li><code>KeyError</code> and <code>IndexError</code></li>
</ul>
</li>
</ul>
</div>

### The anatomy of an error


<div>
<p>Errors in Python have a very specific form, called a <a href="../../gloss.html#traceback">traceback</a>. Let&#39;s examine one:</p>
</div>


<div class="in">
<pre>from errors_01 import favorite_ice_cream
favorite_ice_cream()</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
&lt;ipython-input-1-9d0462a5b07c&gt; in &lt;module&gt;()
      1 from errors_01 import favorite_ice_cream
----&gt; 2 favorite_ice_cream()

/Users/jhamrick/project/swc/novice/python/errors_01.pyc in favorite_ice_cream()
      5         &#34;strawberry&#34;
      6     ]
----&gt; 7     print ice_creams[3]

IndexError: list index out of range</pre>
</div>


<div>
<p>This particular traceback has two levels. You can determine the number of levels by looking for the number of arrows on the left hand side. In this case:</p>
<ol>
<li>The first shows code from the cell above, with an arrow pointing to Line 2 (which is <code>favorite_ice_cream()</code>).</li>
<li>The second shows some code in another function (<code>favorite_ice_cream</code>, located in the file <code>errors_01.py</code>), with an arrow pointing to Line 7 (which is <code>print ice_creams[3]</code>).</li>
</ol>
<p>The last level is the actual place where the error occurred. The other level(s) show what function the program executed to get to the next level down. So, in this case, the program first performed a <a href="../../gloss.html#function-call">function call</a> to the function <code>favorite_ice_cream</code>. Inside this function, the program encountered an error on Line 7, when it tried to run the code <code>print ice_creams[3]</code>.</p>
<blockquote>
<h4 id="long-tracebacks">Long tracebacks</h4>
<p>Sometimes, you might see a traceback that is very long -- sometimes they might even be 20 levels deep! This can make it seem like something horrible happened, but really it just means that your program called many functions before it ran into the error. Most of the time, you can just pay attention to the bottom-most level, which is the actual place where the error occurred.</p>
</blockquote>
<p>So what error did the program actually encounter? In the last line of the traceback, Python helpfully tells us the category or <strong>type of error</strong> (in this case, it is an <code>IndexError</code>) and a more detailed <strong>error message</strong> (in this case, it says &quot;list index out of range&quot;). </p>
<p>If you encounter an error and don&#39;t know what it means, it is still important to read the traceback closely. That way, if you fix the error, but encounter a new one, you can tell that the error changed! Additionally, sometimes just knowing <em>where</em> the error occurred is enough to fix it, even if you don&#39;t entirely understand the message.</p>
<p>If you do encounter an error you don&#39;t recognize, try looking at the <a href="http://docs.python.org/2/library/exceptions.html">official documentation on errors</a>. However, note that you may not always be able to find the error there, as it is possible to create custom errors. In that case, hopefully the custom error message is informative enough to help you figure out what went wrong!</p>
</div>


<div class="challenges">
<h4 id="challenge-reading-error-messages">Challenge: reading error messages</h4>
<p>Read the traceback below, and identify the following pieces of information about it:</p>
<ol>
<li>How many <strong>levels</strong> does the traceback have?</li>
<li>What is the <strong>file name</strong> where the error occurred?</li>
<li>What is the <strong>function name</strong> where the error occurred?</li>
<li>On which <strong>line number</strong> in this function did the error occurr?</li>
<li>What is the <strong>type of error</strong>?</li>
<li>What is the <strong>error message</strong>?</li>
</ol>
</div>


<div class="in">
<pre>from errors_02 import print_friday_message
print_friday_message()</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
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

KeyError: &#39;Friday&#39;</pre>
</div>

### Syntax errors


<div>
<p>When you forget a colon at the end of a line, accidentally add one space too many when indenting under an <code>if</code> statement, or forget a parentheses, you will encounter a <strong>syntax error</strong>. This means that Python couldn&#39;t figure out how to read your program. This is similar to forgetting punctuation in English:</p>
<blockquote>
<p>this text is difficult to read there is no punctuation there is also no capitalization why is this hard because you have to figure out where each sentence ends you also have to figure out where each sentence begins to some extent it might be ambiguous if there should be a sentence break or not</p>
</blockquote>
<p>People can typically figure out what is meant by text with no punctuation, but people are much smarter than computers! If Python doesn&#39;t know how to read the program, it will just give up, and inform you with an error. For example:</p>
</div>


<div class="in">
<pre>def some_function()
    msg = &#34;hello, world!&#34;
    print msg
     return msg</pre>
</div>

<div class="out">
<pre>  File &#34;&lt;ipython-input-3-6bb841ea1423&gt;&#34;, line 1
    def some_function()
                       ^
SyntaxError: invalid syntax
</pre>
</div>


<div>
<p>Here, Python tells us that there is a <code>SyntaxError</code> on line 1, and even puts a little arrow in the place where there is an issue. In this case, the problem is that the function definition is missing a colon at the end.</p>
<p>Actually, the function above has <em>two</em> issues with syntax. If we fix the problem with the colon, we see that there is <em>also</em> an <code>IndentationError</code>, which means that the lines in the function definition do not all have the same indentation:</p>
</div>


<div class="in">
<pre>def some_function():
    msg = &#34;hello, world!&#34;
    print msg
     return msg</pre>
</div>

<div class="out">
<pre>  File &#34;&lt;ipython-input-4-ae290e7659cb&gt;&#34;, line 4
    return msg
    ^
IndentationError: unexpected indent
</pre>
</div>


<div>
<p>Both <code>SyntaxError</code> and <code>IndentationError</code> indicate a problem with the syntax of your program, but an <code>IndentationError</code> is more specific: it <em>always</em> means that there is a problem with how your code is indented.</p>
</div>


<div>
<h4 id="whitespace-tabs-and-spaces">Whitespace: tabs and spaces</h4>
<p>A quick note on indentation errors: they can sometimes be insidious, especially if you are mixing spaces and tabs. Because they are both &quot;whitespace&quot;, it is difficult to visually tell the difference! The IPython notebook actually gives us a bit of a hint, but not all Python editors will do that. In the following example, the first two lines are using a tab for indentation, while the third line uses four spaces.</p>
</div>


<div class="in">
<pre>def some_function():
	msg = &#34;hello, world!&#34;
	print msg
    return msg</pre>
</div>

<div class="out">
<pre>  File &#34;&lt;ipython-input-5-653b36fbcd41&gt;&#34;, line 4
    return msg
              ^
IndentationError: unindent does not match any outer indentation level
</pre>
</div>


<div>
<p>By default, one tab is equivalent to eight spaces, so the only way to mix tabs and spaces is to make it look like this! In general, is is better to just <strong>never use tabs</strong> and <strong>always use spaces</strong>, because it can make things very confusing.</p>
</div>


<div class="in">
<pre>def some_function():
	msg = &#34;hello, world!&#34;
	print msg
        return msg</pre>
</div>


<div class="challenges">
<h4 id="challenge-identifying-syntax-errors">Challenge: identifying syntax errors</h4>
<ol>
<li>Read the code below, and (without running it) try to identify what the errors are.</li>
<li>Run the cell, and read the error message. Is it a <code>SyntaxError</code> or an <code>IndentationError</code>?</li>
<li>Fix the error.</li>
<li>Repeat steps 2 and 3, until you have fixed all the errors.</li>
</ol>
</div>


<div class="in">
<pre>def another_function
  print &#34;Syntax errors are annoying.&#34;
   print &#34;But at least python tells us about them!&#34;
  print &#34;So they are usually not too hard to fix.&#34;</pre>
</div>

### Variable name errors


<div>
<p>Another very common type of error is called a <code>NameError</code>, and occurs when you try to use a variable that does not exist. For example:</p>
</div>


<div class="in">
<pre>print a</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-7-9d7b17ad5387&gt; in &lt;module&gt;()
----&gt; 1 print a

NameError: name &#39;a&#39; is not defined</pre>
</div>


<div>
<p>Variable name errors come with some of the most informative error messages, which are usually of the form &quot;name &#39;the_variable_name&#39; is not defined&quot;.</p>
<p><em>Why</em> does this error message occur? That&#39;s harder question to answer, because it depends on what your code is supposed to do. However, there are a few very common reasons why you might have an undefined variable. The first is that you meant to use a <a href="../../gloss.html#string">string</a>, but forgot to put quotes around it:</p>
</div>


<div class="in">
<pre>print hello</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-8-9553ee03b645&gt; in &lt;module&gt;()
----&gt; 1 print hello

NameError: name &#39;hello&#39; is not defined</pre>
</div>


<div>
<p>The second is that you just forgot to create the variable before using it. In the following example, <code>count</code> should have been defined (e.g., with <code>count = 0</code>) before the for loop:</p>
</div>


<div class="in">
<pre>for number in range(10):
    count = count + number
print &#34;The count is: &#34; + str(count)</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-9-dd6a12d7ca5c&gt; in &lt;module&gt;()
      1 for number in range(10):
----&gt; 2     count = count + number
      3 print &#34;The count is: &#34; + str(count)

NameError: name &#39;count&#39; is not defined</pre>
</div>


<div>
<p>Finally, the third possibility is that you made a typo when you were writing your code. Let&#39;s say we fixed the error above by adding the line <code>Count = 0</code> before the for loop. Frustratingly, this actually does not fix the error! Remember that variables are <a href="../../gloss.html#case-sensitive">case-sensitive</a>, so the variable <code>count</code> is different from <code>Count</code>. We still get the same error, because we still have not defined <code>count</code>:</p>
</div>


<div class="in">
<pre>Count = 0
for number in range(10):
    count = count + number
print &#34;The count is: &#34; + str(count)</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-10-d77d40059aea&gt; in &lt;module&gt;()
      1 Count = 0
      2 for number in range(10):
----&gt; 3     count = count + number
      4 print &#34;The count is: &#34; + str(count)

NameError: name &#39;count&#39; is not defined</pre>
</div>


<div class="challenges">
<h4 id="challenge-identifying-variable-name-errors">Challenge: identifying variable name errors</h4>
<ol>
<li>Read the code below, and (without running it) try to identify what the errors are.</li>
<li>Run the cell, and read the error message. What type of <code>NameError</code> do you think this is? In other words, is it a string with no quotes, a misspelled variable, or a variable that should have been defined but was not?</li>
<li>Fix the error.</li>
<li>Repeat steps 2 and 3, until you have fixed all the errors.</li>
</ol>
</div>


<div class="in">
<pre>for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (Number % 3) == 0:
        message = message + a
    else:
        message = message + &#34;b&#34;
print message</pre>
</div>

### Item errors


<div>
<p>The last types of errors that we&#39;ll be covering in this lesson are errors having to do with containers (like lists and dictionaries) and the items within them. If you try to access an item in a list or a dictionary that does not exist, then you will get an error! This makes sense. Think about a real life example: if you asked someone for a number between 1 and 10, and they gave you the number 15, you would probably be annoyed that they did not follow your instructions! Python gets similarly annoyed:</p>
</div>


<div class="in">
<pre>letters = [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]
print &#34;Letter #1 is &#34; + letters[0]
print &#34;Letter #2 is &#34; + letters[1]
print &#34;Letter #3 is &#34; + letters[2]
print &#34;Letter #4 is &#34; + letters[3]</pre>
</div>

<div class="out">
<pre>Letter #1 is a
Letter #2 is b
Letter #3 is c
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
&lt;ipython-input-11-d817f55b7d6c&gt; in &lt;module&gt;()
      3 print &#34;Letter #2 is &#34; + letters[1]
      4 print &#34;Letter #3 is &#34; + letters[2]
----&gt; 5 print &#34;Letter #4 is &#34; + letters[3]

IndexError: list index out of range</pre>
</div>


<div>
<p>Here, Python is telling us that there is an <code>IndexError</code> in our code, meaning we tried to access a <em>list index</em> that did not exist.</p>
<p>We get a similar error in the case of dictionaries:</p>
</div>


<div class="in">
<pre>us_state_capitals = {
    &#39;california&#39;: &#39;sacramento&#39;,
    &#39;virginia&#39;: &#39;richmond&#39;,
    &#39;new york&#39;: &#39;albany&#39;,
    &#39;massachusetts&#39;: &#39;boston&#39;
}

print &#34;The capital of Oregon is: &#34; + us_state_capitals[&#39;oregon&#39;]</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
&lt;ipython-input-12-27fa113dd73c&gt; in &lt;module&gt;()
      6 }
      7 
----&gt; 8 print &#34;The capital of Oregon is: &#34; + us_state_capitals[&#39;oregon&#39;]

KeyError: &#39;oregon&#39;</pre>
</div>


<div>
<p>In this case, we get a <code>KeyError</code>, which means that the key we requested (<code>&#39;oregon&#39;</code>, as the error message tells us) is not present in the dictionary. This might be because it genuinely does not exist in the dictionary, but it could <em>also</em> be due to a typo. This is similar to the case we discussed above, where you can sometimes receive a <code>NameError</code> due to a typo. For example:</p>
</div>


<div class="in">
<pre>us_state_capitals = {
    &#39;california&#39;: &#39;sacramento&#39;,
    &#39;virginia&#39;: &#39;richmond&#39;,
    &#39;new york&#39;: &#39;albany&#39;,
    &#39;massachusetts&#39;: &#39;boston&#39;
}

print &#34;The capital of Massachusetts is: &#34; + us_state_capitals[&#39;massachussetts&#39;]</pre>
</div>

<div class="out">
<pre>---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
&lt;ipython-input-13-ae1dac4c6a45&gt; in &lt;module&gt;()
      6 }
      7 
----&gt; 8 print &#34;The capital of Massachusetts is: &#34; + us_state_capitals[&#39;massachussetts&#39;]

KeyError: &#39;massachussetts&#39;</pre>
</div>


<div class="challenges">
<h4 id="challenge-identifying-item-errors">Challenge: identifying item errors</h4>
<ol>
<li>Read the code below, and (without running it) try to identify what the errors are.</li>
<li>Run the cell, and read the error message. Is it an <code>IndexError</code> or a <code>KeyError</code>?</li>
<li>Fix the error.</li>
<li>Repeat steps 2 and 3, until you have fixed all the errors.</li>
</ol>
</div>


<div class="in">
<pre>seasons = {
    &#39;spring&#39;: [&#39;march&#39;, &#39;april&#39;, &#39;may&#39;],
    &#39;summer&#39;: [&#39;june&#39;, &#39;july&#39;, &#39;august&#39;],
    &#39;fall&#39;: [&#39;september&#39;, &#39;october&#39;, &#39;november&#39;],
    &#39;winter&#39;: [&#39;december&#39;, &#39;january&#39;, &#39;february&#39;]
}

print &#34;The first month in spring is: &#34; + seasons[&#39;spring&#39;][0]
print &#34;The third month in summer is: &#34; + seasons[&#39;summer&#39;][3]
print &#34;The third month in fall is: &#34; + seasons[&#39;fal&#39;][3]
print &#34;The second month in winter is: &#34; + seasons[&#39;Winter&#39;][1]</pre>
</div>


<div class="keypoints">
<h4 id="key-points">Key Points</h4>
<ul>
<li>Tracebacks can look intimidating, but they give us a lot of useful information about what went wrong in our program, including where the error occurred and what type of error it was.</li>
<li>An error having to do with the &quot;grammar&quot; or syntax of the program is called a <code>SyntaxError</code>. If the issue has to do with how the code is indented, then it will be called an <code>IndentationError</code>.</li>
<li>A <code>NameError</code> will occur if you use a variable that has not been defined (either because you meant to use quotes around a string, you forgot to define the variable, or you just made a typo).</li>
<li>Containers like lists and dictionaries will generate errors if you try to access items in them that do not exist. For lists, this type of error is called an <code>IndexError</code>; for dictionaries, it is called a <code>KeyError</code>.</li>
</ul>
</div>
