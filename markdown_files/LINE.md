


LINE - QB64 Phoenix Edition Wiki








# LINE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The LINE statement is used in graphic [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes to create lines or boxes.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


LINE [STEP] [**(***column1***,** *row1***)**]**-**[STEP] **(***column2*, *row2***),** *color*[, [{B|BF}], *style%*]
  




## Parameters


* The [STEP](/qb64wiki/index.php/STEP "STEP") keyword make *column* and *row* coordinates relative to the previously coordinates set by any graphic statement.
* The optional parameters (*column1*, *row1*) set the line's starting point.
* The dash and second coordinate parameters (*column2*, *row2*) must be designated to complete the line or box.
* The [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") *color* attribute or [LONG](/qb64wiki/index.php/LONG "LONG") [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") 32 bit color value sets the drawing color. If omitted, the current [destination](/qb64wiki/index.php/DEST "DEST") page's [\_DEFAULTCOLOR](/qb64wiki/index.php/DEFAULTCOLOR "DEFAULTCOLOR") is used.
* Optional **B** keyword creates a rectangle (**b**ox) using the start and end coordinates as diagonal corners. **BF** creates a **b**ox **f**illed.
* The *style%* signed [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value sets a dotted pattern to draw the line or rectangle outline.


  




## Description


* Creates a colored line between the given coordinates. Can be drawn partially off screen.
* **B** creates a box outline with each side parallel to the program screen sides. **BF** creates a filled box.
* *style%* can be used to create a dotted pattern to draw the line.
	+ **B** can be used with a *style%* to draw the rectangle outline using the desired pattern.
	+ **BF** ignores the *style%* parameter. See examples 2, 3 and 4 below.
* The graphic cursor is set to the center of the program window on program start. Using the [STEP](/qb64wiki/index.php/STEP "STEP") keyword makes the coordinates relative to the current graphic cursor.
* LINE **can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only.**


  




## Examples


*Example 1:* Following one line with another by omitting the second line's first coordinate parameter bracket entirely:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  LINE (100, 100)-(200, 200), 10    'creates a line LINE -(400, 200), 12              'creates a second line from end of first  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Explanation:* The full equivalent LINE statement would be: **LINE(200, 200)-(400, 200), 12**
  

*Example 2:* Creating styled lines and boxes with the LINE statement. Different style values create different dashed line spacing.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  LINE (100, 100)-(300, 300), 10, , 63    'creates a styled line LINE (100, 100)-(300, 300), 12, B, 255  'creates styled box shape  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Explanation:* The first diagonal dashed green line bisects the red dashed square from Top Left to Bottom Right Corners.
  

*Example 3:* The *style* value sets each 16 pixel line section as the value's bits are set on or off:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN") 'required in QB64 only [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 5 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i% = 1 [TO](/qb64wiki/index.php/TO "TO") 2 ^ 15 'use exponential value instead of -32768     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15:[LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 5: [PRINT](/qb64wiki/index.php/PRINT "PRINT") i%;     LINE (10, 60)-(300, 60), 0 'erase previous lines     LINE (10, 60)-(300, 60), 12, , i%     tmp$ = ""     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") b% = 15 [TO](/qb64wiki/index.php/TO "TO") 0 [STEP](/qb64wiki/index.php/STEP "STEP") -1 'create binary text value showing bits on as █, off as space         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") i% [AND](/qb64wiki/index.php/AND "AND") 2 ^ b% [THEN](/qb64wiki/index.php/THEN "THEN") tmp$ = tmp$ + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(219) [ELSE](/qb64wiki/index.php/ELSE "ELSE") tmp$ = tmp$ + [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1)     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 12:[LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 20: [PRINT](/qb64wiki/index.php/PRINT "PRINT") tmp$;     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT](/qb64wiki/index.php/EXIT "EXIT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") 'any key exit     [_DELAY](/qb64wiki/index.php/DELAY "DELAY") .001 'set delay time as required [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |


*Explanation:* The *style* value's Most Significant Bit (MSB) is set to the left with LSB on right as 16 text blocks are set on or off.
  

*Example 4:* Using [binary code](/qb64wiki/index.php/%26B "&B") to design a style pattern:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  LINE (100, 100)-(300, 100), 10, , &B0000111100001111 '16-bits LINE (100, 110)-(300, 110), 11, , &B0011001100110011 LINE (100, 120)-(300, 120), 12, , &B0101010101010101 LINE (100, 130)-(300, 130), 13, , &B1000100010001000  ``` |
| --- |


*Explanation:* The binary pattern created with 0s and 1s using the [&B](/qb64wiki/index.php/%26B "&B") number prefix define the pattern to draw the colored lines.
  




## See also


* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [COLOR](/qb64wiki/index.php/COLOR "COLOR")
* [DRAW](/qb64wiki/index.php/DRAW "DRAW"), [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE"), [STEP](/qb64wiki/index.php/STEP "STEP")
* [PSET](/qb64wiki/index.php/PSET "PSET"), [PRESET](/qb64wiki/index.php/PRESET "PRESET")
* [AND](/qb64wiki/index.php/AND "AND"), [OR](/qb64wiki/index.php/OR "OR") (logical operators)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LINE&oldid=7898>"




## Navigation menu








### Search





















