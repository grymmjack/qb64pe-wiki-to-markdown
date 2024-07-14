


DEF SEG - QB64 Phoenix Edition Wiki








# DEF SEG



From QB64 Phoenix Edition Wiki
(Redirected from [SEG](/qb64wiki/index.php?title=SEG&redirect=no "SEG"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
DEF SEG is used to define the area in memory to access QB64's emulated conventional memory.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Legacy support](#Legacy_support) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


DEF SEG [=][{segment|VARSEG(variable}]
### Legacy support


* **QB64 implements memory access using [\_MEM](/qb64wiki/index.php/MEM "MEM") and related functions. For that reason, DEF SEG isn't recommended practice anymore and is supported to maintain compatibility with legacy code.**


  




## Description


* Used to set the pointer to a memory area of a variable/array or register.
* [PEEK](/qb64wiki/index.php/PEEK "PEEK") and [POKE](/qb64wiki/index.php/POKE "POKE") require a segment memory address (often just 0) without using VARSEG.
* Important segments using [PEEK](/qb64wiki/index.php/PEEK "PEEK") and [POKE](/qb64wiki/index.php/POKE "POKE") include &HB800 (text segment) and &HA000 (graphics segment).
* [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE") and [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD") require a VARSEG reference to the grahic array(0 index) used.
* Always use DEF SEG when the procedure is completed, in order to reset the segment to QBasic's default value.
* DEF SEG, [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG"), [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR"), [PEEK](/qb64wiki/index.php/PEEK "PEEK") and [POKE](/qb64wiki/index.php/POKE "POKE") access QB64's emulated 16 bit conventional memory block. **It is highly recommended to use QB64's [\_MEM](/qb64wiki/index.php/MEM "MEM") memory system to avoid running out of memory.**


  




## See also


* [DEF SEG = 0](/qb64wiki/index.php/DEF_SEG_%3D_0 "DEF SEG = 0")
* [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR"), [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG")
* [PEEK](/qb64wiki/index.php/PEEK "PEEK"), [POKE](/qb64wiki/index.php/POKE "POKE")
* [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE"), [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DEF_SEG&oldid=7261>"




## Navigation menu








### Search





















