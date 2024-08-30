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

1.  Complete function `lookup`, first (1a) as a linear search and 
    then (1b) as a binary search.  

```python
def lookup(item_key: str, keys: list[str], values: list[int]) -> int:
    """With keys and items as parallel arrays, ordered
    by key, return values[i] such that keys[i] == item_key, 
    or return -1 if there is no such i. 
    """
    return -1  # FIXME

print(lookup("tiger", ["bear", "lion", "tiger"], [13, 47, 17]))
# Expect 17

print(lookup("tiger", ["bear", "lion", "tiger", "zebra"],
             [13, 47, 17, 24]))
# Expect 17

print(lookup("bear", ["bear", "lion", "tiger", "zebra"],
             [13, 47, 17, 24]))
# Expect 13

print(lookup("zebra", ["bear", "lion", "tiger", "zebra"],
             [13, 47, 17, 24]))
# Expect 24

print(lookup("wolf", ["bear", "lion", "tiger"], [13, 47, 17]))
# Expect -1
```

2. Complete function `matches`.

```python
def matches(x_l: list[str], y_l: list[str]) -> list[bool]:
    """Returns list m in which each m[i] is
    True if and only if x_l[i] is same as y_l[i].
    x_l and y_l are parallel lists.
    """
    assert len(x_l) == len(y_l), "x_l and y_l must be parallel lists"
    return [False]  # FIXME


print(matches(["a", "b", "c"], ["a", "x", "c"]))
# Expect [True, False, True]
```

3.  At Oregano University of Culinary Arts, (OU), 
each student must complete courses in
each of 3 areas:  Athletics and Leisure (AL), 
Spices and Condiments (SC), and Soft Skills (SS).

An OU transcript represented by parallel lists
giving courses and areas, e.g., 

```python
courses = ["CS 210 - Intro to Cooking and Serving", 
           "WR 123 - Wrangling Customers", 
           "PS 222 - Poisonous Substances"]
areas =  ["SC", "SS", "SC"]
```

To help student gauge their progress toward satisfying the
area requirements, you will write a function already_taken
that takes a transcript (two lists) and an area code
(usually "SC", "SS", or "SC") and returns a list of the
transcripted courses that count toward that area. 


```python
def already_taken(courses: list[str],
                  areas: list[str], 
                  selection: str) -> list[str]:
    """Result summarizes the transcripted courses in each area"""
    return []  # FIXME
    
# Course titles shortened to keep test cases short
courses = ["CS 210", "WR 123", "PS 222"]
areas = ["SC", "SS", "SC"]
print(already_taken(courses, areas, "SC"))
 # Expect   ['CS 210', 'PS 222']

print(already_taken(courses, areas, "SS"))
 # Expect    ['WR 123']

print(already_taken(courses, areas, "AL"))
# Expect   []
```

4. Given a price table represented as a dict, with product names as keys
and unit price as value, 
and given a list of purchases as (units, product) pairs,
write a function total_cost that
gives the total cost for the list of purchases.  
Units will always be positive integers.

Prices and total cost are given in cybercoins,
a currency which will be created by an Oregon CS graduate in 2032.
All items purchased will
have a corresponding price in the price list.

```python
def total_cost(purchases: list[tuple[str, int]], prices: dict[str, int]) -> int:
    """Sum of costs of purchases, where
    ("item", n) in purchases means n units of item,
    "item": k  in prices means each unit of item costs k cybercoins
    """
    return 0  # FIXME

print(total_cost([("apple", 2), ("banana", 3)],
                 { "pizza": 12,  "apple": 2, "banana": 1 }))
#Expect    7

print(total_cost([], {"yacht": 99_000_000, "apple": 2}))
# Expect   0 
```


5. Complete function `score_word`, consistent with its docstring.
   (Use the global variable VALUES, which is constructed by the
   `point_values` function.)

```python
def point_values() -> dict[str, int]:
    """Returns per-letter point values as dict"""
    points = {1: "AEILNORSTU", 2: "DG", 3: "BCMP",
              4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
    letter_values = {}
    for value in points:
        for letter in points[value]:
            letter_values[letter] = value
    return letter_values

VALUES = point_values()

def score_word(word: str) -> int:
    """Returns the sum of point values
     (from global variable VALUES) of letters in word,
    according to points table.
    Word contains only upper case English letters.
    """
    return 0  # FIXME


print(score_word("QUACK"))
# Expect   20

print(score_word("DUCK"))
# Expect 11
```


## Solutions to exercises

1a.  Linear search solution to `lookup`. 

```{code-cell} python3
def lookup(item_key: str, keys: list[str], values: list[int]) -> int:
    """With keys and items as parallel arrays, ordered
    by key, return values[i] such that keys[i] == item_key, 
    or return -1 if there is no such i. 
    """
    for probe in range(len(keys)):
        if keys[probe] == item_key: 
            return values[probe]
    return -1

print(lookup("tiger", ["bear", "lion", "tiger"], [13, 47, 17]))
# Expect 17

print(lookup("tiger", ["bear", "lion", "tiger", "zebra"],
             [13, 47, 17, 24]))
# Expect 17

print(lookup("bear", ["bear", "lion", "tiger", "zebra"],
             [13, 47, 17, 24]))
# Expect 13

print(lookup("zebra", ["bear", "lion", "tiger", "zebra"],
             [13, 47, 17, 24]))
# Expect 24

print(lookup("wolf", ["bear", "lion", "tiger"], [13, 47, 17]))
# Expect -1
```

1b. Binary search solution to `lookup`.

```{code-cell} python3
def lookup(item_key: str, keys: list[str], values: list[int]) -> int:
    """With keys and items as parallel arrays, ordered
    by key, return values[i] such that keys[i] == item_key, 
    or return -1 if there is no such i. 
    """
    low = 0
    high = len(keys) - 1
    while high >= low: 
        probe = (high + low) // 2
        if keys[probe] == item_key:
            return values[probe]
        if keys[probe] < item_key: 
            low = probe + 1
        else: 
            high = probe - 1
    return -1 

print(lookup("tiger", ["bear", "lion", "tiger"], [13, 47, 17]))
# Expect 17

print(lookup("tiger", ["bear", "lion", "tiger", "zebra"],
             [13, 47, 17, 24]))
# Expect 17

print(lookup("bear", ["bear", "lion", "tiger", "zebra"],
             [13, 47, 17, 24]))
# Expect 13

print(lookup("zebra", ["bear", "lion", "tiger", "zebra"],
             [13, 47, 17, 24]))
# Expect 24

print(lookup("wolf", ["bear", "lion", "tiger"], [13, 47, 17]))
# Expect -1
```

2. `matches` requires you to apply the _accumulator pattern_ to 
   parallel arrays, building a new array of boolean values.
   Notice that we can obtain the boolean values _without_ an if 
   statement.

```{code-cell} python3
def matches(x_l: list[str], y_l: list[str]) -> list[bool]:
    """Returns list m in which each m[i] is
    True if and only if x_l[i] is same as y_l[i].
    x_l and y_l are parallel lists.
    """
    assert len(x_l) == len(y_l), "x_l and y_l must be parallel lists"
    result = []   
    for i in range(len(x_l)):
        result.append(x_l[i] == y_l[i])
    return result

print(matches(["a", "b", "c"], ["a", "x", "c"]))
# Expect [True, False, True]
```

3. Graduation progress at Oregano University. 

```{code-cell} python3
def already_taken(courses: list[str],
                  areas: list[str], 
                  selection: str) -> list[str]:
    """Result summarizes the transcripted courses in each area"""
    taken = []
    for i in range(len(courses)):
        if areas[i] == selection:
            taken.append(courses[i])
    return taken
    
# Course titles shortened to keep test cases short
courses = ["CS 210", "WR 123", "PS 222"]
areas = ["SC", "SS", "SC"]
print(already_taken(courses, areas, "SC"))
 # Expect   ['CS 210', 'PS 222']

print(already_taken(courses, areas, "SS"))
 # Expect    ['WR 123']

print(already_taken(courses, areas, "AL"))
# Expect   []
```

4. Total cost from list of items and table of prices.

```{code-cell} python3
def total_cost(purchases: list[tuple[str, int]], prices: dict[str, int]) -> int:
    """Sum of costs of purchases, where
    ("item", n) in purchases means n units of item,
    "item": k  in prices means each unit of item costs k cybercoins
    """
    total = 0
    for product, units in purchases:
        total += prices[product] * units
    return total


print(total_cost([("apple", 2), ("banana", 3)],
                 { "pizza": 12,  "apple": 2, "banana": 1 }))
# Expect  7

print(total_cost([], {"yacht": 99_000_000, "apple": 2}))
# Expect   0 
```

5. Function `score_word`.  

```{code-cell} python3
def point_values() -> dict[str, int]:
    """Returns per-letter point values as dict"""
    points = {1: "AEILNORSTU", 2: "DG", 3: "BCMP",
              4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
    letter_values = {}
    for value in points:
        for letter in points[value]:
            letter_values[letter] = value
    return letter_values

VALUES = point_values()

def score_word(word: str) -> int:
    """Returns the sum of point values
     (from global variable VALUES) of letters in word,
    according to points table.
    Word contains only upper case English letters.
    """
    score = 0
    for letter in word: 
        score += VALUES[letter]
    return score


print(score_word("QUACK"))
# Expect   20

print(score_word("DUCK"))
# Expect 11
```