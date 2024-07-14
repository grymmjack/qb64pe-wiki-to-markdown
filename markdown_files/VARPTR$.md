


VARPTR$ - QB64 Phoenix Edition Wiki








# VARPTR$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**VARPTR$** is a memory function that returns a [STRING](/qb64wiki/index.php/STRING "STRING") representation of a variable's memory address value for use in a [DRAW](/qb64wiki/index.php/DRAW "DRAW") or [PLAY](/qb64wiki/index.php/PLAY "PLAY") statement.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


string\_value$ = VARPTR$(*variable*)
  




* Can use any [string](/qb64wiki/index.php/STRING "STRING") or numerical variable reference **existing** in memory.
* If the parameter value is from an array it must be dimensioned already. Cannot use fixed length string arrays.
* When using **numerical** *variable* values in [DRAW](/qb64wiki/index.php/DRAW "DRAW") strings, use an = sign after the function letter. "TA=" + VARPTR$(*variable%*)
* Always use variable X as in "X" + VARPTR$(*string\_variable$*) to [DRAW](/qb64wiki/index.php/DRAW "DRAW") or [PLAY](/qb64wiki/index.php/PLAY "PLAY") another [STRING](/qb64wiki/index.php/STRING "STRING") value.
* DRAW relative Moves use a + or - before the equal sign. EX: DRAW "M+=" + VARPTR$(x%) + ",-=" + VARPTR$(y%)


  

*Example 1:* How VARPTR$ reads consecutive values from memory.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 2 [CLS](/qb64wiki/index.php/CLS "CLS") WIND$ = "r10 d7 l10 u7 br20"   'create draw string to be read by function ROW$ = "x"+VARPTR$(WIND$)+"x"+VARPTR$(WIND$)+"x"+VARPTR$(WIND$)+" x"+VARPTR$(WIND$)+"bl80 bd11" [LINE](/qb64wiki/index.php/LINE "LINE") (100, 50)-(200, 160), , B [DRAW](/qb64wiki/index.php/DRAW "DRAW") "bm 115,52" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") I = 1 [TO](/qb64wiki/index.php/TO "TO") 10     [DRAW](/qb64wiki/index.php/DRAW "DRAW") "x" + VARPTR$(ROW$) [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |


*NOTE:* **GWBasic** allows **semicolons** to be used in the ROW$ definition, but QBasic and **QB64** MUST use **+** concatenation.
  

*Example 2:* Using the function to change a Turn Angle value using DRAW.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12                            'Demonstrates how string DRAW angles are used with TA [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 360 [STEP](/qb64wiki/index.php/STEP "STEP") 30           'mark clock hours every 30 degrees   angle$ = [STR$](/qb64wiki/index.php/STR$ "STR$")(i)                 'change degree value i to a string   [PSET](/qb64wiki/index.php/PSET "PSET") (175, 250), 6               'clock center   [DRAW](/qb64wiki/index.php/DRAW "DRAW") "TA" + angle$ + "BU100"     'add string angle to Turn Angle and draw blind up   [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") [STEP](/qb64wiki/index.php/STEP "STEP")(0, 0), 5, 12         'place a circle at end of Up line   [DRAW](/qb64wiki/index.php/DRAW "DRAW") "P9, 12"   [_DELAY](/qb64wiki/index.php/DELAY "DELAY") .5 [NEXT](/qb64wiki/index.php/NEXT "NEXT")                             'Demonstrates how VARPTR$ is used with TA= [DO](/qb64wiki/index.php/DO "DO"): sec$ = [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 2)        'get current second value from time   degree = [VAL](/qb64wiki/index.php/VAL "VAL")(sec$) * -6          'use a negative value to Turn Angle clockwise   [PSET](/qb64wiki/index.php/PSET "PSET") (175, 250), 9               'clock center   [DRAW](/qb64wiki/index.php/DRAW "DRAW") "TA=" + VARPTR$(degree) + "U90"  'VARPTR$ value requires = in DRAW   [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30: [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 2) <> sec$  'loop until seconds value changes   [IF](/qb64wiki/index.php/IF "IF") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")   [PSET](/qb64wiki/index.php/PSET "PSET") (175, 250), 0   [DRAW](/qb64wiki/index.php/DRAW "DRAW") "TA=" + VARPTR$(degree) + "U90"  'erase previous second hand draw [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


*Explanation:* When the VARPTR$ value is used in DRAW, **=** MUST be used to pass the value to the draw! Negative Turn Angle values move clockwise and each second moves the hand 6 degrees. **TA** uses actual degree angles starting at 0 or noon.
  

*Example 3:* Comparing DRAW moves using VARPTR$ and [STR$](/qb64wiki/index.php/STR$ "STR$") values.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [PSET](/qb64wiki/index.php/PSET "PSET") (200, 200), 12 [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") [STEP](/qb64wiki/index.php/STEP "STEP")(0, 0), 5, 10 A = 100: B = 100 [DRAW](/qb64wiki/index.php/DRAW "DRAW") "M+=" + VARPTR$(A) + ",-=" + VARPTR$(B)  [PSET](/qb64wiki/index.php/PSET "PSET") (400, 400), 10 [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") [STEP](/qb64wiki/index.php/STEP "STEP")(0, 0), 5, 12 C = 100: D = -100 [DRAW](/qb64wiki/index.php/DRAW "DRAW") "M+" + [STR$](/qb64wiki/index.php/STR$ "STR$")(C) + "," + [STR$](/qb64wiki/index.php/STR$ "STR$")(D) 'must add + for positive relative moves [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Explanation:* A negative STR$ value will move the DRAW relatively where VARPTR$ won't without the sign before the equal.
  




## See also


* [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR"), [STR$](/qb64wiki/index.php/STR$ "STR$")
* [DRAW](/qb64wiki/index.php/DRAW "DRAW"), [PLAY](/qb64wiki/index.php/PLAY "PLAY")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=VARPTR$&oldid=7464>"




## Navigation menu








### Search





















