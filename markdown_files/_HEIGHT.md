


\_HEIGHT - QB64 Phoenix Edition Wiki








# \_HEIGHT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_HEIGHT function returns the height of an image handle or of the current write page.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*columns&* = \_HEIGHT[(*imageHandle&*)]
  




## Description


* If *imageHandle&* is omitted, it's assumed to be the handle of the current [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") or write page.
* To get the height of the current program [screen](/qb64wiki/index.php/SCREEN "SCREEN") window use zero for the handle value or nothing: *lines&* = \_HEIGHT(0) *or* *lines&* = \_HEIGHT
* If the image specified by *imageHandle&* is in text only([SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0) mode, the number of lines of rows of characters are returned.
* If the image specified by *imageHandle&* is in graphics mode, the number rows of pixels is returned.
* If *imageHandle&* is an invalid handle, then an [invalid handle error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") is returned.
* The last visible pixel coordinate of a program [screen](/qb64wiki/index.php/SCREEN "SCREEN") is **\_HEIGHT - 1**.


  




## See also


* [\_WIDTH (function)](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)"), [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")
* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=HEIGHT&oldid=7305>"




## Navigation menu








### Search





















