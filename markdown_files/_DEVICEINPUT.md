


\_DEVICEINPUT - QB64 Phoenix Edition Wiki








# \_DEVICEINPUT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_DEVICEINPUT** function returns the device number when a controller device button, wheel or axis event occurs.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*device%* = \_DEVICEINPUT
*device\_active%* = \_DEVICEINPUT(*device\_number%*)
  




## Parameters


* Use the *device%* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") returned to find the number of the controller device being used.
* A literal specific *device\_number%* parameter can be used to return -1 if active or 0 if inactive, e.g. [WHILE](/qb64wiki/index.php/WHILE "WHILE") \_DEVICEINPUT(2).


  




## Description


* Use [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") to find the number of controller devices available BEFORE using this function.
* [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$") can be used to list the device names and control types using valid [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") numbers.
* When a device button is pressed or a scroll wheel or axis is moved, the device number will be returned.
* Devices are numbered as 1 for keyboard and 2 for mouse. Other controller devices will be numbered 3 or higher if installed.
* [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON"), [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS"), or [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL") will indicate the number of functions available with the specified *device%* number.
* User input events can be monitored reading valid numbered [\_AXIS](/qb64wiki/index.php/AXIS "AXIS"), [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON"), [\_BUTTONCHANGE](/qb64wiki/index.php/BUTTONCHANGE "BUTTONCHANGE") or [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL") functions.
* [ON \_DEVICEINPUT GOSUB](/qb64wiki/index.php/ON...GOSUB "ON...GOSUB") keyboard, mouse, gamecontrol could be used to easily branch to device specific handler routines (see Example 3 below).


  




## Examples


Example 1
Checking device controller interfaces and finding out what devices are being used.


| ``` [FOR](/qb64wiki/index.php/FOR "FOR") i% = 1 [TO](/qb64wiki/index.php/TO "TO") [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STR$](/qb64wiki/index.php/STR$ "STR$")(i%) + ") " + [_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(i%)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Button:"; [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(i%); ",Axis:"; [_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS")(i%); ",Wheel:"; [_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")(i%) [NEXT](/qb64wiki/index.php/NEXT "NEXT") i%  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [DO](/qb64wiki/index.php/DO "DO")     x% = _DEVICEINPUT     [IF](/qb64wiki/index.php/IF "IF") x% [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Device ="; x%; [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ``` [KEYBOARD][BUTTON] Buttons: 512 Axis: 0 Wheels: 0 [MOUSE][BUTTON][AXIS][WHEEL] Buttons: 3 Axis: 2 Wheels: 3 [CONTROLLER]
| --- |




| ``` **Note**  Mouse events must be within the program screen area. Keyboard presses  are registered only when program is in focus.  ``` |
| --- |




---


Example 2
Why does a mouse have 3 wheels? Relative x and y movements can be read using the first 2 [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL") reads.


| ``` ignore% = [_MOUSEMOVEMENTX](/qb64wiki/index.php/MOUSEMOVEMENTX "MOUSEMOVEMENTX") 'dummy call to put mouse into relative movement mode  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Move your mouse and/or your mouse wheel (ESC to exit)"  d% = [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") 'always read number of devices to enable device input [DO](/qb64wiki/index.php/DO "DO")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30 'main loop     [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") _DEVICEINPUT(2) 'loop only runs during a device 2 mouse event         [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL")(1), [_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL")(2), [_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL")(3)     [LOOP](/qb64wiki/index.php/LOOP "LOOP") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ``` **Explanation**  Referencing the [_MOUSEMOVEMENTX](/qb64wiki/index.php/MOUSEMOVEMENTX "MOUSEMOVEMENTX") function hides the mouse and sets  the mouse to a relative movement mode which can be read by [_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL").  _DEVICEINPUT(2) returns -1 (true) only when the mouse is moved,  scrolled or clicked.  ``` |
| --- |




---


Example 3
Using [ON...GOSUB](/qb64wiki/index.php/ON...GOSUB "ON...GOSUB") with the \_DEVICEINPUT number to add keyboard, mouse and game controller event procedures.


| ``` n% = [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") 'required when reading devices [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Number of devices found ="; n% [FOR](/qb64wiki/index.php/FOR "FOR") i% = 1 [TO](/qb64wiki/index.php/TO "TO") n%     [PRINT](/qb64wiki/index.php/PRINT "PRINT") i%; [_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(i%) '1 = keyboard, 2 = mouse, 3 = other controller, etc. [NEXT](/qb64wiki/index.php/NEXT "NEXT") i%  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [DO](/qb64wiki/index.php/DO "DO")     device% = _DEVICEINPUT     [ON](/qb64wiki/index.php/ON "ON") device% [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") keyboard, mouse, controller 'must be inside program loop [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)  [END](/qb64wiki/index.php/END "END")  keyboard: [PRINT](/qb64wiki/index.php/PRINT "PRINT") device%; "Keyboard"; [RETURN](/qb64wiki/index.php/RETURN "RETURN")  mouse: [PRINT](/qb64wiki/index.php/PRINT "PRINT") device%; "Mouse "; [RETURN](/qb64wiki/index.php/RETURN "RETURN")  controller: [PRINT](/qb64wiki/index.php/PRINT "PRINT") device%; "Game control "; [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


Code by Ted Weissgerber


| ``` **Note**  [ON...GOSUB](/qb64wiki/index.php/ON...GOSUB "ON...GOSUB") and [ON...GOTO](/qb64wiki/index.php/ON...GOTO "ON...GOTO") events require numerical values to match  the order of line labels listed in the event used inside loops.  ``` |
| --- |


  




## See also


* [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES"), [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")
* [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON"), [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS"), [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")
* [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON"), [\_AXIS](/qb64wiki/index.php/AXIS "AXIS"), [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL")
* [STRIG](/qb64wiki/index.php/STRIG "STRIG"), [STICK](/qb64wiki/index.php/STICK "STICK")
* [ON...GOSUB](/qb64wiki/index.php/ON...GOSUB "ON...GOSUB")
* [Controller Devices](/qb64wiki/index.php/Controller_Devices "Controller Devices")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DEVICEINPUT&oldid=8576>"




## Navigation menu








### Search





















