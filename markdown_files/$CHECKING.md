


$CHECKING - QB64 Phoenix Edition Wiki








# $CHECKING



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $CHECKING metacommand turns C++ event checking ON or OFF.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 Details](#Details) * [3 See also](#See_also) |
| --- |


## Syntax


$CHECKING:{ON|OFF}
  




## Description


* The Metacommand does **not** require a comment or REM before it. There is no space after the colon.
* The OFF action turns event checking off and should **only be used when running stable, errorless code.**
* The default $CHECKING:ON action is only required when checking has been turned OFF previously.
* When $CHECKING:OFF is used, all error code and the reporting code is removed from the EXE program.
* **Warning: Turning OFF error checking could create a General Protection Fault (or segfault). Use only with 100% stable sections of code.**


### Details


* After every QB64 command is translated to C++, the compiler adds special code sections to check for [ON TIMER(n)](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)") events and errors that may have occured in the last function call. Disabling error checking with the $CHECKING:OFF directive prevents the compiler from adding the extra code sections.
* Setting $CHECKING:OFF is only designed for 100% stable, errorless sections of code, where every CPU cycle saved counts, such as in a software 3D texture mapper, for example.


  




## See also


* [ON TIMER(n)](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)")
* [ON ERROR](/qb64wiki/index.php/ON_ERROR "ON ERROR")
* [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand")
* [ERROR Codes](/qb64wiki/index.php/ERROR_Codes "ERROR Codes")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$CHECKING&oldid=8027>"




## Navigation menu








### Search





















