


LSET - QB64 Phoenix Edition Wiki








# LSET



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
LSET left-justifies a fixed length string expression based on the size of the [STRING](/qb64wiki/index.php/STRING "STRING") variable and string expression.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


LSET {stringVariable = stringExpression | stringExpression1 = stringExpression2}
  




## Description


* If the string expression is longer than a fixed length string variable the value is truncated from the right side in LSET or [RSET](/qb64wiki/index.php/RSET "RSET").
* If the LSET string expression is smaller, spaces will occupy the extra positions to the right in the string.
* LSET can be used with a [FIELD](/qb64wiki/index.php/FIELD "FIELD") or [TYPE](/qb64wiki/index.php/TYPE "TYPE") definition to set the buffer position before a [PUT](/qb64wiki/index.php/PUT "PUT").


  




## Examples


*Example 1:* Using LSET with a [FIELD](/qb64wiki/index.php/FIELD "FIELD") definition. Note: May create an empty (unchanged) file that can be deleted.





| ``` [OPEN](/qb64wiki/index.php/OPEN "OPEN") "testfile.dat" FOR [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") AS #1 [LEN](/qb64wiki/index.php/LEN "LEN") = 15 [FIELD](/qb64wiki/index.php/FIELD "FIELD") 1, 6 [AS](/qb64wiki/index.php/AS "AS") a$, 9 [AS](/qb64wiki/index.php/AS "AS") other$ [FIELD](/qb64wiki/index.php/FIELD "FIELD") 1, 2 [AS](/qb64wiki/index.php/AS "AS") b$, 13 [AS](/qb64wiki/index.php/AS "AS") another$ LSET a$ = "1234567890" LSET other$ = "1234567890" [PRINT](/qb64wiki/index.php/PRINT "PRINT") a$, b$, other$, another$ [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1   ``` |
| --- |




| ``` 123456            12         123456789     3456123456789  ``` |
| --- |


  

*Example 2:* How LSET can define two different string length values in one statement.





| ```   [TYPE](/qb64wiki/index.php/TYPE "TYPE") ninestring head [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 9 [END TYPE](/qb64wiki/index.php/END_TYPE "END TYPE")  [TYPE](/qb64wiki/index.php/TYPE "TYPE") fivestring head AS [STRING](/qb64wiki/index.php/STRING "STRING") * 5 [END TYPE](/qb64wiki/index.php/END_TYPE "END TYPE")  [DIM](/qb64wiki/index.php/DIM "DIM") me [AS](/qb64wiki/index.php/AS "AS") ninestring, you [AS](/qb64wiki/index.php/AS "AS") fivestring me.head = "ACHES NOT" [CLS](/qb64wiki/index.php/CLS "CLS")  LSET you.head = me.head [PRINT](/qb64wiki/index.php/PRINT "PRINT") "me.head: "; me.head [PRINT](/qb64wiki/index.php/PRINT "PRINT") "you.head: "; you.head  ``` |
| --- |




| ``` me.head: ACHES NOT you.head: ACHES  ``` |
| --- |


  




## See also


* [RSET](/qb64wiki/index.php/RSET "RSET"), [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$")
* [FIELD](/qb64wiki/index.php/FIELD "FIELD"), [TYPE](/qb64wiki/index.php/TYPE "TYPE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LSET&oldid=6084>"




## Navigation menu








### Search





















