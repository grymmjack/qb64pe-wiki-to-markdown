


TIMER - QB64 Phoenix Edition Wiki








# TIMER



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
A **TIMER** statement enables, turns off or stops timer event trapping. QBasic only uses the base timer, but **QB64** can run many.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


QuickBASIC
TIMER {ON|STOP|OFF}
QB64
TIMER(*number%*) {ON|STOP|OFF|FREE}
  




## Parameters


* *number* denotes a specific numbered timer event in **QB64 only**. QB64 can run many timer events at once including the base timer.
* TIMER ON enables event trapping of an [ON TIMER(n)](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)") statement. While enabled, a check is made after every code statement to see if the specified time has elapsed and the ON TIMER [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") (or [SUB](/qb64wiki/index.php/SUB "SUB") in QB64) procedure is executed.
* TIMER STOP disables timer event trapping. When an event occurs while stopped, it is remembered. If timer events are turned back on later, any remembered events are immediately executed.
* TIMER OFF turns timer event trapping completely off and no subsequent events are remembered.


**QB64 only**
* Get a TIMER number from [\_FREETIMER](/qb64wiki/index.php/FREETIMER "FREETIMER") ONLY except when the base timer(no number or 0) is used. Use specific variables or an array to hold each event number value for later reference.
* If the TIMER number is omitted or 0, the TIMER used is the base timer.
* Specific TIMER events can be enabled, suspended, turned off or freed using TIMER(n) ON, STOP, OFF or FREE.
* TIMER(n) **FREE** clears a specific timer event when it is no longer needed. **The base TIMER or TIMER(0) cannot be freed!**


**QB64 Timing Alternatives**
* The [TIMER (function)](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") can be used to find timed intervals down to 1 millisecond(.001) accuracy.
* The [\_DELAY](/qb64wiki/index.php/DELAY "DELAY") statement can be used to delay program execution for intervals down to milliseconds.
* [\_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") can slow down loops to a specified number of frames per second. This can also alleviate a program's CPU usage.


  




## Examples


*Example:* How to update the time while [printing](/qb64wiki/index.php/PRINT "PRINT") at the same time in a program.





| ```   TIMER ON ' enable timer event trapping   LOCATE 4, 2 ' set the starting PRINT position   [ON TIMER](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)")(10) GOSUB Clock ' set procedure execution repeat time   DO WHILE INKEY$ = "": PRINT "A"; : SLEEP 6: LOOP   TIMER OFF   [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")   Clock:   row = [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN") ' Save current print cursor row.   col = [POS(0)](/qb64wiki/index.php/POS "POS") ' Save current print cursor column.   LOCATE 2, 37: PRINT [TIME$](/qb64wiki/index.php/TIME$ "TIME$"); ' print current time at top of screen.   LOCATE row, col ' return to last print cursor position  [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


NOTE: SLEEP will be interrupted in QBasic.
  




## See also


* [ON TIMER(n)](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)"), [TIMER (function)](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")
* [\_DELAY](/qb64wiki/index.php/DELAY "DELAY"), [\_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=TIMER&oldid=8072>"




## Navigation menu








### Search





















