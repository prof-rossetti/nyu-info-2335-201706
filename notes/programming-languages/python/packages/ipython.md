# Python Language Overview

## The `ipython` Package

Reference:

  + http://ipython.readthedocs.io/en/stable/interactive/tutorial.html
  + https://github.com/ipython/ipython

> NOTE: The `ipython` package only works with Python 3.x.

Once you have learned how to install packages using the `pip` package manager, you should be able to use it to install a third-party module called `ipython`, which provides some useful debugging capabilities.

First install `ipython`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install ipython

# All others:
pip install ipython
````

Use the `ipython` package from the command line to enter into an interactive console, or from within a script to debug it using an interactive console.

### Interactive Console with `ipython`

From the command-line:

```shell
ipython
#> Python 3.6.1 (default, Apr  4 2017, 09:40:51)
#> Type 'copyright', 'credits' or 'license' for more information
#> IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.
#>
#> In [1]: 2+2
#> Out[1]: 4
#>
#> In [2]:
```

### Debugging Scripts with `ipython`

Drop an interactive break-point onto any line in a Python script by inserting an `embed()` statement. Once you run the script, it will stop at the break-point to allow further investigation.

```python
from IPython import embed # the capitalization of IPython matters

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
