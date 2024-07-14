


SIN - QB64 Phoenix Edition Wiki








# SIN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The SIN function returns the vertical component or sine of an angle measured in radians.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


value! = **SIN(***radian\_angle!***)**
  




## Parameters


* The *radian\_angle* must be measured in radians from 0 to 2 \* Pi.


  




## Description


* To convert from degrees to radians, multiply degrees \* π/180.
* SINE is the vertical component of a unit vector in the direction theta (θ).
* Accuracy can be determined as [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") by default or [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") by following the parameter value with a # suffix.


  

*Example 1:* Converting degree angles to radians for QBasic's trig functions and drawing the line at the angle.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 PI = 4 * [ATN](/qb64wiki/index.php/ATN "ATN")(1) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "PI = 4 * [ATN](/qb64wiki/index.php/ATN "ATN")(1) ="; PI [PRINT](/qb64wiki/index.php/PRINT "PRINT") "COS(PI) = "; [COS](/qb64wiki/index.php/COS "COS")(PI) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "SIN(PI) = "; SIN(PI) DO   [PRINT](/qb64wiki/index.php/PRINT "PRINT")   [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter the degree angle (0 quits): ", DEGREES%   RADIANS = DEGREES% * PI / 180   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "RADIANS = DEGREES% * PI / 180 = "; RADIANS   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "X = COS(RADIANS) = "; [COS](/qb64wiki/index.php/COS "COS")(RADIANS)   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Y = SIN(RADIANS) = "; SIN(RADIANS)   [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (400, 240), 2, 12   [LINE](/qb64wiki/index.php/LINE "LINE") (400, 240)-(400 + (50 * SIN(RADIANS)), 240 + (50 * [COS](/qb64wiki/index.php/COS "COS")(RADIANS))), 11   DEGREES% = RADIANS * 180 / PI   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "DEGREES% = RADIANS * 180 / PI ="; DEGREES% [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") DEGREES% = 0  ``` |
| --- |




| ``` PI = 4 * ATN(1) = 3.141593 COS(PI) = -1 SIN(PI) = -8.742278E-08  Enter the degree angle (0 quits): 45 RADIANS = DEGREES% * PI / 180 = .7853982 X = COS(RADIANS) = .7071068 Y = SIN(RADIANS) = .7071068 DEGREES% = RADIANS * 180 / PI = 45  ``` |
| --- |


*Explanation:* When 8.742278E-08(.00000008742278) is returned by SIN or [COS](/qb64wiki/index.php/COS "COS") the value is essentially zero.
  

*Example 2:* Displays rotating gears made using SIN and [COS](/qb64wiki/index.php/COS "COS") to place the teeth lines.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 9 [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") Pi [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") Pi = 4 * [ATN](/qb64wiki/index.php/ATN "ATN")(1) [DO](/qb64wiki/index.php/DO "DO")     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") G = 0 [TO](/qb64wiki/index.php/TO "TO") Pi * 2 [STEP](/qb64wiki/index.php/STEP "STEP") Pi / 100         [CLS](/qb64wiki/index.php/CLS "CLS")                                   'erase previous         [CALL](/qb64wiki/index.php/CALL "CALL") GEARZ(160, 60, 40, 20, 4, G, 10)         [CALL](/qb64wiki/index.php/CALL "CALL") GEARZ(240, 60, 40, 20, 4, -G, 11)         [CALL](/qb64wiki/index.php/CALL "CALL") GEARZ(240, 140, 40, 20, 4, G, 12)         [CALL](/qb64wiki/index.php/CALL "CALL") GEARZ(320, 140, 40, 20, 4, -G, 13)         [CALL](/qb64wiki/index.php/CALL "CALL") GEARZ(320 + 57, 140 + 57, 40, 20, 4, G, 14)         [CALL](/qb64wiki/index.php/CALL "CALL") GEARZ(320 + 100, 140 + 100, 20, 10, 4, -G * 2 - 15, 15)         [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")         [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 20                 'regulates gear speed and CPU usage     [NEXT](/qb64wiki/index.php/NEXT "NEXT") G [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") GEARZ (XP, YP, RAD, Teeth, TH, G, CLR) t = 0 x = XP + (RAD + TH * SIN(0)) * [COS](/qb64wiki/index.php/COS "COS")(0) y = YP + (RAD + TH * SIN(0)) * SIN(0) [PRESET](/qb64wiki/index.php/PRESET "PRESET") (x, y) m = Teeth * G [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") t = -Pi / 70 [TO](/qb64wiki/index.php/TO "TO") 2 * Pi [STEP](/qb64wiki/index.php/STEP "STEP") Pi / 70     x = XP + (RAD + TH * SIN((Teeth * t + m)) ^ 3) * [COS](/qb64wiki/index.php/COS "COS")(t)     y = YP + (RAD + TH * SIN((Teeth * t + m)) ^ 3) * SIN(t)     [LINE](/qb64wiki/index.php/LINE "LINE") -(x, y), CLR     IF [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" THEN [END](/qb64wiki/index.php/END "END") [NEXT](/qb64wiki/index.php/NEXT "NEXT") t [PAINT](/qb64wiki/index.php/PAINT "PAINT") (XP, YP), CLR            'gear colors optional [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Adapted from code by: DarthWho
  

*Example 3:* Displaying the current seconds for an analog clock. See [COS](/qb64wiki/index.php/COS "COS") for the clock face hour markers.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 Pi2! = 8 * [ATN](/qb64wiki/index.php/ATN "ATN")(1): sec! = Pi2! / 60  ' (2 * pi) / 60 movements per rotation [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (320, 240), 80, 1 [DO](/qb64wiki/index.php/DO "DO")   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [TIME$](/qb64wiki/index.php/TIME$ "TIME$")   Seconds% = [VAL](/qb64wiki/index.php/VAL "VAL")([RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 2)) - 15 ' update seconds   S! = Seconds% * sec! ' radian from the TIME$ value   Sx% = [CINT](/qb64wiki/index.php/CINT "CINT")([COS](/qb64wiki/index.php/COS "COS")(S!) * 60)   ' pixel columns (60 = circular radius)   Sy% = [CINT](/qb64wiki/index.php/CINT "CINT")(SIN(S!) * 60)   ' pixel rows   [LINE](/qb64wiki/index.php/LINE "LINE") (320, 240)-(Sx% + 320, Sy% + 240), 12   [DO](/qb64wiki/index.php/DO "DO"): Check% = [VAL](/qb64wiki/index.php/VAL "VAL")([RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([TIME$](/qb64wiki/index.php/TIME$ "TIME$"), 2)) - 15: [LOOP](/qb64wiki/index.php/LOOP "LOOP") UNTIL Check% <> Seconds%  ' wait loop   [LINE](/qb64wiki/index.php/LINE "LINE") (320, 240)-(Sx% + 320, Sy% + 240), 0 ' erase previous line [LOOP](/qb64wiki/index.php/LOOP "LOOP") UNTIL [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) ' escape keypress exits  ``` |
| --- |


Code by: Ted Weissgerber
The value of 2 π is used to determine the sec! multiplier that determines the radian value as S! The value is divided by 60 second movements. To calculate the seconds the [TIME$](/qb64wiki/index.php/TIME$ "TIME$") function is used and that value is subtracted 15 seconds because the 0 value of pi is actually the 3 hour of the clock (15 seconds fast). SIN and COS will work with negative values the same as positive ones! Then the column and row coordinates for one end of the line are determined using SIN and [COS](/qb64wiki/index.php/COS "COS") multiplied by the radius of the circular line movements. The minute and hour hands could use similar procedures to read different parts of TIME$.


  




## See also


* [\_PI](/qb64wiki/index.php/PI "PI")
* [COS](/qb64wiki/index.php/COS "COS")
* [ATN](/qb64wiki/index.php/ATN "ATN")
* [TAN](/qb64wiki/index.php/TAN "TAN")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [Derived Mathematical Functions](/qb64wiki/index.php/Mathematical_Operations#Derived_Mathematical_Functions "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SIN&oldid=7957>"




## Navigation menu








### Search





















