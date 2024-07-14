


\_SHL - QB64 Phoenix Edition Wiki








# \_SHL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SHL function is used to shift the bits of a numerical value to the left.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*result* = \_SHL(*numericalVariable*, *numericalValue*)
  




## Parameters


* *numericalVariable* is the variable to shift the bits of and can be of the following types: [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"),[\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64"), or [\_BYTE](/qb64wiki/index.php/BYTE "BYTE").
* Integer values can be signed or [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED").
* *numericalValue* is the number of places to shift the bits.
* While 0 is a valid value it will have no affect on the variable being shifted.


  




## Description


* Allows for multiplication of a value by 2 faster than normal multiplication (see example 2 below).
* Bits that reach the end of a variable's bit count are dropped (when using a variable of the same type - otherwise they will carry over).
* The type of variable used to store the results should match the type of the variable being shifted.


  




## Availability


* **Version 1.3 and up**.


  




## Examples


*Example 1:*





| ``` A~%% = 1 'set right most bit of an[_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") A~%% [PRINT](/qb64wiki/index.php/PRINT "PRINT") _SHL(A~%%,7) B~%% = _SHL(A~%%,8) 'shift the bit off the left 'edge' [PRINT](/qb64wiki/index.php/PRINT "PRINT") B~%%  ``` |
| --- |




| ```  1  128  0  ``` |
| --- |


  

*Example 2:*





| ``` A~%% = 1 [FOR](/qb64wiki/index.php/FOR "FOR") I%% = 0 [TO](/qb64wiki/index.php/TO "TO") 8     [PRINT](/qb64wiki/index.php/PRINT "PRINT") _SHL(A~%%, I%%) [NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") I%%  ``` |
| --- |




| ```    1    2    4    8   16   32   64  128  256  ``` |
| --- |


* Note: When directly [PRINTing](/qb64wiki/index.php/PRINT "PRINT") to screen, the result is calculated internally using a larger variable type so the left most bit is carried to the next value.
	+ To avoid this store the result in a variable of the same type before printing.


  




## See also


* [\_SHR](/qb64wiki/index.php/SHR "SHR"), [\_ROL](/qb64wiki/index.php/ROL "ROL"), [\_ROR](/qb64wiki/index.php/ROR "ROR")
* [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")
* [LONG](/qb64wiki/index.php/LONG "LONG"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SHL&oldid=7411>"




## Navigation menu








### Search





















