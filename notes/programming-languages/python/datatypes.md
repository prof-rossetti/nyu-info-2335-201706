# Python Language Overview

## Datatypes

Use the `type()` function to return the type of any object:

```python
type("Hello") #> <type 'str'>
type("100") #> <type 'str'>
type(100) #> <type 'int'>
type(0.45) #> <type 'float'>
type(True) #> <type 'bool'>
type(False) #> <type 'bool'>
type(None) #> <type 'NoneType'>
type({"a":1, "b":2, "c":3}) #> <type 'dict'>
type([1,2,3]) #> <type 'list'>

"Hello".__class__.__name__ #> 'str'
{"a":1}.__class__.__name__ #> 'dict'
[1,2,3].__class__.__name__ #> 'list'
```

Here are a few examples of how to convert between datatypes:

```python
# convert strings to numbers:
int("500") #> 500
float("0.45") #> 0.45

# convert numbers to strings:
str(100) #> "100"
str(0.45) #> "0.45"
```

See the subsections below for more information about the most prevalent data types:

  + [Booleans](datatypes/booleans.md)
  + [Strings](datatypes/strings.md)
  + [Numbers](datatypes/numbers.md)
  + [Dates and Times](datatypes/dates-and-times.md)
  + [Arrays, a.k.a "Lists"](datatypes/lists.md)
  + [Objects, a.k.a "Dictionaries"](datatypes/dictionaries.md)

<hr>

## Further Exploration

Pass an object into the `dir()` function to see what methods you can call on that object.

Pass an object into the `help()` function to view documentation for that type of object.
