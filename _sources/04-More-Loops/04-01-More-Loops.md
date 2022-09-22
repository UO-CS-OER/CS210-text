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

# Loops and more loops

Loops again?  And again and again.  Because looping is all about 
repetition. Every interesting thing a computer can do involves loops.
The basic operations a computer can carry out are _extremely_ simple.
Complex operations are always performed by performing a lot of simple 
operations in some kind of loop.  

## [Parallel Lists](04-02-Parallel-Lists.md)

Before jumping into indefinite loops, we will take a look at a data 
structure called _parallel lists_ or _parallel arrays_.  This is not 
a new data type in Python, but rather a way of organizing data using 
the `list` type you already know.  It is a structure used in this 
week's project. 

## [Indefinite Loops](04-03-Indefinite-Loops.md)

In [Chapter 3](../03-Collections-Loops/03-01-Collections.md) 
we considered loops through collections, especially 
lists.  Most of our loops took the form of doing something with each 
item, one by one, such as counting or summing the items.  We also 
looked at creating a summary (such as a count) for each value found 
in a collection (e.g., a count of the number of students in each 
major).  In this section we'll look at some loops that are not so 
easy to fit into the "for each x do p" form.  

## [Successive Approximation](04-04-Successive-Approximation.md)

Indefinite loops are often used in an algorithmic technique called 
_successive approximation_.  The basic logic of successive 
approximation is 

```
make an initial guess
while it's not good enough: 
      improve it
Voila!  Good enough answer! 
```

Of course the "make a guess", "not good enough",  and "improve it" 
steps 
may require a 
little more refinement. [Our wildfire clustering project](
https://github.com/UO-CS210/wildfire
) instantiates "make an initial guess" as "randomly assign fires to 
clusters" and "improve it" as "reassign based on proximity", and 
"not good enough" as "assignments are still changing, so maybe we 
can do better." 