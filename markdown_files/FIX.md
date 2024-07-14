


FIX - QB64 Phoenix Edition Wiki








# FIX



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The FIX function rounds a numerical value to the next whole number closest to zero.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*result* = FIX(*expression*)
  




## Parameters


* *expression* is any [type](/qb64wiki/index.php/Data_types "Data types") of literal or variable numerical value or mathematical calculation.


  




## Description


* FIX effectively truncates (removes) the fractional part of *expression*, returning the integer part.
	+ This means that FIX rounds down for positive values and up for negative values.
* Use [INT](/qb64wiki/index.php/INT "INT") to round down negative values. Positive values are rounded down by both.


  




## Examples


*Example 1:* Showing the behavior of FIX with positive and negative decimal point values.





| ```  PRINT FIX(2.5)  PRINT FIX(-2.5)  ``` |
| --- |




| ``` 2 -2  ``` |
| --- |


  

*Example 2:* The NORMAL arithmetic method (round half up) can be achieved using the function in the example code below:





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") MATHROUND(0.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") MATHROUND(1.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") MATHROUND(2.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") MATHROUND(3.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") MATHROUND(4.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") MATHROUND(5.5)  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") MATHROUND(n)     MATHROUND = FIX(n + 0.5 * [SGN](/qb64wiki/index.php/SGN "SGN")(n)) [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |




| ``` 1 2 3 4 5 6  ``` |
| --- |


  




## See also


* [\_CEIL](/qb64wiki/index.php/CEIL "CEIL")
* [INT](/qb64wiki/index.php/INT "INT"), [CINT](/qb64wiki/index.php/CINT "CINT")
* [CLNG](/qb64wiki/index.php/CLNG "CLNG"), [\_ROUND](/qb64wiki/index.php/ROUND "ROUND")
* [MOD](/qb64wiki/index.php/MOD "MOD"), [Integer Division](/qb64wiki/index.php/%5C "\")
* [Normal division](/qb64wiki/index.php// "/")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FIX&oldid=6413>"




## Navigation menu








### Search





















