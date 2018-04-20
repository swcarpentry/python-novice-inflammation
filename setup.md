---
layout: page
title: Setup
permalink: /setup/
root: ..
---

## Get the data

To download materials used in this lesson, please follow these 4 steps:

1. Download [python-novice-inflammation-data.zip][zipfile1] and [python-novice-inflammation-code.zip][zipfile2].
2. Create a folder called `python-novice-inflammation` on your Desktop and move downloaded files into it.
3. Unzip the files. You should end up with two new folders called `data` and `code`.
4. Navigate to the `data` folder. The way you can do this is different on different platforms. 

In a Unix shell (Terminal app in macOS, Console or Terminal in Linux) or [Git Bash](https://gitforwindows.org/) (Windows):

~~~
$ cd ~/Desktop/python-novice-inflammation/data
~~~
{: .source}

If you are using Windows, you can also use its Command Prompt program.
The easiest way to start using it is by pressing <kbd>Windows Logo Key</kbd>+<kbd>R</kbd> (run dialog), 
entering `cmd`, and hitting <kbd>Enter</kbd>. In the Command Prompt, use the following command
to navigate to the `data` folder:

~~~
$ cd /D %userprofile%\Desktop\python-novice-inflammation\data
~~~
{: .source}

## Launch Python interpreter

To start working with Python, we need to launch a program that will interpret and execute
our Python code. To do that, simply execute the following command:

~~~
$ python
~~~
{: .source}

If using Git Bash, you have to call Python _via_ `winpty`:

~~~
$ winpty python
~~~
{: .source}

## Jupyter Notebook

Jupyter Notebooks provide a browser-based interface for working with Python.
If you would like to use them during the lesson, make sure to install
[Anaconda Distribution](http://swcarpentry.github.io/workshop-template/#python).

To start the notebook, execute the following command:

~~~
$ jupyter notebook
~~~
{: .source}

Then create a new notebook using the drop-down menu on the right to select 'Python 3 notebook':

![](../fig/new-notebook.png)

[zipfile1]: {{ page.root }}/data/python-novice-inflammation-data.zip
[zipfile2]: {{ page.root }}/code/python-novice-inflammation-code.zip
