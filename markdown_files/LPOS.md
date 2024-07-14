


LPOS - QB64 Phoenix Edition Wiki








# LPOS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The LPOS function returns the current LPT printer head position.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result%* = LPOS(*index%*)
  




## Description


* *index%* is the index of the printer, which can have the following values:
	+ 0 - LPT1:
	+ 1 - LPT1:
	+ 2 - LPT2:
	+ 3 - LPT3:
* The LPOS function does not necessarily give the physical position of the print head because it does not expand tab characters. In addition, some printers may buffer characters.


  




## Examples


Prompts the user for team names and the names of players on each team. It then prints the players and their teams on the printer.


| ``` [CLS](/qb64wiki/index.php/CLS "CLS") [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT") "Team Members"; [TAB](/qb64wiki/index.php/TAB "TAB")(76); "TEAM" : [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT") [INPUT](/qb64wiki/index.php/INPUT "INPUT") "How many teams"; TEAMS [INPUT](/qb64wiki/index.php/INPUT "INPUT") "How many players per team";PPT [PRINT](/qb64wiki/index.php/PRINT "PRINT") [FOR](/qb64wiki/index.php/FOR "FOR") T = 1 TO TEAMS     [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Team name: ", TEAM$     [FOR](/qb64wiki/index.php/FOR "FOR") P = 1 TO PPT         [INPUT](/qb64wiki/index.php/INPUT "INPUT") "   Enter player name: ", PLAYER$         [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT") PLAYER$;         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") P < PPT [THEN](/qb64wiki/index.php/THEN "THEN")             [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") LPOS(0) > 55 [THEN](/qb64wiki/index.php/THEN "THEN") ' Print a new line if print head past column 55.                 [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT") : [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT") [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(5);             [ELSE](/qb64wiki/index.php/ELSE "ELSE")                 [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT") ", ";         'Otherwise, print a comma.             [END](/qb64wiki/index.php/END "END") IF         [END](/qb64wiki/index.php/END "END") IF     [NEXT](/qb64wiki/index.php/NEXT "NEXT") P [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT") [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(80 - LPOS(0) - [LEN](/qb64wiki/index.php/LEN "LEN")(TEAM$),"."); TEAM$ [NEXT](/qb64wiki/index.php/NEXT "NEXT") T  ``` |
| --- |


  




## See also


* [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LPOS&oldid=658>"




## Navigation menu








### Search





















