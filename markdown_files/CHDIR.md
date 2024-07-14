


CHDIR - QB64 Phoenix Edition Wiki








# CHDIR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The CHDIR statement changes the program's location from one working directory to another by specifying a literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") path.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


CHDIR *path$*
  




## Description


* *path$* is the new directory path the program will work in.
* *path$* can be an absolute path (starting from the root folder) or relative path (starting from the current program location).
* If *path$* specifies a non-existing path, a ["Path not found"](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* **A QB64 [SHELL](/qb64wiki/index.php/SHELL "SHELL") statement cannot use "CD " or "CHDIR " + path$ to change directories.**


  




## Examples


*Example 1:* The following code is Windows-specific:





| ``` CHDIR "C:\"      'change to the root drive C (absolute path) CHDIR "DOCUME~1" 'change to "C:\Documents and Settings" from root drive (relative path) CHDIR "..\"      'change back to previous folder one up  ``` |
| --- |


*Details:* **QB64** can use long or short (8.3 notation) file and path names.
  

*Example 2:* Using the Windows API to find the current program's name and root path. The PATH$ is a shared function value.





| ``` [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "My program" [PRINT](/qb64wiki/index.php/PRINT "PRINT") TITLE$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") PATH$  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") TITLE$ *=== SHOW CURRENT PROGRAM* [SHARED](/qb64wiki/index.php/SHARED "SHARED") PATH$           'optional path information shared with main module only [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")        'Directory Information using KERNEL32 provided by Dav   [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") GetModuleFileNameA ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") Module [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), FileName [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") nSize [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")) [END DECLARE](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")  FileName$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(256) Result = GetModuleFileNameA(0, FileName$, [LEN](/qb64wiki/index.php/LEN "LEN")(FileName$))  '0 designates the current program [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Result [THEN](/qb64wiki/index.php/THEN "THEN")             'Result returns the length or bytes of the string information   PATH$ = [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(FileName$, Result)   start = 1   DO     posit = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(start, PATH$, "\")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") posit [THEN](/qb64wiki/index.php/THEN "THEN") last = posit     start = posit + 1   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") posit = 0   TITLE$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(PATH$, last + 1)   PATH$ = [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(PATH$, last) [ELSE](/qb64wiki/index.php/ELSE "ELSE") TITLE$ = "": PATH$ = "" [END IF](/qb64wiki/index.php/END_IF "END IF") [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


**Note:** The program's [\_TITLE](/qb64wiki/index.php/TITLE "TITLE") name may be different from the actual program module's file name returned by Windows.
  




## See also


* [SHELL](/qb64wiki/index.php/SHELL "SHELL"), [FILES](/qb64wiki/index.php/FILES "FILES")
* [MKDIR](/qb64wiki/index.php/MKDIR "MKDIR"), [RMDIR](/qb64wiki/index.php/RMDIR "RMDIR")
* [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CHDIR&oldid=8112>"




## Navigation menu








### Search





















