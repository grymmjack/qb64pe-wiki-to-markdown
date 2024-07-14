


SYSTEM - QB64 Phoenix Edition Wiki








# SYSTEM



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The SYSTEM statement immediately closes a program and returns control to the operating system.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 See also](#See_also) |
| --- |


## Syntax


**SYSTEM** [return\_code%]
  




## Parameters


* QB64 allows a *code* number to be used after SYSTEM to be read in another program module by the [SHELL](/qb64wiki/index.php/SHELL "SHELL") or [\_SHELLHIDE](/qb64wiki/index.php/SHELLHIDE "SHELLHIDE") functions.


  

*Usage:*



* This command should be used to close a program quickly instead of pausing with [END](/qb64wiki/index.php/END "END") or nothing at all.
* A code can be added after the statement to send a value to the [SHELL (function)](/qb64wiki/index.php/SHELL_(function) "SHELL (function)") or [\_SHELLHIDE](/qb64wiki/index.php/SHELLHIDE "SHELLHIDE") function in another module.
* SYSTEM ends the program and closes the window immediately. The last screen image may not be displayed.


  



*QBasic or QuickBASIC:*



* **QBasic BAS files can be run like compiled programs without returning to the IDE when SYSTEM is used to [end](/qb64wiki/index.php/END "END") them!**
* If a program BAS module is run from the IDE, stopped by Ctrl-Break or an error occurs the QB program will exit to the IDE.
* To run a QuickBASIC program without the IDE use the following DOS command line: QB.EXE /L /RUN filename.BAS


  




## See also


* [SHELL (function)](/qb64wiki/index.php/SHELL_(function) "SHELL (function)")
* [\_SHELLHIDE](/qb64wiki/index.php/SHELLHIDE "SHELLHIDE")
* [\_EXIT (function)](/qb64wiki/index.php/EXIT_(function) "EXIT (function)"), [END](/qb64wiki/index.php/END "END")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SYSTEM&oldid=7968>"




## Navigation menu








### Search





















