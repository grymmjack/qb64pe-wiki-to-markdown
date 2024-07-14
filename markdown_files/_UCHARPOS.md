


\_UCHARPOS - QB64 Phoenix Edition Wiki








# \_UCHARPOS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_UCHARPOS** function calculates the starting pixel positions of every character of the text [string](/qb64wiki/index.php/STRING "STRING") (0 being the starting pixel position of the first character). This information is returned in a [long](/qb64wiki/index.php/LONG "LONG") array. The function also returns the number of characters in the text [string](/qb64wiki/index.php/STRING "STRING"). The function supports Unicode encoded text.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*codepoints&* = \_UCHARPOS(*text$*[, *posArray&()*][, *utfEncoding&*][, *fontHandle&*])
  




## Parameters


* *text$* is any literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") value. This can be a Unicode encoded text.
* *posArray&()* is a [long](/qb64wiki/index.php/LONG "LONG") array that contains the pixel position information after a call to **\_UCHARPOS**.
* *utfEncoding&* is an optional UTF encoding of *text$*. This can be 0 for ASCII, 8 for UTF-8, 16 for UTF-16 or 32 for UTF-32.
* *fontHandle&* is an optional font handle.


  




## Description


* If *posArray&()* is omitted, then the function simply returns the number of characters in the text [string](/qb64wiki/index.php/STRING "STRING").
* If *utfEncoding&* is omitted, then it is assumed to be 0 (ASCII).
* If *fontHandle&* is omitted, then the current write page font is used.
* *posArray&(codepoints&)* (assuming *posArray&()* is declared (indexed) as 0 [TO](/qb64wiki/index.php/TO "TO") *codepoints&*) will hold the (ending pixel position of the last character) + 1.
* All multi-byte UTF encodings are expected in little-endian.
* Unicode byte order mark (BOM) is not processed and must be handled by user code.
* This can be useful when the positions of every character in a string is required (e.g., when underling text or drawing a text cursor). This can be especially helpful when using variable width fonts.
* When working with Unicode excoded text, instead of calling the function twice (first time to get the array size and then a second time to get the pixel positions), call it once with a large enough array (0 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(*text$*)) and then resize the array (0 [TO](/qb64wiki/index.php/TO "TO") *codepoints&*) using [REDIM](/qb64wiki/index.php/REDIM "REDIM") [PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE").


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.8.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.8.0")

**v3.8.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


Example
Underlines every character of a text printed using a variable width font.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  [CONST](/qb64wiki/index.php/CONST "CONST") TEXT = "Hello, world!" [CONST](/qb64wiki/index.php/CONST "CONST") TEXT_X = 220 [CONST](/qb64wiki/index.php/CONST "CONST") TEXT_Y = 220  [DIM](/qb64wiki/index.php/DIM "DIM") fh [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): fh = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("arial.ttf", 32) [_FONT](/qb64wiki/index.php/FONT "FONT") fh  [DIM](/qb64wiki/index.php/DIM "DIM") arr(0 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(TEXT)) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), i [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Len of "; TEXT; " ="; _UCHARPOS(TEXT, arr())  [_UPRINTSTRING](/qb64wiki/index.php/UPRINTSTRING "UPRINTSTRING") (TEXT_X, TEXT_Y), TEXT  [FOR](/qb64wiki/index.php/FOR "FOR") i = [LBOUND](/qb64wiki/index.php/LBOUND "LBOUND")(arr) [TO](/qb64wiki/index.php/TO "TO") [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")(arr) - 1     [PRINT](/qb64wiki/index.php/PRINT "PRINT") arr(i + 1);     [LINE](/qb64wiki/index.php/LINE "LINE") (TEXT_X + arr(i), TEXT_Y + [_UFONTHEIGHT](/qb64wiki/index.php/UFONTHEIGHT "UFONTHEIGHT"))-(TEXT_X + arr(i + 1) - 1, TEXT_Y + [_UFONTHEIGHT](/qb64wiki/index.php/UFONTHEIGHT "UFONTHEIGHT")), 9 + i [MOD](/qb64wiki/index.php/MOD "MOD") 7 [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2826)
* [\_UFONTHEIGHT](/qb64wiki/index.php/UFONTHEIGHT "UFONTHEIGHT"), [\_ULINESPACING](/qb64wiki/index.php/ULINESPACING "ULINESPACING"), [\_UPRINTWIDTH](/qb64wiki/index.php/UPRINTWIDTH "UPRINTWIDTH"), [\_UPRINTSTRING](/qb64wiki/index.php/UPRINTSTRING "UPRINTSTRING")
* [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH"), [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT"), [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH")
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")
* [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING"), [\_FONT](/qb64wiki/index.php/FONT "FONT")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=UCHARPOS&oldid=9015>"




## Navigation menu








### Search





















