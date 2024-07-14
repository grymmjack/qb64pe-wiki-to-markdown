


$STATIC - QB64 Phoenix Edition Wiki








# $STATIC



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $STATIC [metacommand](/qb64wiki/index.php/Metacommand "Metacommand") allows the creation of static (unresizable) arrays.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


{[REM](/qb64wiki/index.php/REM "REM") | ['](/qb64wiki/index.php/Apostrophe "Apostrophe") } $STATIC
  




## Description


* QBasic [Metacommands](/qb64wiki/index.php/Metacommand "Metacommand") require a REM or apostrophy (') before them and are normally placed at the start of the main module.
* Static arrays cannot be resized. If a variable is used to size any array, it becomes [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC").
* A [REDIM](/qb64wiki/index.php/REDIM "REDIM") statement has no effect on $STATIC arrays except perhaps a [duplicate definition error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") at the [REDIM](/qb64wiki/index.php/REDIM "REDIM") statement.
* The array's type cannot be changed once [DIM](/qb64wiki/index.php/DIM "DIM") and a literal value sets the dimensions and element size.
* $STATIC defined program [arrays](/qb64wiki/index.php/Arrays "Arrays") cannot be [re-sized](/qb64wiki/index.php/REDIM "REDIM") or use [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE").


  




## Examples


*Example:* When a variable is used, the array can be resized despite $STATIC. The array becomes [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC").





| ``` '$STATIC  [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter array size: ", size [DIM](/qb64wiki/index.php/DIM "DIM") array(size)   'using an actual number instead of the variable will create an error!  [REDIM](/qb64wiki/index.php/REDIM "REDIM") array(2 * size)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")(array)  ``` |
| --- |


*Note:* [DIM](/qb64wiki/index.php/DIM "DIM") using a literal numerical size will create a Duplicate definition error.
  




## See also


* [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC"), [STATIC](/qb64wiki/index.php/STATIC "STATIC")
* [Arrays](/qb64wiki/index.php/Arrays "Arrays"), [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$STATIC&oldid=5851>"




## Navigation menu








### Search





















