


DIM - QB64 Phoenix Edition Wiki








# DIM



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The DIM statement is used to declare a variable or a list of variables as a specified data type or to dimension [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC") or [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") [arrays](/qb64wiki/index.php/Arrays "Arrays").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*To declare variables:*
DIM  [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] *type*}] [, *variable2*...
*To declare arrays:*
DIM  [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] *type*}] [, *variable2*...]
 ***QB64** Alternative Syntax:*
DIM [[[SHARED] [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] *type* *variable* [, *variable2*...]
DIM [[[SHARED] [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] *type* *array([lowest% [TO](/qb64wiki/index.php/TO "TO")] highest%])* [, *array2(elements)*...]
  




## Description


* Sets the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") range of elements (indices) of a [STATIC](/qb64wiki/index.php/STATIC "STATIC") array. If only one number is used, the [lowest boundary](/qb64wiki/index.php/LBOUND "LBOUND") is 0 by default.
* When used before an array is dimensioned, **[OPTION BASE](/qb64wiki/index.php/OPTION_BASE "OPTION BASE") 1** can set the default [lower boundary](/qb64wiki/index.php/LBOUND "LBOUND") of arrays to 1.
* DIM [SHARED](/qb64wiki/index.php/SHARED "SHARED") shares variable values with sub-procedures without passing the value in a parameter.
* Use the [AS](/qb64wiki/index.php/AS "AS") keyword to define a variable or array *type* [AS](/qb64wiki/index.php/AS "AS")...
	+ [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") (or use variable suffix **%**)
	+ [LONG](/qb64wiki/index.php/LONG "LONG") (or use variable suffix **&**)
	+ [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") (or use variable suffix **!** or no suffix by default)
	+ [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") (or use variable suffix **#**)
	+ [STRING](/qb64wiki/index.php/STRING "STRING") (or use variable suffix **$**). An AS multiplier can set the string [length](/qb64wiki/index.php/LEN "LEN"). Ex: DIM *variable* AS STRING \* 8
* **QB64** variable types:
	+ [\_BIT](/qb64wiki/index.php/BIT "BIT") (or use variable suffix **`**). An AS multiplier can be used for multiple bits. Ex: DIM *variable* AS \_BIT \* 8
	+ [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") (or use variable suffix **%%**)
	+ [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") (or use variable suffix **&&**)
	+ [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") (or use variable suffix **##**)
	+ [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") (or use variable suffix **%&**)
	+ DIM AS [\_MEM](/qb64wiki/index.php/MEM "MEM") (the \_MEM type has no type suffix).
* **Note: When a variable has not been defined or has no type suffix, the type defaults to [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE").**
* When using the **AS type variable-list** syntax, type symbols cannot be used.
* When the [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") metacommand or [REDIM](/qb64wiki/index.php/REDIM "REDIM") is used, array element sizes are changeable (not [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC")).
* Use [REDIM](/qb64wiki/index.php/REDIM "REDIM") instead of DIM to dimension arrays as dynamic without the [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") metacommand.
* Use [REDIM](/qb64wiki/index.php/REDIM "REDIM") [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") in **QB64** to retain previous array values when changing the size of an array.
* [REDIM](/qb64wiki/index.php/REDIM "REDIM") [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") cannot change the number of array dimensions. An [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.
* [Dynamic](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") arrays MUST be [REDIMensioned](/qb64wiki/index.php/REDIM "REDIM") if [ERASE](/qb64wiki/index.php/ERASE "ERASE") or [CLEAR](/qb64wiki/index.php/CLEAR "CLEAR") are used, as the arrays are completely removed.
* All numerical variable types **except** [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") and [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") can be dimensioned as [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") (suffix ~) or positive only.
* **NOTE:** Many QBasic keyword variable names can be used with a [STRING](/qb64wiki/index.php/STRING "STRING") suffix ($). You cannot use them without the suffix, use a numerical suffix or use *DIM, [REDIM](/qb64wiki/index.php/REDIM "REDIM"), [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") or [TYPE](/qb64wiki/index.php/TYPE "TYPE") variable [AS](/qb64wiki/index.php/AS "AS")* statements. **Although possible, it's recommended to avoid using reserved names.**
* **Warning: Do not use negative array upper bound index values, or OS access or "Out of Memory" [errors](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.**


  




## Examples


*Example 1:* Defines Qt variable as a one byte fixed length string.





| ```  DIM Qt [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 1  ``` |
| --- |


*Example 2:* Dimensions and types an array.





| ```  DIM Image(2000) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  ``` |
| --- |


*Example 3:* Dimensions array with an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") type suffix.





| ```  DIM Image%(2000)  ``` |
| --- |


*Example 4:* Dimensions a range of [array](/qb64wiki/index.php/Arrays "Arrays") elements as [SHARED](/qb64wiki/index.php/SHARED "SHARED") integers.





| ```  DIM [SHARED](/qb64wiki/index.php/SHARED "SHARED") Image(1 [TO](/qb64wiki/index.php/TO "TO") 1000) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  ``` |
| --- |


*Example 5:* Dimensions variable as an [array](/qb64wiki/index.php/Arrays "Arrays") of 8 elements of the type [UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") BIT.





| ```  DIM bit(8) [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BIT](/qb64wiki/index.php/BIT "BIT")  ``` |
| --- |


  

*Example 6:* QB64 is more flexible than QBasic when it comes to "Duplicate Definition" errors. The following code does not error:





| ``` x = 1 'x is a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") variable [PRINT](/qb64wiki/index.php/PRINT "PRINT") x DIM x [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") [PRINT](/qb64wiki/index.php/PRINT "PRINT") x  ``` |
| --- |


*Explanation:* The [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") variable can be differentiated from the [LONG](/qb64wiki/index.php/LONG "LONG") x variable by using suffixes like x! or x& in later code.
  

*Example 7:* The following code will create a "Name already in use" **status error** in QB64 when the variable types are the same.





| ``` x = 1 'x is a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") variable [PRINT](/qb64wiki/index.php/PRINT "PRINT") x DIM x [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") x  ``` |
| --- |


*Explanation:* QB64 gives an error because the creation of the new variable would make referring to the existing one impossible.
  

*Example 8:* Using QB64's alternative syntax to declare multiple variables/arrays of the same type.





| ``` DIM [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") w, h, id, weight, index 'all of these variables are created as type LONG DIM [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") x, y, z               'all of these variables are created as type SINGLE  ``` |
| --- |


  




## See also


* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE")
* [REDIM](/qb64wiki/index.php/REDIM "REDIM"), [TYPE](/qb64wiki/index.php/TYPE "TYPE")
* [ERASE](/qb64wiki/index.php/ERASE "ERASE"), [CLEAR](/qb64wiki/index.php/CLEAR "CLEAR")
* [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT"), [DEFSNG](/qb64wiki/index.php/DEFSNG "DEFSNG"), [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG"), [DEFDBL](/qb64wiki/index.php/DEFDBL "DEFDBL"), [DEFSTR](/qb64wiki/index.php/DEFSTR "DEFSTR")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations"), [Arrays](/qb64wiki/index.php/Arrays "Arrays")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")
* [OPTION \_EXPLICIT](/qb64wiki/index.php/OPTION_EXPLICIT "OPTION EXPLICIT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DIM&oldid=6589>"




## Navigation menu








### Search





















