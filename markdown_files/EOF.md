


EOF - QB64 Phoenix Edition Wiki








# EOF



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **EOF** function indicates that the end of a file or HTTP response has been reached.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 Notes](#Notes) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*endReached%%* = EOF([#]*fileNumber&*)
*endReached%%* = EOF([#]*httpHandle&*)
  




## Description


* *fileNumber&* or *httpHandle&* is the number of the file or HTTP connected being read. **#** is not required.
	+ *fileNumber&* is a file opened using [OPEN](/qb64wiki/index.php/OPEN "OPEN").
	+ *httpHandle&* is a HTTP connection opened using [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT").
* Returns 0 until the end of a file. This avoids a file read error.
* Returns -1 (true) at the end of the file.


### Notes


* In files opened with the [INPUT (file mode)](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") the **EOF** function returns **true** after any used input function reads a [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(26) (Ctrl-Z) from the file, which denotes the "logical" end of a file. This is not necessarily equal to the "physical" end.
	+ Although this subtle behavior is not required nowadays, it is still here for the sake of compatibility. If you're interested in the historic cause of it see [this Article](https://devblogs.microsoft.com/oldnewthing/20040316-00/?p=40233).
	+ To be able to read those files completely use the [BINARY (file mode)](/qb64wiki/index.php/BINARY "BINARY") instead, which is also much faster when used in conjunction with the regular [INPUT](/qb64wiki/index.php/INPUT_(file_statement) "INPUT (file statement)"), [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") and [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$") functions.
* [GET](/qb64wiki/index.php/GET "GET") can return invalid data at the end of a file. Read **EOF** after a [GET](/qb64wiki/index.php/GET "GET") operation to see if the end of the file has been reached and discard the last read if required.
	+ This is not a problem when using [GET](/qb64wiki/index.php/GET "GET") with HTTP connections with a variable length string, the string will always only contain valid data or be empty.


  




## Examples


Example 1
Showing the difference between INPUT and BINARY file modes when Ctrl-Z is involved.


| ``` 'Write a simple test file with Ctrl-Z in the middle. [OPEN](/qb64wiki/index.php/OPEN "OPEN") "test.txt" [FOR](/qb64wiki/index.php/FOR "FOR") [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT") [AS](/qb64wiki/index.php/AS "AS") #1 [PRINT](/qb64wiki/index.php/PRINT "PRINT") #1, "Hello"; [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(26); "World!" [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  'Now read it back, but uhh, this gives us the "Hello" 'only because of the Ctrl-Z. [OPEN](/qb64wiki/index.php/OPEN "OPEN") "test.txt" [FOR](/qb64wiki/index.php/FOR "FOR") [INPUT](/qb64wiki/index.php/INPUT "INPUT") [AS](/qb64wiki/index.php/AS "AS") #1 [WHILE](/qb64wiki/index.php/WHILE "WHILE") [NOT](/qb64wiki/index.php/NOT "NOT") EOF(1)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1, 1); [WEND](/qb64wiki/index.php/WEND "WEND") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT")  'However, it works in the BINARY file mode. [OPEN](/qb64wiki/index.php/OPEN "OPEN") "test.txt" [FOR](/qb64wiki/index.php/FOR "FOR") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") #1 [WHILE](/qb64wiki/index.php/WHILE "WHILE") [NOT](/qb64wiki/index.php/NOT "NOT") EOF(1)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1, 1); [WEND](/qb64wiki/index.php/WEND "WEND") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  ``` |
| --- |




| ``` Hello  Hello→World!  ``` |
| --- |


  




## See also


* [OPEN](/qb64wiki/index.php/OPEN "OPEN")
* [LOF](/qb64wiki/index.php/LOF "LOF"), [LEN](/qb64wiki/index.php/LEN "LEN")
* [INPUT (file statement)](/qb64wiki/index.php/INPUT_(file_statement) "INPUT (file statement)")
* [LINE INPUT (file statement)](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)")
* [GET](/qb64wiki/index.php/GET "GET"), [PUT](/qb64wiki/index.php/PUT "PUT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=EOF&oldid=7205>"




## Navigation menu








### Search





















