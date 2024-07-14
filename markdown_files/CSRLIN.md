


CSRLIN - QB64 Phoenix Edition Wiki








# CSRLIN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The CSRLIN function returns the current text row position of the [PRINT](/qb64wiki/index.php/PRINT "PRINT") cursor.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*row%* = CSRLIN
  




## Description


* The value returned is within the range of 1 to the current number of rows in the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode used.
	+ In [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 (text mode), the [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") function returns the number of text rows.
	+ In graphic modes, the number of available text rows can be calculated by dividing [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") (measured in pixels in graphic modes) by [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT"): ***totalRows%* = \_HEIGHT / \_FONTHEIGHT**
* In screen modes that support page flipping, the CSRLIN function returns the vertical coordinate of the cursor on the active page.
* x = [POS](/qb64wiki/index.php/POS "POS")(0) returns the column location of the cursor.


  




## Examples


*Example:* A semicolon stops the print cursor immediately after the print.





| ```   LOCATE 5, 5: PRINT "HELLO ";   Y = CSRLIN 'save the row   X = [POS](/qb64wiki/index.php/POS "POS")(0) 'save the column   LOCATE 10, 10: PRINT "WORLD"   LOCATE Y, X 'restore saved position   PRINT "GOODBYE"  ``` |
| --- |




| ```               HELLO GOODBYE              WORLD    ``` |
| --- |


*Explanation:* "HELLO " is printed and the semicolon stops the cursor immediately after the text. The CSRLIN variable records the current print cursor's text row in Y. The [POS](/qb64wiki/index.php/POS "POS") function records the current print cursor's text column in X. The second [PRINT](/qb64wiki/index.php/PRINT "PRINT") statement displays the comment "WORLD" on the 10th line of the screen. The last [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") statement restores the position of the cursor to the original line and column immediately after the first print.
  




## See also


* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE"), [POS](/qb64wiki/index.php/POS "POS")
* [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (graphic print)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CSRLIN&oldid=7247>"




## Navigation menu








### Search





















