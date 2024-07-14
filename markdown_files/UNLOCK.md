


UNLOCK - QB64 Phoenix Edition Wiki








# UNLOCK



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
This statement opens access to parts or all of a file to other programs and network users.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


UNLOCK [#]*fileNumber%*
UNLOCK [#]*fileNumber%*, *record&*
UNLOCK [#]*fileNumber%*, [*firstRecord&*] TO *lastRecord&*
  




## Description


* *fileNumber%* is the file number of the file to unlock.
* In the first syntax, the entire file is unlocked.
* In the second syntax, *record&* is the record number of the file to unlock.
* In the third syntax, the records or bytes in the range [*firstRecord&*,*lastRecord&*] are unlocked. If *firstRecord&* is omitted, it is assumed to be the first record or byte.
* For files opened in [BINARY](/qb64wiki/index.php/BINARY "BINARY") mode, each record corresponds to a single byte.
* [LOCK](/qb64wiki/index.php/LOCK "LOCK") and UNLOCK statements are always used in pairs and each statement must match the other one.
* Files must be unlocked before other programs can access them, and before the file is closed.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## See also


* [LOCK](/qb64wiki/index.php/LOCK "LOCK")
* [OPEN](/qb64wiki/index.php/OPEN "OPEN")
* [ACCESS](/qb64wiki/index.php/ACCESS "ACCESS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=UNLOCK&oldid=6563>"




## Navigation menu








### Search





















