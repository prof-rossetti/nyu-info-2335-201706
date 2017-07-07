# Ruby Language Overview

### The `pry` Gem

Reference:

  + http://pryrepl.org/
  + https://github.com/pry/pry

Once you have learned [how to install gems](../package-management.md), you should be able to to install a gem called `pry`, which provides some useful debugging capabilities.

Install `pry` if necessary:

```shell
gem list pry # to see if it is already installed
gem install pry # to install
```

Use the `pry` gem from the command line to enter into an interactive console, or from within a script to debug it using an interactive console.

#### Interactive Console with `pry`

From the command-line:

```shell
pry
#> [1] pry(main)> 2+2
#> => 4
#> [2] pry(main)>
```
#### Debugging Scripts with `pry`

Drop an interactive break-point onto any line in a Ruby script by inserting a `binding.pry` statement. Once you run the script, it will stop at the break-point to allow further investigation:

```ruby
require "pry"

[1, 2, 3, 4, 5].each do |i|
  puts i
  binding.pry if i == 4
end

#> 1
#> 2
#> 3
#> 4
#> [1] pry(main)> i
#> => 4
#> [2] pry(main)>
```

After you are done, type `exit` to step-through to the next break-point. Or type `exit-app` to skip remaining break-points and quit the session.
