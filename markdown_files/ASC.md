


ASC - QB64 Phoenix Edition Wiki








# ASC



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **ASC** statement allows a program to change a character at any position of a [STRING](/qb64wiki/index.php/STRING "STRING") variable.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


ASC(*stringExpression$*[, *position%*]) = *code%*
  




## Description


* **Note:** The statement variant of **ASC** is not available in QBasic/QuickBASIC, but in **QB64 only**.
* The *stringExpression$* variable's value must have been previously defined and cannot be an empty string ("").
* *position%* is optional. If no position is used, the leftmost character at position 1 is assumed.
* *position%* cannot be zero or greater than the string's length or an [Illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* The [ASCII](/qb64wiki/index.php/ASCII "ASCII") replacement *code%* value can be any [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value from 0 to 255.


  




## Examples


Example
Demonstrates how to change existing text characters one letter at a time.


| ``` a$ = "YZC" ASC(a$) = 65                 ' CHR$(65) = "A" ASC(a$, 2) = 66              ' CHR$(66) = "B" [PRINT](/qb64wiki/index.php/PRINT "PRINT") a$  ASC(a$, 2) = 32              ' CHR$(32) = " " [PRINT](/qb64wiki/index.php/PRINT "PRINT") a$  ASC(a$, 2) = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("S")        ' get code value from ASC function [PRINT](/qb64wiki/index.php/PRINT "PRINT") a$  ``` |
| --- |




| ``` ABC A C ASC  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1149)
* [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)")
* [MID$](/qb64wiki/index.php/MID$ "MID$"), [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)")
* [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"), [ASCII](/qb64wiki/index.php/ASCII "ASCII")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ASC&oldid=8892>"




## Navigation menu








### Search





















