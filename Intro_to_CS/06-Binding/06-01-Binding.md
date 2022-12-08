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

#  Binding and scope

We touched on variable bindings in local and global scopes in 
[Chapter 2](../02-Functions/02-01-Functions.md).  It is time to both 
review that material and take a deeper dive. 

## [Aliasing](06-02-Alias.md)

We begin with a review of how _variables_ are bound to _objects_ 
containing _values_ in _name spaces_.  This time, we focus especially 
on the consequences 
of _aliasing_, when two variables are bound to the same object.
This leads us to make an important distinction between _mutable_ and 
_immutable_ objects.

## [Scopes](06-03-Scopes.md)

In Python (as in most programming 
languages), _activation records_ reside as _frames_ on a _stack_. 
Objects containing values, on the other hand, reside in the _heap_. 
Understanding _stack allocation_ and _heap allocation_ is 
fundamental to understanding functions in Python.

With this understanding of binding, frames in the stack, and objects 
in the heap containing values, we can describe more precisely what 
Python does when it encounters a variable name, including "qualified 
names" from other modules.

## TBD
  - qualified names (imported modules)
  - stack and heap (review)

## [Binding and recursion](06-04-Binding-Recursion.md)

Recursive functions follow the same scope rules as any other 
functions.  We revisit the palindrome example from the previous 
chapter to illustrate how binding rules and stack allocation of 
activation 
records work together. 



## Project

TBD


