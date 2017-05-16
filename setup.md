---
layout: page
title: Setup
permalink: /setup/
---

You need to download some files to follow this lesson:

1. Make a new folder in your Desktop called `python-novice-inflammation`.
2. Download [python-novice-inflammation-data.zip][zipfile1] and move the file to this folder.
3. Also download [python-novice-inflammation-code.zip][zipfile2] and move it to the same folder.
4. If the files aren't unzipped yet, double-click to unzip them. You should end up with 
two new folders called `data` and `code`.
5. To get started, go into the `data` folder from the Unix shell with:

~~~
$ cd
$ cd Desktop/python-novice-inflammation/data
~~~
{: .source}

If you will be using the Jupyter (IPython) notebook for the lesson,
you should have already
[installed Anaconda](http://swcarpentry.github.io/workshop-template/#setup)
which includes the notebook.

To start the notebook, open a terminal or git bash and type the command:

~~~
$ jupyter notebook
~~~
{: .source}

To start the Python interpreter without the notebook, open a terminal or git bash and type the command:

~~~
$ python
~~~
{: .source}

[zipfile1]: {{ page.root }}/data/python-novice-inflammation-data.zip
[zipfile2]: {{ page.root }}/code/python-novice-inflammation-code.zip