


\_MOUSEMOVEMENTX - QB64 Phoenix Edition Wiki








# \_MOUSEMOVEMENTX



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MOUSEMOVEMENTX function returns the relative horizontal position of the mouse cursor as positive or negative values.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


*horizontalMove* = \_MOUSEMOVEMENTX
  




* Returns the relative horizontal cursor pixel position compared to the previous cursor position. Negative values are moves to the left.
* **Note:** A [\_MOUSESHOW](/qb64wiki/index.php/MOUSESHOW "MOUSESHOW") statement will disable \_MOUSEMOVEMENTX or [\_MOUSEMOVEMENTY](/qb64wiki/index.php/MOUSEMOVEMENTY "MOUSEMOVEMENTY") relative mouse movement reads.
* Can also be used to check for any mouse movements to enable a program or close [Screen Saver Programs](/qb64wiki/index.php/Screen_Saver_Programs "Screen Saver Programs").
* Sets the mouse to a relative movement mode which can be read by [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL") instead of [\_AXIS](/qb64wiki/index.php/AXIS "AXIS") as mouse [device](/qb64wiki/index.php/DEVICES "DEVICES") 2.


  




## Examples


Example 1
Since values returned are relative to the last position, the returns can be positive or negative.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 PX = 320: PY = 240 'center position [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 200     [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")         PX = PX + _MOUSEMOVEMENTX         PY = PY + [_MOUSEMOVEMENTY](/qb64wiki/index.php/MOUSEMOVEMENTY "MOUSEMOVEMENTY")     [LOOP](/qb64wiki/index.php/LOOP "LOOP")     [CLS](/qb64wiki/index.php/CLS "CLS")     [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (PX, PY), 10, 10     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") PX, PY [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) 'escape key exit  ``` |
| --- |




---


Example 2
MOD is used to keep horizontal movement of the circle and cursor inside of the SCREEN 13 window(320).
Note when using the function this way, then give the user a keypress exit option. Make sure the user has some way to exit that is not dependent on clicking the X button.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13, , 1, 0 [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 200     [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")         x = x + _MOUSEMOVEMENTX         y = y + [_MOUSEMOVEMENTY](/qb64wiki/index.php/MOUSEMOVEMENTY "MOUSEMOVEMENTY")     [LOOP](/qb64wiki/index.php/LOOP "LOOP")     x = (x + 320) [MOD](/qb64wiki/index.php/MOD "MOD") 320 'keeps object on screen     y = (y + 200) [MOD](/qb64wiki/index.php/MOD "MOD") 200 'remove if off screen moves are desired     [CLS](/qb64wiki/index.php/CLS "CLS")     [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (x, y), 20     [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY") 1, 0 [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" 'press any key to exit  ``` |
| --- |


  




## See also


* [\_MOUSEMOVEMENTY](/qb64wiki/index.php/MOUSEMOVEMENTY "MOUSEMOVEMENTY")
* [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT"), [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")
* [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES"), [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")
* [\_WHEEL](/qb64wiki/index.php/WHEEL "WHEEL"), [\_LASTWHEEL](/qb64wiki/index.php/LASTWHEEL "LASTWHEEL")
* [\_AXIS](/qb64wiki/index.php/AXIS "AXIS"), [\_LASTAXIS](/qb64wiki/index.php/LASTAXIS "LASTAXIS")
* [\_MOUSESHOW](/qb64wiki/index.php/MOUSESHOW "MOUSESHOW"), [\_MOUSEHIDE](/qb64wiki/index.php/MOUSEHIDE "MOUSEHIDE")
* [Screen Saver Programs](/qb64wiki/index.php/Screen_Saver_Programs "Screen Saver Programs")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MOUSEMOVEMENTX&oldid=8838>"




## Navigation menu








### Search





















