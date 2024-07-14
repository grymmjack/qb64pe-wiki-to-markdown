


\_MOUSEMOVE - QB64 Phoenix Edition Wiki








# \_MOUSEMOVE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MOUSEMOVE statement moves the mouse pointer to a new position on the screen as determined by the column and row coordinates.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


\_MOUSEMOVE *column%*, *row%*
  




## Parameters


* *column%* is the horizontal pixel coordinate to place the mouse pointer and can be any value from 0 to [\_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(0) - 1.
* *row%* is the vertical pixel position to place the mouse pointer and can be any value from 0 to [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(0) - 1


  




## Description


* Maximum coordinate values are based on a program's current [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode resolution or the pixel size set by [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE").
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 uses text block coordinates. **Coordinates off the screen area will create an "Illegal Function Call" [ERROR](/qb64wiki/index.php/ERROR_Codes "ERROR Codes")**
* Can be used to position the pointer to a default dialog button or move the cursor away from a button so it is not clicked twice.
* Does not require [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") to be used, but all moves will be remembered and can be read by mouse functions.


  




## Availability


* **Versions prior to 1.000** (Version 1.000 had this function disabled for compatibility reasons.)
* **Version 1.1 and up**


  




## Examples


*Example:* How to move the mouse cursor using remembered mouse movements. Press any key to quit.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") 'start reading mouse events before INPUT to hold in memory [PRINT](/qb64wiki/index.php/PRINT "PRINT") [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Move the mouse pointer and make a few clicks, then press Enter!", dummy$ _MOUSEMOVE 1, 1 DO: [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30     count = count + 1     i = [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")     x = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"): y = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")     b = [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(1)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") count, x, y, b     _MOUSEMOVE x, y [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") i = 0 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") > "" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Done!"  ``` |
| --- |


*Explanation:* The [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") function will hold previous and \_MOUSEMOVE events so press any key when you want to quit.
**Note: [INPUT](/qb64wiki/index.php/INPUT "INPUT"), [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$") and [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") will allow continued reading of mouse events while awaiting program user input!**
It is recommended that a [WHILE](/qb64wiki/index.php/WHILE "WHILE") [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT"): [WEND](/qb64wiki/index.php/WEND "WEND") loop be used immediately after to clear stored mouse events.
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1141)
* [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MOUSEMOVE&oldid=8890>"




## Navigation menu








### Search





















