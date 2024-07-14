


MKDIR - QB64 Phoenix Edition Wiki








# MKDIR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The MKDIR statement creates a new folder (**dir**ectory) at a specified path.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


MKDIR pathSpec$
  




## Description


* The path specification (pathSpec$) is a literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") expression that also specifies the new folder's name.
* If no path is given the directory will become a sub-directory of the present directory where the program is currently running.
* **QB64** can use both long or short path and file names with spaces when required.
* The new folder will be created without a user prompt or verification.
* If a path is specified, the path must exist or a ["Path not found" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur. See [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS").
* [SHELL](/qb64wiki/index.php/SHELL "SHELL") can use the DOS command "MD " or "MKDIR " + path$ + newfolder$ to do the same thing.


  




## See also


* [SHELL](/qb64wiki/index.php/SHELL "SHELL"), [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR"), [FILES](/qb64wiki/index.php/FILES "FILES")
* [NAME](/qb64wiki/index.php/NAME "NAME"), [KILL](/qb64wiki/index.php/KILL "KILL"), [RMDIR](/qb64wiki/index.php/RMDIR "RMDIR")
* [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")
* [Windows Open and Save Dialog Boxes](/qb64wiki/index.php/Windows_Libraries#File_Dialog_Boxes "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MKDIR&oldid=6470>"




## Navigation menu








### Search





















