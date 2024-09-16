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

The [enrollment analysis project](
https://github.com/UO-CS210/enrollmentLinks)
asks you to loop over a collection of elements representing
individual student enrollments in a class, selecting and separating
values to produce a summary of enrollments by major.

The primary objective of the enrollment analysis project is to
practice a fundamental loop
idiom, the _accumulator pattern_, together with some ways of
representing tabular data. You will use both lists and dictionaries
as representations of tabular data. You will use dictionaries (type
`dict`) in a version of the accumulator pattern, to keep counts of
elements in a list. You will also use a dictionary to expand abbreviated
codes from a list of student majors.

