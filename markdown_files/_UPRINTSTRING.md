


\_UPRINTSTRING - QB64 Phoenix Edition Wiki








# \_UPRINTSTRING



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_UPRINTSTRING** statement prints ASCII / UNICODE text [strings](/qb64wiki/index.php/STRING "STRING") using graphic column and row coordinate positions.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


\_UPRINTSTRING (*column*, *row*), *textExpression$*[, *maxWidth&*][, *utfEncoding&*][, *fontHandle&*][, *imageHandle&*]
  




## Parameters


* *column* and *row* are [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [LONG](/qb64wiki/index.php/LONG "LONG") starting PIXEL (graphic) column and row coordinates to set text or custom fonts.
* *textExpression$* is any literal or variable [string](/qb64wiki/index.php/STRING "STRING") value of text to be displayed.
* *maxWidth&* is an optional horizontal pixel limit after which the text rendering will be clipped.
* *utfEncoding&* is an optional UTF encoding of *textExpression$*. This can be 0 for ASCII, 8 for UTF-8, 16 for UTF-16 or 32 for UTF-32.
* *fontHandle&* is an optional font handle.
* *imageHandle&* is the optional image or destination to use. Zero designates current [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") page.


  




## Description


* The starting coordinate sets the top left corner of the text to be printed.
* If *maxWidth&* is omitted, then the entire *textExpression$* is rendered.
* If *utfEncoding&* is omitted, then it is assumed to be 0 (ASCII).
* If *fontHandle&* is omitted, then the current write page font is used.
* [\_UPRINTWIDTH](/qb64wiki/index.php/UPRINTWIDTH "UPRINTWIDTH") can be used to determine how wide a text print will be so that the screen width is not exceeded. Alternatively, *maxWidth&* can be used to clip text rending after a certain amount of pixel width.
* [\_ULINESPACING](/qb64wiki/index.php/ULINESPACING "ULINESPACING") can be used to calculate the next [font](/qb64wiki/index.php/FONT "FONT") vertical position.
* Unicode byte order mark (BOM) is not processed and must be handled by user code except for UTF-16.
* UTF-16 LE is assumed if BOM is absent in the string and *utfEncoding&* is 16.
* Can use the current font alpha blending with a designated image background. See the [\_RGBA](/qb64wiki/index.php/RGBA "RGBA") function example.
* Use the [\_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE") statement before printing to set how the background is rendered.
	+ Use the [\_PRINTMODE (function)](/qb64wiki/index.php/PRINTMODE_(function) "PRINTMODE (function)") to find the current \_PRINTMODE setting.
* SCREEN 0 (text only) mode is not supported. Attempting to use this in SCREEN 0 will generate an error.


  




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


Example 1
Centers and prints a Russian text on a graphics screen.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32)  [DIM](/qb64wiki/index.php/DIM "DIM") fh [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): fh = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("cyberbit.ttf", 21) [IF](/qb64wiki/index.php/IF "IF") fh <= 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to load font file!"     [END](/qb64wiki/index.php/END "END") [END IF](/qb64wiki/index.php/END_IF "END IF")  [_FONT](/qb64wiki/index.php/FONT "FONT") fh  [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") text_data [DIM](/qb64wiki/index.php/DIM "DIM") myString [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"): myString = LoadUData$  _UPRINTSTRING ([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") \ 2 - [_UPRINTWIDTH](/qb64wiki/index.php/UPRINTWIDTH "UPRINTWIDTH")(myString, 8, fh) \ 2, [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") \ 2 - [_UFONTHEIGHT](/qb64wiki/index.php/UFONTHEIGHT "UFONTHEIGHT") \ 2), myString, [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)"), 8  [END](/qb64wiki/index.php/END "END")  text_data: [DATA](/qb64wiki/index.php/DATA "DATA") 6F,D0,91,D1,8B,D1,81,D1,82,D1,80,D0,B0,D1,8F,20,D0,BA,D0,BE,D1,80,D0,B8,D1 [DATA](/qb64wiki/index.php/DATA "DATA") 87,D0,BD,D0,B5,D0,B2,D0,B0,D1,8F,20,D0,BB,D0,B8,D1,81,D0,B0,20,D0,BF,D0,B5 [DATA](/qb64wiki/index.php/DATA "DATA") D1,80,D0,B5,D0,BF,D1,80,D1,8B,D0,B3,D0,B8,D0,B2,D0,B0,D0,B5,D1,82,20,D1,87 [DATA](/qb64wiki/index.php/DATA "DATA") D0,B5,D1,80,D0,B5,D0,B7,20,D0,BB,D0,B5,D0,BD,D0,B8,D0,B2,D1,83,D1,8E,20,D1 [DATA](/qb64wiki/index.php/DATA "DATA") 81,D0,BE,D0,B1,D0,B0,D0,BA,D1,83,2E  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") LoadUData$     [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") i, s     [DIM](/qb64wiki/index.php/DIM "DIM") d [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING")     [DIM](/qb64wiki/index.php/DIM "DIM") buffer [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING")      [READ](/qb64wiki/index.php/READ "READ") d     s = [VAL](/qb64wiki/index.php/VAL "VAL")("&h" + d)     buffer = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(s)      [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") s         [READ](/qb64wiki/index.php/READ "READ") d         [ASC](/qb64wiki/index.php/ASC "ASC")(buffer, i) = [VAL](/qb64wiki/index.php/VAL "VAL")("&h" + d)     [NEXT](/qb64wiki/index.php/NEXT "NEXT")      LoadUData = buffer [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |




---


Example 2
Prints multiple lines of text using a recommended line gap.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32)  [DIM](/qb64wiki/index.php/DIM "DIM") fh [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): fh = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("LHANDW.TTF", 23) [IF](/qb64wiki/index.php/IF "IF") fh <= 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to load font file!"     [END](/qb64wiki/index.php/END "END") [END IF](/qb64wiki/index.php/END_IF "END IF")  [_FONT](/qb64wiki/index.php/FONT "FONT") fh  [CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(200, 200, 200) [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(0, 0, 0) [_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE") [_KEEPBACKGROUND](/qb64wiki/index.php/KEEPBACKGROUND "KEEPBACKGROUND")  [DIM](/qb64wiki/index.php/DIM "DIM") l [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), i [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") [FOR](/qb64wiki/index.php/FOR "FOR") i = 0 [TO](/qb64wiki/index.php/TO "TO") 4     [READ](/qb64wiki/index.php/READ "READ") l     _UPRINTSTRING (0, [_ULINESPACING](/qb64wiki/index.php/ULINESPACING "ULINESPACING") * i), l [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [END](/qb64wiki/index.php/END "END")  [DATA](/qb64wiki/index.php/DATA "DATA") "We are not now that strength which in old days" [DATA](/qb64wiki/index.php/DATA "DATA") "Moved earth and heaven; that which we are,we are;" [DATA](/qb64wiki/index.php/DATA "DATA") "One equal temper of heroic hearts," [DATA](/qb64wiki/index.php/DATA "DATA") "Made weak by time and fate,but strong in will" [DATA](/qb64wiki/index.php/DATA "DATA") "To strive,to seek,to find,and not to yield."  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series (Part 1)](https://qb64phoenix.com/forum/showthread.php?tid=2765)
* [Featured in our "Keyword of the Day" series (Part 2)](https://qb64phoenix.com/forum/showthread.php?tid=2778)
* [\_UPRINTWIDTH](/qb64wiki/index.php/UPRINTWIDTH "UPRINTWIDTH"), [\_UFONTHEIGHT](/qb64wiki/index.php/UFONTHEIGHT "UFONTHEIGHT"), [\_ULINESPACING](/qb64wiki/index.php/ULINESPACING "ULINESPACING"), [\_UCHARPOS](/qb64wiki/index.php/UCHARPOS "UCHARPOS")
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH"), [\_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE")
* [\_CONTROLCHR](/qb64wiki/index.php/CONTROLCHR "CONTROLCHR")
* [\_FONT](/qb64wiki/index.php/FONT "FONT"), [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT"), [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT"), [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE"), [\_SCREENPRINT](/qb64wiki/index.php/SCREENPRINT "SCREENPRINT")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=UPRINTSTRING&oldid=8970>"




## Navigation menu








### Search





















