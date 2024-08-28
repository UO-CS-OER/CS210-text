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
# Exercises

These exercises are taken from old exams.  Check your 
understanding by working them
individually before peeking forward to answers or discussing
them with classmates. 

1. What does this program print? 

```python
def f(x: int) -> int:
    x = x + 1
    return x

x = 5
y = 7
z = f(y)
print(f"x={x}, y={y}, z={z}")
```

2. What will go wrong with this program? How should you fix it? 

```python
def sign(n: int):
    """Return -1, 0, or 1 depending on n being negative, zero, or 
    positive
    """
    if n > 0: 
        result = 1
    elif n < 0:
        result = -1
    else: 
        result = 0

sign(-12)
print(result)
```

3.  What is wrong with this function? 

```python
def double(x: int) -> int: 
    """Returns double the original value of x."""
    z = x + x
    print(z)
```


## Answers to exercises

1. What does this program print? 

```python
def f(x: int) -> int:
    x = x + 1
    return x

x = 5
y = 7
z = f(y)
print(f"x={x}, y={y}, z={z}")
```

Answer:  `x=5, y=7, z=8`

 This is a question about variable scope and argument passing.  The
    `x` in an activation of function `f` is distinct from
    the globabl `x`.  The _actual argument_ `y` is
    copied to the _formal argument_ `x` when `f` is
    called, so incrementing `x` in `f` affects neither the
    global n`x` nor the global `y`.

 Don't be confused by f-strings like `f"x={x}, y={y}, z={z}"`.
This `f` is not the same as the function `f`.  
 f-strings are used in Python to format output by _interpolating_ 
 values into template strings.  For example, within the f-string, `
 {x}` is replaced by the value of variable `x`. 
 
2. What will go wrong with this program? How should you fix it? 

```python
def sign(n: int):
    """Return -1, 0, or 1 depending on n being negative, zero, or 
    positive
    """
    if n > 0: 
        result = 1
    elif n < 0:
        result = -1
    else: 
        result = 0

sign(-12)
print(result)
```

Function `sign` is not returning the `result` variable.  The 
`result` variable exists only while the function is executing. When 
we try to print `result` from outside the `sign` function, we will 
encounter an error: 

```
    print(result)
          ^^^^^^
NameError: name 'result' is not defined
```

We can fix it this way: 

```{code-cell} python3
def sign(n: int) -> int:
    """Return -1, 0, or 1 depending on n being negative, zero, or 
    positive
    """
    if n > 0: 
        result = 1
    elif n < 0:
        result = -1
    else: 
        result = 0
    return result

s = sign(-12)
print(s)
```

Since the function stops running as soon as it returns a value, we 
could also shorten it up like this: 

```{code-cell} python3
def sign(n: int) -> int:
    """Return -1, 0, or 1 depending on n being negative, zero, or 
    positive
    """
    if n > 0: 
        return 1
    elif n < 0:
        return -1
    return 0

s = sign(-12)
print(s)
```

3.  What is wrong with this function? 

```python
def double(x: int) -> int: 
    """Returns double the original value of x."""
    z = x + x
    print(z)
```

The signature of this function (given in its header,
`def double(x: int) -> int:` and its docstring is a kind of contract 
with code that uses it.  The header says it has a
_result_, which is an 
integer, and the docstring says that result will be twice the 
original value of x.  That's a lie.  It does not have a _result_.
It has an _effect_, which is printing double the value x.  It should 
return the value instead, like this: 

```python
def double(x: int) -> int: 
    """Returns double the original value of x."""
    z = x + x
    return z
```