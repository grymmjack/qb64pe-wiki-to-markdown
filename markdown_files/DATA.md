


DATA - QB64 Phoenix Edition Wiki








# DATA



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The DATA statement creates a line of fixed program information separated by commas. The DATA can be later READ by the program at runtime.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


DATA [value1, value2, ...]
  




## Description


* DATA is used at the beginning of every data field line with commas separating the values that follow.
* Values can be any **literal** [STRING](/qb64wiki/index.php/STRING "STRING") or numerical type. **Variables cannot be used.**
* DATA fields can be placed and READ consecutively in the main program code body with or without line labels for [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE").
* DATA is best placed after the main program code.
	+ **QB64** DATA can be placed inside a [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures.
* [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") will only read the first data field if the DATA is not labeled or no label is specified in a RESTORE call.
* When using multiple DATA fields, label each data field with a line label so that each data pointer can be reset for multiple reads with **[RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") *linelabel***.
* QBasic comma separations were flexible to allow column alignments when creating them. QB64 removes spacing between commas.
* [STRING](/qb64wiki/index.php/STRING "STRING") DATA values with end spaces, QBasic keywords and values that include the comma character must be enclosed in quotation marks.
* DATA fields can only be created by the programmer and cannot be changed by a user or lost.
* Comments after a data line require a colon before the comment.
* If a [READ](/qb64wiki/index.php/READ "READ") statement attempts to read past the last data value, an ["Out of Data" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur. Use end of data markers when necessary.
* **DATA fields can be placed after [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures, but line labels are not allowed.**


  




## Examples


*Example 1:* Creating two DATA fields that can be [READ](/qb64wiki/index.php/READ "READ") repeatedly using [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") with the appropriate line label.





| ``` [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") Database2 [READ](/qb64wiki/index.php/READ "READ") A$, B$, C$, D$         'read 4 string values from second DATA field PRINT A$ + B$ + C$ + D$     'note that quoted strings values are spaced  [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") Database1 FOR i = 1 TO 18   [READ](/qb64wiki/index.php/READ "READ") number%                     'read first DATA field 18 times only   PRINT number%; NEXT  END  Database1: DATA 1, 0, 0, 1, 1, 0, 1, 1, 1 DATA 2, 0, 0, 2, 2, 0, 2, 2, 2 :       ' DATA line comments require a colon  Database2: DATA "Hello, ", "world! ", Goodbye, work!  ``` |
| --- |




| ``` Hello world! Goodbyework! 1  0  0  1  1  0  1  1  1  2  0  0  2  2  0  2  2  2  ``` |
| --- |


  

*Example 2:* How to [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") and [READ](/qb64wiki/index.php/READ "READ") DATA in a [SUB](/qb64wiki/index.php/SUB "SUB") procedure in QB64. Line labels can be used for multiple DATA fields.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") num(10) 'shared array or must be passed as a parameter ReadData 2 '<<<<<<< change value to 1 to read other data [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 10   [PRINT](/qb64wiki/index.php/PRINT "PRINT") num(i); [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") ReadData (mode) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") mode = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") mydata1 [ELSE](/qb64wiki/index.php/ELSE "ELSE") [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") mydata2 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 10   [READ](/qb64wiki/index.php/READ "READ") num(i) [NEXT](/qb64wiki/index.php/NEXT "NEXT")  mydata1: DATA 1,2,3,4,5,6,7,8,9,10 mydata2: DATA 10,9,8,7,6,5,4,3,2,1 [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |




| ```  10  9  8  7  6  5  4  3  2  1  ``` |
| --- |


  




## See also


* [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE"). [READ](/qb64wiki/index.php/READ "READ")
* [$EMBED](/qb64wiki/index.php/$EMBED "$EMBED"). [\_EMBEDDED$](/qb64wiki/index.php/EMBEDDED$ "EMBEDDED$")
* [SUB](/qb64wiki/index.php/SUB "SUB"), [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DATA&oldid=8696>"




## Navigation menu








### Search





















