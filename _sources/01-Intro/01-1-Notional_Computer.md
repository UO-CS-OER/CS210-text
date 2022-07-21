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
and more important.  It will be the difference between a huge and 
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

The Python notional computer presents us with a program execution state
consisting of a set of _name spaces_.   A name space is an 
association of _names_ with _value_.  A _value_ (also called an 
_object_) has a type, 
which determines what we can do with it.  

### Some Python object types

Python supports the following basic types (as well as some others).

|  Python type |  Meaning  | Example |
|--------------|-----------|---------|
| int | Integer; represented precisely. | 42 |Python integers can be arbitrarily large |
| float | Floating point, an approximation of a real number. | 3.1415 |
| str | String, which is what we call text. Strings may contain many kinds of characters, including Ελληνικά and 漢子.| "Hello world" | 
| bool | Boolean (truth value) | False |

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
