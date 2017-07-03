
### Strings

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String.

```` js
"Hello World"
````

Example string functions:

```` js
"Hello".toUpperCase() //=> "HELLO"
"Hello" + "World" //=> "Hello World" (string concatenation)
"Hello World".split(" ") //=> ["Hello", "World"]
"Hello World".includes("Hel") //=> true
"Hello World".includes("Gur") //=> false
````

Strings also support equality operators:

```` js
"Hello" == "Hello" //=> true
"Hello" == "Hel" //=> false
````
