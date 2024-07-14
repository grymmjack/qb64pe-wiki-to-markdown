


CLOSE - QB64 Phoenix Edition Wiki








# CLOSE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**CLOSE** closes an open file or port using the number(s) assigned in an [OPEN](/qb64wiki/index.php/OPEN "OPEN") statement.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


CLOSE [*fileNumber*[, ...
  




## Parameters


* *fileNumber* indicates the file or list of file numbers to close. When not specified, all open files are closed.


  




## Description


* A file must be closed when changing to another file mode.
* CLOSE files when they are no longer needed, in order to save memory.
* Files cannot be opened in the same [OPEN](/qb64wiki/index.php/OPEN "OPEN") mode using another number until the first one is closed.
* Use holding variables for each file number returned by [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") so that the file reference is known.
* Will not return an error if a filenumber is already closed or was never opened. It does not verify that a file was closed.
* [CLEAR](/qb64wiki/index.php/CLEAR "CLEAR") can be used to close all open files.
* CLOSE can also be used to close an open TCP/IP or HTTP connection using a handle returned by **QB64**.


  




## See also


* [OPEN](/qb64wiki/index.php/OPEN "OPEN"), [OPEN COM](/qb64wiki/index.php/OPEN_COM "OPEN COM")
* [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT"), [\_OPENHOST](/qb64wiki/index.php/OPENHOST "OPENHOST")
* [\_OPENCONNECTION](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION")
* [\_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CLOSE&oldid=6572>"




## Navigation menu








### Search





















