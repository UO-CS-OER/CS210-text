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

# Review of terms

Terminology of functions and scopes can be confusing, because there 
are many different terms commonly used for the same or almost the 
same concept ... even in the Python documentation.

## Scope, namespace, frame, symbol table

A _namespace_ may also be called a _symbol table_ or a _frame_.  
These terms are not quite identical (a _frame_ is really a 
structure inside the Python interpreter used to implement a 
_namespace_), but they are so closely related that you can treat 
them as synonyms.  

The term _scope_ is also almost 
interchangeable with _namespace_, except "local scope" means 
"the namespace of the currently executing function."  There is 
always exactly one "local" scope and one "global" scope, while there 
may be many namespaces that are temporarily inaccessible.

Every frame implements a namespace, which may be the local scope or 
global scope.  Outside of any function, the local scope and the 
global scope may be the same namespace.  

The technical distinctions may matter 
to you someday if you build your own programming language interpreter.  
For now you can treat _namespace_, _scope_, and _frame_
as synonyms. 

## Local and global variables 

A _local variable_ is a variable in the namespace (scope) of a 
function, accessible only when that function is executing.  A 
_global variable_ is a variable defined in the global namespace, 
which may also be accessible from within functions. 

## Formal and actual arguments (parameters)

The terms _parameter_ (_formal parameter_ or _actual parameter_) 
and _argument_ (_formal argument_ or _actual argument_) are 
synonymous.  The author of 
this chapter looked to the Python documentation to see which term 
was standard in Python.  The disappointing answer was "both".

It could be
confusing to pair "formal parameter" with "actual argument", so we will 
try to be consistent in preferring "argument" in both contexts. 
Occasionally we will use both terms, since you will often encounter 
"formal parameter" in other documentation.  
Sometimes we will mess up ... let us know so we can fix 
inconsistencies in this text.

When we use the term _argument_ in the context of defining a 
function, we mean _formal argument_, that is, the name that will be 
used within the function body.  When we use 
the term _argument_ in the context of calling a function, we mean 
_actual argument_, that is, the value transmitted to the function.  

```python
def f(a):  # a is a formal argument
    """Does nothing"""
    pass

f(x)      # x is an actual argument
```