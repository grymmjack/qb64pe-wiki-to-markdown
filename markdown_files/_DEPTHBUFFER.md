


\_DEPTHBUFFER - QB64 Phoenix Edition Wiki








# \_DEPTHBUFFER



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_DEPTHBUFFER statement turns depth buffering ON or OFF, LOCKs or \_CLEARS the buffer.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


\_DEPTHBUFFER {ON|OFF|LOCK|\_CLEAR}[,handle&]
  




## Description


* Depth buffers store the distance of each pixel on an image/surface. When 3D drawing occurs new pixels are only drawn if they are closer than the existing pixels. After all content is drawn, it results in a scene which looks correct because content which is closer hides content which is further away.
* Depth buffers are automatically created for any hardware image or surface which is the target/destination of a 3D command (such as the 3D version of [\_MAPTRIANGLE](/qb64wiki/index.php/MAPTRIANGLE "MAPTRIANGLE")).
* The buffering can be turned ON, OFF or LOCKed. The default state is ON.
* \_DEPTHBUFFER \_CLEAR can be used to reset/erase the depth buffer, meaning that future drawing will not be blocked by existing/previously buffered depth content.
* Whenever \_DISPLAY is called the primary surface's depth buffer is automatically \_CLEARed, so unless you are drawing onto a hardware image you may never need to use this option.
* LOCKing the depth buffer makes it read only. New content cannot be drawn unless it is closer than existing content, but when that new content is drawn it will not update the depth buffer.
* Turning OFF or LOCKing the depth buffer is typically performed when semi-transparent content is being drawn.


  




## See also


* [\_MAPTRIANGLE](/qb64wiki/index.php/MAPTRIANGLE "MAPTRIANGLE")
* [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE")
* [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DEPTHBUFFER&oldid=7262>"




## Navigation menu








### Search





















