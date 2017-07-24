# Python Language Overview

## The `pytest` Package

Reference:

  + https://github.com/pytest-dev/pytest/
  + https://docs.pytest.org/en/latest/
  + https://docs.pytest.org/en/latest/getting-started.html#our-first-test-run
  + https://docs.pytest.org/en/latest/goodpractices.html
  + https://docs.pytest.org/en/latest/usage.html#dropping-to-pdb-python-debugger-on-failures
  + http://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/#py-test

### Installation

Install `pytest`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install pytest

# All others:
pip install pytest
````

### Usage

To setup these examples, create a new directory on your Desktop called `testing123` and navigate there from your command line, then create files called `my_script.py` and `my_test.py` and place inside the following contents, respectively:

```python
# this is the my_script.py
def enlarge(i):
    return i * 100
```

```python
# this is the my_test.py

from my_script import * # load accompanying code (i.e. the `enlarge()` function to avoid NameError: name 'enlarge' is not defined

def test_enlarge(): # name this function anything, but hopefully something corresponding to the function it is testing
    result = enlarge(3)
    assert result == 300
```

Once you have setup the example, run `pytest` from the `testing123` directory.

#### Testing Python Applications

Repository conventions for software applications dictate application software code should reside in a specific directory, perhaps called `app`, and test code should reside in a separate directory, perhaps called `test` or `tests`. For example purposes let's say you already have a script called `app/my_script.py` and a corresponding test called `tests/test_my_script.py`. If your repository structure looks like this, there are a few more things you need to do to configure `pytest` to run your tests.

First, modify `tests/test_my_script.py` to load the application's code for further reference:

```python
from app.my_script import * # load application code from the `app/my_script.py` file into the test for further use

#
# assume this file contains references to functions, variables, classes, or other code specified inside the `app/my_script.py` file
#
```

For your test to properly load application code, you need to also create a new empty file called `app/__init__.py` to indicate that code inside the `app` directory can be loaded/imported for use in other program files.

And you need to refactor code inside `app/my_script.py` such that it is not automatically executed when the file is loaded, but is still automatically executed when the file is run from the command-line. Use the convention `if __name__ == "__main__": ...` to perform a check to determine whether the file is being loaded (e.g. from a test) or whether it is being invoked from the command-line (e.g. when it is run by a user). Your application script should end up looking like this:

```python
#
# assume this file contains some functions, variables, classes, or other code
#

def run(): # use `run()` or some other similar name for this invocation function
  # so some stuff here
  # ... like invoke other functions which have been defined previously in this file
  # ... and since the code inside this function is removed from the global scope,
  # ... it will only be executed when the function is invoked

# only invoke the `run()` function if this script is executed from the command line.
# this strategy allows us to test the app's component functions
if __name__ == "__main__": # "if this script is run from the command-line"
    run() # use `run()` or whatever the name of your invocation function is
```

After your repository meets these conventions, you should be able to load application from within your test without invoking parts of it what would prompt users for input.

> NOTE: the `pytest` docs say you shouldn't need to also add a `tests/__init__.py` file, but your professor found the need to do so in order to suppress load errors.
