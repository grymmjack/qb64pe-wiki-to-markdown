


\_SCREENIMAGE - QB64 Phoenix Edition Wiki








# \_SCREENIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SCREENIMAGE function stores the current desktop image or a portion of it and returns an image handle.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) 	+ [3.1 Sample code to save images to disk](#Sample_code_to_save_images_to_disk) * [4 See also](#See_also) |
| --- |


## Syntax


*imageHandle&* = \_SCREENIMAGE[(*column1*, *row1*, *column2*, *row2*)]
  




## Description


* *imageHandle&* is the handle to the new image in memory that will contain the desktop screenshot.
* The optional screen *column* and *row* positions can be used to get only a portion of the desktop image.
* The desktop image or partial image is always a 32-bit image.
* The current screen resolution or width-to-height aspect ratio can be obtained with [\_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH") and [\_DESKTOPHEIGHT](/qb64wiki/index.php/DESKTOPHEIGHT "DESKTOPHEIGHT").
* Can be used to take screenshots of the desktop or used with [\_PRINTIMAGE](/qb64wiki/index.php/PRINTIMAGE "PRINTIMAGE") to print them.
* It is important to free unused or uneeded image handles with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") to prevent memory overflow errors.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Examples


*Example:* Determining the present screen resolution of user's PC for a screensaver program.





| ```  desktop& = _SCREENIMAGE  MaxScreenX& = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(desktop&)  MaxScreenY& = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(desktop&)  [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") desktop& 'free image after measuring screen(it is not displayed)  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(MaxScreenX&, MaxScreenY&, 256) 'program window is sized to fit  [_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE") _MIDDLE  ``` |
| --- |


### Sample code to save images to disk


* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [Program ScreenShots](/qb64wiki/index.php/Program_ScreenShots "Program ScreenShots") (member-contributed program for legacy screen modes)
* [ThirtyTwoBit SUB](/qb64wiki/index.php/ThirtyTwoBit_SUB "ThirtyTwoBit SUB")
* [SaveIcon32](/qb64wiki/index.php/SaveIcon32 "SaveIcon32")


  




## See also


* [\_SCREENCLICK](/qb64wiki/index.php/SCREENCLICK "SCREENCLICK"), [\_SCREENPRINT](/qb64wiki/index.php/SCREENPRINT "SCREENPRINT")
* [\_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE"), [\_SCREENX](/qb64wiki/index.php/SCREENX "SCREENX"), [\_SCREENY](/qb64wiki/index.php/SCREENY "SCREENY")
* [\_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)"), [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")
* [\_DESKTOPWIDTH](/qb64wiki/index.php/DESKTOPWIDTH "DESKTOPWIDTH"), [\_DESKTOPHEIGHT](/qb64wiki/index.php/DESKTOPHEIGHT "DESKTOPHEIGHT")
* [\_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN"), [\_PRINTIMAGE](/qb64wiki/index.php/PRINTIMAGE "PRINTIMAGE")
* [Screen Saver Programs](/qb64wiki/index.php/Screen_Saver_Programs "Screen Saver Programs")
* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps"), [Icons and Cursors](/qb64wiki/index.php/Icons_and_Cursors "Icons and Cursors")
* [Hardware images](/qb64wiki/index.php/Hardware_images "Hardware images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SCREENIMAGE&oldid=8673>"




## Navigation menu








### Search





















