---
title: "Additional Exercises"
---
A collection of exercises that have been either removed from
or not (yet) added to the main lesson.


> ## Swapping the contents of variables (5 min)
>
> Explain what the overall effect of this code is:
>
> ~~~
> left = 'L'
> right = 'R'
>
> temp = left
> left = right
> right = temp
> ~~~
> {: .language-python}
>
> Compare it to:
>
> ~~~
> left, right = right, left
> ~~~
> {: .language-python}
>
> Do they always do the same thing?
> Which do you find easier to read?
>
> > ## Solution
> > Both examples exchange the values of `left` and `right`:
> >
> > ~~~
> > print(left, right)
> > ~~~
> > {: .language-python}
> >
> > ~~~
> > R L
> > ~~~
> > {: .output}
> >
> > In the first case we used a temporary variable `temp` to keep the value of `left` before we
> > overwrite it with the value of `right`. In the second case, `right` and `left` are packed into a
> > [tuple]({{ page.root }}/reference.html#tuple)
> > and then unpacked into `left` and `right`.
> {: .solution}
{: .challenge}

> ## Turn a String into a List
>
> Use a for-loop to convert the string "hello" into a list of letters:
>
> ~~~
> ["h", "e", "l", "l", "o"]
> ~~~
> {: .language-python}
>
> Hint: You can create an empty list like this:
>
> ~~~
> my_list = []
> ~~~
> {: .language-python}
>
> > ## Solution
> > ~~~
> > my_list = []
> > for char in "hello":
> > 	my_list.append(char)
> > print(my_list)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Reverse a String
>
> Knowing that two strings can be concatenated using the `+` operator,
> write a loop that takes a string
> and produces a new string with the characters in reverse order,
> so `'Newton'` becomes `'notweN'`.
>
> > ## Solution
> > ~~~
> > newstring = ''
> > oldstring = 'Newton'
> > for char in oldstring:
> >     newstring = char + newstring
> > print(newstring)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Fixing and Testing
> From: "Defensive Programming"
>
> Fix `range_overlap`. Re-run `test_range_overlap` after each change you make.
>
> > ## Solution
> > ~~~
> > def range_overlap(ranges):
> >     '''Return common overlap among a set of [left, right] ranges.'''
> >     if not ranges:
> >         # ranges is None or an empty list
> >         return None
> >     max_left, min_right = ranges[0]
> >     for (left, right) in ranges[1:]:
> >         max_left = max(max_left, left)
> >         min_right = min(min_right, right)
> >     if max_left >= min_right:  # no overlap
> >         return None
> >     return (max_left, min_right)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

{% include links.md %}
