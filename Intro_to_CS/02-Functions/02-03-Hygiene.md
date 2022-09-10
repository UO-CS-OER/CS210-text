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

# Function Hygiene in Python

## Function headers and docstrings

Consider again the `abs_diff` function defined in the prior chapter.

```{code-cell} python3
def abs_diff(x: int, y: int) -> int:
    """Absolute value of the difference between x and y."""
    if x > y: 
        return x - y
    else: 
        return y - x
```

The name of the new function will be `abs_diff`.  Following
[Python naming conventions](https://peps.python.org/pep-0008/), it 
is made of lower case letters (no capital letters), with parts 
separated by underscore ("`_`").  
The triple-quoted string immediately following the function header 
is the _docstring comment_.  

## Names matter

We have chosen 
`abs_diff` rather than `absolute_difference` to keep it short. 
We have not shortened it further to `a_d`, nor chosen an arbitrary 
name like `theta`, because it is important for the name to be 
mnemonic and suggestive of its purpose. 

How long is long enough?  How descriptive must a name be?
Kernighan and Plauger provide nuanced and pragmatic guidance to 
naming in their classic book 
[_The Elements of Program Style_](
https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style).
Although the original version of that book uses examples from older 
programming languages that you may never encounter, the essential 
principles remain valid.  One of these is that distinctiveness 
(avoiding names that can be confused with each other) is paramount.
For example, `hours_weekday_worked` and `hours_weekend_worked` are a 
bad pair, because they are distinguished only by middle words 
that look similar.  `weekend_hours` and 
`weekday_hours`, or even `wkend_hours` and `wkday_hours`, are 
easier to distinguish because their differences are more 
prominent. 

A second principle, which 
like distinctiveness is rooted in properties of human memory, is 
that a name which is defined in one place and then referenced far 
away needs to be more descriptive than a name 
that is defined and
then used just once nearby (e.g., within the span of code that is 
likely to be visible on the same screen of text).

## Arguments

Function `abs_diff` has two _arguments_, also called _formal 
parameters_, `x` and `y`, and returns a single 
`int` value.  This information comprises the _signature_ of
function `abs_diff`, which is _(int, int) -> int_.  This is enough 
to tell us that `x = abs_diff(5, 7)` is a legal assignment that
assigns an `int` value to `x`, but `abs_diff("cats", "dogs")` is
an error, as is `abs_diff(3, 2) + "turtles"`.

Less obviously, `abs_diff(3.2, 5.4)` is a programming error, even 
though it will return 2.2.  This is because the header of a function
together with its docstring
is a contract between the author of the function and anyone 
who calls that function (even if they are the same person).  Passing 
a floating point number like 3.2 to `abs_diff` breaks that contract.

Why do we care about this "contract", if the code works?
Because the contract determines what the author of 
the function is permitted to change without notice.  Calling a 
function in a way that violates the contract might work today, but 
fail sometime later when the author of the function makes a 
perfectly acceptable change to the body of the function.  The user 
of a function must only rely on the contract as given in the 
function header and docstring.  This applies even if the author and 
the user are the same programmer!  It is all too easy to make a 
small and seemingly harmless change to one part of a program and 
accidentally break a completely different part because of some 
forgotten dependency.

## Information hiding

We treat the body of the function as 
if it were invisible to the programmer who writes calls to that 
function, and subject to change without notice, even if it is the same 
programmer.  This is called _information hiding_. 
Students and beginning programmers often find _information hiding_ 
unintuitive and bothersome.  Understandably so, because as a 
beginner they write most code individually, and seldom work on the 
same project for more than a few weeks.  This is apt to change as 
you tackle larger and more complex projects.

The software systems 
that matter to people are typically collaborative or change hands 
over time, and they last much longer than you might imagine.  Even 
the original developer of a function will find themselves 
essentially an outsider when they return to it after a few months 
working on other parts of an application. 

There is another reason for clear, simple contracts and information 
hiding.  Programs are written by humans.  Human brains are amazing, 
but one thing they do not do well is maintain a large number of 
details in working memory.  

We solve complex problems by decomposing 
them into smaller problems, then composing simple solutions of 
sub-problems to solve the overall problem.  This is _only_ possible 
if we can ignore and abstract away details of some of the 
sub-problems while working on other parts.   If we need to 
understand _how_ a function works to understand _what_ it does,
we can't suppress that detail in any part of the program that uses 
the function.  Information hiding is an essential tool for 
controlling complexity by giving us permission to ignore most 
details most of the time, focusing in on just a few at a time. 

## Docstrings 

As useful as the _signature_ of a function is in telling us what 
kind of values we can pass to it and what kind of value we can 
expect back from it, the signature alone cannot tell us everything 
we need to know.  The name can help, but it's not enough:  We can 
guess that `abs_diff` probably does not give us the sum or the 
product of its arguments, but the docstring comment immediately 
following the function header gives us a more complete description.

The Python interpreter makes the 
docstring comment available through its built-in help system: 

```{code-cell} python3
help(abs_diff)
```

As with choosing names, writing docstring comments that are clear 
but concise is an art that requires care and practice.

## Argument names 

What about those formal argument names, `x` and `y`?  Should they be 
longer?  Would it help?  If there were particular meanings 
associated with them (e.g., if the first argument should be a height 
in centimeters and second should be an angle in degrees), then `x` 
and `y` would be poor names.   Consider the following function,
in which longer names are needed: 

```python3
def relative_error(est: float, expected: float) -> float:
    """Relative error of estimate (est) as non-negative fraction 
    of expected value.
    """"
```
Here the formal parameters are `est` (for estimate) and `expected` 
(for expected value, i.e., for the value that `est` should be close 
to).   These have been chosen to be _mnemonic_.  You can probably 
guess that `est` means "estimate" even without context.  Without 
context it is less likely that you would guess that `expected` means 
"the value we expected to get", but in the context of a function 
called `relative_error` it is clear. 


These formal parameters are not interchangeable;
`relative_error(3.5, 3.8)` will 
not give the same result as `relative_error(3.8, 3.5)`.  If we give 
them meaningless names like `x` and `y`, we are likely to reverse 
them and get the wrong answers.  Ambiguous names would be dangerous 
in that case!   In the case of `abs_diff`, on the other hand, `x` 
and `y` are just numbers, nothing more, which is what their generic 
names communicate. 

Names that are distinguished only by suffixes, like `v1`, `v2`, `v3`,
etc., are never acceptable, because they are too easy to confuse. 
Arbitrary names like your favorite colors or your pets are also not 
acceptable, even for generic values for which `x` and `y` would be 
acceptable, because they falsely _appear_ to have some meaning. 

## Results, effects, and side effects

A function should normally _either_ return a well-documented result 
_or_ have some well-documented effect on the arguments it is passed, 
but not both. For example, here is a function that returns a list 
containing just the positive elements from a list of integers: 

```{code-cell} python3
def select_pos(m: list[int]) -> list[int]:
    """Returns a list of the positive elements from m."""
    result = []
    for el in m: 
        if el > 0:
            result.append(el)
    return result
    
li = [1, 0, 2, 0, 3, 0]
li_selection = select_pos(li)
print(f"li after selection is {li}")
print(f"selection is {li_selection}")
```

`select_pos` is ok ... it returns a well-documented result and it 
does not have effects on anything outside its local scope.
We could also write a function that appends the positive elements of 
one list to another: 

```{code-cell} python3
def append_pos(src: list[int], dest: list[int]):
    """Positive elements of src are appended to dest."""
    for el in src: 
        if el > 0:
            dest.append(el)
    
li = [1, 0, 2, 0, 3, 0]
li_selection = []
append_pos(li, li_selection)
print(f"li after selection is {li}")
print(f"li_selection is {li_selection}")
```

`append_pos` is also ok ... it has a well-documented effect, and it 
does not return a result.  (Technically it returns a special value 
called `None`.)

We generally avoid creating functions or methods that both
return a result _and_ have a result. It is easier to understand just 
one or the other. For example, the built-in 
function `sorted` returns a sorted list without changing the list it 
is given, while the list method `sort` puts the list into sorted 
order but does not return a result.
In the rare cases that doing both makes a program 
significantly shorter, clearer, or faster, we must document that 
combination particularly well. A rare example of a built-in method 
that has both an effect and a result is the `list` method `pop`, 
which both removes an item from the list and returns it. 

## Side effects

When a function or method affects something _other than_ its 
arguments or the object on which a method is called, it is called a 
_side effect_.  Side effects make it easy to create program bugs and 
hard to find and correct them. One case where side effects may be 
justifiable is in output, e.g., printing something, logging 
something to a file, or presenting a graphic.  The more _obvious_ 
and _well-documented_ such a side effect is, the less chance it will 
lead to a frustrating debugging session as unexpected effects seem 
to come from nowhere.

## Summary of function hygiene guidelines

- Make the function header and docstring a _contract_ between the 
  author and user of the function.  The user should not depend on 
  details of the body of the function, or even have to read the body 
  of the function to know how to use it correctly.
- Use names that are sufficiently clear and distinct.  They don't 
  have to be long, but they must be understandable in the context in 
  which they will be used.  
- Generic names like `x` are ok only for 
  generic purposes like "some number", never for something specific 
  like "the number of sides of the polygon."  The names of your pets 
  or siblings are only acceptable if the program computing something 
  about your pets or siblings. 
- A function (or method) should _either_ return a result _or_ have 
  an effect.  Very seldom should a function or method have both an 
  effect and a result, and those rare cases must be carefully 
  documented. 
- Side effects are particularly dangerous.  Avoid them when 
  practical, and particularly avoid side effects that could go 
  unnoticed, unless you love long and confusing debugging sessions. 
- You may be tempted to ignore these guidelines because you will be 
  the only user of the functions you write.  The you of next week 
  will be angry at the you of this week if you do.  
