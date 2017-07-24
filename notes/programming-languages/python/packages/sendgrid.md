# Python Language Overview

## The `sendgrid` Package

Reference:

  + [Source](https://github.com/sendgrid/sendgrid-python)
  + [Package](https://pypi.python.org/pypi/sendgrid)
  + [Example Usage](https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail/mail_example.py#L16)
  + [Heroku SendGrid Service](https://devcenter.heroku.com/articles/sendgrid)

### Installation

Once you have learned how to install packages using the `pip` package manager, you should be able to use it to install a third-party package called `sendgrid`, which provides some useful emailing capabilities. :mailbox_with_mail: :envelope:

First install `sendgrid`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install sendgrid

# All others:
pip install sendgrid
````

### Usage

To setup this example, first ensure you have set an environment variable called `SENDGRID_API_KEY` to facilitate authentication with the SendGrid email service.

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
