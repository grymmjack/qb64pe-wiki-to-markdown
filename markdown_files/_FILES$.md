


\_FILES$ - QB64 Phoenix Edition Wiki








# \_FILES$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_FILES$ function returns a file or directory name that matches the specified pattern.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*e$* = \_FILES$[(*filespec$*)]
  




## Parameters


* *filespec$* is an optional string expression that specifies a file name or path; may include wildcard characters.


  




## Description


* If you omit *filespec$* when you first call \_FILES$, QB64-PE generates the error message, "Illegal Function Call."
* If *filespec$* is an empty string, then it is assumed to be "**\***" internally.
* \_FILES$ returns the first file or directory name that matches the *filespec$* you specify. To retrieve additional file or directory names that match the *filespec$* pattern, call \_FILES$ again with no argument. When no file or directory names match, \_FILES$ returns an empty string.
* You do not have to retrieve all the file names that match a given *filespec$* before calling \_FILES$ again with a new *filespec$*.
* \_FILES$ is not case sensitive in Windows. However, it is case sensitive in Linux and macOS.
* Because file and directory names are retrieved in no particular order, you may want to store file names in a dynamic array and sort the array.
* Directory names returned, ends with a backslash on Windows and a forward-slash on Linux and macOS.


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.11.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.11.0")

**v3.11.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


Example 1
Prints the names of all ".bas" files in the parent directory.


| ``` [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"):[ONLY](/qb64wiki/index.php/ONLY "ONLY") [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [DIM](/qb64wiki/index.php/DIM "DIM") f [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"): f = _FILES$("../*.bas")  [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [LEN](/qb64wiki/index.php/LEN "LEN")(f) > 0     [PRINT](/qb64wiki/index.php/PRINT "PRINT") f      f = _FILES$ [LOOP](/qb64wiki/index.php/LOOP "LOOP")  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Example 2
Recursively prints the directory tree.


| ``` [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"):[ONLY](/qb64wiki/index.php/ONLY "ONLY") [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [DIM](/qb64wiki/index.php/DIM "DIM") directory [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"): directory = [COMMAND$](/qb64wiki/index.php/COMMAND$ "COMMAND$")  [IF](/qb64wiki/index.php/IF "IF") [NOT](/qb64wiki/index.php/NOT "NOT") [_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")(directory) [THEN](/qb64wiki/index.php/THEN "THEN") directory = [_CWD$](/qb64wiki/index.php/CWD$ "CWD$")  [$IF](/qb64wiki/index.php/$IF "$IF") WINDOWS [THEN](/qb64wiki/index.php/THEN "THEN")     [IF](/qb64wiki/index.php/IF "IF") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(directory, 1) <> "\" [THEN](/qb64wiki/index.php/THEN "THEN") directory = directory + "\" [$ELSE](/qb64wiki/index.php/$ELSE "$ELSE")     [IF](/qb64wiki/index.php/IF "IF") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(directory, 1) <> "/" [THEN](/qb64wiki/index.php/THEN "THEN") directory = directory + "/" [$END IF](/qb64wiki/index.php/$END_IF "$END IF")   PrintDirectory 3, directory  [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") PrintDirectory (L [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), directory [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"))     [DIM](/qb64wiki/index.php/DIM "DIM") entry(0 [TO](/qb64wiki/index.php/TO "TO") 0) [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), n [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")      [DIM](/qb64wiki/index.php/DIM "DIM") CL [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): CL = L     [IF](/qb64wiki/index.php/IF "IF") CL > [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") [THEN](/qb64wiki/index.php/THEN "THEN") CL = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")      [DIM](/qb64wiki/index.php/DIM "DIM") e [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"): e = _FILES$(directory)      [DO](/qb64wiki/index.php/DO "DO")         entry(n) = e         n = n + 1          [IF](/qb64wiki/index.php/IF "IF") n > [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")(entry) [THEN](/qb64wiki/index.php/THEN "THEN") [REDIM](/qb64wiki/index.php/REDIM "REDIM") [_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") entry(0 [TO](/qb64wiki/index.php/TO "TO") n) [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING")          e = _FILES$     [LOOP WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [LEN](/qb64wiki/index.php/LEN "LEN")(e) > 0      [IF](/qb64wiki/index.php/IF "IF") CL > 2 [THEN](/qb64wiki/index.php/THEN "THEN") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , CL - 2 [ELSE](/qb64wiki/index.php/ELSE "ELSE") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , CL     [PRINT](/qb64wiki/index.php/PRINT "PRINT") directory      [DIM](/qb64wiki/index.php/DIM "DIM") i [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")      [WHILE](/qb64wiki/index.php/WHILE "WHILE") i < n         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , CL: [PRINT](/qb64wiki/index.php/PRINT "PRINT") entry(i)          [$IF](/qb64wiki/index.php/$IF "$IF") WINDOWS [THEN](/qb64wiki/index.php/THEN "THEN")             [IF](/qb64wiki/index.php/IF "IF") entry(i) <> ".\" [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") entry(i) <> "..\" [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(entry(i), 1) = "\" [THEN](/qb64wiki/index.php/THEN "THEN") PrintDirectory CL + 2, directory + entry(i)         [$ELSE](/qb64wiki/index.php/$ELSE "$ELSE")             [IF](/qb64wiki/index.php/IF "IF") entry(i) <> "./" [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") entry(i) <> "../" [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(entry(i), 1) = "/" [THEN](/qb64wiki/index.php/THEN "THEN") PrintDirectory CL + 2, directory + entry(i)         [$END IF](/qb64wiki/index.php/$END_IF "$END IF")           i = i + 1     [WEND](/qb64wiki/index.php/WEND "WEND") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2727)
* [FILES](/qb64wiki/index.php/FILES "FILES")
* [\_CWD$](/qb64wiki/index.php/CWD$ "CWD$"), [\_STARTDIR$](/qb64wiki/index.php/STARTDIR$ "STARTDIR$")
* [\_DIR$](/qb64wiki/index.php/DIR$ "DIR$")
* [\_FULLPATH$](/qb64wiki/index.php/FULLPATH$ "FULLPATH$")
* [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS"), [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FILES$&oldid=8968>"




## Navigation menu








### Search





















