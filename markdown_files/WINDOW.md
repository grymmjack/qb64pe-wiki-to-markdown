


WINDOW - QB64 Phoenix Edition Wiki








# WINDOW



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **WINDOW** command scales the graphics coordinate system of the current [\_DEST](/qb64wiki/index.php/DEST "DEST") image, optionally inverting the direction of the vertical axis. Any coordinates used in drawing commands made to the image are scaled such that the image seems have have the dimensions requested.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


**WINDOW** [ [ **SCREEN**] (*x1!*, *y1!*) - (*x2!*, *y2!*)]
  




## Parameters


Where (*x1!*, *y1!*)-(*x2!*, *y2!*) specifies the new dimensions of the image to scale to. Non-integer values may be used.
Using **WINDOW** with no parameters reverts the effect of any previous calls to it.


  




## Description


When a command such as [LINE](/qb64wiki/index.php/LINE "LINE"), [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") or [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") needs a position in an image specified, it is given as a combination of x (horizontal) and y (vertical) coordinates. Usually these values are measured as pixels from the top-left origin. The **WINDOW** command changes the way these values are measured. This is best illustrated with an example:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(600, 600, 32) '600 pixels in x and y directions and displayed on screen WINDOW [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") (0, 0)-(6, 6)  ``` |
| --- |


The coordinates of the image now run from 0 to 6 in both the x and y directions. The centre of the screen is now referred to as (3, 3) and the bottom-right corner of the screen is (6, 6). The image has not actually just changed size or the number of pixels, just the way the program refers to positions on the image. Despite this example, there is no requirement for the image or scaling coordinates to be square; each direction is scaled independently, and can result in commands such as LINE (0, 0)-(10, 10), , BF drawing a rectangle instead of a square.


If the **SCREEN** part is omitted, the y axis is inverted. Thus the origin is now at the bottom-left, and y coordinates increase as you move up the screen. Such a system may be more familiar to mathematically-oriented programmers.


**WINDOW** does not change any of the content already on the image; it only modifies coordinates used while it is in effect. The scaling is relative to the original image, so successive invocations do not compound upon each other.


Although **WINDOW** affects all coordinates, it does not affect all graphics operations entirely. [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE"), if only given one destination coordinate, will not scale or stretch the image being drawn. [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") will scale its radius such that it matches the horizontal axis. This means it always draws perfect circles even if the scaling of the two axes are not the same, but the radius measured against the vertical scale may not be correct.


The location of the graphics cursor (used to calculate relative positions for STEP) is not affected. It will remain in the same position on the image, but the relative coordinates that are specified with STEP will be scaled as described above.


  




## Examples


Demonstrate a circle's radius only matching the scaling in the horizontal direction by comparing against a box:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) 'Not a square image WINDOW [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") (0, 0)-(10, 10) 'SCREEN keeps the axis direction the same [LINE](/qb64wiki/index.php/LINE "LINE") (4, 4)-(6, 6), [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(255, 0, 0), BF 'Red square centred on (5, 5); will be stretched into a rectangle [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (5, 5), 1, [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(0, 255, 0) 'Green circle at (5, 5) with radius 1  ``` |
| --- |


  




## See also


* [PMAP](/qb64wiki/index.php/PMAP "PMAP")
* [VIEW](/qb64wiki/index.php/VIEW "VIEW")
* [VIEW PRINT](/qb64wiki/index.php/VIEW_PRINT "VIEW PRINT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=WINDOW&oldid=7470>"




## Navigation menu








### Search





















