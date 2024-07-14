


PUT - QB64 Phoenix Edition Wiki








# PUT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **PUT #** file or port statement writes data to a specific byte or record location.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 More Examples](#More_Examples) * [2 See also](#See_also) |
| --- |


## Syntax


**PUT #*filenumber&*,** [*position*][, {*holdingvariable*|*holdingarray()*}]
  




* File/port number is the number used in the [OPEN](/qb64wiki/index.php/OPEN "OPEN") statement.
* The [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [LONG](/qb64wiki/index.php/LONG "LONG") file byte *position* in a [BINARY](/qb64wiki/index.php/BINARY "BINARY") file or the record *position* in a [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") file **must be greater than zero**.
* The file byte or record *position* can be omitted if the PUT or [GET](/qb64wiki/index.php/GET "GET") is consecutive or when creating new file data sequentially.
* The *holding variable* [type](/qb64wiki/index.php/TYPE "TYPE") determines byte size and the next byte position in the file when the *position* is ommitted.
* The first byte or record position is 1. This may require adding one to an offset value when documentation uses that position as 0.
* Both the file *position* and *holding variable*(and comma) can be omitted when using a [FIELD](/qb64wiki/index.php/FIELD "FIELD") definition.
* If a [LEN](/qb64wiki/index.php/LEN "LEN") = record length statement is omitted in an [OPEN](/qb64wiki/index.php/OPEN "OPEN") FOR [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") statement the record size defaults to 128 bytes!
* **Warning: Not designating a PUT position can overwrite previous file data based on the current file *position*!**
* When using a numeric *holding variable*, values do NOT require conversion using [MKI$](/qb64wiki/index.php/MKI$ "MKI$"), [MKL$](/qb64wiki/index.php/MKL$ "MKL$"), [MKS$](/qb64wiki/index.php/MKS$ "MKS$") or [MKD$](/qb64wiki/index.php/MKD$ "MKD$").
* **QB64** can load [array](/qb64wiki/index.php/Arrays "Arrays") data directly(brackets required) to a [BINARY](/qb64wiki/index.php/BINARY "BINARY") file using **one** PUT to a [BINARY](/qb64wiki/index.php/BINARY "BINARY") file: **PUT #1, , array()**


  

*Example 1:* Using a [TYPE](/qb64wiki/index.php/TYPE "TYPE") record variable(Contact) to enter a new [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") record to a file.





| ``` [TYPE](/qb64wiki/index.php/TYPE "TYPE") ContactType   first [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 10   last [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 20   age [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [END](/qb64wiki/index.php/END "END") [TYPE](/qb64wiki/index.php/TYPE "TYPE") [DIM](/qb64wiki/index.php/DIM "DIM") Contact [AS](/qb64wiki/index.php/AS "AS") ContactType  [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a first name: ", Contact.first [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a last name: ", Contact.last [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter an age: ", Contact.age  [OPEN](/qb64wiki/index.php/OPEN "OPEN") "Record.lst" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [AS](/qb64wiki/index.php/AS "AS") #1 [LEN](/qb64wiki/index.php/LEN "LEN") = [LEN](/qb64wiki/index.php/LEN "LEN")(Contact) NumRecords% = [LOF](/qb64wiki/index.php/LOF "LOF")(1) \ [LEN](/qb64wiki/index.php/LEN "LEN")(Contact) [PRINT](/qb64wiki/index.php/PRINT "PRINT") NumRecords%; "previous records"  PUT #1, NumRecords% + 1, Contact ' add a new record [TYPE](/qb64wiki/index.php/TYPE "TYPE") record value [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  ``` |
| --- |


*Note:* The DOT record variable values were created or changed before the PUT. The record length is 32 bytes.
  

*Example 2:* Placing the contents of a numerical array into a [BINARY](/qb64wiki/index.php/BINARY "BINARY") file. You may want to put the array size at the beginning too.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") array(100) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 100   array(i) = i [NEXT](/qb64wiki/index.php/NEXT "NEXT") showme  'display array contents  [OPEN](/qb64wiki/index.php/OPEN "OPEN") "BINFILE.BIN" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") #1  PUT #1, , array()  [ERASE](/qb64wiki/index.php/ERASE "ERASE") array 'clear element values from array and display empty showme [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  [OPEN](/qb64wiki/index.php/OPEN "OPEN") "BINFILE.BIN" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") #2 [GET](/qb64wiki/index.php/GET "GET") #2, , array() [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #2 showme  'display array after transfer from file  [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") showme [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 100   [PRINT](/qb64wiki/index.php/PRINT "PRINT") array(i); [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "done" [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


*Note:* Use empty brackets in QB64 when using [GET](/qb64wiki/index.php/GET "GET") to create an array or PUT to create a [BINARY](/qb64wiki/index.php/BINARY "BINARY") data file.
### More Examples


* [Program ScreenShots](/qb64wiki/index.php/Program_ScreenShots "Program ScreenShots")


  




## See also


* [GET #](/qb64wiki/index.php/GET "GET")
* [SEEK](/qb64wiki/index.php/SEEK "SEEK"), [SEEK (function)](/qb64wiki/index.php/SEEK_(function) "SEEK (function)")
* [PRINT #](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)")
* [FIELD](/qb64wiki/index.php/FIELD "FIELD")
* [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [PUT (TCP/IP statement)](/qb64wiki/index.php/PUT_(TCP/IP_statement) "PUT (TCP/IP statement)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PUT&oldid=8098>"




## Navigation menu








### Search





















