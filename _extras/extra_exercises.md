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
