


\_DESKTOPHEIGHT - QB64 Phoenix Edition Wiki








# \_DESKTOPHEIGHT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_DESKTOPHEIGHT function returns the height of the users current desktop.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*y&* = \_DESKTOPHEIGHT
  




## Description


* No parameters are needed for this function.
* This returns the height of the user's desktop, not the size of any screen or window which might be open on that desktop.


  




## Availability


* **QB64 v1.0 and up**
* **QB64-PE all versions**


  




## Examples




| ``` s& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 256) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") s& [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH"), _DESKTOPHEIGHT [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)"), [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")  ``` |
| --- |


*Explanation:* This will print the size of the user desktop (for example *1920, 1080* for a standard hdmi monitor), and then the size of the current [screen](/qb64wiki/index.php/SCREEN "SCREEN") (800, 600).
  




## See also


* [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT"), [\_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH")
* [\_WIDTH](/qb64wiki/index.php/WIDTH "WIDTH"), [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DESKTOPHEIGHT&oldid=8305>"




## Navigation menu








### Search





















