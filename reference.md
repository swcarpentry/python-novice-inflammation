---
layout: reference
permalink: /reference/
---

## Glossary

{:auto_ids}
additive color model
:   A way to represent colors as the sum of contributions from primary colors
    such as [red, green, and blue](#rgb).

argument
:   A value given to a function or program when it runs.
    The term is often used interchangeably (and inconsistently) with [parameter](#parameter).

assertion
:   An expression which is supposed to be true at a particular point in a program.
    Programmers typically put assertions in their code to check for errors;
    if the assertion fails (i.e., if the expression evaluates as false),
    the program halts and produces an error message.
    See also: [invariant](#invariant), [precondition](#precondition), [postcondition](#postcondition).

assign
:   To give a value a name by associating a variable with it.

body
:   (of a function): the statements that are executed when a function runs.

call stack
:   A data structure inside a running program that keeps track of active function calls.

case-insensitive
:   Treating text as if upper and lower case characters of the same letter were the same.
    See also: [case-sensitive](#case-sensitive).

case-sensitive
:   Treating text as if upper and lower case characters of the same letter are different.
    See also: [case-insensitive](#case-insensitive).

comment
:   A remark in a program that is intended to help human readers understand what is going on,
    but is ignored by the computer.
    Comments in Python, R, and the Unix shell start with a `#` character and run to the end of the line;
    comments in SQL start with `--`,
    and other languages have other conventions.

compose
:   To apply one function to the result of another, such as `f(g(x))`.

conditional statement
:   A statement in a program that might or might not be executed
    depending on whether a test is true or false.

comma-separated values
:   (CSV) A common textual representation for tables
    in which the values in each row are separated by commas.

default value
:   A value to use for a [parameter](#parameter) if nothing is specified explicitly.

defensive programming
:   The practice of writing programs that check their own operation to catch errors as early as possible.

delimiter
:   A character or characters used to separate individual values,
    such as the commas between columns in a [CSV](#comma-separated-values) file.

docstring
:   Short for "documentation string",
    this refers to textual documentation embedded in Python programs.
    Unlike comments, docstrings are preserved in the running program
    and can be examined in interactive sessions.

documentation
:   Human-language text written to explain what software does,
    how it works, or how to use it.

dotted notation
:   A two-part notation used in many programming languages
    in which `thing.component` refers to the `component` belonging to `thing`.

empty string
:   A character string containing no characters,
    often thought of as the "zero" of text.

encapsulation
:   The practice of hiding something's implementation details
    so that the rest of a program can worry about *what* it does
    rather than *how* it does it.

floating-point number
:   A number containing a fractional part and an exponent.
    See also: [integer](#integer).

for loop
:   A loop that is executed once for each value in some kind of set, list, or range.
    See also: [while loop](#while-loop).

function
:   A group of instructions (i.e., lines of code) that transform
    some input [arguments](#argument) to some output.

function call
:   A use of a function in another piece of software.

immutable
:   Unchangeable.
    The value of immutable data cannot be altered after it has been created.
    See also: [mutable](#mutable).

import
:   To load a [library](#library) into a program.

in-place operators
:   An operator such as `+=` that provides a shorthand notation for
    the common case in which the variable being assigned to
    is also an operand on the right hand side of the assignment.
    For example, the statement `x += 3` means the same thing as `x = x + 3`.

index
:   A subscript that specifies the location of a single value in a collection,
    such as a single pixel in an image.

inner loop
:   A loop that is inside another loop. See also: [outer loop](#outer-loop).

integer
:   A whole number, such as -12343. See also: [floating-point number](#floating-point-number).

invariant
:   An expression whose value doesn't change during the execution of a program,
    typically used in an [assertion](#assertion).
    See also: [precondition](#precondition), [postcondition](#postcondition).

library
:   A family of code units (functions, classes, variables) that implement a set of
    related tasks.

loop variable
:   The variable that keeps track of the progress of the loop.

member
:   A variable contained within an [object](#object).

method
:   A function which is tied to a particular [object](#object).
    Each of an object's methods typically implements one of the things it can do,
    or one of the questions it can answer.

object
:   A collection of conceptually related variables ([members](#member)) and
    functions using those variables ([methods](#method)).

outer loop
:   A loop that contains another loop.
    See also: [inner loop](#inner-loop).

parameter
:   A variable named in the function's declaration that is used to hold a value passed into the call.
    The term is often used interchangeably (and inconsistently) with [argument](#argument).

pipe
:   A connection from the output of one program to the input of another.
    When two or more programs are connected in this way, they are called a "pipeline".

postcondition
:   A condition that a function (or other block of code) guarantees is true
    once it has finished running.
    Postconditions are often represented using [assertions](#assertion).

precondition
:   A condition that must be true in order for a function (or other block of code) to run correctly.

regression
:   To re-introduce a bug that was once fixed.

return statement
:   A statement that causes a function to stop executing and return a value to its caller immediately.

RGB
:   An [additive model](#additive-color-model)
    that represents colors as combinations of red, green, and blue.
    Each color's value is typically in the range 0..255
    (i.e., a one-byte integer).

sequence
:   A collection of information that is presented in a specific order.
    For example, in Python, a [string](#string) is a sequence of characters,
    while a list is a sequence of any variable.

shape
:   An array's dimensions, represented as a vector.
    For example, a 5×3 array's shape is `(5,3)`.

silent failure
:   Failing without producing any warning messages.
    Silent failures are hard to detect and debug.

slice
:   A regular subsequence of a larger sequence,
    such as the first five elements or every second element.

stack frame
:   A data structure that provides storage for a function's local variables.
    Each time a function is called, a new stack frame is created
    and put on the top of the [call stack](#call-stack). When the function returns,
    the stack frame is discarded.

standard input
:   A process's default input stream.
    In interactive command-line applications,
    it is typically connected to the keyboard; in a [pipe](#pipe),
    it receives data from the [standard output](#standard-output) of the preceding process.

standard output
:   A process's default output stream.
    In interactive command-line applications,
    data sent to standard output is displayed on the screen;
    in a [pipe](#pipe),
    it is passed to the [standard input](#standard-input) of the next process.

string
:   Short for "character string",
    a [sequence](#sequence) of zero or more characters.

syntax error
:   A programming error that occurs when statements are in an order or contain characters
    not expected by the programming language.

test oracle
:   A program, device, data set, or human being
    against which the results of a test can be compared.

test-driven development
:   The practice of writing unit tests *before* writing the code they test.

traceback
:   The sequence of function calls that led to an error.

tuple
:   An [immutable](#immutable) [sequence](#sequence) of values.

type
:   The classification of something in a program (for example, the contents of a variable)
    as a kind of number (e.g. [floating-point](#float), [integer](#integer)), [string](#string), or something else.

type of error
:   Indicates the nature of an error in a program. For example, in Python,
    an `IOError` to problems with file input/output.
    See also: [syntax error](#syntax-error).

while loop
:   A loop that keeps executing as long as some condition is true.
    See also: [for loop](#for-loop).
