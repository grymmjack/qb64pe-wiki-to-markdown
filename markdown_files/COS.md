


COS - QB64 Phoenix Edition Wiki








# COS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The COS function returns the horizontal component or the cosine of an angle measured in radians.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*value!* = COS(*radianAngle!*)
  




## Parameters


* The *radianAngle!* must be measured in radians.


  




## Description


* To convert from degrees to radians, multiply degrees \* π / 180.
* COSINE is the horizontal component of a unit vector in the direction theta (θ).
* COS(x) can be calculated in either [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") or [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") precision depending on its argument.


COS(4) = -.6536436 ...... COS(4#) = -.6536436208636119
  




## Examples


*Example 1:* Converting degree angles to radians for QBasic's trig functions and drawing the line at the angle.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 PI = 4 * [ATN](/qb64wiki/index.php/ATN "ATN")(1) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "PI = 4 * [ATN](/qb64wiki/index.php/ATN "ATN")(1) ="; PI [PRINT](/qb64wiki/index.php/PRINT "PRINT") "COS(PI) = "; COS(PI) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "SIN(PI) = "; [SIN](/qb64wiki/index.php/SIN "SIN")(PI) [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")   [PRINT](/qb64wiki/index.php/PRINT "PRINT")   [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter the degree angle (0 quits): ", DEGREES%   RADIANS = DEGREES% * PI / 180   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "RADIANS = DEGREES% * PI / 180 = "; RADIANS   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "X = COS(RADIANS) = "; COS(RADIANS)   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Y = SIN(RADIANS) = "; [SIN](/qb64wiki/index.php/SIN "SIN")(RADIANS)   [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (400, 240), 2, 12   [LINE](/qb64wiki/index.php/LINE "LINE") (400, 240)-(400 + (50 * [SIN](/qb64wiki/index.php/SIN "SIN")(RADIANS)), 240 + (50 * COS(RADIANS))), 11   DEGREES% = RADIANS * 180 / PI   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "DEGREES% = RADIANS * 180 / PI ="; DEGREES% [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") DEGREES% = 0  ``` |
| --- |




| ``` PI = 4 * ATN(1) = 3.141593 COS(PI) = -1 SIN(PI) = -8.742278E-08  Enter the degree angle (0 quits): 45 RADIANS = DEGREES% * PI / 180 = .7853982 X = COS(RADIANS) = .7071068 Y = SIN(RADIANS) = .7071068 DEGREES% = RADIANS * 180 / PI = 45  ``` |
| --- |


*Explanation:* When 8.742278E-08(.00000008742278) is returned by [SIN](/qb64wiki/index.php/SIN "SIN") or COS the value is essentially zero.
  

*Example 2:* Creating 12 analog clock hour points using [CIRCLEs](/qb64wiki/index.php/CIRCLE "CIRCLE") and [PAINT](/qb64wiki/index.php/PAINT "PAINT")





| ```  PI2 = 8 * [ATN](/qb64wiki/index.php/ATN "ATN")(1)                  '2 * π  arc! = PI2 / 12                          'arc interval between hour circles  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  FOR t! = 0 TO PI2 STEP arc!    cx% = [CINT](/qb64wiki/index.php/CINT "CINT")(COS(t!) * 70) ' pixel columns (circular radius = 70)    cy% = [CINT](/qb64wiki/index.php/CINT "CINT")([SIN](/qb64wiki/index.php/SIN "SIN")(t!) * 70) ' pixel rows    [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (cx% + 320, cy% + 240), 3, 12    [PAINT](/qb64wiki/index.php/PAINT "PAINT") [STEP](/qb64wiki/index.php/STEP "STEP")(0, 0), 9, 12  NEXT  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* The 12 circles are placed at radian angles that are 1/12 of 6.28318 or .523598 radians apart.


  

*Example 3:* Creating a rotating spiral with COS and [SIN](/qb64wiki/index.php/SIN "SIN").





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32)  [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")   [LINE](/qb64wiki/index.php/LINE "LINE") (0, 0)-(640, 480), [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 0, 0), BF   j = j + 1   [PSET](/qb64wiki/index.php/PSET "PSET") (320, 240)   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 100 [STEP](/qb64wiki/index.php/STEP "STEP") .1     [LINE](/qb64wiki/index.php/LINE "LINE") -(.05 * i * i * COS(j + i) + 320, .05 * i * i * [SIN](/qb64wiki/index.php/SIN "SIN")(j + i) + 240)   [NEXT](/qb64wiki/index.php/NEXT "NEXT")   [PSET](/qb64wiki/index.php/PSET "PSET") (320, 240)   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 100 [STEP](/qb64wiki/index.php/STEP "STEP") .1     [LINE](/qb64wiki/index.php/LINE "LINE") -(.05 * i * i * COS(j + i + 10) + 320, .05 * i * i * [SIN](/qb64wiki/index.php/SIN "SIN")(j + i + 10) + 240)   [NEXT](/qb64wiki/index.php/NEXT "NEXT")   [PSET](/qb64wiki/index.php/PSET "PSET") (320, 240)   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 100 [STEP](/qb64wiki/index.php/STEP "STEP") .1     [PAINT](/qb64wiki/index.php/PAINT "PAINT") (.05 * i * i * COS(j + i + 5) + 320, .05 * i * i * [SIN](/qb64wiki/index.php/SIN "SIN")(j + i + 5) + 240)   [NEXT](/qb64wiki/index.php/NEXT "NEXT")    [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")   [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")60) = 1 'escape exit  ``` |
| --- |


Code by Ben
  




## See also


* [\_PI](/qb64wiki/index.php/PI "PI") (QB64 function)
* [SIN](/qb64wiki/index.php/SIN "SIN") (sine)
* [ATN](/qb64wiki/index.php/ATN "ATN") (arctangent)
* [TAN](/qb64wiki/index.php/TAN "TAN") (tangent)
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [Derived Mathematical Functions](/qb64wiki/index.php/Mathematical_Operations#Derived_Mathematical_Functions "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=COS&oldid=7844>"




## Navigation menu








### Search





















