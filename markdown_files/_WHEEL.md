


\_WHEEL - QB64 Phoenix Edition Wiki








# \_WHEEL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_WHEEL function returns the relative position of a specified wheel number on a controller device.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


*move* = \_WHEEL(*wheelNumber%*)
  




* Returns -1 when scrolling up and 1 when scrolling down with 0 indicating no movement since last read.
* Add consecutive wheel values to determine a cumulative value over time for scrolling or moving objects.
* *wheelNumber%* must be a number which does not exceed the number of wheels found by the [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL") function.
* When a mouse indicates it has 3 wheels, the first two are for relative movement reads. The third wheel is for scrolling.
* **The number of [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") must be read before using [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$"), [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT") or [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL").**


  




## Examples


*Example 1:* Reading multiple controller device buttons, axis and wheels.





| ``` [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES")   [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STR$](/qb64wiki/index.php/STR$ "STR$")(i) + ") " + [_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(i) + " Buttons:"; [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(i); ",Axis:"; [_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS")(i); ",Wheel:"; [_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")(i) [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")   d& = [_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") d& [THEN](/qb64wiki/index.php/THEN "THEN") '             the device number cannot be zero!     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Found"; d&;     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") b = 1 [TO](/qb64wiki/index.php/TO "TO") [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(d&)       [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_BUTTONCHANGE](/qb64wiki/index.php/BUTTONCHANGE "BUTTONCHANGE")(b); [_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON")(b);     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") a = 1 [TO](/qb64wiki/index.php/TO "TO") [_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS")(d&)       [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_AXIS](/qb64wiki/index.php/AXIS "AXIS")(a);     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") w = 1 [TO](/qb64wiki/index.php/TO "TO") [_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")(d&)       [PRINT](/qb64wiki/index.php/PRINT "PRINT") _WHEEL(w);     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [PRINT](/qb64wiki/index.php/PRINT "PRINT")   [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) 'escape key exit  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Note:* When there is no device control to read, a [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") n = 1 TO 0 loop will not run thus avoiding a control function read error.
  

*Example 2:* Why does a mouse have 3 wheels? Relative x and y movements can be read using the first 2 \_WHEEL reads.





| ``` ignore = [_MOUSEMOVEMENTX](/qb64wiki/index.php/MOUSEMOVEMENTX "MOUSEMOVEMENTX") 'dummy call to put mouse into relative movement mode  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Move your mouse and/or your mouse wheel (ESC to exit)"  d = [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") '  always read number of devices to enable device input DO: [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30  'main loop   [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")(2) 'loop only runs during a device 2 mouse event         [PRINT](/qb64wiki/index.php/PRINT "PRINT") _WHEEL(1), _WHEEL(2), _WHEEL(3)   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)  ``` |
| --- |


*Explanation:* Referencing the [\_MOUSEMOVEMENTX](/qb64wiki/index.php/MOUSEMOVEMENTX "MOUSEMOVEMENTX") function hides the mouse and sets the mouse to a relative movement mode which can be read by \_WHEEL. [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")(2) returns -1 (true) only when the mouse is moved, scrolled or clicked.
  




## See also


* [\_MOUSEWHEEL](/qb64wiki/index.php/MOUSEWHEEL "MOUSEWHEEL")
* [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL"), [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON"), [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS")
* [\_AXIS](/qb64wiki/index.php/AXIS "AXIS"), [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON"), [\_BUTTONCHANGE](/qb64wiki/index.php/BUTTONCHANGE "BUTTONCHANGE")
* [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES"), [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$"), [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")
* [\_MOUSEMOVEMENTX](/qb64wiki/index.php/MOUSEMOVEMENTX "MOUSEMOVEMENTX"), [\_MOUSEMOVEMENTY](/qb64wiki/index.php/MOUSEMOVEMENTY "MOUSEMOVEMENTY")
* [Controller Devices](/qb64wiki/index.php/Controller_Devices "Controller Devices")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=WHEEL&oldid=6315>"




## Navigation menu








### Search





















