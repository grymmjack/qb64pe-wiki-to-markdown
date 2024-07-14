


SPC - QB64 Phoenix Edition Wiki








# SPC



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The SPC function is used in [PRINT](/qb64wiki/index.php/PRINT "PRINT") and [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT") statements to print or output a number of space characters.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


**SPC(*count%*)**
  




## Parameters


* *count* designates the number of column spaces to move the cursor in a [PRINT](/qb64wiki/index.php/PRINT "PRINT") statement.


  




## Description


* When used in a [PRINT](/qb64wiki/index.php/PRINT "PRINT") statement,
	+ *count%* is the number of space characters to print, overwriting existing characters.
	+ If *count%* is greater than the number of columns left in the current row, remaining space characters are printed on the next row.
* When used in a [PRINT #](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") statement,
	+ *count%* is the number of space characters to output.
	+ If *count%* is less than or equal to zero, the function has no effect.


  




## Examples


*Example:* Using SPC to space a text print.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "123456789" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "abc" ; SPC(3) ; "123" ``` |
| --- |




| ``` 123456789 abc   123  ``` |
| --- |


  




## See also


* [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [PRINT #](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)")
* [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT"), [STRING$](/qb64wiki/index.php/STRING$ "STRING$")
* [TAB](/qb64wiki/index.php/TAB "TAB"), [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SPC&oldid=7420>"




## Navigation menu








### Search





















