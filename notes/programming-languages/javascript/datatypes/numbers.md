# JavaScript Language Overview

## Numbers

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number.

```` js
100
-100
0.45
````

Numeric functions include many arithmetic operators:

```` js
100 + 5
100 - 5
100 * 5
100 / 5
````

Indicate order of operations by using parentheses:

```` js
3 + 1 * 2 //=> 5
(3 + 1) * 2 //=> 8
````

Numbers also support equality operators:

```` js
100 == 100 //=> true
100 == 100.0 //=> true
100 == 99 //> false
100 == (99 + 1) //=> true
````

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#Arithmetic_operators for more information about arithmetic operators.

### `Math` Methods

Also reference the functionality of the "Math" object: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math.

```` js
Math.PI //=> 3.141592653589793

Math.random()

Math.round(4.555) //=> 5
Math.ceil(4.555) //=> 5
Math.floor(4.555) //=> 4

Math.min(4,3,7,9) //=> 3
Math.max(4,3,7,9) //=> 9
````
