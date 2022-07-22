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
23", because it is really a _statement_ or command that binds the 
a reference to an object representing the integer 
to the name "x".  

One way to see how different this is from the 
"equals" we know from math is to try turning it around --- what 
happens if 
you write `23 = x` instead of `x = 23`?   Try it in IDLE or, if you 
are reading this in a executable format, try modifying the code cell 
above. 


### Some Python object types

Python supports the following basic types (as well as some others).

|  Python type |  Meaning  | Example |
|--------------|-----------|---------|
| int | Integer; represented precisely. | 42 |Python integers can be arbitrarily large |
| float | Floating point, an approximation of a real number. | 3.1415 |
| str | String, which is what we call text. Strings may contain many kinds of characters, including Ελληνικά and 漢子.| "Hello world" | 
| bool | Boolean (truth value) | False |



### Lists 

Python also gives us ways of combining values into composite objects.
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
is a list with two elements.  The first element of that list is a 
list with two elements, and the first element of _that_ list is a 
string ("corvids").   



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

What happens if you modify the code above to add an additional 
definition for "mouse", perhaps "A computer input device", without 
removing the first definition?  What does this tell you about the 
`dict` type in Python? 





