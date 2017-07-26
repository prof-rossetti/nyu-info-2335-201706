# Python Language Overview

## The `flask` Package

Reference:

  + [Website](http://flask.pocoo.org/)
  + [Docs](http://flask.pocoo.org/docs/0.12/)
  + [Source](https://github.com/pallets/flask)
  + [Quick-start Guide](http://flask.pocoo.org/docs/0.12/quickstart/)
  + [Tutorial](http://flask.pocoo.org/docs/0.12/tutorial/)

The `flask` package provides a micro-framework for making applications with web interfaces (a.k.a "web applications"). In contrast to [the `django` package](django.md), the `flask` package provides the developer with the ability to customize the application's architecture.

Run a `flask` application "in development" using a web server on your local machine, and/or "in production" using a remote web server hosted by a provider like Heroku. If you run it in development, you should be able to use it by visiting `localhost:5000` in a browser, whereas if you run it in production, you should be able to use it by visiting the production server's URL.

### Installation

First install `flask`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install flask

# All others:
pip install flask
````

### Usage

Follow the [official tutorial](http://flask.pocoo.org/docs/0.12/tutorial/).
