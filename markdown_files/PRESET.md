


PRESET - QB64 Phoenix Edition Wiki








# PRESET



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **PRESET** graphic [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") statement turns a pixel at a coordinate to the background color or a designated color attribute.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


**PRESET** [STEP]**(***column%*, *row%***)**[, colorAttribute]
  

*[Parameters](/qb64wiki/index.php/Parameters "Parameters"):*



* Can use [STEP](/qb64wiki/index.php/STEP "STEP") when relative graphics coordinates are required.
* *column* and *row* coordinates can be literal ot variable [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values which can be offscreen.
* If the *colorAttribute* is omitted, PRESET will use the current [destination](/qb64wiki/index.php/DEST "DEST") page's [\_BACKGROUNDCOLOR](/qb64wiki/index.php/BACKGROUNDCOLOR "BACKGROUNDCOLOR").


  

*Usage:*



* Color attributes are limited to those available in the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode used. [PSET](/qb64wiki/index.php/PSET "PSET") can be used to adopt previously used colors.
* Any color value other than 0 will be white in monochrome [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes 2 and 11 where the [COLOR](/qb64wiki/index.php/COLOR "COLOR") statement cannot be used.
* PRESET can invisibly locate other graphics objects like [CIRCLEs](/qb64wiki/index.php/CIRCLE "CIRCLE") and add color to subsequent graphic objects and [DRAW](/qb64wiki/index.php/DRAW "DRAW") when used.
* The PRESET action can be used in a graphics [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)") to produce a color inverted image on any background. See Example 2.
* The graphic cursor is set to the center of the program window on program start for [STEP](/qb64wiki/index.php/STEP "STEP") relative coordinates.
* **PRESET can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only!**


  

*Example 1:* Using PRESET to locate a [DRAW](/qb64wiki/index.php/DRAW "DRAW") statement that draws a box that is bright red.





| ``` SCREEN 12 PRESET(100, 100) [DRAW](/qb64wiki/index.php/DRAW "DRAW") "C12 U20 R20 D20 L20"  ``` |
| --- |


*Explanation:* The [DRAW](/qb64wiki/index.php/DRAW "DRAW") string required a color designation as PRESET defaulted to the black background color.
  



*Example 2:* Displays the flags of countries that use simple horizontal or vertical color blocks with a highlighted arrow key menu.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") c$(21), x$(21), gg%(477)  ARRAY SETUP SELECTION TERMINATE  [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") ARRAY c$(1) = "Armenia H040914" c$(2) = "Austria H041504" c$(3) = "Belgium V001404" c$(4) = "Bulgaria H150204" c$(5) = "Chad V011404" c$(6) = "C“te D'Ivoire V061502" c$(7) = "Estonia H090015" c$(8) = "France V011504" c$(9) = "Germany H000414" c$(10) = "Hungary H041502" c$(11) = "Ireland V021506" c$(12) = "Italy V021504" c$(13) = "Lithuania H140204" c$(14) = "Luxembourg H041509" c$(15) = "Mali V021404" c$(16) = "Netherlands H041501" c$(17) = "Nigeria V021502" c$(18) = "Romania V091404" c$(19) = "Russia H150104" c$(20) = "Sierra Leone H021509" c$(21) = "Yemen H041500" [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") DISPLAY.FLAG (calc%) f% = [VAL](/qb64wiki/index.php/VAL "VAL")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(x$(calc%), 2, 2)) s% = [VAL](/qb64wiki/index.php/VAL "VAL")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(x$(calc%), 4, 2)) t% = [VAL](/qb64wiki/index.php/VAL "VAL")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(x$(calc%), 6, 2))  [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(x$(calc%), 1) = "V" [THEN](/qb64wiki/index.php/THEN "THEN")   [LINE](/qb64wiki/index.php/LINE "LINE") (120, 225)-(253, 465), f%, BF   [LINE](/qb64wiki/index.php/LINE "LINE") (254, 225)-(385, 465), s%, BF   [LINE](/qb64wiki/index.php/LINE "LINE") (386, 225)-(519, 465), t%, BF [END IF](/qb64wiki/index.php/END_IF "END IF")  [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(x$(calc%), 1) = "H" [THEN](/qb64wiki/index.php/THEN "THEN")   [LINE](/qb64wiki/index.php/LINE "LINE") (120, 225)-(519, 305), f%, BF   [LINE](/qb64wiki/index.php/LINE "LINE") (120, 306)-(519, 386), s%, BF   [LINE](/qb64wiki/index.php/LINE "LINE") (120, 387)-(519, 465), t%, BF [END IF](/qb64wiki/index.php/END_IF "END IF") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") SELECTION 'menu selection using arrow keys x% = 2: y% = 4  DO   [WHILE](/qb64wiki/index.php/WHILE "WHILE") (x% <> prevx% [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") y% <> prevy%) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") k$ <> [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)     k$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")     x% = x% + (k$ = ([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "K") [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x% > 1) + [ABS](/qb64wiki/index.php/ABS "ABS")(k$ = ([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "M") [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x% < 3)     y% = y% + (k$ = ([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "H") [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y% > 1) + [ABS](/qb64wiki/index.php/ABS "ABS")(k$ = ([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "P") [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y% < 7)     calc% = (x% - 1) * 7 + y%: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 14, 18: [PRINT](/qb64wiki/index.php/PRINT "PRINT") c$(calc%); [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(10)     x1% = 140 + (x% - 1) * 128     x2% = x1% + [LEN](/qb64wiki/index.php/LEN "LEN")(c$(calc%)) * 8 + 7     y1% = 48 + y% * 16     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x1% <> prevx1% [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") y1% <> prevy1% [THEN](/qb64wiki/index.php/THEN "THEN")       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") g% [THEN](/qb64wiki/index.php/THEN "THEN") [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")(prevx1%, prevy1%), gg%(), [PSET](/qb64wiki/index.php/PSET "PSET")       [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)")(x1%, y1%)-(x2%, y1% + 16), gg%(): g% = 1       [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")(x1%, y1%), gg%(), PRESET       prevx1% = x1%: prevx2% = x2%: prevy1% = y1%       DISPLAY.FLAG calc%     [END IF](/qb64wiki/index.php/END_IF "END IF")   [WEND](/qb64wiki/index.php/WEND "WEND") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") k$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") SETUP [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 6 c% = 1  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") x% = 11 [TO](/qb64wiki/index.php/TO "TO") 50 [STEP](/qb64wiki/index.php/STEP "STEP") 16   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y% = 1 [TO](/qb64wiki/index.php/TO "TO") 7     x$(c%) = [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(c$(c%), 7)     c$(c%) = [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$")([LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(c$(c%), [LEN](/qb64wiki/index.php/LEN "LEN")(c$(c%)) - 7))     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") y% + 4, x% + 8: [PRINT](/qb64wiki/index.php/PRINT "PRINT") c$(c%)     c% = c% + 1 [NEXT](/qb64wiki/index.php/NEXT "NEXT") y%, x%  [COLOR](/qb64wiki/index.php/COLOR "COLOR") 11: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 3, 20: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Use the Cursor Keys to Select a Country:" [LINE](/qb64wiki/index.php/LINE "LINE") (119, 224)-(520, 466), 7, B [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") TERMINATE [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") c% = 1 [TO](/qb64wiki/index.php/TO "TO") 219   [LINE](/qb64wiki/index.php/LINE "LINE") (116 + c%, 29 + c%)-(523 - c%, 469 - c%), 0, B [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by AlGoreIthm
*Explanation:* Using the [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)") PRESET action highlights the menu selection in graphic screen modes by returning a negative image.
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1157)
* [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)")
* [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE"), [LINE](/qb64wiki/index.php/LINE "LINE"), [PSET](/qb64wiki/index.php/PSET "PSET")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PRESET&oldid=8896>"




## Navigation menu








### Search





















