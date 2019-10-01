---
layout: page
title: Setup
permalink: /setup/index.html
root: ..
---

### Install Python

In this lesson we will be using Python 3 with some of its scientific libraries.
Although one can install a "plain vanilla" Python 3 and all required libraries "by hand",
we recommend installing [Anaconda][workshop-template-python-instructions], a Python distribution
that comes with everything we need for the lesson.

&nbsp; <!-- vertical spacer -->

### Obtain lesson materials

1. Download [python-novice-inflammation-data.zip][zipfile1]
        and [python-novice-inflammation-code.zip][zipfile2].
2. Create a folder called `swc-python` on your Desktop.
3. Move downloaded files into this newly created folder.
4. Unzip the files.

You should now see two new folders called `data` and `code` in your `swc-python` directory on your
Desktop.

&nbsp; <!-- vertical spacer -->

### Navigate to the `data` folder

If you're using a Unix shell application, such as Terminal app in macOS, Console or Terminal in
Linux, or [Git Bash](https://gitforwindows.org/) on Windows, execute the following command:

~~~
$ cd ~/Desktop/swc-python/data
~~~
{: .source}

On Windows, you can use its native Command Prompt program.  The easiest way to start it up is by
pressing <kbd>Windows Logo Key</kbd>+<kbd>R</kbd>, entering `cmd`, and hitting <kbd>Return</kbd>. In
the Command Prompt, use the following command to navigate to the `data` folder:
~~~
$ cd /D %userprofile%\Desktop\swc-python\data
~~~
{: .source}

&nbsp; <!-- vertical spacer -->

### Option 1: Launch "plain vanilla" Python interpreter

To start working with Python, we need to launch a program that will interpret and execute our Python
commands. To launch a "plain vanilla" Python interpreter, execute:
~~~
$ python
~~~
{: .source}

If you are using Git Bash on Windows, you have to call Python _via_ `winpty`:
~~~
$ winpty python
~~~
{: .source}

&nbsp; <!-- vertical spacer -->

### Option 2: Start Jupyter Notebook

Jupyter Notebook provides a browser-based interface for working with Python. If you would like to
use a notebook during the lesson, make sure to install [Anaconda](http://carpentries.github.io/workshop-template/#python)
distribution.

To start a Jupyter server, execute:
~~~
$ jupyter notebook
~~~
{: .source}

Then create a new notebook by clicking "New" button on the right and selecting "Python 3" from the
drop-down menu:

![](../fig/new-notebook.png)

&nbsp; <!-- vertical spacer -->

### Option 3: Start IPython interpreter

IPython is an alternative solution situated somewhere in between the plain vanilla Python
interpreter and Jupyter Notebook. It provides an interactive command-line based interpreter with
various convenience features and commands.  You should have IPython on your system if you installed
[Anaconda](http://carpentries.github.io/workshop-template/#python) distribution.

To start using IPython, execute:
~~~
$ ipython
~~~
{: .source}

[zipfile1]: {{ page.root }}/data/python-novice-inflammation-data.zip
[zipfile2]: {{ page.root }}/code/python-novice-inflammation-code.zip
[workshop-template-python-instructions]: https://carpentries.github.io/workshop-template/#python
