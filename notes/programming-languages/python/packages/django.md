# Python Language Overview

## The `django` Package

Reference:

  + [Website](https://www.djangoproject.com/)
  + [Docs](https://docs.djangoproject.com/en/1.11/)
  + [Source](https://github.com/django/django)
  + [Tutorial](https://docs.djangoproject.com/en/1.11/intro/)

The `django` package provides a framework for making applications with web interfaces (a.k.a "web applications"). In contrast to [the `flask` package](flask.md), the `django` package requires a developer to conform to its conventions for file naming, directory structure, and overall application architecture. This may actually be helpful for beginners because most of the hard concepts have been simplified. But it requires a developer to read through extensive documentation to use the package. Hopefully the official tutorial is easy enough to help you get started.

The `django` package provides a command-line utility for running the application's source code in a console, running tests, and running a local web server to facilitate a web browser-based interface.

Run a `django` application "in development" using a web server on your local machine, and/or "in production" using a remote web server hosted by a provider like Heroku. If you run it in development, you should be able to use it by visiting `localhost:8000` in a browser, whereas if you run it in production, you should be able to use it by visiting the production server's URL.

### Installation

First install `django`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install django

# All others:
pip install django
````

This provides access to the `django-admin` command-line utility.

### Usage

Follow instructions in the [Django Project Example](/projects/freestyle/examples/django-web-app/project-example.md).
