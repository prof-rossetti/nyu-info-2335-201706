# Ruby Language Overview

## Hashes

Reference: https://ruby-doc.org/core-2.4.1/Hash.html.

Many programming languages provide an "associative array" datatype  which provides an opportunity to create objects with named attributes. In this way, an associative array is similar to a row in a CSV-formatted spreadsheet or a record in a database, where the associative array's "keys" represent the column names and its "values" represent the cell values. associative arrays are said to have "key/value" pairs, where the "key" represents the name of the attribute and the "value" represents the attribute's value.

city | name | league
--- | --- | ---
New York | Yankees | major
New York | Mets | major
Boston | Red Sox | major
New Haven | Ravens | minor

Ruby's implementation of the associative array concept is known as a "hash". A Ruby hash comprises curly braces (`{}`) containing one or more key/value pairs, with each key separated from its value by a colon (`:`) and each key/value pair separated by a comma (`,`).

```ruby
teams = [
  {city: "New York", name: "Yankees", league: "major"},
  {city: "New York", name: "Mets", league: "major"},
  {city: "Boston", name: "Red Sox", league: "major"},
  {city: "New Haven", name: "Ravens", league: "minor"}
]
```

If you are familiar with JavaScript "objects" (JSON) or Python "dictionaries", the concept is the same. Ruby hashes can even be converted to and from JSON.

Example hashes:

```ruby
{}
{a:1, b:2, c:3}
{a:1, b:2, c:3, fruits:["apple","banana","pear"]} # dictionaries can contain lists
{first:"Santa", last:"Claus", message:"Ho Ho Ho"}
```

Access individual object elements by their key:

```ruby
person = {
  first: "Santa",
  last: "Claus",
  message: "Ho Ho Ho",
  stops: ["New York", "Denver", "San Francisco"]
}

person[:first] #> "Santa"
person[:last] #> "Claus"
person[:message] #> "Ho Ho Ho"
person[:stops] #> ["New York", "Denver", "San Francisco"]
person[:stops][1] #> "Denver" (an array is still an array, even if it exists inside a dictionary!)
```

Add or remove items from an object:

```ruby
person = {
  first: "Santa",
  last: "Claus",
  message: "Ho Ho Ho",
  stops: ["New York", "Denver", "San Francisco"]
}

person[:wife] = "Mrs. Claus"

person.delete(:stops) # this is mutating

person #> {:first=>"Santa", :last=>"Claus", :message=>"Ho Ho Ho", :wife=>"Mrs. Claus"}
```

Make use of built-in methods for easier data-processing:

```ruby
person = {
  first: "Santa",
  last: "Claus",
  message: "Ho Ho Ho",
  stops: ["New York", "Denver", "San Francisco"]
}

person.keys #> [:first, :last, :message, :stops]

person.values #> ["Santa", "Claus", "Ho Ho Ho", ["New York", "Denver", "San Francisco"]]

person.to_a #> [[:first, "Santa"], [:last, "Claus"], [:message, "Ho Ho Ho"], [:stops, ["New York", "Denver", "San Francisco"]]]

person.each do |k,v|
  puts "KEY: #{k} VALUE: #{v}"
end

#> KEY: first ... VALUE: Santa
#> KEY: last ... VALUE: Claus
#> KEY: message ... VALUE: Ho Ho Ho
#> KEY: stops ... VALUE: ["New York", "Denver", "San Francisco"]
```
