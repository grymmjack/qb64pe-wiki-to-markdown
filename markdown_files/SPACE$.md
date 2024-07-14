


SPACE$ - QB64 Phoenix Edition Wiki








# SPACE$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The SPACE$ function returns a [STRING](/qb64wiki/index.php/STRING "STRING") consisting of a number of space characters.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*result$* = **SPACE$(*count&*)**
  




## Parameters


* *count&* is the number of space characters to repeat. Cannot use negative values!


  




## Description


* Semicolons can be used to combine spaces with text [STRING](/qb64wiki/index.php/STRING "STRING") or numerical values.
* [Concatenation](/qb64wiki/index.php/Concatenation "Concatenation") using + can be used to combine [STRING](/qb64wiki/index.php/STRING "STRING") text values only.
* Spaces are often used to erase previous text PRINTs from the screen.
* The function result can also be used to [GET](/qb64wiki/index.php/GET "GET") and [PUT](/qb64wiki/index.php/PUT "PUT") a number of bytes as zero characters: bytes$ = SPACE$(numbytes)
* Spaces can also be made using [SPC](/qb64wiki/index.php/SPC "SPC"), [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(32) or [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(n%, 32).


  

*Differences between QB64 and QB 4.5:*



* **QB64** can use [LONG](/qb64wiki/index.php/LONG "LONG") values for count up to 2,147,483,647 while **QB 4.5** could only use [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values up to 32,767.


  




## Examples


*Example 1:* How to space text in a [PRINT](/qb64wiki/index.php/PRINT "PRINT") statement using SPACE$ with string [concatenation](/qb64wiki/index.php/Concatenation "Concatenation").





| ``` [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") count% = 0 [TO](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") 3     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "abc" + SPACE$( count% ) + "def" [NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") count%  ``` |
| --- |




| ``` abcdef abc def abc  def abc   def  ``` |
| --- |


  

*Example 2:* In [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 SPACE$ can be used to change the background color to make an American flag.





| ```  USA flag centered on screen with thin horizontal red & white stripes ' blue corner field with randomly twinkling stars [CLS](/qb64wiki/index.php/CLS "CLS") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 25, 1 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press any key to stop twinkling"; [COLOR](/qb64wiki/index.php/COLOR "COLOR") , 4 z = 15 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") x = 5 [TO](/qb64wiki/index.php/TO "TO") 19          '13 red & white stripes (x =5 to 21 for 15 stripes)     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") z = 15 [THEN](/qb64wiki/index.php/THEN "THEN") z = 4 [ELSE](/qb64wiki/index.php/ELSE "ELSE") z = 15     [COLOR](/qb64wiki/index.php/COLOR "COLOR") , z     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") x, 15     [PRINT](/qb64wiki/index.php/PRINT "PRINT") SPACE$(55) [NEXT](/qb64wiki/index.php/NEXT "NEXT") x [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") x = 5 [TO](/qb64wiki/index.php/TO "TO") 11          'blue field in upper left quadrant (x = 5 to 13 to hold all 50 stars)     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15, 1            'sits above 4th white stripe     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") x, 15     [PRINT](/qb64wiki/index.php/PRINT "PRINT") SPACE$(23) [NEXT](/qb64wiki/index.php/NEXT "NEXT") x DO     stop$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") x = 5 [TO](/qb64wiki/index.php/TO "TO") 10 [STEP](/qb64wiki/index.php/STEP "STEP") 2  '39 stars staggered across blue field (50 stars if x = 5 to 12)         w = 16         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y = 1 [TO](/qb64wiki/index.php/TO "TO") 6      '5 rows of 6 stars             r = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 6)             [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") r = 0 [THEN](/qb64wiki/index.php/THEN "THEN") z = 31 [ELSE](/qb64wiki/index.php/ELSE "ELSE") z = 15             [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") stop$ = "" [THEN](/qb64wiki/index.php/THEN "THEN") [COLOR](/qb64wiki/index.php/COLOR "COLOR") z [ELSE](/qb64wiki/index.php/ELSE "ELSE") [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15             [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") x, w             w = w + 4             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "*";         [NEXT](/qb64wiki/index.php/NEXT "NEXT") y         w = 18         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y = 1 [TO](/qb64wiki/index.php/TO "TO") 5      '5 rows of 5 stars             r = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 6)             [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") r = 0 [THEN](/qb64wiki/index.php/THEN "THEN") z = 31 [ELSE](/qb64wiki/index.php/ELSE "ELSE") z = 15             [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") stop$ = "" [THEN](/qb64wiki/index.php/THEN "THEN") [COLOR](/qb64wiki/index.php/COLOR "COLOR") z [ELSE](/qb64wiki/index.php/ELSE "ELSE") [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15             [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") x + 1, w             w = w + 4             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "*";         [NEXT](/qb64wiki/index.php/NEXT "NEXT") y     [NEXT](/qb64wiki/index.php/NEXT "NEXT") x     w = 16     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y = 1 [TO](/qb64wiki/index.php/TO "TO") 6          '1 row of 6 stars             r = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 6)             [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") r = 0 [THEN](/qb64wiki/index.php/THEN "THEN") z = 31 [ELSE](/qb64wiki/index.php/ELSE "ELSE") z = 15         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") stop$ = "" [THEN](/qb64wiki/index.php/THEN "THEN") [COLOR](/qb64wiki/index.php/COLOR "COLOR") z [ELSE](/qb64wiki/index.php/ELSE "ELSE") [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") x, w         w = w + 4         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "*";     [NEXT](/qb64wiki/index.php/NEXT "NEXT") y     t = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")     [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") t + .2 >= [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") stop$ = "" [COLOR](/qb64wiki/index.php/COLOR "COLOR") 7, 0 [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Solitaire
*Explanation:* In [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0, the background color is only placed with the the printed text and spaces. [CLS](/qb64wiki/index.php/CLS "CLS") can color the entire screen.
  




## See also


* [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING")
* [STRING$](/qb64wiki/index.php/STRING$ "STRING$"), [CLS](/qb64wiki/index.php/CLS "CLS")
* [SPC](/qb64wiki/index.php/SPC "SPC"), [TAB](/qb64wiki/index.php/TAB "TAB")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SPACE$&oldid=8065>"




## Navigation menu








### Search





















