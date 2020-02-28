---
title: Python Fundamentals
teaching: 20
exercises: 10
questions:
- "What basic data types can I work with in Python?"
- "How can I create a new variable in Python?"
- "Can I change the value associated with a variable after I create it?"
objectives:
- "Assign values to variables."
keypoints:
- "Basic data types in Python include integers, strings, and floating-point numbers."
- "Use `variable = value` to assign a value to a variable in order to record it in memory."
- "Variables are created on demand whenever a value is assigned to them."
- "Use `print(something)` to display the value of `something`."
---

## Variables

Any Python interpreter can be used as a calculator:
~~~
3 + 5 * 4
~~~
{: .language-python}
~~~
23
~~~
{: .output}

This is great but not very interesting.
To do anything useful with data, we need to assign its value to a _variable_.
In Python, we can [assign]({{ page.root }}/reference/#assign) a value to a
[variable]({{ page.root }}/reference/#variable), using the equals sign `=`.
For example, to assign value `60` to a variable `weight_kg`, we would execute:

~~~
weight_kg = 60
~~~
{: .language-python}

From now on, whenever we use `weight_kg`, Python will substitute the value we assigned to
it. In layman's terms, **a variable is a name for a value**.

In Python, variable names:

 - can include letters, digits, and underscores
 - cannot start with a digit
 - are [case sensitive]({{ page.root }}/reference/#case-sensitive).

This means that, for example:
 - `weight0` is a valid variable name, whereas `0weight` is not
 - `weight` and `Weight` are different variables

## Types of data
Python knows various types of data. Three common ones are:

* integer numbers
* floating point numbers, and
* strings.

In the example above, variable `weight_kg` has an integer value of `60`.
To create a variable with a floating point value, we can execute:

~~~
weight_kg = 60.0
~~~
{: .language-python}

And to create a string, we add single or double quotes around some text, for example:

~~~
weight_kg_text = 'weight in kilograms:'
~~~
{: .language-python}

## Using Variables in Python
To display the value of a variable to the screen in Python, we can use the `print` function:

~~~
print(weight_kg)
~~~
{: .language-python}

~~~
60.0
~~~
{: .output}

We can display multiple things at once using only one `print` command:

~~~
print(weight_kg_text, weight_kg)
~~~
{: .language-python}
~~~
weight in kilograms: 60.0
~~~
{: .output}

Moreover, we can do arithmetic with variables right inside the `print` function:

~~~
print('weight in pounds:', 2.2 * weight_kg)
~~~
{: .language-python}

~~~
weight in pounds: 132.0
~~~
{: .output}

The above command, however, did not change the value of `weight_kg`:
~~~
print(weight_kg)
~~~
{: .language-python}

~~~
60.0
~~~
{: .output}

To change the value of the `weight_kg` variable, we have to
**assign** `weight_kg` a new value using the equals `=` sign:

~~~
weight_kg = 65.0
print('weight in kilograms is now:', weight_kg)
~~~
{: .language-python}

~~~
weight in kilograms is now: 65.0
~~~
{: .output}

> ## Variables as Sticky Notes
>
> A variable is analogous to a sticky note with a name written on it:
> assigning a value to a variable is like putting that sticky note on a particular value.
>
> ![Value of 65.0 with weight_kg name stuck on it](../fig/python-sticky-note-variables-01.svg)
>
> This means that assigning a value to one variable does **not** change
> values of other variables.
> For example, let's store the subject's weight in pounds in its own variable:
>
> ~~~
> # There are 2.2 pounds per kilogram
> weight_lb = 2.2 * weight_kg
> print(weight_kg_text, weight_kg, 'and in pounds:', weight_lb)
> ~~~
> {: .language-python}
>
> ~~~
> weight in kilograms: 65.0 and in pounds: 143.0
> ~~~
> {: .output}
>
> ![Creating Another Variable](../fig/python-sticky-note-variables-02.svg)
>
> Let's now change `weight_kg`:
>
> ~~~
> weight_kg = 100.0
> print('weight in kilograms is now:', weight_kg, 'and weight in pounds is still:', weight_lb)
> ~~~
> {: .language-python}
>
> ~~~
> weight in kilograms is now: 100.0 and weight in pounds is still: 143.0
> ~~~
> {: .output}
>
> ![Value of 100.0 with label weight_kg stuck on it, and value of 143.0 with label weight_lb stuck on it](../fig/python-sticky-note-variables-03.svg)
>
> Since `weight_lb` doesn't "remember" where its value comes from,
> it is not updated when we change `weight_kg`.
{: .callout}


> ## Check Your Understanding
>
> What values do the variables `mass` and `age` have after each statement in the following program?
> Test your answers by executing the commands.
>
> ~~~
> mass = 47.5
> age = 122
> mass = mass * 2.0
> age = age - 20
> print(mass, age)
> ~~~
> {: .language-python}
>
> > ## Solution
> > ~~~
> > 95.0 102
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## Sorting Out References
>
> What does the following program print out?
>
> ~~~
> first, second = 'Grace', 'Hopper'
> third, fourth = second, first
> print(third, fourth)
> ~~~
> {: .language-python}
>
> > ## Solution
> > ~~~
> > Hopper Grace
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

{% include links.md %}
