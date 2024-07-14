


CDBL - QB64 Phoenix Edition Wiki








# CDBL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
CDBL converts a value to the closest [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")-precision value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*doubleValue#* = CDBL(*expression*)
  




## Parameters


* *expression* is any [TYPE](/qb64wiki/index.php/TYPE "TYPE") of literal or variable numerical value or mathematical calculation.


  




## Description


* Rounds to the closest [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") floating decimal point value.
* Also can be used to define a value as [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")-precision up to 15 decimals.


  




## Examples


*Example:* Prints a double-precision version of the single-precision value stored in the variable named A.





| ```  A = 454.67  [PRINT](/qb64wiki/index.php/PRINT "PRINT") A; CDBL(A)  ``` |
| --- |




| ```  454.67 454.6700134277344  ``` |
| --- |


The last 11 numbers in the double-precision number change the value in this example, since A was previously defined to only two-decimal place accuracy.
  




## See also


* [CINT](/qb64wiki/index.php/CINT "CINT"), [CLNG](/qb64wiki/index.php/CLNG "CLNG")
* [CSNG](/qb64wiki/index.php/CSNG "CSNG"), [\_ROUND](/qb64wiki/index.php/ROUND "ROUND")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CDBL&oldid=7233>"




## Navigation menu








### Search





















