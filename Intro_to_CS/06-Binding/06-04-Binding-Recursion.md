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

#  Binding in Recursive Functions

We have seen that Python searches in LEGM order (local, enclosing, 
global, and finally built-in scopes), and we know that calling a 
function creates a _stack frame_ for its namespace.  The _local_ 
scope is the namespace in the top stack frame.  

While we have seen each of these facts before, it may be worthwhile 
to revisit [our `palindrome` function](final-palindrome) to see how 
scopes work in a recursive function.  Recall that we created a 
wrapper function called `palindrome` to get started and delegate the 
main work to `_palindrome` (with a leading underscore `_` to 
indicate that it is not the public interface).  We'll focus on the 
actual recursive function `_palindrome`.  

```{code-cell} python3
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

word = ['n', 'o', 'o', 'n']
_palindrome(word, 0, len(word) - 1)
```

`_palindrome` will be called three times: `_palindrome(word, 0, 3)`, 
`_palindrome(word, 1, 2)`, and then `_palindrome(word, 2, 1)`.  The 
third call reaches the base case, ending the recursion.  Let's 
consider the stack and scopes at the third call: 

![Memory of `_palindrome` with three levels of recursion](
img/palindrome-binding.png
)

Each execution of `_palindrome` has its own namespace in a _stack 
frame_.  The _top_ stack frame holds the namespace for the _local 
scope_.  In this namespace,  
`first` has value 2 and `last` has value 1, which makes the 
condition `last - first < 1` true (the base case of the recursion).  
As the same value `word` is passed as arguments through the 
recursive calls, the `word` value in each activation of 
`_palindrome` is a reference to the same list.  In other words, 
although each activation of `_palindrome` has a local variable 
`word`, they are all aliases. 


