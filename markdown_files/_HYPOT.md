


\_HYPOT - QB64 Phoenix Edition Wiki








# \_HYPOT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_HYPOT function returns the hypotenuse of a right-angled triangle whose legs are x and y.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*result!* = \_HYPOT(*x*, *y*)
  




## Parameters


* *x* and *y* are the floating point values corresponding to the legs of a right-angled (90 degree) triangle for which the hypotenuse is computed.


  




## Description


* The function returns what would be the square root of the sum of the squares of x and y (as per the Pythagorean theorem).
* The hypotenuse is the longest side between the two 90 degree angle sides


  




## Examples


*Example:*





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") leg_x [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), leg_y [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), result [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") leg_x = 3 leg_y = 4 result = _HYPOT(leg_x, leg_y) [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") "## , ## and ## form a right-angled triangle."; leg_x; leg_y; result  ``` |
| --- |




| ```  3 , 4 and 5 form a right-angled triangle.  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1782)
* [ATN](/qb64wiki/index.php/ATN "ATN") (arctangent)
* [\_PI](/qb64wiki/index.php/PI "PI") (function)
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [C++ reference for hypot() - source of the text and sample above](http://www.cplusplus.com/reference/cmath/hypot/)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=HYPOT&oldid=8938>"




## Navigation menu








### Search





















