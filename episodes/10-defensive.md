---
title: Defensive Programming
teaching: 30
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Understand the importance of input validation.
- Learn how to use exceptions and raise errors in Python.
- Practice writing defensive code to validate inputs.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I make my programs more reliable?

::::::::::::::::::::::::::::::::::::::::::::::::::

Our previous lessons have introduced the basic tools of programming:
- Variables and lists,
- File I/O,
- Loops,
- Conditionals,
- Functions.

Now it's time to learn how to ensure that our programs always work as intended. Defensive programming is a practice used in software development to ensure a program functions correctly even under unexpected conditions. A key aspect of defensive programming is input validation, which involves checking input data to prevent errors and ensure the program behaves as expected.

## Why is Input Validation Important?

- **Reliability**: Ensures that the program receives the correct type and range of input data.
- **Security**: Prevents malicious input from causing harm.
- **Data Integrity**: Maintains the consistency and accuracy of the data.

In general, input validation makes our lives easier by preventing the program from running with invalid input and delivering invalid results.

The general pattern of input validation usually follows these steps:

```python
def some_func(x):
    if x does not meet the condition:
        Stop the program and print an error message
    do something with x
```
As you can see above, input validation is one of the first, if not the first, things a function does. Different programming languages have different ways of expressing the steps above, with different keywords and built-in functions. In Python, we use the `if` keyword to check conditions, and the `raise` keyword to print error messages. Additionally, Python enforces the use of built-in error classes, called `exceptions`. There are many built-in exceptions (see: [Python Documentation: Errors and Exceptions](https://docs.python.org/3/library/exceptions.html) ), but we will focus on the most common ones: `ValueError` and `TypeError`.

A `ValueError` is raised when a function receives an argument of the right type but an inappropriate value. For example, a function expects a positive integer, but a negative one is passed.

A `TypeError` is raised when an operation or function is applied to an object of inappropriate type. For example, a function expects a string, but an integer is passed.

By focusing on these common exceptions, you can write robust and error-resistant code that handles unexpected inputs gracefully.

Let's look at a simple example. Let's create a function that takes the square root of a number. This function needs to check for two things. First, that the inputs are indeed numbers, and second, that the inputs are not negative:

```python
import math

def safe_sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < 0:
        raise ValueError("Input must be non-negative")
    return math.sqrt(x)
```

In this example, the `safe_sqrt` function first checks if the input is a number using isinstance. If the input is not a number, it raises a `TypeError`. Then, it checks if the input is non-negative. If the input is negative, it raises a `ValueError`. If both conditions are met, it returns the square root of the input using the `math.sqrt` function.

Notice that the error types allow for the inclusion of a helpful error message. We should always include helpful and descriptive error messages to make it clear what went wrong and why. This practice not only aids in debugging but also helps users of your code understand what input is expected. For example, instead of a generic error message like "Invalid input," a specific message like "Input must be a number" or "Input must be non-negative" provides clear guidance on how to correct the error. Providing detailed error messages is a key aspect of writing maintainable and user-friendly code.

Now, let's see how we can use this function and evaluate it in Python:

```python
>>> print(safe_sqrt(9))  # Expected output: 3.0

3.0
```

```python
>>> print(safe_sqrt(-1)) # Expected to raise ValueError

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in safe_sqrt
ValueError: Input must be non-negative
```

```python
>>> print(safe_sqrt("nine"))  # Expected to raise TypeError

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in safe_sqrt
TypeError: Input must be a number
```

The evaluated results of the `safe_sqrt` function are as follows:

- `safe_sqrt(9)` returns 3.0, as expected.
- `safe_sqrt(-1)` raises a ValueError with the message "Input must be non-negative".
- `safe_sqrt("nine")` raises a TypeError with the message "Input must be a number".

Hurray! We managed to create a function that is robust to the most common input errors. These useful error messages will help future users (ourselves included) to input the correct data and get the correct results. However, sometimes we cannot afford to stop the execution of a program just because our function fails. For example, let's imagine our `safe_sqrt` function is part of a bigger program that has to get the square root of many numbers stored in a list, from which we do not have access before doing the processing.

## The `Try` and `Except` Pattern

In cases such as the one described above, where we cannot afford the program to stop for a single erroneous input, we would like to have the option to try the function with the unknown input, and if it works, we keep the output. However, if it does not work (e.g., raises an `Exception`), we decide separately what to do, depending on the case.

Going back to the example, let's recall that we have a program that gets the square root of many numbers stored in a large list. This program uses our safe_sqrt function and stores the results in a list. This program will run indefinitely, so we cannot afford the program to stop every time it finds something weird in the input numbers. Let's create a function `process_list` that uses `safe_sqrt` to process a list of numbers:

```python
def process_list(numbers):
    results = []
    for num in numbers:
        result = safe_sqrt(num)
        results.append(result)
    return results

numbers = [9, -1, 16, 'twenty', 25, 36, -49, 64, 81, 100]
print(process_list(numbers))
```

When running the above code, it would produce a traceback when it encounters an invalid input. Here is the expected output and traceback:

```python
Traceback (most recent call last):
  File "example.py", line 11, in <module>
    print(process_list(numbers))
  File "example.py", line 5, in process_list
    result = safe_sqrt(num)
  File "example.py", line 6, in safe_sqrt
    raise ValueError("Input must be non-negative")
ValueError: Input must be non-negative
```

This traceback occurs because the function `safe_sqrt` encounters a negative number -1 in the list and raises a `ValueError`.

In its current form, the function `process_list` is sub-optimal. Remember, our program needs to run indefinitely or until it finishes with the whole list of numbers. In the case above, it stopped at the second number. We need to find a way to manage the exceptions and allow the program to keep running.

Here is where the `try` `except` pattern comes in handy. The `try` block lets you test a block of code for errors. The `except` block lets you handle the error. Let's modify our code to handle our exceptions using `try` and `except` in a way that does not stop the program:

```python
def process_list(numbers):
    results = []
    for num in numbers:
        try:
            result = safe_sqrt(num)
        except Exception as e:
            print(f"Error with input {num}: {e}")
            result = None  # Store None or some other placeholder
        results.append(result)
    return results

numbers = [9, -1, 16, 'twenty', 25, 36, -49, 64, 81, 100]
print(process_list(numbers))
```

In this modified `process_list` function, we use a `try` block to attempt to compute the square root with `safe_sqrt`. If an exception is raised, we catch it with the `except` block, print a helpful error message, and store `None` (or some other placeholder) in the results list. This way, the program continues running even if some inputs are invalid.

In the first case, we used the generic `Exception` to catch any errors. However, since we have different types of exceptions, we can be specific and catch them separately. This allows us to handle different errors in different ways, providing more specific error messages and actions for each case. Here is an example:

```python
def process_list(numbers):
    results = []
    for num in numbers:
        try:
            result = safe_sqrt(num)
        except TypeError as e:
            print(f"TypeError with input {num}: {e}")
            result = None  # Store None or some other placeholder
        except ValueError as e:
            print(f"ValueError with input {num}: {e}")
            result = None  # Store None or some other placeholder
        results.append(result)
    return results

numbers = [9, -1, 16, 'twenty', 25, 36, -49, 64, 81, 100]
print(process_list(numbers))
```

In this code, we use separate `except` blocks to handle `TypeError` and `ValueError` specifically. This way, we can provide more precise error messages and take different actions based on the type of error.

It is best practice to catch exceptions independently. Using a generic `Exception` or an empty `except` block can lead to invisible errors, making debugging difficult and potentially masking other issues in the code. By specifying the exception types, you ensure that you handle each case appropriately and maintain the clarity and reliability of your code.

:::::::::::::::::::::::::::::::::::::::  challenge

## Safe Divide

Now that you've learned about input validation, exceptions, and the `try` `except` pattern, here's a challenge for you:

1. Write a function `safe_divide` that takes two numbers and returns their division. The function should check for invalid inputs and raise appropriate exceptions if necessary (e.g., division by zero, non-numeric inputs).
2. Modify the `process_list` function to use `safe_divide` to process a list of tuples, where each tuple contains two numbers to be divided. Ensure that the program continues running even if some divisions fail, and handle different exceptions appropriately.

Example input for `process_list`:
```python
numbers = [(10, 2), (3, 0), (5, 'two'), (9, 3)]
```

Expected output:
```python
[5.0, None, None, 3.0]
```

:::::::::::::::  solution

## Solution
1. Writing the `safe_divide` function:

```python
def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
```

2. Modifying the `process_list` function to use `safe_divide`:

```python
def process_list(pairs):
    results = []
    for a, b in pairs:
        try:
            result = safe_divide(a, b)
        except TypeError as e:
            print(f"TypeError with inputs {a} and {b}: {e}")
            result = None  # Store None or some other placeholder
        except ValueError as e:
            print(f"ValueError with inputs {a} and {b}: {e}")
            result = None  # Store None or some other placeholder
        results.append(result)
    return results

# Example input
numbers = [(10, 2), (3, 0), (5, 'two'), (9, 3)]

# Running the function and printing the results
print(process_list(numbers))
```

Expected output:
```python
TypeError with inputs 5 and two: Both inputs must be numbers
ValueError with inputs 3 and 0: Division by zero is not allowed
[5.0, None, None, 3.0]
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::



:::::::::::::::::::::::::::::::::::::::: keypoints

- **Input Validation**: Ensuring that functions receive the correct type and range of input data to prevent errors and maintain data integrity.
- **Exceptions**: Using built-in error classes like ValueError and TypeError to handle invalid inputs and unexpected conditions.
- **Try and Except Pattern**: Using try and except blocks to manage exceptions and allow programs to continue running even when errors occur.
- **Specific Exception Handling**: Catching specific exception types separately to provide more precise error messages and actions.
- **Best Practices**: Avoiding the use of generic Exception or empty except blocks to prevent invisible errors and maintain code reliability.

::::::::::::::::::::::::::::::::::::::::::::::::::


