# Python Language Overview

## Classes

Reference:

  + https://docs.python.org/3/tutorial/classes.html
  + https://docs.python.org/3/tutorial/classes.html#class-objects
  + https://www.tutorialspoint.com/python/python_classes_objects.htm

A **class** is a representation of one or more objects which share the same or similar properties. Each class is like its own custom data type with properties defined by the developer.

In Python, class definition requires a specific function called `__init__()` to initialize, or create a new member of the object class.

### Usage

#### Definition

To setup this example, create a new directory on your Desktop called `class-time` or something. Inside it, create a new file called `baseball_team.py` and place inside the following contents:

```python
class BaseballTeam():
  """
  bt = BaseballTeam({"city": "Little Town", "name": "Tots", "league":"little", "players": ["JJ", "Zhang", "Margaret", "Ryan", "Joey"]})
  """ # optional docstring

  def __init__(self, params):
    self.city = params["city"]
    self.name = params["name"]
    self.league = params["league"]
    self.players = params["players"]

  def full_name(self):
    return self.city + " " + self.name

  #
  # ... probably more instance methods down here ...
  #

```

#### Instantiation

After defining an object class, create a new member of that object class. This is called "instantiating", or "initializing", or creating an "instance" of the object class.

Normally we would reference the class from another file by importing it (e.g. `from baseball_team import BaseballTeam`), but for example purposes, place the following contents at the bottom of the `baseball_team.py` script:

```python
attributes = {
    "city": "New York",
    "name": "Yankees",
    "league": "major",
    "players": ["Jeter", "Mariano", "Mantle", "Babe"]
}
type(attributes) #> <class 'dict'>

bt = BaseballTeam(attributes)
type(bt) #> __main__.BaseballTeam

bt.name #> 'Yankees'

bt.city #> 'New York'

bt.players #> ['Jeter', 'Mariano', 'Mantle', 'Babe']

bt.full_name() #> 'New York Yankees'
```

<hr>

<hr>

## Inheritance

Reference: https://docs.python.org/3.1/tutorial/classes.html#inheritance

It is possible for a class to "inherit" its properties and functionality from its "parent" class while at the same time retaining its own specific characteristics.

### Usage

To setup this example, create a new file in the `class-time` directory called something like `inheritance_example.py` or `team.py`. Inside it, place the following contents:

#### Definition

```python
#
# PARENT CLASS DEFINITION
#

class Team():

  def __init__(self, params):
    self.city = params["city"]
    self.name = params["name"]
    self.sport = params["sport"]
    self.league = params["league"]
    self.players = params["players"]

  def full_name(self):
    return self.city + " " + self.name

#
# CHILD CLASS DEFINITION
#

class BaseballTeam(Team):

    def __init__(self, params):
        params["sport"] = "baseball"
        super().__init__(params) # equivalent to: `Team.__init__(self, params)`

```

Normally, each class definition would exist inside its own file, but we are defining both in the same file for example purposes.

#### Instantiation

Normally we would reference the class from another file by importing it, but for example purposes, place the following contents at the bottom of the script you used to set up your inheritance example:

```python
attributes = {
    "city": "New York",
    "name": "Yankees",
    "league": "major",
    "players": ["Jeter", "Mariano", "Mantle", "Babe"]
}

bt = BaseballTeam(attributes)

type(bt) #> __main__.BaseballTeam

bt.name #> 'Yankees'

bt.city #> 'New York'

bt.players #> ['Jeter', 'Mariano', 'Mantle', 'Babe']

bt.full_name() #> 'New York Yankees'
```

In this inheritance example, the reason why an instance of the `BaseballTeam` class has the `full_name()` property is because that property was defined in the parent class (`Team`).
