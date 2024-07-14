


\_SCREENEXISTS - QB64 Phoenix Edition Wiki








# \_SCREENEXISTS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SCREENEXISTS function returns true (-1) once a screen has been created.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*screenReady%%* = \_SCREENEXISTS
  




## Description


* Function returns true (-1) once a program screen is available to use or change.
* Can be used to avoid program errors because a screen was not ready for input or alterations.
	+ Use before [\_TITLE](/qb64wiki/index.php/TITLE "TITLE"), [\_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE") and other functions that require the output window to have been created.


  




## Examples


Example
Waiting in a loop until the screen exists to add the title. The [\_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") prevents the loop from using all CPU time while waiting.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 10: [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") _SCREENEXISTS [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "My Title"  ``` |
| --- |


  




## See also


* [\_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")
* [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE")
* [$RESIZE](/qb64wiki/index.php/$RESIZE "$RESIZE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SCREENEXISTS&oldid=4818>"




## Navigation menu








### Search





















