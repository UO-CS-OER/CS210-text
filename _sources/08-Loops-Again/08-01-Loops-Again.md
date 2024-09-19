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
# Loops Again

Yet again?  Yes, and again and again, because loops are such a 
fundamental algorithmic tool, and because it takes some time to 
fully internalize loop patterns.  And isn't it appropriate that we 
should have some repetition in studying loops? 

## Python `for` loops

Python's `for` loops are convenient, flexible, and expressive.  The 
cost of this flexibility is that students often get confused by 
their choices.  The [What For](08-02-WhatFor.md) section was 
contributed by CS 211 learning assistant
[Audra McNamee](https://audmcname.com/) (also a talented
[comics artist](https://audmcname.com/cat/comics/)).  It especially 
reviews the difference between iterating over _elements_ of a 
list (`for el in li:`) and iterating over the _indexes_ of a list 
(`for i in range(len(li)):`).  Mixing them up is one of the _very 
most common_ errors on CS 210 exams. 

- [What For](08-02-WhatFor.md)

## The Python `list` type

We've already used lists a lot, but a peek inside the Python `list` 
type will help us understand why some list operations require just 
constant time and other operations require time proportional to the 
length of the list.  We'll also take a quick look at the cost of 
string (`str`) operations, and at dictionaries (`dict`). 

- [Lists Again](08-03-Lists-Again.md)


## Exercises

- [Loop and list exercises](08-04-Exercises.md)

## Project

The [path simplification project](
https://github.com/UO-CS210/08-Path-Simplifier)
introduces an algorithm that is almost certainly used in every map 
application you've used, including Google maps, but also in 
production of paper maps.  It provides practice with recursion, list 
indexing, and loops that access and build lists.