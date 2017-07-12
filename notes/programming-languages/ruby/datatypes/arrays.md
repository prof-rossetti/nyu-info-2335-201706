# Ruby Language Overview

## Arrays

Reference:
  + https://ruby-doc.org/core-2.4.1/Array.html
  + https://ruby-doc.org/core-2.4.1/Enumerable.html

An Array represents a numbered, ordered collection of items. An array may contain zero or more items. An array can contain items of any datatype, but as a best practice, all items in an array should share a datatype and structure:

```ruby
# DO:

[]
[1,2,3,4]
[100, 75, 33]
["fun", "times", "right?"]
[ {a:1, b:2}, {a:5, b:6}] # arrays can contain hashes
[ [1,2,3], [4,5,6], [7,8,9]] # arrays can be "nested" inside other arrays

# DON'T:
[100, "fun"]
[ {a:1, b:2}, {x:5, z:6}]
```

Like other languages, individual array items can be accessed by their index. Array item indices are zero-based, meaning the index of the first item is 0.

```ruby
arr = ["a", "b", "c", "d"]
arr[0] #> "a"
arr[1] #> "b"
arr[2] #> "c"
arr[3] #> "d"
arr[4] #> nil
arr.first #> "a"
arr.last #> "d"

arr.index("a") #> 0
arr.index("b") #> 1
arr.index("c") #> 2
arr.index("z") #> nil
```

Equality operators apply:

```ruby
[1,2,3] == [1,2,3] #> true
[1,2,3] == [3,2,1] #> false
```

Inclusion operators apply:

```ruby
[1,2,3,4,5].include?(3) #> true
```

Common array functions and operators include:

```ruby
arr = [6,3,9,7]

arr.count #> 4

arr.min #> 3

arr.max #> 9
```

Add an element to the end of an array:

```ruby
arr = ["a", "b", "c", "d"]

arr.push("e") # this is a mutating operation
arr #> ["a", "b", "c", "d", "e"]

arr << "f" # double-left-arrow is maybe the more common way. also mutating
arr #> ["a", "b", "c", "d", "e", "f"]
```

Concatenate two arrays:

```ruby
arr = ["a", "b", "c", "d"]
arr2 = ["x", "y", "z"]
arr3 = arr + arr2 #> ["a", "b", "c", "d", "x", "y", "z"]

arr4 = arr3 - arr2 #> ["a", "b", "c", "d"]
```

Flatten an array of arrays:

```ruby
[[1,2,3,4], [5,6,7], [8,9,10]].flatten #> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Remove duplicate values in an array:

```ruby
[1,2,2,2,3].uniq #> [1, 2, 3]
```

Perform randomness-related operations on arrays:

```ruby
arr = [1,2,3,4,5,6,7,8,9]

arr.shuffle #> [7, 8, 5, 4, 6, 2, 3, 1, 9]
arr.shuffle #> [7, 1, 6, 4, 8, 5, 2, 3, 9]
arr.shuffle #> [2, 4, 9, 3, 8, 6, 1, 7, 5]

arr.sample #> 2
arr.sample #> 4
arr.sample #> 4

arr.sample(5) #> [8, 9, 2, 1, 5]
```

### Iteration

Reference:

  + https://ruby-doc.org/core-2.4.1/Array.html#method-i-each
  + https://ruby-doc.org/core-2.4.1/Array.html#method-i-map
  + https://ruby-doc.org/core-2.4.1/Enumerable.html#method-i-reduce

Arrays can be iterated, or "looped" using the `each` function:

```ruby
["a", "b", "c", "d"].each do |letter|
  puts letter
end

#> a
#> b
#> c
#> d
```

A common pattern is to loop through one array to populate the contents of another:

```ruby
arr = [1, 2, 3, 4]
arr2 = []

arr.each do |i|
  arr2 << i * 100
end

arr #> [1, 2, 3, 4]
arr2 #> [100, 200, 300, 400]
```

Arrays can be looped in-place using the `map` function.

```ruby
arr = [1, 2, 3, 4]

arr2 = arr.map{|i| i * 100 } #> [100, 200, 300, 400]
```







### Sorting

Sort an array:

```ruby
arr = [6,3,8]
arr2 = arr.sort #> [3, 6, 8]
arr3 = arr2.reverse #> [8, 3, 6]
```

If you have an array full of hashes, sort by hash values:

```ruby
teams = [
  {city: "New York", name: "Yankees"},
  {city: "New York", name: "Mets"},
  {city: "Boston", name: "Red Sox"},
  {city: "New Haven", name: "Ravens"}
]

teams.sort_by{|team| team[:name] } #> [{:city=>"New York", :name=>"Mets"}, {:city=>"New Haven", :name=>"Ravens"}, {:city=>"Boston", :name=>"Red Sox"}, {:city=>"New York", :name=>"Yankees"}]

teams.sort_by{|team| team[:city] } #> [{:city=>"Boston", :name=>"Red Sox"}, {:city=>"New Haven", :name=>"Ravens"}, {:city=>"New York", :name=>"Mets"}, {:city=>"New York", :name=>"Yankees"}]

teams.sort_by{|team| "#{team[:city]}-#{team[:name]}" } #> [{:city=>"Boston", :name=>"Red Sox"}, {:city=>"New Haven", :name=>"Ravens"}, {:city=>"New York", :name=>"Mets"}, {:city=>"New York", :name=>"Yankees"}]
```





















### Filtering

Reference:

  + https://ruby-doc.org/core-2.4.1/Enumerable.html#method-i-find
  + https://ruby-doc.org/core-2.4.1/Array.html#method-i-select
  + https://ruby-doc.org/core-2.4.1/Enumerable.html#method-i-reject

Use the `find` and `select` functions to select a subset of item(s) from an array - only those items which match a given condition:

```ruby
arr = [1,2,4,8,16]

arr.select{|i| true} #> [1, 2, 4, 8, 16]
arr.select{|i| i == 2} #> [2]
arr.select{|i| i > 2} #> [4, 8, 16]
arr.select{|i| i > 102} #> []

arr.find{|i| true} #> 1
arr.find{|i| i == 2} #> 2
arr.find{|i| i > 2} #> 4
arr.find{|i| i > 102} #> nil

arr.reject{|i| i == 2} #> [1, 4, 8, 16]
```



If your array is full of hashes, you can filter based on their attribute values:

```ruby
teams = [
  {city: "New York", name: "Yankees"},
  {city: "New York", name: "Mets"},
  {city: "Boston", name: "Red Sox"},
  {city: "New Haven", name: "Ravens"}
]

teams.find{|team| team[:name] == "Yankees" } #> {:city=>"New York", :name=>"Yankees"}
teams.select{|team| team[:city] == "New York" } #> [{:city=>"New York", :name=>"Yankees"}, {:city=>"New York", :name=>"Mets"}]
teams.select{|team| team[:city] == "New Haven" } #> [{:city=>"New Haven", :name=>"Ravens"}]
teams.select{|team| team[:city].include?("New") } #> [{:city=>"New York", :name=>"Yankees"}, {:city=>"New York", :name=>"Mets"}, {:city=>"New Haven", :name=>"Ravens"}]

teams.reject{|team| team[:city] == "Boston" } #> [{:city=>"New York", :name=>"Yankees"}, {:city=>"New York", :name=>"Mets"}, {:city=>"New Haven", :name=>"Ravens"}]
```
