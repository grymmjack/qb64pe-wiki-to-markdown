


\_MEMPUT - QB64 Phoenix Edition Wiki








# \_MEMPUT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEMPUT statement writes data to a portion of a designated memory block at an [OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") position.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Description](#Description_2) * [5 See also](#See_also) |
| --- |


## Syntax


\_MEMPUT *memoryBlock*, *bytePosition*, *sourceVariable* [AS *type*]
  




## Parameters


* *memoryBlock* is a [\_MEM](/qb64wiki/index.php/MEM "MEM") variable type memory block name created by [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW") or the [\_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)") function.
* *bytePosition* is the *memoryBlock*.[OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") start position plus any bytes needed to read specific values.
* The *sourceVariable* type designates the size and *bytePosition* it should be written to. It can be a variable, [array](/qb64wiki/index.php/Arrays "Arrays") or user defined type.
* *bytePosition* can be converted [AS](/qb64wiki/index.php/AS "AS") a specific variable *[type](/qb64wiki/index.php/TYPE "TYPE")* before being written to the *memoryBlock* as bytes.


  




## Description


* The \_MEMPUT statement is similar to the [PUT](/qb64wiki/index.php/PUT "PUT") file statement, but *bytePosition* is required.
* The *memoryBlock*.[OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") returns the starting byte position of the block. Add bytes to move into the block.
* The variable type held in the memory block can determine the next *byte position* to write a value.
* [LEN](/qb64wiki/index.php/LEN "LEN") can be used to determine the byte size of numerical or user defined [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types") regardless of the value held.
* [STRING](/qb64wiki/index.php/STRING "STRING") values should be of a defined length. Variable length strings can actually move around in memory and not be found.


  




## Description


*Example:* \_MEMPUT can be used just like [POKE](/qb64wiki/index.php/POKE "POKE") without [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG").





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") o [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM") o = [_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)")(d&) _MEMPUT o, o.OFFSET + 1, 3 [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")  'POKE v = [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(o, o.OFFSET + 1, [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")) 'PEEK [PRINT](/qb64wiki/index.php/PRINT "PRINT") v 'prints 3 [PRINT](/qb64wiki/index.php/PRINT "PRINT") d& 'print 768 because the 2nd byte of d& has been set to 3 or 3 * 256  ``` |
| --- |


  




## See also


* [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMGET (function)](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")
* [\_MEM](/qb64wiki/index.php/MEM "MEM"), [\_MEM (function)](/qb64wiki/index.php/MEM_(function) "MEM (function)")
* [\_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE"), [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")
* [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE"), [\_MEMCOPY](/qb64wiki/index.php/MEMCOPY "MEMCOPY")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMPUT&oldid=8716>"




## Navigation menu








### Search





















