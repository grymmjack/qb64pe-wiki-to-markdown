


RETURN - QB64 Phoenix Edition Wiki








# RETURN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**RETURN** is used in [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") procedures to return to the original call code line or a specified line label.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 See also](#See_also) |
| --- |


## Syntax


**RETURN** [{*linelabel*|*linenumber*}]
  




## Parameters


* RETURN without parameters returns to the code immediately following the original [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") call.
* *line number* or *linelabel* after the RETURN statement returns code execution to that label.


  

*Usage:*



* Normally required at the end of a [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") procedure unless the procedure returns using a loop.
* RETURN is not used in error handling procedures. Error procedures use [RESUME](/qb64wiki/index.php/RESUME "RESUME") *line number* or [RESUME NEXT](/qb64wiki/index.php/RESUME "RESUME").
* GOSUB procedures use line numbers or line labels designated with a colon after the number or label.
* If RETURN is encountered without a previous [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") call a ["RETURN without GOSUB" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") is produced.
* To avoid errors, place [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") procedures AFTER the main program code [END](/qb64wiki/index.php/END "END") or after an [EXIT SUB](/qb64wiki/index.php/EXIT_SUB "EXIT SUB") or [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION") call.


  



*Example 1:* Returns after a Gosub.





| ``` [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") a = 1 [TO](/qb64wiki/index.php/TO "TO") 10 [PRINT](/qb64wiki/index.php/PRINT "PRINT") a [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") a = 5 [THEN](/qb64wiki/index.php/THEN "THEN") [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") five [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")       'END or SYSTEM stop the program before the execution of a sub procedure  five: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Aha! Five!" RETURN  ``` |
| --- |




| ```  1  2  3  4  5 Aha! Five!  6  7  8  9  10  ``` |
| --- |


  

*Example 2:* Returns to a specific line label.





| ``` [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") hey [PRINT](/qb64wiki/index.php/PRINT "PRINT") "it didn't go here." hoho: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "it went here." [END](/qb64wiki/index.php/END "END")  hey: RETURN hoho  ``` |
| --- |


Code by Cyperium


| ``` it went here.  ``` |
| --- |


  




## See also


* [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB"), [GOTO](/qb64wiki/index.php/GOTO "GOTO")
* [RESUME](/qb64wiki/index.php/RESUME "RESUME")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RETURN&oldid=7943>"




## Navigation menu








### Search





















