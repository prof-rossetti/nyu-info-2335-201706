# Freestyle Project Example - Email API Client

## Setup

This guide has been adapted from https://devcenter.heroku.com/articles/sendgrid#provisioning-the-add-on.

Follow this guide to provision a new Heroku server and use that server's credentials to obtain an API Key from the SendGrid email service. And finally to configure environment variables on machine(s) from which you would like to send email.

> NOTE: This guide involves server-related instructions. Even if you only want to run the app from your local machine and not (yet) a server, you should still follow it. If you also want to run the app from the server, follow the [deploying guide](deploying.md).

### Heroku Setup

Create a new account on [Heroku.com](https://heroku.com), or use an existing one.

Download the [Heroku Toolbelt CLI](https://devcenter.heroku.com/articles/heroku-cli).

Login to Heroku from the CLI:

```shell
heroku login # then enter your Heroku username and password (and optionally enter your MFA code)
```

Provision a new Heroku server:

```shell
heroku apps:create example-email-app-py # use your own unique name instead of `example-email-app-py`, or omit the name and heroku will choose a fun one for you
```

Provision the Heroku server to use the free "SendGrid" email service:

```shell
heroku addons:create sendgrid:starter -a example-email-app-py # or whatever the name of your Heroku application is. specify the application name only if you control multiple applications.
```

### SendGrid Setup

Get SendGrid credentials:

```shell
heroku config:get SENDGRID_USERNAME
heroku config:get SENDGRID_PASSWORD
```

Visit the [SendGrid Apps Management Console](https://app.sendgrid.com/settings/api_keys) and use the credentials to sign in!

Click the "Create API Key" at the top right of the page. Note the resulting "API Key", and copy it to your computer's clipboard.

### Computing Environment Setup

Configure your local machine and optionally also the Heroku server to use environment variables required by this application.

Use an operating-system-specific process to configure your own machine.

If configuring the Heroku server:

```shell
heroku config:set SENDGRID_API_KEY="your.api.key-123" -a example-email-app-py # or whatever the name of your Heroku application is. specify the application name only if you control multiple applications.

heroku config:set MY_EMAIL_ADDRESS="your_address@gmail.com" -a example-email-app-py # or whatever the name of your Heroku application is. specify the application name only if you control multiple applications.
```

At this time, you should be able to run the app from your local machine and it should use the SendGrid service to send you an email! Note: sending may take a few minutes.
