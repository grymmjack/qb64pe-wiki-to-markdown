


\_ROUND - QB64 Phoenix Edition Wiki








# \_ROUND



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ROUND function rounds to the closest even [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG") or [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") numerical value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*value* = \_ROUND(*number*)
  




## Description


* Can round [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") or [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") floating decimal point parameter values.
* Can be used when numerical values exceed the limits of [CINT](/qb64wiki/index.php/CINT "CINT") or [CLNG](/qb64wiki/index.php/CLNG "CLNG").
* Rounding is done to the closest even [integer](/qb64wiki/index.php/INTEGER "INTEGER") value. The same as QBasic does with [integer division](/qb64wiki/index.php/%5C "\").


  

*Example:* Displays how QB64 rounds to the closest even integer value.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") _ROUND(0.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") _ROUND(1.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") _ROUND(2.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") _ROUND(3.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") _ROUND(4.5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") _ROUND(5.5)  ``` |
| --- |




| ``` 0 2 2 4 4 6  ``` |
| --- |


  




## See also


* [INT](/qb64wiki/index.php/INT "INT"), [CINT](/qb64wiki/index.php/CINT "CINT")
* [FIX](/qb64wiki/index.php/FIX "FIX"), [CLNG](/qb64wiki/index.php/CLNG "CLNG")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ROUND&oldid=7392>"




## Navigation menu








### Search





















