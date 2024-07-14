


\_COPYIMAGE - QB64 Phoenix Edition Wiki








# \_COPYIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
This function creates an identical designated image in memory with a different negative [LONG](/qb64wiki/index.php/LONG "LONG") handle value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


newhandle& = \_COPYIMAGE(*imageHandle&*[, *mode%*])
  




## Parameters


* The [LONG](/qb64wiki/index.php/LONG "LONG") *newhandle&* value returned will be different than the source handle value supplied.
* If *imageHandle&* is designated being zero, the current software [destination](/qb64wiki/index.php/DEST "DEST") screen or image is copied.
* If 1 is designated instead of an *imageHandle&*, it designates the last OpenGL hardware surface to copy.
* *Mode* 32 can be used to convert 256 color images to 32 bit colors.
* *Mode* 33 images are hardware accelerated in **version 1.000 and up**, and are created using [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") or \_COPYIMAGE.


  




## Description


* The function copies any image or screen handle to a new and unique negative [LONG](/qb64wiki/index.php/LONG "LONG") handle value.
* Valid copy handles are less than -1. Invalid handles return -1 or 0 if it was never created.
* Every attribute of the passed image or program screen is copied to a new handle value in memory.
* **32 bit screen surface backgrounds (black) have zero [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") so that they are transparent when placed over other surfaces.**


Use [CLS](/qb64wiki/index.php/CLS "CLS") or [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") to make a new surface background [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") 255 or opaque.
* **Images are not deallocated when the [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") they are created in ends. Free them with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE").**
* **It is important to free discarded images with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") to prevent PC memory allocation errors!**
* **Do not try to free image handles currently being used as the active [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"). Change screen modes first.**


  




## Examples


Example 1
Restoring a Legacy SCREEN using the \_COPYIMAGE return value.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (160, 100), 100, 40 [DO](/qb64wiki/index.php/DO "DO"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  'backup screen before changing SCREEN mode oldmode& = _COPYIMAGE(0) 'the 0 value designates the current destination SCREEN  s& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") s& [LINE](/qb64wiki/index.php/LINE "LINE") (100, 100)-(500, 500), [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 255, 255), BF [DO](/qb64wiki/index.php/DO "DO"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") oldmode& 'restore original screen [IF](/qb64wiki/index.php/IF "IF") s& < -1 [THEN](/qb64wiki/index.php/THEN "THEN") [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") s& [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code courtesy of Galleon
Note
Only free valid handle values with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") AFTER a new [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode is being used by the program.


---


Example 2
Program that copies desktop to a hardware image to form a 3D triangle (**version 1.000 and up**):


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) my_hardware_handle = _COPYIMAGE([_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE"), 33) 'take a screenshot and use it as our texture [_MAPTRIANGLE](/qb64wiki/index.php/MAPTRIANGLE "MAPTRIANGLE") (0, 0)-(500, 0)-(250, 500), my_hardware_handle [TO](/qb64wiki/index.php/TO "TO") _ (-1, 0, -1)-(1, 0, -1)-(0, 5, -10), , [_SMOOTH](/qb64wiki/index.php/SMOOTH_(function) "SMOOTH (function)") [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30: [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  ``` |
| --- |


Code courtesy of Galleon
  




## See also


* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_SAVEIMAGE](/qb64wiki/index.php/SAVEIMAGE "SAVEIMAGE")
* [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE"), [\_MAPTRIANGLE](/qb64wiki/index.php/MAPTRIANGLE "MAPTRIANGLE")
* [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE"), [\_DEST](/qb64wiki/index.php/DEST "DEST")
* [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE")
* [\_FILELIST$ (function)](/qb64wiki/index.php/FILELIST$_(function) "FILELIST$ (function)") (Demo of \_COPYIMAGE)
* [\_DISPLAYORDER](/qb64wiki/index.php/DISPLAYORDER "DISPLAYORDER")
* [Hardware images](/qb64wiki/index.php/Hardware_images "Hardware images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=COPYIMAGE&oldid=8683>"




## Navigation menu








### Search





















