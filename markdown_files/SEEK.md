


SEEK - QB64 Phoenix Edition Wiki








# SEEK



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **SEEK** statement sets the byte or record position in a file for the next read or write.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) 	+ [2.1 Notes](#Notes) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


SEEK *filenumber&*, *position*
  




## Parameters


* *filenumber&* must be the file number that is [OPEN](/qb64wiki/index.php/OPEN "OPEN") and being read or written to.
* *position* is a byte in [BINARY](/qb64wiki/index.php/BINARY "BINARY") or sequencial files created in [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT"), [APPEND](/qb64wiki/index.php/APPEND "APPEND") or [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") modes. The first byte = 1.
* *position* is the record in [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") files to read or write. Records can hold more than one variable defined in a [TYPE](/qb64wiki/index.php/TYPE "TYPE").
* Since the first **SEEK** file position is 1 it may require adding one to an offset value when documentation uses that position as 0.
* After a **SEEK** statement, the next file operation starts at that **SEEK** byte position.
* The **SEEK** statement can work with the [SEEK (function)](/qb64wiki/index.php/SEEK_(function) "SEEK (function)") to move around in a file.


### Notes


* Don't confuse the [LOC](/qb64wiki/index.php/LOC "LOC") position with the [SEEK](/qb64wiki/index.php/SEEK_(function) "SEEK (function)") position !!
	+ **LOC** is the last read or written byte or record prosition.
	+ **SEEK** is the byte or record prosition to read or write next.


  




## Examples


Example 1
A **SEEK** statement using the [SEEK (function)](/qb64wiki/index.php/SEEK_(function) "SEEK (function)") to move to the next random record in a file.


| ``` SEEK 1, [SEEK](/qb64wiki/index.php/SEEK_(function) "SEEK (function)")(1) + 1  ``` |
| --- |




---


Example 2
Demonstrate the difference between **LOC** and **SEEK** positions in a file.


| ``` OPEN "readme.md" FOR BINARY AS #1  PRINT LOC(1) 'LOC returns 0, as we didn't read something yet PRINT SEEK(1) 'SEEK otherwise returns 1, as it's the first byte to read  GET #1, , a& 'now let's read a LONG (4 bytes)  PRINT LOC(1) 'now LOC returns 4, the last read byte PRINT SEEK(1) 'and SEEK returns 5 now, the next byte to read  CLOSE #1 END  ``` |
| --- |




| ``` 0 1 4 5  ``` |
| --- |


  




## See also


* [SEEK (function)](/qb64wiki/index.php/SEEK_(function) "SEEK (function)"), [LOC](/qb64wiki/index.php/LOC "LOC")
* [GET](/qb64wiki/index.php/GET "GET"), [PUT](/qb64wiki/index.php/PUT "PUT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SEEK&oldid=8105>"




## Navigation menu








### Search





















