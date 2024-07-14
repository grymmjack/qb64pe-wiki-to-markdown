


DEFSNG - QB64 Phoenix Edition Wiki








# DEFSNG



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The DEFSNG statement defines all variables with names starting with the specified letter (or letter range) AS [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") variables.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Legacy support](#Legacy_support) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


DEFSNG *letter*[-*range*], *letter2*[-*range2*], [...]
### Legacy support


* **DEF** statements ([DEFDBL](/qb64wiki/index.php/DEFDBL "DEFDBL"), DEFSNG, [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG"), [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT"), [DEFSTR](/qb64wiki/index.php/DEFSTR "DEFSTR")) were used when storage space was a concern in older computers, as their usage could save up typing. Instead of DIM a AS SINGLE, a2 AS SINGLE, a3 AS SINGLE, simply having DEFSNG A in the code before using variables starting with letter **A** would do the same job.
* For clarity, it is recommended to declare variables with meaningful names.


  




## Description


* Undeclared variables with no type suffix are of type [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") by default.
* *letter* (or *range*) can be from A-Z or any other range, like **G-M**.
* You can also use commas for specific undefined variable first letters.
* Variables [DIMensioned](/qb64wiki/index.php/DIM "DIM") as another variable type or that use type suffixes are not affected by DEFSNG.
* DEFSNG sets the [type](/qb64wiki/index.php/Variable_Types "Variable Types") of all variable names with the starting letter(s) or letter ranges when encountered in the progression of the program (even in conditional statement blocks not executed and subsequent [SUB](/qb64wiki/index.php/SUB "SUB") procedures).
* **Warning: QBasic keyword names cannot be used as numerical variable names with or without the type suffix.**


### QBasic/QuickBASIC


* QBasic's IDE would add DEF statements before any [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION"). QB64 (like QBasic) will change all variable types in subsequent sub-procedures to that default variable type without giving a ["Parameter Type Mismatch"](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") warning or adding DEF statement to subsequent procedures. If you do not want that to occur, either remove that DEF statement or add the proper DEF type statements to subsequent procedures. May also affect [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") procedures.


  




## Examples




| ``` DEFSNG A, F-H, M  'With the above, all variables with names starting with A, F, G, H and M 'will be of type SINGLE, unless they have a type suffix 'indicating another type or they are [dimensioned](/qb64wiki/index.php/DIM "DIM") differently  ``` |
| --- |


  




## See also


* [DEFDBL](/qb64wiki/index.php/DEFDBL "DEFDBL"), [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG"), [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT"), [DEFSTR](/qb64wiki/index.php/DEFSTR "DEFSTR")
* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DEFSNG&oldid=8706>"




## Navigation menu








### Search





















