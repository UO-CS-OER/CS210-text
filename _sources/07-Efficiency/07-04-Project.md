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
# Project

![A physical Boggle board](img/sample-board.jpeg)

The [Boggler project](https://github.com/UO-CS210/06-Boggle)
uses a recursive depth-first search to find words in a
[Boggle](https://en.wikipedia.org/wiki/Boggle) board.  This part of 
the project is similar to our earlier _Flooding the Cave_ project, 
but a little more complex in the information it maintains during the 
search.  In addition, this project introduces _binary search_, which 
it uses to search a word list at each possible move.
