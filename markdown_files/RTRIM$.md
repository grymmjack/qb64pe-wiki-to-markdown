


RTRIM$ - QB64 Phoenix Edition Wiki








# RTRIM$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The RTRIM$ function removes trailing space characters from a [STRING](/qb64wiki/index.php/STRING "STRING") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*return$* = RTRIM$(*value$*)
  




## Description


* *value$* is the [STRING](/qb64wiki/index.php/STRING "STRING") value to trim.
* If *value$* contains no trailing space characters, *value$* is returned unchanged.
* Convert fixed length [STRING](/qb64wiki/index.php/STRING "STRING") values by using a different *return$* variable.


  




## Examples


Trimming a fixed length string value for use by another string variable:





| ``` name$ = RTRIM$(contact.name) ' trims spaces from end of fixed length [TYPE](/qb64wiki/index.php/TYPE "TYPE") value.  ``` |
| --- |


Trimming text string ends:





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") RTRIM$("some text") + "." [PRINT](/qb64wiki/index.php/PRINT "PRINT") RTRIM$("some text   ") + "." [PRINT](/qb64wiki/index.php/PRINT "PRINT") RTRIM$("Tommy    ")  ``` |
| --- |




| ``` some text. some text. Tommy  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1246)
* [\_TRIM$](/qb64wiki/index.php/TRIM$ "TRIM$"), [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$"), [STR$](/qb64wiki/index.php/STR$ "STR$")
* [LSET](/qb64wiki/index.php/LSET "LSET"), [RSET](/qb64wiki/index.php/RSET "RSET")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RTRIM$&oldid=8911>"




## Navigation menu








### Search





















