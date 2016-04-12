---
layout: page
title: Programming with Python
subtitle: Storing Multiple Values in Lists
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Explain what a list is.
> *   Create and index lists of simple values.

Just as a `for` loop is a way to do operations many times,
a list is a way to store many values.
Unlike NumPy arrays,
lists are built into the language (so we don't have to load a library
to use them).
We create a list by putting values inside square brackets:

~~~ {.python}
odds = [1, 3, 5, 7]
print('odds are:', odds)
~~~

~~~ {.output}
odds are: [1, 3, 5, 7]
~~~

We select individual elements from lists by indexing them:

~~~ {.python}
print('first and last:', odds[0], odds[-1])
~~~

~~~ {.output}
first and last: 1 7
~~~

and if we loop over a list,
the loop variable is assigned elements one at a time:

~~~ {.python}
for number in odds:
    print(number)
~~~

~~~ {.output}
1
3
5
7
~~~

There is one important difference between lists and strings:
we can change the values in a list,
but we cannot change the characters in a string.
For example:

~~~ {.python}
names = ['Newton', 'Darwing', 'Turing'] # typo in Darwin's name
print('names is originally:', names)
names[1] = 'Darwin' # correct the name
print('final value of names:', names)
~~~

~~~ {.output}
names is originally: ['Newton', 'Darwing', 'Turing']
final value of names: ['Newton', 'Darwin', 'Turing']
~~~

works, but:

~~~ {.python}
name = 'Bell'
name[0] = 'b'
~~~

~~~ {.error}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-220df48aeb2e> in <module>()
      1 name = 'Bell'
----> 2 name[0] = 'b'

TypeError: 'str' object does not support item assignment
~~~

does not.

> ## Ch-Ch-Ch-Changes {.callout}
>
> Data which can be modified in place is called [mutable](reference.html#mutable),
> while data which cannot be modified is called [immutable](reference.html#immutable).
> Strings and numbers are immutable. This does not mean that variables with string or number values are constants,
> but when we want to change the value of a string or number variable, we can only replace the old value
> with a completely new value.
>
> Lists and arrays, on the other hand, are mutable: we can modify them after they have been created. We can
> change individual elements, append new elements, or reorder the whole list.  For some operations, like
> sorting, we can choose whether to use a function that modifies the data in place or a function that returns a
> modified copy and leaves the original unchanged.
>
> Be careful when modifying data in place.  If two variables refer to the same list, and you modify the list
> value, it will change for both variables! If you want variables with mutable values to be independent, you
> must make a copy of the value when you assign it.
>
> Because of pitfalls like this, code which modifies data in place can be more difficult to understand. However,
> it is often far more efficient to modify a large data structure in place than to create a modified copy for
> every small change. You should consider both of these aspects when writing your code.


> ## Nested Lists {.callout}
> Since lists can contain any Python variable, it can even contain other lists.
>
> For example, we could represent the products in the shelves of a small grocery shop:
>
> ~~~ {.python}
> x = [['pepper', 'zucchini', 'onion'],
>      ['cabbage', 'lettuce', 'garlic'],
>      ['apple', 'pear', 'banana']]
> ~~~
>
>
> Here is a visual example of how indexing a list of lists `x` works:
>
> <a href='https://twitter.com/hadleywickham/status/643381054758363136'>
> ![The first element of a list. Adapted from @hadleywickham's tweet about R > lists.](img/indexing_lists_python.png)</a>
>
> Using the previously declared list `x`, these would be the results of the
> index operations shown in the image:
>
> ~~~ {.python}
> print([x[0]])
> ~~~
>
> ~~~ {.output}
> [['pepper', 'zucchini', 'onion']]
> ~~~
>
> ~~~ {.python}
> print(x[0])
> ~~~
>
> ~~~ {.output}
> ['pepper', 'zucchini', 'onion']
> ~~~
>
> ~~~ {.python}
> print(x[0][0])
> ~~~
>
> ~~~ {.output}
> 'pepper'
> ~~~
>
> Thanks to [Hadley Wickham](https://twitter.com/hadleywickham/status/643381054758363136)
> for the image above.

There are many ways to change the contents of lists besides assigning new values to
individual elements:

~~~ {.python}
odds.append(11)
print('odds after adding a value:', odds)
~~~
~~~ {.output}
odds after adding a value: [1, 3, 5, 7, 11]
~~~

~~~ {.python}
del odds[0]
print('odds after removing the first element:', odds)
~~~
~~~ {.output}
odds after removing the first element: [3, 5, 7, 11]
~~~

~~~ {.python}
odds.reverse()
print('odds after reversing:', odds)
~~~
~~~ {.output}
odds after reversing: [11, 7, 5, 3]
~~~

While modifying in place, it is useful to remember that Python treats lists in a slightly counterintuitive way.

If we make a list and (attempt to) copy it then modify in place, we can cause all sorts of trouble:

~~~ {.python}
odds = [1, 3, 5, 7]
primes = odds
primes += [2]
print('primes:', primes)
print('odds:', odds)
~~~
~~~ {.output}
primes: [1, 3, 5, 7, 2]
odds: [1, 3, 5, 7, 2]
~~~

This is because Python stores a list in memory, and then can use multiple names to refer to the same list.
If all we want to do is copy a (simple) list, we can use the `list` function, so we do not modify a list we did not mean to:

~~~ {.python}
odds = [1, 3, 5, 7]
primes = list(odds)
primes += [2]
print('primes:', primes)
print('odds:', odds)
~~~
~~~ {.output}
primes: [1, 3, 5, 7, 2]
odds: [1, 3, 5, 7]
~~~

This is different from how variables worked in lesson 1, and more similar to how a spreadsheet works.

> ## Turn a string into a list {.challenge}
>
> Use a for-loop to convert the string "hello" into a list of letters:
>
> ~~~ {.python}
> ["h", "e", "l", "l", "o"]
> ~~~
> Hint: You can create an empty list like this:
>
> ~~~ {.python}
> my_list = []
> ~~~

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
>
> Compare it to:
>
> ~~~ {.python}
> left, right = right, left
> ~~~
>
> Do they always do the same thing?
> Which do you find easier to read?
> ## Nested loops in list comprehension {.callout}
>
> Use a loop inside a list to perform basic and complex list manipulations in a straight forward way. 
> 
>
> Let’s say we create two lists of integers, 
> list1 contains also numbers but will be treated as strings because each number is quoted ‘’.
> list2 contains numbers which will be treated as integers
> 
> ~~~ {.python}
> list1=['1','2','3','4','5','6','7','8']
> list2=[8,7,6,5,4,3,2,1]
> ~~~
> 
> Now we would like to convert the list1 to a list of integers i.e. removing the quotes in order to match list2 values type. 
> In order to do that we will use the basic python function called int() which will remove the quotes around the numbers in list1
> We will also use a for loop that we already saw in the previous lesson (02-loop)
> 
> ~~~ {.python}
> list1_int=[]
> for x in list1:
> 	list1_int.append(int(x))
>
> print list1
> print list1_int
> ~~~
>
>
> ~~~ {.output}
> [‘1’, '2', '3', '4', '5', '6', '7', '8']
> [1, 2, 3, 4, 5, 6, 7, 8]~~~
> ~~~
> 
> Now let’s do the same thing with a single line code. In order to do so, we need to use the nested loop within list1_int.
> This concept is called list comprehensions which allows us to perform an operation on all list values (list1) and returns a new list in our case it is list1_int.
>
> ~~~ {.python}
> list1_int = [int(x) for x in list1]
> print list1_int
> ~~~
>
> ~~~ {.output}
> [1, 2, 3, 4, 5, 6, 7, 8]
> ~~~
>
> In the upper code we applied the function int() of the variable x that will go through list1 items and will append the values to list1_int
> in one step
>
>
> ## Arithmetics over multiple list indexes {.challenge}
>
>  Here it gets a little more complicated, we would like to sum up the items in list1_int and list2 with respect to their positions using list comprehension. 
> In other words, print out a result list that is the sum of list1_int and list2, with respect to items indexes (summing up the first item of list1_int to the first item list2 than the second until the last item). 
> HINTS: Use the function zip() which aggregates items with respect to their position in two lists.
>
>
> ~~~ {.python}
> summed_lists= [ k+j for k,j in zip(list1_int, list2)] 
> ~~~
>
> ~~~ {.output}
> [9, 9, 9, 9, 9, 9, 9, 9]
> ~~~
>
>
> In the upper code we assigned two variables to iterate over two lists i.e. k will iterate over list1_int and j will iterate over list2 at the same time. 
> k+j will perform the operation of summing at each simultaneous iteration of k and j. the zip() will make sure the item indexes are respected.
