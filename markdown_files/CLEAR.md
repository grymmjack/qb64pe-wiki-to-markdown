


CLEAR - QB64 Phoenix Edition Wiki








# CLEAR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The CLEAR statement clears all variable and array element values in a program.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


CLEAR [, *ignored&* , *ignored&*]
  




## Description


* All parameters are optional and ignored by **QB64**.
* Normally used to clear all program variable and [array](/qb64wiki/index.php/Arrays "Arrays") values where numerical values become zero and string values become empty ("").
* It does not clear [constant](/qb64wiki/index.php/CONST "CONST") values.
* Closes all opened files.
* [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") or [REDIM](/qb64wiki/index.php/REDIM "REDIM") arrays will need to be [redimensioned](/qb64wiki/index.php/REDIM "REDIM") or an [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur when referenced because they are removed.


  




## Examples


*Example:* Using CLEAR to clear array elements from [static](/qb64wiki/index.php/STATIC "STATIC") arrays or arrays created using [DIM](/qb64wiki/index.php/DIM "DIM").





| ``` [CLS](/qb64wiki/index.php/CLS "CLS") [DIM](/qb64wiki/index.php/DIM "DIM") array(10)   'create a [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC") array array(5) = 23  [PRINT](/qb64wiki/index.php/PRINT "PRINT") array(5)  CLEAR  [PRINT](/qb64wiki/index.php/PRINT "PRINT") array(5)  ``` |
| --- |


*Note:* If you change DIM to REDIM a "Subscript out of range" error will occur because a [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") array is removed by CLEAR.
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1223)
* [ERASE](/qb64wiki/index.php/ERASE "ERASE")
* [REDIM](/qb64wiki/index.php/REDIM "REDIM"), [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE")
* [Arrays](/qb64wiki/index.php/Arrays "Arrays")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CLEAR&oldid=9011>"




## Navigation menu








### Search





















