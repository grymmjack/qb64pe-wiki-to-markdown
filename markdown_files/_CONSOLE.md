


\_CONSOLE - QB64 Phoenix Edition Wiki








# \_CONSOLE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CONSOLE statement can be used to turn a console window ON/OFF.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


\_CONSOLE {OFF|ON}
\_DEST \_CONSOLE
  




* \_CONSOLE OFF or ON must be used after the [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand") has established that a console window is desired.
* \_CONSOLE OFF turns the console window off once a console has been established using [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"):ON or ONLY.
* \_CONSOLE ON should only be used after the console window has been turned OFF previously.
* [\_DEST](/qb64wiki/index.php/DEST "DEST") \_CONSOLE can be used to send screen output to the console window using QB64 commands such as [PRINT](/qb64wiki/index.php/PRINT "PRINT").
* [\_SCREENHIDE](/qb64wiki/index.php/SCREENHIDE "SCREENHIDE") or [\_SCREENSHOW](/qb64wiki/index.php/SCREENSHOW "SCREENSHOW") can be used to hide or display the main program window.
* The [$SCREENHIDE](/qb64wiki/index.php/$SCREENHIDE "$SCREENHIDE") [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand") can hide the main program window throughout a program when only the console is used.
* **Note:** Text can be copied partially or totally from console screens in Windows by highlighting and using the title bar menu.


To copy console text output, right click the title bar and select *Edit* for *Mark* to highlight and repeat to *Copy*.
  




## Examples


*Example 1:* Hiding and displaying a console window. Use [\_DELAY](/qb64wiki/index.php/DELAY "DELAY") to place console in front of main program window.





| ``` [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") _CONSOLE [OFF](/qb64wiki/index.php/OFF "OFF") 'close original console [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 2 _CONSOLE [ON](/qb64wiki/index.php/ON "ON") 'place console above program window  [_DEST](/qb64wiki/index.php/DEST "DEST") _CONSOLE [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter your name: ", nme$ 'get program input _CONSOLE [OFF](/qb64wiki/index.php/OFF "OFF") 'close console  [_DEST](/qb64wiki/index.php/DEST "DEST") 0 'destination program window [PRINT](/qb64wiki/index.php/PRINT "PRINT") nme$ [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Explanation:* The [destination](/qb64wiki/index.php/DEST "DEST") must be changed with [\_DEST](/qb64wiki/index.php/DEST "DEST") \_CONSOLE to get [INPUT](/qb64wiki/index.php/INPUT "INPUT") from the [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") screen.


---


*Example 2:* [\_CONSOLETITLE](/qb64wiki/index.php/CONSOLETITLE "CONSOLETITLE") can be used to create a console title, but it must be redone every time the console window is restored once turned off:





| ``` [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE")  [_CONSOLETITLE](/qb64wiki/index.php/CONSOLETITLE "CONSOLETITLE") "firstone" [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 10  _CONSOLE [OFF](/qb64wiki/index.php/OFF "OFF") [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 10  _CONSOLE [ON](/qb64wiki/index.php/ON "ON") [_CONSOLETITLE](/qb64wiki/index.php/CONSOLETITLE "CONSOLETITLE") "secondone"  ``` |
| --- |


*Note:* Some versions of Windows may display the program path or Administrator: prefix in console title bars.
  




## See also


* [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"), [\_CONSOLETITLE](/qb64wiki/index.php/CONSOLETITLE "CONSOLETITLE")
* [$SCREENHIDE](/qb64wiki/index.php/$SCREENHIDE "$SCREENHIDE"), [$SCREENSHOW](/qb64wiki/index.php/$SCREENSHOW "$SCREENSHOW") (QB64 [Metacommands](/qb64wiki/index.php/Metacommand "Metacommand"))
* [\_SCREENHIDE](/qb64wiki/index.php/SCREENHIDE "SCREENHIDE"), [\_SCREENSHOW](/qb64wiki/index.php/SCREENSHOW "SCREENSHOW")
* [\_DEST](/qb64wiki/index.php/DEST "DEST"), [\_ECHO](/qb64wiki/index.php/ECHO "ECHO")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CONSOLE&oldid=8455>"




## Navigation menu








### Search





















