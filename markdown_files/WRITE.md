


WRITE - QB64 Phoenix Edition Wiki








# WRITE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The WRITE statement writes a [comma](/qb64wiki/index.php/Comma "Comma")-separated list of values to the screen without spacing.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


WRITE [*expression, List*]
  




## Description


* *expressionList* is a comma-separated list of variable or literal values to be written to the screen.
* Write statement separates displayed values using [comma](/qb64wiki/index.php/Comma "Comma") separators(required) that will display on the screen.
* Leading and trailing number spaces are omitted when displaying numerical values.
* [String](/qb64wiki/index.php/STRING "STRING") [quotation marks](/qb64wiki/index.php/Quotation_mark "Quotation mark") will also be displayed.
* [Semicolons](/qb64wiki/index.php/Semicolon "Semicolon") cannot be used in or following the WRITE statement!


  

*Example:* Comparing WRITE to the same PRINT statement.





| ``` a% = 123 b$ = "Hello" c! = 3.1415  [PRINT](/qb64wiki/index.php/PRINT "PRINT") a%, b$, c!   'commas display tab spaced data WRITE a%, b$, c!   'displays commas between values, strings retain end quotes  ``` |
| --- |




| ``` 123        Hello      3.1415 123,"Hello",3.1415  ``` |
| --- |


  




## See also


* [WRITE #](/qb64wiki/index.php/WRITE_(file_statement) "WRITE (file statement)")
* [INPUT #](/qb64wiki/index.php/INPUT_(file_statement) "INPUT (file statement)")
* [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [PRINT #](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)")
* [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=WRITE&oldid=6632>"




## Navigation menu








### Search





















