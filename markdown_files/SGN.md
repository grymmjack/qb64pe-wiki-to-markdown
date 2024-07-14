


SGN - QB64 Phoenix Edition Wiki








# SGN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **SGN** function returns the sign of a number value.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


sign% = SGN(value)
  




* Returns -1 when a sign is negative, 0 when a value is zero, or 1 when a value is positive.
* Function is used to store the original sign of a number.
* **QB64** allows programs to return only [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") variable values using a [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE") statement.


  



*Example:* Checking and changing negative values to positive ones.





| ``` n = -100 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") SGN(n) = -1 THEN n = [ABS](/qb64wiki/index.php/ABS "ABS")(n) PRINT n  ``` |
| --- |




| ```  100  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1079)
* [ABS](/qb64wiki/index.php/ABS "ABS")
* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SGN&oldid=8884>"




## Navigation menu








### Search





















