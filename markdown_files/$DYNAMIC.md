


$DYNAMIC - QB64 Phoenix Edition Wiki








# $DYNAMIC



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $DYNAMIC [metacommand](/qb64wiki/index.php/Metacommand "Metacommand") allows the creation of dynamic (resizable) arrays.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


{[REM](/qb64wiki/index.php/REM "REM") | ['](/qb64wiki/index.php/Apostrophe "Apostrophe") } $DYNAMIC
  




## Description


* QBasic [metacommands](/qb64wiki/index.php/Metacommand "Metacommand") require [REM](/qb64wiki/index.php/REM "REM") or [apostrophe](/qb64wiki/index.php/Apostrophe "Apostrophe") (') before them and are normally placed at the start of the main module.
* Dynamic arrays can be resized using [REDIM](/qb64wiki/index.php/REDIM "REDIM"). The array's type cannot be changed.
* All data in the array will be lost when [REDIMensioned](/qb64wiki/index.php/REDIM "REDIM") except when [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") is used.
* [REDIM](/qb64wiki/index.php/REDIM "REDIM") [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") can preserve and may move the previous array data when the array boundaries change.
* [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") allows the [upper](/qb64wiki/index.php/UBOUND "UBOUND") and [lower](/qb64wiki/index.php/LBOUND "LBOUND") boundaries of an array to be changed. The number of dimensions cannot change.
* $DYNAMIC arrays must be [REDIMensioned](/qb64wiki/index.php/REDIM "REDIM") if [ERASE](/qb64wiki/index.php/ERASE "ERASE") or [CLEAR](/qb64wiki/index.php/CLEAR "CLEAR") are used as the arrays are removed completely.


  




## Examples


*Example:* [REDIMing](/qb64wiki/index.php/REDIM "REDIM") a $DYNAMIC array using [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") to retain previous array values.





| ``` [REM](/qb64wiki/index.php/REM "REM") $DYNAMIC             'create dynamic arrays only [DIM](/qb64wiki/index.php/DIM "DIM") array(10)            'create array with 11 elements [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 10   array(i) = i: [PRINT](/qb64wiki/index.php/PRINT "PRINT") array(i); 'set and display element values [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [REDIM](/qb64wiki/index.php/REDIM "REDIM") [_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") array(10 [TO](/qb64wiki/index.php/TO "TO") 20) [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 10 [TO](/qb64wiki/index.php/TO "TO") 20   [PRINT](/qb64wiki/index.php/PRINT "PRINT") array(i); [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ``` 0  1  2  3  4  5  6  7  8  9  10  0  1  2  3  4  5  6  7  8  9  10  ``` |
| --- |


  




## See also


* [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC"), [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE")
* [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM"), [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE")
* [STATIC](/qb64wiki/index.php/STATIC "STATIC")
* [ERASE](/qb64wiki/index.php/ERASE "ERASE"), [CLEAR](/qb64wiki/index.php/CLEAR "CLEAR")
* [Arrays](/qb64wiki/index.php/Arrays "Arrays"), [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$DYNAMIC&oldid=8204>"




## Navigation menu








### Search





















