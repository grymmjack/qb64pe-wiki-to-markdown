


\_CWD$ - QB64 Phoenix Edition Wiki








# \_CWD$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
  

The \_CWD$ function returns the current working directory path as a string value without a trailing path separator.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 Errors](#Errors) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*workingDirectory$* = \_CWD$
  




## Description


* By default, the initial working directory path is usually the same as the directory of the executable file run.
* The current working directory can be changed with the [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR") or [SHELL](/qb64wiki/index.php/SHELL "SHELL") command; CHDIR sets it, \_CWD$ returns it.
* Path returns will change only when the working path has changed. When in C:\ and run QB64\cwd.exe, it will still return C:\
* The current working directory string can be used in [OPEN](/qb64wiki/index.php/OPEN "OPEN") statements and [SHELL](/qb64wiki/index.php/SHELL "SHELL") commands that deal with files.
* Works in Windows, macOS and Linux. [\_OS$](/qb64wiki/index.php/OS$ "OS$") can be used by a program to predict the proper slash separations in different OS's.


### Errors


* If an error occurs while obtaining the working directory from the operating system, [error code](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") 51 (Internal Error) will be generated.


  




## Examples


*Example:* Get the current working directory, and move around the file system:





| ``` startdir$ = _CWD$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") "We started at "; startdir$ [MKDIR](/qb64wiki/index.php/MKDIR "MKDIR") "a_temporary_dir" [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR") "a_temporary_dir" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "We are now in "; _CWD$ [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR") startdir$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") "And now we're back in "; _CWD$ [RMDIR](/qb64wiki/index.php/RMDIR "RMDIR") "a_temporary_dir"  ``` |
| --- |




| ``` We started at C:\QB64 We are now in C:\QB64\a_temporary_dir And now we're back in C:\QB64  ``` |
| --- |


  




## See also


* [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR") (Change the current working directory)
* [RMDIR](/qb64wiki/index.php/RMDIR "RMDIR") (Remove a directory in the file system)
* [KILL](/qb64wiki/index.php/KILL "KILL") (Delete a file in the file system)
* [MKDIR](/qb64wiki/index.php/MKDIR "MKDIR") (Create a directory in the file system)
* [\_OS$](/qb64wiki/index.php/OS$ "OS$") (returns current OS to program)
* [\_STARTDIR$](/qb64wiki/index.php/STARTDIR$ "STARTDIR$") (returns path the user called program from)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CWD$&oldid=8299>"




## Navigation menu








### Search





















