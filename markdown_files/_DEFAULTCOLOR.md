


\_DEFAULTCOLOR - QB64 Phoenix Edition Wiki








# \_DEFAULTCOLOR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_DEFAULTCOLOR** function returns the current default (text/drawing) color for an image handle or page.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*col~&* = \_DEFAULTCOLOR [(*imageHandle&*)]
  




## Parameters


* If *imageHandle&* is omitted, it is assumed to be the current write page or image designated by [\_DEST](/qb64wiki/index.php/DEST "DEST").
* If *imageHandle&* is an invalid handle, an [Invalid handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error occurs. Check handle values first. Zero designates the current screen.


  




## Description


* Use it to get the current default (foreground) color to restore it later in a program.
* In legacy [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes and in [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") 256 colors mode the color attribute/palette index is returned.
* In [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") 32-bit mode the [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32") value (**&H00000000** to **&HFFFFFFFF**) is returend, make sure to store it in an [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") variable (as seen in the syntax above with the **~&** suffix), otherwise the blue component may be lost.


  




## Examples


Example
Storing the default color for later use. The default color is the color set as foreground.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 4, 7 'set color 4 as foreground, color 7 as background [CLS](/qb64wiki/index.php/CLS "CLS") col~& = _DEFAULTCOLOR [PRINT](/qb64wiki/index.php/PRINT "PRINT") col~&  ``` |
| --- |




| ``` 4  ``` |
| --- |


  




## See also


* [\_BACKGROUNDCOLOR](/qb64wiki/index.php/BACKGROUNDCOLOR "BACKGROUNDCOLOR")
* [COLOR](/qb64wiki/index.php/COLOR "COLOR"), [\_DEST](/qb64wiki/index.php/DEST "DEST")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [SCREEN (function)](/qb64wiki/index.php/SCREEN_(function) "SCREEN (function)")
* [Color Dialog Box](/qb64wiki/index.php/Windows_Libraries#Color_Dialog_Box "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DEFAULTCOLOR&oldid=8302>"




## Navigation menu








### Search





















