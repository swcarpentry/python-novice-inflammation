---
layout: lesson
root: ../..
---

## Defensive Programming


Our previous lessons have introduced the basic tools of programming:
variables and lists,
file I/O,
loops,
conditionals,
and functions.
What they *haven't* done is show us how to tell
whether a program is getting the right answer,
and how to tell if it's *still* getting the right answer
as we make changes to it.

To achieve that,
we need to:

*   write programs that check their own operation,
*   write and run tests for widely-used functions, and
*   make sure we know what "correct" actually means.

The good news is,
doing these things will speed up our programming,
not slow it down.
As in real carpentry&mdash;the kind done with lumber&mdash;the time saved
by measuring carefully before cutting a piece of wood
is much greater than the time that measuring takes.


#### Objectives

*   Explain what an assertion is.
*   Add assertions to programs that correctly check the program's state.
*   Correctly add precondition and postcondition assertions to functions.
*   Explain what test-driven development is, and use it when creating new functions.
*   Explain why variables should be initialized using actual data values rather than arbitrary constants.
*   Debug code containing an error systematically.

### Assertions


The first step toward getting the right answers from our programs
is to assume that mistakes *will* happen
and to guard against them.
This is called [defensive programming](../../gloss.html#defensive-programming),
and the most common way to do it is to add [assertions](../../gloss.html#assertion) to our code
so that it checks itself as it runs.
An assertion is simply a statement that something must be true at a certain point in a program.
When Python sees one,
it checks that the assertion's condition.
If it's true,
Python does nothing,
but if it's false,
Python halts the program immediately
and prints the error message provided.
For example,
this piece of code halts as soon as the loop encounters a value that isn't positive:


<pre class="in"><code>numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for n in numbers:
    assert n &gt;= 0.0, &#39;Data should only contain positive values&#39;
    total += n
print &#39;total is:&#39;, total</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
&lt;ipython-input-19-33d87ea29ae4&gt; in &lt;module&gt;()
      2 total = 0.0
      3 for n in numbers:
----&gt; 4     assert n &gt;= 0.0, &#39;Data should only contain positive values&#39;
      5     total += n
      6 print &#39;total is:&#39;, total

AssertionError: Data should only contain positive values</code></pre></div>


Programs like the Firefox browser are full of assertions:
10-20% of the code they contain
are there to check that the other 80-90% are working correctly.
Broadly speaking,
assertions fall into three categories:

-   A [precondition](../../gloss.html#precondition) is something that must be true
 at the start of a function in order for it to work correctly.
-   A [postcondition](../../gloss.html#postcondition) is something that
 the function guarantees is true when it finishes.
-   An [invariant](../../gloss.html#invariant) is something that is always true
 at a particular point inside a piece of code.

For example,
suppose we are representing rectangles using a tuple of four coordinates `(x0, y0, x1, y1)`.
In order to do some calculations,
we need to normalize the rectangle so that it is at the origin
and 1.0 units long on its longest axis.
This function does that,
but checks that its input is correctly formatted and that its result makes sense:


<pre class="in"><code>def normalize_rectangle(rect):
    &#39;&#39;&#39;Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.&#39;&#39;&#39;
    assert len(rect) == 4, &#39;Rectangles must contain 4 coordinates&#39;
    x0, y0, x1, y1 = rect
    assert x0 &lt; x1, &#39;Invalid X coordinates&#39;
    assert y0 &lt; y1, &#39;Invalid Y coordinates&#39;
    
    dx = x1 - x0
    dy = y1 - y0
    if dx &gt; dy:
        scaled = float(dx) / dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 &lt; upper_x &lt;= 1.0, &#39;Calculated upper X coordinate invalid&#39;
    assert 0 &lt; upper_y &lt;= 1.0, &#39;Calculated upper Y coordinate invalid&#39;

    return (0, 0, upper_x, upper_y)</code></pre>


The preconditions on lines 2, 4, and 5 catch invalid inputs:


<pre class="in"><code>print normalize_rectangle( (0.0, 1.0, 2.0) ) # missing the fourth coordinate</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
&lt;ipython-input-21-3a97b1dcab70&gt; in &lt;module&gt;()
----&gt; 1 print normalize_rectangle( (0.0, 1.0, 2.0) ) # missing the fourth coordinate

&lt;ipython-input-20-408dc39f3915&gt; in normalize_rectangle(rect)
      1 def normalize_rectangle(rect):
      2     &#39;&#39;&#39;Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.&#39;&#39;&#39;
----&gt; 3     assert len(rect) == 4, &#39;Rectangles must contain 4 coordinates&#39;
      4     x0, y0, x1, y1 = rect
      5     assert x0 &lt; x1, &#39;Invalid X coordinates&#39;

AssertionError: Rectangles must contain 4 coordinates</code></pre></div>


<pre class="in"><code>print normalize_rectangle( (4.0, 2.0, 1.0, 5.0) ) # X axis inverted</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
&lt;ipython-input-22-f05ae7878a45&gt; in &lt;module&gt;()
----&gt; 1 print normalize_rectangle( (4.0, 2.0, 1.0, 5.0) ) # X axis inverted

&lt;ipython-input-20-408dc39f3915&gt; in normalize_rectangle(rect)
      3     assert len(rect) == 4, &#39;Rectangles must contain 4 coordinates&#39;
      4     x0, y0, x1, y1 = rect
----&gt; 5     assert x0 &lt; x1, &#39;Invalid X coordinates&#39;
      6     assert y0 &lt; y1, &#39;Invalid Y coordinates&#39;
      7 

AssertionError: Invalid X coordinates</code></pre></div>


The post-conditions help us catch bugs by telling us when our calculations cannot have been correct.
For example,
if we normalize a rectangle that is taller than it is wide everything seems OK:


<pre class="in"><code>print normalize_rectangle( (0.0, 0.0, 1.0, 5.0) )</code></pre>

<div class="out"><pre class='out'><code>(0, 0, 0.2, 1.0)
</code></pre></div>


but if we normalize one that's wider than it is tall,
the assertion is triggered:


<pre class="in"><code>print normalize_rectangle( (0.0, 0.0, 5.0, 1.0) )</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
&lt;ipython-input-24-5f0ef7954aeb&gt; in &lt;module&gt;()
----&gt; 1 print normalize_rectangle( (0.0, 0.0, 5.0, 1.0) )

&lt;ipython-input-20-408dc39f3915&gt; in normalize_rectangle(rect)
     16 
     17     assert 0 &lt; upper_x &lt;= 1.0, &#39;Calculated upper X coordinate invalid&#39;
---&gt; 18     assert 0 &lt; upper_y &lt;= 1.0, &#39;Calculated upper Y coordinate invalid&#39;
     19 
     20     return (0, 0, upper_x, upper_y)

AssertionError: Calculated upper Y coordinate invalid</code></pre></div>


Re-reading our function,
we realize that line 10 should divide `dy` by `dx` rather than `dx` by `dy`.
(You can display line numbers by typing Ctrl-M, then L.)
If we had left out the assertion at the end of the function,
we would have created and returned something that had the right shape as a valid answer,
but wasn't.
Detecting and debugging that would almost certainly have taken more time in the long run
than writing the assertion.

But assertions aren't just about catching errors:
they also help people understand programs.
Each assertion gives the person reading the program
a chance to check (consciously or otherwise)
that their understanding matches what the code is doing.

Most good programmers follow two rules when adding assertions to their code.
The first is, "[fail early, fail often](../../rules.html#fail-early-fail-often)".
The greater the distance between when and where an error occurs and when it's noticed,
the harder the error will be to debug,
so good code catches mistakes as early as possible.

The second rule is, "[turn bugs into assertions or tests](../../rules.html#turn-bugs-into-assertions-or-tests)".
If you made a mistake in a piece of code,
the odds are good that you have made other mistakes nearby,
or will make the same mistake (or a related one)
the next time you change it.
Writing assertions to check that you haven't [regressed](../../gloss.html#regression)
(i.e., haven't re-introduced an old problem)
can save a lot of time in the long run,
and helps to warn people who are reading the code
(including your future self)
that this bit is tricky.


#### Challenges

1. Suppose you are writing a function called `average` that calculates the average of the numbers in a list.
 What pre-conditions and post-conditions would you write for it?
 Compare your answer to your neighbor's:
 can you think of a function that will past your tests but not hers or vice versa?

2. Explain in words what the assertions in this code check,
 and for each one,
 give an example of input that will make that assertion fail.
 
  ~~~python
  def running(values):
      assert len(values) > 0
      result = [values[0]]
      for v in values[1:]:
          assert result[-1] >= 0
          result.append(result[-1] + v)
          assert result[-1] >= result[0]
      return result
  ~~~

### Test-Driven Development


An assertion checks that something is true at a particular point in the program.
The next step is to check the overall behavior of a piece of code,
i.e.,
to make sure that it produces the right output when it's given a particular input.
For example,
suppose we need to find where two or more time series overlap.
The range of each time series is represented as a pair of numbers,
which are the time the interval started and ended.
The output is the largest range that they all include:


<img src="img/python-overlapping-ranges.svg" alt="Overlapping Ranges" />


Most novice programmers would solve this problem like this:

1. Write a function `range_overlap`.
2. Call it interactively on two or three different inputs.
3. If it produces the wrong answer, fix the function and re-run that test.

This clearly works&mdash;after all, thousands of scientists are doing it right now&mdash;but
there's a better way:

1. Write a short function for each test.
2. Write a `range_overlap` function that should pass those tests.
3. If `range_overlap` produces any wrong answers, fix it and re-run the test functions.

Writing the tests *before* writing the function they exercise
is called [test-driven development](../../gloss.html#test-driven-development) (TDD).
Its advocates believe it produces better code faster because:

1. If people write tests after writing the thing to be tested,
 they are subject to confirmation bias,
 i.e.,
 they subconsciously write tests to show that their code is correct,
 rather than to find errors.
2. Writing tests helps programmers figure out what the function is actually supposed to do.

Here are three test functions for `range_overlap`:


<pre class="in"><code>assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
&lt;ipython-input-25-d8be150fbef6&gt; in &lt;module&gt;()
      1 assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
----&gt; 2 assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
      3 assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)

AssertionError: </code></pre></div>


The error is actually reassuring:
we haven't written `range_overlap` yet,
so if the tests passed,
it would be a sign that someone else had
and that we were accidentally using their function.

And as a bonus of writing these tests,
we've implicitly defined what our input and output look like:
we expect a list of pairs as input,
and produce a single pair as output.

Something important is missing, though.
We don't have any tests for the case where the ranges don't overlap at all:

~~~
assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == ???
~~~

What should `range_overlap` do in this case:
fail with an error message,
produce a special value like `(0.0, 0.0)` to signal that there's no overlap,
or something else?
Any actual implementation of the function will do one of these things;
writing the tests first helps us figure out which is best
*before* we're emotionally invested in whatever we happened to write
before we realized there was an issue.

And what about this case?

~~~
assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == ???
~~~

Do two segments that touch at their endpoints overlap or not?
Mathematicians usually say "yes",
but engineers usually say "no".
The best answer is "whatever is most useful in the rest of our program",
but again,
any actual implementation of `range_overlap` is going to do *something*,
and whatever it is ought to be consistent with what it does when there's no overlap at all.

Since we're planning to use the range this function returns
as the X axis in a time series chart,
we decide that:

1. every overlap has to have non-zero width, and
2. we will return the special value `None` when there's no overlap.

`None` is built into Python,
and means "nothing here".
(Other languages often call the equivalent value `null` or `nil`).
With that decision made,
we can finish writing our last two tests:


<pre class="in"><code>assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
&lt;ipython-input-26-d877ef460ba2&gt; in &lt;module&gt;()
----&gt; 1 assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
      2 assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None

AssertionError: </code></pre></div>


Again,
we get an error because we haven't written our function,
but we're now ready to do so:


<pre class="in"><code>def range_overlap(ranges):
    &#39;&#39;&#39;Return common overlap among a set of [low, high] ranges.&#39;&#39;&#39;
    lowest = 0.0
    highest = 1.0
    for (low, high) in ranges:
        lowest = max(lowest, low)
        highest = min(highest, high)
    return (lowest, highest)</code></pre>


(Take a moment to think about why we use `max` to raise `lowest`
and `min` to lower `highest`.)
We'd now like to re-run our tests,
but they're scattered across three different cells.
To make running them easier,
let's put them all in a function:


<pre class="in"><code>def test_range_overlap():
    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)</code></pre>


We can now test `range_overlap` with a single function call:


<pre class="in"><code>test_range_overlap()</code></pre>

<div class="out"><pre class='err'><code>---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
&lt;ipython-input-29-cf9215c96457&gt; in &lt;module&gt;()
----&gt; 1 test_range_overlap()

&lt;ipython-input-28-5d4cd6fd41d9&gt; in test_range_overlap()
      1 def test_range_overlap():
----&gt; 2     assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
      3     assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
      4     assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
      5     assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)

AssertionError: </code></pre></div>


The first of the tests that was supposed to produce `None` fails,
so we know there's something wrong with our function.
What we *don't* know,
though,
is whether the other four tests passed or failed,
because Python halted the program as soon as it spotted the first error.
Still,
some information is better than none,
and if we trace the behavior of the function with that input,
we realize that we're initializing `lowest` and `highest` to 0.0 and 1.0 respectively,
regardless of the input values.
This violates another important rule of programming:
"[always initialize from data](../../rules.html#always-initialize-from-data)".
We'll leave it as an exercise to fix `range_overlap`.


<div class="challenges" markdown="1">
#### Challenges

1. Fix `range_overlap`. Re-run `test_range_overlap` after each change you make.
</div>

### Debugging


Once testing has uncovered problems,
the next step is to fix them.
Many novices do this by making more-or-less random changes to their code
until it seems to produce the right answer,
but that's very inefficient
(and the result is usually only correct for the one case they're testing).
The more experienced a programmer is,
the more systematically they debug,
and most follow some variation on the rules explained below.

#### Know What It's Supposed to Do

The first step in debugging something is to
[know what it's supposed to do](../../rules.html#know-what-its-supposed-to-do).
"My program doesn't work" isn't good enough:
in order to diagnose and fix problems,
we need to be able to tell correct output from incorrect.
If we can write a test case for the failing case&mdash;i.e.,
if we can assert that with *these* inputs,
the function should produce *that* result&mdash;
then we're ready to start debugging.
If we can't,
then we need to figure out how we're going to know when we've fixed things.

But writing test cases for scientific software is frequently harder than
writing test cases for commercial applications,
because if we knew what the output of the scientific code was supposed to be,
we wouldn't be running the software:
we'd be writing up our results and moving on to the next program.
In practice,
scientists tend to do the following:

1. *Test with simplified data.*
 Before doing statistics on a real data set,
 we should try calculating statistics for a single record,
 for two identical records,
 for two records whose values are one step apart,
 or for some other case where we can calculate the right answer by hand.

2. *Test a simplified case.*
 If our program is supposed to simulate
 magnetic eddies in rapidly-rotating blobs of supercooled helium,
 our first test should be a blob of helium that isn't rotating,
 and isn't being subjected to any external electromagnetic fields.
 Similarly,
 if we're looking at the effects of climate change on speciation,
 our first test should hold temperature, precipitation, and other factors constant.

3. *Compare to an oracle.*
 A [test oracle](../../gloss.html#test-oracle) is something&mdash;experimental data,
 an older program whose results are trusted,
 or even a human expert&mdash;against which we can compare the results of our new program.
 If we have a test oracle,
 we should store its output for particular cases
 so that we can compare it with our new results as often as we like
 without re-running that program.

4. *Check conservation laws.*
 Mass, energy, and other quantitites are conserved in physical systems,
 so they should be in programs as well.
 Similarly,
 if we are analyzing patient data,
 the number of records should either stay the same or decrease
 as we move from one analysis to the next
 (since we might throw away outliers or records with missing values).
 If "new" patients start appearing out of nowhere as we move through our pipeline,
 it's probably a sign that something is wrong.

5. *Visualize.*
 Data analysts frequently use simple visualizations to check both
 the science they're doing
 and the correctness of their code
 (just as we did in the [opening lesson](01-numpy.html) of this tutorial).
 This should only be used for debugging as a last resort,
 though,
 since it's very hard to compare two visualizations automatically.

#### Make It Fail Every Time

We can only debug something when it fails,
so the second step is always to find a test case that
[makes it fail every time](../../rules.html#make-it-fail-every-time).
The "every time" part is important because
few things are more frustrating than debugging an intermittent problem:
if we have to call a function a dozen times to get a single failure,
the odds are good that we'll scroll past the failure when it actually occurs.

As part of this,
it's always important to check that our code is "plugged in",
i.e.,
that we're actually exercising the problem that we think we are.
Every programmer has spent hours chasing a bug,
only to realize that they were actually calling their code on the wrong data set
or with the wrong configuration parameters,
or are using the wrong version of the software entirely.
Mistakes like these are particularly likely to happen when we're tired,
frustrated,
and up against a deadline,
which is one of the reasons late-night (or overnight) coding sessions
are almost never worthwhile.

#### Make It Fail Fast

If it takes 20 minutes for the bug to surface,
we can only do three experiments an hour.
That doesn't must mean we'll get less data in more time:
we're also more likely to be distracted by other things as we wait for our program to fail,
which means the time we *are* spending on the problem is less focused.
It's therefore critical to [make it fail fast](../../rules.html#make-it-fail-fast).

As well as making the program fail fast in time,
we want to make it fail fast in space,
i.e.,
we want to localize the failure to the smallest possible region of code:

1. The smaller the gap between cause and effect,
 the easier the connection is to find.
 Many programmers therefore use a divide and conquer strategy to find bugs,
 i.e.,
 if the output of a function is wrong,
 they check whether things are OK in the middle,
 then concentrate on either the first or second half,
 and so on.

2. N things can interact in N<sup>2/2</sup> different ways,
 so every line of code that *isn't* run as part of a test
 means more than one thing we don't need to worry about.

#### Change One Thing at a Time, For a Reason

Replacing random chunks of code is unlikely to do much good.
(After all,
if you got it wrong the first time,
you'll probably get it wrong the second and third as well.)
Good programmers therefore
[change one thing at a time, for a reason](../../rules.html#change-one-thing-at-a-time)
They are either trying to gather more information
("is the bug still there if we change the order of the loops?")
or test a fix
("can we make the bug go away by sorting our data before processing it?").
 
Every time we make a change,
however small,
we should re-run our tests immediately,
because the more things we change at once,
the harder it is to know what's responsible for what
(those N<sup>2</sup> interactions again).
And we should re-run *all* of our tests:
more than half of fixes made to code introduce (or re-introduce) bugs,
so re-running all of our tests tells us whether we have [regressed](../../gloss.html#regression).

#### Keep Track of What You've Done

Good scientists keep track of what they've done
so that they can reproduce their work,
and so that they don't waste time repeating the same experiments
or running ones whose results won't be interesting.
Similarly,
debugging works best when we
[keep track of what we've done](../../rules.html#keep-track-of-what-youve-done)
and how well it worked.
If we find ourselves asking,
"Did left followed by right with an odd number of lines cause the crash?
Or was it right followed by left?
Or was I using an even number of lines?"
then it's time to step away from the computer,
take a deep breath,
and start working more systematically.
 
Records are particularly useful when the time comes to ask for help.
People are more likely to listen to us
when we can explain clearly what we did,
and we're better able to give them the information they need to be useful.

> #### Version Control Revisited
>
> Version control is often used to reset software to a known state during debugging,
> and to explore recent changes to code that might be responsible for bugs.
> In particular,
> most version control systems have a `blame` command
> that will show who last changed particular lines of code...

#### Be Humble

And speaking of help:
if we can't find a bug in 10 minutes,
we should [be humble](../../rules.html#be-humble) and ask for help.
Just explaining the problem aloud is often useful,
since hearing what we're thinking helps us spot inconsistencies and hidden assumptions.

Asking for help also helps alleviate confirmation bias.
If we have just spent an hour writing a complicated program,
we want it to work,
so we're likely to keep telling ourselves why it should,
rather than searching for the reason it doesn't.
People who aren't emotionally invested in the code can be more objective,
which is why they're often able to spot the simple mistakes we have overlooked.

Part of being humble is learning from our mistakes.
Programmers tend to get the same things wrong over and over:
either they don't understand the language and libraries they're working with,
or their model of how things work is wrong.
In either case,
taking note of why the error occurred
and checking for it next time
quickly turns into not making the mistake at all.

And that is what makes us most productive in the long run.
As the saying goes,
"[A week of hard work can sometimes save you an hour of thought](../../rules.html#week-hard-work-hour-thought)."
If we train ourselves to avoid making some kinds of mistakes,
to break our code into modular, testable chunks,
and to turn every assumption (or mistake) into an assertion,
it will actually take us *less* time to produce working programs,
not more.


<div class="keypoints" markdown="1">
#### Key Points

*   Program defensively, i.e., assume that errors are going to arise, and write code to detect them when they do.
*   Put assertions in programs to check their state as they run, and to help readers understand how those programs are supposed to work.
*   Use preconditions to check that the inputs to a function are safe to use.
*   Use postconditions to check that the output from a function is safe to use.
*   Write tests before writing code in order to help determine exactly what that code is supposed to do.
*   Know what code is supposed to do *before* trying to debug it.
*   Make it fail every time.
*   Make it fail fast.
*   Change one thing at a time, and for a reason.
*   Keep track of what you've done.
*   Be humble.
</div>


#### Next Steps

We have now seen the basics of building and testing Python code in the IPython Notebook.
The last thing we need to learn is how to build command-line programs
that we can use in pipelines and shell scripts,
so that we can integrate our tools with other people's work.
This will be the subject of our next and final lesson.
