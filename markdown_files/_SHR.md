


\_SHR - QB64 Phoenix Edition Wiki








# \_SHR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SHR function is used to shift the bits of a numerical value to the right.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*result* = \_SHR(*numericalVariable*, *numericalValue*)
  




## Parameters


* *numericalVariable* is the variable to shift the bits of and can be of the following types: [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64"), or [\_BYTE](/qb64wiki/index.php/BYTE "BYTE").
* Integer values can be signed or [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED").
* *numericalValue* the number of places to shift the bits.
* While 0 is a valid value it will have no affect on the variable being shifted.


  




## Description


* Allows for division of a value by 2 faster than normal division (see example 2 below).
* Bits that reach the end of a variables bit count are dropped.
* The type of variable used to store the results should match the type of the variable being shifted.
* NOTE: When dealing with SIGNED variables, shifting the bits right will leave the sign bit set. This is due to how C++ deals with bit shifting under the hood.


  




## Availability


* **Version 1.3 and up**.


  




## Examples


*Example 1:*





| ``` A~%% = 128 'set left most bit of an[_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") A~%% [PRINT](/qb64wiki/index.php/PRINT "PRINT") _SHR(A~%%,7) [PRINT](/qb64wiki/index.php/PRINT "PRINT") _SHR(A~%%,8) 'shift the bit off the right 'edge'  ``` |
| --- |




| ```  128  1  0  ``` |
| --- |


  

*Example 2:*





| ``` A~%% = 128 [FOR](/qb64wiki/index.php/FOR "FOR") I%% = 0 [TO](/qb64wiki/index.php/TO "TO") 8     [PRINT](/qb64wiki/index.php/PRINT "PRINT") _SHR(A~%%, I%%) [NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") I%%  ``` |
| --- |




| ```  128   64   32   16   8   4   2   1   0  ``` |
| --- |


  




## See also


* [\_SHL](/qb64wiki/index.php/SHL "SHL"), [\_ROL](/qb64wiki/index.php/ROL "ROL"), [\_ROR](/qb64wiki/index.php/ROR "ROR")
* [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")
* [LONG](/qb64wiki/index.php/LONG "LONG"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SHR&oldid=7412>"




## Navigation menu








### Search





















