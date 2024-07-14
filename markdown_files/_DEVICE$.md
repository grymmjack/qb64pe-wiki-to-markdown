


\_DEVICE$ - QB64 Phoenix Edition Wiki








# \_DEVICE$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_DEVICE$** function returns a [STRING](/qb64wiki/index.php/STRING "STRING") value holding the controller type, name and input types of the input devices on a computer.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


*device$* = \_DEVICE$(*device\_number*)
  




* The **[\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") function must be read first to get the number of devices and to enable \_DEVICE$ and [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT").**
* The *device\_number* parameter indicates the number of the controller device to be read.
* Returns the [STRING](/qb64wiki/index.php/STRING "STRING") control type, name of the device and input types each can use included in brackets:


* Control type:


[KEYBOARD] always listed as first device when keyboard(s) available. Only one keyboard will show.
[MOUSE always listed as second device when keyboard(s) and mouse(mice) are available. Only one mouse will show.
[CONTROLLER] subsequent devices are listed as controllers which include joysticks and game pads.
* When [CONTROLLER] is returned it may also give the [STRING](/qb64wiki/index.php/STRING "STRING") [[NAME] [device description of the controller.
* When [DISCONNECTED] is returned, then the device was unplugged after device init.
* Returns the type of input after the device name as one or more of the following types:


[[[BUTTON] indicates there are button types of input. [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON") can return the number of buttons available.
[[[AXIS] indicates there are stick types of input. [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS") can return the number of axis available.
[[[WHEEL] indicates that a scrolling input can be read. [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL") can return the number of wheels available.
* **Device numbers above the number of [devices](/qb64wiki/index.php/DEVICES "DEVICES") found will return an OS error.**
* Devices found include keyboard, mouse, joysticks, game pads and multiple stick game controllers.


  




## Examples


*Example 1:* Checking for the system's input devices and the number of buttons available.





| ``` devices = [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") 'MUST be read in order for other 2 device functions to work! [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Number of input devices found ="; devices [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") devices     [PRINT](/qb64wiki/index.php/PRINT "PRINT") _DEVICE$(i)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Buttons:"; [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(i); "Axis:"; [_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS")(i); "Wheels:"; [_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")(i) [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |




| ``` Number of input devices found = 3 [KEYBOARD][BUTTON] Buttons: 512 Axis: 0 Wheels: 0 [MOUSE][BUTTON][AXIS][WHEEL] Buttons: 3 Axis: 2 Wheels: 3 [CONTROLLER]
| --- |


Note: The [STRIG](/qb64wiki/index.php/STRIG "STRIG")/[STICK](/qb64wiki/index.php/STICK "STICK") commands won't read from the keyboard or mouse device the above example lists. They will only work on controllers.


---


*Example 2:* Finding the number of mouse buttons available in QB64. This could also be used for other devices.





| ``` [FOR](/qb64wiki/index.php/FOR "FOR") d = 1 [TO](/qb64wiki/index.php/TO "TO") [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") 'number of input devices found     dev$ = _DEVICE$(d)     [IF](/qb64wiki/index.php/IF "IF") [INSTR](/qb64wiki/index.php/INSTR "INSTR")(dev$, "[MOUSE]") [THEN](/qb64wiki/index.php/THEN "THEN") buttons = [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(d): [EXIT FOR](/qb64wiki/index.php/EXIT_FOR "EXIT FOR") [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") buttons; "mouse buttons available"  ``` |
| --- |


  




## See also


* [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES"), [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")
* [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON"), [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS"), [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")
* [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON"), [\_BUTTONCHANGE](/qb64wiki/index.php/BUTTONCHANGE "BUTTONCHANGE")
* [\_AXIS](/qb64wiki/index.php/AXIS "AXIS"), [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL")
* [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")
* [STRIG](/qb64wiki/index.php/STRIG "STRIG"), [STICK](/qb64wiki/index.php/STICK "STICK")
* [ON STRIG(n)](/qb64wiki/index.php/ON_STRIG(n) "ON STRIG(n)"), [STRIG(n)](/qb64wiki/index.php/STRIG(n) "STRIG(n)")
* [Controller Devices](/qb64wiki/index.php/Controller_Devices "Controller Devices")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DEVICE$&oldid=8447>"




## Navigation menu








### Search





















