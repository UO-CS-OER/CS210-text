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

# Indefinite loops

Loops that iterate through the elements of a 
collection are most common, but a loop can also be written to 
iterate as long as some condition holds.  Sometimes such a loop is 
useful even when we are iterating through collections, but not 
stepping through them at a pace of one item per iteration.  

## Example: Merging sorted lists

Suppose we want to _merge_ two lists that are already in 
sorted order.   While we could just concatenate and then sort short 
lists, that approach would not be good if the lists had 
millions of elements, or if instead of lists in memory we were 
reading two streams of network data and producing a merged output 
stream.  In that case we would need a loop that advances through 
just one or the other list on each iteration.  I'll illustrate with 
short lists: 

```{code-cell} python3
# My lists of precious and cheap rocks are each sorted
precious = ["amber", "amethyst", "diamond", "ruby"]
cheap = ["basalt", "granite", "pumice", "shale"]

# I want to combine them into one sorted list
# Start at the beginning of each list
i_precious = 0
i_cheap = 0

rocks = []
while i_precious < len(precious) and i_cheap < len(cheap):
    # We'll add one element to rocks on each iteration, 
    # but it could come from either the precious or the cheap list.
    if precious[i_precious] < cheap[i_cheap]:
        rocks.append(precious[i_precious])
        i_precious += 1
    else: 
        rocks.append(cheap[i_cheap])
        i_cheap += 1
        
# One of the lists, cheap or precious, has not been used up.
# One of these two loops will execute zero times, and one will 
# execute at least once. 
while i_precious < len(precious):
    rocks.append(precious[i_precious])
    i_precious += 1
while i_cheap < len(cheap):
    rocks.append(cheap[i_cheap])
    i_cheap += 1 

print(rocks)
```

## Breaking out

The condition for finishing and exiting a loop is not always in the 
`while` condition.  Sometimes it is more convenient to place the 
test somewhere in the body of the loop.  In that case we may write 
what appears to be an infinite loop with `while true:`, and use the 
`break` statement for the actual exit.  The code for combining lists 
of rocks could also be written with a single loop:  

```{code-cell} python3
i_precious = 0
i_cheap = 0

rocks = []
while True: 
    if i_precious < len(precious) and i_cheap < len(cheap):
        # Both lists have more items.  Take the smallest.
        if precious[i_precious] < cheap[i_cheap]:
            rocks.append(precious[i_precious])
            i_precious += 1
        else: 
            rocks.append(cheap[i_cheap])
            i_cheap += 1
    elif i_precious < len(precious): 
        # Only precious rocks remain.  Take the next. 
        rocks.append(precious[i_precious])
        i_precious += 1
    elif i_cheap < len(cheap):
        # Only cheap rocks remain.  Take the next. 
        rocks.append(cheap[i_cheap])
        i_cheap += 1
    else: 
        # Both lists are exhausted; we're done! 
        break

print(rocks)
```

Usually we want to be sure that the `break` statement will be 
executed after a predictable number of iterations.  In the loop 
above, we can argue that each iteration adds one to either `i_cheap` 
or `i_precious`, and that the total number of loop iterations will 
be exactly `len(precious) + len(cheap)`. 

In some other situations it may be much harder to determine how many 
times an indefinite loop could execute.  For example, we may be 
simulating a physical system until some condition holds, or trying 
different solutions to a puzzle. 
If we cannot be sure of eventually executing the `break` 
statement, we could replace the `while` with a `for` to set an 
upper limit on the number of iterations.  That is the approach we 
will take  in this week's project, in which the main loop is an 
attempt to improve an assignment of events to geographic clusters.
