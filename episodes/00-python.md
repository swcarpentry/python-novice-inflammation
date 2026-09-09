---
title: Running Python
teaching: 10
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

- Understand what Python is
- Understand basic ways to run python

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What is a programming language?
- How can you run a python program?

::::::::::::::::::::::::::::::::::::::::::::::::::

## What is a programming language?

Simply: A programming language is a way for humans to tell a computer what to do.

Usually it is a set of instructions a human gives a computer to carry out.

- A program is just text that computers can understand
- The order of instructions is important

An analogy would be a recipe:

```
Program: Bake a cake

Take:
- 1 cup flour
- 1 cup sugar
- 2 eggs
- 1/2 cup milk

Steps:
1. Combine flour and sugar
2. Mix with eggs and milk until smooth
3. Pour into cake pan
4. Bake for 30 minutes at 180 degrees.
```

## Python

- Interpreted language
- Dynamically typed

Other programming languages you may have heard of:
- [Java](https://en.wikipedia.org/wiki/Java_(programming_language))
- [C](https://en.wikipedia.org/wiki/C_(programming_language)) or [C++](https://en.wikipedia.org/wiki/C++)
- [Rust](https://en.wikipedia.org/wiki/Rust_(programming_language))
- [R](https://en.wikipedia.org/wiki/R_(programming_language))
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

## Running Python in the CLI

### Interactively

You can run python in what is called Read–Eval–Print Loop (REPL).
It allows you to run Python code line by line and receive instant feedback.

```bash
python
```

```output
Python 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 17.0.0 (clang-1700.0.13.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 5
>>> y = 12
>>> x * y
60
```

Type `exit()` to exit the REPL and return to your regular shell.

### With a command

```bash
python -c "print('hello there')"
```

```output
hello there
```

The `-c` option tells python to look at the following text and treat it as a program.
In this case the program to run is: `print('hello there')`.

### From a script

We can also create file to store our program.
This is called a script, and allows us to write many

For example a file name `my-script.py` containing the text:
```python
# my-script.py
print('hello from my-script.py')
```

Can be run with the following command:
```bash
python my-script.py
```

```output
hello from my-script.py
```

## Running Python from notebooks

Notebooks are a way run python code in an interactive and graphical way.
They let your code to be separated into sections called "cells" that can be executed independent of one another.

You can mix code and text with different cell types: code and markdown.

Examples of notebooks are:
- [Jupyter](https://jupyter.org/)
- [Google Colab](https://colab.research.google.com/)
