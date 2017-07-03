# JavaScript

## Debugging

> NOTE: You might want to familiarize yourself with functions before reading this.

Insert a `debugger` statement to drop a break-point in script execution. When the break-point is reached, it will stop and allow you to interact with the state of the code at that particular line.

```` js
debugger;
````

For example:

```` js
function debugStuff(){
  console.log("START OF FUNCTION");
  var x = 100;
  debugger;
  var y = 999;
  console.log("END OF FUNCTION");
}

debugStuff()
x //=> 100
y //=> undefined
````

## Errors

### Throwing Errors

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw.

Raise, or "throw" errors yourself:

```` js
throw "MyError"
throw 4
throw true
````

### Handling Errors

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch.

Handle, or "catch" errors:

```` js
try {
   throw("OOPS")
   console.log("TRYING TO DO STUFF HERE")
} catch (err) {
   console.log(err)
}
````
