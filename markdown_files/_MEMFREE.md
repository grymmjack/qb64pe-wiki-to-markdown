


\_MEMFREE - QB64 Phoenix Edition Wiki








# \_MEMFREE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEMFREE statement frees the designated memory block [\_MEM](/qb64wiki/index.php/MEM "MEM") value and must be used with all memory functions.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


\_MEMFREE *memoryVariable*
  




## Parameters


* ALL designated [\_MEM](/qb64wiki/index.php/MEM "MEM") type *memoryVariable* values must be freed to conserve memory when they are no longer used or needed.


  




## Description


* Since [\_MEM](/qb64wiki/index.php/MEM "MEM") type variables cannot use a suffix, use [DIM](/qb64wiki/index.php/DIM "DIM") *memoryVariable* [AS](/qb64wiki/index.php/AS "AS") [\_MEM](/qb64wiki/index.php/MEM "MEM") to create memory handle variables.
* All values created by memory functions must be freed using \_MEMFREE with a valid [\_MEM](/qb64wiki/index.php/MEM "MEM") variable.


  




## See also


* [\_MEM](/qb64wiki/index.php/MEM "MEM")
* [\_MEM (function)](/qb64wiki/index.php/MEM_(function) "MEM (function)")
* [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")
* [\_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE")
* [\_MEMELEMENT](/qb64wiki/index.php/MEMELEMENT "MEMELEMENT")
* [\_MEMGET (function)](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMFREE&oldid=7619>"




## Navigation menu








### Search





















