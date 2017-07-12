# Ruby Language Overview

## Variables

Use a variable to store some value in the program's temporary memory. Declare a variable using a name and assign its value by using a single equal sign (`=`) followed by the value. Any object can be stored in a variable.

```ruby
my_bool = true
my_int = 10
my_float = 0.45
my_str = "My Message"
my_arr = [1,2,3,4]
my_hash = {a:1, b:2, c:3}
```

If you try to reference a variable that has not yet been defined, you will see an error like `NameError: undefined local variable or method 'my_var'`.

Don't be surprised if a variable's value changes. It is common to overwrite a variable's value by re-assigning it or manipulating it in some way:

```ruby
a = 1
puts a #> 1

a = 2
puts a #> 2

a = a + 1
puts a #> 3
```
