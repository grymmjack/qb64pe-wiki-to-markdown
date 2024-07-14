


\_FILEEXISTS - QB64 Phoenix Edition Wiki








# \_FILEEXISTS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_FILEEXISTS** function determines if a designated file name exists and returns true (-1) or false (0).


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*theFileExists%* = \_FILEEXISTS(*filename$*)
  




## Description


* The *filename$* parameter can be a literal or variable [string](/qb64wiki/index.php/STRING "STRING") value that can include a path.
* The function returns -1 when a file exists and 0 when it does not.
* The function reads the system information directly without using a [SHELL](/qb64wiki/index.php/SHELL "SHELL") procedure.
* The function will use the appropriate Operating System path separators. [\_OS$](/qb64wiki/index.php/OS$ "OS$") can determine the operating system.
* **This function does not guarantee that a file can be accessed or opened, just that it exists.**


  




## Examples


*Example:* Checks if a file exists before opening it.





| ``` [IF](/qb64wiki/index.php/IF "IF") _FILEEXISTS("mysettings.ini") [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Settings file found." [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


  




## See also


* [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS"), [\_OS$](/qb64wiki/index.php/OS$ "OS$")
* [SHELL](/qb64wiki/index.php/SHELL "SHELL"), [FILES](/qb64wiki/index.php/FILES "FILES")
* [KILL](/qb64wiki/index.php/KILL "KILL")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FILEEXISTS&oldid=8332>"




## Navigation menu








### Search





















