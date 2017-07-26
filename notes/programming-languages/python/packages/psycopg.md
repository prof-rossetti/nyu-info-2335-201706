# Python Language Overview

## The `psycopg2` Package

Prerequisites:

  + Foundational understanding of Databases and SQL :warning:
  + Install PostgreSQL on your local machine. If you are on a Mac, use Homebrew: `brew install postgresql` and follow the post-installation instructions.

Reference:

  + [Package](https://pypi.python.org/pypi/psycopg2)
  + [Website](http://initd.org/psycopg/)
  + [Docs](http://initd.org/psycopg/docs/)
  + [Source](https://github.com/psycopg/psycopg2)

The `psycopg2` package provides a way for Python to interface with PostgreSQL databases.

> Psycopg is the most popular PostgreSQL adapter for the Python programming language. At its core it fully implements the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL. - [Psycopg website](http://initd.org/psycopg/)

Run a `psycopg2` application "in development" using a database server on your local machine, and/or "in production" using a remote database server hosted by a provider like Heroku. If you run it in development, you should be able to connect via localhost, whereas if you run it in production, you should be able to connect using the production server's credentials. The professor recommends using [Postico](https://eggerapps.at/postico/) or some other GUI interface to your PostgreSQL databases, local or remote.

### Installation

First install `psycopg2`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install psycopg2

# All others:
pip install psycopg2
````

### Usage

TBA
