


$SCREENHIDE - QB64 Phoenix Edition Wiki








# $SCREENHIDE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $SCREENHIDE [metacommand](/qb64wiki/index.php/Metacommand "Metacommand") can be used to hide the main program window throughout a program.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


$SCREENHIDE
  




## Description


* $SCREENHIDE may be used at the start of a program to hide the main program window when using a [console](/qb64wiki/index.php/$CONSOLE "$CONSOLE") window.
* The [\_SCREENHIDE](/qb64wiki/index.php/SCREENHIDE "SCREENHIDE") statement must be used before [\_SCREENSHOW](/qb64wiki/index.php/SCREENSHOW "SCREENSHOW") can be used in sections of a program.
* **QB64 [metacommands](/qb64wiki/index.php/Metacommand "Metacommand") cannot be commented out with [apostrophe](/qb64wiki/index.php/Apostrophe "Apostrophe") or [REM](/qb64wiki/index.php/REM "REM")**.


  




## Examples


*Example:* Hiding a program when displaying a message box in Windows.





| ``` $SCREENHIDE [DECLARE DYNAMIC LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") "user32"   [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") MessageBoxA& ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") hWnd%&, [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") lpText%&, [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") lpCaption%&, [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") uType~&) [END DECLARE](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") [DECLARE DYNAMIC LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") "kernel32"   [SUB](/qb64wiki/index.php/SUB "SUB") ExitProcess ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") uExitCode~&) [END DECLARE](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") [DIM](/qb64wiki/index.php/DIM "DIM") s0 [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") [DIM](/qb64wiki/index.php/DIM "DIM") s1 [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") s0 = "Text" + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) s1 = "Caption" + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) ExitProcess MessageBoxA(0, [_OFFSET](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)")(s0), [_OFFSET](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)")(s1), 0)  ``` |
| --- |


Code by Michael Calkins
  




## See also


* [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"), [$SCREENSHOW](/qb64wiki/index.php/$SCREENSHOW "$SCREENSHOW")
* [\_SCREENHIDE](/qb64wiki/index.php/SCREENHIDE "SCREENHIDE"), [\_SCREENSHOW](/qb64wiki/index.php/SCREENSHOW "SCREENSHOW")
* [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$SCREENHIDE&oldid=8791>"




## Navigation menu








### Search





















