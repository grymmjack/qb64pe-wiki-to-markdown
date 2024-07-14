


\_MEMNEW - QB64 Phoenix Edition Wiki








# \_MEMNEW



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEMNEW function allocates new memory and returns a [\_MEM](/qb64wiki/index.php/MEM "MEM") memory block referring to it.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*memoryBlock* = \_MEMNEW(*byteSize*)
  




## Parameters


* The *byteSize* parameter is the desired byte size of the memory block based on the variable [type](/qb64wiki/index.php/Variable_Types "Variable Types") it will hold.


  




## Description


* The *memoryBlock* value created holds the elements .OFFSET, .SIZE, .TYPE and .ELEMENTSIZE.
* \_MEMNEW does not clear the data previously in the memory block it allocates, for speed purposes.
* To clear previous data from a new memory block, use [\_MEMFILL](/qb64wiki/index.php/MEMFILL "MEMFILL") with a byte value of 0.
* When a new memory block is created the memory .TYPE value will be 0.
* **If the read only memory block .SIZE is 0, the memory block was not created.**
* **All values created by memory functions must be freed using [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") with a valid [\_MEM](/qb64wiki/index.php/MEM "MEM") variable.**


  




## Examples


*Example:* Shows how [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") numerical values can be passed, but non-fixed [STRING](/qb64wiki/index.php/STRING "STRING") lengths cannot get the value.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") m [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM") [DIM](/qb64wiki/index.php/DIM "DIM") f [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 5 m = _MEMNEW(5) 'create new memory block of 5 bytes a = 12345.6 [_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT") m, m.OFFSET, a 'put single value [_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET") m, m.OFFSET, b 'get single value [PRINT](/qb64wiki/index.php/PRINT "PRINT") "b = "; b c$ = "Doggy" [_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT") m, m.OFFSET, c$ 'put 5 byte string value [_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET") m, m.OFFSET, d$ 'get unfixed length string value [_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET") m, m.OFFSET, f  'get 5 byte string value e$ = [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(m, m.OFFSET, [STRING](/qb64wiki/index.php/STRING "STRING") * 5) 'get 5 byte string value [PRINT](/qb64wiki/index.php/PRINT "PRINT") "d$ = "; d$; [LEN](/qb64wiki/index.php/LEN "LEN")(d$) 'prints empty string [PRINT](/qb64wiki/index.php/PRINT "PRINT") "e$ = "; e$; [LEN](/qb64wiki/index.php/LEN "LEN")(e$) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "f = "; f; [LEN](/qb64wiki/index.php/LEN "LEN")(f)  ``` |
| --- |




| ``` b =  12345.6 d$ =  0 e$ = Doggy 5 f = Doggy 5  ``` |
| --- |


  




## See also


* [\_MEM](/qb64wiki/index.php/MEM "MEM"), [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT")
* [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMGET (function)](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")
* [\_MEMFILL](/qb64wiki/index.php/MEMFILL "MEMFILL"), [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMNEW&oldid=8715>"




## Navigation menu








### Search





















