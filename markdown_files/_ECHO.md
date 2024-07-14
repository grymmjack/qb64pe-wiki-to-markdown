


\_ECHO - QB64 Phoenix Edition Wiki








# \_ECHO



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ECHO statement allows outputting text to a [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") window without having to alternate between [\_DEST](/qb64wiki/index.php/DEST "DEST") pages.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_ECHO {*"text to output"* | *textVariable$*}
  




## Description


* \_ECHO is a shorthand to saving current [\_DEST](/qb64wiki/index.php/DEST "DEST"), switching to [\_DEST](/qb64wiki/index.php/DEST "DEST") [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE"), [PRINTing](/qb64wiki/index.php/PRINT "PRINT"), then switching back to the previous [\_DEST](/qb64wiki/index.php/DEST "DEST").
* To output numbers, use the [STR$](/qb64wiki/index.php/STR$ "STR$") function.


  




## Availability


* **QB64 v1.3 and up**
* **QB64-PE all versions**


  




## Examples




| ``` [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "this will show in the main window" _ECHO "this will show in the console"  ``` |
| --- |


  




## See also


* [\_DEST](/qb64wiki/index.php/DEST "DEST")
* [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"), [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")
* [STR$](/qb64wiki/index.php/STR$ "STR$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ECHO&oldid=8318>"




## Navigation menu








### Search





















