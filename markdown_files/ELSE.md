


ELSE - QB64 Phoenix Edition Wiki








# ELSE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
ELSE is used in [IF...THEN](/qb64wiki/index.php/IF...THEN "IF...THEN") or [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") statements to offer an alternative to other conditional statements.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*Single-line syntax:*



[IF](/qb64wiki/index.php/IF "IF") *condition* [THEN](/qb64wiki/index.php/THEN "THEN") *{code}* ELSE *{alternative-code}*
  

*Block syntax:*



[IF](/qb64wiki/index.php/IF "IF") *condition* [THEN](/qb64wiki/index.php/THEN "THEN")
*{code}*
⋮
[ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") *condition2* [THEN](/qb64wiki/index.php/THEN "THEN")
*{code}*
⋮
ELSE
*{alternative-code}*
⋮
[END IF](/qb64wiki/index.php/END_IF "END IF")
  




## Description


* ELSE is used in a IF block statement to cover any remaining conditions not covered in the main block by IF or [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF").
* [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE") covers any remaining conditions not covered by the other CASE statements.
* ELSE can also be used as a false comparison to a true IF statement when a condition will only be true or false.
* Other [IF...THEN](/qb64wiki/index.php/IF...THEN "IF...THEN") statements can be inside of an ELSE statement.


  




## Examples


*Example 1:* One line IF statement





| ```   IF x = 100 THEN PRINT "100" ELSE PRINT "Not 100"   ``` |
| --- |


*Example 2:* Multiple line IF statement block





| ```   IF x = 100 THEN ' code executed MUST be on next statement line!    PRINT "100" ELSE PRINT "Not 100" END IF   ``` |
| --- |


  

*Example 3:* To alternate between any two values (as long as the value after ELSE is the same as the condition)





| ```   IF a = 3 THEN a = 5 ELSE a = 3   ``` |
| --- |


  




## See also


* [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF")
* [IF...THEN](/qb64wiki/index.php/IF...THEN "IF...THEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ELSE&oldid=7268>"




## Navigation menu








### Search





















