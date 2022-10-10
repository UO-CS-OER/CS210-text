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
collections including lists, tuples, and dictionaries. 
We will introduce some additional 
operations, and especially we will examine ways of looping through 
collections. 

## Collection basics

A _collection type_ (or _collection class_) is a kind of data that 
can contain other data as elements.  For example, `["alpha", "beta", 
"gamma"]` is a list of strings (`str`), while `[1, 2, 3]` is a list of 
integers (`int`).  

In general a collection type will have:
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

We can determine how many elements are in `m` with `len(m)`.  Note 
that even if a list contains other lists, `len` counts each element 
just once (not elements of the sublists). 

```{code-cell} python3
m = ["a", "b", "c", "d", "e"]
print(len(m))
r = [["a", "b", "c"], ["d", "e", "f"]]
print(len(r))
```

There are two main ways to iterate (loop) through the values of a 
list.  The simplest is the way we will use most often:  We can ask a 
`for` loop to iterate through the elements of the list, like this: 

```{code-cell} python3
m = ["one", "two", "three"]
for s in m: 
    print(s)
    # or do anything else with s in the body of the loop
```

Later we will use other approaches, usually because we need to know 
the position (index) of each element in addition to its value.  In 
that case we might write something like 

```{code-cell} python3
for s_i in range(len(m)):
    s = m[s_i]
    print(s_i, s)
```

In the code snippet above, we have used an arbitrary variable name 
`s` for elements of `m`.  In an application, we would try to use a 
more meaningful name.  We are also free to choose the name of the 
index variable.  Python does not require that they be related at all.
I have chosen `s_i` to suggest that it is the _index for `s`_.  You 
are not required to use such a convention, but in general it is a 
good idea to help a reader of your code see the meanings and 
relationships among your variables.

What if we have _nested lists_, i.e., lists within lists?  They 
often call for _nested loops_, loops within loops.  Suppose for 
example we have `m = [["a", "b"], ["c", "d"]]`.  We often think of 
such nested lists as a grid or matrix in which each sublist is a row:

|     |     | 
|-----|-----|
| "a" | "b" |
| "c" | "d" |

If we wanted to 
print all the strings in the sub-lists of `m`, we might write 
something like 

```{code-cell} python3
m = [["a", "b"], ["c", "d"]]
for row in m:
    for s in row:
        print(s)
```

This order of access is called _row-major order_. 
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

The term "tuple" comes from generalizing doubles (pairs), 
triples, quadruples, quintuples, etc., i.e., sequences of some fixed 
size.  Tuples are very similar to lists, but they
are _immutable_.  We can 
create new tuples based on the contents of other tuples, but we 
cannot change the value or length of a tuple.

To write a literal tuple value, we separate them by commas, usually 
in parentheses: 

`("a", "b", "c")`.  

We _cannot_ add elements to the end of a tuple, or anywhere else.  
They are _immutable_.  

While the elements of a tuple have _indexes_ like the elements of a 
list, and can be accessed in the same manner, we more typically access 
tuple elements by _destructuring_: 

```{code-cell} python3
character = ("Wesley", "Dread pirate Roberts", "As you wish")
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

## Dictionaries

While lists and tuples represent sequences, dictionaries (type `dict`)
represent _associations_ between a set of _keys_ and a set of 
_values_.   We can think of them as "lookup tables".  For example, 
we might have a `dict` that associates postal abbreviations with the 
names of U.S. states: 

| | |
| ----- | --------- |
| WA | Washington |
| OR | Oregon |
| CA | California |
| AK | Alaska |

We can write a `dict` literal using curly braces and associating 
each key to a value with `:`.  We can then "look up" an association 
by treating the key as an index. 

```{code-cell} python3
state_abbrevs = {
    "WA": "Washington",
    "OR": "Oregon", 
    "CA": "California", 
    "AK": "Arkansas"
    }
    
or_state = state_abbrevs["OR"]
print(or_state)
```

We can add a new (key, value) pair to a `dict` using the key as an 
index. 

```{code-cell} python3
state_abbrevs["NV"] = "Nevada"
```

The keys in a `dict` are unique.  If we associate a new value with 
key, the old (key, value) association is replaced. 

```{code-cell} python3
state_abbrevs["AK"] = "Alaska"
print(state_abbrevs)
print(state_abbrevs["AK"])
```

The values in a `dict` can be any data type, but the keys must be 
_hashable_, which in practice means that you should use _immutable_ 
values as dictionary keys.  While we most often use strings as 
dictionary keys, integers and tuples are also acceptable.  Lists 
cannot be dictionary keys. 

```{code-cell} python3
good_dict = { (1, "Alpha"): "A", (2, "Beta"): "B" }
print(good_dict[(2, "Beta")])
```
```{code-cell} python3
:tags: ["raises-exception"] 

bad_dict = { [1, "Alpha"]: "A", [2, "Beta"]: "B" }
print(bad_dict[[2, "Beta"]])
```

The `in` operation tests whether a `dict` contains a key: 

```{code-cell} python3
if "TX" in state_abbrevs:
    print(state_abbrevs["TX"])
else: 
    print("TX expansion not found")
```

We cannot directly iterate a `dict`, but we can obtain a list of key 
values with the `keys` method or a list of (key, value) pairs 
(tuples) with the `items` method of type `dict`. 

```{code-cell} python3
for abbrev in state_abbrevs.keys():
    print(abbrev)
```

Since the elements in the list returned by the `items` method are 
tuples, it is common to _destructure_ them into separate variables 
for each key and value: 

```{code-cell} python3
for kv_pair in state_abbrevs.items(): 
    abbrev, name = kv_pair
    print(abbrev, name)
```

The destructuring can be done right in the `for` statement, like this: 

```{code-cell} python3
for abbrev, name in state_abbrevs.items():
    print(abbrev, name)
```

## Loops

### Counting

A very common programming task is to count elements in a collection. 
If we just need to know the size of the collection, in Python we can 
use the `len` method, e.g., 

```{code-cell} python3
print(len(state_abbrevs))
```

Often we want to count only elements that satisfy some 
condition.  For example, suppose for some reason we wanted to 
determine how many elements of a list of strings are state 
abbreviations: 

```{code-cell} python3
abbrevs = ["CO", "OR", "WA", "MD"]
states_count = 0
for ab in abbrevs:
    if ab in state_abbrevs:
        states_count = states_count + 1
print(states_count) 
```

Note the pattern:  We initialize the count _before_ the loop, 
add to it _within_ the loop, and do something with the result 
_after_ the whole loop is complete.  

### Counting multiple values

The counting pattern we have considered so far keeps a count of one 
thing in a variable.  What if we wanted to keep a count of several 
different values?   For example, what if we wanted to know that
`['dog', 'dog', 'cat', 'dog', 'cat']` is three dogs and two cats? 
We might not even know that the list will contain only dogs and cats 
... someone might have snuck in a squirrel or a marmoset or some 
other random animal.  Since we don't know what values we will 
encounter, we can't create a count variable for each one.  What we 
can do, however, is use a `dict` to keep a collection of count 
variables.

```{code-cell} python3
animals = ['dog', 'dog', 'cat', 'orca', 'dog', 'cat']
counts = { }
for animal in animals: 
    if animal in counts:
        counts[animal] += 1
    else:
        # First time we've encountered this one! 
        counts[animal] = 1
print(counts)
```

### Summing 

To count items, we always add 1 to the count for each item that 
satisfies the condition (e.g., items that appear as keys in 
`state_abbrevs`).    Summing values is almost the same, except 
instead of adding 1 for each item, we add the relevant value. 

```{code-cell} python3
populations = {
    "Portland":   641_162,
    "Salem":      177_723,
    "Eugene":	  175_096,
    "Gresham":	  113_103,
    "Hillsboro":  106_633,
    "Bend":       102_059,
    "Beaverton":   98_216,
    "Medford":	   86_367,
    "Springfield": 62_256,
    "Corvallis":   59_864,
    "Albany":	   56_828,
    "Tigard":	   55_767,
    "Aloha":	   53_724
}
itinerary = ["Eugene", "Corvallis", "Albany", "Salem", "Hillsboro"]

pop_sum = 0
for town in itinerary:
    pop_sum += populations[town]
print(pop_sum)
```

For either counting or summing, it is idiomatic to use the `+=` 
operation to clearly communicate that the purpose of the 
incrementing statement.

### Scanning

Another common task is to determine whether _some_ or _all_ elements 
of a collection satisfy some condition. For example, if we wanted 
to determine whether all the towns on an itinerary were included in 
a table, we might write: 

```{code-cell} python3
all_present = True
for town in itinerary: 
    if town not in populations: 
        all_present = False
        break
print(all_present)
```

The code above illustrates the general pattern to determine a _for 
all_ property: 

- Initially we assume the condition is true
- If any element does _not_ satisfy the condition, we conclude the 
  property is false.  We do not need to look further (so we can 
  `break` from the loop).
- The final answer is known _after_ the loop body.

If we write a _for all_ scan as a function, the logic is similar, 
but we don't need an explicit `bool` variable: 

```{code-cell} python3
def all_in_table(li: list, table: dict) -> bool: 
    """True if all elements of li are keys in table"""
    for elem in li:
        if elem not in table: 
            return False
    return True
    
print(all_in_table(itinerary, populations))
```

In this version of the _for all_ scan, an early `return` takes the 
place of the `break` from the loop, and the final `return True` 
takes the place of initializing a `bool` variable to `True`. 

We can also scan to determine whether _any_ elements in a 
collection satisfy a condition.  In terms of mathematical logic,
we would call this a _there exists_ scan. 
Suppose we want to know whether at 
least one 
of the towns on our itinerary are among the most populous cities in 
Oregon, which are listed in our population table. 

```{code-cell} python3
reach_big_city = False
for town in itinerary: 
    if town in populations: 
        reach_big_city = True
        break
print(reach_big_city)
```

In a _there exists_ scan, we can break from the loop as soon as we 
find any element that satisfies the criterion, but we must finish 
the whole loop to conclude that there are no satisfying elements. 

Like the _for all_ scan, a _there exists_ scan may be implemented as 
a function: 

```{code-cell} python3
def exists_in_table(li: list, table: dict) -> bool: 
    """True if any elements of li are keys in table"""
    for elem in li:
        if elem in table: 
            return True
    return False
   
print(exists_in_table(itinerary, populations))
```

Once again, initialization of the boolean variable and the break 
from the loop are replaced with `return` statements in appropriate 
places. 

## Other iterables

We have already seen at least one other type of Python data type 
with behavior similar to lists:  After opening a file, we can 
iterate (loop) through it line by line.  You can also loop through 
the characters in a string: 

```{code-cell} python3
s = "What?"
for ch in s:
    print(ch)
```

There are more.  In Python, "things you can loop through" are called 
_iterables_.  When we loop through indexes for a list `l` using
`range(len(l))`, we are actually iterating through elements of a `range` 
object: 

```{code-cell} python3
for e in range(3):
    print(e)
```

It is even possible to create new kinds of collection 
that you can loop through, but we won't do that in this course. 

## Project

The [project for this week](https://github.com/UO-CS210/enrollment) 
asks you to produce a summary report from a class roster. It uses 
lists, dictionaries, and tuples.  The pattern above, using a `dict` to 
keep several counts of items in a list, is the key to counting the 
number of students in each major. 





