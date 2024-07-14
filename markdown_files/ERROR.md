


ERROR - QB64 Phoenix Edition Wiki








# ERROR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The ERROR statement is used to simulate a program error or to troubleshoot error handling procedures.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


ERROR *codeNumber%*
  




## Description


* Can be used to test an error handling routine by simulating an error.
* Error code 97 can be used to invoke the error handler for your own use, no real error in the program will trigger error 97.
* Use error codes between 100 and 200 for custom program errors that will not be responded to by QB64.


  




## Examples


*Example:* Creating custom error codes for a program that can be handled by an [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR") handling routine.





| ``` [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR") [GOTO](/qb64wiki/index.php/GOTO "GOTO") handler  [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x = 0 [THEN](/qb64wiki/index.php/THEN "THEN") ERROR 123 x = x + 1 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x [THEN](/qb64wiki/index.php/THEN "THEN") ERROR 111  [END](/qb64wiki/index.php/END "END")   handler: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [ERR](/qb64wiki/index.php/ERR "ERR"), [_ERRORLINE](/qb64wiki/index.php/ERRORLINE "ERRORLINE") [BEEP](/qb64wiki/index.php/BEEP "BEEP") [RESUME](/qb64wiki/index.php/RESUME "RESUME") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |


**Note: Don't use error codes under 97 or over 200 as QB64 may respond to those errors and interrupt the program.**
  




## See also


* [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR")
* [ERR](/qb64wiki/index.php/ERR "ERR"), [ERL](/qb64wiki/index.php/ERL "ERL")
* [\_ERRORLINE](/qb64wiki/index.php/ERRORLINE "ERRORLINE")
* [ERROR Codes](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") (list)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ERROR&oldid=5980>"




## Navigation menu








### Search





















