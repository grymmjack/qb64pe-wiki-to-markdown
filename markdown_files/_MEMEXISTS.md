


\_MEMEXISTS - QB64 Phoenix Edition Wiki








# \_MEMEXISTS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEMEXISTS function returns true (-1) if the memory block variable name specified exists in memory and false (0) if it does not.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*result* = \_MEMEXISTS(*memBlock*)
  




## Description


* The *memBlock* variable name must have been created using [DIM](/qb64wiki/index.php/DIM "DIM") memBlock [AS](/qb64wiki/index.php/AS "AS") [\_MEM](/qb64wiki/index.php/MEM "MEM") type ([DIM](/qb64wiki/index.php/DIM "DIM").
* The function verifies that the memory variable exists in memory before using a passed block, to avoid generating QB64 errors.
* Typically, this function is used by a [LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") which accepts a [\_MEM](/qb64wiki/index.php/MEM "MEM") structure as input, to avoid an error.


  




## See also


* [\_MEM (function)](/qb64wiki/index.php/MEM_(function) "MEM (function)")
* [\_MEMELEMENT](/qb64wiki/index.php/MEMELEMENT "MEMELEMENT"), [\_MEMCOPY](/qb64wiki/index.php/MEMCOPY "MEMCOPY")
* [\_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE"), [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")
* [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT")
* [\_MEMFILL](/qb64wiki/index.php/MEMFILL "MEMFILL"), [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMEXISTS&oldid=7340>"




## Navigation menu








### Search





















