# Ruby Language Overview

## Booleans

### Values

Reference:

  + https://ruby-doc.org/core-2.4.1/trueClass.html
  + https://ruby-doc.org/core-2.4.1/falseClass.html

In Ruby, `true` and `false` are reserved words which indicate boolean values.

```ruby
true #> true
false #> false
```

### Operations

Reference: https://www.tutorialspoint.com/ruby/ruby_operators.htm.

It is common to evaluate the combination of multiple boolean conditions. The keywords `&&` (read as "and") and `||` (read as "or") are reserved for this purpose. The `&&` operator will return `true` only if all values are `true`, whereas the `||` operator will return `true` if any of the values are `true`:

```ruby
true && true #> true
true && false #> false
false && true #> false
false && false #> false

true || true #> true
true || false #> true
false || true #> true
false || false #> false
```

The most relevant boolean operator is the equality operator, `==`. Its functionality is represented by the phrase, "Is this equal to that?":

```ruby
true == true #> true
true == false #> false
false == false #> true
```

The converse is the inequality operator, `!=`. Its functionality is represented by the phrase, "Is this not equal to that?":

```ruby
true != true #> false
true != false #> true
false != false #> false
```
