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

# A Notional Computer

As you learn to construct useful programs in Python, you will need a
clear mental model of how your Python programs work.  At first this
may seem trivial, and hardly any improvement over remembering the
observable effects of particular sequences of commands.  As you tackle
larger problems, a clear and accurate mental model will become more 
and more helpful.  It will be the difference between a huge and 
disordered set of particulars, beyond the capacity of human memory, 
and a much smaller, systematic set of basic understandings into 
which it is easier to fit one more piece.

Depending on your background in computing, much of this chapter may 
be review for you.  If you have learned to program in a different 
programming 
language, such as C or Java or Javascript, you may note some 
differences between concepts you are familiar with and our notional 
Python computer.  But even if you have programmed before in Python, 
and feel that you have a good grasp of basic concepts such as 
variables and types, you should read this chapter with some care to 
ensure that your mental model is consistent with the model that we 
will rely upon as we dive deeper into computational problem solving 
through Python programming. 


## Languages present notional computers 

A programming language presents us an abstraction of a physical 
computer.  By _abstraction_ I mean that it hides ("abstracts 
away") certain details,
such as whether you are using a computer with a central processing 
unit (CPU) based in the Intel x86 series, a computer with a CPU
based on the Arm architecture, or perhaps some other processor that
hasn't even been invented yet.  

Each programming language presents us a _notional_ computer that can 
be implemented on several different kinds of computer hardware. 
Because we can program in a language, and not for a particular 
collection of circuits, it is possible to _learn to program_, and 
not only _learn to program this particular machine_.  

The notional computers presented by different programming languages, 
such as Python, Javascript, Java, and C++, differ in some 
important ways, yet have many things in common.  As your 
knowledge grows, you will likely use several languages, sometimes 
even on the same project.  A clear understanding of what those 
notional computers have in common will help you transfer your 
understanding of programming in one language to others.  A clear 
understanding of their differences will help you keep them straight, 
choose well, and use them together.  

For now it is best to focus on a single programming language and the 
notional computer it presents us.  We have chosen Python as a first 
language because it presents an exceptionally 
simple and uniform notional computer.  In particular we will use
version 3.10 or greater of Python. We will occasionally note ways 
in which the Python notional computer resembles that of other 
languages, and ways in which it differs from languages that you may 
already be familiar with or that you are likely to use in the future. 

## The Python Notional Computer

A notional computer is like a building toy, perhaps wooden
blocks, Legos, or Tinker Toys. The kit comes 
with a handful of basic
parts that can be combined to build an unlimited
set of more complex structures. A particular kit provides us both
some basic parts and some ways of putting them together.  Likewise a 
programming language provides us some basic elements like objects of 
particular types, and ways of building up larger structures from them. 
A _program_ is like a set of directions for constructing and 
manipulating a structure, the _execution state_ of the running program.

### Basic Python data types

Python supports the following basic types (as well as some others).

|  Python type |  Meaning  | Example |
|--------------|-----------|---------|
| int | Integer; represented precisely. | 42 |Python integers can be arbitrarily large |
| float | Floating point, an approximation of a real number. | 3.1415 |
| str | String, which is what we call text. Strings may contain many kinds of characters, including Ελληνικά and 漢子.| "Hello world" | 
| bool | Boolean (truth value) | False |

Every value in Python has a type.  For example, `0` has type `int`, 
but `"0"` has type `str`.   The meaning of an operation like 
addition depends on the types of values.  To see this clearly, 
consider addition.   

```{code-cell} python3
"111" + "222"
```

For strings (type `str`), addition means concatenation.  What 
happens if you remove the quotes, so that the code cell above is 
addition of `int` values instead of `str` values?  What if you make 
one of the values an integer, but not the other?   (Try it in IDLE 
or in the code cell above). 

Sometimes an operation on values of one type can produce a value 
of another type.  For example, the values `5` and `2` are both 
integers (type `int`).  What is the value of `5 / 2`?

```{code-cell} python3
5 / 2
```

Besides common arithmetic operations like `+` and `-`, the basic 
types have many built-in _functions_ like `max` and 
`round`.   For example, `max(5, 7)` and `max(7, 5)` both produce the 
value `7`.   We say call `5` and `7` the _arguments_ of the `max` 
function in this example, and we say it _returns_ 7.  

Just as we can build complex expressions like `(5 + 3) / 2` by 
combining operations like `+` and `/`, we can use the result of one 
function as an argument to another, like `max(min(2, 3), 7)`.  We 
can also freely mix function calls and operations, like
`max(3 + 7, 8)` or `min(3, 7) + len("Some text")`. 

There is 
no difference between _arguments_ of a function like "max" and 
_operands_ of an operator like `+` except in how we write them.  

```{code-cell} python3
min(3, 7) + len("Some text")
```


### Collections 

Python also gives us ways of combining values in composite 
objects, called _collections_.  

### Lists 

The collections we will use most are _lists_, which are sequences of 
other values.  For example, `[1, 2, "buckle my shoe"]` is a list of
three elements.  The first two elements are `int` (integer) objects and 
the 
third is a 
`str` (string) object.  The elements of
a list may also be lists (we call this _nesting_, like matryoshka 
dolls).

```{figure} img/800px-Matryoshka_transparent.png
:height: 150px
:name: Matryoshka

Lists within lists are "nested", like nested dolls.  (Image by user 
Fanghong in Mediawiki commons, used under CC by SA license.) 
```

We can _nest_ lists as deeply as we like. 
`[["corvids", ["crow", "raven"]], ["primates", ["lemur", "human"]]]`
denotes a list with two elements.  The first element of that list is a 
list with two elements, and the first element of _that_ list is a 
string ("corvids").   

```{figure} img/nested-list.png
:height: 300px
:name: nested

List elements can be references to other lists, as well as other
kinds of object, as illustrated by this representation of 
`[["corvids", ["crow", "raven"]], ["primates", ["lemur", "human"]]]`
```


### Dictionaries

A _dictionary_ collection (type `dict`) is like a table with a column 
with two 
columns. We could construct a `dict` like the kind of dictionary in 
which we look up word definitions: 

```{code-cell} python3
d = { 
  "mouse" : "A small rodent", 
  "rat" : "A somewhat larger rodent", 
  "bat" : "A flying rodent",
  42 : "The answer to life, the universe, and everything"
  }
print(d)
```

What happens if you modify the code above to add another 
definition for "mouse", perhaps "A computer input device", without 
removing the first definition?  What does this tell you about the 
`dict` type in Python?   (Try it in IDLE or by editing the code cell 
above.)

## Binding

As a Python program runs, the _execution state_ is modified. 
An important component of the execution state is a set of _bindings_,
which are associations of names with objects that contain values. 
We can _bind_ a name with _assignment_, which we write `=`. 

```{code-cell} python3
x = 23
```

```{figure} img/bind_x_23.*

The name _x_ is bound to a value, which is a reference to
an object containing the integer 23.  
```

It is tempting to pronounce this "x equals 23", because it looks 
like a mathematical equation.  We suggest pronouncing it "x gets 
23", because it is really a command that binds 
a reference to an object representing the integer 
to the name "x".  

One way to see how different this is from the 
"equals" we know from math is to try turning it around --- what 
happens if you write `23 = x` instead of `x = 23`?   Try it in IDLE or,
if you are reading this in a executable format, try modifying the code
cell above. 

We call `x` a _variable_ because it can be bound to different values 
at different times as the program executes.  If we have an 
assignment like `x = y + 2`, the right-hand side of the assignment 
(`y + 2`) is evaluated first, using the current binding of `y`, and 
then the result is bound to `x`.  We can even use a current binding of 
a variable to compute a new binding for the same variable: 

```{code-cell}  python3
x = 7
print(x)
x = x + 2
print(x)
```

## Objects and Values

When we say that a variable like `x` has a value like `9`, we really 
mean that `x` is bound to an object, and the object contains the 
`int` value `9`.  It is easier to ignore that detail and
just say that 
`x` "has the value" 
`9`.  Often that is just fine.

The distinction between binding to a value and binding to an object 
containing a value matters when we are dealing with composite 
_collection_ objects like lists and dictionaries.  It is possible 
for two different names to be bound to the same collection object.  
Moreover, the value of a collection object can be modified.  For 
example, when we add an element to a list with `append`, we do not 
get a new, longer list object.  Rather, we _mutate_ (that is, change)
the value in the existing list object.  

Consider the following. 

```{code-cell} python3
a = ["one", "two", "three"]
b = ["one", "two", "three"]
c = b
c.append("four")
print(a)
print(b)
print(c)
```

Can you explain what happens when we execute the Python code above?  
It helps to have a mental picture of the objects bound to the 
variables `a`, `b`, and `c`: 

```{figure} img/bind_alias_before.png

Variables _b_ and _c_ are bound to the same `list` object. 
Variable _a_ is bound to a different object, although it
contains the same `str` elements.   We say _b_ and _c_
are _aliases_.   
```

When we executed `c.append("four")`, we change the value of the 
object that both variable `c` and variable `b` are bound to: 

```{figure} img/bind_alias_before.png

Variables _b_ and _c_ are bound to the same `list` object. 
Variable _a_ is bound to a different object, although it
contains the same `str` elements.   We say _b_ and _c_
are _aliases_.   
```

You may be tempted to skip over this part of the notional computer 
state without fully understanding it.  Don't!  Although it seems 
confusing at first, it is the key to making sense of much that 
follows.  You must understand that two variables can be bound to the 
same object, so that changing (_mutating_) the value of that object 
changes the value associated with both variables.  We will see that 
this is actually a powerful tool we can use when we write new 
_functions_. 

## Scopes and Functions

So far we have considered a single _name space_ in which the name of 
a variable can be bound to an object containing a value.  If we had 
only a single name space, it would be very difficult to write large 
and complex programs.  Such a program might have thousands of 
variables, which would force us to give them names like
`angle_x_btwn_fuselage_and_main_fin`.  Programming would be 
unpleasant, and reading programs written by others would be even 
more unpleasant. 

Python makes it easier for us to use short but meaningful names by 
allowing us to have more than one set of bindings, called _scopes_. 
The same variable name can have different bindings in different scopes.

In particular, execution of a function creates a scope for variables 
that are bound within the function.  In addition to the built-in 
functions like `max` and `len`, we can write our own functions.  We 
call our own functions just like we call the built-in functions. 

```{code-cell} python3
def middle(x: int, y: int) -> int: 
  """Returns the an integer roughly midway between x and y"""
  result = (x + y) // 2
  return result
  
a = middle(12, 16)
print(a)
```

In the code cell above, integers `12` and `16` are passed as 
_arguments_ to function `middle`.  Objects containing these `int` 
values are bound to variables `x` and `y` in a _scope_ (separate 
name space) when `middle` begins execution.  This _scope_ is 
discarded when function `middle` finishes execution by returning the 
result value. 

Note the syntax of a Python function.  The body of the function is 
indented.  The _head_ of the function indicates the _formal 
arguments_ (`x` and `y` in this case) and their types, as well as 
the type of result the function will return.  The number and types 
of the formal arguments and the type of the result are called the 
_signature_ of the function.  You can think of them as a (part of) a 
contract between the function and code that calls the function. The 
rest of the contract is given by the _docstring comment_ immediately 
after the head.  In addition to being visible in your Python source 
code, the docstring comment is available through the `help` function:

```{code-cell}  python3
help(middle)
```


You can think of scopes as being stacked one atop another.  When we 
begin executing a function, a new scope is stacked atop the others.
When it finishes, that scope is removed from the stack, uncovering
the scope that was previously on top.  

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

![Scopes during execution of `example(x)`](../Intro_to_CS/02-Functions/img/bind_stack.png)

There are several things to notice: 

- Although there are two name spaces (scopes) in the example, there 
  is only one object space.  
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

## Control Flow:  Loops and Decisions

The operations we have performed so far have been very simple.  We 
can build up more complex operations by writing and calling 
functions, and in fact this is a fundamental tool in composing 
programs.  We need one more kind of "glue" for constructing more 
complex programs from simple parts:  Control flow. 

We have already written sequences of commands (statements).  We did 
not say explicitly that they are executed in order, one after the 
other, but you likely inferred that even if you were not previously 
familiar with a sequential, imperative programming language like 
Python.  (There are other kinds of languages, but _imperative_ 
languages that modify an execution _state_ through a sequence of 
commands are most common.)  

### Decisions: The "if" statement

Python provides an `if` 
construct for choosing between possible actions.  We'll illustrate 
it with a very simple example: 

```{code-cell} python3
x = 17
y = 30
if x > y: 
    x_y_max = x
else: 
    x_y_max = y
print(x_y_max)
```

We can _nest_ `if` statements within other `if` statements: 

```{code-cell} python3
x = 17
y = 30
z = 15
if x > y: 
    if x > z:
      biggest = x
    else:
      biggest = z
else:
    if y > z:
      biggest = y
    else: 
      biggest = z
print(biggest)
```

Sometimes we can write simpler, clearer code by using `elif` instead of 
nesting `if` statements.  Combining comparisons with `and` and `or` 
can also help.  

```{code-cell} python3
x = 17
y = 30
z = 15
if x > y and x > z:
  biggest = x
elif y > x and y > z:
  biggest = y
else:
  biggest = z
print(biggest)
```

```{note}
We have chosen an over-simplified example to illustrate `if` and 
`elif`.  An even better way to find the largest of three values 
would be to use Python's built-in `max` function.
```

### Repetition (looping): `for` 

Often we need to repeat the same action with different values.  Most 
commonly we will want to perform an action with each element of a 
collection (e.g., a `list` or `dict` object).  Python lets us do 
this with a _for loop_, like this: 

```{code-cell} python3
animals = ["elephant", "tapir", "manatee"]
for pet in animals:
    print(pet)
```

Typically, when we _loop through_ a collection of objects, we 
accumulate some information about the collection as a whole. Suppose,
for example, we wanted to determine the number of characters 
(letters) in all the animal names together.  We would _initialize_ a 
total just before the loop, then _accumulate_ values within the loop.

```{code-cell} python3
animals = ["elephant", "tapir", "manatee"]
total_length = 0
for pet in animals:
    total_length = total_length + len(pet)
print(total_length)
```

This is such a common _pattern_ that it has a name, the _accumulator 
pattern_.  

We will see many variations on `for` loops and on the accumulator 
pattern in projects.  There are other kinds of loops in Python (e.g.,
a `while` loop repeats as long as some condition is true), but `for` 
loops are most common. 





