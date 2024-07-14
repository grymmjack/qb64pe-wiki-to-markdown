


\_CONSOLETITLE - QB64 Phoenix Edition Wiki








# \_CONSOLETITLE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CONSOLETITLE statement creates the title of the console window using a literal or variable [string](/qb64wiki/index.php/STRING "STRING").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_CONSOLETITLE *text$*
  




## Description


* The *text$* used can be a literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") value.


  




## Examples


*Example:* Hiding the main program window while displaying the console window with a title.





| ``` [$SCREENHIDE](/qb64wiki/index.php/$SCREENHIDE "$SCREENHIDE") [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 4 [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") _CONSOLETITLE "Error Log"  [_DEST](/qb64wiki/index.php/DEST "DEST") [_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Errors go here! (fyi, this line is not an error)" [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Note:* You can also use [SHELL](/qb64wiki/index.php/SHELL "SHELL") "title consoletitle" to set the title of the console window. However, **the recommended practice is to use \_CONSOLETITLE**.
  




## See also


* [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"), [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")
* [$SCREENHIDE](/qb64wiki/index.php/$SCREENHIDE "$SCREENHIDE"), [$SCREENSHOW](/qb64wiki/index.php/$SCREENSHOW "$SCREENSHOW")
* [\_SCREENHIDE](/qb64wiki/index.php/SCREENHIDE "SCREENHIDE"), [\_SCREENSHOW](/qb64wiki/index.php/SCREENSHOW "SCREENSHOW")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CONSOLETITLE&oldid=8292>"




## Navigation menu








### Search





















