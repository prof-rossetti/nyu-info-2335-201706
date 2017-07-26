# Python Language Overview

## The `code` Module

Reference: https://docs.python.org/3/library/code.html.

If using the `code` module, drop an interactive break-point on any line of code by inserting a `code.interact(local=locals())` statement. Once you run the script, it will stop at the break-point to allow further investigation:

```python
import code

for i in [1, 2, 3, 4, 5]:
    print(i)
    if i == 4:
        code.interact(local=locals())

#> 1
#> 2
#> 3
#> 4
#> Python 3.6.1 (default, Apr  4 2017, 09:40:51)
#> [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
#> Type "help", "copyright", "credits" or "license" for more information.
#> (InteractiveConsole)
#> >>> i
#> 4
#> >>>
```

After you are done, type `exit()` to quit the session.
