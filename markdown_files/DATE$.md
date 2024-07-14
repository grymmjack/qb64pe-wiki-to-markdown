


DATE$ - QB64 Phoenix Edition Wiki








# DATE$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The DATE$ function returns the current computer date as a string in the format "mm-dd-yyyy".


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*today$* = DATE$
  




## Description


* Returns the current computer date in the format "mm-dd-yyyy" (e.g., "12-25-2009").


  




## Examples


*Example:* Displaying the weekday and current date.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") DATE$ month$ = [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(DATE$, 2): M = [VAL](/qb64wiki/index.php/VAL "VAL")(month$) day$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(DATE$, 4, 2): D = [VAL](/qb64wiki/index.php/VAL "VAL")(day$) day$ = [STR$](/qb64wiki/index.php/STR$ "STR$")(D)                  ' eliminate any leading zeros year$ = [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(DATE$, 4): Y = [VAL](/qb64wiki/index.php/VAL "VAL")(year$) [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") M    [CASE](/qb64wiki/index.php/CASE "CASE") 1: Moon$ = "January"    [CASE](/qb64wiki/index.php/CASE "CASE") 2: Moon$ = "February"    [CASE](/qb64wiki/index.php/CASE "CASE") 3: Moon$ = "March"    [CASE](/qb64wiki/index.php/CASE "CASE") 4: Moon$ = "April"    [CASE](/qb64wiki/index.php/CASE "CASE") 5: Moon$ = "May"    [CASE](/qb64wiki/index.php/CASE "CASE") 6: Moon$ = "June"    [CASE](/qb64wiki/index.php/CASE "CASE") 7: Moon$ = "July"    [CASE](/qb64wiki/index.php/CASE "CASE") 8: Moon$ = "August"    [CASE](/qb64wiki/index.php/CASE "CASE") 9: Moon$ = "September"    [CASE](/qb64wiki/index.php/CASE "CASE") 10: Moon$ = "October"    [CASE](/qb64wiki/index.php/CASE "CASE") 11: Moon$ = "November"    [CASE](/qb64wiki/index.php/CASE "CASE") 12: Moon$ = "December" [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Today is " + WeekDay$(M, D, Y) + ", " + Moon$ + day$ + ", " + year$ + [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(10)  [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT") A-Z [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") WeekDay$ (M, D, Y) [IF](/qb64wiki/index.php/IF "IF") M < 3 [THEN](/qb64wiki/index.php/THEN "THEN") M = M + 12: Y = Y - 1  'add 12 to Jan - Feb month, -1 year C = Y \ 100: Y = Y [MOD](/qb64wiki/index.php/MOD "MOD") 100           'split century and year number S1 = (C \ 4) - (2 * C) - 1           'century leap S2 = (5 * Y) \ 4                     '4 year leap S3 = 26 * (M + 1) \ 10               'days in months WkDay = (S1 + S2 + S3 + D) [MOD](/qb64wiki/index.php/MOD "MOD") 7     'weekday total remainder [IF](/qb64wiki/index.php/IF "IF") WkDay < 0 [THEN](/qb64wiki/index.php/THEN "THEN") WkDay = WkDay + 7  'Adjust negative results to 0 to 6 [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") WkDay    [CASE](/qb64wiki/index.php/CASE "CASE") 0: day$ = "Sunday"    [CASE](/qb64wiki/index.php/CASE "CASE") 1: day$ = "Monday"    [CASE](/qb64wiki/index.php/CASE "CASE") 2: day$ = "Tuesday"    [CASE](/qb64wiki/index.php/CASE "CASE") 3: day$ = "Wednesday"    [CASE](/qb64wiki/index.php/CASE "CASE") 4: day$ = "Thursday"    [CASE](/qb64wiki/index.php/CASE "CASE") 5: day$ = "Friday"    [CASE](/qb64wiki/index.php/CASE "CASE") 6: day$ = "Saturday" [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT") WeekDay$ = day$ [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Code by Ted Weissgerber


| ``` 06-02-2010 Today is Wednesday, June 2, 2010  ``` |
| --- |


  




## See also


* [TIME$](/qb64wiki/index.php/TIME$ "TIME$"), [IF...THEN](/qb64wiki/index.php/IF...THEN "IF...THEN")
* [VAL](/qb64wiki/index.php/VAL "VAL"), [STR$](/qb64wiki/index.php/STR$ "STR$"), [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)"), [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$"), [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DATE$&oldid=8122>"




## Navigation menu








### Search





















