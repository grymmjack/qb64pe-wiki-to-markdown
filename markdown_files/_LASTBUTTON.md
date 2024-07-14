


\_LASTBUTTON - QB64 Phoenix Edition Wiki








# \_LASTBUTTON



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_LASTBUTTON function returns the number of buttons a specified INPUT device on your computer has.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


*buttonCount%* = \_\_LASTBUTTON(*deviceNumber*)
  




* Returns the number of buttons that can be read on a specified device number within the number of [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") found.
* A valid number can be sent to the [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON") or [\_BUTTONCHANGE](/qb64wiki/index.php/BUTTONCHANGE "BUTTONCHANGE") function to find any button events.
* The specific device name and functions can be found by the [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$") function [string](/qb64wiki/index.php/STRING "STRING").
* The devices are listed in a numerical order determined by the OS and can be read by the [DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$") function.
* **The [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") function must be read before using \_LASTBUTTON or an ["Illegal Function Call" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.**
* Devices include keyboard (reported as 1), mouse (reported as 2), joysticks, game pads and multiple stick game controllers.


  




## Examples


*Example:* Checking for the system's input devices.





| ``` devices = [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES")  'MUST be read in order for other 2 device functions to work! PRINT "Number of input devices found ="; devices FOR i = 1 TO devices   PRINT [_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(i)   PRINT "Buttons:"; _LASTBUTTON(i) NEXT  ``` |
| --- |




| ``` Number of input devices found = 2 [KEYBOARD][BUTTON] Buttons: 512 [MOUSE][BUTTON][AXIS][WHEEL] Buttons: 3  ``` |
| --- |


Note: The [STRIG](/qb64wiki/index.php/STRIG "STRIG")/[STICK](/qb64wiki/index.php/STICK "STICK") commands won't read from the keyboard or mouse device the above example lists.
  




## See also


* [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS"), [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")
* [\_AXIS](/qb64wiki/index.php/AXIS "AXIS"), [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON"), [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL")
* [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES"), [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")
* [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")
* [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")
* [STRIG](/qb64wiki/index.php/STRIG "STRIG"), [STICK](/qb64wiki/index.php/STICK "STICK")
* [ON STRIG(n)](/qb64wiki/index.php/ON_STRIG(n) "ON STRIG(n)"), [STRIG(n)](/qb64wiki/index.php/STRIG(n) "STRIG(n)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LASTBUTTON&oldid=6064>"




## Navigation menu








### Search





















