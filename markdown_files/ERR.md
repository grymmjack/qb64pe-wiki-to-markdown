


ERR - QB64 Phoenix Edition Wiki








# ERR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The ERR function returns the last QBasic error code number.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*errorNum%* = ERR
  




## Description


* If there is no error, the function returns 0
* Can be used in an error handling routine to report the last error code number.


  




## Examples


*Example:* Simulating an error to test a program error handler that looks for a "Subscript out of range" error.





| ``` [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR") [GOTO](/qb64wiki/index.php/GOTO "GOTO") handler  [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [ERROR](/qb64wiki/index.php/ERROR "ERROR") 111  'simulate an error code that does not exist x = x + 1 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x [THEN](/qb64wiki/index.php/THEN "THEN") [ERROR](/qb64wiki/index.php/ERROR "ERROR") 9        'simulate array boundary being exceeded  [END](/qb64wiki/index.php/END "END")  handler: [PRINT](/qb64wiki/index.php/PRINT "PRINT") ERR, [_ERRORLINE](/qb64wiki/index.php/ERRORLINE "ERRORLINE") [BEEP](/qb64wiki/index.php/BEEP "BEEP") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ERR = 9 [THEN](/qb64wiki/index.php/THEN "THEN")   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "The program has encountered an error and needs to close! Press a key!"   K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1)   [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM") [END IF](/qb64wiki/index.php/END_IF "END IF") [RESUME](/qb64wiki/index.php/RESUME "RESUME") [NEXT](/qb64wiki/index.php/NEXT "NEXT")               'RESUME can only be used in error handlers  ``` |
| --- |


  




## See also


* [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR"), [RESUME](/qb64wiki/index.php/RESUME "RESUME")
* [ERL](/qb64wiki/index.php/ERL "ERL")
* [\_ERRORLINE](/qb64wiki/index.php/ERRORLINE "ERRORLINE"), [\_INCLERRORLINE](/qb64wiki/index.php/INCLERRORLINE "INCLERRORLINE"), [\_INCLERRORFILE$](/qb64wiki/index.php/INCLERRORFILE$ "INCLERRORFILE$")
* [ERROR](/qb64wiki/index.php/ERROR "ERROR")
* [ERROR Codes](/qb64wiki/index.php/ERROR_Codes "ERROR Codes")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ERR&oldid=5979>"




## Navigation menu








### Search





















