


REDIM - QB64 Phoenix Edition Wiki








# REDIM



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
A REDIM statement can re-dimension one [dynamic](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC")(flexible) [array](/qb64wiki/index.php/Arrays "Arrays") or a [comma](/qb64wiki/index.php/Comma "Comma") separated list of arrays.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


REDIM low\_element[[[TO *upper\_element*, ...]}) [[[AS [Type](/qb64wiki/index.php/TYPE "TYPE")]
  




## Description


* Can change the number of elements in an array (the present array data is lost unless [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") is used).
* Dynamic array elements can also be sized or resized by a program user's entry.
* The [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") option also allows the *element* range values to be moved upward or downward in **QB64 only!**
* *Array* is the name of the array to be dimensioned or re-dimensioned.
* *elements* is the number of elements the array should hold. Use the optional [TO](/qb64wiki/index.php/TO "TO") *elements2* to set a range.
* **Always use the same array [TYPE](/qb64wiki/index.php/TYPE "TYPE") suffix ([AS](/qb64wiki/index.php/AS "AS") type) or a new array type with the same name may be created.**
* REDIM cannot change [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC") arrays created with a [DIM](/qb64wiki/index.php/DIM "DIM") statement unless the [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand") is used!
* To create a dynamic array use the [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") metacommand or use REDIM rather than [DIM](/qb64wiki/index.php/DIM "DIM") when first creating the array.
* Use REDIM [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") to change the range or number of array elements without losing the remaining elements. Data may move up or down to accommodate those boundary changes.
* **REDIM [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") cannot change the number of array dimensions or type!**
* [Dynamic](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") arrays MUST be REDIMensioned if [ERASE](/qb64wiki/index.php/ERASE "ERASE") or [CLEAR](/qb64wiki/index.php/CLEAR "CLEAR") are used to clear the arrays as they no longer exist.
* When [AS](/qb64wiki/index.php/AS "AS") is used to declare the type, use [AS](/qb64wiki/index.php/AS "AS") to retain that type or it will change to [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")!
* **NOTE: Many QBasic keyword variable names CAN be used with a [STRING](/qb64wiki/index.php/STRING "STRING") suffix($) ONLY! You CANNOT use them without the suffix, use a numerical suffix or use [DIM](/qb64wiki/index.php/DIM "DIM"), REDIM, [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") or [TYPE](/qb64wiki/index.php/TYPE "TYPE") variable [AS](/qb64wiki/index.php/AS "AS") statements!**
* **Warning! Do not use negative array upper bound index values as OS access or "Out of Memory" [errors](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur!**


  

*Example 1:* The [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") Metacommand allows an array to be re-sized using [DIM](/qb64wiki/index.php/DIM "DIM") and REDIM.





| ``` '[$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC")  [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter array size: ", size [DIM](/qb64wiki/index.php/DIM "DIM") Array(size)  REDIM Array(2 * size)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")(Array)  ``` |
| --- |


  

*Example 2:* Shows the difference between REDIM and REDIM [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE").





| ``` REDIM array(20) array(10) = 24  [PRINT](/qb64wiki/index.php/PRINT "PRINT") array(10)  REDIM [_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") array(30) [PRINT](/qb64wiki/index.php/PRINT "PRINT") array(10)  REDIM array(15) [PRINT](/qb64wiki/index.php/PRINT "PRINT") array(10)  ``` |
| --- |




| ```  24  24  0  ``` |
| --- |


*Explanation:* REDIM without \_PRESERVE erases the array data and cannot change the number of dimensions.
  




## See also


* [Arrays](/qb64wiki/index.php/Arrays "Arrays")
* [DIM](/qb64wiki/index.php/DIM "DIM"), [SHARED](/qb64wiki/index.php/SHARED "SHARED")
* [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE"), [ERASE](/qb64wiki/index.php/ERASE "ERASE")
* [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC"), [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=REDIM&oldid=6608>"




## Navigation menu








### Search





















