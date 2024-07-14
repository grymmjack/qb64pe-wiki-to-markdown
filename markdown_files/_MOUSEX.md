


\_MOUSEX - QB64 Phoenix Edition Wiki








# \_MOUSEX



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MOUSEX function returns the current horizontal (column) mouse cursor position when read after [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*pixelColumn%* = \_MOUSEX
  




## Description


* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 returns the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") horizontal text column position (from build 20170817/62 onward); older versions return a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") horizontal text column position. Use [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") variables to avoid floating decimal returns.
* Graphic screen modes 1, 2 and 7 to 13 and [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") 32 bit return the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") pixel columns.
* To calculate text columns in graphic modes, divide the return by 8 or the [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH") of [\_FONT](/qb64wiki/index.php/FONT "FONT") characters.
* [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") must be used to detect any changes in the mouse position and is **required** for any coordinate returns.


### QBasic/QuickBASIC


* In [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0, QBasic's [ABSOLUTE](/qb64wiki/index.php/CALL_ABSOLUTE "CALL ABSOLUTE") returned graphic coordinates. QB64 mouse functions return the text coordinates.


  




## Examples


*Example:* A simple mouse drawing board using \_MOUSEX and [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY") coordinate values.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [LINE](/qb64wiki/index.php/LINE "LINE") (99, 9)-(601, 401), 7, BF [LINE](/qb64wiki/index.php/LINE "LINE") (101, 11)-(599, 399), 8, BF tm$ = " Column = ###  Row = ###  Button1 = ##  Button2 = ##  Button3 = ##" [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 29, 20: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "LeftButton = draw - RightButton = Erase"; [DO](/qb64wiki/index.php/DO "DO"): K$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")   [DO](/qb64wiki/index.php/DO "DO") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")     X = _MOUSEX: Y = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")     [IF](/qb64wiki/index.php/IF "IF") X > 100 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") X < 600 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") PX > 100 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") PX < 600 [THEN](/qb64wiki/index.php/THEN "THEN")       [IF](/qb64wiki/index.php/IF "IF") Y > 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Y < 400 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") PY > 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") PY < 400 [THEN](/qb64wiki/index.php/THEN "THEN")         [IF](/qb64wiki/index.php/IF "IF") [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(1) [THEN](/qb64wiki/index.php/THEN "THEN") [LINE](/qb64wiki/index.php/LINE "LINE") (PX, PY)-(X, Y), 15         [IF](/qb64wiki/index.php/IF "IF") [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(2) [THEN](/qb64wiki/index.php/THEN "THEN") [LINE](/qb64wiki/index.php/LINE "LINE") (101, 11)-(599, 399), 8, BF       [END IF](/qb64wiki/index.php/END_IF "END IF")     [END IF](/qb64wiki/index.php/END_IF "END IF")     PX = X: PY = Y     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 28, 10: [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") tm$; X; Y; [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(1); [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(2); [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(3)   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") K$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")  ``` |
| --- |


  




## See also


* [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")
* [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON"), [\_MOUSEWHEEL](/qb64wiki/index.php/MOUSEWHEEL "MOUSEWHEEL")
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





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MOUSEX&oldid=7624>"




## Navigation menu








### Search





















