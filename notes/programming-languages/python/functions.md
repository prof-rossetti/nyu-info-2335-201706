# Python Language Overview

## Functions

Reference:

  + https://docs.python.org/3/tutorial/controlflow.html

Use a function to define your own custom, re-usable operation. Like in other languages, Python functions must first be defined before they can be invoked (or called).

Define a function:

```python
def do_stuff(): # NOTE: the trailing parentheses are required.
    print("DOING STUFF HERE!")
```

Invoke the function:

```python
do_stuff() # NOTE: the trailing parentheses are important. If they are omitted, the function will accessed but not be invoked.
```

If you try to invoke a function before or without defining it, you will see an error like `NameError: name 'do_stuff' is not defined`.

You might see some functions invoked by themselves (e.g. `do_stuff()`) while others are invoked on objects (e.g. `some_object.do_something_else()`). These two approaches illustrate the difference between "functional" and "object-oriented" programming, respectively. To find a comprehensive list of functions available to be called on any given type of object, reference the documentation for that type of object.

### Parameters

Some functions accept parameters which can be passed to the function during its invocation. A function's parameters must be configured during the function's definition.

#### Single Parameter

Define a function with a parameter:

```python
def do_stuff_with_param(message):
  print(message)
```

In this case, `message` is the name of the function's parameter. Invoke it like so:

```python
do_stuff_with_param("HELLO!")
```

#### Multiple Parameters

Define a function with multiple parameters:

```python
def do_stuff_with_params(message, first_name, last_name):
    print(message, "says", first_name, last_name)
```

In this case, `message`, `first_name` and `last_name` are the names of the function's parameters. Invoke it like so:

```python
do_stuff_with_params("HO! HO! HO!", "Santa", "Claus")
```

> PRO TIP: if your function uses more than a handful of parameters, especially if some of them are optional, consider re-configuring the function to accept a single dictionary parameter that contains multiple keys, with the key names corresponding to the names of the original parameters.
>
>     def do_stuff_with_params(obj):
>         print(obj["message"], "says", obj["first_name"], obj["last_name"])
>
>     person = {"first_name": "Santa", "last_name": "Claus", "message": "HO! HO! HO!"}
>
>     do_stuff_with_params(person)
>


### Returns

Use the `return` keyword when you want to make use of the value returned by the function:

```python
def calculate_area(length, height):
  length * height

area = calculate_area(4, 2)
print(area) #> None
```

```python
def calculate_area(length, height):
  return length * height

area = calculate_area(4, 2)
print(area) #> 8
```
