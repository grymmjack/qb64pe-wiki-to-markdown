


FREEFILE - QB64 Phoenix Edition Wiki








# FREEFILE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The FREEFILE function returns a [LONG](/qb64wiki/index.php/LONG "LONG") value that is an unused file access number.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


fileHandle& = FREEFILE
  




## Description


* FREEFILE values should be given to unique variables so that each file has a specific variable value assigned to it.
* Once the number is assigned in an [OPEN](/qb64wiki/index.php/OPEN "OPEN") statement, the file number can later be used to read, write or [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") that file.
* File numbers [CLOSEd](/qb64wiki/index.php/CLOSE "CLOSE") are made available to FREEFILE for reuse immediately.
* FREEFILE returns are normally sequential starting with 1. Only file numbers in use will not be returned.
* [OPEN](/qb64wiki/index.php/OPEN "OPEN") each file number after each FREEFILE return or the values returned may be the same.


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1295)
* [GET](/qb64wiki/index.php/GET "GET"), [PUT](/qb64wiki/index.php/PUT "PUT"), [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FREEFILE&oldid=8928>"




## Navigation menu








### Search





















