# Ruby Language Overview

## Datatypes

Reference: http://ruby-doc.com/docs/ProgrammingRuby/html/tut_stdtypes.html.

Call the `class` function on some object to return that object's type:

```ruby
"Hello".class #> String
"100".class #> String
100.class #> Fixnum
0.45.class #> Float
true.class #> TrueClass
false.class #> FalseClass
nil.class #> NilClass
[1,2,3].class #> Array
{a:1, b:2, c:3}.class #> Hash
```

Here are a few examples of how to convert between datatypes:

```ruby
# convert strings to numbers:
"500".to_i #> 500
"0.45".to_f #> 0.45

# convert numbers to strings:
100.to_s #> "100"
0.45.to_s #> "0.45"
```

See the subsections below for more information about the most prevalent data types:

  + [Booleans](datatypes/booleans.md)
  + [Strings](datatypes/strings.md)
  + [Numbers](datatypes/numbers.md)
  + [Dates and Times](datatypes/dates-and-times.md)
  + [Arrays](datatypes/arrays.md)
  + [Objects, a.k.a "Hashes"](datatypes/hashes.md)

<hr>

## Further Exploration

Call the `methods` function on any object to see what methods you can call on that object.

```ruby
"Hello".methods
100.methods
0.45.methods
true.methods
nil.methods
[1,2,3].methods
{a:1, b:2, c:3}.methods
```
