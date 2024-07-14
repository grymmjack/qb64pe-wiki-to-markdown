


EXP - QB64 Phoenix Edition Wiki








# EXP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The EXP math function calculates the exponential function (**e** raised to the power of a *numericExpression*).


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*result* = EXP(*numericExpression*)
  




## Description


* **e** is defined as the base of natural logarithms or as the limit of (1 + 1 / n) ^ n, as n goes to infinity.
* When passing *numericExpression* as a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") variable or as literal number without an explicit type suffix, then it must be less than or equal to **88.02969** or an ["overflow" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.
* When passing *numericExpression* as a [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") or [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") variable, then it must be less than or equal to **709.782712893** or an ["overflow" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur. You may pass literal numbers as [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") or [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") values by explicitly adding the **#** or **##** type suffix to it respectively, e.g. result = EXP(678.9##).
* The value returned is **e** to the exponent parameter (**e = 2.718282** approximately).
* The precision of the returned values depends on the provided *result* variable type, but is usually not higher than that of the given *numericExpression*.
* Positive exponent values indicate the number of times to multiply **e** by itself.
* Negative exponent values indicate the number of times to divide by **e**. Example: e ^ -3 = 1 / e ^ 3 = 1 / (e \* e \* e)


  




## See also


* [LOG](/qb64wiki/index.php/LOG "LOG")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [Derived Mathematical Functions](/qb64wiki/index.php/Mathematical_Operations#Derived_Mathematical_Functions "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=EXP&oldid=8015>"




## Navigation menu








### Search





















