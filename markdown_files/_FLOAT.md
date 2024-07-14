


\_FLOAT - QB64 Phoenix Edition Wiki








# \_FLOAT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**\_FLOAT** numerical values offer the maximum floating-point decimal precision available using **QB64**.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


[DIM](/qb64wiki/index.php/DIM "DIM") *variable* AS \_FLOAT
  




## Description


* **QB64** always allocates 32 bytes to store this value.
* It is safe to assume this value is at least as precise as [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE").
* Under the current implementation it is stored in a 10-byte floating point variable.
* \_FLOAT variables can also use the ## variable name type suffix.
* Values returned may be expressed using exponential or [scientific notation](/qb64wiki/index.php/Scientific_notation "Scientific notation") using **E** for SINGLE or **D** for DOUBLE precision.
* According to [IEEE-754](http://babbage.cs.qc.edu/courses/cs341/IEEE-754references.html) this can store a value of up to 1.1897E+4932 compared to a DOUBLE which goes up to 1.7976E+308.
* Floating decimal point numerical values cannot be [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED").
* Values can be converted to 32 byte [ASCII](/qb64wiki/index.php/ASCII "ASCII") strings using [\_MK$](/qb64wiki/index.php/MK$ "MK$") and back with [\_CV](/qb64wiki/index.php/CV "CV").
* **When a variable has not been assigned or has no type suffix, the value defaults to [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE").**


  




## See also


* [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")
* [\_MK$](/qb64wiki/index.php/MK$ "MK$"), [\_CV](/qb64wiki/index.php/CV "CV")
* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [DIM](/qb64wiki/index.php/DIM "DIM")
* [CURRENCY](/qb64wiki/index.php/PDS(7.1)_Procedures#CURRENCY "PDS(7.1) Procedures")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FLOAT&oldid=7570>"




## Navigation menu








### Search





















