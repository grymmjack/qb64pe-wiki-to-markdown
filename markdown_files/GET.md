


GET - QB64 Phoenix Edition Wiki








# GET



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The GET # statement reads data from a file or port device by bytes or record positions.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


GET #*fileNumber&*, [*position*][, {*targetVariable*|*targetArray()*}]
  




## Description


* *fileNumber&* is the file or port number used in the [OPEN](/qb64wiki/index.php/OPEN "OPEN") AS [BINARY](/qb64wiki/index.php/BINARY "BINARY") or [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") statement.
* The [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [LONG](/qb64wiki/index.php/LONG "LONG") byte *position* in a [BINARY](/qb64wiki/index.php/BINARY "BINARY") file or the record *position* in a [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") file **must be greater than zero**.
* The *position* can be omitted if the GET operations are consecutive based on the *targetVariable* [TYPE](/qb64wiki/index.php/TYPE "TYPE") byte size.
* The *targetVariable* [type](/qb64wiki/index.php/Data_types "Data types") or [FIELD](/qb64wiki/index.php/FIELD "FIELD") *variable* size determines the byte size and the next *position* in the file.
* The first byte position in a file is 1.
* GET does not require a byte or record *position* or *targetVariable* (or comma) when using a [FIELD](/qb64wiki/index.php/FIELD "FIELD") statement.
* **QB64** can [PUT](/qb64wiki/index.php/PUT "PUT") the entire contents of an array to a file and later GET those contents to a *targetArray()* (include brackets).
* **GET may ignore the end of a file and return bad data. If the [EOF](/qb64wiki/index.php/EOF "EOF") function returns -1 after a GET operation, it indicates that the data has ended.**




| ```  DO UNTIL [EOF](/qb64wiki/index.php/EOF "EOF")(1)    GET #1, , value%    IF [NOT](/qb64wiki/index.php/NOT "NOT")([EOF](/qb64wiki/index.php/EOF "EOF")(1)) THEN [PUT](/qb64wiki/index.php/PUT "PUT") #2, , value%  LOOP  ``` |
| --- |


  




## Examples


*Example 1:* Opening a RANDOM file using LEN to calculate and LEN = to designate the file record size.





| ``` [TYPE](/qb64wiki/index.php/TYPE "TYPE") variabletype   x [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")'       '2 bytes   y [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 10'  '10 bytes   z [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")'          '4 bytes [END](/qb64wiki/index.php/END "END") [TYPE](/qb64wiki/index.php/TYPE "TYPE")'            '16 bytes total [DIM](/qb64wiki/index.php/DIM "DIM") record [AS](/qb64wiki/index.php/AS "AS") variabletype [DIM](/qb64wiki/index.php/DIM "DIM") newrec [AS](/qb64wiki/index.php/AS "AS") variabletype  file$ = "testrand.inf" '<<<< filename may overwrite existing file number% = 1 '<<<<<<<<<< record number to write cannot be zero RecordLEN% = [LEN](/qb64wiki/index.php/LEN "LEN")(record) [PRINT](/qb64wiki/index.php/PRINT "PRINT") RecordLEN%; "bytes" record.x = 255 record.y = "Hello world!" record.z = 65535 [PRINT](/qb64wiki/index.php/PRINT "PRINT") record.x, record.y, record.z  [OPEN](/qb64wiki/index.php/OPEN "OPEN") file$ [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [AS](/qb64wiki/index.php/AS "AS") #1 [LEN](/qb64wiki/index.php/LEN "LEN") = RecordLEN% [PUT](/qb64wiki/index.php/PUT "PUT") #1, number% , record 'change record position number to add records [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  [OPEN](/qb64wiki/index.php/OPEN "OPEN") file$ [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [AS](/qb64wiki/index.php/AS "AS") #2 [LEN](/qb64wiki/index.php/LEN "LEN") = RecordLEN% NumRecords% = [LOF](/qb64wiki/index.php/LOF "LOF")(2) \ RecordLEN% PRINT NumRecords%; "records"  GET #2, NumRecords% , newrec 'GET last record available [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #2 [PRINT](/qb64wiki/index.php/PRINT "PRINT") newrec.x, newrec.y, newrec.z  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ```  16 bytes  255        Hello worl       65535  1 records  255        Hello worl       65535  ``` |
| --- |


*Explanation:* The byte size of the record [TYPE](/qb64wiki/index.php/TYPE "TYPE") determines the [LOF](/qb64wiki/index.php/LOF "LOF") byte size of the file and can determine the number of records.
To read the last record GET the number of records. To add a record, use the number of records + 1 to [PUT](/qb64wiki/index.php/PUT "PUT") new record data.
  

*Example 2:* Placing the contents of a numerical array into a [BINARY](/qb64wiki/index.php/BINARY "BINARY") file. You may want to put the array size at the beginning too.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") array(100) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 100   array(i) = i [NEXT](/qb64wiki/index.php/NEXT "NEXT") showme  'display array contents  [OPEN](/qb64wiki/index.php/OPEN "OPEN") "BINFILE.BIN" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") #1  [PUT](/qb64wiki/index.php/PUT "PUT") #1, , array()  [ERASE](/qb64wiki/index.php/ERASE "ERASE") array 'clear element values from array and display empty showme [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  [OPEN](/qb64wiki/index.php/OPEN "OPEN") "BINFILE.BIN" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") #2 GET #2, , array() [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #2 showme  'display array after transfer from file  [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") showme [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 100   [PRINT](/qb64wiki/index.php/PRINT "PRINT") array(i); [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "done" [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


*Note:* Use empty brackets in QB64 when using GET to create an array or [PUT](/qb64wiki/index.php/PUT "PUT") to create a [BINARY](/qb64wiki/index.php/BINARY "BINARY") data file.
  




## See also


* [PUT #](/qb64wiki/index.php/PUT "PUT"), [SEEK](/qb64wiki/index.php/SEEK "SEEK"), [SEEK (function)](/qb64wiki/index.php/SEEK_(function) "SEEK (function)")
* [INPUT #](/qb64wiki/index.php/INPUT_(file_statement) "INPUT (file statement)"), [GET (TCP/IP statement)](/qb64wiki/index.php/GET_(TCP/IP_statement) "GET (TCP/IP statement)")
* [FIELD](/qb64wiki/index.php/FIELD "FIELD"), [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM"), [BINARY](/qb64wiki/index.php/BINARY "BINARY")
* [LEN](/qb64wiki/index.php/LEN "LEN"), [LOF](/qb64wiki/index.php/LOF "LOF"), [EOF](/qb64wiki/index.php/EOF "EOF")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=GET&oldid=8093>"




## Navigation menu








### Search





















