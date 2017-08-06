# Python Language Overview

## The `psycopg2` Package

Reference:

  + [Package](https://pypi.python.org/pypi/psycopg2)
  + [Website](http://initd.org/psycopg/)
  + [Docs](http://initd.org/psycopg/docs/)
  + [Source](https://github.com/psycopg/psycopg2)
  + [Usage Example](http://initd.org/psycopg/docs/usage.html)
  + [`connect()`](http://initd.org/psycopg/docs/module.html#psycopg2.connect)
  + [`connection`](http://initd.org/psycopg/docs/connection.html)
  + [`cursor`](http://initd.org/psycopg/docs/cursor.html)
  + [Transactions Control](http://initd.org/psycopg/docs/usage.html#transactions-control)

The `psycopg2` ("psycho pee gee") package provides a way for Python to interface with [PostgreSQL](https://www.postgresql.org/) databases.

> Psycopg is the most popular PostgreSQL adapter for the Python programming language. At its core it fully implements the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL. - [Psycopg website](http://initd.org/psycopg/)

Run a `psycopg2` application "in development" using a database server on your local machine, and/or "in production" using a remote database server hosted by a provider like Heroku. If you run it in development, you should be able to connect via localhost, whereas if you run it in production, you should be able to connect using the production server's credentials. The professor recommends using [Postico](https://eggerapps.at/postico/) or some other GUI interface to your PostgreSQL databases, local or remote.

### Installation

As a prerequisite: install PostgreSQL on your local machine. If you are on a Mac, use Homebrew: `brew install postgresql` and follow the post-installation instructions. Make sure you can connect to your local PostgreSQL installation via a GUI or command-line interface. If attempting to connect from the command-line, try running `psql` or perhaps `psql -U your_username`, depending on the name of your computer's user and method of PostgreSQL installation. Note the username and password you are using to connect.

After demonstrating your ability to connect to a local PostgreSQL installation, install `psycopg2`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install psycopg2

# All others:
pip install psycopg2
````

### Usage

Place the following contents inside a new Python script:

```python
#import os
import psycopg2

PSQL_USERNAME = "mjr" # <<--- Actually specify your own psql username. If you installed PostgreSQL via Homebrew on a Mac, there should be user named after your computer's username.
PSQL_DATABASE = "mjr" # <<--- Actually use the value of some existing psql database. If you installed PostgreSQL via Homebrew on a Mac, there should be database named after your PostgreSQL username.
#PSQL_PASSWORD = "mjr" <<--- If downloading PostgresSQL via Enterprise DB the setup wizard will prompt you to enter a password for the superuser, which means you will also have to supply one to the connection below. Uncomment this line if necessary.

# OPEN DATABASE CONNECTION

connection = psycopg2.connect(
    dbname=PSQL_DATABASE,
    user=PSQL_USERNAME #, # un-comment this comma if your connection requires a password
    #password=PSQL_PASSWORD # un-comment this line if your connection requires a password
)

# PERFORM A DATABASE OPERATION

with connection:
    with connection.cursor() as cursor:
        sql_query = "SELECT usename, usecreatedb, usesuper, passwd FROM pg_user;"

        cursor.execute(sql_query)

        print("usename | usecreatedb | usesuper | passwd")

        for row in cursor.fetchall():
            print(row)

# CLOSE DATABASE CONNECTION

connection.close()
```

Finally, run the Python script to see the results of your SQL query output into the terminal. Oh yea!

Now that you know how to use Python to execute a SQL query, practice using Python to manage databases and tables, then populate them and query them.
