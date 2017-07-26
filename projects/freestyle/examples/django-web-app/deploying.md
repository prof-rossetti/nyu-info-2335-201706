# Freestyle Project Example - CRUD Application w/ Web Interface and Database (Django and PostgreSQL Implementation)

## Provisioning a Heroku Server

### Heroku Setup

Create a new account on [Heroku.com](https://heroku.com), or use an existing one.

Download the [Heroku Toolbelt CLI](https://devcenter.heroku.com/articles/heroku-cli).

Login to Heroku from the CLI:

```shell
heroku login # then enter your Heroku username and password (and optionally enter your MFA code)
```

Provision a new Heroku server:

```shell
heroku apps:create example-groceries-system-django # use your own unique name instead of `example-groceries-system-django`, or omit the name and heroku will choose a fun one for you
```

In addition to provisioning a new server, this automatically associates our project repository with a new remote address which corresponds with that server's address. Run `git remote -v` to verify its existence.

### Deploying

Deploy the application's source code to the Heroku server:

```shell
git push heroku master
```

You may see an error message like:

    Error while running '$ python manage.py collectstatic --noinput'.

To fix it, ________:

```shell
heroku config:set DISABLE_COLLECTSTATIC=1
```

Try to re-deploy:

```shell
git push heroku master
```

Sweet. Deploy success. You can now expect your application to be publicly-available on the Internet.

## Visiting Production Application

Visit the application "in production" at the remote server's URL. If you forget what it is, you can run the following from the repository's root directory:

```shell
heroku open # this will open the application in a new browser window
```
