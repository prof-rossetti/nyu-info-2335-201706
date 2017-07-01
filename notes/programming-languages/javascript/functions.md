# JavaScript

## Functions

Like in other languages, JavaScript functions must first be defined before they can be invoked (or called).

Define a function:

```` js
function doStuff(){
  console.log("DOING STUFF HERE!")
}
````

Invoke the function:

```` js
doStuff() // NOTE: the trailing parentheses are important. If they are omitted, the function will not be invoked.
````

You might see some functions invoked by themselves (e.g. `doStuff()`) while others are invoked on objects (e.g. `someObject.doSomethingElse()`).

Many of the examples in this language overview involve invoking built-in functions on certain types of objects. To find a comprehensive list of functions available to be called on any given type of object, reference the documentation for that type of object.

### Parameters

Some functions accept parameters which can be passed to the function during its invocation. A function's parameters must be configured during the function's definition.

#### Single Parameter

Define a function with a parameter:

```` js
function doStuffWithParam(message){
  console.log(message)
}
````

In this case, `message` is the name of the function's parameter. Invoke it like so:

```` js
doStuffWithParam("My Message Here")
````

#### Multiple Parameters

Define a function with multiple parameters:

```` js
function doStuffWithParams(message, firstName, lastName){
  console.log("DOING STUFF HERE!")
  console.log(message, "says", firstName, lastName)
}
````

In this case, `message`, `firstName` and `lastName` are the names of the function's parameters. Invoke it like so:

```` js
doStuffWithParams("HO HO HO", "Santa", "Claus")
````

### Returns

Use the `return` keyword when you want to make use of the value returned by the function:

```` js
function calculateArea(length, height){
  length * height
}

var area = calculateArea(4, 2)
area //=> undefined
````

```` js
function calculateArea(length, height){
  return length * height
}

var area = calculateArea(4, 2)
area //=> 8
````
