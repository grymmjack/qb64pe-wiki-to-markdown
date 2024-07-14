


$CONSOLE - QB64 Phoenix Edition Wiki








# $CONSOLE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $CONSOLE [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand") creates a console window that can be used throughout a QB64 program module.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


$CONSOLE[:ONLY]
  




## Description


* [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") **ON** or **OFF** may be used to show or hide the console window at run time.
* The **:ONLY** option can be used when only a console window is desired without a program window.
* [\_DEST](/qb64wiki/index.php/DEST "DEST") [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") may be used to send screen output to the console window.
* [\_SCREENHIDE](/qb64wiki/index.php/SCREENHIDE "SCREENHIDE") and [\_SCREENSHOW](/qb64wiki/index.php/SCREENSHOW "SCREENSHOW") can be used to hide or show the main program window.
* [\_DELAY](/qb64wiki/index.php/DELAY "DELAY") or [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") can be used to allow the console window to be set in front of the main program window.
* **QB64 [Metacommands](/qb64wiki/index.php/Metacommand "Metacommand") are not commented out with ' or REM, unlike QuickBASIC metacommands**
* Change the title of the $CONSOLE windows created using [\_CONSOLETITLE](/qb64wiki/index.php/CONSOLETITLE "CONSOLETITLE")
* **Note:** Text can be copied partially or totally from console screens in Windows by highlighting and using the title bar menu.


To copy console text output, right click the title bar and select *Edit* for *Mark* to highlight and repeat to *Copy*
  




## Examples


*Example 1:* Hiding and displaying a console window. Use [\_DELAY](/qb64wiki/index.php/DELAY "DELAY") to place console in front of main program window.





| ``` $CONSOLE [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 4  [_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") [OFF](/qb64wiki/index.php/OFF "OFF") [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 4 [_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") [ON](/qb64wiki/index.php/ON "ON")  [_DEST](/qb64wiki/index.php/DEST "DEST") [_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Close this console window or click main window and press a key!"  ``` |
| --- |




---


*Example 2:* How to use a Console window to copy screen output using the *Edit* menu by right clicking the console title bar.





| ``` $CONSOLE [_DEST](/qb64wiki/index.php/DEST "DEST") [_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")  c&& = -1: d& = -1: e% = -1: f%% = -1 hx$ = [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(f%%) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Max hex _BYTE = "; hx$; " with"; [LEN](/qb64wiki/index.php/LEN "LEN")(hx$); "digits ="; [VAL](/qb64wiki/index.php/VAL "VAL")("&H" + hx$) hx$ = [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(e%) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Max hex INTEGER = "; hx$; " with"; [LEN](/qb64wiki/index.php/LEN "LEN")(hx$); "digits ="; [VAL](/qb64wiki/index.php/VAL "VAL")("&H" + hx$) hx$ = [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(d&) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Max hex LONG = "; hx$; " with"; [LEN](/qb64wiki/index.php/LEN "LEN")(hx$); "digits ="; [VAL](/qb64wiki/index.php/VAL "VAL")("&H" + hx$) hx$ = [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(c&&) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Max hex _INTEGER64 = "; hx$; " with"; [LEN](/qb64wiki/index.php/LEN "LEN")(hx$); "digits ="; [VAL](/qb64wiki/index.php/VAL "VAL")("&H" + hx$) hx$ = [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(9223372036854775807) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Max _INTEGER64 value = "; hx$; " with"; [LEN](/qb64wiki/index.php/LEN "LEN")(hx$); "digits" hx$ = [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(-9223372036854775808) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Min _INTEGER64 value = "; hx$; " with"; [LEN](/qb64wiki/index.php/LEN "LEN")(hx$); "digits"  ``` |
| --- |




| ``` Max hex _BYTE = FF with 2 digits = 255 Max hex INTEGER = FFFF with 4 digits = 65535 Max hex LONG = FFFFFFFF with 8 digits = 4294967295 Max hex _INTEGER64 = FFFFFFFFFFFFFFFF with 16 digits =-1 Max _INTEGER64 value = 7FFFFFFFFFFFFFFF with 16 digits Min _INTEGER64 value = 8000000000000000 with 16 digits  ``` |
| --- |


*Console:* Right click and select *Edit* > *Select All* (mouse highlight after) then hit Enter or select *Edit* > *Copy* to the clipboard.


| ``` Max hex _BYTE = FF with 2 digits = 255 Max hex INTEGER = FFFF with 4 digits = 65535 Max hex LONG = FFFFFFFF with 8 digits = 4294967295 Max hex _INTEGER64 = FFFFFFFFFFFFFFFF with 16 digits =-1  ``` |
| --- |


*Copied text:* The above text was copied after *Select All* was selected and the smaller area was re-highlighted with the mouse.
  




## See also


* [\_CLIPBOARD$ (function)](/qb64wiki/index.php/CLIPBOARD$_(function) "CLIPBOARD$ (function)"), [\_CLIPBOARD$](/qb64wiki/index.php/CLIPBOARD$ "CLIPBOARD$") (statement)
* [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE"), [\_ECHO](/qb64wiki/index.php/ECHO "ECHO")
* [$SCREENHIDE](/qb64wiki/index.php/$SCREENHIDE "$SCREENHIDE"), [$SCREENSHOW](/qb64wiki/index.php/$SCREENSHOW "$SCREENSHOW") (QB64 [Metacommands](/qb64wiki/index.php/Metacommand "Metacommand"))
* [\_SCREENHIDE](/qb64wiki/index.php/SCREENHIDE "SCREENHIDE"), [\_SCREENSHOW](/qb64wiki/index.php/SCREENSHOW "SCREENSHOW")
* [C Console Library](/qb64wiki/index.php/C_Libraries#Console_Window "C Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$CONSOLE&oldid=8456>"




## Navigation menu








### Search





















