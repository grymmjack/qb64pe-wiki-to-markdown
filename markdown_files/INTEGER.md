


INTEGER - QB64 Phoenix Edition Wiki








# INTEGER



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
INTEGER is a 2-byte number type definition that can hold whole numerical values.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


[DIM](/qb64wiki/index.php/DIM "DIM") *variable* AS INTEGER
  




* Integers do not use decimal point values but will round those off to the nearest even whole number.
* QBasic integer values can range from -32768 to 32767 without an "overflow" error.
* For larger integer values use the [LONG](/qb64wiki/index.php/LONG "LONG") integer type.
* **QB64** INTEGER values greater than 32767 become negative signed values instead of throwing an "overflow" error, as the top bit designates a negative value. See example 1 below.
* **QB64** [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") integers can range from 0 to 65535.
* **QB64** \_UNSIGNED [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") values range from 0 to 18446744073709551615
* Many graphic programs require INTEGER arrays.
* Variable type suffix is % or ~% for [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED"). Suffix can also be placed after a literal or hexadecimal numerical value.
* [LONG](/qb64wiki/index.php/LONG "LONG") integers use the **&** suffix and [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") use the **&&** suffix.
* Values can be converted to 2 byte [ASCII](/qb64wiki/index.php/ASCII "ASCII") string values using [MKI$](/qb64wiki/index.php/MKI$ "MKI$") and back with [CVI](/qb64wiki/index.php/CVI "CVI").
* **When a variable has not been defined or has no type suffix, the value defaults to [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE").**
* **Warning: QBasic keyword names cannot be used as numerical variable names with or without the type suffix.**


  




## Examples


*Example 1:* QBasic signed integers were limited from -32768 to 32767, but could not exceed 32767 or it would error:





| ``` [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 2000   i% = i% + 1   [PRINT](/qb64wiki/index.php/PRINT "PRINT") i% [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") i% = 0  ``` |
| --- |


*Explanation:* In **QB64** the count will go to 32767, then count up from -32768 to 0 before repeating the process without error.
  

*Example 2:* When a signed **QB64** INTEGER value exceeds 32767, the value may become a negative value:





| ``` i% = 38000 [PRINT](/qb64wiki/index.php/PRINT "PRINT") i%  ``` |
| --- |




| ``` -27536  ``` |
| --- |


*Explanation:* Use an [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") INTEGER or a ~% variable type suffix for only positive integer values up to 65535.
  

*Example 3:* In **QB64** [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") INTEGER values greater than 65535 cycle over again from zero:





| ``` i~% = 70000 [PRINT](/qb64wiki/index.php/PRINT "PRINT") i~%  ``` |
| --- |




| ```  4464  ``` |
| --- |


*Explanation:* In QB64 an unsigned integer value of 65536 would be 0 with values increasing by the value minus 65536.
  




## See also


* [DIM](/qb64wiki/index.php/DIM "DIM"), [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT")
* [LONG](/qb64wiki/index.php/LONG "LONG"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")
* [LEN](/qb64wiki/index.php/LEN "LEN"), [MKI$](/qb64wiki/index.php/MKI$ "MKI$"), [CVI](/qb64wiki/index.php/CVI "CVI")
* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")
* [&B](/qb64wiki/index.php/%26B "&B") (binary), [&O](/qb64wiki/index.php/%26O "&O") (octal), [&H](/qb64wiki/index.php/%26H "&H") (hexadecimal)
* [Integer Division](/qb64wiki/index.php/%5C "\"), [MOD](/qb64wiki/index.php/MOD "MOD") (Integer remainder division)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INTEGER&oldid=6045>"




## Navigation menu








### Search





















