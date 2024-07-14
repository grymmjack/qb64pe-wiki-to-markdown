


\_ERRORLINE - QB64 Phoenix Edition Wiki








# \_ERRORLINE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ERRORLINE function returns the source code line number that caused the most recent runtime error.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*e%* = \_ERRORLINE
  




## Description


* Used in program error troubleshooting.
* Does not require that the program use line numbers as it counts the actual lines of code.
* The code line can be found using the QB64 IDE (Use the shortcut **Ctrl+G** to go to a specific line) or any other text editor such as Notepad.


  




## Examples


*Example:* Displaying the current program line using a simulated [ERROR](/qb64wiki/index.php/ERROR "ERROR") code.





| ``` [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR") [GOTO](/qb64wiki/index.php/GOTO "GOTO") DebugLine 'can't use GOSUB  [ERROR](/qb64wiki/index.php/ERROR "ERROR") 250 'simulated error code  [END](/qb64wiki/index.php/END "END") DebugLine: [PRINT](/qb64wiki/index.php/PRINT "PRINT") _ERRORLINE [RESUME](/qb64wiki/index.php/RESUME "RESUME") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |


  




## See also


* [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR")
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





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ERRORLINE&oldid=8328>"




## Navigation menu








### Search





















