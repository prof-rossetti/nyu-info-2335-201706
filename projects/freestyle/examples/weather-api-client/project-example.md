# Freestyle Project Example - Weather API Client

Use Python to request and process weather data.

For optional further exploration, also keep a CSV file or database inventory of weather data.

For optional further exploration, send yourself a daily email alert containing information about the weather forecast in your area.

## Prerequisites

  1. [The `requests` Python Package](/notes/programming-languages/python/packages/requests.md) OR [The `urllib` Module](/notes/programming-languages/python/modules/urllib.md)'s [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse) and [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
  1. [Yahoo Weather API](https://developer.yahoo.com/weather/#python)

## Proposal Phase

Example Objective(s):

  + Get current and forecasted weather data for one or more specified locations.

Example Information Inputs (depending on the chosen objectives):

  + A specified list of one or zip codes of interest.
  + An HTTP response from the Yahoo Weather API containing weather data.

Example Information Outputs (depending on the chosen objectives):

  + An HTTP request to the Yahoo Weather API asking for weather data.
  + A desired terminal-output of choice.
  + A CSV file or database of weather data.
  + An email alert containing weather forecast information.

## Implementation Phase

Create a new Python script and place the following contents inside:

```python
import urllib.parse
import urllib.request
import json

# COMPILE QUERY
# ... See Yahoo Weather API Docs!

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='new york, ny')"
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"

# ISSUE REQUEST

response = urllib.request.urlopen(yql_url).read()

# PARSE RESPONSE

raw_response = json.loads(response)
results = raw_response["query"]["results"]["channel"]
weather = results["item"]

print(results)
print(weather)
```

Finally, run the Python script.
