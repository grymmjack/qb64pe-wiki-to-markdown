


\_MOUSEY - QB64 Phoenix Edition Wiki








# \_MOUSEY



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MOUSEY function returns the current vertical (row) mouse cursor position when read after [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*pixelRow%* = \_MOUSEY
  




## Description


* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 returns the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") vertical text row position (from build 20170817/62 onward); older versions return a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") vertical text row position. Use [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") variables to avoid floating decimal returns.
* Graphic screen modes 1, 2 and 7 to 13 and [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") 32 bit return the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") pixel columns.
* To calculate text rows in graphic modes divide the return by 16 or the [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT") of [\_FONT](/qb64wiki/index.php/FONT "FONT") characters.
* [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") must be used to detect any changes in the mouse position and is **required** for any coordinate returns.


### QBasic/QuickBASIC


* In [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0, QBasic's [ABSOLUTE](/qb64wiki/index.php/CALL_ABSOLUTE "CALL ABSOLUTE") returned graphic coordinates. QB64 mouse functions return the text coordinates.


  




## Examples


*Example:* Highlighting a row of text in Screen 0.





| ``` minX = 20: maxX = 60: minY = 10: maxY = 24 selection = 0 'the screen Y coordinate of the previously highlighted item [FOR](/qb64wiki/index.php/FOR "FOR") i% = 1 [TO](/qb64wiki/index.php/TO "TO") 25: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") i%, 40: [PRINT](/qb64wiki/index.php/PRINT "PRINT") i%;: [NEXT](/qb64wiki/index.php/NEXT "NEXT") [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 100   [IF](/qb64wiki/index.php/IF "IF") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") [THEN](/qb64wiki/index.php/THEN "THEN")     'Un-highlight any selected row     [IF](/qb64wiki/index.php/IF "IF") selection [THEN](/qb64wiki/index.php/THEN "THEN") selectRow selection, minX, maxX, 0     x = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")     y = _MOUSEY     [IF](/qb64wiki/index.php/IF "IF") x >= minX [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x <= maxX [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y >= minY [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y <= maxY [THEN](/qb64wiki/index.php/THEN "THEN")       selection = y     [ELSE](/qb64wiki/index.php/ELSE "ELSE")       selection = 0     [END IF](/qb64wiki/index.php/END_IF "END IF")     'Highlight any selected row     [IF](/qb64wiki/index.php/IF "IF") selection [THEN](/qb64wiki/index.php/THEN "THEN") SelectRow selection, minX, maxX, 2     [IF](/qb64wiki/index.php/IF "IF") [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(1) [THEN](/qb64wiki/index.php/THEN "THEN") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") x, y, selection   [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  [SUB](/qb64wiki/index.php/SUB "SUB") SelectRow (y, x1, x2, col) [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [&H](/qb64wiki/index.php/%26H "&H")B800 addr& = (x1 - 1 + (y - 1) * [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")) * 2 + 1 [FOR](/qb64wiki/index.php/FOR "FOR") x = x1 [TO](/qb64wiki/index.php/TO "TO") x2   oldCol = [PEEK](/qb64wiki/index.php/PEEK "PEEK")(addr&) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [&B](/qb64wiki/index.php/%26B "&B")10001111   ' Mask foreground color and blink bit   [POKE](/qb64wiki/index.php/POKE "POKE") addr&, oldCol [OR](/qb64wiki/index.php/OR "OR") ((col [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [&B](/qb64wiki/index.php/%26B "&B")111) * [&B](/qb64wiki/index.php/%26B "&B")10000) ' Apply background color   addr& = addr& + 2 [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


  




## See also


* [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON"), [\_MOUSEWHEEL](/qb64wiki/index.php/MOUSEWHEEL "MOUSEWHEEL")
* [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT"), [\_MOUSEMOVE](/qb64wiki/index.php/MOUSEMOVE "MOUSEMOVE")
* [\_MOUSESHOW](/qb64wiki/index.php/MOUSESHOW "MOUSESHOW"), [\_MOUSEHIDE](/qb64wiki/index.php/MOUSEHIDE "MOUSEHIDE")
* [\_MOUSEMOVEMENTX](/qb64wiki/index.php/MOUSEMOVEMENTX "MOUSEMOVEMENTX"), [\_MOUSEMOVEMENTY](/qb64wiki/index.php/MOUSEMOVEMENTY "MOUSEMOVEMENTY")
* [Controller Devices](/qb64wiki/index.php/Controller_Devices "Controller Devices")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MOUSEY&oldid=7625>"




## Navigation menu








### Search





















