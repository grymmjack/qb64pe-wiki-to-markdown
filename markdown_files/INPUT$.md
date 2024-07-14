


INPUT$ - QB64 Phoenix Edition Wiki








# INPUT$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The INPUT$ function is used to receive data from the user's keyboard, an open file or an open port.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result$* = INPUT$(*numberOfBytes%*[, fileOrPortNumber])
  




## Description


* Keyboard input is limited to the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") *numberOfBytes%* (characters) designated by program.
* The keyboard is the default device when a file or port number is omitted. The *numberOfBytes%* is number of key presses to read.
* INPUT$ will wait until the number of bytes are read from the keyboard or port. One byte per loop is recommended with ports.
* [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") opened file bytes can be up to the [LEN](/qb64wiki/index.php/LEN "LEN") = recordLength statement, or 128 if no statement is used.
* fileOrPortNumber is the number that was used in the [OPEN](/qb64wiki/index.php/OPEN "OPEN") AS statement.
* Returns [STRING](/qb64wiki/index.php/STRING "STRING") values including spaces or even extended [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters.
* Backspace key results in the [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(8) character being added to an entry.
* Use [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , , 1 to view the cursor entry. Turn the cursor off using [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , , 0.
* Use [\_DEST](/qb64wiki/index.php/DEST "DEST") [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") before INPUT$ is used to receive input from a [console](/qb64wiki/index.php/$CONSOLE "$CONSOLE") window.


### QBasic/QuickBASIC


* *numberOfBytes%* could not exceed 32767 in [BINARY](/qb64wiki/index.php/BINARY "BINARY") files or a QBasic error would occur.
* Ctrl + Break would not interrupt the QBasic program until there was a full INPUT$ key entry. In **QB64** Ctrl + Break will immediately exit a running program.


  




## Examples


*Example 1:* A keyboard limited length entry can be made with a fixed blinking cursor. Entry must be completed before it can be shown.





| ``` [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 10, 1         'display fixed cursor at location year$ = INPUT$(4)        'waits until all 4 digits are entered PRINT year$              'display the text entry  ``` |
| --- |


  

*Example 2:* Reading bytes from a text file for an 80 wide screen mode.





| ``` [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 5, 5, 1                    'locate and display cursor [OPEN](/qb64wiki/index.php/OPEN "OPEN") "Diary.txt" FOR [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") AS #1  'open existing text file text$ = INPUT$(70, 1) [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 5, 6, 0: PRINT text$       'print text and turn cursor off  ``` |
| --- |


  

*Example 3:* Getting the entire text file data as one string value.





| ``` [OPEN](/qb64wiki/index.php/OPEN "OPEN") "Diary.txt FOR [BINARY](/qb64wiki/index.php/BINARY "BINARY") AS #1  'open an existing file up to 32767 bytes IF [LOF](/qb64wiki/index.php/LOF "LOF")(1) <= 32767 THEN Text$ = INPUT$(LOF(1), 1) [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  ``` |
| --- |


*Explanation:* The IF statement gets the entire contents when the file size is less than 32768. The program can then work with the string by using [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)") or [INSTR](/qb64wiki/index.php/INSTR "INSTR"). Note: A text file string will also have **CrLf** line break end characters [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(13) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(10).
  




## See also


* [INPUT](/qb64wiki/index.php/INPUT "INPUT"), [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") (keyboard input)
* [INPUT (file mode)](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)"), [INPUT #](/qb64wiki/index.php/INPUT_(file_statement) "INPUT (file statement)"), [LINE INPUT #](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") (file input)
* [OPEN](/qb64wiki/index.php/OPEN "OPEN"), [LOC](/qb64wiki/index.php/LOC "LOC") (file)
* [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") (cursor on/off)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INPUT$&oldid=8136>"




## Navigation menu








### Search





















