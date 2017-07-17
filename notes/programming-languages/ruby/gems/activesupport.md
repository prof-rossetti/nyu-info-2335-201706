# Ruby Language Overview

### The `activesupport` Gem

Reference:

  + https://github.com/rails/rails/tree/master/activesupport
  + http://api.rubyonrails.org/classes/ActiveSupport.html
  + http://edgeguides.rubyonrails.org/active_support_core_extensions.html

The `activesupport` gem provides much of the basic underlying functionality of the `rails` gem. But we can also use it on its own.

Install it if necessary:

```shell
gem list activesupport # check to see if it is already installed

gem install activesupport
```

Then use some of its helpful functionality:

```ruby
require 'active_support/all' # note the underscore. important. also note the "/all". also important.

nil.blank? #> true
nil.present? #> false
nil.try(:something) #> nil

"hello world".titlecase #> "Hello World"
" \n  hello\n\r \t world \n".squish #> "hello world"
"whale".pluralize #> "wales"
"whales".singularize #> "wale"

1.week.ago #> 2017-07-02 08:07:42 -0400
1.week.from_now #> 2017-07-16 08:14:59 -0400
Date.today.beginning_of_day #> 2017-07-09 00:00:00 -0400
Date.today.beginning_of_week #> Mon, 03 Jul 2017
Date.today.beginning_of_month #> Sat, 01 Jul 2017
Date.today.beginning_of_year #> Sun, 01 Jan 2017

[1, 2, 3].sum #> 6
teams = [{city: "New York", name: "Yankees"}, {city: "New York", name: "Mets"},{city: "Boston", name: "Red Sox"}, {city: "New Haven", name: "Ravens"}]
teams.pluck(:name) #> ["Yankees", "Mets", "Red Sox", "Ravens"]

{a: 1, b: 2}.merge({c:3, d:4}) #> {:a=>1, :b=>2, :c=>3, :d=>4}
```
