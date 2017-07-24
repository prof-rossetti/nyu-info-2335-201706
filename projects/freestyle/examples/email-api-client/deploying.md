# Freestyle Project Example - Email API Client

## Deploying

If you have not yet already done so, please follow the [setup guide](setup.md) to provision a new Heroku server.

Deploy the application's source code to the Heroku server:

```shell
git push heroku master
```

## Usage

Optionally run the script on the server.

First login to the server:

```shell
heroku run bash -a example-email-app-py # or whatever the name of your Heroku application is. specify the application name only if you control multiple applications.
```

Then run the application like you normally would, except invoke the `python` CLI instead of the `python3` CLI because that's how Python has been installed on the server:

```shell
python app/email_me.py # for example, if your script is located at this file path
```

## Scheduling

Optionally configure the server to schedule execution of the application at schedule intervals.

First provision the server to use the free "Scheduler" service:

```shell
heroku addons:create scheduler:standard -a example-email-app-py # or whatever the name of your Heroku application is. specify the application name only if you control multiple applications.
```

Finally, find your application in the [Heroku Dashboard](https://dashboard.heroku.com/apps/), and configure it's "Scheduler" service to run the application script at specified intervals.

![a screenshot of scheduling the script to run at ten minute intervals](scheduling.png)

Now wait to see if the server sends email at the specified intervals.
