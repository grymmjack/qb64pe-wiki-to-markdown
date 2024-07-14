


\_INCLERRORFILE$ - QB64 Phoenix Edition Wiki








# \_INCLERRORFILE$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_INCLERRORFILE$ function returns the name of the original source code [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") module that caused the most recent error.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*errfile$* = \_INCLERRORFILE$
  




## Description


If the last error occurred in the main module, \_INCLERRORFILE$ returns an empty string.


  




## Availability


* **Version 1.1 and up**.


  




## Examples


*Example:*





| ``` [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR") [GOTO](/qb64wiki/index.php/GOTO "GOTO") DebugLine  [ERROR](/qb64wiki/index.php/ERROR "ERROR") 250 'simulated error code - an error in the main module leaves _INCLERRORLINE empty (= 0)  '[$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE"):'haserror.bi'  [END](/qb64wiki/index.php/END "END")  DebugLine: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "An error occurred. Please contact support with the following details: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ERROR "; [ERR](/qb64wiki/index.php/ERR "ERR"); " ON LINE: "; [_ERRORLINE](/qb64wiki/index.php/ERRORLINE "ERRORLINE") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [_INCLERRORLINE](/qb64wiki/index.php/INCLERRORLINE "INCLERRORLINE") [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "    IN MODULE "; _INCLERRORFILE$; " (line"; [_INCLERRORLINE](/qb64wiki/index.php/INCLERRORLINE "INCLERRORLINE"); ")" [END IF](/qb64wiki/index.php/END_IF "END IF") [RESUME](/qb64wiki/index.php/RESUME "RESUME") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |




| ``` An error occurred. Please contact support with the following details: ERROR  250  ON LINE:  6  An error occurred. Please contact support with the following details: ERROR  250  ON LINE:  9     IN MODULE haserror.bi ( line 1 )  ``` |
| --- |


  




## See also


* [\_INCLERRORLINE](/qb64wiki/index.php/INCLERRORLINE "INCLERRORLINE")
* [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR"), [ERR](/qb64wiki/index.php/ERR "ERR")
* [ERROR](/qb64wiki/index.php/ERROR "ERROR")
* [ERROR Codes](/qb64wiki/index.php/ERROR_Codes "ERROR Codes")
* [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INCLERRORFILE$&oldid=7310>"




## Navigation menu








### Search





















