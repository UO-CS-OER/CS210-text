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

1.  Predict the output of this program without executing it. It is a 
    good idea to draw diagrams and/or tables rather than trying to 
    do this in your head. 

```python
globals = ["Jupiter", "Mars"]
galactics = ["Andromeda", "Milky Way"]
locals = ["Portland", "Medford"]

def mess(x: list[str], y: list[str]) -> list[str]:
    """Gonna mess with your data!"""
    x[1] = "Venus"
    galactics = ["Triangulum", "Pinwheel" ]
    z = y
    y = ["Corvallis", "Salem"]
    return z

towns = mess(globals, locals)
print(f"Globals is {globals}")
print(f"Galactics is {galactics}")
print(f"Locals is {locals}")
print(f"Returned {towns}")
```

2. Predict what this program prints without executing it. 
```python
countdown = []

def launch(n: int):
    countdown.append(n)
    if n > 0:
        launch(n-1)
    else:
        print(countdown)
        print("Blast off!")

launch(5)
```

3. This program will _not_ work.  What error do you expect? 
```python
countdown = []
n = 10

def launch():
    countdown.append(n)
    if n > 0:
        n = n - 1
        launch()
    else:
        print(countdown)
        print("Blast off!")

launch()
```
## Solutions to exercises

1. Predict the outcome of this program without executing it. 

```{code-cell} python3
globals = ["Jupiter", "Mars"]
galactics = ["Andromeda", "Milky Way"]
locals = ["Portland", "Medford"]

def mess(x: list[str], y: list[str]) -> list[str]:
    """Gonna mess with your data!"""
    x[1] = "Venus"
    galactics = ["Triangulum", "Pinwheel" ]
    z = y
    y = ["Corvallis", "Salem"]
    return z

towns = mess(globals, locals)
print(f"Globals is {globals}")
print(f"Galactics is {galactics}")
print(f"Locals is {locals}")
print(f"Returned {towns}")
```

Do any of those surprise you? 

- Passing `globals` as argument `x` causes `x` to become an alias of 
  `globals`, i.e., another reference to the same list. Setting `x[1]
  ` to `"Venus"` modifies the second element of that list, which is 
  still the list that `globals` is bound to.
- The assignment to `galactics` within the function creates a new 
  local variable called `galactics`, distinct from the global 
  variable called `galactics`.  It therefore has no effect outside 
  the function. 
- We passed `locals` as argument `y`, so `y` is initially an alias 
  to `locals` within the function.  When we assign `z` the value of 
  `y`, we have three names (`locals`, `y`, and `z`) for the same 
  list. But then we change the local (within `mess`) binding of `y` 
  to a new list `["Corvallis", "Salem"]`.  This has no effect on the 
  bindings of `locals` or `z`.  
- We return `z`, which is bound to the same list as `locals`. 
  `towns` then becomes an alias for `locals`. 

When `mess` begins execution, bindings look like this:

![Bindings at entry to `mess`; x and y are aliases to globals and locals
](img/ex1-binding-entry.svg)

The local variables `x` and `y` are references that have been copied 
from `globals` and `locals`, respectively.  When `mess` is just 
about to return, bindings look like this: 

![Bindings at exit from `mess`;  `y` and `galactics` are local variables
](img/ex1-binding-exit.svg)

Only `globals` has been changed in the global namespace.  
`galactics` is unchanged in the global namespace because the new 
assignment to `galactics` was to a local variable in the scope of 
function `mess`.

2. Predict what this program prints without executing it. 
```{code-cell} python3
countdown = []

def launch(n: int):
    countdown.append(n)
    if n > 0:
        launch(n-1)
    else:
        print(countdown)
        print("Blast off!")

launch(5)
```

3. This program will _not_ work.  What error do you expect? 
```{code-cell} python3
:tags: ["raises-exception"]
countdown = []
n = 10

def launch():
    countdown.append(n)
    if n > 0:
        n = n - 1
        launch()
    else:
        print(countdown)
        print("Blast off!")

launch()
```

Because of the assignment `n = n - 1`, `n` will be a local variable 
in the scope of `launch`.  But `n` is referenced in the call to 
`append` and also in the `if` statement, before it has been given a 
value.  These references will break (exception `UnboundLocalError`)
even though there is another variable `n` in the global scope. 