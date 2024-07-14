


OPTION BASE - QB64 Phoenix Edition Wiki








# OPTION BASE



From QB64 Phoenix Edition Wiki
(Redirected from [BASE](/qb64wiki/index.php?title=BASE&redirect=no "BASE"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The OPTION BASE statement is used to set the default lower bound of arrays.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


OPTION BASE {0|1}
  




## Description


* This statement affects array declarations where the lower bound of a dimension is not specified.
* When used, OPTION BASE must come before any array declarations ([DIM](/qb64wiki/index.php/DIM "DIM")) to be affected.
* By default, the lower bound for arrays is zero, and may be changed to one using the statement.
* Otherwise, arrays will be dimensioned from element 0 if you DIM just the upper bounds.
* You can also set other array boundaries by using [TO](/qb64wiki/index.php/TO "TO") in the DIM declaration such as DIM array(5 TO 10)


  




## Examples


*Example 1:* Set the default lower bound for array declarations to one.





| ``` OPTION BASE 1  ' Declare a 5-element one-dimensional array with element indexes of one through five. [DIM](/qb64wiki/index.php/DIM "DIM") array(5) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LBOUND](/qb64wiki/index.php/LBOUND "LBOUND")(array)  ``` |
| --- |




| ```  1 ``` |
| --- |


  

*Example 2:* Set the default lower bound for array declarations to zero.





| ``` OPTION BASE 0  ' Declare an 18-element two-dimensional array with element indexes of zero through two ' for the first dimension, and 10 through 15 for the second dimension. [DIM](/qb64wiki/index.php/DIM "DIM") array(2, 10 to 15) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LBOUND](/qb64wiki/index.php/LBOUND "LBOUND")(array, 1) [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LBOUND](/qb64wiki/index.php/LBOUND "LBOUND")(array, 2)  ``` |
| --- |




| ```  0  10  ``` |
| --- |


  




## See also


* [Arrays](/qb64wiki/index.php/Arrays "Arrays"), [LBOUND](/qb64wiki/index.php/LBOUND "LBOUND"), [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")
* [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM"), [STATIC](/qb64wiki/index.php/STATIC "STATIC"), [COMMON](/qb64wiki/index.php/COMMON "COMMON")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OPTION_BASE&oldid=6144>"




## Navigation menu








### Search





















