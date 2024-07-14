


\_TOGGLEBIT - QB64 Phoenix Edition Wiki








# \_TOGGLEBIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_TOGGLEBIT function is used to toggle a specified bit of a numerical value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*result* = \_TOGGLEBIT(*numericalVariable*, *numericalValue*)
  




## Parameters


* *numericalVariable* is the variable to toggle the bit of and can be of the following types: [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), or [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64").
* Integer values can be signed or [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED").
* *numericalValue* the number of the bit to be set.


  




## Description


* Can be used to manually manipulate individual bits of an integer value by toggling their state.
* A bit set to 1 is changed to 0 and a bit set to 0 is changed to 1.
* Bits start at 0 (so a [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") has bits 0 to 7, [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") 0 to 15, and so on)


  




## Availability


* **Version 1.4 and up**.


  




## Examples


*Example 1:*





| ``` A~%% = 0 '[_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") A~%% A~%% = _TOGGLEBIT(A~%%,4) 'toggle the fourth bit of A~%% [PRINT](/qb64wiki/index.php/PRINT "PRINT") A~%% A~%% = _TOGGLEBIT(A~%%,4) 'toggle the fourth bit of A~%% [PRINT](/qb64wiki/index.php/PRINT "PRINT") A~%%  ``` |
| --- |




| ```  0  16  0  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1310)
* [\_SHL](/qb64wiki/index.php/SHL "SHL"), [\_SHR](/qb64wiki/index.php/SHR "SHR"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG")
* [\_SETBIT](/qb64wiki/index.php/SETBIT "SETBIT"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")
* [\_RESETBIT](/qb64wiki/index.php/RESETBIT "RESETBIT"), [\_READBIT](/qb64wiki/index.php/READBIT "READBIT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=TOGGLEBIT&oldid=8930>"




## Navigation menu








### Search





















