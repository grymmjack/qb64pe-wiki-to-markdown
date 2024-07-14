


\_CONTINUE - QB64 Phoenix Edition Wiki








# \_CONTINUE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
  

The \_CONTINUE statement is used in a [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP"), [WHILE...WEND](/qb64wiki/index.php/WHILE...WEND "WHILE...WEND") or [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") block to skip the remaining lines of code in a block (without exiting it) and start the next iteration. It works as a shortcut to a [GOTO](/qb64wiki/index.php/GOTO "GOTO"), but without the need for a [line label](/qb64wiki/index.php/Line_numbers "Line numbers").


  






| Contents * [1 Syntax](#Syntax) * [2 Availability](#Availability) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_CONTINUE
  




## Availability


* **QB64 v1.2 and up**
* **QB64-PE all versions**


  




## Examples


*Example:*





| ``` [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") 10     [IF](/qb64wiki/index.php/IF "IF") i = 5 [THEN](/qb64wiki/index.php/THEN "THEN") _CONTINUE     [PRINT](/qb64wiki/index.php/PRINT "PRINT") i; [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |




| ```  1  2  3  4  6  7  8  9  10  ``` |
| --- |


  




## See also


* [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP")
* [WHILE...WEND](/qb64wiki/index.php/WHILE...WEND "WHILE...WEND")
* [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")
* [GOTO](/qb64wiki/index.php/GOTO "GOTO")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CONTINUE&oldid=8293>"




## Navigation menu








### Search





















