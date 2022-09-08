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

# Binding in Python:  Functions and Scope

In the prior chapter and accompanying project we both used functions 
that come built-in to Python (like `max` and `sorted`) and functions 
that you can create yourself.  In this chapter we will look further 
at both, but especially at functions that you write. 

```{figure} img/kitchen-tools.jpg
:height: 250px
:name: Tools

Tools alone will not make you a good cook, or a good programmer,
but good cooks and programmers know their tools.
```

## Built-in and imported functions

A collection of reusable software written by others and ready for us 
to incorporate in our own programs is called a _library_.  Python 
has a rich set of libraries.  In this course we will focus on 
libraries that come pre-packaged with a standard Python 3 
installation.   We will omit consideration of additional libraries 
that you can install, although you might use those in other 
courses or for side projects. 

### Always available

Some functions are always present and available. 
They are documented at 
[https://docs.python.org/3/library/functions.html](
https://docs.python.org/3/library/functions.html).
The always available functions
include some we have already seen, like `len` and `sorted`.
They also include some more esoteric functions that you may never 
use.  You do not need to memorize them all! 

Recall that methods are very much like functions, but instead of a 
function call like `len(s)`, we make a method call like `s.strip()`.
The methods of the built-in types are not listed in the table above,
but they are documented with the types of data they operate on.  
For example, `strip` is described in
[documentation for type `str`](
https://docs.python.org/3/library/stdtypes.html#string-methods).
Again, it is not necessary (or perhaps even possible) to memorize 
all the built-in methods for all the built-in types.  Bookmark the
[Python standard library documentation page](
https://docs.python.org/3/library/index.html) and refer to it
whenever you need to use them.  You will soon enough remember the 
functions and methods you use most often.

### Importing other modules

In addition to the functions that are always available and the 
types that are always available with their methods, the Python 
standard library includes a large number of optional modules.  These 
are installed on your computer when you install Python 3, but they 
are not automatically available in your program until you indicate 
your intent to use them.  

To gain access to functions and types from a part of the standard 
library that is not already available, you _import_ it, like this: 

```{code-cell} python3
import random
```

`random` is a _module_ that contains several functions we might want 
to use.  For example, to generate a random integer between
25 and 100, inclusive, we could write 

```{code-cell} python3
r_int = random.randint(25, 100)
print(r_int)
```
Notice that we cannot call `randint` without specifying that it 
belongs to module `random`.  That is because the module is a 
_namespace_ with a distinct set of names for functions and variables.   
It is possible for the same name to appear in more than one 
namespace, referring to distinct values or objects.
That's the point of namespaces:  Because each 
module or other 
namespace has its own set of names, we don't have to worry about 
accidental conflicts between names in different namespaces.  

The global namespace (or _scope_) of your program is distinct from 
the namespace of modules you import.  When you import `random`, the 
name "random" refers to the whole module, and is distinct from any 
names 
that occur _within_ that module, like `random.randint`.  It is even 
possible for the module `random` to contain within it a function 
that is also called `random`.  It does:  

```{code-cell} python3
r_float = random.random()   # Returns v such that 0.0 <= v < 1.0
print(r_float)
```
There is no confusion in interpreting the name `random.random`.  The 
part before the `.` is in the namespace of your program, so it 
refers to the module.  The part after the `.` is in the namespace of 
the module, so it refers to function `random` found in module 
`random`. 

### Finding useful modules

It is not practical to memorize the names of all the modules in the 
Python standard library, let alone all the functions in all those 
modules.  Just bookmark the 
[standard library documentation](
https://docs.python.org/3/library/index.html)
and search.  The modules are mostly well-named and 
have clear, concise descriptions that will help you find what you 
need.   Once again, the modules you use often will stick in memory 
without conscious attempts at memorization.


## Defining and calling a function 

Recall that a Python function can be created by writing a function 
_header_ (starting with `def`) to define how it is called, and a 
function _body_ that describes how it works.  Here is a simple 
function that returns the absolute difference between two integer 
values: 

```{code-block} python3
def abs_diff(x: int, y: int) -> int:
    """Absolute value of the difference between x and y."""
    if x > y: 
        return x - y
    else: 
        return y - x
```

The name of the new function will be `abs_diff`.  Following
[Python naming conventions](https://peps.python.org/pep-0008/), it 
is made of lower case letters (no capital letters), with parts 
separated by underscore ("`_`").  Names matter:  We have chosen 
`abs_diff` rather than `absolute_difference` to keep it short.   
We have not shortened it further to `a_d`, nor chosen an arbitrary 
name like `theta`, because it is important for the name to be 
mnemonic and suggestive of its purpose.  

Function `abs_diff` has two _arguments_, also called _formal 
parameters_, `x` and `y`.   The _actual parameters_ passed to 
`abs_diff` must be `int` objects representing integers.  The 
function header also indicates that `abs_diff` will return a single 
`int` value.  This information comprises the _signature_ of
function `abs_diff`, which is _(int, int) -> int_.  This is enough 
to tell us that `x = abs_diff(5, 7)` is a legal assignment that
assigns an `int` value to `x`, but `abs_diff("cats", "dogs")` is
an error, as is `abs_diff(3, 2) + "turtles"`.

Less obviously, `abs_diff(3.2, 5.4)` is a programming error, even 
though it will return 2.2.  This is because the header of a function 
is a sort of contract between the author of the function and anyone 
who calls that function (even if they are the same person).  Passing 
a floating point number like 3.2 to `abs_diff` breaks that contract.

Why do we care?  Because the contract also states what the author of 
the function is permitted to change without notice.  Calling a 
function in a way that violates the contract might work today, but 
fail sometime later when the author of the function makes a 
perfectly acceptable change to the body of the function.  The user 
of a function must only rely on the contract as given in the 
function header and docstring.  

We treat the body of the function as 
if it were invisible to the programmer who writes calls to that 
function, and subject to change without notice, even if it is the same 
programmer.  This is called _information hiding_. 
Students and beginning programmers often find _information hiding_ 
unintuitive and bothersome.  Understandably so, because as a 
beginner they write most code individually, and seldom work on the 
same project for more than a few weeks.  This is apt to change as 
you take on larger and more complex projects.  The software systems 
that matter to people are typically collaborative or change hands 
over time, and they last much longer than you might imagine.  Even 
the original developer of a function will find themselves 
essentially an outsider when they return to it after a few months 
working on other parts of an application. 

There is another reason for clear, simple contracts and information 
hiding.  Programs are written by humans.  Human brains are amazing, 
but one thing they do not do well is maintain a large number of 
details in working memory.  We solve complex problems by decomposing 
them into smaller problems, then composing simple solutions of 
sub-problems to solve the overall problem.  This is _only_ possible 
if we can ignore and abstract away details of some of the 
sub-problems while working on other parts.   If we need to 
understand _how_ a function works to understand _what_ it does, then 
we can't suppress that detail in any part of the program that uses 
the function.  Information hiding is an essential tool for 
controlling complexity by giving us permission to ignore most 
details most of the time, focusing in on just a few at a time. 

As useful as the _signature_ of a function is in telling us what 
kind of values we can pass to it and what kind of value we can 
expect back from it, the signature alone cannot tell us everything 
we need to know.  The name can help, but it's not enough:  We can 
guess that `abs_diff` probably does not give us the sum or the 
product of its arguments, but the docstring comment immediately 
following the function header gives us a more complete description.
As with choosing names, writing docstring comments that are clear 
but concise is a delicate art that requires care and practice.

What about those formal argument names, `x` and `y`?  Should they be 
longer?  Would it help?  If there were particular meanings 
associated with them (e.g., if the first argument should be a height 
in centimeters and second should be an angle in degrees), then `x` 
and `y` would be poor names.   Consider the following function,
in which longer names are needed: 

```python3
def relative_error(est: float, expected: float) -> float:
    """Relative error of estimate (est) as non-negative fraction 
    of expected value.
    """"
```
Here the formal parameters are `est` (for estimate) and `expected` 
(for expected value, i.e., for the value that `est` should be close 
to).  They are not interchangeable; `relative_error(3.5, 3.8)` will 
not be the same as `relative_error(3.8, 3.5)`.  If we give them 
meaningless names like `x` and `y`, we are very likely to reverse 
them and get the wrong answers.  Ambiguous names would be dangerous 
in that case!   In the case of `abs_diff`, on the other hand, `x` 
and `y` are just numbers, nothing more, which is what their generic 
names communicate. 

## Scope

We saw earlier that when we call a function, the values we "pass" to 
the function are assigned to the formal arguments, which might have 
different names than the variables that we pass: 

```{code-cell} python3
:tags: ["raises-exception"]

def diff(a: int, b: int) -> int:
    """Returns a - b."""
    return a - b

x = 17
y = 14
z = diff(x, y)
print(z)
print(a)     # Error!  Variable a doesn't exist here. 
```

In the example above, function `diff`, the value of `x` is assigned 
to the formal parameter `a` and the value of `y` is assigned to the 
formal parameter `b`, so we get `17 - 14` which is 3.  Also, the 
variables `a` and `b` exist only while `diff` is executing, so the 
final statement will cause an error ("NameError", which 
basically means there is no variable `a` at that point in the program.)

If you assign to a variable within a function, that variable will 
likewise exist only as long as the function is executing. 

```{code-cell} python3
:tags: ["raises-exception"]

def example(a: int) -> int:
    """Example return a + 1."""
    thing = a
    return thing + 1
    
x = example(41)
print(x)
print(thing)    # No thing here! 
```

We say that both `a` and `thing` exist in the _local scope_ of 
function `example`.   It is even possible for two or more variables 
with the same name to exist in different scopes.   

```{code-cell} python3
# Global scope
x = 23
y = 42
m = 19

def example(m: int):
    """Example to illustrate scope"""
    y = 77
    print(f"x is bound to {x} within example")
    print(f"y is bound to {y} within example")
    print(f"m is bound to {m} within example")

# Executing "example" creates the new scope
example(x)
# When "example" finishes, the new scope is deleted

print(f"After example, x is bound to {x}")
print(f"After example, y is bound to {y}")
print(f"After example, m is bound to {m}")
```

During execution of `example(x)`, the scopes created by the example 
above look like this: 

![Scopes during execution of `example(x)`](img/bind_stack.png)

There are several things to notice: 

- Although there are two name spaces (scopes) in the example, there 
  is only one object space.  This will become important when we 
  consider objects that can be modified. 
- When we call `example(x)`, the value 
  bound to `x` in the global scope is bound to `m` in the scope of 
  `example(x)`.  We say that the "actual argument" `x` is bound to 
  the "formal argument" `m` in `example(m: int)`.  This is always 
  how values are passed to functions in Python. 
- The same value, an `int` object containing the integer 23, is 
  bound to more than one name.  This is called _aliasing_.


Aliasing of the same int object to the name `m` in the 
execution of `example`, and to `x` in the global namespace, is 
hardly noticeable.  We might compute some new value by adding the 
values of 23 and 42, but that would be an entirely new `int` object. 
We would not be changing the int object `23` mean something else 
(thank goodness).  We call `int` objects _immutable_ because they 
can never change value. 

You can watch the example in action with
[Python Tutor](https://pythontutor.com/render.html#code=%23%20Global%20scope%0Ax%20%3D%2023%0Ay%20%3D%2042%0Am%20%3D%2019%0A%0Adef%20example%28m%3A%20int%29%3A%0A%20%20%20%20y%20%3D%2077%0A%20%20%20%20print%28f%22x%20is%20bound%20to%20%7Bx%7D%20within%20example%22%29%0A%20%20%20%20print%28f%22y%20is%20bound%20to%20%7By%7D%20within%20example%22%29%0A%20%20%20%20print%28f%22m%20is%20bound%20to%20%7Bm%7D%20within%20example%22%29%0A%0A%23%20Executing%20%22example%22%20creates%20the%20new%20scope%0Aexample%28x%29%0A%23%20When%20%22example%22%20finishes,%20the%20new%20scope%20is%20deleted%0A%0Aprint%28f%22After%20example,%20x%20is%20bound%20to%20%7Bx%7D%22%29%0Aprint%28f%22After%20example,%20y%20is%20bound%20to%20%7By%7D%22%29%0Aprint%28f%22After%20example,%20m%20is%20bound%20to%20%7Bm%7D%22%29&cumulative=false&curInstr=7&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).
It should look very similar to our illustration above, except Python 
Tutor will not draw the `int` objects in the object space.  They 
really are objects, but Python Tutor draws the integer values 
without the objects that hold them to reduce clutter. 


