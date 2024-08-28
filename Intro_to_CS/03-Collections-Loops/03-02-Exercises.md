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

1. Finish function `count_ge` 

```python
def count_ge(nums: list[int], at_least: int) -> int:
    """Returns a count of elements in nums whose value is
    at least (>=)  at_least.
    """
    return 0  # FIXME

print(count_ge([1, 2, 3, 4, 5], 3))  # Expecting 3
print(count_ge([-10, 17, -3, 5], 0)) # Expecting 2
print(count_ge([], 0))  # Expecting 0
print(count_ge([7, 12, 17], 99))  # Expecting 0
```

2. Complete function `longest_word`.
Recall that `len(s)` returns the length of string `s`. 

```python
def longest_word(words: list[str]) -> str:
    """Return the longest element of words, which must be a
    non-empty list of strings.  In case of a tie, return the
    first of the longest elements.
    """
    return "NOT IMPLEMENTED YET"  # FIXME
    

print(longest_word(['we', 'know', 'how', 'to', 'select', 'extremes']))
# Expect 'extremes'

print(longest_word(['we', 'already', 'know', 'how']))
# Expect 'already'

print(longest_word(['really?']))
# Expect 'really?'
```

## Answers to Exercises

1. Here is one possible way to finish `count_ge` 

```{code-cell} python3
def count_ge(nums: list[int], at_least: int) -> int:
    """Returns a count of elements in nums whose value is
    at least (>=)  at_least.
    """
    count = 0
    for n in nums: 
        if n >= at_least:
            count += 1
    return count

print(count_ge([1, 2, 3, 4, 5], 3))  # Expecting 3
print(count_ge([-10, 17, -3, 5], 0)) # Expecting 2
print(count_ge([], 0))  # Expecting 0
print(count_ge([7, 12, 17], 99))  # Expecting 0
```

2. Here is a possible completion of  `longest_word`.

```{code-cell} python3
def longest_word(words: list[str]) -> str:
    """Return the longest element of words, which must be a
    non-empty list of strings.  In case of a tie, return the
    first of the longest elements.
    """
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
    

print(longest_word(['we', 'know', 'how', 'to', 'select', 'extremes']))
# Expect 'extremes'

print(longest_word(['we', 'already', 'know', 'how']))
# Expect 'already'

print(longest_word(['really?']))
# Expect 'really?'
```
