# Ruby Language Overview

## Errors

Reference:

  + https://ruby-doc.org/core-2.4.1/StandardError.html
  + https://ruby-doc.org/core-2.4.1/ArgumentError.html
  + https://ruby-doc.org/core-2.4.1/NameError.html
  + https://ruby-doc.org/core-2.4.1/Kernel.html#method-i-raise

### Raising Errors

```ruby
options = ["rock", "paper", "scissors"]

puts "Please choose either 'rock', 'paper', or 'scissors'..."

choice = gets.chomp

if options.include?(choice)
  puts "YOU CHOSE #{choice}"
else
  raise "OOPS - Please type 'rock', or 'paper', or 'scissors' (without using using quotation marks)."
end

# the choice is yours...
```

### Handling Errors

```ruby
begin
  raise StandardError("Hello")
  puts "EVERYTHING IS GOING FINE"
rescue StandardError
  puts "OOPS - MY ERROR"
end

#> OOPS - MY ERROR
```
