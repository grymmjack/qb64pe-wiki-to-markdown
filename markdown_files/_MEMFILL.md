


\_MEMFILL - QB64 Phoenix Edition Wiki








# \_MEMFILL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEMFILL statement converts a value to a specified type, then fills memory with that type including any non-whole remainder.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_MEMFILL *memoryBlock*, *memoryBlock.OFFSET*, *fillBytes*, *value* [AS *variableType*]
  




## Parameters


* The *memoryBlock* [\_MEM](/qb64wiki/index.php/MEM "MEM") memory block is the block referenced to be filled.
* *memoryBlock.OFFSET* is the starting offset of the above referenced memory block.
* The *fillBytes* is the number of bytes to fill the memory block.
* The *value* is the value to place in the memory block at the designated OFFSET position.
* A literal or variable *value* can be optionally set [AS](/qb64wiki/index.php/AS "AS") a variable [type](/qb64wiki/index.php/Variable_Types "Variable Types") appropriate for the memory block.


  




## Description


* To clear previous data from a [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW") memory block, use \_MEMFILL with a *value* of 0.


  




## Examples


*Example:* Filling array values quickly using FOR loops or a simple memory fill.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") a(100, 100) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") [DIM](/qb64wiki/index.php/DIM "DIM") b(100, 100) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")  'filling array a with value 13 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i1 = 0 [TO](/qb64wiki/index.php/TO "TO") 100     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i2 = 0 [TO](/qb64wiki/index.php/TO "TO") 100         a(i1, i2) = 13     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  'filling array b with value 13 [DIM](/qb64wiki/index.php/DIM "DIM") mema [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM") mema = [_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)")(b()) _MEMFILL mema, mema.OFFSET, mema.SIZE, 13 [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") [_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") mema  ``` |
| --- |


  




## See also


* [\_MEM](/qb64wiki/index.php/MEM "MEM"), [\_MEM (function)](/qb64wiki/index.php/MEM_(function) "MEM (function)")
* [\_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE"), [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")
* [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMFILL&oldid=8711>"




## Navigation menu








### Search





















