


TAN - QB64 Phoenix Edition Wiki








# TAN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The TAN function returns the ratio of [SINe](/qb64wiki/index.php/SIN "SIN") to [COSine](/qb64wiki/index.php/COS "COS") or tangent value of an angle measured in radians.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


tangent! = **TAN(***radian\_angle!***)**
  




## Parameters


* The *radian\_angle* must be measured in radians.


  




## Description


* To convert from degrees to radians, multiply degrees \* π/180.
* TANGENT is the gradient or slope of the circle or arc at [SIN](/qb64wiki/index.php/SIN "SIN")(θ) / [COS](/qb64wiki/index.php/COS "COS")(θ). Do not use division when the [COS](/qb64wiki/index.php/COS "COS") = 0 to avoid [errors](/qb64wiki/index.php/ERROR_Codes "ERROR Codes").


  

*Example:* Spiraling text using the [SIN](/qb64wiki/index.php/SIN "SIN") and TAN functions.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") text [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") text$ = "S P I R A L" [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") word(1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(text$) * 8, 1 [TO](/qb64wiki/index.php/TO "TO") 16)  [CALL](/qb64wiki/index.php/CALL "CALL") analyse [CLS](/qb64wiki/index.php/CLS "CLS") [CALL](/qb64wiki/index.php/CALL "CALL") redraw  [SUB](/qb64wiki/index.php/SUB "SUB") analyse [CLS](/qb64wiki/index.php/CLS "CLS") [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 2: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") text$ [DIM](/qb64wiki/index.php/DIM "DIM") px [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), py [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), cnt [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), ltrcnt [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") px = 1: py = 1 DO   word(px, py) = [POINT](/qb64wiki/index.php/POINT "POINT")(px, py)   [PSET](/qb64wiki/index.php/PSET "PSET") (px, py), 1   px = px + 1   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") px = [LEN](/qb64wiki/index.php/LEN "LEN")(text$) * 8 [THEN](/qb64wiki/index.php/THEN "THEN")     px = 1     py = py + 1   [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") py = 16 [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") redraw [CLS](/qb64wiki/index.php/CLS "CLS") [DIM](/qb64wiki/index.php/DIM "DIM") row [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), cnt [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), cstart [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), cend [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") [DIM](/qb64wiki/index.php/DIM "DIM") xrot [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), yrot [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), SCALE [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), pan [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") cstart = 0: cend = 6.2 xrot = 6: yrot = 6: SCALE = 3: pan = 30 [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C8, 1: [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C9, 10: [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C9, 10: [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C9, 60 DO   row = 2   DO     DO       [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = cend [TO](/qb64wiki/index.php/TO "TO") cstart [STEP](/qb64wiki/index.php/STEP "STEP") -.03         x = (SCALE * 60 - (row * xrot / 4)) * TAN([COS](/qb64wiki/index.php/COS "COS")(i))         y = [SIN](/qb64wiki/index.php/SIN "SIN")(SCALE * 60 - (row * yrot)) * TAN([SIN](/qb64wiki/index.php/SIN "SIN")(i)) * pan         cnt = cnt + 1         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") word(cnt, row) > 0 [THEN](/qb64wiki/index.php/THEN "THEN")           [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (x + 320, y + 220), SCALE + 1, 1              'circled letters           '[LINE](/qb64wiki/index.php/LINE "LINE") (x + 320, y + 220)-[STEP](/qb64wiki/index.php/STEP "STEP")(12, 12), 1, BF  'boxed letters         [END IF](/qb64wiki/index.php/END_IF "END IF")         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") cnt = [LEN](/qb64wiki/index.php/LEN "LEN")(text$) * 8 [THEN](/qb64wiki/index.php/THEN "THEN") cnt = 0: [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")       [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [LOOP](/qb64wiki/index.php/LOOP "LOOP")     row = row + 1   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") row = 16   cend = cend + .1   cstart = cstart + .1   now! = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")   DO     newnow! = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") newnow! - now! >= .15   [LINE](/qb64wiki/index.php/LINE "LINE") (1, 100)-(639, 280), 0, BF [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Unseen Machine
  




## See also


* [\_PI](/qb64wiki/index.php/PI "PI")
* [SIN](/qb64wiki/index.php/SIN "SIN"), [COS](/qb64wiki/index.php/COS "COS")
* [ATN](/qb64wiki/index.php/ATN "ATN")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")
* [Derived Mathematical Functions](/qb64wiki/index.php/Mathematical_Operations#Derived_Mathematical_Functions "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=TAN&oldid=8070>"




## Navigation menu








### Search





















