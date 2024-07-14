


PAINT - QB64 Phoenix Edition Wiki








# PAINT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The PAINT statement is used to fill a delimited area in a graphic screen mode with color.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


PAINT [**STEP**] (*column%*, *row%*), *fillColor*[, *borderColor%*]
  




## Parameters


* Can use the [STEP](/qb64wiki/index.php/STEP "STEP") keyword for relative coordinate placements. See example 1 below.
* *fillColor* is an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [LONG](/qb64wiki/index.php/LONG "LONG") 32-bit value to paint the inside of an object. Colors are limited to the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode used.
* Optional [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [LONG](/qb64wiki/index.php/LONG "LONG") 32-bit *borderColor%* is the color of the border of the shape to be filled when this is different from the fill color.
* *fillColor* can be a string made up of a sequence of [CHR$](/qb64wiki/index.php/CHR$ "CHR$") values, each representing a tiling pattern to fill the shape. See Example 3 below.


  




## Description


* Graphic *column%* and *row%* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") pixel coordinates should be inside of a fully closed "shape", whether it's a rectangle, circle or custom-drawn shape using [DRAW](/qb64wiki/index.php/DRAW "DRAW").
* If the coordinates passed to the PAINT statement are on a pixel that matches the border colors, no filling will occur.
* If the shape's border isn't continuous, the "paint" will "leak".
* If the shape is not totally closed, every color except the border color may be painted over.
* [DRAW](/qb64wiki/index.php/DRAW "DRAW") shapes can be filled using the string "P *fillColor*, *borderColor*". Use a "B" blind move to offset from the shape's border.


  




## Examples


*Example 1:* Painting a [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") immediately after it is drawn using [STEP](/qb64wiki/index.php/STEP "STEP")(0, 0) to paint from the circle's center point.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 x = 200: y = 200 [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (x, y), 100, 10 PAINT [STEP](/qb64wiki/index.php/STEP "STEP")(0, 0), 2, 10  ``` |
| --- |


*Results:* A circle located at x and y with a bright green border filled in dark green. The last coordinate used was the circle's center point and PAINT used it also with the [STEP](/qb64wiki/index.php/STEP "STEP") relative coordinates being zero.
  

*Example 2:* Routine to check a [DRAW](/qb64wiki/index.php/DRAW "DRAW") string to make sure that the drawn shape is fully closed so that a PAINT does not "leak".





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 drw$ = "C15S20R9D4R6U3R3D3R7U5H3U2R9D3G2D6F1D3F5L10D1G1L4H2L7G2L3H2L3U8L2U5R1BF4"  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(drw$)   tmp$ = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(drw$, i, 1))   check = 1   [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") tmp$     [CASE](/qb64wiki/index.php/CASE "CASE") "U": ver = -1: hor = 0     [CASE](/qb64wiki/index.php/CASE "CASE") "D": ver = 1: hor = 0     [CASE](/qb64wiki/index.php/CASE "CASE") "E": ver = -1: hor = 1     [CASE](/qb64wiki/index.php/CASE "CASE") "F": ver = 1: hor = 1     [CASE](/qb64wiki/index.php/CASE "CASE") "G": ver = 1: hor = -1     [CASE](/qb64wiki/index.php/CASE "CASE") "H": ver = -1: hor = -1     [CASE](/qb64wiki/index.php/CASE "CASE") "L": ver = 0: hor = -1     [CASE](/qb64wiki/index.php/CASE "CASE") "R": ver = 0: hor = 1     [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE"): check = 0   [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") check [THEN](/qb64wiki/index.php/THEN "THEN")     snum$ = ""     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") j = i + 1 [TO](/qb64wiki/index.php/TO "TO") i + 4 'set for up to 4 digits and spaces       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") j > [LEN](/qb64wiki/index.php/LEN "LEN")(drw$) [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT](/qb64wiki/index.php/EXIT "EXIT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")       n$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(drw$, j, 1)       num = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(n$)       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") (num > 47 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") num < 58) [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") num = 32 [THEN](/qb64wiki/index.php/THEN "THEN")         snum$ = snum$ + n$       [ELSE](/qb64wiki/index.php/ELSE "ELSE"): [EXIT](/qb64wiki/index.php/EXIT "EXIT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")       [END IF](/qb64wiki/index.php/END_IF "END IF")     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     vertical = vertical + (ver * [VAL](/qb64wiki/index.php/VAL "VAL")(snum$))     horizont = horizont + (hor * [VAL](/qb64wiki/index.php/VAL "VAL")(snum$))   [END IF](/qb64wiki/index.php/END_IF "END IF")   [PRINT](/qb64wiki/index.php/PRINT "PRINT") tmp$, horizont, vertical   '[SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PSET](/qb64wiki/index.php/PSET "PSET") (300, 300): [DRAW](/qb64wiki/index.php/DRAW "DRAW") drw$  ``` |
| --- |


*Explanation:* If the [DRAW](/qb64wiki/index.php/DRAW "DRAW") string is fully closed, the end values should each be 0. In the example, the proper result should be 4, 4 as there is a BF4 offset for PAINT which cannot be on a border. The result is 4, 5 because the shape is not completely closed.
  

*Example 3:* Tiling using PAINT to create a red brick pattern inside a yellow border:





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") Row$(1 [TO](/qb64wiki/index.php/TO "TO") 8) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12     'make red-brick wall     Row$(1) = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")FE) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")FE)     Row$(2) = Row$(1)     Row$(3) = Row$(1)     Row$(4) = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")0)     Row$(5) = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")EF) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([&H](/qb64wiki/index.php/%26H "&H")EF)     Row$(6) = Row$(5)     Row$(7) = Row$(5)     Row$(8) = Row$(4)     Tile$ = Row$(1) + Row$(2) + Row$(3) + Row$(4) + Row$(5) + Row$(6) + Row$(7) + Row$(8)      [LINE](/qb64wiki/index.php/LINE "LINE") (59, 124)-(581, 336), 14, B 'yellow box border to paint inside     PAINT (320, 240), Tile$, 14 'paints brick tiles within yellow border  ``` |
| --- |


  

*Example 4:* Generating a tiling pattern for PAINT from [DATA](/qb64wiki/index.php/DATA "DATA") statements:





| ``` ptndata: [DATA](/qb64wiki/index.php/DATA "DATA") "c4444444" [DATA](/qb64wiki/index.php/DATA "DATA") "c4444444" [DATA](/qb64wiki/index.php/DATA "DATA") "cccccccc" [DATA](/qb64wiki/index.php/DATA "DATA") "444c4444" [DATA](/qb64wiki/index.php/DATA "DATA") "444c4444" [DATA](/qb64wiki/index.php/DATA "DATA") "444c4444" [DATA](/qb64wiki/index.php/DATA "DATA") "cccccccc" [DATA](/qb64wiki/index.php/DATA "DATA") "c4444444" [DATA](/qb64wiki/index.php/DATA "DATA") ---  [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") ptndata: ptn$ = loadpattern$  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 7 [DRAW](/qb64wiki/index.php/DRAW "DRAW") "c15l15f10g10r30g10f10l50u80r100m160,100" PAINT (160, 90), ptn$, 15  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") loadpattern$     [DIM](/qb64wiki/index.php/DIM "DIM") quad(0 TO 3) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")     res$ = ""     [DO](/qb64wiki/index.php/DO "DO")         [READ](/qb64wiki/index.php/READ "READ") row$         [IF](/qb64wiki/index.php/IF "IF") [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(row$, 3) = "---" [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT](/qb64wiki/index.php/EXIT "EXIT") [DO](/qb64wiki/index.php/DO "DO")         [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") 7             pixel = [VAL](/qb64wiki/index.php/VAL "VAL")("&h" + [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(row$, x + 1, 1))             [FOR](/qb64wiki/index.php/FOR "FOR") bit = 0 [TO](/qb64wiki/index.php/TO "TO") 3                 [IF](/qb64wiki/index.php/IF "IF") pixel [AND](/qb64wiki/index.php/AND "AND") 2 ^ bit [THEN](/qb64wiki/index.php/THEN "THEN")                     quad(bit) = quad(bit) [OR](/qb64wiki/index.php/OR "OR") (2 ^ (7 - x))                 [END](/qb64wiki/index.php/END "END") [IF](/qb64wiki/index.php/IF "IF")             [NEXT](/qb64wiki/index.php/NEXT "NEXT")         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         [FOR](/qb64wiki/index.php/FOR "FOR") i = 0 [TO](/qb64wiki/index.php/TO "TO") 3             res$ = res$ + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(quad(i))             quad(i) = 0         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [LOOP](/qb64wiki/index.php/LOOP "LOOP")     loadpattern$ = res$ [END](/qb64wiki/index.php/END "END") [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")  ``` |
| --- |


*Code provided by collaborator <https://github.com/NEONTEC75>*
  




## See also


* [PSET](/qb64wiki/index.php/PSET "PSET"), [PRESET](/qb64wiki/index.php/PRESET "PRESET")
* [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE"), [LINE](/qb64wiki/index.php/LINE "LINE"), [DRAW](/qb64wiki/index.php/DRAW "DRAW")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [CHR$](/qb64wiki/index.php/CHR$ "CHR$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PAINT&oldid=8158>"




## Navigation menu








### Search





















