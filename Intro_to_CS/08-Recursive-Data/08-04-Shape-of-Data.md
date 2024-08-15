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

# Addendum: The Shape of Data

The [treemap project](https://github.com/UO-CS210/Treemap) asks you 
to process _hierarchical_ data, represented in files in
[JSON](https://www.json.org/json-en.html) notation.  However, most
of the publicly available data you will find in the real world is
not represented this way.  You are more likely to encounter data in
some "flat" tabular format, like comma-separated values (CSV)
or relational database records.  If you want to use the implicit 
hierarchical structure of that data to create treemaps or in other 
ways, you will need to understand the difference between the
_information_ (semantic content) represented by those flat 
structures and the physical data structures used to represent them. 
With this distinction, you can devise conversions from the data 
structures available to you to the data structures you need for your 
computational task. 

## Semantic content vs representation

The same _semantic_ content may be represented in different ways in 
a concrete data structure.  For example, suppose we wanted a data 
structure to represent the data in 
[this table](https://ourworldindata.org/explorers/inequality?tab=table&time=1975..latest&facet=none&showSelectionOnlyInTable=1&country=BRA~USA~FRA~CHN&Data=World+Inequality+Database+%28Incomes+before+tax%29&Indicator=Share+of+the+richest+1%25) 
conveying the income share of the richest 1% of the population in 
different countries in 1975 and 2022: 

| Country or region | 1975   | 2022   | Absolute Change | Relative Change |
|-------------------|--------|--------|-----------------|-----------------|	
| China             | 6.52%  | 15.72% | +9.20 pp        | +141%           |
| France            | 8.20%  | 12.69% | +4.49 pp        | +55%            |           
| United States     | 10.43% | 20.87% | +10.44 pp       | +100%           |      

## Row-wise representation of tabular data

We could represent this data as a _list of lists_ by row or by column: 

```{code-cell} python3
columns = {"region": 0, "1975": 1, "2022": 2, "Chng_Abs": 3, 
"Chng_Rel": 4}
rows = [["China", .0652, .1572, .092, 1.41], 
        ["France", .082, .1269, .0449, .55],
        ["United States", .1043, .2087, .1044, 1.0]]
rows[2][columns["Chng_Abs"]]      
```

This row-wise organization might also be represented by a file with 
a line for each row.  The _comma-separated values_ (CSV) format 
used to exchange data with spreadsheet programs is a common example. 

```
Country or region,1975,2022,Absolute Change,Relative Change
China,6.52%,15.72%,+9.20 pp,+141%
France,8.20%,12.69%,+4.49 pp,+55%
United States,10.43%,20.87%,+10.44 pp,+100%
```

## Column-wise representation of tabular data

The same information could be represented _column-wise_: 

```{code-cell} python3
income_distribution = {
    "Region": ["China", "France", "United States"], 
    "1975": [.0652, .082, .1043],
    "2022": [.1572, .1269, .2087],
    "Chng_Abs": [.092, .0449, .1044],
    "Chng_Rel": [1.41, .55, 1.0]}
income_distribution["Chng_Abs"][2]
```

Column-wise representation is common in scientific and statistical 
computing.  It is the form used in [Pandas](https://pandas.pydata.org/)
dataframes, with each column represented as a [NumPy array](
https://numpy.org/doc/stable/reference/generated/numpy.array.html).

## Hierarchical data

Information is often categorized into a hierarchy.  Hierarchical 
part-whole relations might sometimes be fixed and immutable. 
More often they are at least partly arbitrary and 
mutable conveniences.  Consider, for example, the customary grouping of 
geographic regions into continents:  Europe and Asia are sometimes 
considered a single continent, Eurasia, but traditionally have often 
been considered separate continents, with the consequence that 
Ankara is grouped with Bangkok and not with Athens.  Statistical 
analyses by region may use the
[United Nations geoscheme](
https://en.wikipedia.org/wiki/United_Nations_geoscheme), while the
Internet Corporation for Assigned Names and Numbers uses
a different grouping into just 
[five major administrative regions](
https://meetings.icann.org/en/regions), for example classifying
American Samoa as part of North America.   

One can similarly find 
conflicting and shifting hierarchical groupings for languages, for 
biological taxa, and for social and cultural groups, among many 
other classification systems.  But as arbitrary as they may be, 
hierarchical grouping is often essential to making sense of the 
world.  We may quarrel with a _particular_ hierarchical organization,
but it is hard to argue with the usefulness of hierarchical 
organization for data analysis. 

Hierarchical part-whole relations can be represented by _nesting_ 
collection data structures in Python.  For example, 
[global causes of death in 2019](
https://ourworldindata.org/causes-of-death)
could be represented by nested dictionary structures: 

```{code-cell} python3
death_causes_2017 = {
   "Noncommunicable disease": { 
         "Cardiovascular" : 0.33, 
         "Cancers": 0.18, 
         "Respiratory": 0.07, 
         "Neurological": 0.039, 
         "Digestive": 0.045, 
         "Diabetes": 0.027, 
         "Other noncommunicable": 0.057
         }, 
   "Infectious disease": {
        "Pneumonia": 0.044, 
        "Diarrheal": 0.027, 
        "Tuberculosis": 0.02, 
        "HIV/AIDS": 0.015, 
        "Malaria": 0.011,
        "Other infectious": 0.021,
        },
   "Neonatal": 0.033,
   "Maternal": 0.004,
   "Nutritional": 0.004, 
   "Accidents": {
        "Transport accidents": 0.023,
        "Other accidents": 0.031
        },
   "Violence": {
        "Suicides": 0.013,
        "Homicides": 0.007,
        "Combat":  0.002,
        "Terrorism": 0.0005
   }
}
```

Such a structure may be represented in a file using a suitable data 
exchange format such as [JSON](https://www.json.org/json-en.html)
or [YAML](https://yaml.org/).  The Python snippet above is legal
JSON.  More often, we find hierarchical data that is "flattened"
into a tabular format.  For example, one free online converter from
JSON to comma-separated values (CSV) produces column headers like
`Infectious disease__Pneumonia` and `Infectious disease__Malaria` 
with a single row of numerical entries.  More typically we would find
one or more columns used for labels, and one or more
additional columns used for 
numerical values.

In a "flat" tabular representation (e.g., a CSV file), a row may 
represent a _path_ from the top-level category (e.g, "Infectious 
disease") through sub-categories (e.g., "Pneumonia"), one per column,
to one or more columns of numerical data.  For example, consider the 
following hierarchy, represented in tree form: 

![Beverage consumption in a hypothetical organization](
img/coffee-tree.svg)

Each path from the top of the tree to the amounts of coffee and tea 
consumed in a particular part of this imaginary organization (teams 
A1a, A1b, A2, and B) will be represented by one row in the tabular 
representation.   Intermediate levels A and A1 may be represented on 
separate rows: 

| Division | Subdivision | Team | Coffee | Tea |
|----------|-------------|------|--------|-----|
| A        |             |      |        |     |
|          | A1          |      |        |     |
|          |             | A1a  | 13     | 24  |
|          |             | A1b  | 19     | 17  |
|          | A2          |      | 7      | 12  |
| B        |             |      | 49     | 16  |

Alternatively, each row may contain the complete path:

| Division | Subdivision | Team | Coffee | Tea |
|----------|-------------|------|--------|-----|
| A        | A1          | A1a  | 13     | 24  |
| A        | A1          | A1b  | 19     | 17  |
| A        | A2          |      | 7      | 12  |
| B        |             |      | 49     | 16  |


In place of empty cells, as in subdivision and team for for _B_ 
above, a label may be repeated.  Applying this tactic to the 
mortality data, I have repeated "Neonatal" and "Maternal" in 
the "Cause" column: 

| Category                | Cause               | Proportion |
|-------------------------|---------------------|------------|
| Noncommunicable disease | Cardiovascular      | 0.33       |
| Noncommunicable disease | Cancers             | 0.18       |
| Noncommunicable disease | Respiratory         | 0.07       |
| Noncommunicable disease | Neurological        | 0.039      |
| Noncommunicable disease | Digestive           | 0.045      |
| Noncommunicable disease | Diabetes            | 0.027      |
| Noncommunicable disease | Other               | 0.057      | 
| Infectious disease      | Pneumonia           | 0.044      |
| Infectious disease      | Diarrheal           | 0.027      |
| Infectious disease      | Tuberculosis        | 0.02       |
| Infectious disease      | HIV/AIDS            | 0.015      |
| Infectious disease      | Malaria             | 0.011      |     
| Infectious disease      | Other               | 0.021      |
| Neonatal                | Neonatal            | 0.033      |
| Maternal                | Maternal            | 0.004      |
| Nutritional             | Nutritional         | 0.004      |
| Accidents               | Transport accidents | 0.023      |
| Accidents               | Other accidents     | 0.031      |
| Violence                | Suicides            | 0.013      | 
| Violence                | Homicides           | 0.007      |
| Violence                | Combat              | 0.002      |
| Violence                | Terrorism           | 0.0005     |


###  Indented lists 

An indented list is essentially equivalent to the flattened tabular 
format above, except that each label appears in a row by itself.
Equivalently, one can think of an indented list as shorthand for the 
nested dictionary structure as written above: 

- Noncommunicable disease
  - Cardiovascular: 0.33
  - Cancers: 0.18
  - Respiratory: 0.07 
  - Neurological: 0.039
  - Digestive:  0.045
  - Diabetes:  0.027 
  - Other noncommunicable:  0.057
- Infectious disease
    - Pneumonia: 0.044 
    - Diarrheal: 0.027
    - Tuberculosis: 0.02
    - HIV/AIDS: 0.015
    - Malaria: 0.011
    - Other: 0.021

- Neonatal: 0.033
- Maternal: 0.004
- Nutritional: 0.004 
- Accidents
     - Transport accidents: 0.023
     - Other accidents: 0.031
- Violence 
     - Suicides: 0.013
     - Homicides: 0.007
     - Combat:  0.002
     - Terrorism: 0.0005

### Other representations of hierarchical data

There are additional variations in representations that you will
encounter, including some that combine multiple tables that must be
"joined" to recover the hierarchy and/or a unified flat 
representation.  ("Join" is actually the name of an operation for
combining tables in a relational database.)  

It is often relatively straightforward to convert among 
representations of the same information, provided we make a clear 
distinction between the _semantic content_ of the data and
its representation.  

## Summary

The same _information_ (semantic content) may be represented with 
differently structured _data_.  External sources of
data (say, a spreadsheet or database) may not be organized in a way 
that is convenient for the computations we wish to perform.
Hierarchical information, in particular, is often represented in some 
"flat" structure (e.g., one or more tables) in which the 
hierarchical structure is implicit.  Often it is useful to 
reorganize such data as a first step in using it. 