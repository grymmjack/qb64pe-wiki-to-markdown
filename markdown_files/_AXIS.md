


\_AXIS - QB64 Phoenix Edition Wiki








# \_AXIS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_AXIS function returns the relative position of a specified axis number on a controller device.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*move!* = \_AXIS(*axis\_number%*)
  




## Description


* [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") values returned range between -1 and 1 as maximums and 0 indicating minimum or axis center.
* When the mouse is moved on the program screen, moves left or above center are negative while below or right are positive.
* The *axis\_number* must be a number which does not exceed the number of axis found by the [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS") function.
* **The number of [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") must be read before using [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$"), [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT") or [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS").**


  




## Examples


*Example:* Reading multiple controller device buttons, axis and wheels.





| ``` [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STR$](/qb64wiki/index.php/STR$ "STR$")(i) + ") " + [_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(i) + " Buttons:"; [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(i); ",Axis:"; [_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS")(i); ",Wheel:"; [_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")(i) [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [DO](/qb64wiki/index.php/DO "DO")     d& = [_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")     [IF](/qb64wiki/index.php/IF "IF") d& [THEN](/qb64wiki/index.php/THEN "THEN") '             the device number cannot be zero!         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Found"; d&;         [FOR](/qb64wiki/index.php/FOR "FOR") b = 1 [TO](/qb64wiki/index.php/TO "TO") [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(d&)             [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_BUTTONCHANGE](/qb64wiki/index.php/BUTTONCHANGE "BUTTONCHANGE")(b); [_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON")(b);         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         [FOR](/qb64wiki/index.php/FOR "FOR") a = 1 [TO](/qb64wiki/index.php/TO "TO") [_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS")(d&)             [PRINT](/qb64wiki/index.php/PRINT "PRINT") _AXIS(a);         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         [FOR](/qb64wiki/index.php/FOR "FOR") w = 1 [TO](/qb64wiki/index.php/TO "TO") [_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")(d&)             [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL")(w);         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) 'escape key exit  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Note:* When there is no device control to read, a [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") n = 1 TO 0 loop will not run thus avoiding a control function read error.
  




## See also


* [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL"), [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON"), [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS")
* [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL"), [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON"), [\_BUTTONCHANGE](/qb64wiki/index.php/BUTTONCHANGE "BUTTONCHANGE")
* [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$"), [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES")
* [\_MOUSEMOVEMENTX](/qb64wiki/index.php/MOUSEMOVEMENTX "MOUSEMOVEMENTX"), [\_MOUSEMOVEMENTY](/qb64wiki/index.php/MOUSEMOVEMENTY "MOUSEMOVEMENTY") (relative movement)
* [Controller Devices](/qb64wiki/index.php/Controller_Devices "Controller Devices")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=AXIS&oldid=8263>"




## Navigation menu








### Search





















