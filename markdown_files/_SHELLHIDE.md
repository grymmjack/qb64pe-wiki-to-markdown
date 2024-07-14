


\_SHELLHIDE - QB64 Phoenix Edition Wiki








# \_SHELLHIDE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SHELLHIDE function hides the console window and returns any [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") code sent when a program exits.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*returnCode%* = \_SHELLHIDE(*externalCommand$*)
  




## Parameters


* The literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") *externalCommand$* parameter can be any external command or call to another program.


  




## Description


* A QB64 program can return codes specified after [END](/qb64wiki/index.php/END "END") or [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM") calls.
* The *returnCode%* is usually 0 when the external program ends with no errors.


  




## Examples


*Example:* Shelling to another QB64 program will return the exit code when one is set in the program that is run.





| ``` returncode% = _SHELLHIDE("DesktopSize") 'replace call with your program EXE  [PRINT](/qb64wiki/index.php/PRINT "PRINT") returncode%  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Explanation:* To set a program exit code use an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") parameter value after [END](/qb64wiki/index.php/END "END") or [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM") in the called program.
  




## See also


* [SHELL (function)](/qb64wiki/index.php/SHELL_(function) "SHELL (function)")
* [SHELL](/qb64wiki/index.php/SHELL "SHELL"), [\_HIDE](/qb64wiki/index.php/HIDE "HIDE")
* [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE"), [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE")
* [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM"), [END](/qb64wiki/index.php/END "END")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SHELLHIDE&oldid=6534>"




## Navigation menu








### Search





















