


ERL - QB64 Phoenix Edition Wiki








# ERL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The ERL function returns the closest previous line number before the last error.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*lastErrorLine&* = ERL
  




## Description


* Used in an error handler to report the last line number used before the error.
* If the program does not use line numbers, then ERL returns 0.
* Use [\_ERRORLINE](/qb64wiki/index.php/ERRORLINE "ERRORLINE") to return the actual code line position of an error in a QB64 program.


  




## Examples


*Example:* Using a fake error code to return the line number position in a program.





| ``` [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR") [GOTO](/qb64wiki/index.php/GOTO "GOTO") errorfix 1 [ERROR](/qb64wiki/index.php/ERROR "ERROR") 250 [ERROR](/qb64wiki/index.php/ERROR "ERROR") 250  5 [ERROR](/qb64wiki/index.php/ERROR "ERROR") 250  [END](/qb64wiki/index.php/END "END") errorfix: [PRINT](/qb64wiki/index.php/PRINT "PRINT") ERL [RESUME](/qb64wiki/index.php/RESUME "RESUME") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |




| ``` 1 1 5  ``` |
| --- |


  




## See also


* [ERR](/qb64wiki/index.php/ERR "ERR")
* [ERROR](/qb64wiki/index.php/ERROR "ERROR")
* [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR")
* [\_ERRORLINE](/qb64wiki/index.php/ERRORLINE "ERRORLINE"), [\_INCLERRORLINE](/qb64wiki/index.php/INCLERRORLINE "INCLERRORLINE"), [\_INCLERRORFILE$](/qb64wiki/index.php/INCLERRORFILE$ "INCLERRORFILE$")
* [ERROR Codes](/qb64wiki/index.php/ERROR_Codes "ERROR Codes")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ERL&oldid=5978>"




## Navigation menu








### Search





















