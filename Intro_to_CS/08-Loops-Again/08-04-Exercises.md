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

1.  Function `lookup` in the following snippet is incorrect.  
    Explain the error and fix it.  

```python
def lookup(code: str, abbrevs: list[str], full: list[str]) -> str: 
    """Return the full name corresponding to abbreviated code.
    abbrevs and full are a table in the form of parallel arrays. 
    Returns "NA" if there is no abbrev[i] == code.
    """
    for abbrev in abbrevs: 
        if abbrevs[abbrev] == code: 
            return full[abbrev]
    return "NA"

state_codes = ["OR", "ID", "WA", "CA"]
state_names = ["Oregon", "Idaho", "Washington", "California"]
print(lookup("ID", state_codes, state_names))  # Expect "Idaho"
print(lookup("GA", state_codes, state_names))  # Expect "NA"
```

2.  Function `column_sums` is incorrect.  Explain the error and fix it. 

```python
def col_sums(grid: list[list[int]]) -> list[int]:
    """Return the sum of each column in grid.
    grid must be a non-empty rectangular matrix of integers.
    """
    sums = []
    for col_i in range(len(grid[0])):
        col_sum = 0
        for row_i in range(len(grid)):
            col_sum += grid[col_i][row_i]
        sums.append(col_sum)
    return sums
            
my_grid = [[4, 3, 7],
           [6, 7, 3]]
print(col_sums(my_grid))  # Expect [10, 10, 10]
```

3. Function `find_major` is incorrect.  Explain the error and fix it. 

```python
MAJORS = [("CS", "Computer Science"), ("DSCI", "Data Science"),
          ("MACS", "Mathematics and Computer Science"),
          ("ARDF", "Digital Arts"), ("ATCH", "Art and Technology"),
          ("CH", "Chemistry"), ("CHN", "Chinese"),
          ("CYBR", "Cybersecurity"), ("DANC", "Dance"),
          ("FLR", "Folklore"), ("FR", "French")
          ]

def find_major(code: str) -> str: 
    """Returns full major name corresponding to code. 
    Returns "NONE" if (code, name) is not in MAJORS).
    """
    for el in range(len(MAJORS)):
        major_code, major_name = MAJORS[el]
        if code == major_code: 
            return el
    return "NONE"

print(find_major("CHN"))   # Expect "Chinese"
print(find_major("DSCI"))  # Expect "Data Science"
print(find_major("PHY"))   # Expect "NONE"
```

4.  Which of the functions above (`lookup`, `column_sums`, and 
    `find_major`) _must_ loop through indexes, and which could loop 
    through elements instead?  Why?  Would your answer change if 
    `find_major` uses binary search instead of sequential search?

5.  Function `expand_text` is potentially very inefficient for long 
    inputs. Why?  Fix it to require time at most directly 
    proportional ("linear time") in the length of the expanded
    text. 

```python
ABBRV = {"btw": "by the way", "lmk": "let me know",
         "ttyl": "Talk to you later", "brb": "Be right back",
         "4": "for", "ftw": "for the win", "tbh": "To be honest",
         "lol": "laugh out loud", "idk": "I don't know", 
         "tmi": "too much information"
         }

def expand_text(msg: str) -> str: 
    """Replace abbreviations by full words"""
    words = msg.split() 
    expansion = ""
    for word in words: 
        if word in ABBRV: 
            expansion += ABBRV[word] + " "
        else: 
            expansion += word + " "
    return expansion

msg = """btw its tmi 4 sure . ttyl . """
print(expand_text(msg))  
# Expect: "By the way its too much information for sure . 
#          Talk to you later .
```

## Solutions

1.  The `lookup` function contains a "mix-n-match" loop, a mismatch 
    between 
    the form of the `for` loop and accesses to lists within the loop.
    The `for` loop is iterating through _elements_ of abbrevs, but 
    using those elements as if they were _indexes_.  We can fix it 
    by changing to a loop over indexes. 

```{code-cell} python3
def lookup(code: str, abbrevs: list[str], full: list[str]) -> str: 
    """Return the full name corresponding to abbreviated code.
    abbrevs and full are a table in the form of parallel arrays. 
    Returns "NA" if there is no abbrev[i] == code.
    """
    for abbrev_i in range(len(abbrevs)): 
        if abbrevs[abbrev_i] == code: 
            return full[abbrev_i]
    return "NA"

state_codes = ["OR", "ID", "WA", "CA"]
state_names = ["Oregon", "Idaho", "Washington", "California"]
print(lookup("ID", state_codes, state_names))  # Expect "Idaho"
print(lookup("GA", state_codes, state_names))  # Expect "NA"
```

2. Function `col_sums` correctly iterates columns in the outer loop, 
   rows in the inner loop, but then it indexes the grid using the 
   column number as the first index (the row index) and row number 
   as the second index (the column index).  In `a[m][n]`, `m` always 
   indexes the outer list (usually "rows" when we are thinking of 
   `a` as a matrix) and `n` always indexes the inner lists (usually 
   "columns" when `a` is a matrix).  

    We can fix it just by swapping indexes. 

```{code-cell} python3
def col_sums(grid: list[list[int]]) -> list[int]:
    """Return the sum of each column in grid.
    grid must be a non-empty rectangular matrix of integers.
    """
    sums = []
    for col_i in range(len(grid[0])):
        col_sum = 0
        for row_i in range(len(grid)):
            col_sum += grid[row_i][col_i]
        sums.append(col_sum)
    return sums
            
my_grid = [[4, 3, 7],
           [6, 7, 3]]
print(col_sums(my_grid))  # Expect [10, 10, 10]
```

3. `find_major` contains another "mix-n-match" loop, with confusion 
   between looping through indexes and looping through elements. The 
   `for` loop iterates through indexes, and returns an index, but 
   the function docstring promises to return a string from the 
   MAJORS table.   We could fix it by changing the `return` 
   statement to `return major_name`.  Better yet, since this 
   function doesn't _need_ indexes, we can just loop through 
   elements like this: 

```{code-cell} python3
MAJORS = [("CS", "Computer Science"), ("DSCI", "Data Science"),
          ("MACS", "Mathematics and Computer Science"),
          ("ARDF", "Digital Arts"), ("ATCH", "Art and Technology"),
          ("CH", "Chemistry"), ("CHN", "Chinese"),
          ("CYBR", "Cybersecurity"), ("DANC", "Dance"),
          ("FLR", "Folklore"), ("FR", "French")
          ]

def find_major(code: str) -> str: 
    """Returns full major name corresponding to code. 
    Returns "NONE" if (code, name) is not in MAJORS).
    """
    for major_code, major_name in MAJORS:
        if code == major_code: 
            return major_name
    return "NONE"
    
print(find_major("CHN"))   # Expect "Chinese"
print(find_major("DSCI"))  # Expect "Data Science"
print(find_major("PHY"))   # Expect "NONE"
```

4.  Function `lookup` _must_ loop through indexes because it 
    accesses parallel arrays.  It needs the index in one list
    to access the corresponding element in the other list.  
    `column_sums` _must_ loop through column indexes, because rows 
    in the grid are like parallel arrays. 
    `find_major` could loop through elements for sequential search, 
    but binary search requires using indexes (with a `while` 
    loop, not a `for` loop).  

5. Function `expand_text` is potentially very inefficient for long 
    inputs because it concatenates strings in the loop.  Each 
   concatenation takes time proportional to the length of 
   `expansion`, which can add up to time proportional to the square 
   of the length of the result.  (More precisely, it will be 
   proportional to the length of the result multiplied by the number 
   of words.)  The standard repair is to build a list instead (as 
   the cost of `append` is constant) and then use the `join` method 
   just once after the loop. 

```{code-cell} python3
ABBRV = {"btw": "by the way", "lmk": "let me know",
         "ttyl": "Talk to you later", "brb": "Be right back",
         "4": "for", "ftw": "for the win", "tbh": "To be honest",
         "lol": "laugh out loud", "idk": "I don't know", 
         "tmi": "too much information"
         }

def expand_text(msg: str) -> str: 
    """Replace abbreviations by full words"""
    words = msg.split() 
    expansion = []
    for word in words: 
        if word in ABBRV: 
            expansion.append(ABBRV[word])
        else: 
            expansion.append(word)
    return " ".join(expansion)

msg = """btw its tmi 4 sure . ttyl . """
print(expand_text(msg))  
# Expect: "By the way its too much information for sure . 
#          Talk to you later .
```