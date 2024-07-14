


\_PRINTWIDTH - QB64 Phoenix Edition Wiki








# \_PRINTWIDTH



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_PRINTWIDTH function returns the width in pixels of the text [string](/qb64wiki/index.php/STRING "STRING") specified.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*pixelWidth%* = \_PRINTWIDTH(*textToPrint$*[, *destinationHandle&*])
  




## Description


* *textToPrint$* is any literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") value.
* If the *destinationHandle&* is omitted, the current destination image or screen page is used.
* Useful to find the width of the font print [string](/qb64wiki/index.php/STRING "STRING") before actually printing it.
* Can be used with variable-width fonts or built-in fonts, unlike [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH") which requires a MONOSPACE font handle.
* In SCREEN 0, \_PRINTWIDTH returns the character length of a text string, exactly as [LEN](/qb64wiki/index.php/LEN "LEN")(*textToPrint$*) (**version 1.000 and up**).


  




## Examples


*Example:* SUB returns font or screen mode's text block size using \_PRINTWIDTH and [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT") without a handle parameter.





| ``` [DO](/qb64wiki/index.php/DO "DO")   [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter Screen mode 1, 2 or 7 to 13: ", scr$   mode% = [VAL](/qb64wiki/index.php/VAL "VAL")(scr$) [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") mode% > 0 [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode% [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter first name of TTF font to use or hit enter for text size: ", TTFont$ [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")(TTFont$) [THEN](/qb64wiki/index.php/THEN "THEN") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") "Enter font height: ", hi$ height& = [VAL](/qb64wiki/index.php/VAL "VAL")(hi$) [IF](/qb64wiki/index.php/IF "IF") height& > 0 [THEN](/qb64wiki/index.php/THEN "THEN") [_FONT](/qb64wiki/index.php/FONT "FONT") [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("C:\Windows\Fonts\" + TTFont$ + ".ttf", height&, style$)  TextSize wide&, high&       'get the font or current screen mode's text block pixel size  [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (20, 100), [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(1) + [STR$](/qb64wiki/index.php/STR$ "STR$")(wide&) + " X" + [STR$](/qb64wiki/index.php/STR$ "STR$")(high&) + " " + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(2)  [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") TextSize (TextWidth&, TextHeight&) TextWidth& = _PRINTWIDTH("W")     'measure width of one font or text character TextHeight& = [_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT")         'can measure normal text block heights also [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Ted Weissgerber
**Note:** The SUB procedure does not need the font handle for font sizes after [\_FONT](/qb64wiki/index.php/FONT "FONT") enables one.
  




## See also


* [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH"), [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT")
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")
* [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING"), [\_FONT](/qb64wiki/index.php/FONT "FONT")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PRINTWIDTH&oldid=7932>"




## Navigation menu








### Search





















