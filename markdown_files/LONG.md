


LONG - QB64 Phoenix Edition Wiki








# LONG



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
LONG defines a variable as a 4 byte number type definition for larger [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


[DIM](/qb64wiki/index.php/DIM "DIM") *variable* AS LONG
  




* LONG integer values range from -2147483648 to 2147483647.
* **QB64'**s [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") LONG integer values range from 0 to 4294967295.
* **QB64** [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") values range from 0 to 18446744073709551615.
* Decimal point values assigned to a LONG variable will be rounded to the nearest whole number.
* The LONG variable type suffix is & or ~& for [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED"). Suffix can also be placed after a literal or hexadecimal numerical value.
* [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") uses the **&&** or **~&&** [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") suffix.
* Values can be converted to 4 byte [ASCII](/qb64wiki/index.php/ASCII "ASCII") string values using [MKL$](/qb64wiki/index.php/MKL$ "MKL$") and back with [CVL](/qb64wiki/index.php/CVL "CVL").
* **When a variable has not been assigned or has no type suffix, the type defaults to [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE").**
* **Warning: QBasic keyword names cannot be used as numerical variable names with or without the type suffix.**


  




## See also


* [DIM](/qb64wiki/index.php/DIM "DIM"), [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG")
* [LEN](/qb64wiki/index.php/LEN "LEN"), [CLNG](/qb64wiki/index.php/CLNG "CLNG")
* [MKL$](/qb64wiki/index.php/MKL$ "MKL$"), [CVL](/qb64wiki/index.php/CVL "CVL")
* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")
* [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")
* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LONG&oldid=6080>"




## Navigation menu








### Search





















