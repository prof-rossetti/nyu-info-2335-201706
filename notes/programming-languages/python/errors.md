# Python Language Overview

## Errors

Reference:

  + https://docs.python.org/3/library/exceptions.html#bltin-exceptions
  + https://docs.python.org/3/tutorial/errors.html

### Raising Errors

```python
options = ["rock", "paper", "scissors"]

choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

if choice in options:
    print("YOU CHOSE", choice)
else:
    raise ValueError("OOPS - Please type 'rock', or 'paper', or 'scissors' (without using using quotation marks).")

# the choice is yours...
```

### Handling Errors

```python
try:
  raise RuntimeError("Hello")
  print("EVERYTHING IS GOING FINE")
except RuntimeError:
  print("OOPS - MY ERROR")

#> OOPS - MY ERROR
```
