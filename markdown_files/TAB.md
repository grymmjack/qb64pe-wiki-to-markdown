


TAB - QB64 Phoenix Edition Wiki








# TAB



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The TAB function is used in [PRINT](/qb64wiki/index.php/PRINT "PRINT") and [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT") statements to move to a specified column position.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


TAB(*column%*)
  




## Description


* Space characters are printed until the print cursor reaches the designated *column%*, overwriting existing characters.
* If a subsequent TAB *column%* is less than the current position, TAB moves the next print to that column on the next row.
* [ASCII](/qb64wiki/index.php/ASCII "ASCII") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(9) can be substituted for sequencial 9 space column moves.
* [Comma](/qb64wiki/index.php/Comma "Comma") PRINT spacing is up to 15 column places (IE: TAB(15)) to a maximum column of 57.
* When printing to a file, a carriage return([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(13)) and linefeed([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(10)) character are output when it moves to the next row.
* **Note:** QBasic did not allow a TAB to be [added](/qb64wiki/index.php/Concatenation "Concatenation") to a string value. In [PRINT](/qb64wiki/index.php/PRINT "PRINT") statements the [plus](/qb64wiki/index.php/%2B "+") would be changed to a [semicolon](/qb64wiki/index.php/Semicolon "Semicolon").


In QB64, TAB [concatenation](/qb64wiki/index.php/Concatenation "Concatenation") is allowed instead of [semicolons](/qb64wiki/index.php/Semicolon "Semicolon"). Example: PRINT "text" + TAB(9) + "here"
  

*Example:* Comparing TAB to [comma](/qb64wiki/index.php/Comma "Comma") print spacing which moves the next text print 15 columns.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") TAB(15); "T" 'TAB spacing  [PRINT](/qb64wiki/index.php/PRINT "PRINT") , "T" 'comma spacing  [PRINT](/qb64wiki/index.php/PRINT "PRINT") TAB(15); "T"; TAB(20); "A"; TAB(15); "B" 'semicolons add nothing to position  [PRINT](/qb64wiki/index.php/PRINT "PRINT") TAB(15); "T", TAB(20); "A"; TAB(15); "B" 'comma moves column position beyond 20  ``` |
| --- |




| ```               T               T               T    A               B               T                    A               B ``` |
| --- |


*Explanation:* TAB moves the PRINT down to the next row when the current column position is more than the TAB position.
  




## See also


* [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT")
* [SPC](/qb64wiki/index.php/SPC "SPC"), [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")
* [STRING$](/qb64wiki/index.php/STRING$ "STRING$")
* [CHR$](/qb64wiki/index.php/CHR$ "CHR$"), [ASCII](/qb64wiki/index.php/ASCII "ASCII")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=TAB&oldid=7977>"




## Navigation menu








### Search





















