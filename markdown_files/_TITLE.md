


\_TITLE - QB64 Phoenix Edition Wiki








# \_TITLE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_TITLE statement provides the program name in the title bar of the program window.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_TITLE *text$*
  




## Parameters


* *text$* can be any literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") or [ASCII](/qb64wiki/index.php/ASCII "ASCII") character value.


  




## Description


* The title can be changed anywhere in a program procedure.
* The title bar will say "Untitled" if a title is not set.
* Change the title of the [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") windows created using [\_CONSOLETITLE](/qb64wiki/index.php/CONSOLETITLE "CONSOLETITLE")
* **Note: A [delay](/qb64wiki/index.php/DELAY "DELAY") may be required before the title can be set.** See [\_SCREENEXISTS](/qb64wiki/index.php/SCREENEXISTS "SCREENEXISTS").


  




## Examples


*Example 1:* How to create the window title bar.





| ``` _TITLE "My New Program"  ``` |
| --- |


  

*Example 2:* How to find the currently running program module name and current path using a Windows API Library.





| ``` _TITLE "My program" [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 5             '5 second delay  _TITLE [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(TITLE$, 1, [INSTR](/qb64wiki/index.php/INSTR "INSTR")(TITLE$, ".") - 1)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") PATH$   [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") TITLE$ '=== SHOW CURRENT PROGRAM [SHARED](/qb64wiki/index.php/SHARED "SHARED") PATH$ [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") 'Directory Information using KERNEL32 provided by Dav   [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") GetModuleFileNameA ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") Module [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), FileName [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") nSize [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")) [END DECLARE](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")  FileName$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(256) Result = GetModuleFileNameA(0, FileName$, [LEN](/qb64wiki/index.php/LEN "LEN")(FileName$)) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Result [THEN](/qb64wiki/index.php/THEN "THEN")   PATH$ = [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(FileName$, Result)   start = 1   DO     posit = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(start, PATH$, "\")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") posit [THEN](/qb64wiki/index.php/THEN "THEN") last = posit     start = posit + 1   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") posit = 0   TITLE$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(PATH$, last + 1)   PATH$ = [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(PATH$, last) [ELSE](/qb64wiki/index.php/ELSE "ELSE") TITLE$ = "": PATH$ = "" [END IF](/qb64wiki/index.php/END_IF "END IF") [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


*Note:* The actual module file name is returned. Not necessarily the Title value. The value returned can be used however.
  




## See also


* [\_TITLE$](/qb64wiki/index.php/TITLE$ "TITLE$")
* [\_ICON](/qb64wiki/index.php/ICON "ICON")
* [\_DELAY](/qb64wiki/index.php/DELAY "DELAY")
* [ASCII](/qb64wiki/index.php/ASCII "ASCII")
* [\_CONSOLETITLE](/qb64wiki/index.php/CONSOLETITLE "CONSOLETITLE")
* [\_SCREENEXISTS](/qb64wiki/index.php/SCREENEXISTS "SCREENEXISTS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=TITLE&oldid=8176>"




## Navigation menu








### Search





















