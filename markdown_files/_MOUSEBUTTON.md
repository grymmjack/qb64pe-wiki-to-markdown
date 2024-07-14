


\_MOUSEBUTTON - QB64 Phoenix Edition Wiki








# \_MOUSEBUTTON



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MOUSEBUTTON function returns the button status of a specified mouse button when read after [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT").


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*buttonStatus%%* = \_MOUSEBUTTON(*buttoNumber*)
  




## Parameters


* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") *buttoNumber* designates the mouse button to read (See [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") for more than 3).
	+ 1 = Left mouse button
	+ 2 = Right mouse button
	+ 3 = Center or scroll button


  




## Description


* Returns -1 if the corresponding *buttoNumber* is pressed or zero when released.
* Read [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") first to return the current button up or down status. (See Example 2)
* Button clicks and mouse movements will be remembered and should be cleared after an [INPUT](/qb64wiki/index.php/INPUT "INPUT") statement or other interruption.
* To clear unread mouse input, use a [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") loop that loops until it returns 0.
* Use [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$") to find the "[MOUSE]" [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES") number to find the number of buttons available using [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON").
* **Note:** The center mouse button can also be read as [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON")(2) on [\_DEVICEINPUT](/qb64wiki/index.php/DEVICEINPUT "DEVICEINPUT")(2) when a mouse is present.


  




## Examples


*Example 1:* Finding the number of mouse buttons available in QB64. This could also be used for other controller devices.





| ``` [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") d = 1 [TO](/qb64wiki/index.php/TO "TO") [_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES")  'number of input devices found   dev$ = [_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")(d)   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [INSTR](/qb64wiki/index.php/INSTR "INSTR")(dev$, "[MOUSE]") [THEN](/qb64wiki/index.php/THEN "THEN") buttons = [_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")(d): [EXIT](/qb64wiki/index.php/EXIT "EXIT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") buttons; "mouse buttons available"  ``` |
| --- |


  

*Example 2:* How to monitor when a button is down or wait until a mouse button is not held down.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hold down the left mouse button until you want to quit!" DO     i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") ' read #1     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") _MOUSEBUTTON(1) [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Left button down!": [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") '                                                      need to wait     i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") '  read #2                         until the mouse [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [NOT](/qb64wiki/index.php/NOT "NOT") _MOUSEBUTTON(1) '                       button is released  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "DONE!"  ``` |
| --- |


  

*Example 3:* Checking for a click or a double-click by the user.





| ``` [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")  'main program loop    [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")                'check mouse status     buttondown = _MOUSEBUTTON(1)   [LOOP](/qb64wiki/index.php/LOOP "LOOP")   [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") buttondown                 'check for button release     i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")     buttondown = _MOUSEBUTTON(1)     Click = 1   [LOOP](/qb64wiki/index.php/LOOP "LOOP")    [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Click = 1 [THEN](/qb64wiki/index.php/THEN "THEN")                   'if button was pressed and released     t = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") + .3     [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") < t      'check for a second press within .3 seconds       i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") _MOUSEBUTTON(1) [THEN](/qb64wiki/index.php/THEN "THEN") Click = 2: [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")     [LOOP](/qb64wiki/index.php/LOOP "LOOP")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Click = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Double click" [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Click"   [END IF](/qb64wiki/index.php/END_IF "END IF")   Click = 0: buttondown = 0            'reset where needed [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)  ``` |
| --- |


*Explanation:* To find the current button status read [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") repeatedly. The [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") loop looks for a second click.
  

*Example 4:* Verifying that a user clicked and released a mouse button on a program button.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [LINE](/qb64wiki/index.php/LINE "LINE") (250, 250)-(300, 300), 14, BF  [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")   Mouser mx, my, mb   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") mb [THEN](/qb64wiki/index.php/THEN "THEN")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") mx >= 250 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") my >= 250 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") mx <= 300 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") my <= 300 [THEN](/qb64wiki/index.php/THEN "THEN") 'button down       [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") mb 'wait for button release         Mouser mx, my, mb       [LOOP](/qb64wiki/index.php/LOOP "LOOP")       'verify mouse still in box area       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") mx >= 250 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") my >= 250 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") mx <= 300 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") my <= 300 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Click verified on yellow box!"     [END IF](/qb64wiki/index.php/END_IF "END IF")   [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP")  [SUB](/qb64wiki/index.php/SUB "SUB") Mouser (x, y, b) mi = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") b = _MOUSEBUTTON(1) x = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX") y = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


*Explanation:* The mouse SUB has no internal [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") loop so that no button presses, releases or moves are missed.
If the above read procedure goes to another one, it may be advisable to skip over unread input in a [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") only loop.


| ``` [SUB](/qb64wiki/index.php/SUB "SUB") Catchup [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT"): [LOOP](/qb64wiki/index.php/LOOP "LOOP")  [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


The above procedure can be used to catch up after [INPUT](/qb64wiki/index.php/INPUT "INPUT"), [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") or [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$") delays when mouse input may accumulate.
  

*Example 5:* Combining mouse button or keyboard selections in a menu or test:





| ``` [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") 'main program loop in demo only   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "A" 'position A, B & C in same position on every question   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 12, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "B"   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 14, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "C" 'demo only    [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 10 'get user answer loop     [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") 'read mouse     K$ = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")([INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")) 'read keypresses also     x% = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")     y% = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")     Lclick = _MOUSEBUTTON(1)      [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") x%, y%, Lclick 'only used to find mouse coordinates     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x% = 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y% = 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Lclick [THEN](/qb64wiki/index.php/THEN "THEN") 'position clicked       DO         i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")         x% = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")         y% = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")       [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") _MOUSEBUTTON(1)       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x% = 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y% = 10 [THEN](/qb64wiki/index.php/THEN "THEN") K$ = "A" 'position released     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x% = 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y% = 12 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Lclick [THEN](/qb64wiki/index.php/THEN "THEN") 'position clicked       DO         i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")         x% = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")         y% = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")       [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") _MOUSEBUTTON(1)       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x% = 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y% = 12 [THEN](/qb64wiki/index.php/THEN "THEN") K$ = "B" 'position released     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x% = 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y% = 14 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Lclick [THEN](/qb64wiki/index.php/THEN "THEN") 'position clicked       DO         i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")         x% = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")         y% = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")       [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") _MOUSEBUTTON(1)       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x% = 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y% = 14 [THEN](/qb64wiki/index.php/THEN "THEN") K$ = "C" 'position released     [END IF](/qb64wiki/index.php/END_IF "END IF")   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") K$ = "A" [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") K$ = "B" [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") K$ = "C" '[GOTO](/qb64wiki/index.php/GOTO "GOTO") next question    [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LEN](/qb64wiki/index.php/LEN "LEN")(K$) [THEN](/qb64wiki/index.php/THEN "THEN") 'DEMO ONLY     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 22, 35: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "  Answer = "; K$ 'display user answer at location     [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 2 'allow time for user to view answer     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 22, 35: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "SELECT AGAIN"     K$ = "" 'reset K$   [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") 'DEMO only loop use red X box to quit  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* User can cancel letter selection by moving pointer off letter before releasing the left mouse button.
  




## See also


* [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY"), [\_MOUSEWHEEL](/qb64wiki/index.php/MOUSEWHEEL "MOUSEWHEEL")
* [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT"), [\_MOUSEMOVE](/qb64wiki/index.php/MOUSEMOVE "MOUSEMOVE")
* [\_MOUSESHOW](/qb64wiki/index.php/MOUSESHOW "MOUSESHOW"), [\_MOUSEHIDE](/qb64wiki/index.php/MOUSEHIDE "MOUSEHIDE")
* [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES"), [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$"), [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON")
* [\_BUTTON](/qb64wiki/index.php/BUTTON "BUTTON"), [\_BUTTONCHANGE](/qb64wiki/index.php/BUTTONCHANGE "BUTTONCHANGE")
* [Controller Devices](/qb64wiki/index.php/Controller_Devices "Controller Devices")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MOUSEBUTTON&oldid=8047>"




## Navigation menu








### Search





















