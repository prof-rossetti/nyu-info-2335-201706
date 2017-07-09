# JavaScript Language Overview

## Arrays

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array.

Arrays are ordered lists. Arrays contain zero or more elements. Arrays can contain elements of any type. As a best practice, array elements should share a datatype and structure:

```` js
// DO:

[]
[1,2,3,4]
[100, 75, 33]
["fun", "times", "right?"]
[ {a:1, b:2}, {a:5, b:6}] // arrays can contain objects
[ [1,2,3], [4,5,6], [7,8,9]] // arrays can be "nested" inside other arrays

// DON'T:
[100, "fun"]
[ {a:1, b:2}, {c:5, d:6}]
````

Like other languages, individual array elements can be accessed by their index. Array indices are zero-based, meaning the index of the first element in an array is 0.

```` js
var arr = ["a", "b", "c", "d"]
arr[0] //=> "a"
arr[1] //=> "b"
arr[2] //=> "c"
arr[3] //=> "d"
arr[4] //=> undefined

arr.indexOf("a") //> 0
arr.indexOf("b") //> 1
arr.indexOf("c") //> 2
arr.indexOf("z") //> -1 (applies to any item not found in the array)
````

Common array functions and operators include:

```` js
var arr = ["a", "b", "c", "d"]
a.length //=> 4
arr.includes("a") //=> true
arr.includes("z") //=> false
````

Add an element to the end of an array:

```` js
var arr = ["a", "b", "c", "d"]
arr.push("e") //> "e"
arr //> ["a", "b", "c", "d", "e"] (MUTATING)
````

Concatenate two arrays:

```` js
var arr = ["a", "b", "c", "d"]
var arr2 = ["x", "y", "z"]
var arr3 = arr.concat(arr2)
arr //=> ["a", "b", "c", "d"] (NON-MUTATING)
arr2 //=> ["x", "y", "z"] (NON-MUTATING)
arr3 //=> "a", "b", "c", "d", "x", "y", "z"]
````

### Iteration

Arrays can be iterated, or "looped" using the `forEach()` function:

```` js
var arr = ["a", "b", "c", "d"]

arr.forEach(function(item, index, array) { // uses all available params
  console.log(item, index);
})

arr.forEach(function(item) { // uses the most simple params possible
  console.log(item);
})
````

A common pattern is to loop through one array to populate the contents of another:

```` js
var arr = [1, 2, 3, 4]
var arr2 = []

arr.forEach(function(item) {
  arr2.push(item * 100)
})

arr //=> [1, 2, 3, 4]
arr2  //=> [100, 200, 300, 400]
````

Arrays can be looped "in-place" using the `map()` function:

```` js
var arr = [1, 2, 3, 4]

var arr2 = arr.map(function(x){
  return x * 100
})

arr2 //=> [100, 200, 300, 400]
````

> NOTE: remember to use the `return` keyword when mapping.

### Filtering

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter.

Use the `filter()` function to select a subset of items from an array - only those items matching a given condition.

```` js
var arr = [1,2,4,8,16]
arr.filter(function(i){ return true })
arr.filter(function(i){ return i == 2})
arr.filter(function(i){ return i != 2})
arr.filter(function(i){ return i > 2})
arr.filter(function(i){ return i <= 2})
arr.filter(function(i){ return i > 102})
````

```` js
var teams = [{city:"New York", name:"Yankees"}, {city:"New York", name:"Mets"}, {city:"Boston", name:"Red Sox"}]
teams.filter(function(obj){ return obj["name"] == "Yankees" })
teams.filter(function(obj){ return obj["city"] == "New York" })
teams.filter(function(obj){ return obj["city"] == "New Haven" })
teams.filter(function(obj){ return obj["city"].includes("New") })
````

> Note: the `filter()` function returns an Array, even if it is empty or only contains one item.

### Finding

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find.

Use the `find()` function to select a single items from an array - only the first item matching a given condition.

```` js
var arr = [1,2,4,8,16]
arr.find(function(i){ return true })
arr.find(function(i){ return i == 2})
arr.find(function(i){ return i != 2})
arr.find(function(i){ return i > 2})
arr.find(function(i){ return i <= 2})
arr.find(function(i){ return i > 102})
````

```` js
var teams = [{city:"New York", name:"Yankees"}, {city:"New York", name:"Mets"}, {city:"Boston", name:"Red Sox"}]
teams.find(function(obj){ return obj["name"] == "Yankees" })
teams.find(function(obj){ return obj["city"] == "New York" })
teams.find(function(obj){ return obj["city"] == "New Haven" })
teams.find(function(obj){ return obj["city"].includes("New") })

````

> Note: the `find()` function returns a single value, or undefined.
