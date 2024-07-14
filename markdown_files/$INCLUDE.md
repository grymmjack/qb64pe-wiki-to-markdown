


$INCLUDE - QB64 Phoenix Edition Wiki








# $INCLUDE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
$INCLUDE is a metacommand that is used to insert a source code file into your program which is then executed at the point of the insertion.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 How to $INCLUDE a BAS or Text file with a QB64 Program](#How_to_$INCLUDE_a_BAS_or_Text_file_with_a_QB64_Program) * [3 Examples](#Examples) 	+ [3.1 More examples](#More_examples) * [4 See also](#See_also) |
| --- |


## Syntax


{[REM](/qb64wiki/index.php/REM "REM") | ['](/qb64wiki/index.php/Apostrophe "Apostrophe") } $INCLUDE**:** '*sourceFile*'
  




## Description


* QBasic [metacommands](/qb64wiki/index.php/Metacommand "Metacommand") must be commented with [REM](/qb64wiki/index.php/REM "REM") or an apostrophe.
* The *sourceFile* name must be enclosed in apostrophes and can include a path.
* $INCLUDE is often used to add functions and subs from an external text QBasic code library.
* The $INCLUDE metacommand should be the only statement on a line.


### How to $INCLUDE a BAS or Text file with a QB64 Program


* Assemble the code to be reused into a file.
* Common extensions are **.BI** (for declarations, usually included in the beginning of a program) or **.BM** (with SUBs and FUNCTIONs, usually included at the end of a program).
	+ Any extension can be used, as long as the file contains code in plain text (binary files are not accepted).
* $INCLUDE any [DIM](/qb64wiki/index.php/DIM "DIM"), [CONST](/qb64wiki/index.php/CONST "CONST"), [SHARED](/qb64wiki/index.php/SHARED "SHARED") arrays or [DATA](/qb64wiki/index.php/DATA "DATA") at the **beginning** of the main program code.
* $INCLUDE [SUBs](/qb64wiki/index.php/SUB "SUB") or [FUNCTIONs](/qb64wiki/index.php/FUNCTION "FUNCTION") at the bottom of the main program code **after any SUB procedures.**
	+ **Note:** [TYPE](/qb64wiki/index.php/TYPE "TYPE") definitions, [DATA](/qb64wiki/index.php/DATA "DATA") and [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") can be placed inside of sub-procedures.
* **Compile** the program.
* *Note: Once the program is compiled, the included text files are no longer needed with the program EXE.*


  




## Examples




| ```  **'$INCLUDE:** 'QB.BI' ``` |
| --- |


### More examples


* [SelectScreen](/qb64wiki/index.php/SelectScreen "SelectScreen")
* [FILELIST$](/qb64wiki/index.php/FILELIST$ "FILELIST$")
* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")


  




## See also


* [INTERRUPT](/qb64wiki/index.php/INTERRUPT "INTERRUPT"), [INTERRUPTX](/qb64wiki/index.php/INTERRUPTX "INTERRUPTX")
* [TYPE](/qb64wiki/index.php/TYPE "TYPE"), [DIM](/qb64wiki/index.php/DIM "DIM")
* [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$INCLUDE&oldid=8655>"




## Navigation menu








### Search





















