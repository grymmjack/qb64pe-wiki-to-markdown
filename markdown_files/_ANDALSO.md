


\_ANDALSO - QB64 Phoenix Edition Wiki








# \_ANDALSO



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
\_ANDALSO is a [boolean](/qb64wiki/index.php/Boolean "Boolean") logical operator that performs short-circuiting logical conjunction on two expressions.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*result* = *firstvalue* \_ANDALSO *secondvalue*
  




## Description


* A logical operation is said to be short-circuiting if the compiled code can bypass the evaluation of one expression depending on the result of another expression.
* If the result of the first expression evaluated determines the final result of the operation, there is no need to evaluate the second expression, because it cannot change the final result.
* Short-circuiting can improve performance if the bypassed expression is complex, or if it involves procedure calls.
* If both expressions evaluate to true, result is true.


  




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


*Example:* AND versus \_ANDALSO





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") index, values(1 [TO](/qb64wiki/index.php/TO "TO") 10), v  [FOR](/qb64wiki/index.php/FOR "FOR") index = 1 [TO](/qb64wiki/index.php/TO "TO") 10     values(index) = [RND](/qb64wiki/index.php/RND "RND") * 255 [NEXT](/qb64wiki/index.php/NEXT "NEXT") index  ' value of index is now > 10  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Trying _ANDALSO"  ' _ANDALSO performs short-circuiting logical conjunction and hence the GetArrayValue check is completely bypassed [IF](/qb64wiki/index.php/IF "IF") index >= 1 _ANDALSO index <= 10 _ANDALSO GetArrayValue(values(), index, v) [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_ANDALSO: Value ="; v [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_ANDALSO: Outside range." [END IF](/qb64wiki/index.php/END_IF "END IF")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Trying AND"  ' AND does not performs short-circuiting logical conjunction and hence QB64-PE will throw a runtime error: Subscript out of range [IF](/qb64wiki/index.php/IF "IF") index >= 1 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") index <= 10 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") GetArrayValue(values(), index, v) [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "AND: Value ="; v [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "AND: Outside range." [END IF](/qb64wiki/index.php/END_IF "END IF")  [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") GetArrayValue%% (arr() [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), idx [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), value [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     value = arr(idx)     GetArrayValue = -1 ' return true [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2658)
* [\_BIT](/qb64wiki/index.php/BIT "BIT"), [&B](/qb64wiki/index.php/%26B "&B"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE")
* [AND](/qb64wiki/index.php/AND "AND"), [XOR](/qb64wiki/index.php/XOR "XOR"), [OR](/qb64wiki/index.php/OR "OR")
* [AND (boolean)](/qb64wiki/index.php/AND_(boolean) "AND (boolean)"), [XOR (boolean)](/qb64wiki/index.php/XOR_(boolean) "XOR (boolean)"), [OR (boolean)](/qb64wiki/index.php/OR_(boolean) "OR (boolean)")
* [\_ORELSE](/qb64wiki/index.php/ORELSE "ORELSE"), [\_NEGATE](/qb64wiki/index.php/NEGATE "NEGATE")
* [Binary](/qb64wiki/index.php/Binary "Binary"), [Boolean](/qb64wiki/index.php/Boolean "Boolean")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ANDALSO&oldid=8939>"




## Navigation menu








### Search





















