


\_CONSOLEINPUT - QB64 Phoenix Edition Wiki








# \_CONSOLEINPUT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CONSOLEINPUT function is used to monitor any new mouse or keyboard input coming from a $CONSOLE window. It must be called in order for [\_CINP](/qb64wiki/index.php/CINP "CINP") to return valid values. Windows-only.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*infoExists%%* = \_CONSOLEINPUT
  




## Description


* Returns 1 if new keyboard information is available, 2 if mouse information is available, otherwise it returns 0.
* Must be called before reading any of the other mouse functions and before reading [\_CINP](/qb64wiki/index.php/CINP "CINP").
* To clear all previous input data, read \_CONSOLEINPUT in a loop until it returns 0.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Examples


*Example 1:* Reading individual key strokes from a console window (Windows).





| ``` [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"):[ONLY](/qb64wiki/index.php/ONLY "ONLY") [_DEST](/qb64wiki/index.php/DEST "DEST") [_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE"): [_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") [_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press any key, and I'll give you the scan code for it.  <ESC> quits the demo." [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [DO](/qb64wiki/index.php/DO "DO")     x = _CONSOLEINPUT     [IF](/qb64wiki/index.php/IF "IF") x = 1 [THEN](/qb64wiki/index.php/THEN "THEN") 'read only keyboard input ( = 1)         c = [_CINP](/qb64wiki/index.php/CINP "CINP")         [PRINT](/qb64wiki/index.php/PRINT "PRINT") c;     [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") c = 1 [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"), [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")
* [\_CINP](/qb64wiki/index.php/CINP "CINP"), [Scan Codes](/qb64wiki/index.php/Keyboard_scancodes#INP_Scan_Codes "Keyboard scancodes")
* [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY"), [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON"), [\_MOUSEWHEEL](/qb64wiki/index.php/MOUSEWHEEL "MOUSEWHEEL")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CONSOLEINPUT&oldid=8291>"




## Navigation menu








### Search





















