


LEN - QB64 Phoenix Edition Wiki








# LEN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **LEN** function returns the number of bytes used by a variable value or the number of characters in a [STRING](/qb64wiki/index.php/STRING "STRING"). In QB64 it can also return the size of an array or [TYPE](/qb64wiki/index.php/TYPE "TYPE") variable.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


*length%* = LEN(*literalTextOrVariable*)
  




* Literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") values return the number of string bytes which is the same as the number of string characters.
* A numerical *variable* will return the number of bytes used by a numerical variable type.
	+ [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") variable types return 1 byte.
	+ [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") variable types return 2 bytes.
	+ [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") and [LONG](/qb64wiki/index.php/LONG "LONG") integer variable types return 4 bytes.
	+ [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") and [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") variable types return 8 bytes.
	+ [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") variable types return 32 bytes.
	+ [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") and [\_MEM](/qb64wiki/index.php/MEM "MEM") variable types return varying byte sizes.
	+ *Note:* [\_BIT](/qb64wiki/index.php/BIT "BIT") variable types and bit multiples **cannot be measured in bytes**.
* **LEN cannot return lengths of literal numerical values and will create a "variable required" status error in the IDE.**
* **LEN =** can be used with a user defined [TYPE](/qb64wiki/index.php/TYPE "TYPE") variable to determine the number of bytes used in [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") file records:


[OPEN](/qb64wiki/index.php/OPEN "OPEN") file$ FOR [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") AS #n LEN = LEN(recordTypeVariable)
* If a LEN = statement is not used, [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") default record length is 128 or sequencial is 512 up to a maximum of 32767 bytes.
* [BINARY](/qb64wiki/index.php/BINARY "BINARY") OPEN statements will ignore LEN = statements. The byte size of a [read](/qb64wiki/index.php/GET "GET") or [write](/qb64wiki/index.php/PUT "PUT") is determined by the [variable type](/qb64wiki/index.php/Variable_Types "Variable Types").

* In QB64 the **LEN** function can also return the size of entire arrays (except variable length string arrays), see example 5 below.


## Examples


*Example 1:* With a string variable the byte size is the same as the number of characters.





| ``` LastName$ = "Williams" PRINT LEN(LastName$); "bytes"  ``` |
| --- |




| ```  8 bytes  ``` |
| --- |


  

*Example 2:* Testing [INPUT](/qb64wiki/index.php/INPUT "INPUT") for numerical [STRING](/qb64wiki/index.php/STRING "STRING") entries from a user.





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "number: ", num$  value$ = [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")([VAL](/qb64wiki/index.php/VAL "VAL")(num$))) L = LEN(value$)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") LEN(num$), L  ``` |
| --- |


*Note:* [&H](/qb64wiki/index.php/%26H "&H"), [&O](/qb64wiki/index.php/%26O "&O"), D and E will also be accepted as numerical type data in a [VAL](/qb64wiki/index.php/VAL "VAL") conversion, but will add to the entry length.
  

*Example 3:* With numerical value types you MUST use a variable to find the inherent byte length when using LEN.





| ``` DIM I AS INTEGER PRINT "INTEGER ="; LEN(I); "bytes" DIM L AS LONG PRINT "LONG ="; LEN(L); "bytes" DIM I64 AS _INTEGER64 PRINT "_INTEGER64 ="; LEN(I64); "bytes" DIM S AS SINGLE PRINT "SINGLE ="; LEN(S); "bytes" DIM D AS DOUBLE PRINT "DOUBLE ="; LEN(D); "bytes" DIM F AS _FLOAT PRINT "_FLOAT ="; LEN(F); "bytes"  ``` |
| --- |




| ``` INTEGER = 2 bytes LONG = 4 bytes _INTEGER64 = 8 bytes SINGLE = 4 bytes DOUBLE = 8 bytes _FLOAT = 32 bytes  ``` |
| --- |


  

*Example 4:* Opening a RANDOM file using LEN to calculate and LEN = to designate the file record size.





| ``` [TYPE](/qb64wiki/index.php/TYPE "TYPE") variabletype   x [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")'       '2 bytes   y [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 10'  '10 bytes   z [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")'          '4 bytes [END](/qb64wiki/index.php/END "END") [TYPE](/qb64wiki/index.php/TYPE "TYPE")'            '16 bytes total [DIM](/qb64wiki/index.php/DIM "DIM") record [AS](/qb64wiki/index.php/AS "AS") variabletype [DIM](/qb64wiki/index.php/DIM "DIM") newrec [AS](/qb64wiki/index.php/AS "AS") variabletype  file$ = "testrand.inf" '<<<< filename may overwrite existing file number% = 1 '<<<<<<<<<< record number to write cannot be zero RecordLEN% = LEN(record) [PRINT](/qb64wiki/index.php/PRINT "PRINT") RecordLEN%; "bytes" record.x = 255 record.y = "Hello world!" record.z = 65535 [PRINT](/qb64wiki/index.php/PRINT "PRINT") record.x, record.y, record.z  [OPEN](/qb64wiki/index.php/OPEN "OPEN") file$ [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [AS](/qb64wiki/index.php/AS "AS") #1 LEN = RecordLEN% [PUT](/qb64wiki/index.php/PUT "PUT") #1, number% , record 'change record position number to add records [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  [OPEN](/qb64wiki/index.php/OPEN "OPEN") file$ [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [AS](/qb64wiki/index.php/AS "AS") #2 LEN = RecordLEN% NumRecords% = [LOF](/qb64wiki/index.php/LOF "LOF")(2) \ RecordLEN% PRINT NumRecords%; "records"  [GET](/qb64wiki/index.php/GET "GET") #2, NumRecords% , newrec 'GET last record available [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #2 [PRINT](/qb64wiki/index.php/PRINT "PRINT") newrec.x, newrec.y, newrec.z  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ```  16 bytes  255        Hello worl       65535  1 records  255        Hello worl       65535  ``` |
| --- |


*Explanation:* The byte size of the record [TYPE](/qb64wiki/index.php/TYPE "TYPE") determines the [LOF](/qb64wiki/index.php/LOF "LOF") byte size of the file and can determine the number of records.
To read the last record [GET](/qb64wiki/index.php/GET "GET") the number of records. To add a record, use the number of records + 1 to [PUT](/qb64wiki/index.php/PUT "PUT") new record data.
  

*Example 5:* Find the size of arrays and array elements.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") a!(1 [TO](/qb64wiki/index.php/TO "TO") 5) 'a SINGLE has 4 bytes [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Element size ="; LEN(a!(1)), "Overall size ="; LEN(a!()) '5 elements * 4 bytes = 20 bytes  [DIM](/qb64wiki/index.php/DIM "DIM") b%(1 [TO](/qb64wiki/index.php/TO "TO") 5) 'an INTEGER has 4 bytes [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Element size ="; LEN(b%(1)), "Overall size ="; LEN(b%()) '5 elements * 2 bytes = 10 bytes  [DIM](/qb64wiki/index.php/DIM "DIM") c$(1 [TO](/qb64wiki/index.php/TO "TO") 5) 'PRINT LEN(c$()) 'Error: cannot use for array of variable length strings  'but for fixed length strings it works [DIM](/qb64wiki/index.php/DIM "DIM") d$3(1 [TO](/qb64wiki/index.php/TO "TO") 5) 'fixed length (3 chars) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Element size ="; LEN(d$3(1)), "Overall size ="; LEN(d$3()) '5 elements * 3 bytes = 15 bytes  'and it also works for TYPE arrays [TYPE](/qb64wiki/index.php/TYPE "TYPE") t     a [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") '4 bytes     b [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") '2 bytes [END TYPE](/qb64wiki/index.php/END_TYPE "END TYPE") [DIM](/qb64wiki/index.php/DIM "DIM") e(1 [TO](/qb64wiki/index.php/TO "TO") 5) [AS](/qb64wiki/index.php/AS "AS") t 'type is 6 bytes long [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Element size ="; LEN(e(1)), "Overall size ="; LEN(e()) '5 elements * 6 bytes = 30 bytes  ``` |
| --- |


  




## See also


* [LOF](/qb64wiki/index.php/LOF "LOF"), [EOF](/qb64wiki/index.php/EOF "EOF")
* [AS](/qb64wiki/index.php/AS "AS"), [TYPE](/qb64wiki/index.php/TYPE "TYPE")
* [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM"), [BINARY](/qb64wiki/index.php/BINARY "BINARY")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LEN&oldid=8870>"




## Navigation menu








### Search





















