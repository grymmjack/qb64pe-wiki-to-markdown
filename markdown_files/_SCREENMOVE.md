


\_SCREENMOVE - QB64 Phoenix Edition Wiki








# \_SCREENMOVE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SCREENMOVE statement positions the program window on the desktop using designated coordinates.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


\_SCREENMOVE {*column&*, *row&*|\_MIDDLE}
  




## Parameters


* Positions the program window on the desktop using the *column&* and *row&* pixel coordinates for the upper left corner.
* **\_MIDDLE** can be used instead to automatically center the program window on the desktop, in any screen resolution.


  




## Description


* The program's [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") dimensions may influence the desktop position that can be used to keep the entire window on the screen.
* Use [\_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH") and [\_DESKTOPHEIGHT](/qb64wiki/index.php/DESKTOPHEIGHT "DESKTOPHEIGHT") to find the current desktop resolution to place the program's window.
* On dual monitors a negative *column&* position or a value greater than the main screen width can be used to position a window in another monitor.
* **A small delay may be necessary when a program first starts up to properly orient the screen on the desktop properly.** See [\_SCREENEXISTS](/qb64wiki/index.php/SCREENEXISTS "SCREENEXISTS").
* **[Keyword not supported in Linux versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Availability


* [![v0.926](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v0.926")

**v0.926**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![no](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "no")

**no**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


*Example 1:* Calculating the border and header offsets by comparing a coordinate move with \_MIDDLE by using trial and error.





| ``` userwidth& = [_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH"): userheight& = [_DESKTOPHEIGHT](/qb64wiki/index.php/DESKTOPHEIGHT "DESKTOPHEIGHT") 'get current screen resolution [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 256) scrnwidth& = [_WIDTH](/qb64wiki/index.php/WIDTH "WIDTH"): scrnheight& = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")  'get the dimensions of the program screen  _SCREENMOVE (userwidth& \ 2 - scrnwidth& \ 2) - 3, (userheight& \ 2 - scrnheight& \ 2) - 29 [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 4 _SCREENMOVE _MIDDLE  'check centering  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


When positioning the window, offset the position by -3 columns and - 29 rows to calculate the top left corner coordinate.
  

*Example 2:* Moving a program window to a second monitor positioned to the right of the main desktop.





| ``` wide& = [_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH") high& = [_DESKTOPHEIGHT](/qb64wiki/index.php/DESKTOPHEIGHT "DESKTOPHEIGHT")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") wide&; "X"; high&  [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 4 _SCREENMOVE wide& + 200, 200 'positive value for right monitor 2  img2& = [_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE") wide2& = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(img2&) high2& = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(img2&) [PRINT](/qb64wiki/index.php/PRINT "PRINT") wide2&; "X"; high2& [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 4 _SCREENMOVE _MIDDLE 'moves program back to main monitor 1  ``` |
| --- |


*Notes:* Change the \_SCREENMOVE column to negative for a left monitor.
**[\_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN") works in the primary monitor and may push all running programs to a monitor on the right.**
  




## See also


* [\_SCREENX](/qb64wiki/index.php/SCREENX "SCREENX"), [\_SCREENY](/qb64wiki/index.php/SCREENY "SCREENY")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE"), [\_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH"), [\_DESKTOPHEIGHT](/qb64wiki/index.php/DESKTOPHEIGHT "DESKTOPHEIGHT")
* [\_SCREENPRINT](/qb64wiki/index.php/SCREENPRINT "SCREENPRINT")
* [\_SCREENEXISTS](/qb64wiki/index.php/SCREENEXISTS "SCREENEXISTS")
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SCREENMOVE&oldid=7748>"




## Navigation menu








### Search





















