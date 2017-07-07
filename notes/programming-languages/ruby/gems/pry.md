# Ruby Language Overview

### The `pry` Gem

Reference: http://pryrepl.org/.

If using the `pry` module, drop an interactive break-point on any line of code by inserting a `binding.pry` statement. Once you run the script, it will stop at the break-point to allow further investigation:

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
