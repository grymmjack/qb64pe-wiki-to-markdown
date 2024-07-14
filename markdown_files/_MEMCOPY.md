


\_MEMCOPY - QB64 Phoenix Edition Wiki








# \_MEMCOPY



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEMCOPY statement copies a block of bytes from one memory offset to another offset in memory.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_MEMCOPY *sourceBlock*, *sourceBlock.OFFSET*, *sourceBlock.SIZE* [TO](/qb64wiki/index.php/TO "TO") *destBlock*, *destBlock.OFFSET*
  




## Parameters


* *sourceBlock* is the source memory block name created AS [\_MEM](/qb64wiki/index.php/MEM "MEM").
* *sourceBlock.OFFSET* is the dot [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") within the source memory block to read from.
* *sourceBlock.SIZE* is the total number of bytes to transfer based on actual size.
* *destBlock* is the destination [\_MEM](/qb64wiki/index.php/MEM "MEM") memory block name to transfer data to.
* *destBlock.OFFSET* is the dot [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") within the dest [\_MEM](/qb64wiki/index.php/MEM "MEM") memory block to write to.


  




## Description


* The dot OFFSET is the memory block's start location in memory. Add bytes to place data further into the block.
* The dot SIZE is the total byte size of the memory block to transfer. You can transfer all or a portion of the data bytes.
* The memory block regions may overlap.
* **Always free memory blocks after values have been transferred to variables and are no longer required.**


  




## Examples


*Example:* Swapping data from one [STRING](/qb64wiki/index.php/STRING "STRING") variable to another. Fixed length strings are recommended for speed.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") m [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM") [DIM](/qb64wiki/index.php/DIM "DIM") n [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM")  m = [_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")(10) n = [_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")(100)  [_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT") m, m.OFFSET, "1234567890"  s$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(10) 'to load into a variable length string set its length first [_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET") m, m.OFFSET, s$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") "in:[" + s$ + "]"  _MEMCOPY m, m.OFFSET, m.SIZE [TO](/qb64wiki/index.php/TO "TO") n, n.OFFSET 'put m into n  b$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(10) [_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET") n, n.OFFSET, b$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") "out:[" + b$ + "]" [_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") m: [_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") n 'always clear the memory when done  ``` |
| --- |


  

*Snippet:* Instead of copying each array element, one at a time in nested [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") loops, \_MEMCOPY does it in one statement instantly.





| ``` 'copy array a to array b one index at a time: [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i1 = 0 [TO](/qb64wiki/index.php/TO "TO") 100     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i2 = 0 [TO](/qb64wiki/index.php/TO "TO") 100         b(i1, i2) = a(i1, i2)     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  'copy array a to array b in memory instantly: [DIM](/qb64wiki/index.php/DIM "DIM") ma [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM"): ma = [_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)")(a()) 'place array data into blocks [DIM](/qb64wiki/index.php/DIM "DIM") mb [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM"): mb = [_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)")(b()) _MEMCOPY ma, ma.OFFSET, ma.SIZE [TO](/qb64wiki/index.php/TO "TO") mb, mb.OFFSET [_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") ma: [_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") mb 'clear the memory when done  ``` |
| --- |


  




## See also


* [\_MEM](/qb64wiki/index.php/MEM "MEM"), [\_MEM (function)](/qb64wiki/index.php/MEM_(function) "MEM (function)")
* [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW"), [\_MEMGET (function)](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")
* [\_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE"), [\_MEMELEMENT](/qb64wiki/index.php/MEMELEMENT "MEMELEMENT")
* [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT")
* [\_MEMFILL](/qb64wiki/index.php/MEMFILL "MEMFILL"), [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMCOPY&oldid=6461>"




## Navigation menu








### Search





















