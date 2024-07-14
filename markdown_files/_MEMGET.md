


\_MEMGET - QB64 Phoenix Edition Wiki








# \_MEMGET



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEMGET statement reads a portion of a memory block at an OFFSET position into a variable, array or user defined type.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


\_MEMGET *memoryBlock*, *bytePosition*, *destinationVariable*
  




* *memoryBlock* is a [\_MEM](/qb64wiki/index.php/MEM "MEM") variable type memory block name created by [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW") or the [\_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)") function.
* *bytePosition* is the *memoryBlock*.[OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") memory start position plus any bytes to move into the block.
* *destinationVariable* is the variable assigned to hold the data. The number of bytes read is determined by the variable [type](/qb64wiki/index.php/Variable_Types "Variable Types") used.


  




## Description


* The \_MEMGET statement is similar to the [GET](/qb64wiki/index.php/GET "GET") statement used in files, but the position is required.
* The memory block name.[OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") returns the starting byte position of the block. Add bytes to move into the block.
* The variable type held in the memory block can determine the next *bytePosition* to read.
* [LEN](/qb64wiki/index.php/LEN "LEN") can be used to determine the byte size of numerical or user defined [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types") regardless of the value held.
* [STRING](/qb64wiki/index.php/STRING "STRING") values should be of a defined length. Variable length strings can actually move around in memory and not be found.


  

{{PageExamples
*Example:* Shows how to read the PSET color values from a program's [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") memory to an array.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 [PSET](/qb64wiki/index.php/PSET "PSET") (0, 0), 123 [PSET](/qb64wiki/index.php/PSET "PSET") (1, 0), 222 'create screen image  'here is an array [DIM](/qb64wiki/index.php/DIM "DIM") screen_array(319, 199) [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") 'use screen dimensions from 0  'here's how we can copy the screen to our array [DIM](/qb64wiki/index.php/DIM "DIM") m [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM") m = [_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE")  '0 or no handle necessary when accessing the current program screen _MEMGET m, m.OFFSET, screen_array()  'here's the proof [PRINT](/qb64wiki/index.php/PRINT "PRINT") screen_array(0, 0) 'print 123 [PRINT](/qb64wiki/index.php/PRINT "PRINT") screen_array(1, 0) 'print 222 [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [\_MEMGET (function)](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")
* [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT")
* [\_MEM](/qb64wiki/index.php/MEM "MEM")
* [\_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE")
* [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMGET&oldid=8712>"




## Navigation menu








### Search





















