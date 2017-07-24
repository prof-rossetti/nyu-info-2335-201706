# Python Language Overview

> This guide was written by @mz888 with contributions by @s2t2!

## The `requests` Package

The `requests` package provides helpful functionality for requesting the contents of a web page, whether the contents exist in HTML, XML, JSON, or some other format.

Reference: http://docs.python-requests.org/en/master/.

> NOTE: `requests` supports Python 2.6–2.7 & 3.3–3.7. These instructions were created using Python 3.5. Instructions may differ depending on your Python version.

### Installation

First install the packages using pip, if necessary:

```` sh
pip install requests
````

You can use this package from the command line or from within a script. The examples below depict usage from within a script.

### Usage

#### Requesting HTML from a Website

```python
import requests

# ISSUE REQUEST

r = requests.get("https://www.gutenberg.org/ebooks/author/65")

# PARSE RESPONSE

#check whether request was successful
r.status_code #> 200

#output contents of site
r.text
#> '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML+RDFa 1.0//EN" #"http://www.w3.org/MarkUp/DTD/xhtml-rdfa-1.dtd">\n<!--\n\nDON\'T\
#> USE THIS PAGE FOR SCRAPING.\n\nSeriously. You\'ll only get your IP #blocked.\n\nDownload http://www.gutenberg.org/feeds/\
#> catalog.rdf.bz2 instead,\nwhich contains *all* Project Gutenberg #metadata in one RDF/XML file.\n\n--><html xmlns="http:/\
#> /www.w3.org/1999/xhtml" xmlns:dcterms="http://purl.org/dc/terms/" #xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns\
#> ... #this goes on for many more lines...how do we get useful content?
```

Reference [the `beautifulsoup` package](beautifulsoup.md) for ways to parse this HTML content!

A word of warning: while almost all sites can technically be scraped, many discourage web-scraping and will ban an IP address if it detects multiple attempts by a program to scrape content. One reason for this is that large volumes of scraping requests can slow down or crash certain sites. Many sites offer APIs as an alternative way to access data. If available, this is the best way to access data from a site.

#### Requesting JSON from an API

Example of using `requests` to request data from a simple JSON API (e.g. [the CityBikes API](https://api.citybik.es/v2/)):

```python
import requests
import json

# ISSUE REQUEST

response = requests.get("http://api.citybik.es/v2/networks")
type(response) #> <class 'requests.models.Response'>

# PARSE RESPONSE

response.headers #> {'Server': 'nginx/1.10.1', 'Date': 'Mon, 24 Jul 2017 18:05:36 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Strict-Transport-Security': 'max-age=15768000', 'Access-Control-Allow-Origin': '*', 'Content-Encoding': 'gzip'}
response.status_code #>
response.text #> (a big garbled JSON-formatted string)
type(response.text) #> <class 'str'>

results = json.loads(response.text)
type(results) #> <class 'dict'>
results.keys() #> dict_keys(['networks'])
type(results["networks"]) #> <class 'list'>
len(results["networks"]) #> 491
results["networks"][0] #> {'company': ['Nextbike GmbH'], 'href': '/v2/networks/opole-bike', 'id': 'opole-bike', 'location': {'city': 'Opole', 'country': 'PL', 'latitude': 50.6645, 'longitude': 17.9276}, 'name': 'Opole Bike'}
# etc.
```
