# Ruby Language Overview

## Logging

Output, or "log" an object by passing it as a parameter into a `puts` statement. Printing works from inside an interactive shell as well as inside a script. If scripting, when the script executes you will see the printed logs output onto the command-line.

```ruby
puts "HELLO WORLD" #> HELLO WORLD
```

You can even log multiple objects, including various types of objects:

```ruby
puts "HELLO", "WORLD", 5, {'a': 1, 'c': 3, 'b': 2}
#> HELLO
#> WORLD
#> 5
#> {:a=>1, :c=>3, :b=>2}
```
