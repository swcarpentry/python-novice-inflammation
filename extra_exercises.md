---
title: Additional Exercises
---

A collection of exercises that have been either removed from
or not (yet) added to the main lesson.

:::::::::::::::::::::::::::::::::::::::  challenge

## Swapping the contents of variables (5 min)

Explain what the overall effect of this code is:

```python
left = 'L'
right = 'R'

temp = left
left = right
right = temp
```

Compare it to:

```python
left, right = right, left
```

Do they always do the same thing?
Which do you find easier to read?

:::::::::::::::  solution

## Solution

Both examples exchange the values of `left` and `right`:

```python
print(left, right)
```

```output
R L
```

In the first case we used a temporary variable `temp` to keep the value of `left` before we
overwrite it with the value of `right`. In the second case, `right` and `left` are packed into a
[tuple](../learners/reference.md#tuple)
and then unpacked into `left` and `right`.



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Turn a String into a List

Use a for-loop to convert the string "hello" into a list of letters:

```python
["h", "e", "l", "l", "o"]
```

Hint: You can create an empty list like this:

```python
my_list = []
```

:::::::::::::::  solution

## Solution

```python
my_list = []
for char in "hello":
	my_list.append(char)
print(my_list)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Reverse a String

Knowing that two strings can be concatenated using the `+` operator,
write a loop that takes a string
and produces a new string with the characters in reverse order,
so `'Newton'` becomes `'notweN'`.

:::::::::::::::  solution

## Solution

```python
newstring = ''
oldstring = 'Newton'
for char in oldstring:
    newstring = char + newstring
print(newstring)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Fixing and Testing

From: "Defensive Programming"

Fix `range_overlap`. Re-run `test_range_overlap` after each change you make.

:::::::::::::::  solution

## Solution

```python
def range_overlap(ranges):
    '''Return common overlap among a set of [left, right] ranges.'''
    if not ranges:
        # ranges is None or an empty list
        return None
    max_left, min_right = ranges[0]
    for (left, right) in ranges[1:]:
        max_left = max(max_left, left)
        min_right = min(min_right, right)
    if max_left >= min_right:  # no overlap
        return None
    return (max_left, min_right)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::




