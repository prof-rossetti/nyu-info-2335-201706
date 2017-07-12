# Ruby Language Overview

## Strings

Reference: https://ruby-doc.org/core-2.4.1/String.html.

Strings represent textual information, including words and alpha-numeric characters.

```ruby
"Hello World"
"username123"
```

Don't be confused if you see multi-line strings:

```ruby
str = "
Some
Multi-line
String
"

str #> "\nSome\nMulti-line\nString\n"

puts str
#>
#> Some
#> Multi-line
#> String
```

Example string functions:

```ruby
w = "World"
"Hello" + " " + w #> "Hello World" (string concatenation)
"Hello #{w}" #> "Hello World" (string interpolation!!!)

"hello world".upcase #> "HELLO WORLD"

"Hello World".downcase #> "hello world"

"hello world".titlecase #> "Hello World" (FYI: requires you to first install and load the "activesupport" gem)

"   Hello World   ".strip #> "Hello World"

"Hello World".gsub("Hello", "Goodbye") #> "Goodbye World"
```

Strings also support equality, inclusion, and matching operators:

```ruby
"Hello World" == "Hello World" #> true
"Hello World" == "hello world" #> false

"Hello World".include?("Hello") #> true
"Hello World".include?("hello") #> false

"Hello World".count("l") #> 3
```

Strings are iterable objects comprised of multiple characters. Once you have learned about arrays, or "lists", you can perform additional array-related string operations:

```ruby
"Hello World"[0] #> "H"
"Hello World"[6] #> "W"
"Hello World"[-1] #> "d"
"Hello World"[-3] #> "r"

"Hello World".each_char do |character|
  puts character
end

#>
#> H
#> e
#> l
#> l
#> o
#>  
#> W
#> o
#> r
#> l
#> d

"Hello World".split #> ["Hello", "World"]
"My Title - My Subtitle".split(" - ") #> ['My Title', 'My Subtitle']
"a, b, c, d".split(", ") #> ['a', 'b', 'c', 'd']

str = "
Some
Multi-line
String
"
str.strip.split("\n") #> ['Some', 'Multi-line', 'String']
```
