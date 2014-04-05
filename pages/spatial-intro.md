---
layout: lesson
root: ../..
---

## A note to students and instructors

This lesson requires the [Basemap](http://matplotlib.org/basemap) toolkit for
Matplotlib. This library is not distributed with Matplotlib directly. If you are
using Continuum's Anaconda distribution, you can obtain the library using:

    conda install basemap

If you are using Enthought Canopy and have the full version or an academic
license, Basemap should already be installed on your system. Otherwise, you will
need to follow the [installation
instructions](http://matplotlib.org/basemap/users/installing.html) on the
Basemap documentation. Using one of the two scientific distributions is
preferred in most instances.

## Visualizing spatial data

Original materials by <a href="https://github.com/synapticarbors">Joshua
Adelman</a>; modified by <a href="http://www.randalolson.com/">Randy Olson</a>

We are examining some simple spatial coordinate data, specifically the location
of all of the previous Software Carpentry bootcamps. The data set is stored in
[comma-separated values](../../gloss.html#csv) (CSV) format. After the header
line (marked with a `#`), each row contains the latitude and longitude for each
bootcamp, separated by a comma.

    # Latitude, Longitude
    43.661476,-79.395189
    39.332604,-76.623190
    45.703255, 13.718013
    43.661476,-79.395189
    39.166381,-86.526621
    ...

We want to:

* Load the data into our analysis environment
* Inspect the data
* Visualize it in a meaningful context

To do this, we'll begin to delve into working with Python and do a bit of
programming.

## Objectives

*   Explain what a library is, and what libraries are used for.
*   Load a Python library and use the things it contains.
*   Read tabular data from a file into a program.
*   Display simple visualizations of the data

### Loading the data

In order to work with the coordinates stored in the file, we need to
[import](../../gloss.html#import) a library called NumPy that is designed to
easily handle arrays of data.


    import numpy as np

It's very common to create an [alias](../../gloss.html#alias-library) for a
library when importing it
in order to reduce the amount of typing we have to do. We can now refer to this
library in the code as `np` instead of typing out `numpy` each time we want to
use it.

We can now ask numpy to read our data file:


    lat, lon = np.loadtxt('swc_bc_coords.csv', delimiter=',', unpack=True)

The expression `np.loadtxt(...)` means,
"Run the function `loadtxt` that belongs to the `numpy` library."
This [dotted notation](../../gloss.html#dotted-notation) is used everywhere in
Python
to refer to the parts of larger things.

`np.loadtxt` has three [parameters](../../gloss.html#parameter):
the name of the file we want to read,
and the [delimiter](../../gloss.html#delimiter) that separates values on a line.
These both need to be character strings (or [strings](../../gloss.html#string)
for short),
so we put them in quotes.
Finally, passing the `unpack` paramter the boolean value, `True` tells
`np.loadtxt` to take the first and second column of data and
[assign](../../gloss.html#assignment) them to the
[variables](../../gloss.html#variable)  `lat` and `lon`, respectively.
A variable is just a name for some data.
Also note that `np.loadtxt` automatically skipped the line with the header
information, since it recognizes that
this line is a [comment](../../gloss.html#comment) and does not contain
numerical data.

When we are finished typing and press Shift+Enter,
the notebook runs our command.

`lat` and `lon` now contain our data, which we can inspect by just executing a
cell with the name of a variable:


    lat




    array([ 43.661476,  39.332604,  45.703255,  43.661476,  39.166381,
            36.802151,  37.808381,  41.790113,  41.744949,  51.559882,
            42.727288,  54.980095,  53.523454,  49.261715,  39.32758 ,
            48.831673,  42.359133,  43.47013 ,  44.632261,  43.783551,
            53.948193,  59.939959,  40.808078,  40.428267,  37.875928,
            49.261715,  37.8695  ,  54.980095,  34.141411,  38.831513,
            51.757137,  43.261328,  38.648056,  32.89533 ,  34.227425,
            21.300662,  55.945328,  30.283599,  49.261715,  41.790113,
            45.417417,  43.469128,  49.261715,  48.264934,  43.647118,
            48.53698 ,  40.808078,  37.228384,  49.261715, -33.773636,
           -37.825328,  47.655965,  37.875928,  38.031441,  33.900058,
            41.744949,  22.3101  ,  32.236358,  51.524789, -33.929492,
            53.467102,  37.8695  ,  53.478349,  48.82629 ,  39.291389,
            43.07718 ,  52.33399 ,  54.32707 ,  39.07141 ,  37.42949 ,
            37.875928,  43.64712 ,  51.759865,  38.54926 ,  36.00803 ,
            50.060833,  36.00283 ,  40.03131 ,  42.388889,  53.52345 ,
            50.937716,  42.35076 ,  41.789722,  49.276765,  32.887151,
            41.790113,  42.3625  ,  30.283599, -43.523333,  35.20859 ,
            59.939959,  30.538978,  39.166381,  51.377743,  37.228384,
            41.7408  ,  41.70522 ,  47.655   ,  40.443322,  44.968657,
            38.958455,  32.30192 ,  43.07718 ,  41.66293 ,  51.457971,
            43.468889,  42.724085, -34.919159,  49.261111, -37.9083  ,
            34.052778,  41.526667])



## Visualizing the data

The array is a type of container defined by numpy to hold values. We will
discuss how to manipulate arrays in more detail in another lesson.
For now let's just make a simple plot of the data. For this, we will use another
library called `matplotlib`. First, let's tell the IPython Notebook that we want
our plots displayed inline, rather than in a separate viewing window:


    %matplotlib inline

The `%` at the start of the line signals that this is a command for the
notebook,
rather than a statement in Python.
Next,
we will import the `pyplot` module from `matplotlib` and use one of the commands
it defines to make plot a point for each latitude, longitude pair of data.


    from matplotlib import pyplot
    pyplot.plot(lon, lat, 'o')




    [<matplotlib.lines.Line2D at 0x10690d490>]




![png](spatial-intro_files/spatial-intro_17_1.png)


### Exercise 1

Plot the dots with a different color according to the continent they would be
on.


    

While matplotlib provides a simple facility for visualizing numerical data in a
variety of ways, we will use a supplementary toolkit called *Basemap* that
enhances matplotlib to specifically deal with spatial data. We need to import
this library and can do so using:


    from mpl_toolkits.basemap import Basemap

Now let's create a Basemap object that will allow us to project the coordinates
onto map. For this example we are going to use a [Robinson
Projection](http://en.wikipedia.org/wiki/Robinson_projection).


    basemap_graph = Basemap(projection='robin', lat_0=0.0, lon_0=0.0)

The parameters `lat_0` and `lon_0` define the center of the map. Now let's add
some features to our map using methods defined by the `bm` object. We will also
use the object itself to get the coordinates of the bootcamps in the projection
given our original longitudes and latitudes. We will also tell pyplot to make
the figure 12 inches by 12 inches to make it more legible.


    pyplot.figure(figsize=(12,12))
    basemap_graph.drawcoastlines()
    basemap_graph.drawcountries()
    basemap_graph.fillcontinents()
    basemap_graph.drawmeridians(np.arange(-180,180,20))
    basemap_graph.drawparallels(np.arange(-90,90,20))
    
    x, y = basemap_graph(lon, lat)
    basemap_graph.plot(x, y, 'o', markersize=4, color='red')




    [<matplotlib.lines.Line2D at 0x107f94d90>]




![png](spatial-intro_files/spatial-intro_26_1.png)


The final line of the above code cell mimics matplotlib's built-in `plot` method
to plot our projected coordinates onto the map.

With just a handful of lines of code, you see that we can create a rich
visualization of our data.

### Exercise 2

1. Integrate the coloring scheme from Exercise 1 into the Basemap projection.
2. Try out a different projection that better shows the boot camp locations in
North America. Here is the list of projections in Basemap:
http://matplotlib.org/basemap/users/mapsetup.html


    
