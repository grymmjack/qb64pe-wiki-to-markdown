


CIRCLE - QB64 Phoenix Edition Wiki








# CIRCLE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The CIRCLE statement is used in graphic [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes to create circles, arcs or ellipses.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


CIRCLE [[[STEP]**(***column***,** *row***),** *radius%***,** [*drawColor%*][, *startRadian!*, *stopRadian!*] [, *aspect!*]
  




## Parameters


* Can use [STEP](/qb64wiki/index.php/STEP "STEP") for relative coordinate moves from the previous graphic coordinates.
* Coordinates designate the center position of the circle. Can be partially drawn offscreen.
* *radius%* is an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value for half of the total circle diameter.
* *drawColor%* is any available color attribute in the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode used.
* *startRadian!* and *stopRadian!* can be any [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") value from 0 to 2 \* π to create partial circles or ellipses.
* *aspect!* [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") values of 0 to 1 affect the vertical height and values over 1 affect the horizontal width of an ellipse. Aspect = 1 is a normal circle.


  




## Description


* When using *aspect!* the *startRadian!* and *stopRadian!* commas must be included even if not used.
* Radians move in a counter clockwise direction from 0 to 2 \* π. Zero and 2 \* π are the same circle radian at 3 o'clock.
* Negative radian values can be used to draw lines from the end of an arc or partial ellipse to the circle center.
* Commas after the *drawColor%* parameter are not required when creating a normal circle. *drawColor%* can also be omitted to use the last color used in a draw statement.
* The graphic cursor is set to the center of the program window on program start for [STEP](/qb64wiki/index.php/STEP "STEP") relative coordinates.
* **CIRCLE can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only.**


  




## Examples


*Example 1:* Finding when the mouse is inside of a circular area:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  r& = 200 'radius    change circle size and position here cx& = 320 'center x horizontal cy& = 240 'center y vertical  DO   i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")   x& = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")   y& = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")   xy& = ((x& - cx&) ^ 2) + ((y& - cy&) ^ 2) 'Pythagorean theorem   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") r& ^ 2 >= xy& [THEN](/qb64wiki/index.php/THEN "THEN") CIRCLE (cx&, cy&), r&, 10 [ELSE](/qb64wiki/index.php/ELSE "ELSE") CIRCLE (cx&, cy&), r&, 12 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) 'escape key exit  ``` |
| --- |


*Explanation:* The square of the circle radius will be greater than or equal to the sum of the square of the mouse coordinates minus the center position when the pointer is inside of the circle. In this example the circle color will change from red to green.
  

*Example 2:* Program illustrates how the CIRCLE command using a negative radian value can be used to create the hands of a clock.





| ``` [CONST](/qb64wiki/index.php/CONST "CONST") PI = 3.141593 'The mathematical value of PI to six places. You can also use QB64's native _PI. [DIM](/qb64wiki/index.php/DIM "DIM") clock(60)             'A dimensioned array to hold 60 radian points clockcount% = 15          'A counter to keep track of the radians  '* Start at radian 2*PI and continue clockwise to radian 0 '* Since radian 2*PI points directly right, we need to start clockcount% '* at 15 (for 15 seconds).  The [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")/[NEXT](/qb64wiki/index.php/NEXT "NEXT") loop counts backwards in increments '* of 60 giving us the 60 second clock points.  These points are then stored '* in the dimensioned array clock() to be used later. '* [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") radian = 2 * PI [TO](/qb64wiki/index.php/TO "TO") 0 [STEP](/qb64wiki/index.php/STEP "STEP") -(2 * PI) / 60     clock(clockcount%) = radian     clockcount% = clockcount% + 1     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") clockcount% = 61 [THEN](/qb64wiki/index.php/THEN "THEN") clockcount% = 1 [NEXT](/qb64wiki/index.php/NEXT "NEXT") radian '* Change to a graphics screen and draw the clock face [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 7 [CLS](/qb64wiki/index.php/CLS "CLS") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14, 0 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Ritchie's Clock" [COLOR](/qb64wiki/index.php/COLOR "COLOR") 9, 0 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Uses CIRCLE to" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "draw hands!" [COLOR](/qb64wiki/index.php/COLOR "COLOR") 8, 0 CIRCLE (160, 100), 110, 8 'circle with radius of 110 and dark gray CIRCLE (160, 100), 102, 8 'circle with radius of 102 and dark gray [PAINT](/qb64wiki/index.php/PAINT "PAINT") (265, 100), 8, 8 'fill between the two dark gray circles with gray CIRCLE (160, 100), 110, 7 'circle with radius of 110 and light gray '* '* Get the current time from the QuickBASIC built in variable [TIME$](/qb64wiki/index.php/TIME$ "TIME$") '* Since [TIME$](/qb64wiki/index.php/TIME$ "TIME$") is a string, we need to extract the hours, minutes and '* seconds from it using [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$"), [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$") and [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)"). Then, each of these '* extractions need to be converted to a numeric value using VAL and '* stored in their respective variables. '* seconds% = [INT](/qb64wiki/index.php/INT "INT")([VAL](/qb64wiki/index.php/VAL "VAL")([RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 2))) 'extract seconds from [TIME$](/qb64wiki/index.php/TIME$ "TIME$") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") seconds% = 0 [THEN](/qb64wiki/index.php/THEN "THEN") seconds% = 60 'array counts 1 to 60 not 0 to 59 previoussecond% = seconds% 'hold current second for later use minutes% = [INT](/qb64wiki/index.php/INT "INT")([VAL](/qb64wiki/index.php/VAL "VAL")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 4, 2))) 'extract minutes from [TIME$](/qb64wiki/index.php/TIME$ "TIME$") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") minutes% = 0 [THEN](/qb64wiki/index.php/THEN "THEN") minutes% = 60 'array counts 1 to 60 not 0 to 59 previousminute% = minutes% 'hold current minute for later use hours% = [INT](/qb64wiki/index.php/INT "INT")([VAL](/qb64wiki/index.php/VAL "VAL")([LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 2))) 'extract hour from [TIME$](/qb64wiki/index.php/TIME$ "TIME$") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") hours% >= 12 [THEN](/qb64wiki/index.php/THEN "THEN") hours% = hours% - 12 'convert from military time [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") hours% = 0 [THEN](/qb64wiki/index.php/THEN "THEN") hours% = 12 'count from 1 to 12 not 0 to 11 previoushour% = hours% 'hold current hour for later use '* '* Start of main program loop '* [DO](/qb64wiki/index.php/DO "DO")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") seconds% <> previoussecond% [THEN](/qb64wiki/index.php/THEN "THEN") 'has a second elapsed?         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 22, 17 'print the time on the screen at         [PRINT](/qb64wiki/index.php/PRINT "PRINT") [TIME$](/qb64wiki/index.php/TIME$ "TIME$"); 'position 22, 17         '* Since a second has elapsed we need to erase the old second hand         '* position and draw the new position          CIRCLE (160, 100), 100, 0, -clock(previoussecond%), clock(previoussecond%)         CIRCLE (160, 100), 100, 15, -clock(seconds%), clock(seconds%)         previoussecond% = seconds% 'hold current second for later use         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") minutes% <> previousminute% [THEN](/qb64wiki/index.php/THEN "THEN") 'has a minute elapsed?             '* Since a minute has elapsed we need to erase the old hour hand position             CIRCLE (160, 100), 90, 0, -clock(previousminute%), clock(previousminute%)             previousminute% = minutes% 'hold current minute for later use         [END IF](/qb64wiki/index.php/END_IF "END IF")         '*         '* Draw the current minute hand position         '*         CIRCLE (160, 100), 90, 14, -clock(minutes%), clock(minutes%)         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") hours% <> previoushour% [THEN](/qb64wiki/index.php/THEN "THEN") 'has an hour elapsed?             '* Since an hour has elapsed we need to erase the old hour hand position             CIRCLE (160, 100), 75, 0, -clock(previoushour% * 5), clock(previoushour% * 5)             previoushour% = hours% 'hold current hour for later use         [END IF](/qb64wiki/index.php/END_IF "END IF")         '*         '* Draw the current hour hand position         '*         CIRCLE (160, 100), 75, 12, -clock(hours% * 5), clock(hours% * 5)     [END IF](/qb64wiki/index.php/END_IF "END IF")     seconds% = [VAL](/qb64wiki/index.php/VAL "VAL")([RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 2)) 'extract time again and do all over     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") seconds% = 0 [THEN](/qb64wiki/index.php/THEN "THEN") seconds% = 60     minutes% = [VAL](/qb64wiki/index.php/VAL "VAL")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 4, 2))     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") minutes% = 0 [THEN](/qb64wiki/index.php/THEN "THEN") minutes% = 60     hours% = [VAL](/qb64wiki/index.php/VAL "VAL")([LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 2))     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") hours% >= 12 [THEN](/qb64wiki/index.php/THEN "THEN") hours% = hours% - 12     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") hours% = 0 [THEN](/qb64wiki/index.php/THEN "THEN") hours% = 12 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" 'stop program if user presses a key  ``` |
| --- |


code by Terry Ritchie
  




## See also


* [STEP](/qb64wiki/index.php/STEP "STEP"), [DRAW](/qb64wiki/index.php/DRAW "DRAW")
* [LINE](/qb64wiki/index.php/LINE "LINE"), [PSET](/qb64wiki/index.php/PSET "PSET"), [PRESET](/qb64wiki/index.php/PRESET "PRESET")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [SCREEN (function)](/qb64wiki/index.php/SCREEN_(function) "SCREEN (function)")
* [Alternative circle routine](/qb64wiki/index.php/Alternative_circle_routine "Alternative circle routine") (member-contributed program)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CIRCLE&oldid=8114>"




## Navigation menu








### Search





















