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
# Imported and Qualified Names

The LEGB rule for finding something by name applies to imported 
modules as well.  A module, whether from a built-in Python library 
or a new source file we construct, is a kind of object with a name.  
An `import` statement is like an assignment that gives it a binding 
in the current module.  

```{code-cell} python3
import csv            # Now "csv" is the name of a module object

another_name = csv    # Legal, but not the best approach
print(another_name)
```
We don't usually assign modules to variables, but the code above 
demonstrates that Python treats the name of an imported module just 
like any other name.   If we did want to use another name for a 
module, Python provides an `import ... as ...` syntax: 

```{code-cell}  python3
import doctest as dt

print(dt)
```

A module you write yourself is treated just like library module that 
Python provides.

## Qualified names

 A module is an object that can contain other objects, including 
 functions and variables.   When we write `m.v`, we are asking 
 Python to find `m`, and then to look inside `m` to find `v`.  

Suppose, for example, we have this source file `exporter.py`:

```python
"""exporter.py.  This module is designed to be imported by importer.py.
Its "symbols"  (names of functions and variables) will be
visible as attributes of the module.
"""

STEP_SIZE = 5

def step(i: int) -> int:
    return i + STEP_SIZE
```

We might _import_ it as a module in another source file, `exporter.py`:

```python
"""importer.py.  Demonstration of referencing qualified names
from another module.
"""

import exporter

print(exporter.step(10))
exporter.STEP_SIZE = 20
print(exporter.step(10))
```

After the `import` statement in `importer.py`, `exporter` is the 
name of a _module object_ that contains variables and functions.  
When we write `exporter.step(10)` in `importer.py`, Python first 
looks for the name `exporter` (following the LEGB search order) and 
finds it in the global scope.  It looks within the module object for 
`step`, and finds a function object that it can call.  The `step` 
function in `exporter.py` uses the LEGB search order to find 
`STEP_SIZE`, but "global" in this case means "global to the same 
module that `step` is in".  It finds the variable `STEP_SIZE` 
variable bound to integer value 5. 

Similarly the statement `exporter.STEP_SIZE = 20` asks Python to
look within the module object `exporter` to find `STEP_SIZE`. 
It finds a variable that can be bound to the new value 20.
When we call 
`exporter.step` the second time, the `step` function again uses the 
`LEGB` order, and again finds `STEP_SIZE` in its own module (the 
"global" scope for that module), now bound to integer value 20. 

```shell
>>> python3 06-binding/samples/importer.py
15
30
```





