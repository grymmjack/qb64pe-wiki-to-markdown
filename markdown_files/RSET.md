


RSET - QB64 Phoenix Edition Wiki








# RSET



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **RSET** statement right-justifies a string according to length of the string expression.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


RSET string\_variable = string\_expression
  




* If the *string\_expression* is longer than a fixed length string variable the value is truncated from the right side in [LSET](/qb64wiki/index.php/LSET "LSET") or RSET.
* If the *string\_expression* is smaller than the fixed length, spaces will occupy the extra positions in the string.
* RSET can be used with a [FIELD](/qb64wiki/index.php/FIELD "FIELD") or [TYPE](/qb64wiki/index.php/TYPE "TYPE") string definition to set the buffer position before a [PUT](/qb64wiki/index.php/PUT "PUT").


  

*Example:*





| ``` [CLS](/qb64wiki/index.php/CLS "CLS") [DIM](/qb64wiki/index.php/DIM "DIM") thestring [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 10 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "12345678901234567890" RSET thestring = "Hello!" [PRINT](/qb64wiki/index.php/PRINT "PRINT") thestring anystring$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(20) RSET anystring$ = "Hello again!" [PRINT](/qb64wiki/index.php/PRINT "PRINT") anystring$ RSET thestring = "Over ten characters long" [PRINT](/qb64wiki/index.php/PRINT "PRINT") thestring  ``` |
| --- |




| ``` 12345678901234567890     Hello!         Hello Again! Over ten c  ``` |
| --- |


*Explanation:* Notice how "Hello!" ends at the tenth position because the length of *thestring* is 10. When we used SPACE$(20) the length of *anystring$* became 20 so "Hello Again!" ended at the 20th position. That is right-justified. The last line "Over ten c" is truncated as it didn't fit into *thestring'*s length of only 10 characters.
  




## See also


* [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$"), [FIELD](/qb64wiki/index.php/FIELD "FIELD")
* [LSET](/qb64wiki/index.php/LSET "LSET"), [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")
* [PUT](/qb64wiki/index.php/PUT "PUT"), [GET](/qb64wiki/index.php/GET "GET")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RSET&oldid=7393>"




## Navigation menu








### Search





















