


TIME$ - QB64 Phoenix Edition Wiki








# TIME$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **TIME$** Function returns a [STRING](/qb64wiki/index.php/STRING "STRING") representation of the current computer time in a 24 hour format.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


PRINT "Present time = "; **TIME$**
  




## Description


* Returns the present computer time in hh:mm:ss 24 hour format: "19:20:33"
* Uses 2 colon (:) separators between hours, minutes and seconds
* Hour values range from "00" to "23" starting from midnite.
* Minutes and seconds range from "00" to "59"
* Continuous TIME$ calls may lag if a QBasic program is minimized to the taskbar!


  




## Examples


*Example 1:* A simple clock using [DRAW](/qb64wiki/index.php/DRAW "DRAW") with Turn Angle.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [DO](/qb64wiki/index.php/DO "DO")     [CLS](/qb64wiki/index.php/CLS "CLS")     t$ = TIME$: h = [VAL](/qb64wiki/index.php/VAL "VAL")(t$): m = [VAL](/qb64wiki/index.php/VAL "VAL")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(t$, 4, 2)): s = [VAL](/qb64wiki/index.php/VAL "VAL")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(t$, 7, 2))     [PRINT](/qb64wiki/index.php/PRINT "PRINT") t$     [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") [STEP](/qb64wiki/index.php/STEP "STEP")(0, 0), 200, 8     [DRAW](/qb64wiki/index.php/DRAW "DRAW") "c12ta" + [STR$](/qb64wiki/index.php/STR$ "STR$")((h [MOD](/qb64wiki/index.php/MOD "MOD") 12) * -30) + "nu133"     [DRAW](/qb64wiki/index.php/DRAW "DRAW") "c14ta" + [STR$](/qb64wiki/index.php/STR$ "STR$")(m * -6) + "nu200"     [DRAW](/qb64wiki/index.php/DRAW "DRAW") "c9ta" + [STR$](/qb64wiki/index.php/STR$ "STR$")(s * -6) + "nu200"     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 1 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)  ``` |
| --- |


Code by Galleon
Explanation: Note that [VAL](/qb64wiki/index.php/VAL "VAL")(TIME$) can just return the hour number 0 to 23 as the read stops at the first colon.
  

*Example 2:* The following Function converts TIME$ to normal 12 hour AM-PM digital clock format.





| ``` PRINT TIME$ PRINT Clock$  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") Clock$ hour$ = [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(TIME$, 2): H% = [VAL](/qb64wiki/index.php/VAL "VAL")(hour$) min$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(TIME$, 3, 3) IF H% >= 12 THEN ampm$ = " PM" ELSE ampm$ = " AM" IF H% > 12 THEN   IF H% - 12 < 10 THEN hour$ = [STR$](/qb64wiki/index.php/STR$ "STR$")(H% - 12) ELSE hour$ = [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(H% - 12)) ELSEIF H% = 0 THEN hour$ = "12"          ' midnight hour ELSE : IF H% < 10 THEN hour$ = [STR$](/qb64wiki/index.php/STR$ "STR$")(H%)  ' eliminate leading zeros END IF Clock$ = hour$ + min$ + ampm$ END FUNCTION  ``` |
| --- |




| ``` 14:13:36  2:13 PM  ``` |
| --- |


*Explanation:* When hours are less than 10 (but not 0), [STR$](/qb64wiki/index.php/STR$ "STR$")(H%) alone keeps a space ahead of the hour. For 2 digit hours, [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$") is used to remove that leading space. For the hours of 10 AM to 12 PM, the hour [STRING](/qb64wiki/index.php/STRING "STRING") value is passed from [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(TIME$, 2) at the beginning of the function.
  




## See also


* [TIMER (function)](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")
* [DATE$](/qb64wiki/index.php/DATE$ "DATE$"), [IF...THEN](/qb64wiki/index.php/IF...THEN "IF...THEN")
* [VAL](/qb64wiki/index.php/VAL "VAL"), [STR$](/qb64wiki/index.php/STR$ "STR$"), [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)")
* [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$"), [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=TIME$&oldid=8175>"




## Navigation menu








### Search





















