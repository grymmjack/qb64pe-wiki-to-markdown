


CHR$ - QB64 Phoenix Edition Wiki








# CHR$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The CHR$ function returns the character associated with a certain [character code](/qb64wiki/index.php/ASCII "ASCII") as a [STRING](/qb64wiki/index.php/STRING "STRING").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result$* = CHR$(*code%*)
  




## Description


* Valid ASCII *code%* numbers range from 0 to 255.
* The character code of a character can be found using the [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)").
* Some control codes below 32 will not [PRINT](/qb64wiki/index.php/PRINT "PRINT") or will move the screen cursor, unless [\_CONTROLCHR OFF](/qb64wiki/index.php/CONTROLCHR "CONTROLCHR") is used.


  




## Examples


*Example 1:* Outputs the characters of several character codes:





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") CHR$(65); CHR$(65 + 32) [PRINT](/qb64wiki/index.php/PRINT "PRINT") CHR$(66); CHR$(66 + 32)  ``` |
| --- |




| ``` Aa Bb  ``` |
| --- |


Explanation: 65 is the ASCII code for "A" and 65 + 32 is the ASCII code for "a". 66 is the ASCII code for "B" and 66 + 32 is the ASCII code for "b"
  

*Example 2:* To cut down on typing CHR$(???) all day, define often used characters as variables such as Q$ = CHR$(34) as shown.





| ```   [DIM](/qb64wiki/index.php/DIM "DIM") Q AS [STRING](/qb64wiki/index.php/STRING "STRING") * 1   'define as one byte string(get rid of $ type suffix too) Q = CHR$(34)          'Q will now represent the elusive quotation mark in a string  PRINT "This text uses "; Q; "quotation marks"; Q; " that could have caused a syntax error!"   ``` |
| --- |




| ``` This text uses "quotation marks" that could have caused a syntax error!  ``` |
| --- |


  

*Example 3:* Using [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)") and CHR$ to *encrypt* a text file size up to 32K bytes





| ``` [OPEN](/qb64wiki/index.php/OPEN "OPEN") FileName$ [FOR](/qb64wiki/index.php/FOR "FOR") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") [AS](/qb64wiki/index.php/AS "AS") #1 ' FileName to be encrypted [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LOF](/qb64wiki/index.php/LOF "LOF")(1) <= 32000 [THEN](/qb64wiki/index.php/THEN "THEN") Text$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")([LOF](/qb64wiki/index.php/LOF "LOF")(1), 1) ' get Text as one string [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1 Send$ = "" ' clear value [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(Text$)     Letter$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(Text$, i, 1) ' get each character in the text     Code = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(Letter$)     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") (Code > 64 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Code < 91) [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") (Code > 96 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Code < 123) [THEN](/qb64wiki/index.php/THEN "THEN")         Letter$ = CHR$(Code + 130) ' change letter's ASCII character by 130     [END IF](/qb64wiki/index.php/END_IF "END IF")     Send$ = Send$ + Letter$ ' reassemble string with just letters encrypted [NEXT](/qb64wiki/index.php/NEXT "NEXT") i [OPEN](/qb64wiki/index.php/OPEN "OPEN") FileName$ [FOR](/qb64wiki/index.php/FOR "FOR") [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT") [AS](/qb64wiki/index.php/AS "AS") #1 ' erase FileName to be encrypted [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #1, Send$   ' Text as one string [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  ``` |
| --- |


*Warning: The routine above will change an original text file to be unreadable. Use a second file name to preserve the original file.*
  

*Example 4:* **Decrypting** the above encrypted text file (32K byte file size limit).





| ``` [OPEN](/qb64wiki/index.php/OPEN "OPEN") FileName$ [FOR](/qb64wiki/index.php/FOR "FOR") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") [AS](/qb64wiki/index.php/AS "AS") #1       ' FileName to be decrypted     Text$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")([LOF](/qb64wiki/index.php/LOF "LOF")(1), 1)         ' open Text as one string [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1 Send$ = "" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(Text$)     Letter$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(Text$, i, 1)     Code = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(Letter$)     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") (Code > 194 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Code < 221) [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") (Code > 226 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Code < 253) [THEN](/qb64wiki/index.php/THEN "THEN")         Letter$ = CHR$(Code - 130)  ' change back to a Letter character     [END IF](/qb64wiki/index.php/END_IF "END IF")     Send$ = Send$ + Letter$ ' reassemble string as normal letters     [NEXT](/qb64wiki/index.php/NEXT "NEXT") i [OPEN](/qb64wiki/index.php/OPEN "OPEN") FileName$ [FOR](/qb64wiki/index.php/FOR "FOR") [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT") [AS](/qb64wiki/index.php/AS "AS") #1 ' Erase file for decrypted text     [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #1, Send$ ' place Text as one string [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* Examples 3 and 4 encrypt and decrypt a file up to 32 thousand bytes. [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$") can only get strings less than 32767 characters. The upper and lower case letter characters are the only ones altered, but the encryption and decryption rely on the fact that most text files do not use the code characters above 193. You could alter any character from ASCII 32 to 125 without problems using the 130 adder. No [ASCII](/qb64wiki/index.php/ASCII "ASCII") code above 255 is allowed. Don't alter the codes below code 32 as they are control characters. Specifically, characters 13 and 10 (CrLf) may be used for line returns in text files.
  




## See also


* [ASC](/qb64wiki/index.php/ASC "ASC"), [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)")
* [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")
* [ASCII character codes](/qb64wiki/index.php/ASCII "ASCII")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CHR$&oldid=8113>"




## Navigation menu








### Search





















