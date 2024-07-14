


\_ROR - QB64 Phoenix Edition Wiki








# \_ROR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ROR function is used to rotate the bits of a numerical value to the right. A rotation (or circular shift) is an operation similar to shift ([\_SHL](/qb64wiki/index.php/SHL "SHL") and [\_SHR](/qb64wiki/index.php/SHR "SHR")) except that the bits that fall off at one end are put back to the other end.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*result* = \_ROR(*numericalVariable*, *numericalValue*)
  




## Parameters


* *numericalVariable* is the variable to shift the bits of and can be of the following types: [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), or [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64").
* Integer values can be signed or [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED").
* *numericalValue* is the number of places to rotate the bits.
* While 0 is a valid value it will have no affect on the variable being rotated.


  




## Description


* In right rotation, the bits that fall off at right end are put back at left end.
* The type of variable used to store the results should match the type of the variable being shifted.


  




## Availability


* **QB64-PE v3.1.0 and up**


  




## Examples




| ``` [OPTION _EXPLICIT](/qb64wiki/index.php/OPTION_EXPLICIT "OPTION EXPLICIT")  [DIM](/qb64wiki/index.php/DIM "DIM") a [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") [DIM](/qb64wiki/index.php/DIM "DIM") b [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") c [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") [DIM](/qb64wiki/index.php/DIM "DIM") d [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")  a = &B11110000 b = &B1111111100000000 c = &B11111111111111110000000000000000 d = &B1111111111111111111111111111111100000000000000000000000000000000  [DO](/qb64wiki/index.php/DO "DO")     a = _ROR(a, 1)     b = _ROR(b, 1)     c = _ROR(c, 1)     d = _ROR(d, 1)      [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([STRING$](/qb64wiki/index.php/STRING$ "STRING$")(8, "0") + [_BIN$](/qb64wiki/index.php/BIN$ "BIN$")(a), 8);     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([STRING$](/qb64wiki/index.php/STRING$ "STRING$")(16, "0") + [_BIN$](/qb64wiki/index.php/BIN$ "BIN$")(b), 16);     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 3, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([STRING$](/qb64wiki/index.php/STRING$ "STRING$")(32, "0") + [_BIN$](/qb64wiki/index.php/BIN$ "BIN$")(c), 32);     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 4, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([STRING$](/qb64wiki/index.php/STRING$ "STRING$")(64, "0") + [_BIN$](/qb64wiki/index.php/BIN$ "BIN$")(d), 64);      [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 15 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") <> 27  ``` |
| --- |


  




## See also


* [\_ROL](/qb64wiki/index.php/ROL "ROL"), [\_SHL](/qb64wiki/index.php/SHL "SHL"), [\_SHR](/qb64wiki/index.php/SHR "SHR")
* [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")
* [LONG](/qb64wiki/index.php/LONG "LONG"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ROR&oldid=6514>"




## Navigation menu








### Search





















