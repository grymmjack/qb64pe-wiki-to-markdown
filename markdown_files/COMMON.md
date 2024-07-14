


COMMON - QB64 Phoenix Edition Wiki








# COMMON



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
COMMON shares common variable values with other linked or [CHAINed](/qb64wiki/index.php/CHAIN "CHAIN") modules.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Legacy support](#Legacy_support) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


COMMON [SHARED] variableList
### Legacy support


* The multi-modular technique goes back to when **QBasic** and **QuickBASIC** had module size constraints. In **QB64** the COMMON statement has been implemented so that that older code can still be compiled, though it is advisable to use single modules for a single project (not counting [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") libraries), for ease of sharing and also because the module size constraints no longer exist.


  




## Description


* COMMON must be called before any executable statements.
* [SHARED](/qb64wiki/index.php/SHARED "SHARED") makes the variables shared within [SUB](/qb64wiki/index.php/SUB "SUB") and [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures within that module.
* variableList is the list of common variables made available separated by commas.
* Remember to keep the variable type *order* the same in all modules, as the variables names don't matter.
* [COMMON SHARED](/qb64wiki/index.php/COMMON_SHARED "COMMON SHARED") is most commonly used to share the variables with subs and functions of that module.
* **Note: Values assigned to shared variables used as procedure call parameters will not be passed to other procedures. The shared variable value must be assigned inside of the [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedure to be passed.**


  




## See also


* [COMMON SHARED](/qb64wiki/index.php/COMMON_SHARED "COMMON SHARED"), [CHAIN](/qb64wiki/index.php/CHAIN "CHAIN")
* [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM"), [SHARED](/qb64wiki/index.php/SHARED "SHARED")
* [DEFSTR](/qb64wiki/index.php/DEFSTR "DEFSTR"), [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG"), [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT"), [DEFSNG](/qb64wiki/index.php/DEFSNG "DEFSNG"), [DEFDBL](/qb64wiki/index.php/DEFDBL "DEFDBL")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=COMMON&oldid=7240>"




## Navigation menu








### Search





















