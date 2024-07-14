


\_DISPLAYORDER - QB64 Phoenix Edition Wiki








# \_DISPLAYORDER



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_DISPLAYORDER statement defines the order to render software, hardware and custom-OpenGL-code.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) 	+ [3.1 Errors](#Errors) * [4 Availability](#Availability) * [5 See also](#See_also) |
| --- |


## Syntax


\_DISPLAYORDER [{\_SOFTWARE|\_HARDWARE|\_HARDWARE1|\_GLRENDER}][, ...][, ...][, ...][, ...]
  




## Parameters


* \_SOFTWARE refers to software created surfaces or [SCREENs](/qb64wiki/index.php/SCREEN "SCREEN").
* \_HARDWARE and \_HARDWARE1 refer to surfaces created by OpenGL hardware acceleration.
* \_GLRENDER refers to OpenGL code rendering order


  




## Description


* The default on program start is: \_DISPLAYORDER \_SOFTWARE, \_HARDWARE, \_GLRENDER, \_HARDWARE1
* Any content or combination order is allowed, except listing the same content twice consecutively.
* Simply using \_DISPLAYORDER \_HARDWARE will render hardware surfaces only.
* Use an [underscore](/qb64wiki/index.php/Underscore "Underscore") to continue a code line on a new text row in the IDE.
* After \_DISPLAYORDER has been used, it must be used to make any changes, even to default.


### Errors


* If a rendering content is not listed it will not be rendered except when using the startup default.
* Rendering the same content twice consecutively in a combination is not allowed.


  




## Availability


* **Version 1.000 and up.**


  




## See also


* [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")
* [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE")
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")
* [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")
* [Hardware images](/qb64wiki/index.php/Hardware_images "Hardware images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DISPLAYORDER&oldid=7494>"




## Navigation menu








### Search





















