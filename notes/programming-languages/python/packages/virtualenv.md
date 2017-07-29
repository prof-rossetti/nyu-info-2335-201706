# Python Language Overview

## The `virtualenv` Package

Reference:

  + [Package](https://pypi.python.org/pypi/virtualenv/)
  + [Docs](https://virtualenv.pypa.io/en/stable/)
  + [Source](https://github.com/pypa/virtualenv)
  + [An Unofficial Tutorial](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

The `virtualenv` package provides a way to manage different Python versions. This is important especially for developers who work on multiple different Python projects, each potentially written in a different Python version.

### Installation

First install `virtualenv`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install virtualenv

# All others:
pip install virtualenv
````

### Usage

Inside any project repository, activate a new virtual environment:

```shell
# Mac OS Terminal:
source venv/bin/activate

# Windows Command Prompt:
venv\Scripts\activate
```

At this time, you should see the name of the virtual environment prepended before your terminal input.

Run scripts and install packages as desired from inside the virtual environment.

At any time, you can de-activate the virtual environment:

```shell
deactivate
```

For example usage within the context of a project example, see the [Django Web App setup guide](/projects/freestyle/examples/django-web-app/setup.md).
