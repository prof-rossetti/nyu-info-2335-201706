# Python Language Overview

### The `ipython` Module

Reference: http://ipython.readthedocs.io/en/stable/interactive/tutorial.html.

Once you have learned how to install modules using the `pip` package manager, you should be able to use it to install a third-party module called `ipython`, which provides some useful debugging capabilities.

First install `ipython`, if necessary:

```` sh
pip install ipython
````

After installing `ipython`, you can drop an interactive break-point on any line of code by inserting an `embed()` statement. Once you run the script, it will stop at the break-point to allow further investigation.

```python
from IPython import embed

for i in [1, 2, 3, 4, 5]:
    print(i)
    embed() if i == 4

#> 1
#> 2
#> 3
#> 4
#> Python 3.6.1 (default, Apr  4 2017, 09:40:51)
#> Type 'copyright', 'credits' or 'license' for more information
#> IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.
#>
#> In [1]: i
#> Out[1]: 4
#>
#> In [2]:
```

After you are done, type `exit` to quit the IPython session.
