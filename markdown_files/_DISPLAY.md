


\_DISPLAY - QB64 Phoenix Edition Wiki








# \_DISPLAY



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_DISPLAY statement turns off the automatic display while only displaying the screen changes when called.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_DISPLAY
  




## Description


* **\_DISPLAY** turns off the auto refresh screen default [\_AUTODISPLAY](/qb64wiki/index.php/AUTODISPLAY "AUTODISPLAY") behavior. Prevents screen flickering.
* Call \_DISPLAY each time the screen graphics are to be displayed. Place call after the image has been changed.
* Re-enable automatic display refreshing by calling [\_AUTODISPLAY](/qb64wiki/index.php/AUTODISPLAY "AUTODISPLAY"). If it isn't re-enabled, things may not be displayed later.
* \_DISPLAY tells **QB64** to render all of the hardware [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") commands loaded into the buffer previously.
* The [\_AUTODISPLAY (function)](/qb64wiki/index.php/AUTODISPLAY_(function) "AUTODISPLAY (function)") can be used to detect the current display behavior.
* **QB64** can set the graphic rendering order of \_SOFTWARE, \_HARDWARE, and \_GLRENDER with [\_DISPLAYORDER](/qb64wiki/index.php/DISPLAYORDER "DISPLAYORDER").


  




## Examples


*Example 1:* Displaying a circle bouncing around the screen.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 x = 21: y = 31 'start position dx = 3: dy = 3 'number of pixel moves per loop [DO](/qb64wiki/index.php/DO "DO")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 100 ' set to 100 frames per second     x = x + dx: y = y + dy     [IF](/qb64wiki/index.php/IF "IF") x < 0 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") x > 640 [THEN](/qb64wiki/index.php/THEN "THEN") dx = -dx 'limit columns and reverse column direction each side     [IF](/qb64wiki/index.php/IF "IF") y < 0 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") y > 480 [THEN](/qb64wiki/index.php/THEN "THEN") dy = -dy 'limit rows and reverse row direction top or bottom     [IF](/qb64wiki/index.php/IF "IF") px <> x [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") py <> y [THEN](/qb64wiki/index.php/THEN "THEN") [FOR](/qb64wiki/index.php/FOR "FOR") d = 1 [TO](/qb64wiki/index.php/TO "TO") 20: [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (px, py), d, 0: [NEXT](/qb64wiki/index.php/NEXT "NEXT") 'erase     [FOR](/qb64wiki/index.php/FOR "FOR") c = 1 [TO](/qb64wiki/index.php/TO "TO") 20: [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (x, y), c, 6: [NEXT](/qb64wiki/index.php/NEXT "NEXT") 'draw new circle at new position     px = x: py = y 'save older coordinates to erase older circle next loop     _DISPLAY 'after new circle is set, show it [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)  ``` |
| --- |


*Explanation:* The loop is set with [\_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") to 100 frames per second to limit CPU usage and the speed of the ball. Each loop a circle is drawn while the previous one is erased when the coordinates change. \_DISPLAY only shows the new circle position once each loop. The **\_DISPLAY** routine eliminates the need for setting [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") swap pages, [CLS](/qb64wiki/index.php/CLS "CLS") and [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY"). \_DISPLAY keeps the image off of the screen until the changes have all completed. Drawing 40 circles every loop helps slow down the ball.


---


*Example 2:* \_DISPLAY must be used to render hardware images placed with [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (**version 1.000 and up**).





| ``` [CONST](/qb64wiki/index.php/CONST "CONST") MenuHeight = 200   [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) 'SLEEP 1 [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20 [DO](/qb64wiki/index.php/DO "DO")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30     DisplayMenu     k = [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT")     [IF](/qb64wiki/index.php/IF "IF") k <> 0 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") k, [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") k = 32 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") k = 27   [SUB](/qb64wiki/index.php/SUB "SUB") DisplayMenu     [STATIC](/qb64wiki/index.php/STATIC "STATIC") init, MS_HW [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")     [IF](/qb64wiki/index.php/IF "IF") [NOT](/qb64wiki/index.php/NOT "NOT") init [THEN](/qb64wiki/index.php/THEN "THEN")         init = -1         MS = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, MenuHeight, 32) 'MenuScreen image         D = [_DEST](/qb64wiki/index.php/DEST_(function) "DEST (function)"): [_DEST](/qb64wiki/index.php/DEST "DEST") MS         [CLS](/qb64wiki/index.php/CLS "CLS") , &HFFAAAAAA 'background color gray         [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (20, 2), "Menu Test" 'image text         MS_HW = [_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")(MS, 33) 'create the MenuScreen_HardWare image         [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") MS         [_DEST](/qb64wiki/index.php/DEST "DEST") D     [END IF](/qb64wiki/index.php/END_IF "END IF")     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 0)-(640, MenuHeight), MS_HW     _DISPLAY [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code adapted by Galleon
*Notes:* When \_DISPLAY is commented out, the hardware Menu Test screen portion will blink and key codes may be seen underneath.
  




## See also


* [\_DISPLAY (function)](/qb64wiki/index.php/DISPLAY_(function) "DISPLAY (function)")
* [\_DISPLAYORDER](/qb64wiki/index.php/DISPLAYORDER "DISPLAYORDER")
* [\_AUTODISPLAY](/qb64wiki/index.php/AUTODISPLAY "AUTODISPLAY"), [\_AUTODISPLAY (function)](/qb64wiki/index.php/AUTODISPLAY_(function) "AUTODISPLAY (function)")
* [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE")
* [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DISPLAY&oldid=8313>"




## Navigation menu








### Search





















