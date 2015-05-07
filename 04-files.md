---
layout: page
title: Programming with Python
subtitle: Analyzing Data from Multiple Files
minutes: 20
---
> ## Learning Objectives {.objectives}
>
> *   Use a library function to get a list of filenames that match a simple wildcard pattern.
> *   Use a for loop to process multiple files.

We now have almost everything we need to process all our data files.
The only thing that's missing is a library with a rather unpleasant name:

~~~ {.python}
import glob
~~~

The `glob` library contains a single function, also called `glob`,
that finds files whose names match a pattern.
We provide those patterns as strings:
the character `*` matches zero or more characters,
while `?` matches any one character.
We can use this to get the names of all the IPython Notebooks we have created so far:

~~~ {.python}
print glob.glob('*.ipynb')
~~~

~~~ {.output}
['01-numpy.ipynb', '02-func.ipynb', '03-loop.ipynb', '04-cond.ipynb', '05-defensive.ipynb', '06-cmdline.ipynb', 'spatial-intro.ipynb']
~~~

or to get the names of all our CSV data files:

~~~ {.python}
print glob.glob('*.csv')
~~~

~~~ {.output}
['inflammation-01.csv', 'inflammation-02.csv', 'inflammation-03.csv', 'inflammation-04.csv', 'inflammation-05.csv', 'inflammation-06.csv', 'inflammation-07.csv', 'inflammation-08.csv', 'inflammation-09.csv', 'inflammation-10.csv', 'inflammation-11.csv', 'inflammation-12.csv', 'small-01.csv', 'small-02.csv', 'small-03.csv']
~~~

As these examples show,
`glob.glob`'s result is a list of strings,
which means we can loop over it
to do something with each filename in turn.
In our case,
the "something" we want is the code that generates those plots of our inflammation data.
Let's test it by analyzing the first three files in the list:

~~~ {.python}
filenames = glob.glob('*.csv')
filenames = filenames[0:3]
for f in filenames:
    print f
    data = np.loadtxt(fname=f, delimiter=',')
    # create a figure with three subplots
    fig = plt.figure(figsize=(10.0, 3.0))
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)
    # add a plot of the mean
    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))
    # add a plot of the maximum values        
    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))
    # add a plot of the minimum values
    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))
    # show the figure
    fig.tight_layout()
    plt.show(fig)
~~~

~~~ {.output}
inflammation-01.csv
~~~

![Analysis of inflammation-01.csv](fig/03-loop_49_1.png)\


~~~ {.output}
inflammation-02.csv
~~~

![Analysis of inflammation-02.csv](fig/03-loop_49_3.png)\


~~~ {.output}
inflammation-03.csv
~~~

![Analysis of inflammation-03.csv](fig/03-loop_49_5.png)\

Sure enough,
the maxima of the first two data sets show exactly the same ramp as the first,
and their minima show the same staircase structure;
a different situation has been revealed in the third dataset,
where the maxima are a bit less regular, but the minima are consistently zero.
