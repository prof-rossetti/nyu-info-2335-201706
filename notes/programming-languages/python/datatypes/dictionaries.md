# Python Language Overview

## Dictionaries

Reference:

  + https://docs.python.org/3/library/stdtypes.html#dict
  + https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
  + https://docs.python.org/3/tutorial/datastructures.html#dictionaries
  + https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

Many programming languages provide an "associative array" datatype  which provides an opportunity to create objects with named attributes. In this way, an associative array is similar to a row in a CSV-formatted spreadsheet or a record in a database, where the associative array's "keys" represent the column names and its "values" represent the cell values. associative arrays are said to have "key/value" pairs, where the "key" represents the name of the attribute and the "value" represents the attribute's value.

Python's implementation of the associative array concept is known as a "dictionary". A Python dictionary comprises curly braces (`{}`) containing one or more key/value pairs, with each key separated from its value by a colon (`:`) and each key/value pair separated by a comma (`,`).

If you are familiar with JavaScript "Objects" (JSON) or Ruby "Hashes", the concept is the same. If you need to convert a Python dictionary to JSON, reference the [`json` module](../modules.json.md).

```python
{}
{"a":1, "b":2, "c":3}
{"a":1, "b":2, "c":3, "fruits":["apple","banana","pear"]} # dictionaries can contain lists
{"first":"Santa", "last":"Claus", "message":"Ho Ho Ho"}
```

Access individual object elements by their key:

```python
person = {
    "first": "Santa",
    "last": "Claus",
    "message": "Ho Ho Ho",
    "stops": ["New York", "Denver", "San Francisco"]
}

person["first"] #> "Santa"
person["last"] #> "Claus"
person["message"] #> "Ho Ho Ho"
person["stops"] #> ["New York", "Denver", "San Francisco"]
person["stops"][1] #> "Denver" (an array is still an array, even if it exists inside a dictionary!)
```

Add or remove items from an object:

```python
person = {
    "first": "Santa",
    "last": "Claus",
    "message": "Ho Ho Ho",
    "stops": ["New York", "Denver", "San Francisco"]
}

person["wife"] = "Mrs. Claus"

del person["stops"]

person #> {'first': 'Santa', 'last': 'Claus', 'message': 'Ho Ho Ho', 'wife': 'Mrs. Claus'}
```

Make use of built-in Dictionary methods for easier data-processing:

```python
person = {
    "first": "Santa",
    "last": "Claus",
    "message": "Ho Ho Ho",
    "stops": ["New York", "Denver", "San Francisco"]
}

person.keys() #> dict_keys(['first', 'last', 'message', 'stops'])
list(person.keys()) #> ['first', 'last', 'message', 'stops']

person.values() #> dict_values(['Santa', 'Claus', 'Ho Ho Ho', ['New York', 'Denver', 'San Francisco']])
list(person.values()) #> ['Santa', 'Claus', 'Ho Ho Ho', ['New York', 'Denver', 'San Francisco']]

person.items() #> dict_items([('first', 'Santa'), ('last', 'Claus'), ('message', 'Ho Ho Ho'), ('stops', ['New York', 'Denver', 'San Francisco'])])

for k, v in person.items():
    print("KEY:", k, "... VALUE:", v)

#> KEY: first ... VALUE: Santa
#> KEY: last ... VALUE: Claus
#> KEY: message ... VALUE: Ho Ho Ho
#> KEY: stops ... VALUE: ['New York', 'Denver', 'San Francisco']
```

After you have studied list iteration, mapping, and filtering, if you have a list full of dictionaries, you should be able to sort it based on dictionary values:

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
