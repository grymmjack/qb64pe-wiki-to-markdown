


CLNG - QB64 Phoenix Edition Wiki








# CLNG



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The CLNG function rounds decimal point numbers up or down to the nearest [LONG](/qb64wiki/index.php/LONG "LONG") integer value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*value&* = CLNG(*expression*)
  




## Parameters


* *expression* is any [TYPE](/qb64wiki/index.php/TYPE "TYPE") of literal or variable numerical value or mathematical calculation.


  




## Description


* Used when integer values exceed 32767 or are less than -32768.
* Values greater than .5 are rounded up; .5 or lower are rounded down.
* CLNG can return normal [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values under 32768 too.
* Use it when a number could exceed normal [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") number limits.


  




## Examples




| ```  a& = CLNG(2345678.51)  [PRINT](/qb64wiki/index.php/PRINT "PRINT")  ``` |
| --- |




| ```  2345679  ``` |
| --- |


  




## See also


* [CINT](/qb64wiki/index.php/CINT "CINT"), [INT](/qb64wiki/index.php/INT "INT")
* [CSNG](/qb64wiki/index.php/CSNG "CSNG"), [CDBL](/qb64wiki/index.php/CDBL "CDBL")
* [\_ROUND](/qb64wiki/index.php/ROUND "ROUND")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CLNG&oldid=6381>"




## Navigation menu








### Search





















