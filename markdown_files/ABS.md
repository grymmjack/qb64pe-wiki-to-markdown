


ABS - QB64 Phoenix Edition Wiki








# ABS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The ABS function returns the unsigned numerical value of a variable or literal value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*positive* = ABS(*numericalValue*)
  




## Description


* ABS always returns positive numerical values. The value can be any numerical type.
* Often used to keep a value positive when necessary in a program.
* Use [SGN](/qb64wiki/index.php/SGN "SGN") to determine a value's sign when necessary.
* **QB64** allows programs to return only positive [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") variable values using a [DIM](/qb64wiki/index.php/DIM "DIM") or [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE") statement.


  




## Examples


*Example:* Finding the absolute value of positive and negative numerical values.





| ``` a = -6 b = -7 c = 8 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") a < 0 [THEN](/qb64wiki/index.php/THEN "THEN") a = ABS(a) b = ABS(b) c = ABS(c) [PRINT](/qb64wiki/index.php/PRINT "PRINT") a, b, c  ``` |
| --- |




| ```  6        7        8  ``` |
| --- |


  




## See also


* [SGN](/qb64wiki/index.php/SGN "SGN"), [DIM](/qb64wiki/index.php/DIM "DIM")
* [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED")
* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ABS&oldid=5857>"




## Navigation menu








### Search





















