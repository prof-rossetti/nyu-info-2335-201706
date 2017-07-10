# Ruby Language Overview

## Control Flow

### If Statements

Reference:

  + http://ruby-doc.org/docs/keywords/1.9/Object.html#method-i-if
  + https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

Use "If" statements to handle conditional logic (i.e. checking whether or not something is true and responding accordingly).

In Ruby, an "If" statement is defined using the `if` keyword, followed by a condition to be evaluated, followed by one or more indented lines which contain statement(s) to be executed if the condition is met, finally closed by an `end` keyword.

```ruby

if true
  puts "YES THIS IS TRUE"
end

#> YES THIS IS TRUE

if 1 == 1
  puts "YES THIS IS TRUE"
end

#> YES THIS IS TRUE

if false
  puts "YES THIS IS TRUE"
end

#> nil

if 1 == 2
  puts "YES THIS IS TRUE"
end

#> nil
```

An "If" statement may include an `else` keyword, followed by one or more indented lines which contain statement(s) to be executed if the original condition is not met.

```ruby
if 1 == 2
  puts "YES THIS IS TRUE"
else
  puts "NO THIS IS FALSE"
end

#> NO THIS IS FALSE
```

An "If" statement, regardless of whether or not it contains an `else` keyword, can contain any number of `elsif` keywords, each followed by one or more indented lines which contain statement(s) to be executed if the condition is met. If there is an `else` keyword, it should come last.

```ruby
# run this script a few times in a row...

fruit = ["Apple", "Banana", "Orange"].sample

if fruit == "Orange"
  puts "WE GOT AN ORANGE HERE"
elsif fruit == "Banana"
  puts "WE GOT A BANANA HERE"
elsif fruit == "Peach"
  puts "WE GOT A PEACH HERE"
else
  puts "NOT SURE WHAT WE GOT HERE"
end
```

As in other languages, statement order matters:

```ruby
if true
  puts "First"
elsif true
  puts "Second"
end

#> "First"
```

Hey, did you know about these alternative syntaxes:

```ruby
true ? "YEP THAT'S TRUE" : "NO, THAT'S FALSE" # ternary

a = 5 if true

a = 5 unless false
```

### Case Statements

Reference: http://ruby-doc.org/docs/keywords/1.9/Object.html#method-i-case.

```ruby
# run this script a few times in a row...

fruit = ["Apple", "Banana", "Orange"].sample

case fruit
when "Orange"
  puts "WE GOT AN ORANGE HERE"
when "Banana"
  puts "WE GOT A BANNANA HERE"
when "Peach"
  puts "WE GOT A PEACH HERE"
else
  puts "NOT SURE WHAT WE GOT HERE"
end
```

```ruby
# run this script a few times in a row...

fruit = ["Apple", "Banana", "Orange"].sample

case fruit
when "Orange"
  puts "WE GOT AN ORANGE HERE"
when "Banana", "Peach"
  puts "WE GOT A #{fruit.upcase} HERE"
else
  puts "NOT SURE WHAT WE GOT HERE"
end
```
