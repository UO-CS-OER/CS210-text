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

# Collections and Loops

We have already introduced lists and basic loops, including loops 
that read each line in a file.  In this chapter we will revisit 
those basics and dig a little deeper.  We will look at 
collections including tuples and 
dictionaries in addition to lists, introduce some additional 
operations, and especially we will examine ways of looping through 
collections. 

## Collection basics

A _collection type_ (or _collection class_) is a kind of data that 
can contain other data as elements.  For example, `["alpha", "beta", 
"gamma"]` is a list of strings (`str`), while `[1, 2, 3]` is a list of 
integers (`int`).  

In general a collection type will have
- A syntax for _literals_, i.e., a way to write down a value and 
  indicate that we intend a collection of a certain kind.  For 
  example, if we write `[1, 2, 3]`, Python will interpret it as a 
  list of integers, while if we write `(1, 2, 3)` Python will 
  interpret it as a tuple of integers.
- Operations for building or extending values.  For example, if we 
  have a list `m = [1, 2, 3]`, then `m.append(17)` will make the new 
  value of `m` be `[1, 2, 3, 17]`. 
- Operations for accessing individual elements.  For example, we can
  _index_ a list.  If `m` is `[1, 2, 3, 17]`, then `m[0]` is 1 and
  `m[2]` is 3.  
- A way of _iterating_ (looping) through the elements of the 
  collection. 

For a complete list and detailed description of these features for 
all the standard collection types in Python, refer to the
[Python library documentation](https://docs.python.org/3/library/stdtypes.html).
In this chapter we will cover just some basics. 

## Lists

A list (type `list`) holds a sequence of elements.  The elements can 
be any other kind of value, including integers and strings but also 
other collections including lists.

To write a literal list value, we use square brackets, e.g.,
`["a", "b", "c"]`.  

We can add an element to the end of a list with the `append` method. 
Here's another way to create the value `["a", "b", "c"]`:

```{code-cell} python3
m = []
m.append("a")
m.append("b")
m.append("c")
m
```

The elements of a list have _indexes_, or positions, starting with 
zero.  

```{code-cell} python3
m = ["a", "b", "c"]
print(m[0])
print(m[2])
```

Suppose instead we have `m = [["a", "b"], ["c", "d"]]`.  Now `m` is 
a list of lists of strings.  Now `m[1]` is `["c", "d"]`.  If we 
wanted to access the first element of the second sublist, we can 
write `m[1][0]` to first index `m` to get `["c", "d"]` and then 
index `["c", "d"]` to get `"c"`.  

```{code-cell} python3
m = [["a", "b"], ["c", "d"]]
print(m[1][0])
```

We can determine how many elements are in `m` with `len(m)`.  

There are two main ways to iterate (loop) through the values of a 
list.  The simplest is the way we will use most often:  We can ask a 
`for` loop to iterate through the elements of the list, like this: 

```{code-cell} python3
m = ["one", "two", "three"]
for s in m: 
    print(s) # or do something else with s
```

Later we will use other approaches, usually because we need to know 
the position (index) of each element in addition to its value.  In 
that case we might write something like 

```{code-cell} python3
for s_i in range(len(m)):
    s = m[s_i]
    print(s_i, s)
```

What if we have _nested lists_, i.e., lists within lists?  They 
often call for _nested loops_, loops within loops.  Suppose for 
example we have `m = [["a", "b"], ["c", "d"]]`.  If we wanted to 
print all the strings in the sub-lists of `m`, we might write 
something like 

```{code-cell} python3
m = [["a", "b"], ["c", "d"]]
for row in m:
    for s in row:
        print(s)
```

This order of access is called _row-major order_, based on thinking 
of `m` as a grid or matrix:

|     |     | 
|-----|-----|
| "a" | "b" |
| "c" | "d" |

 We might wonder whether we 
can iterate through `m` in _column-major order_, i.e., down the 
 first column and then down the second column.  We can, but 
it's a little more complex: 

```{code-cell} python3
for col_index in range(len(m[0])):
    for row_index in range(len(m)):
        print(row_index, col_index, m[row_index][col_index])
```

Of course, this approach to looping in column major order works only 
if the matrix is _rectangular_, i.e., if every row (sub-list) has 
the same length.  It will also not work for a matrix with zero rows. 

## Tuples

Tuples are sequences of elements, very similar to lists, but they
are _immutable_. We can 
compute new tuples based on the contents of other tuples, but we 
cannot change the value of a tuple.

To write a literal list value, we separate them by commas, usually 
in parentheses: 

`("a", "b", "c")`.  

We _cannot_ add elements to the end of a tuple, or anywhere else.  
They are _immutable_.  

While the elements of a tuple have _indexes_ like the elements of a 
list, and can be accessed in the same manner, we more typically access 
tuple elements by _destructuring_: 

```{code-cell} python3
character = ("Bradley", "Dread pirate Roberts", "As you wish")
name, alias, phrase = character
print(name)
print(alias)
print(phrase)
```

In principle we could loop through tuples in all the ways we loop 
through lists.  In practice that is rare.  Because tuples can never 
change after they have been created, destructuring is usually more 
appropriate, even for nested tuples: 

```{code-cell} python3
pdx = ("Portland International", (45.589,-122.596))
name, (lat, lon) = pdx
print(name)
print(lat)
print(lon)
```





