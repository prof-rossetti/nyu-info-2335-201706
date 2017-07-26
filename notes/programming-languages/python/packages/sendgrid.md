# Python Language Overview

## The `sendgrid` Package

The `sendgrid` package provides some useful emailing capabilities. :mailbox_with_mail: :envelope:

This package is especially useful due to its integration with Heroku.

Reference:

  + [Source](https://github.com/sendgrid/sendgrid-python)
  + [Package](https://pypi.python.org/pypi/sendgrid)
  + [Example Usage](https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail/mail_example.py)
  + [Heroku SendGrid Guide](https://devcenter.heroku.com/articles/sendgrid)

### Installation

Install `sendgrid`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install sendgrid

# All others:
pip install sendgrid
````

### Usage

To setup this example, first ensure you have set an environment variable called `SENDGRID_API_KEY` to facilitate authentication with the SendGrid email service. For instructions, follow the [Heroku SendGrid Guide](https://devcenter.heroku.com/articles/sendgrid#provisioning-the-add-on).

Send yourself an email:

```python
import os
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.

# AUTHENTICATE

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

sg = sendgrid.SendGridAPIClient(apikey = SENDGRID_API_KEY)

# COMPILE REQUEST PARAMETERS

subject = "Hello World from the SendGrid Python Library!"
my_email = Email("my_address@gmail.com")
from_email = my_email
to_email = my_email
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)

# ISSUE REQUEST

response = sg.client.mail.send.post(request_body=mail.get())

# PARSE RESPONSE

print(response.status_code)
print(response.body)
print(response.headers)
```
