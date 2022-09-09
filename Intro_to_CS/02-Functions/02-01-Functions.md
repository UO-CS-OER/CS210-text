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

# Designing and building functions in Python

As we discussed in the
[prior chapter](../01-Intro/01-03-Kickstart.md),
_controlling complexity_ is the main challenge in programming,
and _functions_ are one of the primary ways
we can decompose complex programs into
_brain-size chunks_.  

In this chapter we will take a deeper dive into functions in Python: 
How they work, how to write and test them, and how to design them.
The last part, learning to design _good_ functions that are useful, 
readable, testable, and maintainable, is most challenging.  We will 
not master it in a week or in ten weeks, not even in ten years.
Like learning to play a musical instrument or cooking or playing a 
sport, one can spend a lifetime improving, expanding, and refining 
technique.  Our shorter term objective is to establish a basic level 
of competence to begin. 

We begin with a brief look at the _mechanics_ of functions.  This 
includes the syntax for writing a function header, and a few basic 
rules that they should conform to.  Most importantly, you must 
understand how _formal arguments_ and other variables that are 
_local_ to a function relate to variables outside the function. This 
is called _scope_. 

* [Scope in Python](02-02-Scope.md)

With those mechanics in hand, we can make our first (and certainly 
not our last) foray into function design.  We will look at some 
basic guidelines that (almost) all functions should follow.  We will 
also look at testing functions, and writing documentation that is 
useful for users and maintainers of functions.  We might refer to 
these as guidelines for _function hygiene_. 

* [Function Hygiene in Python](02-03-Hygiene.md)

Basic hygiene helps us avoid some harmful practices.  We would 
like to go farther and learn to design really well-chosen, useful, even 
elegant functions.  How do we choose functions?  Of all the ways we 
could decompose a complex problem into smaller, simpler sub-problems,
what makes some better than others?  Our first steps toward grasping 
these deeper issues are best taken in the context of a project.  

* [Project: Estimating Pi](https://github.com/UO-CS210/pi)

The project illustrates Monte Carlo simulation, an important 
computational technique that is applied in fields from games to 
biology, ecology, and economics.  The project documentation also
walks you through the thought process of decomposing a project into
smaller parts and choosing an order in which to build and test
those parts.  Decomposing problems and composing solutions is a core 
_computational thinking_ skill that you will use and refine as long 
as you are solving problems with computational techniques.  It can 
also be useful to you in other problem-solving domains.
