


\_ULINESPACING - QB64 Phoenix Edition Wiki








# \_ULINESPACING



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_ULINESPACING** function returns the vertical line spacing (distance between two consecutive baselines) in pixels.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*pixels&* = \_ULINESPACING[(*fontHandle&*)]
  




## Parameters


* *fontHandle&* is an optional font handle.


  




## Description


* Returns the vertical line spacing of the last font used if a handle is not designated.
* If no font is set, it returns the current screen mode's text block height.
* This can be used to leave the correct amount of line gap between lines.


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.7.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.7.0")

**v3.7.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


Example
How to use \_ULINESPACING.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32)  [DIM](/qb64wiki/index.php/DIM "DIM") fh [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): fh = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("LHANDW.TTF", 23) [IF](/qb64wiki/index.php/IF "IF") fh <= 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to load font file!"     [END](/qb64wiki/index.php/END "END") [END IF](/qb64wiki/index.php/END_IF "END IF")  [_FONT](/qb64wiki/index.php/FONT "FONT") fh  [CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(200, 200, 200) [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(0, 0, 0) [_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE") [_KEEPBACKGROUND](/qb64wiki/index.php/KEEPBACKGROUND "KEEPBACKGROUND")  [DIM](/qb64wiki/index.php/DIM "DIM") l [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), i [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") [FOR](/qb64wiki/index.php/FOR "FOR") i = 0 [TO](/qb64wiki/index.php/TO "TO") 4     [READ](/qb64wiki/index.php/READ "READ") l     [_UPRINTSTRING](/qb64wiki/index.php/UPRINTSTRING "UPRINTSTRING") (0, _ULINESPACING * i), l [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [END](/qb64wiki/index.php/END "END")  [DATA](/qb64wiki/index.php/DATA "DATA") "We are not now that strength which in old days" [DATA](/qb64wiki/index.php/DATA "DATA") "Moved earth and heaven; that which we are,we are;" [DATA](/qb64wiki/index.php/DATA "DATA") "One equal temper of heroic hearts," [DATA](/qb64wiki/index.php/DATA "DATA") "Made weak by time and fate,but strong in will" [DATA](/qb64wiki/index.php/DATA "DATA") "To strive,to seek,to find,and not to yield."  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2819)
* [\_UPRINTWIDTH](/qb64wiki/index.php/UPRINTWIDTH "UPRINTWIDTH"), [\_UFONTHEIGHT](/qb64wiki/index.php/UFONTHEIGHT "UFONTHEIGHT"), [\_UPRINTSTRING](/qb64wiki/index.php/UPRINTSTRING "UPRINTSTRING"), [\_UCHARPOS](/qb64wiki/index.php/UCHARPOS "UCHARPOS")
* [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH"), [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT"), [\_FONT](/qb64wiki/index.php/FONT "FONT")
* [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH"), [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ULINESPACING&oldid=9014>"




## Navigation menu








### Search





















