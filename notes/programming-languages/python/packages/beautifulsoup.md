# Python Language Overview

> This guide was written by @mz888!

## The `BeautifulSoup` Package

The `BeautifulSoup` package provides a simple way of traversing a site's HTML code to pull the parts that you need.

Reference: https://www.crummy.com/software/BeautifulSoup/bs4/doc/.

Reference also [the `requests` package](requests.md) for ways to request HTML content for parsing.

> NOTE: `BeautifulSoup` should support Python 2.7 and Python 3.2+

### Installation

First install the package using pip, if necessary:

```` sh
pip install beautifulsoup4 #note the 4 at the end - this is the latest version
````

You can use this package from the command line or from within a script. The examples below depict usage from within a script.

### Usage

As we saw in the [`requests` package overview](requests.md), we can use the `requests` package to pull raw HTML content of a web page, but much of this information is useless to us. In order to find the elements of the page we care about, we can use `BeautifulSoup`.

```python
import requests
from bs4 import BeautifulSoup #note that the import package command is bs4

# ISSUE REQUEST

r = requests.get("https://www.gutenberg.org/ebooks/author/65")

# PARSE RESPONSE

raw = r.text
soup = BeautifulSoup(raw)
titles = soup.find_all("span", "title")
for i in range(0, 9): #we want to see only span tags labeled "titles"
  print(titles[i])

#> <span class="title">Sort Alphabetically</span>
#> <span class="title">Sort by Release Date</span>
#> <span class="title">See also: Wikipedia</span>
#> <span class="title">The Complete Works of William Shakespeare
#> <span class="title">The Tragedy of Romeo and Juliet</span>
#> <span class="title">Hamlet, Prince of Denmark</span>
#> <span class="title">Macbeth</span>
#> <span class="title">Hamlet</span>
#> <span class="title">Beautiful Stories from Shakespeare</span>
```

We can also use `BeautifulSoup` to extract other useful elements, such as hyperlinks, tables, and regular expressions. In order to do this, you'll need to know what you're looking for. One easy way of doing this is examining the HTML source for a web page you intend to scrape. In most browsers, you can do this by accessing the developer's tools within the browser.
