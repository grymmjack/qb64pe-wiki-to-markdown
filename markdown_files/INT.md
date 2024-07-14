


INT - QB64 Phoenix Edition Wiki








# INT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The INT function rounds a numeric value down to the next whole number.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*result* = INT(*expression*)
  




## Parameters


* *expression* is any [type](/qb64wiki/index.php/Data_types "Data types") of literal or variable numerical value or mathematical calculation.


  




## Description


* INT returns the first whole number [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") that is less than the *expression* value.
* This means that INT rounds down for both positive and negative numbers.
* Use [FIX](/qb64wiki/index.php/FIX "FIX") to round negative values up. It is identical to INT for positive values.


  




## Examples


*Example:* Displaying the rounding behavior of INT.





| ``` PRINT INT(2.5) PRINT INT(-2.5)  ``` |
| --- |




| ```  2 -3  ``` |
| --- |


  




## See also


* [CINT](/qb64wiki/index.php/CINT "CINT"), [CLNG](/qb64wiki/index.php/CLNG "CLNG"), [FIX](/qb64wiki/index.php/FIX "FIX")
* [CSNG](/qb64wiki/index.php/CSNG "CSNG"), [CDBL](/qb64wiki/index.php/CDBL "CDBL")
* [\_ROUND](/qb64wiki/index.php/ROUND "ROUND"), [\_CEIL](/qb64wiki/index.php/CEIL "CEIL")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INT&oldid=6428>"




## Navigation menu








### Search





















