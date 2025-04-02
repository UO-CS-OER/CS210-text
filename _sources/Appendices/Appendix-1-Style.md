---
jupytext:
  formats: md:myst
  text_representation:
    extension: .myst
    format_name: myst
    format_version: 1.1
    jupytext_version: 1.10.3
    
   
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Style Guide for Python Programs

Most software development organizations have coding guidelines that
constitute a _house style_. These may be based on some more widely used
standard, but often they will also incorporate norms and preferences
developed by a particular organization. Our style guide for CIS 210 
at UO is based on
[PEP 8](https://www.python.org/dev/peps/pep-0008/), extended with
some additional rules suited to an introductory course.


## Living Document

This document represents my best effort at defining style guidelines for
CIS 210, but like many software documents it requires regular revision.
We may find that we need some additional rules, or that some existing
rules are annoyingly strict, or that something is not as clear as it
should be. Also I make mistakes. Students are encouraged to suggest
revisions. Meanwhile, the standard for any particular project is the
version of this document as of the project due date.

## Basics: When in doubt, follow PEP 8

[PEP 8](https://www.python.org/dev/peps/pep-0008/)
is a widely used standard for Python code. It provides guidelines for
all variety of matters from indentation to spacing in expressions.  
Many matters in PEP8 are beyond the scope of CS 210.  Our key 
concerns for CS 210 are summarized here.  If something is unclear or 
not covered here, you may wish to refer to PEP8 (but also let us 
know if something should be spelled out more clearly here).

## Variable and Function Names

We will follow PEP8 naming conventions. 
Use `lower_case` (also known as "snake case") 
for variables and functions.  Use 
`SHOUTS` (all upper case)
for global constants.  Later, in CS 211 you will also encounter 
`UpperCamelCase` for user-defined classes.

Users of a programming language form communities with conventions that
are specific to that language. 
You might have 
used different naming 
conventions with some other programming language.  For example, if 
you have programmed in JavaScript, you might have used 
`lowerCamelCase` for variable names, instead 
of `snake_case` with underscores. When using Python, choose 
pythonic conventions. 

## Line Length 

PEP 8 recommends a maximum line length of 79 characters.  
This matters!  The human eye has limited accuracy as it moves from the
end of one line of text to the beginning of the next line. 79 is not a
magic number (accuracy depends on many other factors, such as vertical
space between lines), but under typical circumstances it is
approximately the length at which readers begin to have trouble finding
the beginning of the correct next line.

PEP 8 refers to
[PEP 257](https://www.python.org/dev/peps/pep-0257/) for docstring
conventions. We will also follow PEP 257 conventions. We will _not_
specify function and method type signatures in docstrings (see below for
the alternative), but when appropriate we may use docstring comments to
say more about arguments and return values.  

## Function docstrings

A docstring should provide information that is *useful to a developer*.
In particular, consider a developer who is building a new module that
uses the functions or classes in your module, or who has been asked to
add a feature to the code, fix a bug, or modify some functionality.
Avoid noisy repetition of information that is already present in type
hints, as well as information that is implicit. 

Every user-written function should include a docstring.  The first 
line of a docstring should very concisely describe what the function 
does.  Some functions require longer docstrings to clearly and 
precisely define their behavior; use your judgment, but be sure the 
docstring describes *what* the function does rather than *how* it 
does it.  In CS 210 many of our function docstrings will also 
contain test cases, as described below. 

### Type annotations in function headers

We will use Python
[type annotations](https://www.python.org/dev/peps/pep-0484/)
(also known as _type hints_) to specify the signature (argument and
return types) of functions and methods.
Type annotations make it possible to specify the
_signature_ of a function very compactly, compared to describing
argument types in a docstring. Instead of this:

```python
def frobnaz(n, s):
    """frob the naz.
    :n:  integer, frob it this many times
    :s:  string from which we extract the naz
    :returns: string in which the naz has been frobbed
    """
```

we will write

```python
def frobnaz(n: int, s: str) -> str:
    """returns copy s with its frob nazzed n times"""
```

An absent return type is equivalent to specifying that the function or
method returns `None`.


### Mutation

Functions that return a value other than `None` (and which therefore 
have
the `-> T`
annotation for some type `T`) should typically *not* modify the value of
their arguments.  

For example, if I write this function header:

```python
def jazziest(musicians: list[str]) -> str:
```

it is implicit that the input list of musicians is not modified.

On rare occasions, concise and efficient code may require a function to
both return a  
value *and* modify an argument. The
`pop` method for lists is an example of a mutator method that returns a
result. This is permissible but must be clearly and explicitly
spelled out in the docstring, and to the extent possible the
function name should suggest that it modifies its input.

For example, if the above function returned the jazziest musician an
also removed it from the list, the function header and docstring might
look like this:

```python
def pull_jazziest(musicians: list[str]) -> str:
    """Remove and return jazziest musician from musicians"""
```

### Composite type annotations

Types like `int` and `str` can be used directly in type annotations.
Types like `tuple` and `list` can also be used in type annotations, but
typically we will prefer to be more specific, e.g., not just a `tuple`
but more precisely
*tuple in which the first element is a string and the second element is
an int*. We can make this more specific annotation by importing type
constructors from the `typing` module:

```python

def i_eat_tuples(t: tuple[str, int]) -> tuple[int, tuple[int, int]]:
    """Convert ("k", n)  to  (n, (n, n))"""
    the_string, the_int = t
    return (the_int, (the_int, the_int))


def to_dict(ls: list[tuple[str, int]]) -> dict[str, int]:
    """Convert [(k,v), (k,v), ...] to {k:v, k:v, ...}"""
    result = {}
    for key, value in ls:
      result[key] = value
    return result
```

### Test cases in docstrings

It is essential to test functions incrementally, as they are written,
rather than waiting until a project is complete.  In CS 210 we will 
*doctests* (tests embedded in function header docstrings) for this 
purpose.   For example, this function header from the Boggler
project contains a single test case for the `normalize` function: 

```python
def normalize(s: str) -> str:
    """Canonical for strings in dictionary or on board
    
    >>> normalize("filter")
    'FILTER'
    """
    return s.upper()
```

As you may infer from the example, a test case is given as
code following the `>>>`, with an expected result on the following 
line.  

We will usually provide a starter test suite with a project, 
mostly in the form of doctests.   These will help you find and 
correct errors early in a project, when they are easiest to fix.  
However, a function that passes all  The
provided test suite is _never_ exhaustive, and passing the provided test
cases is _not_ a guarantee that a project is correct. 



## Symbolic Constants vs Magic Values

A _magic number_ is a constant other than 0, 1, `True`, `False`, or
`""` or `[]` that appears literally in code. For example, this snippet
contains a magic number:

```python
area = radius * radius * 3.141592
```

For more explanation of magic numbers and why they are undesirable, see
the "Unnamed numerical constants" section of the
[Magic Numbers](https://en.wikipedia.org/wiki/Magic_number_(programming))
article on
Wikipedia. I use the concept here to refer not only to numeric
constants, but also to strings that carry some special meaning in an
application.


```python
# Put this near the beginning of the file
PI = 3.141592
...
# Then use the symbolic name throughout
area = radius * radius * PI
```

If the same constant is used in more than one code file, and especially
if it is a value that could conceivably be changed, it should be
factored out into a separate source file. For example, if you are
constructing a board game with multiple source files, the size of the
game board probably belongs in a separate source file.


## Further Reading

[PEP 8](https://www.python.org/dev/peps/pep-0008/)
contains much more than we have included here.  It can be 
worthwhile reading even if you need to skip over parts that 
describe Python features with which you are not yet familiar.  The
[Google Python Style Guide](
https://google.github.io/styleguide/pyguide.html)
is a good example of a "house style" for Python within a software 
development organization.   

Kernighan and Plauger's text
[Elements of Programming Style](
https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style)
is deservedly regarded as a classic.  Despite its age and examples 
drawn from an old programming language that you may (hopefully) 
never use, _Elements of Programming Style_ is especially valuable 
for clear reasoning on matters like good choice of variable names
and writing useful comments.