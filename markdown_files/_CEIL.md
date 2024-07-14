


\_CEIL - QB64 Phoenix Edition Wiki








# \_CEIL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CEIL function rounds a numeric value up to the next whole number or [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Availability](#Availability) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result* = \_CEIL(*expression*)
  




* \_CEIL returns he smallest integral value that is greater than the numerical *expression* (as a floating-point value).
* This means that \_CEIL rounds up for both positive and negative numbers.


  




## Availability


* **QB64 v1.0 and up**
* **QB64-PE all versions**


  




## Examples


*Example:* Displaying the rounding behavior of [INT](/qb64wiki/index.php/INT "INT"), [CINT](/qb64wiki/index.php/CINT "CINT") and [FIX](/qb64wiki/index.php/FIX "FIX") vs \_CEIL.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") [INT](/qb64wiki/index.php/INT "INT")(2.5), [CINT](/qb64wiki/index.php/CINT "CINT")(2.5), [FIX](/qb64wiki/index.php/FIX "FIX")(2.5), _CEIL(2.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") [INT](/qb64wiki/index.php/INT "INT")(-2.5), [CINT](/qb64wiki/index.php/CINT "CINT")(-2.5), [FIX](/qb64wiki/index.php/FIX "FIX")(-2.5), _CEIL(-2.5)  ``` |
| --- |




| ```  2        2         2         3 -3       -2        -2        -2  ``` |
| --- |


  




## See also


* [INT](/qb64wiki/index.php/INT "INT"), [FIX](/qb64wiki/index.php/FIX "FIX")
* [CINT](/qb64wiki/index.php/CINT "CINT"), [CLNG](/qb64wiki/index.php/CLNG "CLNG"),
* [CSNG](/qb64wiki/index.php/CSNG "CSNG"), [CDBL](/qb64wiki/index.php/CDBL "CDBL")
* [\_ROUND](/qb64wiki/index.php/ROUND "ROUND")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CEIL&oldid=8276>"




## Navigation menu








### Search





















