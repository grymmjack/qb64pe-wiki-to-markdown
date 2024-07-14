


ATN - QB64 Phoenix Edition Wiki








# ATN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The ATN or arctangent function returns the angle in radians of a numerical [tangent](/qb64wiki/index.php/TAN "TAN") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*radianAngle* = ATN(*tangent!*)
  




## Parameters


* The return is the *tangent!'*s angle in **radians**.
* *tangent!* [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") or [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") values are used by the function. EX:**Pi = 4 \* ATN(1)**


  




## Description


* To convert from radians to degrees, multiply radians \* (180 / π).
* The *tangent* value would be equal to the tangent value of an angle. Ex: **[TAN](/qb64wiki/index.php/TAN "TAN")(ATN(1)) = 1**
* The function return value is between -π / 2 and π / 2.


  




## Examples


*Example 1:* When the [TANgent](/qb64wiki/index.php/TAN "TAN") value equals 1, the line is drawn at a 45 degree angle (.7853982 radians) where [SIN](/qb64wiki/index.php/SIN "SIN") / [COS](/qb64wiki/index.php/COS "COS") = 1.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 x = 100 * [COS](/qb64wiki/index.php/COS "COS")(ATN(1)) y = 100 * [SIN](/qb64wiki/index.php/SIN "SIN")(ATN(1)) [LINE](/qb64wiki/index.php/LINE "LINE") (200, 200)-(200 + x, 200 + y)  ``` |
| --- |


  

*Example 2:* ATN can be used to define π in [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") or [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") precision. The calculation cannot be used as a [CONSTant](/qb64wiki/index.php/CONST "CONST").





| ``` Pi = 4 * ATN(1)   '[SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") precision Pi# = 4 * ATN(1#) '[DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") precision PRINT Pi, Pi#  ``` |
| --- |


*Note:* You can use QB64's native [\_PI](/qb64wiki/index.php/PI "PI") function.
  

*Example 3:* Finds the angle from the center point to the mouse pointer.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) x1! = 320 y1! = 240  DO   [PRESET](/qb64wiki/index.php/PRESET "PRESET") (x1!, y1!), [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255)   dummy% = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")   x2! = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")   y2! = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")   [LINE](/qb64wiki/index.php/LINE "LINE") (x1, y1)-(x2, y2), [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 0, 0)   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") getangle(x1!, y1!, x2!, y2!)   [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")   [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 200   [CLS](/qb64wiki/index.php/CLS "CLS") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") getangle# (x1#, y1#, x2#, y2#) 'returns 0-359.99... [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y2# = y1# [THEN](/qb64wiki/index.php/THEN "THEN")   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x1# = x2# [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION")   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x2# > x1# [THEN](/qb64wiki/index.php/THEN "THEN") getangle# = 90 [ELSE](/qb64wiki/index.php/ELSE "ELSE") getangle# = 270   [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION") [END IF](/qb64wiki/index.php/END_IF "END IF") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x2# = x1# [THEN](/qb64wiki/index.php/THEN "THEN")   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y2# > y1# [THEN](/qb64wiki/index.php/THEN "THEN") getangle# = 180   [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION") [END IF](/qb64wiki/index.php/END_IF "END IF") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y2# < y1# [THEN](/qb64wiki/index.php/THEN "THEN")   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x2# > x1# [THEN](/qb64wiki/index.php/THEN "THEN")     getangle# = ATN((x2# - x1#) / (y2# - y1#)) * -57.2957795131   [ELSE](/qb64wiki/index.php/ELSE "ELSE")     getangle# = ATN((x2# - x1#) / (y2# - y1#)) * -57.2957795131 + 360   [END IF](/qb64wiki/index.php/END_IF "END IF") [ELSE](/qb64wiki/index.php/ELSE "ELSE")   getangle# = ATN((x2# - x1#) / (y2# - y1#)) * -57.2957795131 + 180 [END IF](/qb64wiki/index.php/END_IF "END IF") [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Function by Galleon
  




## See also


* [\_PI](/qb64wiki/index.php/PI "PI") (QB64 function)
* [\_ATAN2](/qb64wiki/index.php/ATAN2 "ATAN2") ((QB64 function)
* [TAN](/qb64wiki/index.php/TAN "TAN") (tangent function)
* [SIN](/qb64wiki/index.php/SIN "SIN"), [COS](/qb64wiki/index.php/COS "COS")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [Derived Mathematical Functions](/qb64wiki/index.php/Mathematical_Operations#Derived_Mathematical_Functions "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ATN&oldid=8584>"




## Navigation menu








### Search





















