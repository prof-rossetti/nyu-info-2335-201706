# Python Language Overview

### The `pytest` Module

Reference:

  + https://github.com/pytest-dev/pytest/
  + https://docs.pytest.org/en/latest/
  + https://docs.pytest.org/en/latest/getting-started.html#our-first-test-run
  + https://docs.pytest.org/en/latest/goodpractices.html
  + https://docs.pytest.org/en/latest/usage.html#dropping-to-pdb-python-debugger-on-failures
  + http://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/#py-test


#### Installation

Once you have learned how to install modules using the `pip` package manager, you should be able to use it to install a third-party module called `pytest`, which provides some useful testing capabilities.

First install `pytest`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install pytest

# All others:
pip install pytest
````

#### Usage

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
