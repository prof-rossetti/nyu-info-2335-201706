# Ruby Language Overview

## Functions

Reference:

  + http://ruby-doc.org/core-2.4.1/Module.html#method-i-define_method
  + https://www.ruby-lang.org/en/documentation/quickstart/2/
  + http://ruby-doc.org/docs/keywords/1.9/Object.html#method-i-def

Use a function to define your own custom, re-usable operation. In Ruby, functions are called "methods". Like in other languages, Ruby functions must first be defined before they can be invoked (or called).

Define a function:

```ruby
def do_stuff
  puts "DOING STUFF HERE!"
end
```

Invoke the function:

```ruby
do_stuff #> "DOING STUFF HERE!"
```

If you try to invoke a function before or without defining it, you will see an error like `NameError: undefined local variable or method 'do_stuff' for main:Object`.

You might see some functions invoked by themselves (e.g. `do_stuff`) while others are invoked on objects (e.g. `some_object.do_something_else`). These two approaches illustrate the difference between "functional" and "object-oriented" programming, respectively. To find a comprehensive list of functions available to be called on any given type of object, reference the documentation for that type of object.

### Parameters

Some functions accept parameters which can be passed to the function during its invocation. A function's parameters must be configured during the function's definition.

#### Single Parameter

Define a function with a parameter:

```ruby
def do_stuff_with_param(message)
  puts message
end
```

In this case, `message` is the name of the function's parameter. Invoke it like so:

```ruby
do_stuff_with_param("HELLO!") #> "HELLO!"
```

#### Multiple Parameters

Define a function with multiple parameters:

```ruby
def do_stuff_with_params(message, first_name, last_name)
  puts "'" + message + "' says " + first_name + " " + last_name
end
```

In this case, `message`, `first_name` and `last_name` are the names of the function's parameters. Invoke it like so:

```ruby
do_stuff_with_params("HO! HO! HO!", "Santa", "Claus") #> 'HO! HO! HO!' says Santa Claus
```

> PRO TIP: if your function uses more than a handful of parameters, especially if some of them are optional, consider re-configuring the function to accept a single hash parameter that contains multiple keys, with the key names corresponding to the names of the original parameters.
>
>     def do_stuff_with_params(options)
>       puts "'" + options[:message] + "' says " + options[:first_name] + " " + options[:last_name]
>     end
>    
>     person = {first_name: "Santa", last_name: "Claus", message: "HO! HO! HO!"}
>    
>     do_stuff_with_params(person) #> 'HO! HO! HO!' says Santa Claus




### Returns

Some programming languages require use of the `return` keyword in order to make use of the value returned by the function. But Ruby infers the function's return value based on whatever is returned by the last line of the function:

```ruby
def calculate_area(length, height)
  length * height
end

area = calculate_area(4, 2) #> 8
```

With complex functions, you are sometimes required to use the `return` keyword to explicitly specify the value the function should return:

```ruby
def do_something(my_array_of_numbers)
  new_array = []

  my_array_of_numbers.each do |i|
    new_array << i * 10
  end
end

def do_something2(my_array_of_numbers)
  new_array = []

  my_array_of_numbers.each do |i|
    new_array << i * 10
  end

  return new_array
end

a = [5,3,8]

do_something(a) #> [5, 3, 8]
do_something2(a) #> [50, 30, 80]
```
