# Ruby Language Overview

### The `activesupport` Gem

Reference:

  + https://github.com/rails/rails/tree/master/activesupport
  + http://api.rubyonrails.org/classes/ActiveSupport.html

The `activesupport` gem provides much of the basic underlying functionality of the `rails` gem. But we can also use it on its own.

Install it if necessary:

```shell
gem list activesupport # check to see if it is already installed

gem install activesupport
```

Then use some of its helpful functionality:

```ruby
require 'active_support/all' # note the underscore. important.

"hello world".titlecase
```
