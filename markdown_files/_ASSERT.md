


\_ASSERT - QB64 Phoenix Edition Wiki








# \_ASSERT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ASSERT statement can be used to perform tests in code that's in development, for debugging purposes.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_ASSERT *condition*[, *errorMessage$*]
  




## Description


* *condition* is the condition that must be met in order to consider the \_ASSERT valid.
* Optional *errorMessage$* is the message to be displayed in the console window if [$ASSERTS:CONSOLE](/qb64wiki/index.php/$ASSERTS "$ASSERTS") is used.
* If the condition is not met (that is, if it evaluates to 0), an error occurs ("\_ASSERT failed on line #") and program execution stops.


  




## Availability


* **Version 1.4 and up**.


  




## Examples


*Example:* Adding test checks for parameter inputs in a function.





| ``` [$ASSERTS](/qb64wiki/index.php/$ASSERTS "$ASSERTS"):CONSOLE  [DO](/qb64wiki/index.php/DO "DO")     a = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 10)     b$ = myFunc$(a)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") a, , b$     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 3 [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") myFunc$ (value [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"))     _ASSERT value > 0, "Value cannot be zero"     _ASSERT value <= 10, "Value cannot exceed 10"      [IF](/qb64wiki/index.php/IF "IF") value > 1 [THEN](/qb64wiki/index.php/THEN "THEN") plural$ = "s"     myFunc$ = [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(value, "*") + [STR$](/qb64wiki/index.php/STR$ "STR$")(value) + " star" + plural$ + " :-)" [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


  




## See also


* [$ASSERTS](/qb64wiki/index.php/$ASSERTS "$ASSERTS")
* [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING")
* [Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ASSERT&oldid=8261>"




## Navigation menu








### Search





















