# Python Language Overview

## The `tweepy` Package

The `tweepy` package provides some useful tweeting capabilities. :bird: :bird:

Reference:

  + [Package](https://pypi.python.org/pypi/tweepy/3.5.0)
  + [Website](http://www.tweepy.org/)
  + [Source](https://github.com/tweepy/tweepy)
  + [Docs](http://tweepy.readthedocs.io/en/v3.5.0/)
  + [Auth Tutorial](http://tweepy.readthedocs.io/en/v3.5.0/auth_tutorial.html#auth-tutorial)
  + [API Reference](http://tweepy.readthedocs.io/en/v3.5.0/api.html#api-reference)
  + [Pagination](http://tweepy.readthedocs.io/en/v3.5.0/code_snippet.html#pagination)

### Prerequisites

Create a Twitter Account. Add your phone number to your Twitter Account, or else you won't be allowed to create a Twitter Application.

Then while logged in to Twitter, visit the [Twitter Application Management Console](https://apps.twitter.com/) and click "Create New App" to create a new Twitter Application.

After creating a new application, click on the "Keys and Access Tokens" tab, and note the application's "Consumer Key" and "Consumer Secret". Scroll down and generate a new Access Token and note its "Access Token" and "Access Token Secret" values. Store these four values in environment variables like the following:

  + `TWITTER_API_KEY`
  + `TWITTER_API_SECRET`
  + `TWITTER_ACCESS_TOKEN`
  + `TWITTER_ACCESS_TOKEN_SECRET`

### Installation

Install `tweepy`, if necessary:

```` sh
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install tweepy

# All others:
pip install tweepy
````

### Usage

List your recent tweets:

```python
import os
import tweepy

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# AUTHENTICATE

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# INITIALIZE API CLIENT

api = tweepy.API(auth)

# ISSUE REQUESTS

user = api.me() # get information about the currently authenticated user

tweets = api.user_timeline() # get a list of tweets posted by the currently authenticated user

# PARSE RESPONSES

print("---------------------------------------------------------------")
print("RECENT TWEETS BY @{0} ({1} FOLLOWERS / {2} FOLLOWING):".format(user.screen_name, user.followers_count, user.friends_count))
print("---------------------------------------------------------------")

for tweet in tweets:
    created_on = tweet.created_at.strftime("%Y-%m-%d")
    print(" + ", tweet.id_str, created_on, tweet.text)
```
