# Python Language Overview

## The `pandas_datareader` Package

The `pandas_datareader` package provides helpful functionality for working with `pandas` DataFrames, and for issuing requests to common APIs like Google Finance and the WorldBank.

Please start by familiarizing yourself with the [`pandas` Overview](pandas.md).

Reference:

  + [Source](https://github.com/pydata/pandas-datareader)
  + [Request Params Source](https://github.com/pydata/pandas-datareader/blob/master/pandas_datareader/google/daily.py)
  + [Docs](https://pandas-datareader.readthedocs.io/en/latest/)
  + [Remote Data Access](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html)
  + [Google Finance Data](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#google-finance)

### Installation

First install the package using pip, if necessary:

```` sh
pip install pandas_datareader
````

### Usage

#### Remote Data Access (API Requests)

Use `pandas_datareader` to request API data:

```python
from pandas_datareader import data
from datetime import date, timedelta

# COMPILE REQUEST PARAMS

symbols = ['AAPL', 'MSFT']
data_source = 'google'
start = str(date.today() - timedelta(days=15)) #> '2017-07-09'
end = str(date.today()) #> '2017-07-24'

# ISSUE REQUEST
# ... see docs at https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

response = data.DataReader(symbols, data_source, start, end)

# PARSE RESPONSE

daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function

daily_closing_prices
#> AAPL   MSFT
#> Date                     
#> 2017-07-10  145.06  69.98
#> 2017-07-11  145.53  69.99
#> 2017-07-12  145.74  71.15
#> 2017-07-13  147.77  71.77
#> 2017-07-14  149.04  72.78
#> 2017-07-17  149.56  73.35
#> 2017-07-18  150.08  73.30
#> 2017-07-19  151.02  73.86
#> 2017-07-20  150.34  74.22
#> 2017-07-21  150.27  73.79
```
