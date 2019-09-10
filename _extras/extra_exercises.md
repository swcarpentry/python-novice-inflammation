---
layout: page
title: "Additional Exercises"
permalink: /extra_exercises/
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
> left, right = [right, left]
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
> > list and then unpacked into `left` and `right`.
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
