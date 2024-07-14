


\_MEMELEMENT - QB64 Phoenix Edition Wiki








# \_MEMELEMENT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEMELEMENT function returns a [\_MEM](/qb64wiki/index.php/MEM "MEM") block referring to a variable's memory, but not past it.


  






| Contents * [1 Syntax](#Syntax) * [2 .TYPE values (version 1.000 and up)](#.TYPE_values_(version_1.000_and_up)) 	+ [2.1 Versions prior to 1.000](#Versions_prior_to_1.000) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*memoryBlock* = \_MEMELEMENT(*referenceVariable*)
  




* The *referenceVariable* parameter designates the existing variable name using the memory block.
* \_MEMELEMENT is the same as [\_MEM](/qb64wiki/index.php/MEM "MEM") but in an array it returns the specifications of an element, not the entire array.
* All values created by memory functions MUST be freed using [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") with a valid [\_MEM](/qb64wiki/index.php/MEM "MEM") variable type.
* The \_MEMELEMENT type contains the following **read-only** elements where *name* is the variable name:


*name***.OFFSET** is the beginning offset of the memory block AS [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")
*name***.SIZE** returns the largest available region of memory of the ELEMENT in bytes AS [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")
*name***.ELEMENTSIZE** is the [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") size of the elements within the block AS [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")
* 2 = [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values have an element size of 2 bytes
* 4 = [LONG](/qb64wiki/index.php/LONG "LONG") integer and [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") float values have an element size of 4 bytes
* 8 = [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") float and [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") values have an element size of 8 bytes
* 32 = [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") values have an element size of 32 bytes
* [LEN](/qb64wiki/index.php/LEN "LEN") = [STRING](/qb64wiki/index.php/STRING "STRING") or [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") byte sizes vary so use [LEN](/qb64wiki/index.php/LEN "LEN")(variable) for the number of bytes.

*name***.TYPE** is the type (represented as bits combined to form a value) AS [LONG](/qb64wiki/index.php/LONG "LONG") (see below).
  




## .TYPE values (version 1.000 and up)


* 0 = UDT ([user defined type](/qb64wiki/index.php/TYPE "TYPE")) or memory created by [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")
* 1 = 1 bit ELEMENT.SIZE=1 \*Only used along with specific types (currently integers or floats)
* 2 = 2 bit. ELEMENT.SIZE=2 \*
* 4 = 4 bit. ELEMENT.SIZE=4 \*
* 8 = 8 bit. ELEMENT.SIZE=8 \*
* 16 = 16 bit. ELEMENT.SIZE=16 \*
* 32 = 32 bit. ELEMENT.SIZE=32 \*
* 64 = 64 bit. ELEMENT.SIZE=64 \*
* 128 = 128 bit. ELEMENT.SIZE=128 \*
* 256 = 256 bit. ELEMENT.SIZE=256 \*
* 512(+ bit\*) = integer types only(ie. whole numbers)
* 1024(+ bit\*) = floating point types only(ie. numbers that can have a decimal point)
* 2048 = [STRING](/qb64wiki/index.php/STRING "STRING") type only
* 4096(+ 512 + bit\*) = [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") integer type only
* 8192 = [\_MEM](/qb64wiki/index.php/MEM "MEM") type only
* 16384(+ 512 + bit\*)= [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") type only

*Note: If a future integer, float or other type doesn't have a size that is 1,2,4,8,16,32,64,128 or 256 it won't have a size-bit set.*



### Versions prior to 1.000


* 1 = Integer types such as [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") or [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")
* 2 = [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") variable types. Value must be added to the variable type value.(2 cannot be used by itself)
* 3 = ALL [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") type values.(add 1 + 2)
* 4 = Floating point types such as [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") or [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT")
* 8 = [STRING](/qb64wiki/index.php/STRING "STRING")
* 0 = unknown(eg. created with [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")) or [user-defined-types](/qb64wiki/index.php/TYPE "TYPE")

**Note: [\_MEM](/qb64wiki/index.php/MEM "MEM") and [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") values cannot be cast to other variable types.**
  




## Examples


*Example:* Comparing the specifications returned by [\_MEM](/qb64wiki/index.php/MEM "MEM") and \_MEMELEMENT from an array.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") a(1 [TO](/qb64wiki/index.php/TO "TO") 100) [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")  [DIM](/qb64wiki/index.php/DIM "DIM") m1 [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM") [DIM](/qb64wiki/index.php/DIM "DIM") m2 [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM")  m1 = [_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)")(a(50)) 'function returns information about array up to specific element [PRINT](/qb64wiki/index.php/PRINT "PRINT") m1.OFFSET, m1.SIZE, m1.TYPE, m1.ELEMENTSIZE  m2 = _MEMELEMENT(a(50)) 'function returns information about the specific element [PRINT](/qb64wiki/index.php/PRINT "PRINT") m2.OFFSET, m2.SIZE, m2.TYPE, m2.ELEMENTSIZE  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Output using VERSION .954 ONLY .TYPE values: 1 (integer) + 2 (unsigned)


| ``` 28377205        51        3        1 28377205        1         3        1  ``` |
| --- |


*Explanation:* [\_MEM](/qb64wiki/index.php/MEM "MEM") returns the info about the array to that element while \_MEMELEMENT returns info about that element only.
* [\_MEM](/qb64wiki/index.php/MEM "MEM") value returns the available array .SIZE as 51 bytes from the designated array element.
* \_MEMELEMENT value returns the available element .SIZE as one byte.

  




## See also


* [\_MEM](/qb64wiki/index.php/MEM "MEM")
* [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")
* [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT")
* [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMELEMENT&oldid=7511>"




## Navigation menu








### Search





















