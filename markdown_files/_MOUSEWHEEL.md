


\_MOUSEWHEEL - QB64 Phoenix Edition Wiki








# \_MOUSEWHEEL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MOUSEWHEEL function returns a positive or negative [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value indicating mouse scroll events since the last read of [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*scrollAmount%* = \_MOUSEWHEEL
  




## Description


* Returns -1 when scrolling up and 1 when scrolling down with 0 indicating no movement since last read.
* After an event has been read, the value resets to 0 automatically so cumulative position values must be added.
* If no movement on the wheel has occurred since the last [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") read, \_MOUSEWHEEL returns 0.


  




## Availability


* [![v0.851](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v0.851")

**v0.851**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


* Available for *macOS* since **QB64-PE v3.13.0**


  




## Examples


Example 1
Reading the cumulative mouse wheel "clicks".


| ``` [DO](/qb64wiki/index.php/DO "DO")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 50     [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")         Scroll = Scroll + _MOUSEWHEEL         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 20: [PRINT](/qb64wiki/index.php/PRINT "PRINT") Scroll     [LOOP](/qb64wiki/index.php/LOOP "LOOP") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(13) ' press Enter to quit  ``` |
| --- |




---


Example 2
A simple text scrolling routine using the mouse wheel value to read a text array.
You will need a text file that is large enough for this example.


| ``` [DIM](/qb64wiki/index.php/DIM "DIM") Array$(100) [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") "Enter a file name with 100 or more lines of text: ", file$ [OPEN](/qb64wiki/index.php/OPEN "OPEN") file$ [FOR](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [INPUT](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [AS](/qb64wiki/index.php/OPEN "OPEN") #1 [DO UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [EOF](/qb64wiki/index.php/EOF "EOF")(1)     inputcount = inputcount + 1     [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") #1, Array$(inputcount)     [IF](/qb64wiki/index.php/IF "IF") inputcount = 100 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [FOR](/qb64wiki/index.php/FOR "FOR") n = 1 [TO](/qb64wiki/index.php/TO "TO") 21: [PRINT](/qb64wiki/index.php/PRINT "PRINT") Array$(n): [NEXT](/qb64wiki/index.php/NEXT "NEXT") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1 [DO](/qb64wiki/index.php/DO "DO")     [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")         [IF](/qb64wiki/index.php/IF "IF") row >= 0 [THEN](/qb64wiki/index.php/THEN "THEN") row = row + _MOUSEWHEEL [ELSE](/qb64wiki/index.php/ELSE "ELSE") row = 0 'prevent under scrolling         [IF](/qb64wiki/index.php/IF "IF") row > inputcount - 20 [THEN](/qb64wiki/index.php/THEN "THEN") row = inputcount - 20 'prevent over scrolling         [IF](/qb64wiki/index.php/IF "IF") prevrow <> row [THEN](/qb64wiki/index.php/THEN "THEN") 'look for a change in row value             [IF](/qb64wiki/index.php/IF "IF") row > 0 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") row <= inputcount - 20 [THEN](/qb64wiki/index.php/THEN "THEN")                 [CLS](/qb64wiki/index.php/CLS "CLS"): [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 1                 [FOR](/qb64wiki/index.php/FOR "FOR") n = row [TO](/qb64wiki/index.php/TO "TO") row + 20                     [PRINT](/qb64wiki/index.php/PRINT "PRINT") Array$(n)                 [NEXT](/qb64wiki/index.php/NEXT "NEXT")             [END IF](/qb64wiki/index.php/END_IF "END IF")         [END IF](/qb64wiki/index.php/END_IF "END IF")         prevrow = row 'store previous row value     [LOOP](/qb64wiki/index.php/LOOP "LOOP") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") > ""  ``` |
| --- |


Example by Ted Weissgerber
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1302)
* [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY"), [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")
* [\_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT"), [\_MOUSEMOVE](/qb64wiki/index.php/MOUSEMOVE "MOUSEMOVE")
* [\_MOUSESHOW](/qb64wiki/index.php/MOUSESHOW "MOUSESHOW"), [\_MOUSEHIDE](/qb64wiki/index.php/MOUSEHIDE "MOUSEHIDE")
* [Controller Devices](/qb64wiki/index.php/Controller_Devices "Controller Devices")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MOUSEWHEEL&oldid=8927>"




## Navigation menu








### Search





















