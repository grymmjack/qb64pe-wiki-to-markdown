


LCASE$ - QB64 Phoenix Edition Wiki








# LCASE$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The LCASE$ function outputs an all-lowercase version of a [STRING](/qb64wiki/index.php/STRING "STRING").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result$* = LCASE$(*text$*)
  




## Description


* Normally used to guarantee that user input is not capitalized.
* Does not affect non-alphabetical characters.


  




## Examples


*Example:* The following code guarantees that all user letter entries will be lower case:





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Do you want to continue? (y/n)"  [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")     K$ = LCASE$([INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")) [LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") K$ = "y" [OR](/qb64wiki/index.php/OR "OR") K$ = "n"  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1232)
* [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$") (upper case)
* [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")
* [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LCASE$&oldid=8906>"




## Navigation menu








### Search





















