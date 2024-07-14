


RMDIR - QB64 Phoenix Edition Wiki








# RMDIR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The RMDIR statement deletes an empty directory using a designated path relative to the present path location.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


RMDIR *directory$*
  




## Description


* *directory$* is a relative path to the directory to delete.
* Directory path must be a literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") value designating the folder to be deleted.
* If the directory contains files or folders, a [file/path access error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.
* If the directory path cannot be found, a [path not found](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error occurs.


  




## Examples




| ```   [ON ERROR GOTO](/qb64wiki/index.php/ON_ERROR "ON ERROR") ErrorHandler  DO  ERRcode = 0  [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter path and name of directory to delete: "; directory$  IF [LEN](/qb64wiki/index.php/LEN "LEN")(directory$) THEN      'valid user entry or quits    RMDIR directory$    'removes empty folder without a prompt    IF ERRcode = 0 THEN PRINT "Folder "; directory$; " removed."  END IF  LOOP UNTIL ERRcode = 0 OR LEN(directory$) = 0 [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")   ErrorHandler: ERRcode = [ERR](/qb64wiki/index.php/ERR "ERR")    'get error code returned [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") ERRcode [CASE](/qb64wiki/index.php/CASE "CASE") 75     [PRINT](/qb64wiki/index.php/PRINT "PRINT") directory$ + " is not empty!" [CASE](/qb64wiki/index.php/CASE "CASE") 76     [PRINT](/qb64wiki/index.php/PRINT "PRINT") directory$ + " does not exist!" [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Error"; ERRcode; "attempting to delete " + directory$ [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [RESUME NEXT](/qb64wiki/index.php/RESUME "RESUME")   ``` |
| --- |


This Windows-specific output from two runs of the above program is typical, though your output may vary. User-entered text is in italics.


| ```   Enter path and name of directory to delete: *Some\Folder\That\Doesnt\Exist* Some\folder\That\Doesnt\Exist does not exist!  Enter path and name of directory to delete: *C:\temp* C:\temp is not empty!   ``` |
| --- |


  




## See also


* [MKDIR](/qb64wiki/index.php/MKDIR "MKDIR"), [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR")
* [KILL](/qb64wiki/index.php/KILL "KILL"), [FILES](/qb64wiki/index.php/FILES "FILES")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RMDIR&oldid=6610>"




## Navigation menu








### Search





















