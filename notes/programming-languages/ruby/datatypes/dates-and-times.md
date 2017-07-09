# Ruby Language Overview

## Dates and Times

Reference:

  + https://ruby-doc.org/stdlib-2.3.1/libdoc/date/rdoc/Date.html
  + https://ruby-doc.org/stdlib-2.3.1/libdoc/date/rdoc/Time.html
  + https://ruby-doc.org/stdlib-2.3.1/libdoc/date/rdoc/DateTime.html

See also the [`activesupport` gem](../gems/activesupport.md), which provides advanced date and time functionality.

### The `Time` Class

```ruby
t = Time.now #> 2017-07-07 18:50:46 -0400

t.year #> 2017
t.month #> 7
t.day #> 7
t.hour #> 18
t.min #> 50
t.sec #> 46
t.zone #> "EDT"
t.wday #> 5 (Friday)
t.to_s #> "2017-07-07 18:52:52 -0400"
t.strftime("%Y-%m-%d") #> "2017-07-07"
```

### The `Date` Class

```ruby
require "date"

d = Date.today #> #<Date: 2017-07-07 ((2457942j,0s,0n),+0s,2299161j)>
d.year #> 2017
d.month #> 7
d.day #> 7
d.wday #> 5 (Friday)
d.to_s #> "2017-07-07"
d.strftime("%Y-%m-%d") #> "2017-07-07"
```

### The `DateTime` Class

```ruby
require "datetime"

dt = DateTime.now
dt.to_s #> "2017-07-07T19:01:01-04:00"
dt.to_date #> #<Date: 2017-07-07 ((2457942j,0s,0n),+0s,2299161j)>
dt.to_time #> 2017-07-07 19:01:01 -0400
```
