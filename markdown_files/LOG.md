


LOG - QB64 Phoenix Edition Wiki








# LOG



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The LOG math function returns the natural logarithm of a specified numerical value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*logarithm!* = LOG(*value*)
  




## Description


* *value* MUST be greater than 0. ["Illegal function call" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") occurs if negative or zero values are used.
* The natural logarithm is the logarithm to the base **e = 2.718282** (approximately).
* The natural logarithm of *a* is defined as the integral from 1 to *a* of dx/x.
* Returns are default [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") precision unless the value parameter uses [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") precision.


  




## Examples


*Example 1:* [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") to find the base ten logarithm of a numerical value.





| ```  FUNCTION Log10#(value AS DOUBLE) [STATIC](/qb64wiki/index.php/STATIC "STATIC")    Log10# = LOG(value) / LOG(10.#)  END FUNCTION  ``` |
| --- |


*Explanation:* The natural logarithm of the value is divided by the base 10 logarithm. The LOG of ten is designated as a DOUBLE precision return by using # after the Log10 value. The return tells you the number of times 10 goes into a value.
  

*Example 2:* A binary FUNCTION to convert [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values using LOG to find the number of digits the return will be.





| ``` FUNCTION BinStr$ (n&)   IF n& < 0 THEN EXIT FUNCTION            'positive numbers only! negative error!   FOR p% = 0 TO INT(LOG(n& + .1) / LOG(2))     ' added +.1 to get 0 to work     IF n& [AND](/qb64wiki/index.php/AND "AND") 2 ^ p% THEN s$ = "1" + s$ ELSE s$ = "0" + s$  'find bits on   NEXT p%   IF s$ = "" THEN BinStr$ = "&B0" ELSE BinStr$ = "&B" + s$       'check for zero return END FUNCTION   ``` |
| --- |


*Explanation:* The LOG of a **positive** [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value is divided by the LOG of 2 to determine the number of binary digits that will be returned. The FOR loop compares the value with the exponents of two and determines if a bit is ON or OFF as "1" or "0".
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1114)
* [EXP](/qb64wiki/index.php/EXP "EXP"), [&B](/qb64wiki/index.php/%26B "&B") (binary number)
* [Derived Mathematical Functions](/qb64wiki/index.php/Mathematical_Operations#Derived_Mathematical_Functions "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LOG&oldid=8895>"




## Navigation menu








### Search





















