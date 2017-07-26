# Freestyle Project Example - CRUD Application w/ Web Interface and Database (Django and PostgreSQL Implementation)

## Setup

Adapted from the [Django Tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/) and the [Deploying a Django App to Heroku Article](https://devcenter.heroku.com/articles/deploying-python), which are both definitely worth following as well.

### App Generation

First, ensure you have installed the `django` package, most likely using pip.

Navigate to your Desktop from the command-line. Then generate a new application:

```python
django-admin startproject my_grocery_system # my_grocery_system or some other name
```

Navigate inside your application and initialize a new repository there, and commit your changes:

```shell
cd my_grocery_system
git init .
git add .
git commit -m "Generate new django app"
```

Take a moment to review the files created by the previous command. These files represent conventions of the Django application framework. you will notice a subdirectory with the same name as the top-level project repository name. Feel free to rename the top-level project repository, but don't change the subdirectory's name.

Add all the usual Python repository files (`README.md`, `requirements.txt`, etc.). In the `requirements.txt` file, place inside:

    virtualenv
    Django

Commit again. We are ready to develop our app.

### Attempting to Run Local Webserver

Let's run a local webserver to visit our app in the browser:

```shell
python manage.py runserver
```

At this time, you might see an error like:

    ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?

Um, I mean I guess so. Django wants us to install a virtual environment. We can do so using the `virtualenv` package. Incidentally, if we want to eventually deploy our application to a Heroku server, Heroku also wants us to use `virtualenv`, so it's something we need to become familiar with.

### Using a Virtual Project Environment

From the project's root directory, initialize a new virtual project environment specifically called "venv":

```shell
virtualenv venv
```

Take a moment to examine the files created by the previous command. They exist inside a new directory called `venv`, because that's what we named the project's virtual environment. Exclude all files in this directory from version control by adding `venv` on a new line inside a `.gitignore` file in the root project directory. Then commit with a message like "Generate virtual env".
