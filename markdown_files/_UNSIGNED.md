


\_UNSIGNED - QB64 Phoenix Edition Wiki








# \_UNSIGNED



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
\_UNSIGNED defines a numerical value as being only positive.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[DIM](/qb64wiki/index.php/DIM "DIM") *variable* [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] *datatype*
[\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE") *letterRange* [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] *datatype*
  




## Description


* Datatype can be any of the following: [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), [\_BIT](/qb64wiki/index.php/BIT "BIT"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64"), [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")
* **[SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") and [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") variable types cannot be \_UNSIGNED.**
* \_UNSIGNED can be used in a [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE") statement to set undefined variable name first letters as all positive-only values.
* Can also be used in [DIM](/qb64wiki/index.php/DIM "DIM") statements or subprocedure parameter definitions following [AS](/qb64wiki/index.php/AS "AS").
* \_UNSIGNED allows larger positive numerical variable value limits than signed ones.
* The unsigned variable type suffix used is the **tilde (~)**, right before the number's own type suffix: *variableName~&*


  




How negative values affect the \_UNSIGNED value returned by a [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") (8 bits).


| ```                         00000001 - unsigned & signed are both 1                         01111111 - unsigned & signed are both 127                         11111111 - unsigned is 255 but signed is -1                         11111110 - unsigned is 254 but signed is -2                         11111101 - unsigned is 253 but signed is -3  ``` |
| --- |


  




## Examples


*Example 1:* In **QB64**, when a signed [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value exceeds 32767, the value may become a negative value:





| ``` i% = 38000 [PRINT](/qb64wiki/index.php/PRINT "PRINT") i%  ``` |
| --- |




| ``` -27536  ``` |
| --- |


*Explanation:* Use an \_UNSIGNED [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or a ~% variable type suffix for only positive integer values up to 65535.
  

*Example 2:* In **QB64**, \_UNSIGNED [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values greater than 65535 cycle over again from zero:





| ``` i~% = 70000 [PRINT](/qb64wiki/index.php/PRINT "PRINT") i~%  ``` |
| --- |




| ```  4464  ``` |
| --- |


*Explanation:* In QB64 an unsigned integer value of 65536 would be 0 with values increasing by the value minus 65536.
  

*Example 3:* Demonstrating how \_UNSIGNED variables expand the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") range.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") n [AS](/qb64wiki/index.php/AS "AS") _UNSIGNED [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") pn [AS](/qb64wiki/index.php/AS "AS") _UNSIGNED [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 3, 6: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press Esc to exit loop" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") n = 1 [TO](/qb64wiki/index.php/TO "TO") 80000   [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 10000 ' 6.5 second loop   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 12, 37: [PRINT](/qb64wiki/index.php/PRINT "PRINT") n ' display current value   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") n > 0 [THEN](/qb64wiki/index.php/THEN "THEN") pn = n ' find highest value   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") n = 0 [THEN](/qb64wiki/index.php/THEN "THEN") Count = Count + 1: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 14, 37: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Count:"; Count; "Max:"; pn   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [INP](/qb64wiki/index.php/INP "INP")(&H60) = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT FOR](/qb64wiki/index.php/EXIT "EXIT") ' escape key exit [NEXT](/qb64wiki/index.php/NEXT "NEXT") n [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ```      Press Esc to exit loop                                65462                            Count: 13 Max: 65535    ``` |
| --- |


*Explanation:* The maximum value can only be 65535 (32767 + 32768) so the FOR loop repeats itself. Remove the \_UNSIGNED parts and run it again.


  




## See also


* DECLARE, [SUB](/qb64wiki/index.php/SUB "SUB"), [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")
* [DIM](/qb64wiki/index.php/DIM "DIM"), [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE")
* [DEFSTR](/qb64wiki/index.php/DEFSTR "DEFSTR"), [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG"), [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT"), [DEFSNG](/qb64wiki/index.php/DEFSNG "DEFSNG"), [DEFDBL](/qb64wiki/index.php/DEFDBL "DEFDBL")
* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")
* [ABS](/qb64wiki/index.php/ABS "ABS"), [SGN](/qb64wiki/index.php/SGN "SGN")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=UNSIGNED&oldid=7457>"




## Navigation menu








### Search





















