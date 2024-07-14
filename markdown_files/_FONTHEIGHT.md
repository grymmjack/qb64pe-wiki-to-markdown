


\_FONTHEIGHT - QB64 Phoenix Edition Wiki








# \_FONTHEIGHT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_FONTHEIGHT function returns the font height of a font handle created by [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*pixelHeight%* = \_FONTHEIGHT[(*fontHandle&*)]
  




## Description


* Returns the height of the last font used if a handle is not designated.
* If no font is set it returns the current screen mode's text block height.


  




## Examples


*Example:* Finding the [font](/qb64wiki/index.php/FONT "FONT") or text block size of printed [string](/qb64wiki/index.php/STRING "STRING") characters in graphic [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes.





| ``` [DO](/qb64wiki/index.php/DO "DO")     [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter Screen mode 1, 2 or 7 to 13 or 256, 32 for _NEWIMAGE: ", scr$     mode% = [VAL](/qb64wiki/index.php/VAL "VAL")(scr$) [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") mode% > 0 [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") mode%     [CASE](/qb64wiki/index.php/CASE "CASE") 1, 2, 7 [TO](/qb64wiki/index.php/TO "TO") 13: [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode%     [CASE](/qb64wiki/index.php/CASE "CASE") 256, 32: [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, mode%)     [CASE](/qb64wiki/index.php/CASE "CASE") [ELSE](/qb64wiki/index.php/ELSE "ELSE"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Invalid mode selected!": [END](/qb64wiki/index.php/END "END") [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")  [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter first name of TTF font to use or hit enter for text block size: ", TTFont$ [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")(TTFont$) [THEN](/qb64wiki/index.php/THEN "THEN") [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter font height: ", hi$ height& = [VAL](/qb64wiki/index.php/VAL "VAL")(hi$) [IF](/qb64wiki/index.php/IF "IF") height& > 0 [THEN](/qb64wiki/index.php/THEN "THEN")     fnt& = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("C:\Windows\Fonts\" + TTFont$ + ".ttf", height&, style$)     [IF](/qb64wiki/index.php/IF "IF") fnt& <= 0 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Invalid Font handle!": [END](/qb64wiki/index.php/END "END")     [_FONT](/qb64wiki/index.php/FONT "FONT") fnt& [END IF](/qb64wiki/index.php/END_IF "END IF")  TextSize wide&, high& 'get the font or current screen mode's text block pixel size  [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (20, 100), "Block size = " + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(1) + [STR$](/qb64wiki/index.php/STR$ "STR$")(wide&) + " X" + [STR$](/qb64wiki/index.php/STR$ "STR$")(high&) + " " + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(2)  [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") TextSize (TextWidth&, TextHeight&)     TextWidth& = [_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH")("W") 'measure width of one font or text character     TextHeight& = _FONTHEIGHT 'can measure normal text block heights also [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1145)
* [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH"), [\_FONT](/qb64wiki/index.php/FONT "FONT")
* [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH"), [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics") (Demo)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FONTHEIGHT&oldid=8893>"




## Navigation menu








### Search





















