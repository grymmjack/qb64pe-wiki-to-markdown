


RUN - QB64 Phoenix Edition Wiki








# RUN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**RUN** is a control flow statement that clears and restarts the program currently in memory or executes another specified program.


The multi-modular technique goes back to when QBasic and QuickBASIC had module size constraints. In QB64 it has been implemented so that that older code can still be compiled, though **it is advisable to use single modules for a single project (not counting [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") libraries), for ease of sharing and also because the module size constraints no longer exist.**


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 See also](#See_also) |
| --- |


## Syntax


**RUN** [{*line\_number* | *filespec$*}] [*command\_parameter(s)*]
  




## Parameters


* *line number* specifies a line number in the main module code.
* An optional *filespec* specifies a program to load into memory and run.


\* BAS or EXE extensions are assumed to be the same as the calling module's extension, EXE or BAS (QBasic only).
\* *file names specs* with other extensions must use the full filename. No extension requires a dot.
* In **QB64** *command line parameters* can follow the program file name and be read using the [COMMAND$](/qb64wiki/index.php/COMMAND$ "COMMAND$") function later.


  

*Usage:*



* The starting [line number](/qb64wiki/index.php/Line_number "Line number") MUST be one used in the main module code, even if RUN is called from within a SUB or FUNCTION.
* If no line number is given the currently loaded program runs from the first executable line.
* In **QB64** RUN can open any kind of executable program and provide case sensitive program specific parameters.
	+ Recommended practice to run external programs is to use [SHELL](/qb64wiki/index.php/SHELL "SHELL").
* RUN closes all open files and closes the invoking program module before the called program starts.
* RUN resets the [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") sequence to the starting [RND](/qb64wiki/index.php/RND "RND") function value.
* **Note: Calling RUN repeatedly may cause a stack leak in QB64 if it is called from within a [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION"). Avoid when possible.**


  

*Example 1:* Shows how RUN can reference multiple line numbers in the main module code. No line number executes first code line.





| ``` PRINT " A", " B", " C", " D" 10 A = 1 20 B = 2 30 C = 3 40 D = 4 50 [PRINT](/qb64wiki/index.php/PRINT "PRINT") A, B, C, D 60 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") A = 0 [THEN](/qb64wiki/index.php/THEN "THEN") 70 [ELSE](/qb64wiki/index.php/ELSE "ELSE") RUN 20    'RUN clears all values 70 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") B = 0 [THEN](/qb64wiki/index.php/THEN "THEN") 80 [ELSE](/qb64wiki/index.php/ELSE "ELSE") RUN 30 80 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") C = 0 [THEN](/qb64wiki/index.php/THEN "THEN") 90 [ELSE](/qb64wiki/index.php/ELSE "ELSE") RUN 40 90 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") D = 0 [THEN](/qb64wiki/index.php/THEN "THEN") 100 [ELSE](/qb64wiki/index.php/ELSE "ELSE") RUN 50 100 [PRINT](/qb64wiki/index.php/PRINT "PRINT") [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Do you want to quit?(Y/N)", quit$ [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(quit$) = "Y" [THEN](/qb64wiki/index.php/THEN "THEN") [END](/qb64wiki/index.php/END "END") [ELSE](/qb64wiki/index.php/ELSE "ELSE") RUN  'RUN without line number executes at first code line   ``` |
| --- |




| ``` A       B       C       D 1       2       3       4 0       2       3       4 0       0       3       4 0       0       0       4 0       0       0       0  Do you want to quit?(Y/N)_  ``` |
| --- |


  




## See also


* [CHAIN](/qb64wiki/index.php/CHAIN "CHAIN"), [SHELL](/qb64wiki/index.php/SHELL "SHELL")
* [COMMAND$](/qb64wiki/index.php/COMMAND$ "COMMAND$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RUN&oldid=7395>"




## Navigation menu








### Search





















