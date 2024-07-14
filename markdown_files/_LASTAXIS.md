


\_LASTAXIS - QB64 Phoenix Edition Wiki








# \_LASTAXIS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_LASTAXIS function returns the number of axis a specified number INPUT device on your computer has.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*axisCount%* = \_LASTAXIS(*deviceNumber*)
  




## Description


* Returns the number of axis that can be read on a specified device number within the number of [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") found.
* A valid number can be sent to the [\_AXIS](/qb64wiki/index.php/AXIS "AXIS") function to find any relative axis movements.
* The devices are listed in a numerical order determined by the OS and can be read by the [DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$") function.
* **The [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") function must be read before using \_LASTAXIS or an ["Illegal Function Call" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.**
* Devices include keyboard(1), mouse(2), joysticks, game pads and multiple stick game controllers.


  




## Examples


*Example:* Checking for the system's input devices and number of axis.





| ``` devices = [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES")  'MUST be read in order for other 2 device functions to work! PRINT "Number of input devices found ="; devices FOR i = 1 TO devices   PRINT [_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(i)   IF [INSTR](/qb64wiki/index.php/INSTR "INSTR")([_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(i), "[AXIS]") THEN PRINT "Axis:"; _LASTAXIS(i) NEXT  ``` |
| --- |




| ``` Number of input devices found = 2 [KEYBOARD][BUTTON] [MOUSE][BUTTON][AXIS][WHEEL] Axis: 2  ``` |
| --- |


Note: The [STRIG](/qb64wiki/index.php/STRIG "STRIG")/[STICK](/qb64wiki/index.php/STICK "STICK") commands won't read from the keyboard or mouse device the above example lists.
  




## See also


* [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON"), [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")
* [\_AXIS](/qb64wiki/index.php/AXIS "AXIS"), [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON"), [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL")
* [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$"), [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES")
* [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")
* [STRIG](/qb64wiki/index.php/STRIG "STRIG"), [STICK](/qb64wiki/index.php/STICK "STICK")
* [ON STRIG(n)](/qb64wiki/index.php/ON_STRIG(n) "ON STRIG(n)"), [STRIG(n)](/qb64wiki/index.php/STRIG(n) "STRIG(n)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LASTAXIS&oldid=6063>"




## Navigation menu








### Search





















