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

# Binding:  Functions and Scope

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

:::{note}
This section introduces many closely related terms like _scope_, 
_namespace_, and _frame_, as well as some terms like _argument_ that 
are often used interchangeably with other terms like _parameter_ in 
Python documentation.  It can be confusing!  We have provided
a short [discussion of terminology](02-04-Terms.md) to help you
keep them straight.
:::


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
separated by underscore ("`_`").  The following
[chapter on pragmatics](02-03-Hygiene.md)
discusses the choice of name in more depth. 

Function `abs_diff` has two _arguments_, also called _formal 
parameters_, `x` and `y`.   The _actual arguments_ passed to 
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
As [the next chapter](02-03-Hygiene.md) discusses in more depth,
it is essential that a programmer who wants to make use of
`abs_diff` be able to depend entirely on the contract given by
the function header and docstring, without referring to the body of 
the function. 


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

It may help to see this example step-by-step in PythonTutor.  If you 
are viewing this chapter in a web browser, use the 
"next" button in the frame below to step through it. 

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20diff%28a%3A%20int,%20b%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20%22%22%22Returns%20a%20-%20b.%22%22%22%0A%20%20%20%20return%20a%20-%20b%0A%0Ax%20%3D%2017%0Ay%20%3D%2014%0Az%20%3D%20diff%28x,%20y%29%0Aprint%28z%29%0Aprint%28a%29%20%20%20%20%20%23%20Error!%20%20Variable%20a%20doesn't%20exist%20here.&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

In the example above, function `diff`, the value of `x` is assigned 
to the formal argument `a` and the value of `y` is assigned to the 
formal argument `b`, so we get `17 - 14` which is 3.  Also, the 
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

You can also 
[step through this example in PythonTutor.](
https://pythontutor.com/render.html#code=def%20example%28a%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20%22%22%22Example%20return%20a%20%2B%201.%22%22%22%0A%20%20%20%20thing%20%3D%20a%0A%20%20%20%20return%20thing%20%2B%201%0A%20%20%20%20%0Ax%20%3D%20example%2841%29%0Aprint%28x%29%0Aprint%28thing%29%20%20%20%20%23%20No%20thing%20here!&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
)

We say that both `a` and `thing` exist in the _local scope_ of 
function `example`.   It is even possible for two or more variables 
with the same name to exist in different scopes.   

```{code-cell} python3
# Global scope (global frame or namespace)
x = 23
y = 42
m = 19

def example(m: int):
    """Example to illustrate scope"""
    y = 77
    print(f"x is bound to {x} within example")
    print(f"y is bound to {y} within example")
    print(f"m is bound to {m} within example")

# Executing "example" creates the new local scope
example(x)
# When "example" finishes, the new scope is deleted

print(f"After example, x is bound to {x}")
print(f"After example, y is bound to {y}")
print(f"After example, m is bound to {m}")
```

You can
[step through this example in PythonTutor](
https://pythontutor.com/render.html#code=%23%20Global%20scope%0Ax%20%3D%2023%0Ay%20%3D%2042%0Am%20%3D%2019%0A%0Adef%20example%28m%3A%20int%29%3A%0A%20%20%20%20%22%22%22Example%20to%20illustrate%20scope%22%22%22%0A%20%20%20%20y%20%3D%2077%0A%20%20%20%20print%28f%22x%20is%20bound%20to%20%7Bx%7D%20within%20example%22%29%0A%20%20%20%20print%28f%22y%20is%20bound%20to%20%7By%7D%20within%20example%22%29%0A%20%20%20%20print%28f%22m%20is%20bound%20to%20%7Bm%7D%20within%20example%22%29%0A%0A%23%20Executing%20%22example%22%20creates%20the%20new%20scope%0Aexample%28x%29%0A%23%20When%20%22example%22%20finishes,%20the%20new%20scope%20is%20deleted%0A%0Aprint%28f%22After%20example,%20x%20is%20bound%20to%20%7Bx%7D%22%29%0Aprint%28f%22After%20example,%20y%20is%20bound%20to%20%7By%7D%22%29%0Aprint%28f%22After%20example,%20m%20is%20bound%20to%20%7Bm%7D%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
)

During execution of `example(x)`, the scopes created by the example 
above look like this: 

![Scopes during execution of `example(x)`](img/bind_stack.png)

There are several things to notice: 

- Although there are two name spaces (scopes or frames) in the example, 
  there
  is only one object space.  PythonTutor shows the `int` values
  directly in frames as a simplification, but they are actually
  objects in object space.  
- When we call `example(x)`, the value
  bound to `x` in the global scope is bound to `m` in the scope of
  `example(x)`.  We say that the "actual argument" `x` is bound to 
  the "formal argument" `m` in `example(m: int)`.  This is always
  how values are passed to functions in Python.
- The same value, an `int` object containing the integer 23, is
  bound to more than one name.  This is called _aliasing_.  
  It will become important when we consider objects like 
  lists that can be modified, with intentional effects
  or unintentional [side effects](Functions:Hygiene:side-effects).


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

## Global variables

Generally we want to keep the local variables in one function 
execution completely separate not only from the local variables of 
other functions, but also from the global namespace of our program. 
We do _not_ want to write code like this: 

```{code-cell} python3
def bad_bad_bad(x: int):
    """Don't do this!"""
    s.append(x)   # s is not local to bad_bad_bad. 
    
s = [1, 2]
bad_bad_bad(3)    # Not obvious that we are changing s! 
print(s)
```

In this example, `bad_bad_bad` is a function that accesses and 
even changes the variable called `s`, not in its own namespace (the 
local scope of the function) but in the global scope of the program.
The function is at least appropriately named.  This is almost always 
a bad idea.  Python nonetheless permits it because there are a few, 
rare cases in which accessing a global variable is needed.  

If you are reading the online version of this text, you can
[step through `bad_bad_bad` in PythonTutor](
https://pythontutor.com/render.html#code=def%20bad_bad_bad%28x%3A%20int%29%3A%0A%20%20%20%20%22%22%22Don't%20do%20this!%22%22%22%0A%20%20%20%20s.append%28x%29%20%20%20%23%20s%20is%20not%20local%20to%20bad_bad_bad.%20%0A%20%20%20%20%0As%20%3D%20%5B1,%202%5D%0Abad_bad_bad%283%29%20%20%20%20%23%20Not%20obvious%20that%20we%20are%20changing%20s!%20%0Aprint%28s%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false). 

One case in which we might need to access a global variable from 
within a function is when the global variable is some kind of fixed 
constant or configuration.  For example, an anagram finder might 
depend on a file that holds a list of dictionary words.  We do not 
want to bury the name of that file inside some function.  We might 
instead define it near the beginning of the program as a _global 
constant_, like the variable `DICT` in the Jumbler project: 

```python
DICT = "shortdict.txt"    # Short version for testing & debugging
# DICT = "dict.txt"       # Full dictionary word list

# ... other code ... 

def find(anagram: str):
    """Print words in DICT that match anagram.
    ... test cases here ... 
    """
    dict_file = open(DICT, "r") 
    #  Reference to DICT is better than burying
    #  the configuration setting here in the function.
    for line in dict_file:
          word = line.strip()
          if word == anagram:
              print(word)
```

Note the Python convention of using all upper case letters to make it 
clear to readers of this code that `DICT` is a global variable.  

Very rarely we might need to update a global variable from within a 
function.  This is quite unusual, and never something to be done 
without first considering alternatives.  One of those rare cases is 
when for some reason we need to keep a count of how many times a 
function has been called.  We cannot keep the count in a variable 
that is local to the function, because then the local variable would 
disappear after each call.  A new variable would be created each 
time the function is called.   This code will not even work: 

```{code-cell} python3
:tags: ["raises-exception"]

count_foo = 0

def foo() -> int: 
  """This will not work!"""
  count_foo = count_foo + 1
  return count_foo
  
print(foo())
print(foo())
print(foo())
```

What happened here?  While we may have intended to access the global 
variable `count_foo` from within `foo`, we did not. Because there is 
an assignment to `count_foo`, Python has created a local variable 
`count_foo`.  It has the same name, but it is not the same variable, 
because it is in the namespace (scope) of the execution of function 
`foo`.  When Python attempts to evaluate `count_foo + 1`, it 
references  the local variable `count_foo` and finds that it does not 
yet have a value. Hence the "UnboundLocalError". 

If we really, really wanted to reference and change a global 
variable, Python will allow us to _explicitly_ declare that it is 
the global variable `count_foo` we want to refer to, and not a new 
local variable with the same name.  

```{code-cell} python3
count_foo = 0

def foo() -> int: 
    """This will work.  That doesn't make it a good idea."""
    global count_foo
    count_foo = count_foo + 1
    return count_foo
  
print(foo())
print(foo())
print(foo())
```

If you are reading online, you can
[trace it in PythonTutor](
https://pythontutor.com/render.html#code=count_foo%20%3D%200%0A%0Adef%20foo%28%29%20-%3E%20int%3A%20%0A%20%20%20%20%22%22%22This%20will%20work.%20%20That%20doesn't%20make%20it%20a%20good%20idea.%22%22%22%0A%20%20%20%20global%20count_foo%0A%20%20%20%20count_foo%20%3D%20count_foo%20%2B%201%0A%20%20%20%20return%20count_foo%0A%20%20%0Aprint%28foo%28%29%29%0Aprint%28foo%28%29%29%0Aprint%28foo%28%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
).

## Hygiene and pragmatics

Even in this section devoted to the basic mechanics of defining and 
calling functions, it has been difficult to completely avoid talking 
about _good_ and _bad_ approaches.  The
[next section](02-03-Hygiene.md)
takes up hygiene of function design in more depth.  
Instructions for [our project](https://github.com/UO-CS210/pi)
discusses pragmatics of choosing parts of the code to decompose into 
functions. 

## Terminology

The many terms like _scope_ and _frame_ can be confusing, especially 
since you will encounter different names for the same or closely 
related concepts in documentation.  We have provided a brief
[terminology review](02-04-Terms.md) to help you sort them out.
