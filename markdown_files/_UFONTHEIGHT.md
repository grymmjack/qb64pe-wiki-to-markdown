


\_UFONTHEIGHT - QB64 Phoenix Edition Wiki








# \_UFONTHEIGHT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_UFONTHEIGHT** function returns the global glyph height (incl. ascender/descender) of a font loaded by [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT").


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*pixelHeight&* = \_UFONTHEIGHT[(*fontHandle&*)]
  




## Parameters


* *fontHandle&* is an optional font handle.


  




## Description


* Returns the height of the last font used if a handle is not designated.
* If no font is set, it returns the current screen mode's text block height.
* This is different from [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT") as it may return larger values when using scalable fonts.


  




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
Show the difference of **\_UFONTHEIGHT** vs. [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT").


| ``` [DIM](/qb64wiki/index.php/DIM "DIM") fh [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): fh = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("LHANDW.TTF", 23)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_FONTHEIGHT ="; [_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT")(fh) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_UFONTHEIGHT ="; _UFONTHEIGHT(fh)  ``` |
| --- |




| ``` _FONTHEIGHT = 23 _UFONTHEIGHT = 32  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2810)
* [\_UPRINTWIDTH](/qb64wiki/index.php/UPRINTWIDTH "UPRINTWIDTH"), [\_ULINESPACING](/qb64wiki/index.php/ULINESPACING "ULINESPACING"), [\_UPRINTSTRING](/qb64wiki/index.php/UPRINTSTRING "UPRINTSTRING"), [\_UCHARPOS](/qb64wiki/index.php/UCHARPOS "UCHARPOS")
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





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=UFONTHEIGHT&oldid=9008>"




## Navigation menu








### Search





















