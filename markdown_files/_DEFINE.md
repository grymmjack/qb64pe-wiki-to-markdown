


\_DEFINE - QB64 Phoenix Edition Wiki








# \_DEFINE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
\_DEFINE defines a set of variable names according to their first character as a specified data type.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_DEFINE *letter*[*-range*, ...] [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] data[type](/qb64wiki/index.php/Variable_Types "Variable Types")
  




## Parameters


* Variable start *letter range* is in the form firstletter-endingletter (like A-C) or just a single letter.
* *Data types*: [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), [LONG](/qb64wiki/index.php/LONG "LONG"), [STRING](/qb64wiki/index.php/STRING "STRING"), [\_BIT](/qb64wiki/index.php/BIT "BIT"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64"), [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT"), [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET"), [\_MEM](/qb64wiki/index.php/MEM "MEM")
* Can also use the [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") definition for positive whole [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") type numerical values.


  




## Description


* **When a variable has not been defined or has no type suffix, the value defaults to a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") precision floating point value.**
* \_DEFINE sets the [type](/qb64wiki/index.php/Variable_Types "Variable Types") of all variable names with the starting letter(s) or letter ranges when encountered in the progression of the program (even in conditional statement blocks not executed and subsequent [SUB](/qb64wiki/index.php/SUB "SUB") procedures).
* **NOTE: Many QBasic keyword variable names CAN be used with a [STRING](/qb64wiki/index.php/STRING "STRING") suffix ($)! You cannot use them without the suffix, use a numerical suffix or use [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM"), \_DEFINE, [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") or [TYPE](/qb64wiki/index.php/TYPE "TYPE") variable [AS](/qb64wiki/index.php/AS "AS") statements.**
* **QBasic's IDE** added DEF statements before any [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION"). **QB64** (like QB) will change all variable types in subsequent sub-procedures to that default variable type without giving a ["Parameter Type Mismatch"](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") warning or adding the proper DEF statement to subsequent procedures. If you do not want that to occur, either remove that DEF statement or add the proper DEF type statements to subsequent procedures.
* May also affect [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") procedures.


  




## Examples


*Example:* Defining variables that start with the letters A, B, C or F as unsigned integers, including the *Add2* [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION").





| ``` _DEFINE A-C, F [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") Add2(-1.1, -2.2)  [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") Add2 (one, two)     Add2 = one + two [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |




| ``` 65533  ``` |
| --- |


*Explanation:* Unsigned integers can only return positive values while ordinary [integers](/qb64wiki/index.php/INTEGER "INTEGER") can also return negative values.
  




## See also


* [DEFSTR](/qb64wiki/index.php/DEFSTR "DEFSTR"), [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG"), [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT"), [DEFSNG](/qb64wiki/index.php/DEFSNG "DEFSNG"), [DEFDBL](/qb64wiki/index.php/DEFDBL "DEFDBL")
* [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM")
* [COMMON](/qb64wiki/index.php/COMMON "COMMON"), [SHARED](/qb64wiki/index.php/SHARED "SHARED")
* [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DEFINE&oldid=8703>"




## Navigation menu








### Search





















