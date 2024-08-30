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

Check your understanding. These exercises are taken from old exams, 
which implies that you 
should be able to complete them pretty quickly. 

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

3. We classify some letters as vowels, others as consonants.
Some characters (such as "-") are neither vowels nor consonants.
In this problem, you are given a function `is_vowel`, which you
must use.  

You will write function vowel_ratio, which returns
the ratio of vowels to string length as a floating point number.
For example, "bash" has one vowel and three characters that are not
vowels, so its vowel_ratio is 1/4 or 0.25.  

All strings passed to vowel_ratio will have at least one character.

```python
def is_vowel(s: str) -> bool:
    """Returns true if and only if s is a vowel"""
    return (s.lower() in "aeiou")

def vowel_ratio(s: str) -> float:
    """Returns the fraction between 0.0 and 1.0 of characters
    ch in s, a non-empty string,  for which is_vowel(ch) is true.
    """
    return 0  # FIXME

print(vowel_ratio("bear"))   # Expect 0.5
print(vowel_ratio("honey"))  # Expect 0.4
print(vowel_ratio("xXx"))    # Expect 0.0
print(vowel_ratio("aAa"))    # Expect 1.0
```

4. Complete function `count_one_value`. 

```python
def count_one_value(k: str, li: list[str]) -> int:
    """How many occurrences of k are in li?"""
    return 0  # FIXME


print(count_one_value("duck", ["duck", "goose", "duck", "duck"]))
# Expect 3
print(count_one_value("t-rex", ["duck", "goose", "duck", "duck"]))
# Expect 0
```

5. Complete function `count_all_values`. 

```python
def count_all_values(li: list[str]) -> dict[str, int]:
    """Returns dict with counts of strings in li.
    """
    return {}  # FIXME

print(count_all_values(["carrot", "chocolate", "carrot", "strawberry"]))
# Expect {'carrot': 2, 'chocolate': 1, 'strawberry': 1}

print(count_all_values([]))
# Expect {}
```

6. Complete function `select_by_value`. 

```python
def select_by_value(min_val: int, li: list[str], values: dict[str, int]) -> list[str]:
    """Returns list of elements of li associated with a value at least min_val in values.
    (Assume all elements in li are keys in values)
    """
    return []  # FIXME


print(select_by_value(5, ["dog", "cat", "rabbit"], {"cat": 7, "rabbit": 3, "dog": 9}))
# Expect ['dog', 'cat']

print(select_by_value(17, ["dog", "cat", "rabbit"], {"cat": 12, "rabbit": 4, "dog": 9}))
# Expect []
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

3. Here is a function vowel_ratio, which returns
the ratio of vowels to string length as a floating point number,
using function `is_vowel`. 

```{code-cell} python3
def is_vowel(s: str) -> bool:
    """Returns true if and only if s is a vowel"""
    return (s.lower() in "aeiou")

def vowel_ratio(s: str) -> float:
    """Returns the fraction between 0.0 and 1.0 of characters
    ch in s, a non-empty string,  for which is_vowel(ch) is true.
    """
    vowel_count = 0
    total_count = 0
    for ch in s:
        total_count += 1
        if is_vowel(ch):
            vowel_count += 1
    return vowel_count / total_count


print(vowel_ratio("bear"))   # Expect 0.5
print(vowel_ratio("honey"))  # Expect 0.4
print(vowel_ratio("xXx"))    # Expect 0.0
print(vowel_ratio("aAa"))    # Expect 1.0
```

4.  Function `count_one_value`
is an example of the _accumulator pattern_. 

```{code-cell} python3
def count_one_value(k: str, li: list[str]) -> int:
    """How many occurrences of k are in li?"""
    count = 0
    for el in li:
        if el == k:
            count += 1
    return count  


print(count_one_value("duck", ["duck", "goose", "duck", "duck"]))
# Expect 3
print(count_one_value("t-rex", ["duck", "goose", "duck", "duck"]))
# Expect 0
```

5.  `count_all_values` is a variation on our project for analyzing 
    class enrollments (just the counting part).  We can consider it 
    a variation on the accumulator pattern, but we are accumiulating 
    a count for each distinct string, using a `dict`. 

```{code-cell} python3
def count_all_values(li: list[str]) -> dict[str, int]:
    """Returns dict with counts of strings in li.
    """
    counts = {}
    for el in li:
        if el in counts:
            counts[el] += 1
        else:
            counts[el] = 1
    return counts

print(count_all_values(["carrot", "chocolate", "carrot", "strawberry"]))
# Expect {'carrot': 2, 'chocolate': 1, 'strawberry': 1}

print(count_all_values([]))
# Expect {}
```

6. The pattern of `select_by_value` is sometimes called a _filter_.  
   Be sure to solve it by building a new list with just the selected 
   items, and _not_ by removing elements from `li`. 
You need to put together a couple patterns you know
(filtering a collection, using a `dict`) to solve a new problem.
Computational problem solving often involves combining and customizing
familiar patterns into novel forms.


```{code-cell} python3
def select_by_value(min_val: int, li: list[str], values: dict[str, int]) -> list[str]:
    """Returns list of elements of li associated with a value at least min_val in values.
    (Assume all elements in li are keys in values)
    """
    result = []
    for el in li:
        if values[el] >= min_val:
            result.append(el)
    return result


print(select_by_value(5, ["dog", "cat", "rabbit"], {"cat": 7, "rabbit": 3, "dog": 9}))
# Expect ['dog', 'cat']

print(select_by_value(17, ["dog", "cat", "rabbit"], {"cat": 12, "rabbit": 4, "dog": 9}))
# Expect []
```


A common mistake is making a sequential search of `values` for each
element of `li`.   We use the
`dict` data structure to avoid linear searches when we can. If we
had 1000 elements in `li` and 1000 (key, value) pairs in
`values`, the nested loops for sequentially searching
`values` would require 1,000,000 comparisons, while looking up
values with dictionary access `if values[item] >= min_value:`
would require only 1000 dictionary lookups.  Any time you see a 
`dict`, you should expect that it is there so that we can access 
items directly by key rather than making a linear search of the 
structure. 