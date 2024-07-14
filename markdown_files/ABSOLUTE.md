


CALL ABSOLUTE - QB64 Phoenix Edition Wiki








# CALL ABSOLUTE



From QB64 Phoenix Edition Wiki
(Redirected from [ABSOLUTE](/qb64wiki/index.php?title=ABSOLUTE&redirect=no "ABSOLUTE"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
CALL ABSOLUTE is used to access interrupts on the computer or execute assembly type procedures.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Legacy support](#Legacy_support) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


CALL ABSOLUTE([*argumentList*,] *integerOffset*)
### Legacy support


* CALL ABSOLUTE is implemented to support older code and is not recommended practice. To handle mouse input, use [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") and related functions.


  




## Description


* [CALL](/qb64wiki/index.php/CALL "CALL") and parameter brackets are required in the statement.
* *argumentList* contains the list of arguments passed to the procedure.
* *integerOffset* contains the offset from the current code segment, set by [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") and [SADD](/qb64wiki/index.php/SADD "SADD"), to the starting location of the called procedure.
* QBasic and **QB64** have the ABSOLUTE statement built in and require no library, like QuickBASIC did.
* **NOTE: QB64 does not support INT 33h mouse functions above 3 or [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") in an ABSOLUTE statement. Registers are emulated.**


  




## See also


* [SADD](/qb64wiki/index.php/SADD "SADD"), [INTERRUPT](/qb64wiki/index.php/INTERRUPT "INTERRUPT")
* [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CALL_ABSOLUTE&oldid=6742>"




## Navigation menu








### Search





















