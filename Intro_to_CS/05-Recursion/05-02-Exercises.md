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

#   Exercises

1.   Complete the recursive function `subset_sums`.
Students in Fall 2023 struggled with a version of this problem.
See if you can 
solve it by making use of each of the facts in your recursive 
solution.   
  
  Note that `subset_sums(10, [1, 3, 5, 7])` returns `True`
  because $3+7=10$, and `subset_sums(16, [1, 3, 5, 7])` returns
  `True` because $1+3+5+7=16$, but
  `subset_sums(12, [2, 3, 5, 8])` returns `False`
  because no subset of the terms 2, 3, 5, and 8 (each used at most
  once)  sum to 12.   

Useful facts:

- The sum of zero integers is zero.  Thus, `subset_sums(0, t)`
  is always true, but `subset_sums(k, [])` is false if `k > 0`. 
- It is impossible to obtain a negative number by summing any 
  set of non-negative integers. 
- If  `k` is positive, then there are two ways
the sum `k` could be produced:
  - If `terms[0]` is included in the subset that sums to `k`, then it 
    must be possible to sum the remaining terms `terms[1:]`  to
    `k - terms[0]`.   
  - If `terms[0]` is not included in the subset that sums to `k`, then
      it must be possible to sum the remaining terms to `k`.

```python
def subset_sums(k: int, terms: list[int]) -> bool:
    """Return True if it is possible to produce k by adding up
    some subset of terms (using each term no more than once).
    k is a positive integer or zero, and each element of terms is a
    positive integer or zero.
    """
    return False # FIXME

print(subset_sums(10, [1, 3, 5, 7]))
# Expect True

print(subset_sums(12, [2, 3, 5, 8]))
# Expect False
```

## Solutions to Exercises

1. A solution to `subset_sums`.  We use the following facts: 

- The sum of zero integers is zero.  Thus, `subset_sums(0, t)`
  is always true (Fact _ENOUGH_), 
  but `subset_sums(k, [])` is false if `k != 0`
  (Fact _RAN OUT_).
- It is impossible to obtain a negative number by summing any 
  set of non-negative integers.  (Fact _NEGATIVE_)
- If  `k` is positive, then there are two ways
the sum `k` could be produced:
  - If `terms[0]` is included in the subset that sums to `k`, then it 
    must be possible to sum the remaining terms `terms[1:]`  to
    `k - terms[0]`.   (Fact _INCLUDE_)
  - If `terms[0]` is not included in the subset that sums to `k`, then
      it must be possible to sum the remaining terms to `k`.
    (Fact _EXCLUDE_)

```{code-cell} python3
def subset_sums(k: int, terms: list[int]) -> bool:
    """Return True if it is possible to produce k by adding up
    some subset of terms (using each term no more than once).
    k is a positive integer or zero, and each element of terms is a
    positive integer or zero.
    """
    # Case ENOUGH
    if k == 0: 
        return True
    # Case RAN OUT
    if len(terms) == 0: 
        return False
    # Case NEGATIVE
    if k < 0: 
        return False
    # We must have positive k and non-empty terms, 
    # so INCLUDE and EXCLUDE are the only remaining cases
    return (subset_sums(k - terms[0], terms[1:])  # INCLUDE 
            or  subset_sums(k, terms[1:]))        # EXCLUDE


print(subset_sums(10, [1, 3, 5, 7]))
# Expect True

print(subset_sums(12, [2, 3, 5, 8]))
# Expect False
```