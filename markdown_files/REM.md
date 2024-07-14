


REM - QB64 Phoenix Edition Wiki








# REM



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**REM** or an apostrophe is used for programmer remarks, comments or to stop the execution of program code.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


REM program comment or ignore code
  




## Description


* Comments cannot be read by QBasic correctly and may cause syntax and other errors without REM!
* Instead of REM you can use the ' symbol which can be put anywhere.
* Code can also be commented out for program testing purposes.
* QBasic Metacommands such as [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") and [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") require the use of REM or the apostrophe.


  

*Example:* Avoiding an END IF error.





| ``` REM This is a remark... ' This is also a remark... [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") a = 0 [THEN](/qb64wiki/index.php/THEN "THEN") REM (REM follows syntax rules) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") a = 0 [THEN](/qb64wiki/index.php/THEN "THEN") '(apostrophe doesn't follow syntax rules, so use END IF after this) [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1130)
* [Apostrophe](/qb64wiki/index.php/Apostrophe "Apostrophe")
* [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC"), [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC"), [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=REM&oldid=8889>"




## Navigation menu








### Search





















