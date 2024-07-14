


GOSUB - QB64 Phoenix Edition Wiki








# GOSUB



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
GOSUB sends the program flow to a sub procedure identified by a line number or label.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


GOSUB {*lineNumber*|*label*}
  




## Description


* Use [RETURN](/qb64wiki/index.php/RETURN "RETURN") in a sub procedure to return to the next line of code after the original GOSUB call. [END](/qb64wiki/index.php/END "END") or [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM") can also be used to end program.
* GOSUB and GOTO can be used **within** [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures, but cannot refer to a label located outside the procedure.


### QBasic/QuickBASIC


* Too many GOSUBs without a [RETURN](/qb64wiki/index.php/RETURN "RETURN") can eventually cause "Out of Stack Errors" in QBasic as each GOSUB uses memory to store the location to return to. Each [RETURN](/qb64wiki/index.php/RETURN "RETURN") frees the memory of the GOSUB it returns to.


  




## Examples


*Example:* Simple usage of GOSUB





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "1. It goes to the subroutine." GOSUB subroutine [PRINT](/qb64wiki/index.php/PRINT "PRINT") "3. And it returns." [END](/qb64wiki/index.php/END "END")  subroutine: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "2. It is at the subroutine." [RETURN](/qb64wiki/index.php/RETURN "RETURN")   ``` |
| --- |


Code by Cyperium


| ``` 1. It goes to the subroutine. 2. It is at the subroutine. 3. And it returns.  ``` |
| --- |


  



  

*Example:* What happens if two GOSUB executes then two RETURN's?





| ``` start:  a = a + 1 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") a = 1 [THEN](/qb64wiki/index.php/THEN "THEN") GOSUB here: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "It returned to IF a = 1": [END](/qb64wiki/index.php/END "END") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") a = 2 [THEN](/qb64wiki/index.php/THEN "THEN") GOSUB there: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "It returned to IF a = 2": [RETURN](/qb64wiki/index.php/RETURN "RETURN")    here: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "It went here." [GOTO](/qb64wiki/index.php/GOTO "GOTO") start  there: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "It went there." [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


Code by Cyperium


| ``` It went here. It went there. It returned to IF a = 2 It returned to IF a = 1  ``` |
| --- |


*Explanation:* When a = 1 it uses GOSUB to go to "here:", then it uses GOTO to go back to "start:". a is increased by one so when a = 2 it uses GOSUB to go to "there:", and uses RETURN to go the last GOSUB (which is on the IF a = 2 line), it then encounters another RETURN which makes it return to the first GOSUB call we used on the IF a = 1 line.


  




## See also


* [ON...GOSUB](/qb64wiki/index.php/ON...GOSUB "ON...GOSUB")
* [ON...GOTO](/qb64wiki/index.php/ON...GOTO "ON...GOTO"), [GOTO](/qb64wiki/index.php/GOTO "GOTO")
* [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR"), [RESUME](/qb64wiki/index.php/RESUME "RESUME")
* [ON TIMER(n)](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)")
* [Line number](/qb64wiki/index.php/Line_number "Line number")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=GOSUB&oldid=8038>"




## Navigation menu








### Search





















