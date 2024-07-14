


SADD - QB64 Phoenix Edition Wiki








# SADD



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **SADD** function returns the address of a [STRING](/qb64wiki/index.php/STRING "STRING") variable as an offset from the current data segment.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


SADD(stringvariable)
  




* The argument may be a simple string variable or a single element of a string array. You may not use fixed-length strings.
* Use this function carefully because strings can move in the BASIC string space storage area at any time.
* Adding characters may produce a run-time error. Don't add characters to the ends of parameters.


  




## See also


* [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG"), [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR"), [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SADD&oldid=7396>"




## Navigation menu








### Search





















