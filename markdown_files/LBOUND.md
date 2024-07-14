


LBOUND - QB64 Phoenix Edition Wiki








# LBOUND



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The LBOUND function returns the smallest valid index (lower bound) of an array dimension.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result%* = LBOUND(*arrayName*[, *dimension%*])
  




## Description


* *arrayName* specifies the name of the array.
* *dimension%* specifies the dimension number, starting with **1** for the first dimension.
	+ If omitted, *dimension%* is assumed to be **1**.
	+ If *dimension%* is less than **1** or is greater than the number of dimensions, a [subscript out of range](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error occurs.
* LBOUND and [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND") are used to determine the range of valid indexes of an array.


  




## Examples




| ``` [DIM](/qb64wiki/index.php/DIM "DIM") myArray(5) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") myOtherArray(1 to 2, 3 to 4) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") LBOUND(myArray) [PRINT](/qb64wiki/index.php/PRINT "PRINT") LBOUND(myOtherArray, 2)  ``` |
| --- |




| ```  0  3  ``` |
| --- |


  




## See also


* [Arrays](/qb64wiki/index.php/Arrays "Arrays"), [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")
* [DIM](/qb64wiki/index.php/DIM "DIM"), [COMMON](/qb64wiki/index.php/COMMON "COMMON"), [STATIC](/qb64wiki/index.php/STATIC "STATIC"), [SHARED](/qb64wiki/index.php/SHARED "SHARED")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LBOUND&oldid=2312>"




## Navigation menu








### Search





















