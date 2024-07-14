


NAME - QB64 Phoenix Edition Wiki








# NAME



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The NAME statement changes the name of a file or directory to a new name.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


NAME *oldFileOrFolderName$* **AS** *newFileOrFolderName$*
  




## Description


* *oldFileOrFolderName$* and *newFileOrFolderName$* are variables or literal [STRINGs](/qb64wiki/index.php/STRING "STRING") in quotes. Paths can be included.
* If the two paths are different, the statement moves the original file to the new path and renames it.
* If the path is the same or a path is not included, the original file is just renamed.
* [SHELL](/qb64wiki/index.php/SHELL "SHELL") can use *"REN " + filename$ + " " + newname$* for the same purpose (Windows).
* Path or filename [errors](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") are possible and should be handled in the program.
* **Caution: There is no prompt to continue or execution verification.**


  




## Examples




| ```  NAME "BIGBAD.TXT" [AS](/qb64wiki/index.php/AS "AS") "BADWOLF.TXT"  ``` |
| --- |


  




## See also


* [SHELL](/qb64wiki/index.php/SHELL "SHELL"), [MKDIR](/qb64wiki/index.php/MKDIR "MKDIR"), [FILES](/qb64wiki/index.php/FILES "FILES")
* [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR"), [KILL](/qb64wiki/index.php/KILL "KILL"), [RMDIR](/qb64wiki/index.php/RMDIR "RMDIR")
* [Windows Open and Save Dialog Boxes](/qb64wiki/index.php/Windows_Libraries#File_Dialog_Boxes "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=NAME&oldid=7345>"




## Navigation menu








### Search





















