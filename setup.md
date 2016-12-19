---
layout: page
title: Setup
permalink: /setup/
---

You need to download some files to follow this lesson:

1. Make a new folder on your Desktop called `python-novice-inflammation`.
2. Download [python-novice-inflammation-data.zip][zipfile] and move the file to this folder.
3. If it's not unzipped yet, double-click on it to unzip it. You should end up with a new folder called `data`.
4. You can confirm that everything is in the right place by listing the content of the data folder from the terminal or git bash with:

~~~
$ cd ~/Desktop/python-novice-inflammation
$ ls data
~~~
{: .source}

If you will be using the Jupyter (IPython) notebook for the lesson,
you should have already
[installed Anaconda](http://swcarpentry.github.io/workshop-template/#setup)
which includes the notebook.

To start the notebook, type this command in your terminal or git bash next:

~~~
$ jupyter notebook
~~~
{: .source}

To start the Python interpreter without the notebook, type this command in your terminal or git bash next:

~~~
$ python
~~~
{: .source}

[zipfile]: {{ page.root }}/data/python-novice-inflammation-data.zip
