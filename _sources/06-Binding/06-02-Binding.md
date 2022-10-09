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
#  Binding and aliasing

In an earlier chapter we briefly touched the notion of _binding_ a 
variable name to a value.  A _namespace_ in Python is an association 
of names with references to objects.  The _values_ of variables are 
actually in the objects.  When we assign a value to a variable, e.g.,
`x = 5`, we are actually creating an association between the name 
`x` and an object that contains the value `5`. 

![x is bound to an object containing value 5](
img/binding-aliasing-x.png)

When we assign the value of `x` to variable `y` by writing `y = x`, we 
make a copy of 
the reference, not a new copy of the object containing the value. 

![y is bound to the same value object](
img/binding-aliasing-xy.png)

If we bind a new value to `x`, for example by writing `x = x + 1`, it 
will be bound to a reference to 
an object containing that new value. 

![x gets a new value, y is still 5](
img/binding-aliasing-xincr.png)

## Aliasing mutable values

When `x` and `y` referred to the same object containing `5`, we say 
they were _aliased_.  Does aliasing matter?   For `int` values, it 
almost never matters.  When we 
assigned a new value to `x`, we did not change the value in the 
`int` object.  We created a new `int` object to contain the new 
value. We say that type `int` is _immutable_, because we never 
change (mutate) the values in objects.   For immutable types, it 
almost doesn't matter that variables are bound to references that 
could be aliases. 

Aliasing becomes important when we consider _mutable_ types.  For 
example, type `list` is mutable:  We can actually change the value 
in a `list` object.   Consider: 

```{code-cell} python3
m = [1, 3, 5]
```
Now `m` contains a reference to a list containing `int` objects, 
which contain values 1, 3, and 5. 

![m refers to list, which refer to int objects](
img/binding-aliasing-m-before.png
)

Now suppose we change the value of `m[1]`, the second element in the 
list.  

```{code-cell} python3
m[1] = 7
```

This will actually modify the `list` object, without changing 
the binding of `m` to that list object. 

![assignment to m[1] modifies the list](
img/binding-aliasing-m-after.png
)

Consider what happens if another variable `k` refers to the same 
list, becoming an _alias_ of `m`: 

```{code-cell} python3
m = [1, 3, 5]
k = m
```

![assignment to k creates an alias](
img/binding-aliasing-km-aliased.png
)

Now if we modify of an element of `m`... 

```{code-cell} python3
m[1] = 7
print(k)
```

... we have also modified the value of any _alias_ of `m`.

Sometimes this is just what we want. If we mutate an aliased 
variable accidentally, though, it can lead to confusing bugs. 

## Aliasing for functions that mutate values

Sometimes we use aliasing to write functions that modify the values 
passed to them.  

