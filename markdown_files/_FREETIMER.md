


\_FREETIMER - QB64 Phoenix Edition Wiki








# \_FREETIMER



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_FREETIMER function returns a free [TIMER](/qb64wiki/index.php/TIMER "TIMER") number for multiple [ON TIMER(n)](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)") events.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*timerhandle%* = \_FREETIMER
  




## Description


* QB64 can use an unlimited number of ON TIMER (number, seconds!) event [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values at once.
* Every time \_FREETIMER is called the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value returned will increase by one, starting at 1, whether it is used or not.
* Store multiple returns in different variable names to refer to separate events later.


  




## See also


* [ON TIMER(n)](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FREETIMER&oldid=6007>"




## Navigation menu








### Search





















