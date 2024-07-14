


\_SETBIT - QB64 Phoenix Edition Wiki








# \_SETBIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SETBIT function is used to set a specified bit of a numerical value to 1 (on state).


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*result* = \_SETBIT(*numericalVariable*, *numericalValue*)
  




## Parameters


* *numericalVariable* is the variable to set the bit of and can be of the following types: [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), or [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64").
* Integer values can be signed or [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED").
* *numericalValue* the number of the bit to be set.


  




## Description


* Can be used to manually manipulate individual bits of an integer value by setting them to 1 (on state).
* Setting a bit that is already set to 1 will have no effect.
* Bits start at 0 (so a [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") has bits 0 to 7, [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") 0 to 15, and so on)


  




## Availability


* **Version 1.4 and up**.


  




## Examples


*Example 1:*





| ``` A~%% = 0 '[_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") A~%% A~%% = _SETBIT(A~%%,6) 'set the seventh bit of A~%% [PRINT](/qb64wiki/index.php/PRINT "PRINT") A~%%  ``` |
| --- |




| ```  0  64  ``` |
| --- |


  




## See also


* [\_SHL](/qb64wiki/index.php/SHL "SHL"), [\_SHR](/qb64wiki/index.php/SHR "SHR"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG")
* [\_READBIT](/qb64wiki/index.php/READBIT "READBIT"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")
* [\_RESETBIT](/qb64wiki/index.php/RESETBIT "RESETBIT"), [\_TOGGLEBIT](/qb64wiki/index.php/TOGGLEBIT "TOGGLEBIT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SETBIT&oldid=7405>"




## Navigation menu








### Search





















