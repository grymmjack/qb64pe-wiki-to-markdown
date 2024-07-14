


\_SCREENCLICK - QB64 Phoenix Edition Wiki








# \_SCREENCLICK



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SCREENCLICK statement simulates clicking on a pixel coordinate on the desktop screen with the left mouse button.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


\_SCREENCLICK *column%*, *row%*[, *button%*]
  




## Description


* *column%* is the horizontal pixel coordinate position on the screen.
* *row%* is the vertical pixel coordinate position on the screen.
* Optional *button%* can be used to specify left button (1, default), right button (2) or middle button (3) (available with **build 20170924/68**).
* Coordinates can range from 0 to the [\_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH") and [\_DESKTOPHEIGHT](/qb64wiki/index.php/DESKTOPHEIGHT "DESKTOPHEIGHT"). The desktop image acquired by [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE") can be used to map the coordinates required.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## See also


* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE"), [\_SCREENPRINT](/qb64wiki/index.php/SCREENPRINT "SCREENPRINT")
* [\_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE"), [\_SCREENX](/qb64wiki/index.php/SCREENX "SCREENX"), [\_SCREENY](/qb64wiki/index.php/SCREENY "SCREENY")
* [\_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH"), [\_DESKTOPHEIGHT](/qb64wiki/index.php/DESKTOPHEIGHT "DESKTOPHEIGHT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SCREENCLICK&oldid=6519>"




## Navigation menu








### Search





















