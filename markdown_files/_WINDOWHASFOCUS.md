


\_WINDOWHASFOCUS - QB64 Phoenix Edition Wiki








# \_WINDOWHASFOCUS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_WINDOWHASFOCUS function returns true (-1) if the current program's window has focus. Not supported for macOS.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*hasFocus%%* = \_WINDOWHASFOCUS
  




## Description


* The function returns true (-1) if the current program is the topmost window on the user's desktop and has focus. If the current program is running behind another window, the function returns false (0).
* **[Keyword not supported in macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Availability


* [![v1.2](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v1.2")

**v1.2**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![no](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "no")

**no**


  




## Examples


*Example:* Detecting if the current program has focus. Windows and Linux-only.





| ``` [DO](/qb64wiki/index.php/DO "DO")     [IF](/qb64wiki/index.php/IF "IF") _WINDOWHASFOCUS THEN         [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15, 6         [CLS](/qb64wiki/index.php/CLS "CLS")         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "*** Hi there! ***"     [ELSE](/qb64wiki/index.php/ELSE "ELSE")         [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0, 7         [CLS](/qb64wiki/index.php/CLS "CLS")         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "(ain't nobody looking...)"     [END IF](/qb64wiki/index.php/END_IF "END IF")     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30 [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


*Explanation:* The program will display *"\*\*\* Hi There! \*\*\*"* while the window is the topmost and is being manipulated by the user. If another window, the taskbar or the desktop are clicked, the program window loses focus and the message *"(ain't nobody looking...)"* is displayed.
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1084)
* [\_WINDOWHANDLE](/qb64wiki/index.php/WINDOWHANDLE "WINDOWHANDLE")
* [\_SCREENEXISTS](/qb64wiki/index.php/SCREENEXISTS "SCREENEXISTS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=WINDOWHASFOCUS&oldid=8885>"




## Navigation menu








### Search





















