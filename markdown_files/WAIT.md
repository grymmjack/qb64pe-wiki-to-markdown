


WAIT - QB64 Phoenix Edition Wiki








# WAIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The WAIT statement waits until the value read from an I/O port has certain bits set.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


WAIT *port%*, *andMask%*[, *xorMask%*]
  




## Description


* The WAIT statement reads a value from *port%* using [INP](/qb64wiki/index.php/INP "INP").
* If *xorMask%* is specified, the value is [XOR](/qb64wiki/index.php/XOR "XOR")'d with *xorMask%*. It has the effect of "toggle these bits".
* The value is then [AND](/qb64wiki/index.php/AND "AND")'d with *andMask%*. It has the effect of "check if these bits are set".
* If the final value is non-zero, WAIT returns. Otherwise, another value is read from *port%* and checked again.
* The WAIT statement returns immediately if *port%* is not supported.


  




## Examples


Waiting for vertical retrace


| ``` ' Either statement can be used to try to reduce screen flickering. ' If both statements are used, try changing the order.  WAIT &H3DA, 8 ' finishes whenever the screen isn't being written to WAIT &H3DA, 8, 8 ' finishes whenever the screen is being written to  ``` |
| --- |


  




## See also


* [INP](/qb64wiki/index.php/INP "INP"), [OUT](/qb64wiki/index.php/OUT "OUT")
* [Scancodes](/qb64wiki/index.php/Scancodes "Scancodes")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=WAIT&oldid=6630>"




## Navigation menu








### Search





















