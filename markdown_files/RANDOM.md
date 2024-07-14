


RANDOM - QB64 Phoenix Edition Wiki








# RANDOM



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**RANDOM** is used in an [OPEN](/qb64wiki/index.php/OPEN "OPEN") statement to read([GET](/qb64wiki/index.php/GET "GET")) from or write([PUT](/qb64wiki/index.php/PUT "PUT")) to a file.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


OPEN Filename$ FOR RANDOM AS #1 [LEN = *recordlength%*]
  




* RANDOM is the Default mode if no mode is given in the [OPEN](/qb64wiki/index.php/OPEN "OPEN") statement.
* It creates the file if the legal file name given does NOT exist.
* As a RANDOM file, it can read or write any record using [GET](/qb64wiki/index.php/GET "GET") and/or [PUT](/qb64wiki/index.php/PUT "PUT") statements.
* *Recordlength%* is determined by getting the LEN of a [TYPE](/qb64wiki/index.php/TYPE "TYPE") variable or a [FIELD](/qb64wiki/index.php/FIELD "FIELD") statement.


[STRING](/qb64wiki/index.php/STRING "STRING") = 1 byte/character, [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") = 2 bytes, [LONG](/qb64wiki/index.php/LONG "LONG") = 4 bytes, [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") = 4 bytes [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") = 8 bytes
[\_BYTE](/qb64wiki/index.php/BYTE "BYTE") = 1 byte, [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") = 8 bytes, [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") = 10 bytes (so far)
* If no record length is used in the [OPEN](/qb64wiki/index.php/OPEN "OPEN") statement, the default record size is 128 bytes except for the last record.
* A record length cannot exceed 32767 or an [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur!
* To determine the number of records in a file the records% = [LOF](/qb64wiki/index.php/LOF "LOF") \ recordlength%.
* When **variable length strings** are PUT into RANDOM files the record length must exceed the maximum string entry by:


2 bytes are reserved for recording variable string lengths up to 32767 bytes (LEN = longest + 2)
8 bytes are reserved for recording variable string lengths exceeding 32767 bytes (LEN = longest + 8)
* A serial communication port can also be opened for RANDOM in an [OPEN COM](/qb64wiki/index.php/OPEN_COM "OPEN COM") statement.


  

*Example 1:* Function that finds a RANDOM file's record number for a string value such as a phone number.





| ``` [TYPE](/qb64wiki/index.php/TYPE "TYPE") customer   age [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")   phone [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 10 [END](/qb64wiki/index.php/END "END") [TYPE](/qb64wiki/index.php/TYPE "TYPE")  [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") cust [AS](/qb64wiki/index.php/AS "AS") customer, recLEN recLEN = [LEN](/qb64wiki/index.php/LEN "LEN")(cust)            'get the length of the record type [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Rec[LEN](/qb64wiki/index.php/LEN "LEN"):"; recLEN  [OPEN](/qb64wiki/index.php/OPEN "OPEN") "randfile.rec" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") RANDOM [AS](/qb64wiki/index.php/AS "AS") #1 [LEN](/qb64wiki/index.php/LEN "LEN") = recLEN [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 4   [READ](/qb64wiki/index.php/READ "READ") cust.age, cust.phone   [PUT](/qb64wiki/index.php/PUT "PUT") #1, , cust [NEXT](/qb64wiki/index.php/NEXT "NEXT") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  RP = RecordPos("randfile.rec", "2223456789")  'returns 0 if record not found!  [PRINT](/qb64wiki/index.php/PRINT "PRINT") RP  [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") RP [THEN](/qb64wiki/index.php/THEN "THEN")   [OPEN](/qb64wiki/index.php/OPEN "OPEN") "randfile.rec" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") RANDOM [AS](/qb64wiki/index.php/AS "AS") #2 [LEN](/qb64wiki/index.php/LEN "LEN") = recLEN   [GET](/qb64wiki/index.php/GET "GET") #2, RP, cust   [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #2 [PRINT](/qb64wiki/index.php/PRINT "PRINT") cust.age, cust.phone [END IF](/qb64wiki/index.php/END_IF "END IF")  [END](/qb64wiki/index.php/END "END")  [DATA](/qb64wiki/index.php/DATA "DATA") 59,2223456789,62,4122776477,32,3335551212,49,1234567890  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") RecordPos (file$, search$) f = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") [OPEN](/qb64wiki/index.php/OPEN "OPEN") file$ [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") [AS](/qb64wiki/index.php/AS "AS") #f FL = [LOF](/qb64wiki/index.php/LOF "LOF")(f) dat$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(FL, f) [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") f recpos = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(dat$, search$) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") recpos [THEN](/qb64wiki/index.php/THEN "THEN") RecordPos = recpos \ recLEN + 1 [ELSE](/qb64wiki/index.php/ELSE "ELSE") RecordPos = 0 [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


*Note:* Random files can store records holding various variable types using a [TYPE](/qb64wiki/index.php/TYPE "TYPE") definition or a [FIELD](/qb64wiki/index.php/FIELD "FIELD") statement.
  

*Example 2:* When not using a [TYPE](/qb64wiki/index.php/TYPE "TYPE") or fixed length strings, QB4.5 allows RANDOM files to hold variable length strings up to 2 bytes less than the LEN = record length statement:





| ``` [_CONTROLCHR](/qb64wiki/index.php/CONTROLCHR "CONTROLCHR") OFF [OPEN](/qb64wiki/index.php/OPEN "OPEN") "myfile.txt" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT") [AS](/qb64wiki/index.php/AS "AS") #1: [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1: ' clears former file of all entries. [OPEN](/qb64wiki/index.php/OPEN "OPEN") "myfile.txt" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") RANDOM [AS](/qb64wiki/index.php/AS "AS") #1 [LEN](/qb64wiki/index.php/LEN "LEN") = 13 'strings can be up to 11 bytes with 2 byte padder  a$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(1) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "ABCDEFGHI" b$ = "ABCDEFGHI" c$ = "1234"  [PUT](/qb64wiki/index.php/PUT "PUT") #1, 1, a$ [PUT](/qb64wiki/index.php/PUT "PUT") #1, 2, b$ [PUT](/qb64wiki/index.php/PUT "PUT") #1, 3, c$  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 3   [GET](/qb64wiki/index.php/GET "GET") #1, i, a$   [PRINT](/qb64wiki/index.php/PRINT "PRINT") a$, [LEN](/qb64wiki/index.php/LEN "LEN")(a$) [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE")  ``` |
| --- |




| ``` ☺ ABCDEFGHI       11 ABCDEFGHI         9 1234              4  ``` |
| --- |


*Note:* The 2 byte file padders before each string PUT will show the length of a string for GET as [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters. Padders will always be 2 bytes and strings up to the last one will be 13 bytes each no matter the length up to 11, so the file size can be determined as (2 + 11) + (2 + 9 + 2) + (2 + 4) or 13 + 13 + 2 + 4 = 32 bytes.
  




## See also


* [GET](/qb64wiki/index.php/GET "GET"), [PUT](/qb64wiki/index.php/PUT "PUT"), [FIELD](/qb64wiki/index.php/FIELD "FIELD")
* [BINARY](/qb64wiki/index.php/BINARY "BINARY")
* [SEEK](/qb64wiki/index.php/SEEK "SEEK"), [SEEK (function)](/qb64wiki/index.php/SEEK_(function) "SEEK (function)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RANDOM&oldid=8099>"




## Navigation menu








### Search





















