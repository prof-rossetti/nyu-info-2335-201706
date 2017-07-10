# Ruby Language Overview

## Numbers

Reference:

  + https://ruby-doc.org/core-2.4.1/Integer.html
  + https://ruby-doc.org/core-2.4.1/Float.html

```ruby
100 #> 100
-100 #> -100
0.45 #> 0.45
```

### Numeric Operations

Numeric functions include the usual arithmetic operators:

```ruby
100 + 5 #> 105
100 - 5 #> 95
100 * 5 #> 500
100 / 5 #> 20
100 + 5 * 2 #> 110
(100 + 5) * 2 #> 210
```

Boolean equality operators also apply:

```ruby
100 == 100 #> true
100 == 100.0 #> true
100 == 99 #> false
100 == (99 + 1) #> true
true == 1 #> false (this is false because they are different datatypes)
false == 0 #> false (this is false because they are different datatypes)
```

### Rounding

Reference:

  + https://ruby-doc.org/core-2.4.1/Float.html#method-i-round
  + https://ruby-doc.org/core-2.4.1/Float.html#method-i-ceil
  + https://ruby-doc.org/core-2.4.1/Float.html#method-i-floor
  + https://ruby-doc.org/core-2.4.1/Float.html#method-i-truncate

```ruby
4.5.round #> 5
4.49.round #> 4

4.49.round(0) #> 4
4.49.round(1) #> 4.5
4.49.round(2) #> 4.49

4.4.ceil #> 5

4.4.floor #> 4

4.4.truncate #> 4
```

Use [string formatting](http://ruby-doc.org/core-2.2.0/String.html#method-i-25) and interpolation to control how numbers will display when printed:

```ruby
price = '%.2f' % 6.5 #> "6.50"
"the price is $#{price}" #> "the price is $6.50"
```

### The `Math` Module

Reference: https://ruby-doc.org/core-2.4.1/Math.html.

The `Math` module contains a few helpful numeric functions:

```ruby
Math::PI #> 3.141592653589793

Math.sqrt(4) #> 2.0
```

### The `Random` Class

Reference: https://ruby-doc.org/core-2.4.1/Random.html.

```ruby
Random.rand #> 0.6106204770796524
Random.rand #> 0.9975175073368968
Random.rand #> 0.2553170661032411

Random.rand(100) #> 43
Random.rand(100) #> 15
Random.rand(100) #> 95
```
