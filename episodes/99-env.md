---
title: Managing your Project Environment
---

:::::::::::::::::::::::::::::: questions

FIXME

::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::: objectives

* Identify some advantages of creating an environment for their scripts to run in.
* Create a new environment.
* Install Python libraries into an environment.
* Activate and deactivate an environment.

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: challenge

### Benefits of an Isolated Environment
Consider the following scenarios.
In which circumstances would it be appropriate to create a new environment to work in?
In which would it be better to continue working in the existing environment?

1. You have completed an analysis of the current inflammation data and receive a new dataset that you want to process and analyse in the same way.
1. You want to expand your analysis to compare these two datasets in a different way that requires a new library to be installed.
1. You need to begin a new project, which you expect to use the same libraries you already have installed in your first project environment.
1. You need to begin a new project, which will use a completely different set of libraries to those you are currently working with.

::::::::::::::::::::: solution

#### Solution

1. Use the same environment. This is exactly the kind of reproducible analysis that an encapsulated environment is perfect for.
1. As this new analysis is an extension of the same project, you should use the same environment and install the new dependency there.
1. Even though you expect to use the same libraries as you currently have installed in the existing environment, it is good practice to create a new environment anyway.
   As a project develops we often find that we need to install a new dependency and when this happens, the environment you need for the new project will diverge from what is needed in the previous one.
1. Create a new environment and install the dependencies there.

::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::::::::::::::::::::::: keypoints

FIXME

::::::::::::::::::::::::::::::::::::::::