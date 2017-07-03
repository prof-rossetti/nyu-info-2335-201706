# Python

## Functions

Reference:

  + https://docs.python.org/3/tutorial/controlflow.html

Like in other languages, Python functions must first be defined before they can be invoked (or called).

Define a function:

```python
def do_stuff(): # NOTE: the trailing parentheses are required.
    print "DOING STUFF HERE!"
```

Invoke the function:

```python
do_stuff() # NOTE: the trailing parentheses are important. If they are omitted, the function will not be invoked.
```

If you try to invoke a function before or without defining it, you will see an error like `NameError: name 'do_stuff' is not defined`.

You might see some functions invoked by themselves (e.g. `do_stuff()`) while others are invoked on objects (e.g. `some_object.do_something_else()`). Many of the examples in this language overview involve invoking built-in functions on certain types of objects. To find a comprehensive list of functions available to be called on any given type of object, reference the documentation for that type of object.

### Parameters

Some functions accept parameters which can be passed to the function during its invocation. A function's parameters must be configured during the function's definition.

#### Single Parameter

Define a function with a parameter:

```python
def do_stuff_with_param(message):
  print message
```

In this case, `message` is the name of the function's parameter. Invoke it like so:

```python
do_stuff_with_param("HELLO!")
```

#### Multiple Parameters

Define a function with multiple parameters:

```python
def do_stuff_with_params(message, first_name, last_name):
    print message, "says", first_name, last_name
```

In this case, `message`, `firstName` and `lastName` are the names of the function's parameters. Invoke it like so:

```python
do_stuff_with_params("HO! HO! HO!", "Santa", "Claus")
```





### Returns

Use the `return` keyword when you want to make use of the value returned by the function:

```python
def calculate_area(length, height):
  length * height

area = calculate_area(4, 2)
print area #> None
```

```python
def calculate_area(length, height):
  return length * height

area = calculate_area(4, 2)
print area #> 8
```
