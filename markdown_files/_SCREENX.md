


\_SCREENX - QB64 Phoenix Edition Wiki








# \_SCREENX



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SCREENX function returns the current column pixel coordinate of the program window on the desktop.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*positionX&* = \_SCREENX
  




## Description


* Function returns the current program window's upper left corner column position on the desktop.
* Use [\_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH") and [\_DESKTOPHEIGHT](/qb64wiki/index.php/DESKTOPHEIGHT "DESKTOPHEIGHT") to find the current Windows desktop resolution to adjust the position with [\_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE").
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Examples


*Example:* Clicks and opens program window header menu:





| ``` [_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE") [_MIDDLE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE") [_SCREENCLICK](/qb64wiki/index.php/SCREENCLICK "SCREENCLICK") _SCREENX + 10, [_SCREENY](/qb64wiki/index.php/SCREENY "SCREENY") + 10 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello window!"  ``` |
| --- |


  




## See also


* [\_SCREENY](/qb64wiki/index.php/SCREENY "SCREENY")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")
* [\_SCREENCLICK](/qb64wiki/index.php/SCREENCLICK "SCREENCLICK")
* [\_SCREENPRINT](/qb64wiki/index.php/SCREENPRINT "SCREENPRINT")
* [\_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SCREENX&oldid=6525>"




## Navigation menu








### Search





















