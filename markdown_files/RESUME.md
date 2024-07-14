


RESUME - QB64 Phoenix Edition Wiki








# RESUME



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **RESUME** statement is used with **NEXT** or a line number or label in an error handling routine.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


RESUME {**NEXT**|*lineLabel*|*lineNumber*}
  




## Description


* **NEXT** returns execution to the code immediately following the error.
* A *lineLabel* or *lineNumber* is the code line to return to after an error.
* If the line label or number is omitted or the line number = 0, the code execution resumes at the code that created the original error.
* RESUMEcan only be used in ERROR handling routines. Use [RETURN](/qb64wiki/index.php/RETURN "RETURN") in normal [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") procedures.


  




## See also


* [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR"), [ERROR](/qb64wiki/index.php/ERROR "ERROR")
* [RETURN](/qb64wiki/index.php/RETURN "RETURN"), [ERROR Codes](/qb64wiki/index.php/ERROR_Codes "ERROR Codes")
* [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RESUME&oldid=7659>"




## Navigation menu








### Search





















