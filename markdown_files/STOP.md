


STOP - QB64 Phoenix Edition Wiki








# STOP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **STOP** statement is used to stop program execution when troubleshooting a program or to suspend event trapping.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


STOP
  




## Description


* STOP used in the QBasic IDE does not close any files or go to the operating system. It returns to the IDE.
* In the QB64 compiler, STOP closes the program window and returns to the IDE when the code is compiled from there.
* STOP is ONLY used for debugging purposes and should not be used to exit programs!
* STOP can also be used to suspend an event trap in the following statements: [KEY(n)](/qb64wiki/index.php/KEY(n) "KEY(n)"), [STRIG(n)](/qb64wiki/index.php/STRIG(n) "STRIG(n)") and [TIMER(n)](/qb64wiki/index.php/TIMER "TIMER"). The trap can be turned back on with [ON](/qb64wiki/index.php/ON "ON") and returns any trap events since **STOP** was used.


  




## Examples


*Example:* When run in the QBasic IDE, the program will return to the IDE at STOP. Press F5 to finish the program.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "start"  [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 3  STOP  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "resumed"  ``` |
| --- |


*Explanation:* QB64 will STOP the program and close the window as it does not have an interpreter to run the rest of the code.
  




## See also


* [END](/qb64wiki/index.php/END "END"), [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")
* [ON](/qb64wiki/index.php/ON "ON"), [OFF](/qb64wiki/index.php/OFF "OFF")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=STOP&oldid=8066>"




## Navigation menu








### Search





















