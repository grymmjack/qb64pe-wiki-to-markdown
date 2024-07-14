


\_FULLPATH$ - QB64 Phoenix Edition Wiki








# \_FULLPATH$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_FULLPATH$** function returns an absolute or full path name for the specified relative path name.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*p$* = \_FULLPATH$(*pathName$*)
  




## Parameters


* *pathname$* is the file or directory for which to obtain absolute path information.


  




## Description


* The path returned ends with a backslash on Windows and a forward-slash on Linux and macOS if *pathname$* is a directory.
* A nonexistent file or directory generates the error message, "Path Not Found.".


  




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


Example
Display the absolute path name of the parent directory.


| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Parent directory full path: "; _FULLPATH$("../")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2734)
* [\_CWD$](/qb64wiki/index.php/CWD$ "CWD$"), [\_STARTDIR$](/qb64wiki/index.php/STARTDIR$ "STARTDIR$")
* [FILES](/qb64wiki/index.php/FILES "FILES"), [\_FILES$](/qb64wiki/index.php/FILES$ "FILES$")
* [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS"), [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FULLPATH$&oldid=8949>"




## Navigation menu








### Search





















