


\_FULLSCREEN - QB64 Phoenix Edition Wiki








# \_FULLSCREEN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_FULLSCREEN statement attempts to make the program window fullscreen.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_FULLSCREEN [*\_STRETCH | \_SQUAREPIXELS| \_OFF*][, *\_SMOOTH*]
  




## Parameters


* *\_STRETCH* default first choice attempts to mimic QBasic's full screens if possible. [\_FULLSCREEN (function)](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)") returns 1.
* *\_SQUAREPIXELS* alternate choice enlarges the pixels into squares on some monitors. [\_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)") returns 2
* *\_OFF* turns \_FULLSCREEN off after full screen has been enabled. [\_FULLSCREEN (function)](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)") returns 0.
* Second optional parameter *\_SMOOTH* applies antialiasing to the stretched screen.


  




## Description


* **Set the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode and text [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") when necessary first.** Otherwise there may be desktop view issues.
* \_FULLSCREEN with no parameters chooses *\_STRETCH* or *\_SQUAREPIXELS* (prioritizes \_STRETCH to mimic QBasic if possible)
* **Check the fullscreen mode with the [\_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)") function in your programs when a method is required.**
* It is advisable to get [input](/qb64wiki/index.php/INPUT "INPUT") from the user to confirm that fullscreen was completed or there were possible monitor incompatibilities.
* If fullscreen is **not confirmed** with a [\_FULLSCREEN (function)](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)") return **greater than 0**, then disable with **\_FULLSCREEN \_OFF**.
* **NOTE:** \_FULLSCREEN can also be affected by custom [\_FONT](/qb64wiki/index.php/FONT "FONT") size settings and make program screens too large.


  




## Examples


*Example 1:* Setting the screen mode first prevents enlargement of the desktop before the program window is set:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 _FULLSCREEN [IF](/qb64wiki/index.php/IF "IF") [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)") = 0 [THEN](/qb64wiki/index.php/THEN "THEN") _FULLSCREEN [_OFF](/qb64wiki/index.php/OFF "OFF") 'check that a full screen mode initialized  [LINE](/qb64wiki/index.php/LINE "LINE") (100, 100)-(500, 400), 13, BF  ``` |
| --- |




---


*Example 2:* How fonts and \_FULLSCREEN affect the program's window size.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 [DO](/qb64wiki/index.php/DO "DO")     [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") "Enter MODE 1) ENLARGE WINDOW  2) FULL _SQUAREPIXELS  3) FULL _STRETCH: ", WMODE$     [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [IF](/qb64wiki/index.php/IF "IF") WMODE$ = "1" [THEN](/qb64wiki/index.php/THEN "THEN") [INPUT](/qb64wiki/index.php/INPUT "INPUT") "SIZE 1 TO 9: ", ENLARGE%      [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") ENLARGE%         [CASE](/qb64wiki/index.php/CASE "CASE") 1, 2, 3, 4, 5: STYLE$ = "MONOSPACE, BOLD"         [CASE](/qb64wiki/index.php/CASE "CASE") 6, 7, 8, 9: STYLE$ = "MONOSPACE"         [CASE](/qb64wiki/index.php/CASE "CASE") [ELSE](/qb64wiki/index.php/ELSE "ELSE"): STYLE$ = "MONOSPACE"     [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")      [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") WMODE$         [CASE](/qb64wiki/index.php/CASE "CASE") "1"             full = [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)")             [IF](/qb64wiki/index.php/IF "IF") full > 0 [THEN](/qb64wiki/index.php/THEN "THEN") _FULLSCREEN [_OFF](/qb64wiki/index.php/OFF "OFF")             f& = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("c:\windows\fonts\lucon.ttf", 13 + ENLARGE%, STYLE$)             [_FONT](/qb64wiki/index.php/FONT "FONT") f&         [CASE](/qb64wiki/index.php/CASE "CASE") "2"             _FULLSCREEN [_SQUAREPIXELS](/qb64wiki/index.php/SQUAREPIXELS "SQUAREPIXELS")             full = [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)")             [IF](/qb64wiki/index.php/IF "IF") full = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") FCHECK         [CASE](/qb64wiki/index.php/CASE "CASE") "3"             _FULLSCREEN [_STRETCH](/qb64wiki/index.php/STRETCH "STRETCH")             full = [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)")             [IF](/qb64wiki/index.php/IF "IF") full = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") FCHECK     [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")      mode = [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)")     [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_FULLSCREEN mode ="; mode,     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "PRESS ESC TO END OR ENTER TO CONTINUE..."      [DO](/qb64wiki/index.php/DO "DO"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): B$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"): [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") B$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(13) [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") B$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)      [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") ClearFont  [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") B$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") ClearFont [END](/qb64wiki/index.php/END "END")  FCHECK: Z3 = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") [DO](/qb64wiki/index.php/DO "DO")     [IF](/qb64wiki/index.php/IF "IF") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") < Z3 [THEN](/qb64wiki/index.php/THEN "THEN") Z3 = Z3 - [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")     [IF](/qb64wiki/index.php/IF "IF") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") - Z3 > 4 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO") [LOOP](/qb64wiki/index.php/LOOP "LOOP") full = [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)") [IF](/qb64wiki/index.php/IF "IF") full = 0 [THEN](/qb64wiki/index.php/THEN "THEN") _FULLSCREEN [_OFF](/qb64wiki/index.php/OFF "OFF"): [SOUND](/qb64wiki/index.php/SOUND "SOUND") 100, .75 [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ClearFont: [IF](/qb64wiki/index.php/IF "IF") f& > 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [_FONT](/qb64wiki/index.php/FONT "FONT") 16 'select inbuilt 8x16 default font     [_FREEFONT](/qb64wiki/index.php/FREEFONT "FREEFONT") f& [END IF](/qb64wiki/index.php/END_IF "END IF") [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |




---


*Example 3:* Testing all fullscreen methods.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello, world!" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hit 1 for windowed mode;" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "    2 for _STRETCH" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "    3 for _SQUAREPIXELS" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "    4 for _STRETCH, _SMOOTH" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "    5 for _SQUAREPIXELS, _SMOOTH" [DO](/qb64wiki/index.php/DO "DO")     k$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")     [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") [VAL](/qb64wiki/index.php/VAL "VAL")(k$)         [CASE](/qb64wiki/index.php/CASE "CASE") 1             _FULLSCREEN [_OFF](/qb64wiki/index.php/OFF "OFF")         [CASE](/qb64wiki/index.php/CASE "CASE") 2             _FULLSCREEN [_STRETCH](/qb64wiki/index.php/STRETCH "STRETCH")         [CASE](/qb64wiki/index.php/CASE "CASE") 3             _FULLSCREEN [_SQUAREPIXELS](/qb64wiki/index.php/SQUAREPIXELS "SQUAREPIXELS")         [CASE](/qb64wiki/index.php/CASE "CASE") 4             _FULLSCREEN [_STRETCH](/qb64wiki/index.php/STRETCH "STRETCH") , [_SMOOTH](/qb64wiki/index.php/SMOOTH_(function) "SMOOTH (function)")         [CASE](/qb64wiki/index.php/CASE "CASE") 5             _FULLSCREEN [_SQUAREPIXELS](/qb64wiki/index.php/SQUAREPIXELS "SQUAREPIXELS") , [_SMOOTH](/qb64wiki/index.php/SMOOTH_(function) "SMOOTH (function)")     [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30 [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_EXIT](/qb64wiki/index.php/EXIT_(function) "EXIT (function)") [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")  ``` |
| --- |


  




## See also


* [\_FULLSCREEN (function)](/qb64wiki/index.php/FULLSCREEN_(function) "FULLSCREEN (function)")
* [\_SMOOTH (function)](/qb64wiki/index.php/SMOOTH_(function) "SMOOTH (function)")
* [\_ALLOWFULLSCREEN](/qb64wiki/index.php/ALLOWFULLSCREEN "ALLOWFULLSCREEN")
* [\_FONT](/qb64wiki/index.php/FONT "FONT"), [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")
* [\_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE"), [\_SCREENX](/qb64wiki/index.php/SCREENX "SCREENX"), [\_SCREENY](/qb64wiki/index.php/SCREENY "SCREENY")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FULLSCREEN&oldid=8338>"




## Navigation menu








### Search





















