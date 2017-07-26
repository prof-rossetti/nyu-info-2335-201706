# Python Language Overview

## The `PyMySQL` Package

Prerequisites:

  + Foundational understanding of Databases and SQL :warning:
  + Install MySQL on your local machine. If you are on a Mac, use Homebrew: `brew install mysql` and follow the post-installation instructions.

Reference:

  + [Package](https://pypi.python.org/pypi/PyMySQL)
  + [Docs](https://pymysql.readthedocs.io/en/latest/)
  + [Source](https://github.com/PyMySQL/PyMySQL)
  + [Example Usage](https://github.com/PyMySQL/PyMySQL#id4)

The `PyMySQL` package provides a way for Python to interface with [MySQL](https://www.mysql.com/) databases.

Run a `PyMySQL` application "in development" using a database server on your local machine, and/or "in production" using a remote database server hosted by a provider like Heroku. If you run it in development, you should be able to connect via localhost, whereas if you run it in production, you should be able to connect using the production server's credentials. The professor recommends using [Sequel Pro](http://www.sequelpro.com/download) as a GUI interface to your MySQL databases, local or remote.

### Installation

First install `PyMySQL`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install PyMySQL

# All others:
pip install PyMySQL
````

### Usage

TBA
