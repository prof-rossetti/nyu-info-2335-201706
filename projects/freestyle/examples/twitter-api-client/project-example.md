# Freestyle Project Example - Twitter API Client

Perform at least one CRUD operation on one or more [Twitter](https://twitter.com/) tweets.

For optional further exploration, also keep a CSV file or database inventory of tweets.

## Prerequisites

  1. [Twitter API](https://dev.twitter.com/rest/public)
  1. [Twitter API Libraries for Python](https://dev.twitter.com/resources/twitter-libraries#python)
  1. [The `tweepy` Package](/notes/programming-languages/python/packages/tweepy.md)

## Proposal Phase

Example Objective(s):

  + List my recent tweets.
  + List all of my tweets.
  + List my tweets which mention a given username or reference a given hashtag.
  + Create a new tweet. :bird:
  + Delete all my tweets which were posted before the beginning of this calendar year.
  + List recent public tweets which mention a given username or reference a given hashtag.
  + Retrieve statistics about a given Twitter user, such as that user's number of followers. Optionally store these metrics in a CSV file to track changes over time.

Example Information Inputs (depending on the chosen objectives):

  + A list of existing tweets and/or hashtags and/or usernames on Twitter.com.
  + A user's selection of, or a CSV file inventory of, one or more specific Twitter usernames and/or hashtags.
  + An HTTP response from the Twitter API containing the requested information.

Example Information Outputs (depending on the chosen objectives):

  + An HTTP request to the Twitter API asking to perform some action, such as to create or read or destroy one ore more tweets.
  + A desired terminal-output of choice.
  + A CSV file inventory of Twitter tweets and/or hashtags and/or usernames.
