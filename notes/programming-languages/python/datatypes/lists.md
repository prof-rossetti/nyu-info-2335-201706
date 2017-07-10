# Python Language Overview

## Lists

Reference:
  + https://docs.python.org/3/library/stdtypes.html#lists
  + https://docs.python.org/3/tutorial/datastructures.html?highlight=lists#more-on-lists

A List represents a numbered, ordered collection of items. A List may contain zero or more items. A list can contain items of any datatype, but as a best practice, all items in a list should share a datatype and structure:

```python
# DO:

[]
[1,2,3,4]
[100, 75, 33]
["fun", "times", "right?"]
[ {"a":1, "b":2}, {"a":5, "b":6}] # lists can contain dictionaries
[ [1,2,3], [4,5,6], [7,8,9]] # lists can be "nested" inside other lists

# DON'T:
[100, "fun"]
[ {"a":1, "b":2}, {"x":5, "z":6}]
```

Like other languages, individual list items can be accessed by their index. List item indices are zero-based, meaning the index of the first list item is 0.

```python
arr = ["a", "b", "c", "d"]
arr[0] #> "a"
arr[1] #> "b"
arr[2] #> "c"
arr[3] #> "d"
arr[4] #> IndexError: list index out of range

arr.index("a") #> 0
arr.index("b") #> 1
arr.index("c") #> 2
arr.index("z") #> -1 (applies to any item not found in the list)
```

Equality operators apply:

```python
[1,2,3] == [1,2,3] #> True
[1,2,3] == [3,2,1] #> False
```

Inclusion operators apply:

```python
arr = [1,2,3,4,5]

3 in arr #> True

3 not in arr #> False
```

Common list functions and operators include the following built-in Python functions:

```python
arr = [6,3,9,7]

len(arr) #> 4

min(arr) #> 3

max(arr) #> 9
```

Add an element to the end of a list:

```python
arr = ["a", "b", "c", "d"]
arr.append("e") # this is a mutating operation
arr #> ["a", "b", "c", "d", "e"]
```

Concatenate two lists:

```python
arr = ["a", "b", "c", "d"]
arr2 = ["x", "y", "z"]
arr3 = arr + arr2
arr3 #> ["a", "b", "c", "d", "x", "y", "z"]
```

Remove duplicate values in a list by converting it to another datatype called a "Set" and then converting it back to a "List":

```python
arr = [1,2,2,2,3]
arr2 = list(set(arr))
arr2 #> [1, 2, 3]

list(set(["hello", "hello", "hello"])) #> ['hello']
```

### Sorting

Sort a list:

```python
arr = [6,3,8]
arr.sort() # this is mutating
arr #> [3, 6, 8]

arr.reverse() # this is mutating
arr #> [8, 6, 3]
```

If you have a list of dictionaries, you should be able to sort it based on dictionary values:

```python
teams = [
    {"city": "New York", "name": "Yankees"},
    {"city": "New York", "name": "Mets"},
    {"city": "Boston", "name": "Red Sox"},
    {"city": "New Haven", "name": "Ravens"}
]

def team_name(team):
    return team["name"]

def sort_by_hometown(team):
    return team["city"]

def sort_special(team):
    return team["city"] + "-" + team["name"]

teams2 = sorted(teams, key=team_name)
teams2 #> [{'city': 'New York', 'name': 'Mets'}, {'city': 'New Haven', 'name': 'Ravens'}, {'city': 'Boston', 'name': 'Red Sox'}, {'city': 'New York', 'name': 'Yankees'}]

teams3 = sorted(teams, key=sort_by_hometown)
teams3 #> [{'city': 'Boston', 'name': 'Red Sox'}, {'city': 'New Haven', 'name': 'Ravens'}, {'city': 'New York', 'name': 'Yankees'}, {'city': 'New York', 'name': 'Mets'}]

teams4 = sorted(teams, key=sort_special)
teams4 #> [{'city': 'Boston', 'name': 'Red Sox'}, {'city': 'New Haven', 'name': 'Ravens'}, {'city': 'New York', 'name': 'Mets'}, {'city': 'New York', 'name': 'Yankees'}]
```

Alternatively for simple attribute-based sorting, you could use the `operator` module's `itemgetter()` function, for example:

```python
import operator

teams = [
    {"city": "New York", "name": "Yankees"},
    {"city": "New York", "name": "Mets"},
    {"city": "Boston", "name": "Red Sox"},
    {"city": "New Haven", "name": "Ravens"}
]

teams = sorted(teams, key=operator.itemgetter('city'))
teams #> [{'city': 'Boston', 'name': 'Red Sox'}, {'city': 'New Haven', 'name': 'Ravens'}, {'city': 'New York', 'name': 'Yankees'}, {'city': 'New York', 'name': 'Mets'}]
```


### Iteration

Reference:

  + https://docs.python.org/3/tutorial/datastructures.html?#list-comprehensions
  + https://docs.python.org/3/tutorial/datastructures.html?highlight=lists#list-comprehensions
  + https://docs.python.org/3/tutorial/controlflow.html#for-statements

A list can be iterated, or "looped" using a `for ... in ...` statement:

```python
for letter in ["a", "b", "c", "d"]:
    print(letter)

#> a
#> b
#> c
#> d
```

A common pattern is to loop through one list to populate the contents of another:

```python
arr = [1, 2, 3, 4]
arr2 = []

for i in arr:
  arr2.append(i * 100)

arr #> [1, 2, 3, 4]
arr2 #> [100, 200, 300, 400]
```

Lists can be looped "in-place" using Python's built-in `map()` function. The `map()` function takes two parameters. The first parameter is the name of a pre-defined function to perform on each item in the list. The function should accept a single parameter representing a single list item. The second parameter is the actual list to be operated on.

```python
arr = [1, 2, 3, 4]

def enlarge(num):
    return num * 100

arr2 = map(enlarge, arr)

# Python 2.x:
arr2 #> [100, 200, 300, 400]

# Python 3.x:
arr2 #> <map object at 0x10c62e710>
list(arr2) #> [100, 200, 300, 400]
```

> NOTE: remember to use the `return` keyword in your mapping function!

























### Filtering

Reference: https://docs.python.org/2/library/functions.html#filter.

Use the `filter()` function to select a subset of items from a list - only those items matching a given condition. The filter function accepts the same parameters as the `map()` fuction:

```python
arr = [1,2,4,8,16]

def all_of_them(i):
    return True # same as ... return i == i

def equals_two(i):
    return i == 2

def greater_than_two(i):
    return i > 2

def really_big(i):
    return i > 102

# Python 2.x:
filter(all_of_them, arr) #> [1, 2, 4, 8, 16]
filter(equals_two, arr) #> [2]
filter(greater_than_two, arr) #> [4, 8, 16]
filter(really_big, arr) #> []

# Python 3.x:
filter(all_of_them, arr) #> <filter at 0x103fa71d0>
list(filter(all_of_them, arr)) #> [1, 2, 4, 8, 16]
list(filter(equals_two, arr)) #> [2]
list(filter(greater_than_two, arr)) #> [4, 8, 16]
list(filter(really_big, arr)) #> []
```

> Note: the `filter()` function returns a list, even if it is empty or only contains one item.

If your list is full of [dictionaries](dictionaries.md), you can `filter()` based on their attribute values:

```python
teams = [
    {"city": "New York", "name": "Yankees"},
    {"city": "New York", "name": "Mets"},
    {"city": "Boston", "name": "Red Sox"},
    {"city": "New Haven", "name": "Ravens"}
]

def yanks(obj):
    return obj["name"] == "Yankees"

def from_new_york(obj):
    return obj["city"] == "New York"

def from_new_haven(obj):
    return obj["city"] == "New Haven"

def from_new_something(obj):
    return "New" in obj["city"]

# Python 2.x:
filter(yanks, teams) #> [{...}]
filter(from_new_york, teams) #> [{...}, {...}]
filter(from_new_haven, teams) #> [{...}]
filter(from_new_something, teams) #> [{...}, {...}, {...}]

# Python 3.x:
list(filter(yanks, teams)) #> [{...}]
list(filter(from_new_york, teams)) #> [{...}, {...}]
list(filter(from_new_haven, teams)) #> [{...}]
list(filter(from_new_something, teams)) #> [{...}, {...}, {...}]
```

If you need to implement complex filtering conditions, consider using a list comprehension, or consider writing out your function the long way:

```python
teams = [
    {"city": "New York", "name": "Yankees"},
    {"city": "New York", "name": "Mets"},
    {"city": "Boston", "name": "Red Sox"},
    {"city": "New Haven", "name": "Ravens"}
]

# using a list comprehension
def teams_from(city):
  return [team for team in teams if team["city"] == city]

# the long way
def teams_from2(city):
  matches = []
  for team in teams:
      if team["city"].upper() == city.upper():
          matches.append(team)
  return matches

teams_from("New York")
teams_from2("New York")
```

Reference the [`itertools` module](../modules/itertools.md) for additional operations.
