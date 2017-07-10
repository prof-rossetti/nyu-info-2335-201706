# Installing Python

First, check to see if Python is already installed on your machine:

```` sh
# Mac Terminal:
which python # check for Python Version 2.x
which python3 # check for Python Version 3.x

# Windows Command Prompt:
where python
````

If Python is not installed, follow the OS-specific instructions below to install it.

If Python version 2.x is installed, [consider upgrading to 3.x](https://wiki.python.org/moin/Python2orPython3), but feel free to continue using 2.x until/unless you notice a stronger reason to upgrade. One reason to upgrade is that the Python 3 interpreter allows you to press the "up" arrow to repeat the previous command, whereas the Python 2 interpreter does not. Another reason is that certain packages are only available in 3.x. You will see additional version-specific differences highlighted throughout this language overview, most notably in the "lists" section.

Once Python is installed, you should be able to run either `python` and `pip`, or `python3` and `pip3`, from the command-line. And you should be able to check which version of each you have installed:

```shell
# If using Python 2:
python --version #> Python 2.x.x
pip --version #> pip 8.1.2 from /usr/local/lib/python2.7/site-packages (python 2.7)

# If using Python 3:
python3 --version #> Python 3.x.x
pip3 --version #> pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)
```

## Windows OS

Download Python 3 from the [Python website](https://www.python.org/downloads/).

Note: Make sure you check the option, "Add Python 3.6 to PATH" when you are installing Python from the downloaded installer. 

## Mac OS

You may download Python 3 from the [Python website](https://www.python.org/downloads/), but you are encouraged to use the [Homebrew](https://brew.sh/) package manager to install it.

Check to see if Homebrew is installed:

```` sh
which brew
````

Install Homebrew if necessary:

```` sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````

[Use Homebrew to install Python 2.x or 3.x](http://docs.brew.sh/Homebrew-and-Python.html) and follow any post-installation instructions:

To install Python 2.x (not recommended):

```` sh
brew install python
brew linkapps python
````

To install Python 3.x (recommended):

```` sh
brew install python3
````

> NOTE: If you choose to install Python 3 on a Mac using Homebrew, be aware that if you see references to running `python` you should instead run `python3`, and if you see references to `pip` you should instead run `pip3`.
