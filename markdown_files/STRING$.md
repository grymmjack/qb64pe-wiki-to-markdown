


STRING$ - QB64 Phoenix Edition Wiki








# STRING$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The STRING$ function returns a [STRING](/qb64wiki/index.php/STRING "STRING") consisting of a single character repeated a number of times.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) 	+ [3.1 More Examples](#More_Examples) * [4 See also](#See_also) |
| --- |


## Syntax


result$ = STRING$(*count&*, {*character$* | *ASCIIcode%*} )
  




## Description


* *count&* is the number of times the character specified by *character* is repeated.
* Character is a literal string character, a string variable or an [ASCII](/qb64wiki/index.php/ASCII "ASCII") code number.
* If *count&* is negative, an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur. The count can be zero.
* If *character* is a [STRING](/qb64wiki/index.php/STRING "STRING") value and its length is zero, an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* If more than one string character value is used, the first character will be repeated.
* A [STRING](/qb64wiki/index.php/STRING "STRING") statement can be added to a string value with the + [concatenation](/qb64wiki/index.php/Concatenation "Concatenation") operator.
* The function result can also be used to [GET](/qb64wiki/index.php/GET "GET") and [PUT](/qb64wiki/index.php/PUT "PUT") a number of bytes as zero characters: bytes$ = STRING(numbytes, 0)


  

*Differences between QB64 and QB 4.5:*



* **QB64** can use [LONG](/qb64wiki/index.php/LONG "LONG") values for a count up to 2,147,483,647 while **QB 4.5** could only use [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values up to 32,767.


  




## Examples


Printing 40 asterisks across the screen using an ASCII character code instead of [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(42).


| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") STRING$(40, 42)  ``` |
| --- |




| ``` ****************************************  ``` |
| --- |


Using a [STRING](/qb64wiki/index.php/STRING "STRING") to specify the repeated character.


| ``` text$ = "B" + STRING$(40, "A") + "D" [PRINT](/qb64wiki/index.php/PRINT "PRINT") text$  ``` |
| --- |




| ``` BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD  ``` |
| --- |


### More Examples


* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [SaveIcon32](/qb64wiki/index.php/SaveIcon32 "SaveIcon32")


  




## See also


* [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")
* [ASC](/qb64wiki/index.php/ASC "ASC"), [CHR$](/qb64wiki/index.php/CHR$ "CHR$")
* [ASCII](/qb64wiki/index.php/ASCII "ASCII")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=STRING$&oldid=8676>"




## Navigation menu








### Search





















