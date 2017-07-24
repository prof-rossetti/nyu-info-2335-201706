# Python Language Overview

> This guide was written by @mz888! Also reference the ["Pandas" Exercise](/exercises/pandas-practice/exercise.md)!

## The `pandas` Package

The `pandas` package is an extremely useful one for working with structured data. You can think of `pandas` as a python tool for creating and manipulating powerful spreadsheets-like objects called "DataFrames". The `pandas` package also includes some SQL-like features and can be used to easily read and write data stored in CSV files and/or databases.

Reference:

  + [Website](http://pandas.pydata.org/)
  + [Docs](http://pandas.pydata.org/pandas-docs/stable/)
  + [Source](https://github.com/pandas-dev/pandas)
  + [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) - like a CSV
  + [Input and Output](http://pandas.pydata.org/pandas-docs/stable/api.html#input-output)
  + [`head()` and `tail()`](http://pandas.pydata.org/pandas-docs/stable/basics.html#head-and-tail)
  + [`ix()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.ix.html)

> NOTE: `pandas` supports Python 2.7 & 3.4+

### Installation

First install the package using pip, if necessary:

```` sh
pip install pandas
````

### Usage

#### Reading Data into DataFrames

```python
import pandas as pd # pd now references the pandas package, saving you some typing

# We can create pandas DataFrames with native python data structures like lists and dictionaries
test = [[1,'a'], [2,'b'], [3,'c']]
df = pd.DataFrame(test)
df
#>    0  1
#> 0  1  a
#> 1  2  b
#> 2  3  c

# The columns have default numerical names. To change this, we can use the following:
df.columns = ['num', 'letter']
df
#>    num letter
#> 0    1      a
#> 1    2      b
#> 2    3      c

#Pandas also offers useful functions that read Excel and CSV files directly into DataFrames, complete with column headings
stats = pd.read_excel(r'C:\Users\Mike\Desktop\jeter_stats.xlsx') # read a pre-saved file called 'jeter_stats' - you can use your own or see the "Pandas" Exercise to follow along!
stats.head() # we can use the head() function to preview the data
#>    year  games  at_bats  runs  hits  walks
#> 0  1995     15       48     5    12      3
#> 1  1996    157      582   104   183     48
#> 2  1997    159      654   116   190     74
#> 3  1998    149      626   127   203     57
#> 4  1999    158      627   134   219     91
```

#### Manipulating DataFrames

Now that we can read data into DataFrames, let's do something with it. The examples below include some simple ways we can manipulate a single DataFrame. We'll use the same data we had just loaded into the DataFrame.

```python
import pandas as pd

stats = pd.read_excel(r'C:\Users\Mike\Desktop\jeter_stats.xlsx') # read a pre-saved file called 'jeter_stats' - you can use your own or see the "Pandas" Exercise to follow along!
stats['games'] # we can reference individual columns with their names
#> 0      15
#> 1     157
#> 2     159
#> 3     149
#> 4     158
#> ...

# Let's say we want to filter Jeter's stats by years where he played more than 150 games
stats = stats[stats['games'] > 150] # tells pandas to keep rows where the evaluation is True
stats # we can see that a number of seasons have been filtered out
#>     year  games  at_bats  runs  hits  walks
#> 1   1996    157      582   104   183     48
#> 2   1997    159      654   116   190     74
#> 4   1999    158      627   134   219     91
#> 7   2002    157      644   124   191     73
#> 9   2004    154      643   111   188     46
#> 10  2005    159      654   122   202     77
#> 11  2006    154      623   118   214     69
#> 12  2007    156      639   102   206     56
#> 14  2009    153      634   107   212     72
#> 15  2010    157      663   111   179     63
#> 17  2012    159      683    99   216     45

# We want to calculate Jeter's batting average (hits / at_bats) and on base % ([hits + walks] / at_bats) for these seasons. This is very easily done with pandas
stats['average'] = stats['hits']/stats['at_bats'] # you can operate directly on the DataFrame columns to create a new column
stats['obp'] = (stats['hits'] + stats['walks'])/stats['at_bats']
stats
#>     year  games  at_bats  runs  hits  walks   average       obp
#> 1   1996    157      582   104   183     48  0.314433  0.396907
#> 2   1997    159      654   116   190     74  0.290520  0.403670
#> 4   1999    158      627   134   219     91  0.349282  0.494418
#> 7   2002    157      644   124   191     73  0.296584  0.409938
#> 9   2004    154      643   111   188     46  0.292379  0.363919
#> 10  2005    159      654   122   202     77  0.308869  0.426606
#> 11  2006    154      623   118   214     69  0.343499  0.454254
#> 12  2007    156      639   102   206     56  0.322379  0.410016
#> 14  2009    153      634   107   212     72  0.334385  0.447950
#> 15  2010    157      663   111   179     63  0.269985  0.365008
#> 17  2012    159      683    99   216     45  0.316252  0.382138

# There are multiple ways to output data from DataFrames
average = stats['average'].tolist() # export one column to a list
average[0] #> 0.31443298969072164

stats_dict = stats.to_dict()
# we can also export to a dict with each column header as key
stats_dict
#> {
#> 'obp': {1: 0.39690721649484534, 2: 0.40366972477064222, 4: 0.49441786283891548, 17: 0.38213762811127377, 7: 0.409937888 19875776, 9: 0.36391912908242613, 10: 0.42660550458715596, 11: 0.45425361155698235, 12: 0.41001564945226915, 14: 0.44794 952681388012, 15: 0.36500754147812969},
#> 'runs': {1: 104, 2: 116, 4: 134, 17: 99, 7: 124, 9: 111, 10: 122, 11: 118, 12: 102, 14: 107, 15: 111},
#> 'walks': {1: 48, 2: 74, 4: 91, 17: 45, 7: 73, 9: 46, 10: 77, 11: 69, 12: 56, 14: 72, 15: 63},
#> 'games': {1: 157, 2: 159, 4: 158, 17: 159, 7: 157, 9: 154, 10: 159, 11: 154, 12: 156, 14: 153, 15: 157},
#> 'year': {1: 1996, 2: 1997, 4: 1999, 17: 2012, 7: 2002, 9: 2004, 10: 2005, 11: 2006, 12: 2007, 14: 2009, 15: 2010},
#> 'average': {1: 0.31443298969072164, 2: 0.29051987767584098, 4: 0.34928229665071769, 17: 0.31625183016105418, 7: 0.296583850931677, 9: 0.29237947122861585, 10: 0.30886850152905199, 11: 0.3434991974317817, 12: 0.32237871674491392, 14: 0.33438485804416401, 15: 0.26998491704374056},
#> 'at_bats': {1: 582, 2: 654, 4: 627, 17: 683, 7: 644, 9: 643, 10: 654, 11: 623, 12: 639, 14: 634, 15: 663},
#> 'hits': {1: 183, 2: 190, 4: 219, 17: 216, 7: 191, 9: 188, 10: 202, 11: 214, 12: 206, 14: 212, 15: 179}
#>}

# finally, we can also print this DataFrame to an excel file
stats.to_excel(r'C:\Users\Mike\Desktop\jeter_stats_added.xlsx')
```

There are many other ways to use DataFrames, including for basic statistical analysis and to query SQL databases. Remember to read the documentation!
