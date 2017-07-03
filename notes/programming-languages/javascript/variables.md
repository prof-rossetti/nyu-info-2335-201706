# JavaScript Language Overview

## Variables

Declare a variable using the syntax `var` then the name of the variable, then assign its value by using a single equal sign (`=`) followed by the value. Any datatype can be stored in a variable.

```` js
var i = 10
var f = 0.45
var s = "My Message"
var d = new Date(2017,02,23)
var a = [1,2,3,4]
var o = {}
var f = function(){ console.log("LOGGING FROM INSIDE A FUNCTION") }

// REFRESHER ON FUNCTION INVOCATION:
f //=> function (){ console.log("LOGGING FROM INSIDE A FUNCTION") }
f() //> LOGGING FROM INSIDE A FUNCTION
````

> NOTE: when assigning a value, use a single equal sign (`=`).

Variables can be defined without yet being assigned a value. In this case, the variable's value is said to be "undefined".

```` js
var g; //=> undefined
g = 100
g //=> 100
````
