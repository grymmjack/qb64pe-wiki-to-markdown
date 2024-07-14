


STICK - QB64 Phoenix Edition Wiki








# STICK



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **STICK** function returns the directional axis coordinate move of game port (&H201) joystick or USB controller devices.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


QuickBASIC
coordinate\_move% = STICK*(direction%)*
QB64
coordinate\_move% = STICK*(direction%[, axis\_number%])*
  




## Description


* **QB64** allows any number of coordinate pairs for more than two game device controllers. STICK will not read a mouse axis.
* *axis\_number* can be used as the next axis parameter for controllers with multiple axis using the SAME *directional* parameters.
* The *axis\_number* 1 can be omitted for the main stick column and row parameter reads.
* Point of view "hats" also have 2 axis. Slide, turn or twist controls have one. The device determines the order of the axis.
* Returns coordinate values from 1 to 254. QBasic only returned values from 1 to 200.
* STICK(0) is required to get values from the other STICK functions. Always read it first!




| ``` **STICK(0) returns the column coordinate of device 1. Enables reads of the other STICK values.** **STICK(1) returns row coordinate of device 1.** STICK(2) returns column coordinate of device 2. (second joystick if used) STICK(3) returns row coordinate of device 2 if used. (QBasic maximum was 2 controllers) **STICK(4) returns column coordinate of device 3. (other joysticks if used in QB64 only!)** **STICK(5) returns row coordinate of device 3 if used.**  ``` |
| --- |


* **QB64** allows more joysticks by extending the numbers in pairs like device 3 above. EX: STICK(6): STICK(7) 'device 4
* **QB64** allows a dual stick to be read using the same first parameters and 2 as the second parameter. EX: STICK(0, 2)
* **There will not be an error if you try to read too many device axis or buttons!**


  




## Examples


*Example 1:* Displays the input from 3 joysticks, all with dual sticks and 3 buttons.





| ``` [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 10    [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "JOY1: STICK"; STICK(0); STICK(1); STICK(0, 2); STICK(1, 2);_   "STRIG"; [STRIG](/qb64wiki/index.php/STRIG "STRIG")(0); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(1); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(4); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(5); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(8); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(9)    [PRINT](/qb64wiki/index.php/PRINT "PRINT") "JOY2: STICK"; STICK(2); STICK(3); STICK(2, 2); STICK(3, 2);_   "STRIG"; [STRIG](/qb64wiki/index.php/STRIG "STRIG")(2); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(3); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(6); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(7); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(10); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(11)    [PRINT](/qb64wiki/index.php/PRINT "PRINT") "JOY3: STICK"; STICK(4); STICK(5); STICK(4, 2); STICK(5, 2);_   "STRIG"; [STRIG](/qb64wiki/index.php/STRIG "STRIG")(0, 3); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(1, 3); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(4, 3); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(5, 3); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(8, 3); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(9, 3)  [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") > ""  ``` |
| --- |


*Explanation:* Notice the extra **QB64 only** parameters used to cater for the 2nd stick and the buttons of the 3rd joystick.
  

*Example 2:* Displays the Sidewinder Precision Pro Stick, Slider, Z Axis, and Hat Point of View.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 d = [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Number of input devices found ="; d [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") d   [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(i)   buttons = [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(i)   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Buttons:"; buttons [NEXT](/qb64wiki/index.php/NEXT "NEXT")  DO: [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 50   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 1   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "   X    Main    Y          Slider         Z-axis           POV"   [PRINT](/qb64wiki/index.php/PRINT "PRINT") STICK(0, 1), STICK(1, 1), STICK(0, 2), STICK(1, 2), STICK(0, 3); STICK(1, 3); "   "   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "                   Buttons"   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 4 * buttons - 1 [STEP](/qb64wiki/index.php/STEP "STEP") 4     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STRIG](/qb64wiki/index.php/STRIG "STRIG")(i); [STRIG](/qb64wiki/index.php/STRIG "STRIG")(i + 1); [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(219);   [NEXT](/qb64wiki/index.php/NEXT "NEXT")   [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  ``` |
| --- |


*Explanation:* Each axis on the first controller found is either STICK(0, n) or STICK(1, n) with n increasing when necessary.


| ``` Number of input devices found = 3 [KEYBOARD][BUTTON Buttons: 512 [MOUSE][BUTTON][AXIS][WHEEL] Buttons: 3 [CONTROLLER]
| --- |


*Note:* A Sidewinder Precision Pro requires that pins 2 and 7(blue and purple) be connected together for digital USB recognition.
[Sidewinder Precision Pro game port to USB adapter](http://www.amazon.com/Belkin-F3U200-08INCH-Joystick-Adapter-SideWinder/dp/B000067RIV)
  




## See also


* [STRIG](/qb64wiki/index.php/STRIG "STRIG")
* [ON STRIG(n)](/qb64wiki/index.php/ON_STRIG(n) "ON STRIG(n)")
* [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES"), [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$"), [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")
* [Single and Dual Stick Controllers](https://en.wikipedia.org/wiki/Analog_stick "wikipedia:Analog stick")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=STICK&oldid=8996>"




## Navigation menu








### Search





















