


\_DEVICES - QB64 Phoenix Edition Wiki








# \_DEVICES



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_DEVICES** function returns the number of input devices on your computer including keyboard, mouse and game devices.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*device\_count%* = \_DEVICES
  




## Description


* Returns the number of devices that can be listed separately with the [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$") function by the device number.
* Devices include keyboard, mouse, joysticks, game pads and multiple stick game controllers.


Note
This function must be read before trying to use the [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$"), [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT") or any of the **\_LASTxxx** control functions.
  




## Examples


Checking for the system's input devices.


| ``` devices% = _DEVICES 'MUST be read in order for other 2 device functions to work! [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Number of input devices found ="; devices% [FOR](/qb64wiki/index.php/FOR "FOR") i% = 1 [TO](/qb64wiki/index.php/TO "TO") devices%     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(i%)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Buttons:"; [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(i%) [NEXT](/qb64wiki/index.php/NEXT "NEXT") i% [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ``` Number of input devices found = 2 [KEYBOARD][BUTTON] Buttons: 512 [MOUSE][BUTTON][AXIS][WHEEL] Buttons: 3  ``` |
| --- |


Note
The [STRIG](/qb64wiki/index.php/STRIG "STRIG") and [STICK](/qb64wiki/index.php/STICK "STICK") commands won't read from the keyboard or mouse device the above example lists.
  




## See also


* [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$"), [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")
* [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON"), [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS"), [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")
* [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON"), [\_BUTTONCHANGE](/qb64wiki/index.php/BUTTONCHANGE "BUTTONCHANGE")
* [\_AXIS](/qb64wiki/index.php/AXIS "AXIS"), [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL")
* [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT"), [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")
* [STRIG](/qb64wiki/index.php/STRIG "STRIG"), [STICK](/qb64wiki/index.php/STICK "STICK")
* [ON STRIG(n)](/qb64wiki/index.php/ON_STRIG(n) "ON STRIG(n)"), [STRIG(n)](/qb64wiki/index.php/STRIG(n) "STRIG(n)")
* [Controller Devices](/qb64wiki/index.php/Controller_Devices "Controller Devices")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DEVICES&oldid=8408>"




## Navigation menu








### Search





















