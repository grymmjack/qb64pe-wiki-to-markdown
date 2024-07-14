


INTERRUPTX - QB64 Phoenix Edition Wiki








# INTERRUPTX



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The INTERRUPTX statement is an assembly routine for accessing computer information registers.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Legacy support](#Legacy_support) * [2 Parameters](#Parameters) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 See also](#See_also) |
| --- |


## Syntax


[CALL](/qb64wiki/index.php/CALL "CALL") INTERRUPTX(*intNum*, *inRegs*, *outRegs*)
### Legacy support


* Registers are emulated in **QB64** to allow older programs to be compiled. To enable mouse input in your programs, the recommended practice is to use [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") and related functions.


  




## Parameters


* Registers are emulated in QB64 and there is no support for *intNum* 33h mouse functions above 3 or *intNum* requests other than 33.
* *inRegs* are the values placed into the call and *outRegs* are the register return values.


### QBasic/QuickBASIC


* Available in QuickBASIC versions 4 and up and required an external library to be loaded. **QB64** emulates the statement without an external library.
* *intNum* is the interrupt reference vector table address. For historic reference, see: [Ralf Brown's Interrupt List](http://www.ctyme.com/intr/cat.htm)
* The [TYPE](/qb64wiki/index.php/TYPE "TYPE") definition below will work for both [INTERRUPT](/qb64wiki/index.php/INTERRUPT "INTERRUPT") and INTERRUPTX statement calls
* INTERRUPT can use all of the below TYPE elements when they are required.




| ``` [TYPE](/qb64wiki/index.php/TYPE "TYPE") RegTypeX    ax AS INTEGER    bx AS INTEGER    cx AS INTEGER    dx AS INTEGER    bp AS INTEGER    si AS INTEGER    di AS INTEGER    flags AS INTEGER    ds AS INTEGER    es AS INTEGER [END TYPE](/qb64wiki/index.php/END_TYPE "END TYPE")  ``` |
| --- |




| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") inregs [AS](/qb64wiki/index.php/AS "AS") RegTypeX, outregs [AS](/qb64wiki/index.php/AS "AS") RegTypeX  ``` |
| --- |


QBasic's *RegType.BI* $INCLUDE file can be used by INTERRUPT or INTERRUPTX
  




## See also


* [$INCLUDE:](/qb64wiki/index.php/$INCLUDE "$INCLUDE")
* [QB.BI](/qb64wiki/index.php/QB.BI "QB.BI"), [CALL ABSOLUTE](/qb64wiki/index.php/CALL_ABSOLUTE "CALL ABSOLUTE")
* [INTERRUPT](/qb64wiki/index.php/INTERRUPT "INTERRUPT")
* Ethan Winer's free QBasic Book and Programs: [WINER.ZIP](http://www.ethanwiner.com/fullmoon.html)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INTERRUPTX&oldid=7501>"




## Navigation menu








### Search





















