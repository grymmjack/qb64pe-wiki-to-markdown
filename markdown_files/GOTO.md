


GOTO - QB64 Phoenix Edition Wiki








# GOTO



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The GOTO statement sends the procedure to a line label or a line number in the program.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


GOTO {*lineNumber*|*lineLabel*}
  

***IF** Syntax:*



IF condition GOTO {*lineNumber*|*lineLabel*}
  




## Description


* *lineNumber* or *lineLabel* must already exist or an IDE status error will be displayed until it is created.
* Can be used in [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures using their own line labels or numbers.
* The frequent use of GOTO statements can become confusing when trying to follow the code and it could also cause endless loops.
* GOTO is an easy trap for new programmers. Use loops instead when possible.


  




## Examples


*Example:*





| ``` 1 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "first line": GOTO gohere 2 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "second line": GOTO 3  gohere: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "third line" GOTO 2  3 [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ``` first line third line second line  ``` |
| --- |


*Explanation:* After it prints "first line" it goes to the line label "gohere" where it prints "third line", then it goes to the line that is numbered "2" and prints "second line" and goes to line number 3 and an [END](/qb64wiki/index.php/END "END") statement which ends the program.
  




## See also


* [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB"), [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR")
* [ON...GOTO](/qb64wiki/index.php/ON...GOTO "ON...GOTO"), [ON...GOSUB](/qb64wiki/index.php/ON...GOSUB "ON...GOSUB")
* [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP"), [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")
* [IF...THEN](/qb64wiki/index.php/IF...THEN "IF...THEN"), [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE")
* [Line numbers and labels](/qb64wiki/index.php/Line_number "Line number")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=GOTO&oldid=6021>"




## Navigation menu








### Search





















