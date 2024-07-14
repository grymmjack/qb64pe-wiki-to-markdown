


ALIAS - QB64 Phoenix Edition Wiki








# ALIAS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **ALIAS** clause in a [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") statement block tells the program the name of the procedure used in the external library.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


[DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")
SUB *pseudoname* ALIAS *actualname* [(*parameters*)]
[END DECLARE](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")
  




## Parameters


* The *pseudoname* is the name of the [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") the QB64 program will use.
* The *actualname* is the same procedure name as it is inside of the library code, it may optionally have a prepended namespace specification (e.g. **ALIAS** std::malloc).
* QB64 must use all parameters of imported procedures including optional ones.


  




## Description


* The **ALIAS** name clause is optional as the original library procedure name can be used.
* The procedure name does not have to be inside of quotes when using [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY").
* QB64 does not support optional parameters.


  




## Examples


Example
Instead of creating a wrapper [SUB](/qb64wiki/index.php/SUB "SUB") with the Library statement inside of it, just rename it in the declaration.


| ``` [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")     [SUB](/qb64wiki/index.php/SUB "SUB") MouseMove ALIAS glutWarpPointer ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") xoffset&, [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") yoffset&) [END DECLARE](/qb64wiki/index.php/END_DECLARE "END DECLARE")  [DO UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_SCREENEXISTS](/qb64wiki/index.php/SCREENEXISTS "SCREENEXISTS"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hit a key to move the pointer to top left corner..." [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")  MouseMove 1, 1  ``` |
| --- |




| ``` **Explanation**  When a Library procedure is used to represent another procedure name  use **ALIAS** instead of creating a wrapper [SUB](/qb64wiki/index.php/SUB "SUB"). Just place your name for  the procedure first with the actual Library name after **ALIAS**.  ``` |
| --- |


  




## See also


* [SUB](/qb64wiki/index.php/SUB "SUB"), [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")
* [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ALIAS&oldid=8792>"




## Navigation menu








### Search





















