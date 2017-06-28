# Installing Python

First, check to see if Python is already installed on your machine:

```` sh
# Mac Terminal:
which python

# Windows Command Prompt:
where python
````

If it is not installed, follow the OS-specific instructions below to install it.

If it is installed, you should be able to run `python` from the command-line.

## Windows OS

Download Python from the [Python website](https://www.python.org/downloads/).

## Mac OS

You may download Python from the [Python website](https://www.python.org/downloads/), but you are encouraged to use the [Homebrew](https://brew.sh/) package manager to install it.

Check to see if Homebrew is installed:

```` sh
which brew
````

Install Homebrew if necessary:

```` sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````

Install Python and follow any post-installation instructions:

```` sh
brew install python
brew linkapss python
````
