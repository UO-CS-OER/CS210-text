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

# Other Nested Structures

Nested lists are by far the most common recursive data 
structure (aside from
[tree structures built from programmer-defined classes](
https://uo-cs-oer.github.io/CS211-text/03_Recursion/03_1_Recursion.html),
which we will introduce in Part II of this text).  However, other
collection data types in Python  including lists, dictionaries, and 
tuples, can also be nested.  

## Data exchange languages 

We often need to transmit data between applications that may not be 
coded in the same programming language.  For example, the "server 
side" of a web application, which runs within a web server or acts 
as a web server itself, must transmit and receive data from the 
"client side" of the application, which is typically a JavaScript 
program running within a browser.  While any particular message (say,
a weather report) may have a fixed and predictable content, the 
transmission is almost always in a _data exchange format_ which is 
defined by a recursive data structure.  

Among the most common data exchange formats in use today is 
JavaScript Object Notation (JSON).  The first
[example offered at json.org](https://json.org/example.html)
looks (and is semantically) identical to a nested structure of 
`dict`s in Python: 

```json
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
```

The [Mozilla Developer Network (MDN)
introduction to JSON](
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON),
which uses JavaScript terminology (e.g., a "objects" rather than "dicts")
offers an example that (in Python terms) nests lists within dictionaries, and 
dictionaries within lists: 

```json
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
```

The [Python `json` module](https://docs.python.org/3/library/json.html)
can automatically convert JSON text to a nested structure of 
dictionaries and lists, and vice versa.  JSON libraries exist for 
many other programming languages as well. 

Our [treemap project](https://github.com/UO-CS210/Treemap),
introduced at the end of this chapter, reads JSON inputs and uses 
nested dictionaries and lists to represent groupings of student 
majors according to the divisions of a university.

## Recursive Dictionary Example

Suppose we represented
[a business organization](https://www.imdb.com/title/tt0086856/)
using nested dictionaries, like this: 

```python
Yoyodyne = {
    "Manager": "John Whorfin",
    "Enemy": "Banzai Institute",
    "Divisions": {
        "Dimensional Engineering": { 
            "Manager": "John O'Connor",
            "Staff": ["John Gomez", "John Yaya"]
        },
        "Operations": {
            "Manager": "John Bigboote",
            "Staff": ["John Small Berries", "John Many Jars"]
        }
    }
}
```
Suppose that we wished to build a function that, given the name of
a staff member, returned that member's chain of managers.  We could 
look in each level of organization searching for the staff member's 
name: 

```python
OrgChart = str |  list[str] | dict[str, 'OrgChart']

def is_employed_at(person: str, org: OrgChart) -> bool:
    """Returns True iff person is found somewhere in org.

    >>> is_employed_at("John Many Jars", Yoyodyne)
    True
    >>> is_employed_at("John O'Connor", Yoyodyne)
    True
    >>> is_employed_at("Buckaroo Banzai", Yoyodyne)
    False
    >>> is_employed_at("Dr. Emilio Lizardo", Yoyodyne)
    False
    """
    if isinstance(org, str):
        return person == org
    if isinstance(org, list):
        return person in org
    if isinstance(org, dict):
        for role, division in org.items():
            if is_employed_at(person, division):
                return True
        return False
    # Defensive programming --- indicate malformed data structure
    assert False, f"Not a valid OrgChart: {org}"
```


