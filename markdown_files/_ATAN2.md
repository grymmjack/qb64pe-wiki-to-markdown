


\_ATAN2 - QB64 Phoenix Edition Wiki








# \_ATAN2



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ATAN2 function returns the radian angle between the positive x-axis of a plane and the point given by the coordinates (x, y).


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) 	+ [3.1 Errors](#Errors) * [4 See also](#See_also) |
| --- |


## Syntax


*angle!* = \_ATAN2(*y*, *x*)
  




## Parameters


* *y* is the vertical axis position (row) as a positive, zero or negative floating point value.
* *x* is the horizontal axis position (column) as a positive, zero or negative floating point value.


  




## Description


* The [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") radian angle returned is **positive** for upper row values where y > 0.


* \_ATAN2(y, x) = [ATN](/qb64wiki/index.php/ATN "ATN")(y# / x#) when x > 0
* \_ATAN2(y, x) = [ATN](/qb64wiki/index.php/ATN "ATN")(y# / x#) + [\_PI](/qb64wiki/index.php/PI "PI") when x < 0
* \_ATAN2(y, x) = [\_PI](/qb64wiki/index.php/PI "PI") / 2 when x = 0

* The [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") radian angle returned is 0 when x > 0 and [\_PI](/qb64wiki/index.php/PI "PI") when x < 0 where y = 0
* The [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") radian angle returned is **negative** for lower row values where y < 0.


* \_ATAN2(y, x) = [ATN](/qb64wiki/index.php/ATN "ATN")(y# / x#) when x > 0
* \_ATAN2(y, x) = [ATN](/qb64wiki/index.php/ATN "ATN")(y# / x#) - [\_PI](/qb64wiki/index.php/PI "PI") when x < 0
* \_ATAN2(y, x) = -[\_PI](/qb64wiki/index.php/PI "PI") / 2 when x = 0

* \_ATAN2(0, 0) is undefined and the function returns 0 instead of a division error.


### Errors


* With [ATN](/qb64wiki/index.php/ATN "ATN")(y / x), x can never be 0 as that would create a Division by Zero [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") 11 or #IND.


  




## See also


* [ATN](/qb64wiki/index.php/ATN "ATN") (arctangent)
* [\_PI](/qb64wiki/index.php/PI "PI") (QB64 function)
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [Atan2 reference](https://en.wikipedia.org/wiki/Atan2 "wikipedia:Atan2")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ATAN2&oldid=8978>"




## Navigation menu








### Search





















