


\_ORELSE - QB64 Phoenix Edition Wiki








# \_ORELSE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
\_ORELSE is a [boolean](/qb64wiki/index.php/Boolean "Boolean") logical operator that performs short-circuiting inclusive logical disjunction on two expressions.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*result* = *firstvalue* \_ORELSE *secondvalue*
  




## Description


* A logical operation is said to be short-circuiting if the compiled code can bypass the evaluation of one expression depending on the result of another expression.
* If the result of the first expression evaluated determines the final result of the operation, there is no need to evaluate the second expression, because it cannot change the final result.
* Short-circuiting can improve performance if the bypassed expression is complex, or if it involves procedure calls.
* If either or both expressions evaluate to true, result is true.


  




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


*Example:* OR versus \_ORELSE





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Trying _ORELSE"  ' _ORELSE performs short-circuiting logical conjunction and hence for "strawberry", only isFruit() is called [IF](/qb64wiki/index.php/IF "IF") isFruit("strawberry") _ORELSE isRed("strawberry") _ORELSE isSeasonal("strawberry") [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Probably a strawberry." [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Certainly not a strawberry." [END IF](/qb64wiki/index.php/END_IF "END IF")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Trying OR"  ' OR does not performs short-circuiting logical conjunction and hence all is***() functions are called [IF](/qb64wiki/index.php/IF "IF") isFruit("strawberry") [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") isRed("strawberry") [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") isSeasonal("strawberry") [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Probably a strawberry." [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Certainly not a strawberry." [END IF](/qb64wiki/index.php/END_IF "END IF")  [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") isFruit%% (fruit [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"))     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "isFruit() called!"     isFruit = (fruit = "strawberry") [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") isRed%% (fruit [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"))     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "isRed() called!"     isRed = (fruit = "strawberry") [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") isSeasonal%% (fruit [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"))     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "isSeasonal() called!"     isSeasonal = (fruit = "strawberry") [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |




| ``` Trying _ORELSE isFruit() called! Probably a strawberry.  Trying OR isFruit() called! isRed() called! isSeasonal() called! Probably a strawberry.  ``` |
| --- |


## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2661)
* [\_BIT](/qb64wiki/index.php/BIT "BIT"), [&B](/qb64wiki/index.php/%26B "&B"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE")
* [AND](/qb64wiki/index.php/AND "AND"), [XOR](/qb64wiki/index.php/XOR "XOR"), [OR](/qb64wiki/index.php/OR "OR")
* [AND (boolean)](/qb64wiki/index.php/AND_(boolean) "AND (boolean)"), [XOR (boolean)](/qb64wiki/index.php/XOR_(boolean) "XOR (boolean)"), [OR (boolean)](/qb64wiki/index.php/OR_(boolean) "OR (boolean)")
* [\_ANDALSO](/qb64wiki/index.php/ANDALSO "ANDALSO"), [\_NEGATE](/qb64wiki/index.php/NEGATE "NEGATE")
* [Binary](/qb64wiki/index.php/Binary "Binary"), [Boolean](/qb64wiki/index.php/Boolean "Boolean")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ORELSE&oldid=8940>"




## Navigation menu








### Search





















