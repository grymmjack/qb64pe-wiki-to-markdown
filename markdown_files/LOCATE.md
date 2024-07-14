


LOCATE - QB64 Phoenix Edition Wiki








# LOCATE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The LOCATE statement locates the screen text row and column positions for a [PRINT](/qb64wiki/index.php/PRINT "PRINT") or [INPUT](/qb64wiki/index.php/INPUT "INPUT") procedure.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


LOCATE [*row%*][, *column%*] [, *cursor%*][, *cursorStart%*, *cursorStop%*]
  




## Parameters


* optional text *row%* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values are from 1 to 25, 43 or 50 in [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 and 25 in most other legacy graphic screen modes, except screens 11 and 12 which can have 30 or 60 rows.
* optional *column%* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values are from 1 to 40 or 80 in [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 and 80 in all other legacy screen modes.
* optional *cursor%* value can be 0 to turn displaying the cursor off or 1 to turn it on.
* optional *cursorStart%* and *cursorStop%* values define the shape of the cursor by setting the start and stop scanline (values range from 0 to 31) for the cursor character.


  




## Description


* [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") statement can be used to determine the text width and height in [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 and height of 30 or 60 in [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 11 or 12.
* In [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") graphic screen the number of text *rows* are calculated as [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") \ 16 except when a [\_FONT](/qb64wiki/index.php/FONT "FONT") is used. Use [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT") to calculate font rows.
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") graphic screen text *columns* are calculated as [\_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") \ 8 except when a [\_FONT](/qb64wiki/index.php/FONT "FONT") is used. Use [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH") to measure a line of font text.
	+ Additionally, when a variable width [\_FONT](/qb64wiki/index.php/FONT "FONT") is active, then the *columns* are not counted as char positions anymore but as pixel positions instead.
* The text *row* position is not required if the [PRINT](/qb64wiki/index.php/PRINT "PRINT") is going to be on the next row. The [comma](/qb64wiki/index.php/Comma "Comma") and a *column* value are required to set the column.
* If only the *row* parameter is given, then the column position remains the same. **Neither *row* or *column* parameter can be 0.**
* When [PRINTing](/qb64wiki/index.php/PRINT "PRINT") on the bottom 2 *rows*, use a [semicolon](/qb64wiki/index.php/Semicolon "Semicolon") after the PRINT expression to avoid a screen roll.
* If the *cursorStart%* line is given, the *cursorStop%* line must also be given. A wider range between them produces a taller cursor.
* If you use LOCATE beyond the current number of rows in text mode, QB64 will try to adapt the screen instead of tossing an error.
* When writing to the console, only the *row* and *column* arguments are used, all others are ignored. Furthermore, on non-Windows systems LOCATE statements that do not give both a *row* and *column* will be ignored entirely.


  




## Examples


*Example:* Moving the cursor around (now you can finally create a Commodore 64 emulator!). **Default SCREEN 0 only:**





| ``` crx = 10 cry = 10 [DO](/qb64wiki/index.php/DO "DO")     LOCATE cry, crx, 1, 0, 8     a$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")     [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") a$         [CASE](/qb64wiki/index.php/CASE "CASE") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "H": [IF](/qb64wiki/index.php/IF "IF") cry > 1 [THEN](/qb64wiki/index.php/THEN "THEN") cry = cry - 1 'up         [CASE](/qb64wiki/index.php/CASE "CASE") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "P": [IF](/qb64wiki/index.php/IF "IF") cry < 25 [THEN](/qb64wiki/index.php/THEN "THEN") cry = cry + 1 'down         [CASE](/qb64wiki/index.php/CASE "CASE") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "K": [IF](/qb64wiki/index.php/IF "IF") crx > 1 [THEN](/qb64wiki/index.php/THEN "THEN") crx = crx - 1 'left         [CASE](/qb64wiki/index.php/CASE "CASE") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "M": [IF](/qb64wiki/index.php/IF "IF") crx < 80 [THEN](/qb64wiki/index.php/THEN "THEN") crx = crx + 1 'right         [CASE](/qb64wiki/index.php/CASE "CASE") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27): [END](/qb64wiki/index.php/END "END")     [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT") [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


Explanation: The CHR$(0) + "H", "P", "K", "M" represents the cursor arrow keys. start = 0, stop = 8 is the tallest cursor, experiment with the start and stop values for different effects (start = 8, stop = 8 is the default producing a \_ cursor).
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1218)
* [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN"), [POS](/qb64wiki/index.php/POS "POS") (cursor position)
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [COLOR](/qb64wiki/index.php/COLOR "COLOR")
* [INPUT](/qb64wiki/index.php/INPUT "INPUT"), [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT"), [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$") (keyboard input)
* [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH"), [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$"), [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LOCATE&oldid=8903>"




## Navigation menu








### Search





















