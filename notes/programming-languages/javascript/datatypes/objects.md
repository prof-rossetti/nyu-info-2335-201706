# JavaScript Language Overview

## Objects

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object.

JavaScript objects comprise curly braces (`{}`) containing one or more key/value pairs, with the key separated from the value by a colon (`:`) and each key/value pair separated by a comma (`,`). In this respect they resemble Python's "dictionary" datatype or Ruby's "hash" datatype.

**JavaScript Object Notation** is referred to as `JSON`. Files ending in .json contain a javascript object. See this repository's [course.json](/course.json) file for an example.

```` js
{}
{a:1, b:2, c:3}
{a:1, b:2, c:3, fruits:["apple","banana","pear"]} // objects can contain arrays
{first:"Santa", last:"Claus", message:"Ho Ho Ho"}
````

Access individual object elements by their key:

```` js
var person = {first:"Santa", last:"Claus", message:"Ho Ho Ho", stops:["New York", "Denver", "San Francisco"]}
person["first"] //> "Santa"
person["last"] //> "Claus"
person["message"] //> "Ho Ho Ho"
person["stops"] //=> ["New York", "Denver", "San Francisco"]
person["stops"][1] //=> "Denver" (an array is still an array, even if it exists inside a JSON object!)
````

Add or remove items from an object:

```` js
var person = {first:"Santa", last:"Claus", message:"Ho Ho Ho", stops:["New York", "Denver", "San Francisco"]}
person["wife"] = "Mrs. Claus"
delete person["stops"];
person //=> {first: "Santa", last: "Claus", message: "Ho Ho Ho", wife: "Mrs. Claus"}
````

### `Object` Methods

Make use of built-in `Object` methods for easier data-processing:

```` js
var person = {first:"Santa", last:"Claus", message:"Ho Ho Ho", stops:["New York", "Denver", "San Francisco"]}
var keys = Object.keys(person) //> ["first", "last", "message", "stops"]
var vals = Object.values(person) //> ["Santa", "Claus", "Ho Ho Ho", Array[3]]
vals[3] //> ["New York", "Denver", "San Francisco"]
var entries = Object.entries(person) //> [Array[2], Array[2], Array[2], Array[2]]
entries[0] //> ["first", "Santa"]
entries[1] //> ["last", "Claus"]
````
