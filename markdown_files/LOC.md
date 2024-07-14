


LOC - QB64 Phoenix Edition Wiki








# LOC



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **LOC** function returns the status of a serial (COM) port received buffer or the last read/written byte or record position in an open file.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) 	+ [2.1 Notes](#Notes) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*bytes%* = LOC(*fileOrPortNumber%*)
  




## Parameters


* *fileOrPortNumber%* is the number used in the port or file [OPEN](/qb64wiki/index.php/OPEN "OPEN") AS statement.
* Returns 0 if the buffer is empty. Any value above 0 indicates the COM port has received data.
* Use it in conjunction with [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$") to get the data bytes received.
* Can also be used to get the last read/written byte or record position in a file. See also [SEEK](/qb64wiki/index.php/SEEK_(function) "SEEK (function)").


### Notes


* Don't confuse the LOC position with the [SEEK](/qb64wiki/index.php/SEEK_(function) "SEEK (function)") position !!
	+ **LOC** is the last read or written byte or record prosition.
	+ **SEEK** is the byte or record prosition to read or write next.


  




## Examples


Example 1
Reading and writing from a COM port opened in Basic.


| ``` [OPEN](/qb64wiki/index.php/OPEN "OPEN") "[COM](/qb64wiki/index.php/OPEN_COM "OPEN COM")1: 9600,N,8,1,OP0" [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [AS](/qb64wiki/index.php/AS "AS") #1 [LEN](/qb64wiki/index.php/LEN "LEN") = 2048 ' random mode = input and output   [DO](/qb64wiki/index.php/DO "DO"): t$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") ' get any transmit keypresses from user     [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")(t$) [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #1, t$ ' send keyboard byte to transmit buffer     bytes% = LOC(1) ' bytes in buffer     [IF](/qb64wiki/index.php/IF "IF") bytes% [THEN](/qb64wiki/index.php/THEN "THEN") ' check receive buffer for data"       r$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(bytes%, 1)          ' get bytes in the receive buffer       [PRINT](/qb64wiki/index.php/PRINT "PRINT") r$; ' print byte strings consecutively to screen"     [END IF](/qb64wiki/index.php/END_IF "END IF")   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") t$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) 'escape key exit [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #  ``` |
| --- |




---


Example 2
Demonstrate the difference between **LOC** and **SEEK** positions in a file.


| ``` OPEN "readme.md" FOR BINARY AS #1  PRINT LOC(1) 'LOC returns 0, as we didn't read something yet PRINT SEEK(1) 'SEEK otherwise returns 1, as it's the first byte to read  GET #1, , a& 'now let's read a LONG (4 bytes)  PRINT LOC(1) 'now LOC returns 4, the last read byte PRINT SEEK(1) 'and SEEK returns 5 now, the next byte to read  CLOSE #1 END  ``` |
| --- |




| ``` 0 1 4 5  ``` |
| --- |


  




## See also


* [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [OPEN COM](/qb64wiki/index.php/OPEN_COM "OPEN COM"), [PRINT (file statement)](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)")
* [SEEK](/qb64wiki/index.php/SEEK "SEEK"), [SEEK (function)](/qb64wiki/index.php/SEEK_(function) "SEEK (function)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LOC&oldid=8106>"




## Navigation menu








### Search





















