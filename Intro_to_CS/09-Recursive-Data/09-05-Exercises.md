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

1. Write a function to _flatten_ a nested list of integers, i.e., to 
   return a list containing all the same integers but without 
   nesting. For example, given `l = [1, [2, [3, 4], 5], 6]`, `flatten
   (l)` should return `[1, 2, 3, 4, 5, 6]`. 

2. An _S-expression_ is a form of nested list. 
   - An S-expression can be an _atom_.  For this exercise, atoms 
     will be strings. 
   - An S-expression can be a list in which the first element is 
     called the _head_ and must be an atom.  The remainder of the 
     list (zero or more elements) is called the _tail_.  Each 
     element of the tail is an S-expression. 


For example, `["1.", "a", ["b", "b.1", "b.2"], "c"]` is an 
S-expression.  

Write a function to print an S-expression as a bulleted list. For 
example, given the list above, your function should print
```text
- 1.
  - a
  - b
      - b.1
      - b.2
  - c
```
Given this S-expression
```python
menu = ["Menu", ["Coffee",  "Caffe latte", "Caffe espresso", "Cappuccino", "Latte macchiato"],
                ["Tea",  ["Green Teas", "烏龍 (Oolong)", "毛尖花 (Mao Jian flowers)", "抹茶 (Matcha)"],
                        ["Black and Red Teas", "Darjeeling", "Lapsang Souchong", "Assam"],
                        "Masala chai"],
                "Water"]
```
it should print
```text
- Menu
    - Coffee
        - Caffe latte
        - Caffe espresso
        - Cappuccino
        - Latte macchiato
    - Tea
        - Green Teas
            - 烏龍 (Oolong)
            - 毛尖花 (Mao Jian flowers)
            - 抹茶 (Matcha)
        - Black and Red Teas
            - Darjeeling
            - Lapsang Souchong
            - Assam
        - Masala chai
    - Water
```

3. A specification of a data structure is called a _schema_
    (plural: _schemata_). For 
    example, a database schema might describe one or more database 
    tables and associate a name and type with each column in each 
    table.   A user of the _pandas_ statistical software package 
    might use
    [pandas.DataFrame.columns](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html)
    and 
    [pandas.DataFrame.dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)
    to query the schema of a dataframe.
    In Python we use type annotations to document the schema of each
    formal argument to a function, whether that schema is as simple 
    as a built-in type iike `int` or as complex as the recursive 
    `Nest` data structure we used in
    [our treemap project](https://github.com/UO-CS210/Treemap).

    It is convenient to save and restore Python data structures 
    using the [JSON](https://www.json.org/json-en.html) data exchnge 
    format.  Python makes it easy using the built-in
    [json](https://docs.python.org/3/library/json.html) module.
    However, when we read a JSON document into a Python structure,
    it is not easy to check that it conforms to the structures we 
    expected.   It would be nice to be able to check the structure 
    against a schema. 

    We can use S-expressions to express schemata for nested 
    structures of lists and dicts produced by `json.load` or
    `json.loads`. We'll begin by limiting ourselves to structures of 
    fixed depth (i.e., nested but not recursive), and limit the 
    atomic elements to `int`, `str`, and `float`. The permitted 
    forms of a schema will be 
    - An atomic type name `int`, `str`, or `float`
    - A composite structure `[list S]` or `[dict A S]`, where `S` is 
      a schema and `A` is an atomic type name.

    For example, `{ 'a': [1, 2, 3], 'b': [3, 4]}` would conform to 
    schema `[dict str [list int]]` but would not conform to schema
    `[list [dict str int]]`. 
    
    Write a checker function that takes a structure and a schema
    (expressed as an S-expression) and 
    returns `True` iff the structure conforms to the schema. 

4. The schema specifications in exercise 3 allow us to specify the 
   content of a _homogenous_ list (that is, a list in which each 
   element has the same type), but they do not let us specify that a 
   list should have exactly _k_ elements, which a particular type 
   for each element (e.g., each column in a database table or a 
   spreadsheet).   Extend your solution to exercise 2 with a new 
   composite structure `["row", S, S, ...]` where each `S` is a schema. 
   For example `[5, "apple", [2, 3, 6]]` conforms to 
   `["row",  int, str, [list, int]])`.  

4a. Bonus challenge: 
   A schema is itself a nested (and recursive) 
   data structure.  Write a checker that returns `True` if a schema 
   is correctly structured. 

4b. Bonus challenge (advanced):  
   Devise an approach to specify schemata for 
   recursive data structures.   You will need a way to introduce 
   names for the recursive elements and a way to allow alternatives 
   (so that you can give a recursive case and a base case for the 
   structure).  Providing enough expressive power while keeping the 
   schemata as simple and readable as possible is not easy! 

## Solutions

1. Write a function to _flatten_ a nested list of integers, i.e., to 
   return a list containing all the same integers but without 
   nesting. For example, given `l = [1, [2, [3, 4], 5], 6]`, `flatten
   (l)` should return `[1, 2, 3, 4, 5, 6]`. 

```{code-cell} python3
IntNest = int | list['IntNest']

def flatten(l: IntNest) -> list[int]: 
    if isinstance(l, int): 
        # Base case:
        # Counter-intuitively, we will pack the int 
        # into a list so that we can treat all results
        # uniformly in the recursive case.
        return [l]
    elif isinstance(l, list): 
        # Recursive case:  Obtain a flat list from each element,
        # and merge them. 
        result = []
        for el in l: 
            result += flatten(el)
        return result
    else: 
        raise ValueError(f"This isn't an IntNest: {l}")

l = [1, [2, [3, 4], 5], 6]
l_flat = flatten(l)
print(l_flat)  # Expect [1, 2, 3, 4, 5, 6]
```
Here's another approach, which is probably a little more efficient 
because appending to a list is faster than concatenating lists: 

```{code-cell} python3
# Alternative version, with a helper function 
#
def construct_flat(l: IntNest, flat: list[int]): 
    """Insert each integer into flat"""
    if isinstance(l, int):
        flat.append(l)
    elif isinstance(l, list): 
        for el in l: 
             construct_flat(el, flat)
    else: 
        raise ValueError(f"This isn't an IntNest: {l}")
    
def flatten(l: IntNest) -> list[int]:
    result = []
    construct_flat(l, result)
    return result
    
l = [1, [2, [3, 4], 5], 6]
l_flat = flatten(l)
print(l_flat)  # Expect [1, 2, 3, 4, 5, 6]
```

2. Write a function to print an S-expression as a bulleted list.
In this sample solution, I introduce a type name `Sexp` to formulate 
   some (but not all) of the rules for S-expressions, and use a 
   keyword argument `level` with a default value of 0 to control 
   indentation level.   The `howto` document for the [treemap project](
    https://github.com/UO-CS210/Treemap) 
    introduces complex type definitions like the declaration of 
   `Sexp` in this exercise and `Schema` in the next.

   Printing with `end=""` is a way to print 
   without going to the next line, but you could accomplish the same 
   thing by building up a string for the "leader" (indentation plus 
   bullet) on each line. 

```{code-cell} python3
Sexp = str | list['Sexp']

def print_bulleted(exp: Sexp, level=0):
    """Printed nest as bulleted list."""
    for i in range(level):
        print("    ", end="")
    if isinstance(exp, str):
        print(f"- {exp}")
    else:
        print(f"- {exp[0]}")
        for child in exp[1:]:
            print_bulleted(child, level+1)
            
menu = ["Menu", ["Coffee",  "Caffe latte", "Caffe espresso", "Cappuccino", "Latte macchiato"],
                ["Tea",  ["Green Teas", "烏龍 (Oolong)", "毛尖花 (Mao Jian flowers)", "抹茶 (Matcha)"],
                        ["Black and Red Teas", "Darjeeling", "Lapsang Souchong", "Assam"],
                        "Masala chai"],
                "Water"]

print_bulleted(menu)           
```

3. Check conformance of a structure to a schema. Your solution does 
   not need to be as complex as mine – it is ok to assume the schema 
   is well-formed.  A lot of the code 
   in my sample solution, below, is checking the well-formedness of 
   the schema as we work through the schema and the structure 
   together.  Note that my sample solution raises an exception when 
   the schema is 
   ill-formed, instead of returning `False` as it does when the 
   schema is well-formed but the structure does not conform to the 
   schema.  The exception messages print types like `int` as `<class 
   int>` ... let me know if you find a way to fix that! 

```{code-cell} python3
Schema = type | list['Schema']

def conforms(structure: object, schema: Schema) -> bool:
    """Like "isinstance" but checking a structure against a
    schema that could be int, str, float or an S-expression
    [list S] or [dict A S]. where A is int, str, or float and
    S is a schema.
    """
    if schema in [int, float, str]:
        return isinstance(structure, schema)
    elif isinstance(schema, list):
        pass  # continued below
    else:
        raise ValueError(f"Ill-formed schema {schema} should be int, float, str," +
                         "[list element-schema], or [dict key-type value-schema]")

    # Schema is a list
    t, *components = schema
    if t not in [list, dict]:
        raise ValueError(f"Schema composite types are list and dict, not {t}")
    if t == list:
        if len(components) != 1:
            raise ValueError(f"Schema for list should have one component type, not {components}")
        if not isinstance(structure, list):
            return False
        comp_type = components[0]
        for item in structure:
            if not conforms(item, comp_type):
                return False
        return True
    else:
        # t is dict
        if len(components) != 2:
            raise ValueError(f"dict schema should have two component types, for key and value, not {components}")
        key_type, value_type = components
        if key_type not in [int, str, float]:
            raise ValueError(f"dict schema key type should be str, int, or float, not {key_type}")
        if not isinstance(structure, dict):
            return False
        for k,v in structure.items():
            if not isinstance(k, key_type):
                return False
            if not conforms(v, value_type):
                return False
        return True


print(conforms({ 'a': [1, 2, 3], 'b': [3, 4]},  
               [dict, str, [list, int]]))            # Expect True
print(conforms({ 'a': [1, 2, 3], 'b': [3, 4]}, 
               [list, [dict, str, int]]))           # Expect False
print(conforms([{"a": 1, "b": 2}, {"c": 3, "d": 4 }], 
                [list, [dict, str, int]]))          # Expect True
print(conforms([{"a": 1, "b": 2}, {"c": 3, "d": 4 }], 
               [dict, str, [list, int]]))           # Expect False

# Exception rather than False for malformed schemata
try:
    conforms({ 'a': [1, 2, 3], 'b': [3, 4]},
             [dict, [list, int], [list, int]])
    raise(Exception("Malformed schema should have failed!"))
except ValueError as e:
    print(f"Rejected malformed schema as expected: {e}")
```

4. The _row_ schema is an additional case to consider, with 
   traversal of the structure and schema as parallel arrays. 

```{code-cell} python3
Schema = type | list['Schema']

def conforms(structure: object, schema: Schema) -> bool:
    """Like "isinstance" but checking a structure against a
    schema that could be int, str, float or an S-expression
    [list S] or [dict A S]. where A is int, str, or float and
    S is a schema.
    """
    if schema in [int, float, str]:
        return isinstance(structure, schema)
    elif isinstance(schema, list):
        pass  # continued below
    else:
        raise ValueError(f"Ill-formed schema {schema} should be int, float, str," +
                         "[list element-schema], or [dict key-type value-schema]")

    # Schema is a list
    t, *components = schema
    if t not in [list, dict, "row"]:
        raise ValueError(f"Schema composite types are list and dict, not {t}")
    if t == list:
        if len(components) != 1:
            raise ValueError(f"Schema for list should have one component type, not {components}")
        if not isinstance(structure, list):
            return False
        comp_type = components[0]
        for item in structure:
            if not conforms(item, comp_type):
                return False
        return True
    elif t == "row":
        # Also a list, but instead of one homogenous element type, we expect
        # a schema for each column
        if not isinstance(structure, list) or  len(components) != len(structure):
            return False
        for i in range(len(components)):
            if not conforms(structure[i], components[i]):
                return False
        return True
    else:
        # t is dict
        if len(components) != 2:
            raise ValueError(f"dict schema should have two component types, for key and value, not {components}")
        key_type, value_type = components
        if key_type not in [int, str, float]:
            raise ValueError(f"dict schema key type should be str, int, or float, not {key_type}")
        if not isinstance(structure, dict):
            return False
        for k,v in structure.items():
            if not isinstance(k, key_type):
                return False
            if not conforms(v, value_type):
                return False
        return True


print(conforms({ 'a': [1, 2, 3], 'b': [3, 4]},  [dict, str, [list, int]]))        # Expect True
print(conforms({ 'a': [1, 2, 3], 'b': [3, 4]}, [list, [dict, str, int]]))         # Expect False
print(conforms([{"a": 1, "b": 2}, {"c": 3, "d": 4 }], [list, [dict, str, int]]))  # Expect True
print(conforms([{"a": 1, "b": 2}, {"c": 3, "d": 4 }], [dict, str, [list, int]]))  # Expect False
# Row schemata
print(conforms([5, "apple", [2, 3, 6]], 
               ["row",  int, str, [list, int]]))              # Expect  True
print(conforms([1, "alpha", 2, "beta", {"c": 3}], 
               ["row", int, str, int, str, [dict, str, int]])) # Expect True
print(conforms([1, "alpha", 2, "beta", {"c": 3}], 
               ["row", int, str, int, str, ["row", int]]))     # Expect False
```

4a.  Schema well-formedness checker.  The interesting thing about my 
solution is the way it maintains a boolean variable meaning "ok so 
far" so that it can find multiple errors.  How does it compare to 
yours?  Also note how a separate function `check_schema` starts and 
finishes the checking, to simplify the main recursive function 
`schema_well_formed`.  

```{code-cell} python3
Schema = type | list['Schema']

def schema_well_formed(schema: Schema, errors: list[str] | None = None) -> bool:
    """Check schema for being well-formed.
    Optional argument 'errors' receives a list of errors.
    """
    if errors is None:
        # Recall the default argument gotcha from the Binding and Scope chapter.
        # This is the standard workaround.
        errors = []  # Bind it now, not once at point of function definition
    # The rest of this is like a stripped-down version of 'conforms', but with
    # descriptions of issues encountered in the schema.
    if schema in [int, float, str]:
        return True
    elif isinstance(schema, list):
        pass  # continued below
    else:
        errors.append(f"Ill-formed schema {schema} should be int, float, str," +
                         "[list, element-schema], or [dict, key-type, value-schema]" +
                         "or ['row', col-schema, col-schema, ...]")
        return False


    # Schema is a list.  Boolean variasble "ok" is flipped to False when we encounter
    # any error, but we continue to collect all errors we can find.
    ok = True
    t, *components = schema
    if t not in [list, dict, "row"]:
        errors.append(f"Schema composite types are list, row, and dict, not {t} in {schema}")
        ok = False
    if t == list:
        if len(components) != 1:
            ok = False
            errors.append(f"Schema for list should have one component type, not {components}")
        comp_type = components[0]
        for comp_type in components:
            ok = schema_well_formed(comp_type, errors) and ok
    elif t == "row":
        # Also a list, but instead of one homogenous element type, we expect
        # a schema for each column
        for comp_type in components:
            ok = schema_well_formed(comp_type) and ok
    else:
        # t is dict
        if len(components) != 2:
            ok = False
            errors.append(f"dict schema should have two component types, for key and value, not {components}")
        if len(components) >= 1:
            key_type = components[0]
            if key_type not in [str, int, float]:
                ok = False
                errors.append(f"Valid key types for dict are str, int, float, not {key_type} in {schema}")
        for value_type in components[1:]:
            ok = schema_well_formed(value_type, errors) and ok
    return ok
    

def check_schema(schema: Schema):
    """Gathers and prints error messages plus overall well-formedness"""
    errors=[]
    if schema_well_formed(schema, errors):
        print(f"Good schema {schema}, errors={errors}")
    else:
        print(f"Schema {schema} rejected")
        print("Errors:")
        print("\n".join(errors))
        print()


check_schema([dict, [list, int], [list, int]])  # Bad, can't use list as dict key
check_schema([dict, str, [list, int]])          # Good
check_schema([list, [dict, str, int]])          # Good
check_schema(["row", int, str, int, str, [dict, str, int]]) # Good
check_schema(["row", int, str, int, str, ["row", int]])
```

4b.  Devise an approach to specify schemata for 
recursive data structures. This is an open-ended design challenge 
that you could approach in many different ways, to the extent that 
I don't know how to provide a "sample solution" like the more 
constrained exercises.  You might wish to look at how the
[JSON Schema](
https://json-schema.org/understanding-json-schema/structuring)
specification handles recursion (look for a heading "Recursion"), 
but ... honestly, I find that spec overcomplicated and not clearly 
documented.  I'd like you to do better. 

See what you can come up with, and then 
let's talk about it.  