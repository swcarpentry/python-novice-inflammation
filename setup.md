---
layout: page
title: Setup
permalink: /setup/
root: ..
---

In preparation for this lesson, you will need to download two zipped files and place them in the specified folder:

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

If you are using Windows, you can use the `cmd` (Command Prompt) program instead of the Unix shell.
The easiest way to start it is by pressing `Windows Logo Key` + `R` (run dialog) and entering `cmd`.In Windows, the commands above to access the folder in your Desktop become:

~~~
$ cd /D %userprofile%\Desktop\python-novice-inflammation\data
~~~
{: .source}


If you will be using the Jupyter (IPython) notebook for the lesson,
you should have already
[installed Anaconda](http://swcarpentry.github.io/workshop-template/#python)
which includes the notebook.

To start the notebook server, open a terminal or git bash and execute the command:

~~~
$ jupyter notebook
~~~
{: .source}

Then create a new notebook using the drop-down menu on the right to select 'Python 3 notebook':

![](../fig/new-notebook.png)

To start the Python interpreter without the notebook, open a terminal
or command prompt and execute the command:

~~~
$ python
~~~
{: .source}

Note: If using Git Bash on Windows, you have to call Python via `winpty`:

~~~
$ winpty python
~~~
{: .source}

[zipfile1]: {{ page.root }}/data/python-novice-inflammation-data.zip
[zipfile2]: {{ page.root }}/code/python-novice-inflammation-code.zip
