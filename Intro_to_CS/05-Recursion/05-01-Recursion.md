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

# Recursive Functions

We have written many functions that call other functions.  Could we 
write a function that calls itself?  A function that calls itself 
directly or indirectly is called a _recursive_ functon.
We would have to be careful, of 
course.  The following will not work: 

```python3
def mult_v1(a: int, b: int) -> int: 
        """Use commutative law to multiply, a*b = b*a"""
        return mult_v1(b, a)
        
print(mult_v1(5,3))
```

This circular definition of multiplication in terms of 
multiplication fails, as we expect.  It's a kind an _infinite 
recursive loop_.  Python will eventually report a `RecursionError` 
exception: 

```
RecursionError: maximum recursion depth exceeded
```

And yet we can write a recursive function for multiplication. The 
following is a slow way to multiply integers, 
but it works: 

```{code-cell} python3
def mult_v2(a: int, b: int) -> int: 
    """Multiplication by repeated addition.
    a and b must be non-negative integers.
    """
    if a == 0: 
        return 0
    else: 
        return b + mult_v2(a - 1, b)
    
print(mult_v2(3, 5))
```

Why does `mult_v2` work, without causing an infinite 
recursive loop?   The key is that while `mult_v2` 
makes a recursive call on `mult_v2`, the same function, it does not 
call `mult_v2` on the same argument values.  The recursive call is made 
with a smaller value for `a`, until eventually `a` must be 0.  We 
can think of it as transforming `mult_v2(3, 5)` first into
`5 + mult_v2(2, 5)`, then `5 + 5 + mult_v2(1, 5)`, then
`5 + 5 + 5 + mult_v2(1, 5)`, and finally `5 + 5 + 5 + 0`.

You can [visualize this progression in PythonTutor](
https://pythontutor.com/render.html#code=def%20mult%28a%3A%20int,%20b%3A%20int%29%20-%3E%20int%3A%20%0A%20%20%20%20%22%22%22Multiplication%20by%20repeated%20addition.%0A%20%20%20%20a%20and%20b%20must%20be%20non-negative%20integers.%0A%20%20%20%20%22%22%22%0A%20%20%20%20if%20a%20%3D%3D%200%3A%20%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20else%3A%20%0A%20%20%20%20%20%20%20%20return%20b%20%2B%20mult%28a%20-%201,%20b%29%0A%20%20%20%20%0Aprint%28mult%283,%205%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false). 


In `mult_v2`, the code is divided into a _base 
case_ (`a == 0`) and a _recursive case_ (`a > 0`, which we have 
simplified to `else`).  Our recursive functions will always have 
this structure.  The base case is a case that can be handled 
directly, without a recursive call.  The recursive case must make 
the recursive call on data values that are "smaller" in the sense 
that with repeated application the function must eventually reach 
the base case.  When we write recursive functions involving numbers, 
"smaller" is usually our familiar notion of "smaller numbers".  When 
we write other kinds of recursive functions, we may have to think 
harder about what "smaller" could mean, to guarantee that we always 
reach the base case. 

Recursion in computing is closely related to induction in 
mathematics.    Not surprisingly, then, many inductive definitions can 
be straightforwardly translated into recursive functions.  For 
example, the factorial function can be inductively defined as:
$
n! = \left\{ \begin{array}{ll}
            1 & \textrm{if } n < 2\\
            n \times (n-1)! & 
              \textrm{otherwise }
            \end{array}
      \right.
$

Again we see a _base case_ (n < 2) and a recursive (or inductive)
case. Mathematicians might define the base case before or after the
inductive case, but in programming we will almost always check the base 
case first.  We can translate the mathematical definition above to 
Python very simply: 

```{code-cell} python3
def factorial(n: int) -> int: 
    """The inductive definition of factorial"""
    if n < 2: 
        return 1
    return n * factorial(n - 1)
    
factorial(5)
```

While math is full of inductive definitions that can become 
recursive functions, recursion is not limited to 
mathematical or numerical problems.   Often in computing, recursion 
is applied to collections (lists, dicts, etc).  Sometimes the 
recursive call is on a _smaller piece_ of a collection.  Other times 
the data itself is hierarchical, and the recursive calls follow the 
hierarchical structure of the data. 

## Shrinking pieces of a collection 

A palindrome is a word or phrase that is the same written forwards 
or backwards.  For example, "kayak" is a palindrome, as are 
"rotator" and "wow".  We can define palindromes inductively as 
follows: 

- A single letter word is always a palindrome (even if it's a very 
  boring palindrome).
- The empty string is also a palindrome.
- If some sequence of letters _w_ is a palindrome, and _x_ is a 
  letter, then _xwx_ is a palindrome. 

The first two parts of the definition may seem a little strange.  If 
you were asked for examples of palindromes, you probably would not 
answer with "a" or "I".  You almost certainly wouldn't answer with 
the empty string.  But strange as they seem, we need these as 
_base cases_!  (I will return to this below and write a "helper 
function" that can prevent us from accepting these trivial palindromes.)

The third rule, which says that _xwx_ is a palindrome if _x_ is a 
letter and _w_ is a palindrome, is the recursive case.  The 
definition looks like it is adding a letter _x_ to both ends of a 
word, but we will use it backwards:  Given a word _xwy_, we will 
check whether _x_ and _y_ are the same letter, and then make the 
recursive call on a shorter word _w_.   

This will be simpler with a list of letters than with a string.  
Python makes it easy to get such a list of letters: 

```{code-cell} python3
list("hotdog")
```

Now I want to write a recursive function that returns `True` if its
argument is a palindrome, and `False` otherwise.  In the first 
version, I'll use Python list operations to extract the first, last, 
and middle letters.

```{code-cell} python3
def palindrome_v1(word: list[str]) -> bool: 
    """True if word is a palindrome"""
    # Base cases
    if len(word) < 2:
        return True
    # Recursive case
    x = word[0]     # First letter
    w = word[1:-1]  # Middle letters, could be empty
    y = word[-1]    # Last letter
    return x == y and palindrome_v1(w)
    
def is_it_palindrome(word: str) -> bool:
    """Print palindrome judgment for a string"""
    letters = list(word)
    if palindrome_v1(letters):
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is NOT a palindrome")

is_it_palindrome("racecar")
is_it_palindrome("noon")
is_it_palindrome("faff")
is_it_palindrome("a")
```

You can [visualize the execution of `palindrome_v2` with Python Tutor]( 
https://pythontutor.com/render.html#code=from%20typing%20import%20List%20%20%23%20Required%20for%20Python%20v%203.6%0A%0Adef%20palindrome_v1%28word%3A%20List%5Bstr%5D%29%20-%3E%20bool%3A%20%0A%20%20%20%20%22%22%22True%20if%20word%20is%20a%20palindrome%22%22%22%0A%20%20%20%20%23%20Base%20cases%0A%20%20%20%20if%20len%28word%29%20%3C%202%3A%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%23%20Recursive%20case%0A%20%20%20%20x%20%3D%20word%5B0%5D%20%20%20%20%20%23%20First%20letter%0A%20%20%20%20w%20%3D%20word%5B1%3A-1%5D%20%20%23%20Middle%20letters,%20could%20be%20empty%0A%20%20%20%20y%20%3D%20word%5B-1%5D%20%20%20%20%23%20Last%20letter%0A%20%20%20%20return%20x%20%3D%3D%20y%20and%20palindrome_v1%28w%29%0A%20%20%20%20%0Adef%20is_it_palindrome%28word%3A%20str%29%20-%3E%20bool%3A%0A%20%20%20%20%22%22%22Print%20palindrome%20judgment%20for%20a%20string%22%22%22%0A%20%20%20%20letters%20%3D%20list%28word%29%0A%20%20%20%20if%20palindrome_v1%28letters%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22'%7Bword%7D'%20is%20a%20palindrome%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28f%22'%7Bword%7D'%20is%20NOT%20a%20palindrome%22%29%0A%0Ais_it_palindrome%28%22racecar%22%29&cumulative=false&curInstr=34&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
). 

## Logical values

Sometimes the value that becomes "smaller" with each recursive call 
is not the value of an individual variable, but some conceptual 
value that can derived from one or several variables.  I will call 
these "logical values" (as versus "physical values" in an individual 
variable); another term 
you might encounter is "ghost variables".  

Instead of 
decomposing the list of letters in `word` as in `palindrome_v1`, we 
might pass indexes of the first and last letters considered.  Then 
we can pass the same list in a recursive call, but make the _logical_ 
value smaller by passing different indexes of the first and last 
letter under consideration, stopping when they cross (indicating an 
empty word) or meet (indicating a word of one character). 

![Recursive calls passing index of first and last letter in 
"logical" word value](img/racecar-palindrome.png)

Instead of checking whether `len(word) < 2`, we will check whether 
`last - first < 1`. 

```{code-cell} python3
def palindrome_v2(word: list[str], first: int, last: int) -> bool: 
    """True if word[first:last] is a palindrome.
    first and last must be non-negative integers.
    """
    # Base cases
    if last - first < 1:
        return True
    # Recursive case
    x = word[first]
    y = word[last]
    return x == y and palindrome_v2(word, first+1, last-1)
    
def is_it_palindrome(word: str) -> bool:
    """Print palindrome judgment for a string"""
    letters = list(word)
    if palindrome_v2(letters, 0, len(letters)-1):
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is NOT a palindrome")

is_it_palindrome("racecar")
is_it_palindrome("noon")
is_it_palindrome("faff")
is_it_palindrome("a")
```

(final-palindrome)=
## A wrapper function

We noted above that we might not like to consider "a" or "I" 
palindromes, and we might especially not like considering the empty 
string "" a palindrome.  Also `palindrome_v2` takes a list and two 
integers as arguments.  We'd rather have a function that takes a 
string and returns `True` only if that string is a palindrome of at 
least two letters.  A typical way of "fixing up" a function is by 
writing another function to "wrap" it.  

By convention in Python,  a name that begins with an underscore 
character (`"_"`) is "hidden" or "internal" to a module.  For 
palindrome 
checking, we can give the _wrapper_ function a "public" name 
`palindrome`, and use `_palindrome` for its internal partner that 
does the main work.   The wrapper function `palindrome` will just 
check the special cases (rejecting empty and one-letter candidates) 
and call the internal function `_palindrome` with the arguments it 
requires.

```{code-cell} python3
def palindrome(word: str) -> bool: 
    """Is word a palindrome of at least 2 letters?"""
    if len(word) < 2: 
        return False
    letters = list(word)
    return _palindrome(letters, 0, len(letters)-1)
    
    
def _palindrome(word: list[str], first: int, last: int) -> bool: 
    """True if word[first:last] is a palindrome.
    first and last must be non-negative integers.
    """
    # Base cases
    if last - first < 1:
        return True
    # Recursive case
    x = word[first]
    y = word[last]
    return x == y and _palindrome(word, first+1, last-1)
    
    
def is_it_palindrome(word: str) -> bool:
    """Print palindrome judgment for a string"""
    if palindrome(word):
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is NOT a palindrome")


is_it_palindrome("racecar")
is_it_palindrome("noon")
is_it_palindrome("faff")
is_it_palindrome("a")
```

Note that the wrapper function rejected "a". 

[Our project for this week](
https://github.com/UO-CS210/flood-fill
) makes recursive calls to fill cells in a grid.  The grid is always 
the same size in the recursive calls, but the "logical value" that 
gets smaller is the number of cells that can be filled.  This 
logical value must be smaller with each level of recursive call, and 
when it is zero the base case must apply, ending the recursion. 

We will see other projects in which recursive calls are made with 
the same collection (usually a list) but with smaller and smaller 
logical portions of that collection. 

## Recursion for hierarchical data structures

We have seen that lists can be nested within lists.  So far we have 
used lists within lists mainly to represent grids or matrices.
We might also encounter more 
irregular nested structures.  We might not know in advance how 
deeply the lists will be nested or how long they will be.  

How could we sum the integers in a nest of lists like this?

```python
[[1, 2, [3, 4], 5, [6, 7], 8], 9]
```

Python provides an `isinstance` function that we can use to 
determine whether a value is a `list`, an `int`, or something else: 

```{code-cell} python3
def what_is_that(v):
    """Print a description of v"""
    if isinstance(v, list): 
        print(f"{v} is a list!")
    elif isinstance(v, int):
        print(f"{v} is an integer!")
    else:  
        print(f"{v} is neither a list nor an integer")
        
what_is_that([[1, 2, [3, 4], 5, [6, 7], 8], 9])
what_is_that(4)
```

We can use `isinstance` to distinguish between the base case and 
recursive case in a function to sum the integers in nested lists 
like the example above. 

```{code-cell} python3
def sum_atoms(m: object) -> int: 
    """Sum the integer elements of nested lists"""
    if isinstance(m, int):
        return m
    if isinstance(m, list):
        sum = 0
        for el in m: 
            sum += sum_atoms(el)
        return sum
    # Neither an int nor a list?  Ignore it. 
    return 0
    
s = sum_atoms([1, [2, 3], 4])
print(s)
t = sum_atoms([[1, 2, [3, 4], 5, [6, 7], 8], 9])
print(t)
```

Hierarchical data structures are very common:  For example, the 
Document Object Model (DOM) tree representation of a web
page.  A web server transmits HTML web content to a browser as text 
with  "tags" like `<p>` and `<div>` describing its hieararchical 
structure. The browser 
transforms that text into a DOM tree that manifests the
hierarchical structure (e.g., a paragraph (`<p>`) in the text might be 
nested within a division (`<div>`), which might be nested within 
another division.  If interaction is controlled by JavaScript 
functions, those functions act on the DOM tree, not the text.
We will see many more examples of recursion with hierarchical data 
structures in later courses, when we have more techniques for 
building those data structures. 
