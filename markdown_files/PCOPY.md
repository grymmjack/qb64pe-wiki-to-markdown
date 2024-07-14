


PCOPY - QB64 Phoenix Edition Wiki








# PCOPY



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The PCOPY statement copies one source screen page to a destination page in memory.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


PCOPY *sourcePage%*, *destinationPage%*
  




## Description


* *sourcePage%* is an image page in video memory.
* *destinationPage%* is the video memory location to copy the source image to.
* The working page is set as 0. All drawing occurs there.
* The visible page is set as any page number that the SCREEN mode allows.
* The [\_DISPLAY (function)](/qb64wiki/index.php/DISPLAY_(function) "DISPLAY (function)") return can be used a page number reference in **QB64** (See Example 1).
* The **QB64** [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") statement can also be used to stop screen flicker without page flipping or [CLS](/qb64wiki/index.php/CLS "CLS") and **is the recommended practice**.


### QBasic/QuickBASIC


* *sourcePage%* and *destinationPage%* numbers are limited by the SCREEN mode used. In **QB64**, the same limits don't apply.


  




## Examples


*Example 1:* Creating a mouse cursor using a page number that **you create** in memory without setting up page flipping.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) 'any graphics mode should work without setting up pages [_MOUSEHIDE](/qb64wiki/index.php/MOUSEHIDE "MOUSEHIDE") SetupCursor [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello World!" [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30   [DO](/qb64wiki/index.php/DO "DO") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") 'main loop must contain _MOUSEINPUT '       other program code [LOOP](/qb64wiki/index.php/LOOP "LOOP")  [SUB](/qb64wiki/index.php/SUB "SUB") SetupCursor [ON TIMER](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)")(0.02) UpdateCursor [TIMER](/qb64wiki/index.php/TIMER "TIMER") [ON](/qb64wiki/index.php/ON "ON") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") UpdateCursor PCOPY [_DISPLAY](/qb64wiki/index.php/DISPLAY_(function) "DISPLAY (function)"), 100  'any page number as desination with the _DISPLAY function as source [PSET](/qb64wiki/index.php/PSET "PSET") ([_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")), [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 255, 0) [DRAW](/qb64wiki/index.php/DRAW "DRAW") "ND10F10L3F5L4H5L3" [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")                  'statement shows image PCOPY 100, [_DISPLAY](/qb64wiki/index.php/DISPLAY_(function) "DISPLAY (function)") 'function return as destination page [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


*Note:* Works with [\_DISPLAY (function)](/qb64wiki/index.php/DISPLAY_(function) "DISPLAY (function)") as the other page. If mouse reads are not crucial, put the \_MOUSEINPUT loop inside of the UpdateCursor Sub.
  

*Example 2:* Bouncing balls





| ```  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 7, 0, 1, 0  [DIM](/qb64wiki/index.php/DIM "DIM") x(10), y(10), dx(10), dy(10)  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") a = 1 [TO](/qb64wiki/index.php/TO "TO") 10    x(a) = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 320) + 1    y(a) = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 200) + 1    dx(a) = ([RND](/qb64wiki/index.php/RND "RND") * 2) - 1    dy(a) = ([RND](/qb64wiki/index.php/RND "RND") * 2) - 1  [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")  PCOPY 1, 0                           'place image on the visible page 0  [CLS](/qb64wiki/index.php/CLS "CLS")  [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 100                           'regulates speed of balls in QB64  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") a = 1 [TO](/qb64wiki/index.php/TO "TO") 10    [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE")(x(a), y(a)), 5, 15          'all erasing and drawing is done on page 1     x(a) = x(a) + dx(a)     y(a) = y(a) + dy(a)    [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x(a) > 320 [THEN](/qb64wiki/index.php/THEN "THEN") dx(a) = -dx(a): x(a) = x(a) - 1    [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x(a) < 0 [THEN](/qb64wiki/index.php/THEN "THEN") dx(a) = -dx(a): x(a) = x(a) + 1    [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y(a) > 200 [THEN](/qb64wiki/index.php/THEN "THEN") dy(a) = -dy(a): y(a) = y(a) - 1    [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y(a) < 0 [THEN](/qb64wiki/index.php/THEN "THEN") dy(a) = -dy(a): y(a) = y(a) + 1  [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) ' escape exit  ``` |
| --- |


*Explanation:* PCOPY reduces the flickering produced by clearing the screen. x(a) = x(a) - 1, etc. is just to be safe that the balls stay within the boundaries. dx(a) = -dx(a), etc. is to keep the actual speed while inverting it (so that the ball "bounces"). The rest should be self-explanatory, but if you are unsure about arrays you might want to look at QB64 Tutorials -> [Arrays](/qb64wiki/index.php/Arrays "Arrays").
  




## See also


* [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PCOPY&oldid=8055>"




## Navigation menu








### Search





















