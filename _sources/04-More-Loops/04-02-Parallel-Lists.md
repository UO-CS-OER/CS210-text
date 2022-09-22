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

# Parallel Lists

Here are two ways we could represent the ten largest cities in 
Oregon, along with their populations.  We can think of the data as a 
table with a row for each city, one column for city names, and one 
column for populations. 

We could make a single list of tuples, like this: 

```{code-cell} python3
or_cities_pops = [
    ('Portland', 641_162), 
    ('Salem', 177_723),
    ('Eugene', 175_096),
    ('Gresham', 113_103),
    ('Hillsboro', 106_633),
    ('Bend', 102_059),
    ('Beaverton', 98_216),
    ('Medford', 86_367),
    ('Springfield', 62_256),
    ('Corvallis', 59_864)
]
```

This seems fine, but suppose I notice that the populations are 
somewhat out of date.  I might want to add 10% to each population.  
I might even already have a function that adds 10% to each element 
of a list of numbers, but I can't apply that function to this list 
of tuples.  Any function that works on this data has to "know about" 
the (name, population), extracting the population component and 
building a new tuple with the updated population.  Alternatively, I 
could change from a list of tuples to a list of lists to enable 
direct update of the populations, but the function would still need 
to know about the structure of each row. 

Instead of putting all the information in one list, I could separate 
it into two lists.  If we think of the data as being a table with
a row for each city and columns for names and populations,
the individual lists could represent columns of data: 

```{code-cell} python3
or_cities_names = [ 
   'Portland', 'Salem', 'Eugene', 'Gresham', 'Hillsboro', 
   'Bend', 'Beaverton', 'Medford', 'Springfield', 'Corvallis' ]
   
or_cities_pops = [
    641_162, 177_723, 175_096, 113_103, 106_633, 
    102_059, 98_216, 86_367, 62_256, 59_864 ]
```

Now the first element of `or_cities_names` corresponds to the first 
element of `or_cities_pops`, the second elements correspond, and so 
on.  We call these _parallel arrays_ or, in Python, _parallel lists_,
because they "line up".


The advantage of parallel lists is that it is easier to do 
something to all the elements of one column, as long as I don't
change the order of elements in a column.  
Scientific computing packages like scipy and statistical computing 
packages like Python's Pandas typically keep numerical data in parallel 
arrays for this reason. 
The disadvantage of parallel lists is that if I want to do 
something to a whole row, I need an element from each of the column 
lists.  

Let's give these cities some 
population growth.  We will be altering only the population column, 
so we can write a function that takes a list of numbers and returns 
a corresponding list of numbers, in the same order: 

```{code-cell} python3
def nth_increase(n: int, col: list[int]) -> list[int]:
    """Return list with integers 1/n higher than col"""
    result = []
    for el in col: 
        result.append(el + el//n)
    return result
    
# 10% is 1/10
or_cities_pops = nth_increase(10, or_cities_pops)

for i in range(len(or_cities_names)):
    print(or_cities_names[i], or_cities_pops[i])
```

With a parallel arrays structure, the `nth_increase` function can 
apply to _any_ list of integers.  It doesn't have to be specific to 
city populations.  In the project associated with this chapter, we will use parallel 
lists so that we can replace a whole column of a table with a 
function that handles just that column. 

## Zip: From columns to rows 

While printing each row is a little more tedious with organization 
by columns, 
there is a simple workaround:  Python 
provides a function `zip` for combining parallel lists into a single 
sequence of tuples.

```{code-cell} python3
for row in zip(or_cities_names, or_cities_pops):
    print(row)
```

The `zip` function will come in handy if we want to change the 
order of rows in the table.  For example, suppose we wanted to print 
the table of populations in alphabetical order, rather than in order 
of population.  We need to sort them, but we can't sort the 
individual columns.  A list of `(name, population)` pairs will be 
sorted first by name, using population only as a tie-breaker. 

```{code-cell} python3
rows = zip(or_cities_names, or_cities_pops)
by_name = sorted(rows)
for row in by_name: 
  print(row)
```

```{Note}
If you print `rows` in the example above, you will find that it 
is not actually a list, but rather a _zip object_.  Python does
not produce the list of tuples all at once, but 
rather one row at a time as needed.  This is called _laziness_.
We can mostly ignore laziness when 
we use access all the rows in prder, as the `sorted` function 
does.  It will cause a problem if we try to access row _n_ out of 
order, e.g., `by_row[5]`.   Later (but not in this course) you may 
want to zip together extremely long or even _infinite_ sequences, using 
another cool Python feature called _generators_.  Producing an 
infinite list would be slower if it were not done lazily.
```

## Indexes as references

When we organize our data in parallel lists, we often use the index 
of an item as a reference to the whole row.  For example, suppose 
the table were in order by city name, like `by_name` above, and 
suppose we wanted to print the name of the city with the highest 
population.  We could write a function to find the largest population, 
but instead of returning that population, we would return the _index 
of_ that item.  

```{code-cell} python3
def max_index(nums: list[int]):
    """Returns the index of the maximum value in nums"""
    i_max = 0
    v_max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > v_max: 
            v_max = nums[i]
            i_max = i
    return i_max
```

Then we can use this _index_ to print any column in the selected row. 

```{code-cell} python3
city_names = [
  'Beaverton', 'Bend', 'Corvallis', 'Eugene', 
  'Gresham', 'Hillsboro', 'Medford', 'Portland',
  'Salem', 'Springfield']
city_pops = [
    108037, 112264, 65850, 192605,
    124413, 117296, 95003, 705278, 
    195495, 68481]
    
big_city = max_index(city_pops)

print(city_names[i], city_pop[i])
```

We will use this technique in our[clustering project](
https://github.com/UO-CS210/wildfire
).   We will search one list for the _index of_ the cluster to which 
a fire record should belong, then use that index to add the fire to 
the cluster.  
