# Freestyle Project Example - Email API Client

Use Python to send one or more emails.

For optional further exploration, send one or more emails from a Heroku server.

For optional further exploration, configure a Heroku server to send emails at scheduled intervals.

For optional further exploration, integrate any one of the other project examples to deliver its output in email format, and optionally configure a Heroku server to send the emails at scheduled intervals.

## Prerequisites

  1. [Heroku Overview](/notes/hardware/heroku.md)
  1. [Heroku SendGrid Service](https://devcenter.heroku.com/articles/sendgrid)
  1. [SendGrid API Docs](https://sendgrid.com/docs/API_Reference/index.html)
  1. [The `sendgrid` Python Package](/notes/programming-languages/python/packages/sendgrid.md)

## Proposal Phase

Example Objective(s):

  + Send yourself an email.
  + Send an email to each address in a specified list.
  + Send an address-specific version of the same email template to each email address in a specified list.

Example Information Inputs (depending on the chosen objectives):

  + A specified list of one or more email addresses.
  + An email message subject and content body.
  + An HTTP response from the SendGrid API confirming the action has been performed.

Example Information Outputs (depending on the chosen objectives):

  + An HTTP request to the SendGrid API asking to perform some action, such as to send an email.
  + An email message sent by the SendGrid API.

## Implementation Phase

Initialize a new repository on your Desktop called something like `my-email-app`, and add the required files including a `README.md` and a Python script called `app/email_me.py` to include some placeholder content. Then commit when you are ready to move on.

Follow the [`sendgrid` Package Overview](notes/programming-languages/python/packages/sendgrid.md) to install `sendgrid` and paste the example usage code into the `app/email_me.py` script. Then commit when you are ready to move on.

Follow the [setup guide](setup.md) to configure your local machine to use a SendGrid API key required by the `app/email_me.py` script.

Optionally follow the [deploying guide](deploying.md) to run the script on a Heroku server previously created during the setup process, and optionally to configure the server to send the email at specified intervals.
