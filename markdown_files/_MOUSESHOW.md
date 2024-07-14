


\_MOUSESHOW - QB64 Phoenix Edition Wiki








# \_MOUSESHOW



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MOUSESHOW statement displays the mouse cursor and can change its shape.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_MOUSESHOW [*cursorShape$*]
  




## Description


* Simply use the statement whenever [\_MOUSEHIDE](/qb64wiki/index.php/MOUSEHIDE "MOUSEHIDE") has been used previously.
* In **version 1.000 and up** the following *cursorShape$* can be displayed:


\_MOUSESHOW "LINK" will display an upward pointing hand cursor used to denote hypertext
\_MOUSESHOW "TEXT" will display the I cursor often used in text entry areas
\_MOUSESHOW "CROSSHAIR" will display a crosshair cursor
\_MOUSESHOW "VERTICAL" will display vertical arrow cursor for movement
\_MOUSESHOW "HORIZONTAL" will display horizontal arrow cursor for movement
\_MOUSESHOW "TOPLEFT\_BOTTOMRIGHT" will display bottom diagonal arrow cursor for movement
\_MOUSESHOW "TOPRIGHT\_BOTTOMLEFT" will display bottom diagonal arrow cursor for movement
\_MOUSESHOW "DEFAULT" can be used after a mouse cursor statement above was previously used.
* This statement will also disable [\_MOUSEMOVEMENTX](/qb64wiki/index.php/MOUSEMOVEMENTX "MOUSEMOVEMENTX") or [\_MOUSEMOVEMENTY](/qb64wiki/index.php/MOUSEMOVEMENTY "MOUSEMOVEMENTY") relative mouse movement reads.
* The mouse cursor will not interfere with any print or graphic screen changes in **QB64**.


### QBasic/QuickBASIC


* \_MOUSEHIDE statements do not accumulate like they did with [ABSOLUTE](/qb64wiki/index.php/CALL_ABSOLUTE "CALL ABSOLUTE") or [INTERRUPT](/qb64wiki/index.php/INTERRUPT "INTERRUPT") in QBasic.


  




## Examples


*Example 1:* **QB64 1.000 and up** allow special cursors to be displayed by using special string parameters:





| ``` _MOUSESHOW "default": [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.5 _MOUSESHOW "link": [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.5 'a hand, typically used in web browsers _MOUSESHOW "text": [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.5 _MOUSESHOW "crosshair": [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.5 _MOUSESHOW "vertical": [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.5 _MOUSESHOW "horizontal": [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.5 _MOUSESHOW "topleft_bottomright": [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.5 _MOUSESHOW "topright_bottomleft": [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.5  ``` |
| --- |


**Note:** There is no hourglass, stopwatch or spinning colorful wheel in the list. The fact is that these typically only appear in a program when something has gone terribly wrong and the program has crashed or frozen.
  




## See also


* [\_MOUSEHIDE](/qb64wiki/index.php/MOUSEHIDE "MOUSEHIDE")
* [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")
* [\_MOUSEMOVE](/qb64wiki/index.php/MOUSEMOVE "MOUSEMOVE")
* [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")
* [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")
* [\_MOUSEMOVEMENTX](/qb64wiki/index.php/MOUSEMOVEMENTX "MOUSEMOVEMENTX"), [\_MOUSEMOVEMENTY](/qb64wiki/index.php/MOUSEMOVEMENTY "MOUSEMOVEMENTY")
* [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES"), [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MOUSESHOW&oldid=7144>"




## Navigation menu








### Search





















