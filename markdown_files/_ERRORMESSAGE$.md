


\_ERRORMESSAGE$ - QB64 Phoenix Edition Wiki








# \_ERRORMESSAGE$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ERRORMESSAGE$ function returns a human-readable description of the most recent runtime error, or the description of an arbitrary error code passed to it.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*e$* = \_ERRORMESSAGE$
*e$* = \_ERRORMESSAGE$(*errorCode%*)
  




## Description


* Used in program error troubleshooting.
* The message returned is identical to the message shown in the dialog box that appears if your program has no error handler. See [ERROR Codes](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") for the full list of error codes and their messages.


  




## Examples


*Example 1:* Using an error handler that ignores any error.





| ``` [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR") [GOTO](/qb64wiki/index.php/GOTO "GOTO") Errhandler ' Main module program error simulation code [ERROR](/qb64wiki/index.php/ERROR "ERROR") 7 ' simulate an Out of Memory Error [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Error handled...ending program" [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 4 [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM") ' end of program code  Errhandler: ' error handler sub program line label [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Error"; [ERR](/qb64wiki/index.php/ERR "ERR"); "on program file line"; [_ERRORLINE](/qb64wiki/index.php/ERRORLINE "ERRORLINE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Description: "; _ERRORMESSAGE$; "." [BEEP](/qb64wiki/index.php/BEEP "BEEP") ' warning beep [RESUME](/qb64wiki/index.php/RESUME "RESUME") [NEXT](/qb64wiki/index.php/NEXT "NEXT") ' moves program to code following the error.  ``` |
| --- |


  




## See also


* [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR")
* [\_ERRORLINE](/qb64wiki/index.php/ERRORLINE "ERRORLINE")
* [\_INCLERRORLINE](/qb64wiki/index.php/INCLERRORLINE "INCLERRORLINE"), [\_INCLERRORFILE$](/qb64wiki/index.php/INCLERRORFILE$ "INCLERRORFILE$")
* [ERR](/qb64wiki/index.php/ERR "ERR"), [ERL](/qb64wiki/index.php/ERL "ERL")
* [ERROR](/qb64wiki/index.php/ERROR "ERROR")
* [ERROR Codes](/qb64wiki/index.php/ERROR_Codes "ERROR Codes")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ERRORMESSAGE$&oldid=8329>"




## Navigation menu








### Search





















