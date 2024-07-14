


VARPTR - QB64 Phoenix Edition Wiki








# VARPTR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **VARPTR** function returns an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value that is the offset part of the variable or array memory address within it's segment.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


offset% = VARPTR(variable\_name[(reference\_index%)])
  




* If variablename is not defined before VARPTR or [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG") is called, the variable is created and it's address is returned.
* Reference index is used to set the offset address of an array index, not necessarily the lowest index.
* When a string variable, VARPTR returns the offset address location of the first byte of the string.
* Because many QBasic statements change the locations of variables in memory, use the values returned by VARPTR and VARSEG immediately after the functions are used!
* Integer array sizes are limited to 32767 elements when using VARPTR in QB and **QB64**!. Create a larger array using [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"). Example: [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") Memory (65535) AS [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [\_BYTE](/qb64wiki/index.php/BYTE "BYTE")
* **Warning: DEF SEG, VARSEG , VARPTR, PEEK or POKE access QB64's emulated 16 bit conventional memory block!**


**It is highly recommended that QB64's [\_MEM](/qb64wiki/index.php/MEM "MEM") memory system be used to avoid running out of memory.**
  




## See also


* [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE"), [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD")
* [SADD](/qb64wiki/index.php/SADD "SADD"), [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")
* [VARPTR$](/qb64wiki/index.php/VARPTR$ "VARPTR$"), [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG")
* [POKE](/qb64wiki/index.php/POKE "POKE"), [PEEK](/qb64wiki/index.php/PEEK "PEEK")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=VARPTR&oldid=7705>"




## Navigation menu








### Search





















