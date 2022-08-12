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
such as Python, Javascript, Java, and C++, may differ in some 
important ways, and yet have many things in common.  As your 
knowledge grows, you will likely use several languages, sometimes 
even on the same project.  A clear understanding of what those 
notional computers have in common will help you transfer your 
understanding of programming in one language to others.  A clear 
understanding of their differences will help you keep them straight, 
choose well, and use them together. 

For now it is best to focus on a single programming language and the 
notional computer it presents us.  We have chosen Python as an 
excellent first language, because it presents an exceptionally 
simple and uniform notional computer.  In particular we will use
version 3.10 or greater of Python. 

## The Python Notional Computer

A notional computer is like a building toy, perhaps wooden
blocks, Legos, Tinker Toys, or something similar. The kit comes with a
handful of basic
parts that can be combined to build an unlimited
set of more complex structures. A particular kit provides us both
some basic parts and some ways of putting them together.  Likewise a 
programming language provides us some basic elements like objects of 
particular types, and ways of building up larger structures from them. 
A _program_ is like a set of directions for constructing and 
manipulating a structure, the _execution state_ of the running program. 

The Python notional computer presents us with a program execution state
consisting of a set of _name spaces_.   A name space is an 
association of _names_ with _value_.  A _value_ is a reference to an 
_object_.  The type of the object determines what we can do with it 
(like the shape of a block). 

We can _bind_ value to a name with _assignment_, which we write `=`. 

```{code-cell} python
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

Bindings can appear in different _scopes_, also known as _name 
spaces_.  We will say more about that after introducing a few of 
Python's data types. 


### Some Python data types

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

```{code-cell} python
"111" + "222"
```

For strings (type `str`), addition means concatenation.  What 
happens if you remove the quotes, so that the code cell above is 
addition of `int` values instead of `str` values?  What if you make 
one of the values an integer, but not the other?   (Try it in IDLE 
or in the code cell above). 

Sometimes an operation on one values of one type can produce a value 
of another type.  For example, the values `5` and `2` are both 
integers (type `int`).  What is the value of `5 / 2`?

```{code-cell} python
5 / 2
```

Besides common arithmetic operations like `+` and `-`, the basic 
types have many built-in _functions_ like `max` and 
`round`.   For example, `max(5, 7)` and `max(7, 5)` both produce the 
value `7`.   We say call `5` and `7` the _arguments_ of the `max` 
function in this example, and say that it _returns_ 7.   There is 
no difference between _arguments_ of a function like "max" and 
_operands_ of an operator like `+` except in how we write them.

### Lists 

Python also gives us ways of combining values into composite 
objects.
The combination we will use most are _lists_, which are sequences of 
other values.  For example, `[1, 2, "buckle my shoe"]` is a list of
three elements, two `int` objects and a `str` object.  The elements of
a list may also be lists (we call this _nesting_, like matryoshka 
dolls).

```{figure} img/800px-Matryoshka_transparent.png
:height: 150px
:name: Matryoshka

Lists within lists are "nested", like nested dolls.  (Image by user 
Fanghong in Mediawiki commons, used under CC by SA license.) 
```

We can "nest" lists as deeply as we want, e.g., 
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

A _dictionary_  (type `dict`) is like a table with a column with two 
columns. We could construct a `dict` like the kind of dictionary in 
which we look up word definitions: 

```{code-cell} python
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
`dict` type in Python? 

## Scopes

Binding of a value to a name takes place in a _scope_.  The same 
name might have different bindings in different scopes.  In 
particular, execution of a function creates a scope for variables 
that are bound within the function.  

You can think of scopes as being stacked one atop another.  When we 
begin executing a function, a new scope is stacked atop the others.  
When it finishes, that scope is removed from the stack, uncovering
the scope that was previously on top.  

```{code-cell} python
# Global scope
x = 23
y = 42
m = 19

def example(m: int):
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







