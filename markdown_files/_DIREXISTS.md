


\_DIREXISTS - QB64 Phoenix Edition Wiki








# \_DIREXISTS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_DIREXISTS function determines if a designated file path or folder exists and returns true (-1) or false (0).


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*dirExists%* = \_DIREXISTS(*filepath$*)
  




## Description


* The *filepath$* parameter can be a literal or variable [string](/qb64wiki/index.php/STRING "STRING") path value.
* The function returns -1 when a path or folder exists and 0 when it does not.
* The function reads the system information directly without using a [SHELL](/qb64wiki/index.php/SHELL "SHELL") procedure.
* The function will use the appropriate Operating System path separators. [\_OS$](/qb64wiki/index.php/OS$ "OS$") can determine the operating system.
* **This function does not guarantee that a path can be accessed, only that it exists.**
* **NOTE: Checking if a folder exists in a CD drive may cause the tray to open automatically to request a disk when empty.** To find drives in Windows, use this API Library: [Disk Drives](/qb64wiki/index.php/Windows_Libraries#Disk_Drives "Windows Libraries")


  




## Examples


*Example:* Checks if a folder exists before proceeding.





| ``` [IF](/qb64wiki/index.php/IF "IF") _DIREXISTS("internal\temp") [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Folder found." [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


  




## See also


* [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS")
* [SHELL](/qb64wiki/index.php/SHELL "SHELL")
* [\_OS$](/qb64wiki/index.php/OS$ "OS$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DIREXISTS&oldid=8620>"




## Navigation menu








### Search





















