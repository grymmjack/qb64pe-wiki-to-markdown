


\_NEGATE - QB64 Phoenix Edition Wiki








# \_NEGATE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
\_NEGATE is a [boolean](/qb64wiki/index.php/Boolean "Boolean") logical operator that will change a false statement to a true one and vice-versa.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*result* = \_NEGATE *value*
  




## Description


* Unlike [NOT](/qb64wiki/index.php/NOT "NOT"), which evaluates a value and returns the bitwise opposite, \_NEGATE returns the logical opposite. Meaning that \_NEGATE *non\_zero\_value* = 0.
* Often called a negative logic operator, it returns the opposite of a value as true or false.


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.13.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.13.0")

**v3.13.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


*Example:* NOT versus \_NEGATE





| ``` [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")     [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") isdigit& ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") n [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")) [END DECLARE](/qb64wiki/index.php/END_DECLARE "END DECLARE")  [IF](/qb64wiki/index.php/IF "IF") [NOT](/qb64wiki/index.php/NOT "NOT") isdigit([ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("1")) [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "NOT: 1 is not a digit." [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "NOT: 1 is a digit." [END IF](/qb64wiki/index.php/END_IF "END IF")  [IF](/qb64wiki/index.php/IF "IF") _NEGATE isdigit([ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("1")) [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_NEGATE: 1 is not a digit." [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_NEGATE: 1 is a digit." [END IF](/qb64wiki/index.php/END_IF "END IF")  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ``` NOT: 1 is not a digit. _NEGATE: 1 is a digit.  ``` |
| --- |


*Explanation:* NOT is a bitwise operator that inverts all the bits in an integer, whereas \_NEGATE is a logical operator that flips the truth value of a boolean expression.
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2671)
* [\_BIT](/qb64wiki/index.php/BIT "BIT"), [&B](/qb64wiki/index.php/%26B "&B"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE")
* [AND](/qb64wiki/index.php/AND "AND"), [XOR](/qb64wiki/index.php/XOR "XOR"), [OR](/qb64wiki/index.php/OR "OR")
* [AND (boolean)](/qb64wiki/index.php/AND_(boolean) "AND (boolean)"), [XOR (boolean)](/qb64wiki/index.php/XOR_(boolean) "XOR (boolean)"), [OR (boolean)](/qb64wiki/index.php/OR_(boolean) "OR (boolean)")
* [\_ANDALSO](/qb64wiki/index.php/ANDALSO "ANDALSO"), [\_ORELSE](/qb64wiki/index.php/ORELSE "ORELSE")
* [Binary](/qb64wiki/index.php/Binary "Binary"), [Boolean](/qb64wiki/index.php/Boolean "Boolean")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=NEGATE&oldid=8941>"




## Navigation menu








### Search





















