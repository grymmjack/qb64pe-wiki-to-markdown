


POS - QB64 Phoenix Edition Wiki








# POS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **POS** function returns the current print cursor text column position.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


column% = POS(0)
  




* The value in parenthesis is normally 0, but any numerical value or variable could be used for compatibility with Basic.
* When a semicolon ends the previous PRINT statement the cursor column position will be after the last character printed.
* If [TAB](/qb64wiki/index.php/TAB "TAB") or a comma is used the column position will be immediately after the tabbed position normally 9 spaces after text
* If a [PRINT](/qb64wiki/index.php/PRINT "PRINT") statement does not use a semicolon or comma at the end, the return value will be 1 on the next row.
* Column position returned can be saved to return to a previous print position later using [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE").


  

*Example:* Column positions after prints.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") POS(0) 'column position always starts on 1 at top of new or after [CLS](/qb64wiki/index.php/CLS "CLS") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "hello"; 'column position is 6 on same row immediately after text [PRINT](/qb64wiki/index.php/PRINT "PRINT") POS(0) [PRINT](/qb64wiki/index.php/PRINT "PRINT") 'start new row [PRINT](/qb64wiki/index.php/PRINT "PRINT") "hello", 'column position is 15 on same row (normally tabs 9 spaces) [PRINT](/qb64wiki/index.php/PRINT "PRINT") POS(0) [PRINT](/qb64wiki/index.php/PRINT "PRINT") 'start new row [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") POS(0) ' column position is 1 on next row  ``` |
| --- |


*Note:* Column tab prints may not always move 9 spaces past the center of the screen. Some may move text to next row.


  




## See also


* [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN"), [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE"), [PRINT](/qb64wiki/index.php/PRINT "PRINT")
* [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=POS&oldid=7649>"




## Navigation menu








### Search





















