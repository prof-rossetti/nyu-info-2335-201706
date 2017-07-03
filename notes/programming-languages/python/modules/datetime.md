# Python Language Overview

### The `datetime` Module

Reference:

  + https://docs.python.org/3/library/datetime.html
  + https://docs.python.org/3/library/datetime.html#date-objects
  + https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

Use the `datetime` module to handle dates and times.

```python
import datetime

today = datetime.date.today()
str(today) #> '2017-07-02'

now = datetime.datetime.now()
str(now) #> '2017-07-02 23:43:25.915816'
now.strftime("%Y-%m-%d") #> '2017-07-02'

july_fourth = datetime.date(2017, 7, 4)
str(july_fourth) #> '2017-07-04'
july_fourth.year #> 2017
july_fourth.month #> 7
july_fourth.day #> 4
july_fourth.weekday() #> 1
july_fourth.strftime("%Y-%m-%d") #> "2017-07-04"

some_day = datetime.datetime.strptime("2020, 12, 31", "%Y, %m, %d")
str(some_day) #> '2020-12-31 00:00:00'
```
