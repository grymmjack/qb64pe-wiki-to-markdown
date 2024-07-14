


\_MOUSEINPUT - QB64 Phoenix Edition Wiki








# \_MOUSEINPUT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MOUSEINPUT function is used to monitor any new mouse positions, button presses or movements of the scroll wheel. Must be called before other mouse information becomes available.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*infoExists%%* = \_MOUSEINPUT
  




## Description


* Returns -1 if new mouse information is available, otherwise it returns 0.
* Must be called before reading any of the other mouse functions. The function will not miss any mouse input even during an [INPUT](/qb64wiki/index.php/INPUT "INPUT") entry.
* Use in a loop to monitor the mouse buttons, scroll wheel and coordinate positions.
* To clear all previous mouse data, use \_MOUSEINPUT in a loop until it returns 0.


  




## Examples


*Example 1:* Mouse coordinate, click and scroll events are returned sequentially inside of a \_MOUSEINPUT loop.





| ``` DO   [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") _MOUSEINPUT '      Check the mouse status     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY"), [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(1), [_MOUSEWHEEL](/qb64wiki/index.php/MOUSEWHEEL "MOUSEWHEEL")   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  ``` |
| --- |


*Explanation:* The latest mouse function status can be read after the loop. [\_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") and [\_DELAY](/qb64wiki/index.php/DELAY "DELAY") loops will slow returns down.
  

*Example 2:* How to use a \_MOUSEINPUT loop to locate [PSET](/qb64wiki/index.php/PSET "PSET") positions on a screen using a right mouse button click.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") ' main program loop    ' your program code    [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") _MOUSEINPUT'mouse status changes only     x = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")     y = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x > 0 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x < 640 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y > 0 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y < 480 [THEN](/qb64wiki/index.php/THEN "THEN")       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(2) [THEN](/qb64wiki/index.php/THEN "THEN")         [PSET](/qb64wiki/index.php/PSET "PSET") (x, y), 15         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") x, y       [END IF](/qb64wiki/index.php/END_IF "END IF")     [END IF](/qb64wiki/index.php/END_IF "END IF")   [LOOP](/qb64wiki/index.php/LOOP "LOOP")    ' your program code  [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)  ``` |
| --- |


  

*Example 3:* Clearing any mouse data read before or during an [INPUT](/qb64wiki/index.php/INPUT "INPUT") entry. Press "I" to enter input:





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press I to enter input! Press Q to quit" [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")   K$ = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")([INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"))   [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(1) = -1 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "*"    'indicates a mouse click event   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") _MOUSEINPUT   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") K$ = "Q" [THEN](/qb64wiki/index.php/THEN "THEN") [END](/qb64wiki/index.php/END "END")   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") K$ = "I" [THEN](/qb64wiki/index.php/THEN "THEN")                                          'press I to enter text     [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Click the mouse and enter something: ", entry$   'enter some text     [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") Clickcheck                                        'clear mouse data   [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP")  [END](/qb64wiki/index.php/END "END")  Clickcheck: count = 0 [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")   count = count + 1 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") _MOUSEINPUT [PRINT](/qb64wiki/index.php/PRINT "PRINT") count        'returns the number of loops before mouse data is cleared [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


*Explanation:* Click the mouse a few times while entering [INPUT](/qb64wiki/index.php/INPUT "INPUT") text. When Enter is pressed, the number of loops are displayed.
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1165)
* [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY"), [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON"), [\_MOUSEWHEEL](/qb64wiki/index.php/MOUSEWHEEL "MOUSEWHEEL")
* [\_MOUSESHOW](/qb64wiki/index.php/MOUSESHOW "MOUSESHOW"), [\_MOUSEHIDE](/qb64wiki/index.php/MOUSEHIDE "MOUSEHIDE"), [\_MOUSEMOVE](/qb64wiki/index.php/MOUSEMOVE "MOUSEMOVE")
* [Controller Devices](/qb64wiki/index.php/Controller_Devices "Controller Devices")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MOUSEINPUT&oldid=8914>"




## Navigation menu








### Search





















