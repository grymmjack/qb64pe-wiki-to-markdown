


FILES - QB64 Phoenix Edition Wiki








# FILES



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The FILES statement is used to print a list of files in the current directory using a file specification.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


FILES [*fileSpec$*]
  




## Description


* *fileSpec$* is a string expression or variable containing a path when required.
* *fileSpec$* can use the \* and ? wildcard specifications:
	+ **\*** denotes one or more wildcard characters in a filename or path specification as any legal file name character(s).
	+ **?** denotes one wildcard letter in a filename or path specification as any legal filename character.
* If *fileSpec$* is omitted, it is assumed to be **"\*.\*"** (all files and folders in the current directory).
* Illegal filename characters in **QB64** include \* > < : " | \ / with any amount of dot extensions being allowed in Windows.
* FILES lists can make the screen roll up. Try using SHELL "DIR" with the /P option. [DIR command](http://www.computerhope.com/dirhlp.htm).
* To get individual directory entries use [\_FILES$](/qb64wiki/index.php/FILES$ "FILES$") instead.


  




## Examples


*Example 1:* Finding a list of all BAS files in the current folder.


| ``` FILES "*.BAS"  ``` |
| --- |


  




## See also


* [\_FILES$](/qb64wiki/index.php/FILES$ "FILES$")
* [SHELL](/qb64wiki/index.php/SHELL "SHELL")
* [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR"), [MKDIR](/qb64wiki/index.php/MKDIR "MKDIR")
* [RMDIR](/qb64wiki/index.php/RMDIR "RMDIR"), [KILL](/qb64wiki/index.php/KILL "KILL")
* [\_CWD$](/qb64wiki/index.php/CWD$ "CWD$"), [\_STARTDIR$](/qb64wiki/index.php/STARTDIR$ "STARTDIR$")
* [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS"), [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")
* [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FILES&oldid=8625>"




## Navigation menu








### Search





















