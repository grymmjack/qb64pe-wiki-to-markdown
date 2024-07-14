


CONST - QB64 Phoenix Edition Wiki








# CONST



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The CONST statement globally defines one or more named numeric or string values which will not change while the program is running.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


CONST *constantName* = *value*[, ...]
  




## Parameters


* *constantName* is the constant name or list of names assigned by the programmer.
* *value* is the value to initialize the global constant which cannot change once defined.
	+ If *constantName* specifies a numeric type, *value* must be a numeric expression containing literals and other constants.
	+ If *constantName* specifies a string type, the *value* must be a literal value.


  




## Description


* The *constantName* does not have to include a type suffix. The datatype is automatically infered by the compiler using the *value*.
* Constant values cannot reference a variable, [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") return values when defined.
	+ The exception to the above are color functions [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") and [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32"), which can be used in a CONST statement. See *Example 2* below.
* Constants cannot be reassigned values. They retain the same value throughout all of the program procedures.
* Constants defined in module-level code have [shared](/qb64wiki/index.php/SHARED "SHARED") scope, so they can also be used in [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures.
* Constants defined in [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures are local to those procedures.
* [CLEAR](/qb64wiki/index.php/CLEAR "CLEAR") will not affect or change constant values.


  




## Examples


*Example 1:* Display the circumference and area of circles:





| ``` ' Declare a numeric constant approximately equal to the ratio of a circle's ' circumference to its diameter: CONST PI = 3.141593  ' Declare some string constants: CONST circumferenceText = "The circumference of the circle is" CONST areaText = "The area of the circle is"  [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")     [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter the radius of a circle or zero to quit"; radius     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") radius = 0 [THEN](/qb64wiki/index.php/IF...THEN "IF...THEN") [END](/qb64wiki/index.php/END "END")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") circumferenceText; 2 * PI * radius     [PRINT](/qb64wiki/index.php/PRINT "PRINT") areaText; PI * radius * radius ' radius squared     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP")  ``` |
| --- |




| ``` Enter the radius of a circle or zero to quit? *10* The circumference of the circle is 62.83186 The area of the circle is 314.1593  Enter the radius of a circle or zero to quit? *123.456* The circumference of the circle is 775.697 The area of the circle is 47882.23  Enter the radius of a circle or zero to quit? *0*  ``` |
| --- |


*Explanation:* PI cannot change as it is a mathematical constant so it is fitting to define it as a constant. Trying to change PI will result in a calculation error.
  

*Example 2*: Using \_RGB32 to set a constant's value.





| ``` CONST Red = _RGB32(255,0,0)  [COLOR](/qb64wiki/index.php/COLOR "COLOR") Red [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello World"  ``` |
| --- |


  




## See also


* [DIM](/qb64wiki/index.php/DIM "DIM"), [SHARED](/qb64wiki/index.php/SHARED "SHARED")
* [STATIC](/qb64wiki/index.php/STATIC "STATIC"), [COMMON](/qb64wiki/index.php/COMMON "COMMON")
* [\_PI](/qb64wiki/index.php/PI "PI"), [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32"), [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")
* [Windows 32 API constant values](http://doc.pcsoft.fr/en-US/?6510001)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CONST&oldid=7244>"




## Navigation menu








### Search





















