


\_TRIM$ - QB64 Phoenix Edition Wiki








# \_TRIM$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_TRIM$ function removes both leading and trailing space characters from a [STRING](/qb64wiki/index.php/STRING "STRING") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*return$* = \_TRIM$(*text$*)
  




## Description


* Shorthand to using [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$")("text"))
* *text$* is the [STRING](/qb64wiki/index.php/STRING "STRING") value to trim.
* If *text$* contains no leading or trailing space characters, it is returned unchanged.
* Convert fixed length [STRING](/qb64wiki/index.php/STRING "STRING") values by using a different *return$* variable.


  




## Examples


*Example: Demonstrating how \_TRIM$(text$) can replace LTRIM$(RTRIM$(text$)):*





| ``` text$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(10) + "some text" + [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(10) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[" + text$ + "]" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[" + [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$")(text$) + "]" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[" + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")(text$) + "]" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[" + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$")(text$)) + "]" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[" + _TRIM$(text$) + "]"  ``` |
| --- |




| ``` [          some text          ] [          some text] [some text          ] [some text] [some text]  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1246)
* [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$"), [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=TRIM$&oldid=8912>"




## Navigation menu








### Search





















