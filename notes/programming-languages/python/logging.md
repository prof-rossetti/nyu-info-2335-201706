# Python Language Overview

## Logging

Output, or "log" an object using the `print` statement. This works from inside an interpreter or a script. When scripting, you will be able to see the logs from the command-line when the script executes.

```python
print("HELLO WORLD") #> HELLO WORLD
```

Don't be confused if you see the parenthesis omitted:

```python
print "HELLO WORLD" #> HELLO WORLD
```

You can even log multiple objects, including various types of objects:

```python
print "HELLO", "WORLD" #> HELLO WORLD
print "HELLO", "WORLD", 5, {'a': 1, 'c': 3, 'b': 2} #> HELLO WORLD 5 {'a': 1, 'c': 3, 'b': 2}
```
