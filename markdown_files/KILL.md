


KILL - QB64 Phoenix Edition Wiki








# KILL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The KILL statement deletes a file designated by a [STRING](/qb64wiki/index.php/STRING "STRING") value or variable.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


KILL *fileSpec$*
  




* *fileSpec$* is a literal or variable string path and filename. Wildcards \* and ? can be used with caution.


**\*** denotes one or more wildcard letters of a name or extension
**?** denotes one wildcard letter of a name or extension
* *fileSpec$* can include a path that can be either relative to the program's current location or absolute, from the root drive.
* KILL cannot remove an [OPEN](/qb64wiki/index.php/OPEN "OPEN") file. The program must [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") it first.
* If the path or file does not exist, a "File not found" or "Path not found" [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will result. See [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS").
* [SHELL](/qb64wiki/index.php/SHELL "SHELL") "DEL /Q " + fileName$ does the same without a prompt or verification for wildcard deletions.
* [SHELL](/qb64wiki/index.php/SHELL "SHELL") "DEL /P " + fileName$ will ask for user verification.
* Cannot delete folders or directories. Use [RMDIR](/qb64wiki/index.php/RMDIR "RMDIR") to remove empty folders.
* **Warning: files deleted with KILL will not go to the Recycle Bin and they cannot be restored.**


  




## Examples




| ``` KILL "C:\QBasic\data\2000data.dat"  ``` |
| --- |


  




## See also


* [RMDIR](/qb64wiki/index.php/RMDIR "RMDIR"), [FILES](/qb64wiki/index.php/FILES "FILES"), [SHELL](/qb64wiki/index.php/SHELL "SHELL"), [OPEN](/qb64wiki/index.php/OPEN "OPEN")
* [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR"), [MKDIR](/qb64wiki/index.php/MKDIR "MKDIR"), [NAME](/qb64wiki/index.php/NAME "NAME")
* [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS"), [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=KILL&oldid=6059>"




## Navigation menu








### Search





















