


LOF - QB64 Phoenix Edition Wiki








# LOF



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **LOF** function is used to find the length of an [OPEN](/qb64wiki/index.php/OPEN "OPEN") file in bytes, or content length of an HTTP response.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*totalBytes&* = LOF([#]*fileNumber*)
*totalBytes&* = LOF([#]*httpHandle*)
  




## Description


* For regular [OPENed](/qb64wiki/index.php/OPEN "OPEN") files:
	+ LOF returns the number of bytes in an [OPENed](/qb64wiki/index.php/OPEN "OPEN") designated *fileNumber*. File is empty if it returns 0.
	+ *fileNumber* is the number of the opened file. **#** is not required.
	+ Often used to determine the number of records in a [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") access file.
	+ Can also be used to avoid reading an empty file, which would create an error.
	+ LOF in **QB64** can return up to 9 GB (9,223,372,036 bytes) file sizes.


* For HTTP handles opened using [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT"):
	+ LOF returns the length listed in the Content-Length header of the HTTP response.
	+ If no Content-Length header was provided on the HTTP response, then LOF return -1


  




## Examples


Example
Finding the number of records in a RANDOM file using a [TYPE](/qb64wiki/index.php/TYPE "TYPE") variable.


| ```   [OPEN](/qb64wiki/index.php/OPEN "OPEN") file$ [FOR](/qb64wiki/index.php/FOR "FOR") [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [AS](/qb64wiki/index.php/AS "AS") #1 [LEN](/qb64wiki/index.php/LEN "LEN") = [LEN](/qb64wiki/index.php/LEN "LEN")(Type_variable)   NumRecords% = LOF(1) \ RecordLEN%  ``` |
| --- |




---


Example
Reading the Content length of an HTTP response


| ``` [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE"):HTTP h& = [_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")("HTTP:https://qb64phoenix.com") [PRINT](/qb64wiki/index.php/PRINT "PRINT") LOF(h&)  ``` |
| --- |


  




## See also


* [LEN](/qb64wiki/index.php/LEN "LEN"), [EOF](/qb64wiki/index.php/EOF "EOF"), [BINARY](/qb64wiki/index.php/BINARY "BINARY"), [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM"), [TYPE](/qb64wiki/index.php/TYPE "TYPE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LOF&oldid=7593>"




## Navigation menu








### Search





















