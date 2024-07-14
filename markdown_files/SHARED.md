


SHARED - QB64 Phoenix Edition Wiki








# SHARED



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **SHARED** statement allows variables to be passed automatically to any [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedure.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


DIM SHARED Qt AS STRING \* 1
  




* [DIMensioned](/qb64wiki/index.php/DIM "DIM") variables are shared with all procedures in the program module.
* When used with [DIM](/qb64wiki/index.php/DIM "DIM") in the main module, it eliminates the need to pass a parameter variable to a [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION").
* Use [COMMON SHARED](/qb64wiki/index.php/COMMON_SHARED "COMMON SHARED") to share a list of variable values with sub-procedures or other modules. See also: [COMMON](/qb64wiki/index.php/COMMON "COMMON")
* SHARED (**without [DIM](/qb64wiki/index.php/DIM "DIM")**) can share a list of variables inside of [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures with the main module only.


**Note: SHARED variables in sub-procedures will not be passed to other sub-procedures, only the main module.**
  

*Example 1:* Defining variable types with [AS](/qb64wiki/index.php/AS "AS") or type suffixes.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") SHARED Qt AS [STRING](/qb64wiki/index.php/STRING "STRING") * 1, price AS [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"), ID AS [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") SHARED Q$, prices#, IDs%  ``` |
| --- |


  

*Example 2:* The DIR$ function returns a filename or a list when more than one exist. The file spec can use a path and/or wildcards.





| ``` [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 2   [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") "Enter a file spec: ", spec$   file$ = DIR$(spec$)        'use a file spec ONCE to find the last file name listed   [PRINT](/qb64wiki/index.php/PRINT "PRINT") DIRCount%, file$,    'function can return the file count using SHARED variable   [DO](/qb64wiki/index.php/DO "DO")     K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1)     file$ = DIR$("")         'use an empty string parameter to return a list of files!     [PRINT](/qb64wiki/index.php/PRINT "PRINT") file$,   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [LEN](/qb64wiki/index.php/LEN "LEN")(file$) = 0  'file list ends with an empty string [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") DIR$ (spec$) [CONST](/qb64wiki/index.php/CONST "CONST") TmpFile$ = "DIR$INF0.INF", ListMAX% = 500  'change maximum to suit your needs SHARED DIRCount%                                 'returns file count if desired [STATIC](/qb64wiki/index.php/STATIC "STATIC") Ready%, Index%, DirList$() [IF](/qb64wiki/index.php/IF "IF") [NOT](/qb64wiki/index.php/NOT "NOT") Ready% [THEN](/qb64wiki/index.php/THEN "THEN") [REDIM](/qb64wiki/index.php/REDIM "REDIM") DirList$(ListMax%): Ready% = -1  'DIM array first use [IF](/qb64wiki/index.php/IF "IF") spec$ > "" [THEN](/qb64wiki/index.php/THEN "THEN")                               'get file names when a spec is given   [SHELL](/qb64wiki/index.php/SHELL "SHELL") [_HIDE](/qb64wiki/index.php/HIDE "HIDE") "DIR " + spec$ + " /b > " + TmpFile$   Index% = 0: DirList$(Index%) = "": ff% = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE")   [OPEN](/qb64wiki/index.php/OPEN "OPEN") TmpFile$ [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [APPEND](/qb64wiki/index.php/APPEND "APPEND") [AS](/qb64wiki/index.php/AS "AS") #ff%   size& = [LOF](/qb64wiki/index.php/LOF "LOF")(ff%)   [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #ff%   [IF](/qb64wiki/index.php/IF "IF") size& = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [KILL](/qb64wiki/index.php/KILL "KILL") TmpFile$: [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION")   [OPEN](/qb64wiki/index.php/OPEN "OPEN") TmpFile$ [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") [AS](/qb64wiki/index.php/AS "AS") #ff%   [DO](/qb64wiki/index.php/DO "DO") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [NOT](/qb64wiki/index.php/NOT "NOT") [EOF](/qb64wiki/index.php/EOF "EOF")(ff%) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Index% < ListMAX%     Index% = Index% + 1     [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") #ff%, DirList$(Index%)   [LOOP](/qb64wiki/index.php/LOOP "LOOP")   DIRCount% = Index%                       'SHARED variable can return the file count   [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #ff%   [KILL](/qb64wiki/index.php/KILL "KILL") TmpFile$ [ELSE](/qb64wiki/index.php/ELSE "ELSE") [IF](/qb64wiki/index.php/IF "IF") Index% > 0 [THEN](/qb64wiki/index.php/THEN "THEN") Index% = Index% - 1 'no spec sends next file name [END IF](/qb64wiki/index.php/END_IF "END IF") DIR$ = DirList$(Index%) [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* The SHARED variable value *DIRcount%* can tell the main program how many files were found using a wildcard spec.
  




## See also


* [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM")
* [COMMON](/qb64wiki/index.php/COMMON "COMMON"), [COMMON SHARED](/qb64wiki/index.php/COMMON_SHARED "COMMON SHARED")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SHARED&oldid=7955>"




## Navigation menu








### Search





















