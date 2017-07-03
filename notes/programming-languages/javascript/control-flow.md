# JavaScript Language Overview

## Control Flow

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference#Control_flow.

### If

In JavaScript, IF statements are defined using the `if` keyword followed by a set of parentheses (`()`) containing an expression to be evaluated, followed by curly braces (`{}`) which contain statements to be executed if that condition is met.

```` js
if (true) {
  console.log("SWEET")
}

if (!true) {
  console.log("SWEET")
}
````

```` js
if (1 == 1) {
  console.log("SWEET")
}

if (1 == 2) {
  console.log("SWEET")
}
````

```` js
if (undefined) {
  console.log("SWEET")
}

if (!undefined) {
  console.log("SWEET")
}

````

IF statements may be followed by the `else` keyword followed by a set of parentheses (`()`) containing an expression to be evaluated in the event none of the above conditions are met.

```` js
if (1 == 1) {
  console.log("SWEET")
} else {
  console.log("NOPE")
}

if (1 == 2) {
  console.log("SWEET")
} else {
  console.log("NOPE")
}
````

IF statements, regardless of whether or not they contain an ELSE statement, can contain any number of `else if` keywords followed by a set of parentheses (`()`) containing an expression to be evaluated in the event that condition is met.

```` js
var fruit = "Apple"

if (fruit == "Orange") {
  console.log("SWEET")
} else if (fruit == "Banana") {
  console.log("OK")
} else {
  console.log("NOPE")
}
````

As in other languages, statement order matters:

```` js
if (false) {
  console.log("SWEET")
} else if (true) {
  console.log("OK")
} else if (true) {
  console.log("ALSO OK")
} else {
  console.log("NOPE")
}
````

### Switch

Switch statements are essentially case statements.

```` js
var fruit = "Apple"

switch(fruit) {
    case "Orange":
        console.log("SWEET")
        break;
    case "Banana":
        console.log("OK")
        break;
    default:
        console.log("NOPE")
}
````
