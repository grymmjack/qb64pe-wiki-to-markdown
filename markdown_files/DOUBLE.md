


DOUBLE - QB64 Phoenix Edition Wiki








# DOUBLE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
DOUBLE type floating point numerical values use 8 bytes per value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 See also](#See_also) |
| --- |


## Syntax


[DIM](/qb64wiki/index.php/DIM "DIM") *variable* [AS](/qb64wiki/index.php/AS "AS") DOUBLE
  




## Description


* Literal or variable values can range up to 15 decimal point places.
* The variable suffix type is **#**.
* Use DOUBLE and [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") variables sparingly as they use a lot of program memory.
* Values returned may be expressed using exponential or [scientific notation](/qb64wiki/index.php/Scientific_notation "Scientific notation") using **E** for SINGLE or **D** for DOUBLE precision.
* Floating decimal point numerical values cannot be [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED").
* Values can be converted to 8 byte [ASCII](/qb64wiki/index.php/ASCII "ASCII") string values using [\_MKD$](/qb64wiki/index.php/MKD$ "MKD$") and back with [\_CVD](/qb64wiki/index.php/CVD "CVD").
* **When a variable has not been defined or has no type suffix, the value defaults to [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE").**
* **Warning: QBasic keyword names cannot be used as numerical variable names with or without the type suffix.**


### QBasic/QuickBASIC


* Results of mathematical calculations may be approximate or slow in QuickBASIC 4.5.


  




## See also


* [DIM](/qb64wiki/index.php/DIM "DIM"), [DEFDBL](/qb64wiki/index.php/DEFDBL "DEFDBL")
* [MKD$](/qb64wiki/index.php/MKD$ "MKD$"), [CVD](/qb64wiki/index.php/CVD "CVD")
* [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT")
* [LEN](/qb64wiki/index.php/LEN "LEN")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DOUBLE&oldid=6765>"




## Navigation menu








### Search





















