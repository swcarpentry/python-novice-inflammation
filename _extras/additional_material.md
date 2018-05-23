---
layout: page
title: "Additional material"
permalink: /extra_material/
---
A collection of facts about Python that do not fit into the main lesson either due to the scope or time constraints of the main lesson.


## Jupyter Notebook/IPython: Who's Who in Memory

You can use the `%whos` command at any time to see what
variables you have created and what modules you have loaded into the computer's memory.
As this is an IPython command, it will only work if you are in an IPython terminal or the
Jupyter Notebook.

~~~
%whos
~~~
{: .language-python}

~~~
Variable    Type       Data/Info
--------------------------------
weight_kg   float      100.0
weight_lb   float      143.0
~~~
{: .output}


<br />
## Integer Division

We are using Python 3, where division always returns a floating point number:

~~~
5/9
~~~
{: .language-python}
~~~
0.5555555555555556
~~~
{: .output}

Unfortunately, this wasn't the case in Python 2:
~~~
5/9
~~~
{: .language-python}
~~~
0
~~~
{: .output}

If you are using Python 2 and want to keep the fractional part of division
you need to convert one or the other number to floating point:

~~~
float(5)/9
~~~
{: .language-python}

~~~
0.555555555556
~~~
{: .output}

~~~
5/float(9)
~~~
{: .language-python}

~~~
0.555555555556
~~~
{: .output}

~~~
5.0/9
~~~
{: .language-python}

~~~
0.555555555556
~~~
{: .output}
~~~
5/9.0
~~~
{: .language-python}

~~~
0.555555555556
~~~
{: .output}

And if you want an integer result from division in Python 3,
use a double-slash:

~~~
4//2
~~~
{: .language-python}

~~~
2
~~~
{: .output}

~~~
3//2
~~~
{: .language-python}

~~~
1
~~~
{: .output}

