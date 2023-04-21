---
title: Additional material
---

A collection of facts about Python that do not fit into the main lesson
either due to the scope or time constraints of the main lesson.

## Jupyter Notebook/IPython: Who's Who in Memory

You can use the `%whos` command at any time to see what
variables you have created and what modules you have loaded into the computer's memory.
As this is an IPython command, it will only work if you are in an IPython terminal or the
Jupyter Notebook.

```python
%whos
```

```output
Variable    Type       Data/Info
--------------------------------
weight_kg   float      100.0
weight_lb   float      143.0
```

<br />
## Integer Division

We are using Python 3, where division always returns a floating point number:

```python
5/9
```

```output
0.5555555555555556
```

Unfortunately, this wasn't the case in Python 2:

```python
5/9
```

```output
0
```

If you are using Python 2 and want to keep the fractional part of division
you need to convert one or the other number to floating point:

```python
float(5)/9
```

```output
0.555555555556
```

```python
5/float(9)
```

```output
0.555555555556
```

```python
5.0/9
```

```output
0.555555555556
```

```python
5/9.0
```

```output
0.555555555556
```

And if you want an integer result from division in Python 3,
use a double-slash:

```python
4//2
```

```output
2
```

```python
3//2
```

```output
1
```


