


PSET - QB64 Phoenix Edition Wiki








# PSET



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **PSET** grahics [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") statement sets a pixel to a coordinate with a default or designated color attribute.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


**PSET** [STEP]**(***column%*, *row%***)**[, *colorAttribute*]
  

*[Parameters](/qb64wiki/index.php/Parameters "Parameters"):*



* Can use [STEP](/qb64wiki/index.php/STEP "STEP") relative graphics coordinates from a previous graphic object.
* *Column* and *row* can be literal or variable [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") coordinates values which can be offscreen.
* If the *colorAttribute* is omitted, PSET will use the current [destination](/qb64wiki/index.php/DEST "DEST") page's \_DEFAULTCOLOR.


  

*Usage:*



* *Color attributes* are limited to the SCREEN mode used. Any color value other than 0 will be white in [SCREENs](/qb64wiki/index.php/SCREEN "SCREEN") 2 or 11.
* PSET can locate other graphics objects and color [DRAW](/qb64wiki/index.php/DRAW "DRAW") statements.
* The PSET action can be used in a graphics [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)") to produce an identical image on any background.
* The graphic cursor is set to the center of the program window on program start for [STEP](/qb64wiki/index.php/STEP "STEP") relative coordinates.
* **PSET can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only! (Or in any \_NEWIMAGE(x, y, 0) screens which are text only as well.)**


  

*Example:* Using PSET to locate and color a [DRAW](/qb64wiki/index.php/DRAW "DRAW") statement.





| ``` SCREEN 12 PSET(100, 100), 12 [DRAW](/qb64wiki/index.php/DRAW "DRAW") "U20 R20 D20 L20"  ``` |
| --- |


*Screen results:* A drawn box that is bright red.
  

*Example 2:* Magnifying a box portion of a Mandelbrot image with PSET





| ``` [DEFSTR](/qb64wiki/index.php/DEFSTR "DEFSTR") A-Z [DIM](/qb64wiki/index.php/DIM "DIM") red(15) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), green(15) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), blue(15) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") i [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 15: [READ](/qb64wiki/index.php/READ "READ") red(i): [NEXT](/qb64wiki/index.php/NEXT "NEXT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 15: [READ](/qb64wiki/index.php/READ "READ") green(i): [NEXT](/qb64wiki/index.php/NEXT "NEXT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 15: [READ](/qb64wiki/index.php/READ "READ") blue(i): [NEXT](/qb64wiki/index.php/NEXT "NEXT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 15: [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE") i, 65536 * blue(i) + 256& * green(i) + red(i): [NEXT](/qb64wiki/index.php/NEXT "NEXT") [DATA](/qb64wiki/index.php/DATA "DATA") 0,63,63,63,63,63,31, 0, 0,31,31,31,47,63,63,63 [DATA](/qb64wiki/index.php/DATA "DATA") 0, 0,15,31,47,63,63,63,63,31,15, 0, 0, 0, 0, 0 [DATA](/qb64wiki/index.php/DATA "DATA") 0, 0, 0, 0, 0, 0, 0, 0,31,63,63,63,63,63,42,21  [DIM](/qb64wiki/index.php/DIM "DIM") dmag [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), dlogmag [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") a [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), b [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), mag [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") [DIM](/qb64wiki/index.php/DIM "DIM") dx [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), dy [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") mx [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), my [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), mz [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  dmag = 16 mag = 1  a = -.75 b = 0 DO   [DIM](/qb64wiki/index.php/DIM "DIM") limitx [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), limit [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")   [DIM](/qb64wiki/index.php/DIM "DIM") inc [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), left [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), top [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")    limitx = 150 * ([LOG](/qb64wiki/index.php/LOG "LOG")(mag) + 1)   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") limitx > 32767 [THEN](/qb64wiki/index.php/THEN "THEN") limitx = 32767   limit = [INT](/qb64wiki/index.php/INT "INT")(limitx)   inc = .004 / mag   left = a - inc * 319   top = b + inc * 239   [CLS](/qb64wiki/index.php/CLS "CLS")    [DIM](/qb64wiki/index.php/DIM "DIM") yy [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), xx [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")   [DIM](/qb64wiki/index.php/DIM "DIM") x [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), y [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), z [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") yy = 0 [TO](/qb64wiki/index.php/TO "TO") 479     y = top - inc * yy     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") xx = 0 [TO](/qb64wiki/index.php/TO "TO") 639         x = left + inc * xx         z = mandel(x, y, limit)         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") z < limit [THEN](/qb64wiki/index.php/THEN "THEN") PSET (xx, yy), 1 + z [MOD](/qb64wiki/index.php/MOD "MOD") 15         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [THEN](/qb64wiki/index.php/THEN "THEN") [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")     [NEXT](/qb64wiki/index.php/NEXT "NEXT")   [NEXT](/qb64wiki/index.php/NEXT "NEXT")   mz = 0   [CALL](/qb64wiki/index.php/CALL "CALL") readmouse(mx, my, mz)   DO     dx = 319 \ dmag     dy = 239 \ dmag     [CALL](/qb64wiki/index.php/CALL "CALL") readmouse(mx, my, mz)     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") mz [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")     [CALL](/qb64wiki/index.php/CALL "CALL") rectangle(mx - dx, my - dy, mx + dx, my + dy)     [DIM](/qb64wiki/index.php/DIM "DIM") t [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")     t = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")     [WHILE](/qb64wiki/index.php/WHILE "WHILE") t = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")       key$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")       [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") key$         [CASE](/qb64wiki/index.php/CASE "CASE") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)           [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")         [CASE](/qb64wiki/index.php/CASE "CASE") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(72)           dmag = dmag \ 2           [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") dmag < 2 [THEN](/qb64wiki/index.php/THEN "THEN") dmag = 2         [CASE](/qb64wiki/index.php/CASE "CASE") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(80)           dmag = dmag * 2           [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") dmag > 128 [THEN](/qb64wiki/index.php/THEN "THEN") dmag = 128       [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")     [WEND](/qb64wiki/index.php/WEND "WEND")     [CALL](/qb64wiki/index.php/CALL "CALL") rectangle(mx - dx, my - dy, mx + dx, my + dy)   [LOOP](/qb64wiki/index.php/LOOP "LOOP")   a = a + inc * (mx - 319): b = b - inc * (my - 239)   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") (mz = 1) [THEN](/qb64wiki/index.php/THEN "THEN") mag = dmag * mag [ELSE](/qb64wiki/index.php/ELSE "ELSE") mag = mag / dmag   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") (mag < 1) [THEN](/qb64wiki/index.php/THEN "THEN") mag = 1 [LOOP](/qb64wiki/index.php/LOOP "LOOP")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") mandel% (x [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), y [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), limit [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"))   [DIM](/qb64wiki/index.php/DIM "DIM") a [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), b [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), t [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")   [DIM](/qb64wiki/index.php/DIM "DIM") n [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")   n = 0: a = 0: b = 0   DO     t = a * a - b * b + x     b = 2 * a * b + y: a = t     n = n + 1   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") a * a + b * b > 4 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") n > limit   mandel = n [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  [SUB](/qb64wiki/index.php/SUB "SUB") readmouse (x [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), y [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), z [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")) z=0 DO if [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(1) [THEN](/qb64wiki/index.php/THEN "THEN") z = z [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") 1 if [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(2) [THEN](/qb64wiki/index.php/THEN "THEN") z = z [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") 2 if [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(3) [THEN](/qb64wiki/index.php/THEN "THEN") z = z [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") 4 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")=0 x=[_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX") y=[_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") rectangle (x1 [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), y1 [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), x2 [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), y2 [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"))   [DIM](/qb64wiki/index.php/DIM "DIM") i [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), j [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = x1 [TO](/qb64wiki/index.php/TO "TO") x2     j = [POINT](/qb64wiki/index.php/POINT "POINT")(i, y1)     PSET (i, y1), j [XOR](/qb64wiki/index.php/XOR_(boolean) "XOR (boolean)") 15     j = [POINT](/qb64wiki/index.php/POINT "POINT")(i, y2)     PSET (i, y2), j [XOR](/qb64wiki/index.php/XOR_(boolean) "XOR (boolean)") 15   [NEXT](/qb64wiki/index.php/NEXT "NEXT")   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = y1 [TO](/qb64wiki/index.php/TO "TO") y2     j = [POINT](/qb64wiki/index.php/POINT "POINT")(x1, i)     PSET (x1, i), j [XOR](/qb64wiki/index.php/XOR_(boolean) "XOR (boolean)") 15     j = [POINT](/qb64wiki/index.php/POINT "POINT")(x2, i)     PSET (x2, i), j [XOR](/qb64wiki/index.php/XOR_(boolean) "XOR (boolean)") 15   [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Codeguy
*Notes:* Left click, to zoom in on the rectangle. Right click, to zoom out. Up arrow makes the rectangle bigger and down arrow makes the rectangle smaller.
  




## See also


* [PRESET](/qb64wiki/index.php/PRESET "PRESET"), [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE"), [LINE](/qb64wiki/index.php/LINE "LINE")
* [COLOR](/qb64wiki/index.php/COLOR "COLOR"), [POINT](/qb64wiki/index.php/POINT "POINT")
* [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PSET&oldid=8057>"




## Navigation menu








### Search





















