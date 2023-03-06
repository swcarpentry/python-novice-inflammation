---
title: Setup
---

## Overview

This lesson is designed to be run on a personal computer.
All of the software and data used in this lesson are freely available online,
and instructions on how to obtain them are provided below.

## Install Python

In this lesson, we will be using Python 3 with some of its most popular scientific libraries.
Although one can install a plain-vanilla Python and all required libraries by hand,
we recommend installing [Anaconda][anaconda-website],
a Python distribution that comes with everything we need for the lesson.
Detailed installation instructions for various operating systems can be found
on The Carpentries [template website for workshops][anaconda-instructions]
and in [Anaconda documentation][anaconda-install].

## Obtain lesson materials

1. Download [python-novice-inflammation-data.zip][zipfile1]
        and [python-novice-inflammation-code.zip][zipfile2].
2. Create a folder called `swc-python` on your Desktop.
3. Move downloaded files to `swc-python`.
4. Unzip the files.

You should see two folders called `data` and `code` in the `swc-python` directory on your
Desktop.

## Launch Python interface

To start working with Python, we need to launch a program that will interpret and execute our
Python commands. Below we list several options. If you don't have a preference, proceed with the
top option in the list that is available on your machine. Otherwise, you may use any interface
you like.

## Option A: Jupyter Notebook

A Jupyter Notebook provides a browser-based interface for working with Python.
If you installed Anaconda, you can launch a notebook in two ways:

> ## Anaconda Navigator
>
> 1. Launch Anaconda Navigator.
> It might ask you if you'd like to send anonymized usage information to Anaconda developers:
> ![Anaconda Navigator first launch](
{{ page.root }}{% link fig/anaconda-navigator-first-launch.png %})
> Make your choice and click "Ok, and don't show again" button.
> 2. Find the "Notebook" tab and click on the "Launch" button:
> ![Anaconda Navigator Notebook launch](
{{ page.root }}{% link fig/anaconda-navigator-notebook-launch.png %})
> Anaconda will open a new browser window or tab with a Notebook Dashboard showing you the
> contents of your Home (or User) folder.
> 3. Navigate to the `data` directory by clicking on the directory names leading to it:
> `Desktop`, `swc-python`, then `data`:
> ![Anaconda Navigator Notebook directory](
{{ page.root }}{% link fig/jupyter-notebook-data-directory.png %})
> 4. Launch the notebook by clicking on the "New" button and then selecting "Python 3":
> ![Anaconda Navigator Notebook directory](
{{ page.root }}{% link fig/jupyter-notebook-launch-notebook.png %})
{: .solution}

> ## Command line (Terminal)
>
> 1\. Navigate to the `data` directory:
>
> > ## Unix shell
> > If you're using a Unix shell application, such as Terminal app in macOS, Console or Terminal
> > in Linux, or [Git Bash][gitbash] on Windows, execute the following command:
> > ~~~
> > cd ~/Desktop/swc-python/data
> > ~~~
> > {: .language-bash}
> {: .solution}
>
> > ## Command Prompt (Windows)
> > On Windows, you can use its native Command Prompt program.  The easiest way to start it up is
> > pressing <kbd>Windows Logo Key</kbd>+<kbd>R</kbd>, entering `cmd`, and hitting
> > <kbd>Return</kbd>. In the Command Prompt, use the following command to navigate to
> > the `data` folder:
> > ~~~
> > cd /D %userprofile%\Desktop\swc-python\data
> > ~~~
> > {: .source}
> {: .solution}
>
> 2\. Start Jupyter server
>
> > ## Unix shell
> > ~~~
> > jupyter notebook
> > ~~~
> > {: .language-bash}
> {: .solution}
>
> > ## Command Prompt (Windows)
> > ~~~
> > python -m notebook
> > ~~~
> > {: .source}
> {: .solution}
>
> 3\. Launch the notebook by clicking on the "New" button on the right and selecting "Python 3"
> from the drop-down menu:
> ![Anaconda Navigator Notebook directory](
{{ page.root }}{% link fig/jupyter-notebook-launch-notebook2.png %})
{: .solution}

&nbsp; <!-- vertical spacer -->

## Option B: IPython interpreter

IPython is an alternative solution situated somewhere in between the plain-vanilla Python
interpreter and Jupyter Notebook. It provides an interactive command-line based interpreter with
various convenience features and commands.  You should have IPython on your system if you installed
[Anaconda][anaconda-instructions].

To start using IPython, execute:
~~~
ipython
~~~
{: .source}

&nbsp; <!-- vertical spacer -->

## Option C: plain-vanilla Python interpreter

To launch a plain-vanilla Python interpreter, execute:
~~~
python
~~~
{: .source}

If you are using [Git Bash on Windows][gitbash], you have to call Python _via_ `winpty`:
~~~
winpty python
~~~
{: .source}

[anaconda-install]: https://docs.anaconda.com/anaconda/install
[anaconda-instructions]: https://carpentries.github.io/workshop-template/#python
[anaconda-website]: https://www.anaconda.com/
[gitbash]: https://gitforwindows.org
[zipfile1]: {{ page.root }}/data/python-novice-inflammation-data.zip
[zipfile2]: {{ page.root }}/code/python-novice-inflammation-code.zip
