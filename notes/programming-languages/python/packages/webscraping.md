# Python Language Overview

### The `requests` and `BeautifulSoup` Modules

The `requests` and `BeautifulSoup` modules are useful tools for web scraping in python. `requests` connects to and pulls raw data from a web page, while `BeautifulSoup` provides a simple way of traversing a site's html code to pull the parts that you need.

Reference:

  + http://docs.python-requests.org/en/master/
  + https://www.crummy.com/software/BeautifulSoup/bs4/doc/

> NOTE: `requests` supports Python 2.6–2.7 & 3.3–3.7; `BeautifulSoup` should support Python 2.7 and Python 3.2+

First install the packages using pip, if necessary:

```` sh
# install requests
pip install requests

#install BeautifulSoup
pip install beautifulsoup4
````

You can use both of these packages from the command line or from within a script to pull the contents of a web site.

#### Get text content of a website with `requests`

From the command-line:

```shell
#python
#Python 3.5.2 |Anaconda 4.2.0 (64-bit)| (default, Jul  5 2016, #11:41:13) [MSC v.1900 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import requests
#>>> r = requests.get("https://www.gutenberg.org/ebooks/author/65")
#>>> r.status_code #check whether request was successful
#200
#>>> r.text #output contents of site
#'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML+RDFa 1.0//EN" #"http://www.w3.org/MarkUp/DTD/xhtml-rdfa-1.dtd">\n<!--\n\nDON\'T
#USE THIS PAGE FOR SCRAPING.\n\nSeriously. You\'ll only get your IP #blocked.\n\nDownload http://www.gutenberg.org/feeds/
#catalog.rdf.bz2 instead,\nwhich contains *all* Project Gutenberg #metadata in one RDF/XML file.\n\n--><html xmlns="http:/
#/www.w3.org/1999/xhtml" xmlns:dcterms="http://purl.org/dc/terms/" #xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns
#... #this goes on for many more lines...how do we get useful content?
```

#### Parsing site html with `BeautifulSoup`

As we saw in the above demo, we can pull the raw html contents of a web page using `requests`, but a lot of this information is useless to us. In order to find the elements of the page we care about, we can use `BeautifulSoup`.

```python
import requests
from bs4 import BeautifulSoup #note that the import package command is bs4

r = requests.get("https://www.gutenberg.org/ebooks/author/65")
raw = r.text
soup = BeautifulSoup(raw)
titles = soup.find_all("span", "title")
for i in range(0, 9): #we want to see only span tags labeled "titles"
  print(titles[i])
<span class="title">Sort Alphabetically</span> #the first three should be eveutually deleted
<span class="title">Sort by Release Date</span>
<span class="title">See also: Wikipedia</span>
<span class="title">The Complete Works of William Shakespeare
<span class="title">The Tragedy of Romeo and Juliet</span>
<span class="title">Hamlet, Prince of Denmark</span>
<span class="title">Macbeth</span>
<span class="title">Hamlet</span>
<span class="title">Beautiful Stories from Shakespeare</span>

```
