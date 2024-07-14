


CINT - QB64 Phoenix Edition Wiki








# CINT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The CINT function rounds decimal point numbers up or down to the nearest [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*value%* = CINT(*expression*)
  




## Parameters


* *expression* is any [TYPE](/qb64wiki/index.php/TYPE "TYPE") of literal or variable numerical value or mathematical calculation.


  




## Description


* Values greater than .5 are rounded up. Values lower than .5 are rounded down.
* *Warning:* Since CINT is used for integer values, the input values cannot exceed 32767 to -32768!
* Use [CLNG](/qb64wiki/index.php/CLNG "CLNG") for [LONG](/qb64wiki/index.php/LONG "LONG") integer values exceeding [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") limitations.
* Note: When decimal point values are given to BASIC functions requiring [INTEGERs](/qb64wiki/index.php/INTEGER "INTEGER") the value will be CINTed.


  




## Examples


*Example:* Shows how CINT rounds values up or down as in "bankers' rounding".





| ``` a% = CINT(1.49): b% = CINT(1.50): c = 11.5 [COLOR](/qb64wiki/index.php/COLOR "COLOR") c: [PRINT](/qb64wiki/index.php/PRINT "PRINT") a%, b%, c  ``` |
| --- |




| ``` 1       2       11.5  ``` |
| --- |


  




## See also


* [\_ROUND](/qb64wiki/index.php/ROUND "ROUND"), [\_CEIL](/qb64wiki/index.php/CEIL "CEIL")
* [CLNG](/qb64wiki/index.php/CLNG "CLNG"), [CSNG](/qb64wiki/index.php/CSNG "CSNG"), [CDBL](/qb64wiki/index.php/CDBL "CDBL")
* [INT](/qb64wiki/index.php/INT "INT"), [FIX](/qb64wiki/index.php/FIX "FIX")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CINT&oldid=7832>"




## Navigation menu








### Search





















