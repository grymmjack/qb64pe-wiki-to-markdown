


FIELD - QB64 Phoenix Edition Wiki








# FIELD



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The FIELD statement creates a [STRING](/qb64wiki/index.php/STRING "STRING") type definition for a [random](/qb64wiki/index.php/RANDOM "RANDOM")-access file buffer.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


FIELD [#]*fileNumber&*, *fieldWidth1%* AS *variable1$*[, *fieldWidthN%* AS *variableN$*]
  




## Description


* *fileNumber%* is a file number used in the [OPEN](/qb64wiki/index.php/OPEN "OPEN") statement or a value from the [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") function.
* Combined size of the *fieldWidth%* parameters **must not exceed the [LEN](/qb64wiki/index.php/LEN "LEN") = recordsize in the [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [OPEN](/qb64wiki/index.php/OPEN "OPEN") statement** or a ["FIELD overflow" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.
* Variables are limited to [STRING](/qb64wiki/index.php/STRING "STRING") types. Use [TYPE](/qb64wiki/index.php/TYPE "TYPE") instead of FIELD if you want to use numerical values.
* Once a FIELD is defined in a statement, [GET](/qb64wiki/index.php/GET "GET") can read and [PUT](/qb64wiki/index.php/PUT "PUT") can write data without placeholders or variables.
* [LSET](/qb64wiki/index.php/LSET "LSET"), [RSET](/qb64wiki/index.php/RSET "RSET"), [PRINT #](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)"), [PRINT # USING](/qb64wiki/index.php/PRINT_USING_(file_statement) "PRINT USING (file statement)"), and [WRITE #](/qb64wiki/index.php/WRITE_(file_statement) "WRITE (file statement)") can be used to place characters in the file buffer before a [PUT](/qb64wiki/index.php/PUT "PUT").
* All field definitions for a file are removed when the file is [closed](/qb64wiki/index.php/CLOSE "CLOSE") or [RESET](/qb64wiki/index.php/RESET "RESET") and all strings are set to null ("").
* **Do not re-assign a field defined variable value or use it in an [INPUT](/qb64wiki/index.php/INPUT "INPUT") statement if you want the variable to remain a field**.


  




## Examples


*Example:* Comparing a [TYPE](/qb64wiki/index.php/TYPE "TYPE") definition with a FIELD [string](/qb64wiki/index.php/STRING "STRING") definition. Demo using a [TYPE](/qb64wiki/index.php/TYPE "TYPE") definition to create a file:





| ``` [TYPE](/qb64wiki/index.php/TYPE "TYPE") ClientType    CName [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 30     '30 bytes    Address [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 30   '30 bytes    City   [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 15    '15 bytes    State  [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 2     ' 2 bytes    Zip    [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 5     ' 5 bytes [END](/qb64wiki/index.php/END "END") [TYPE](/qb64wiki/index.php/TYPE "TYPE")      ' total size = 82 bytes [DIM](/qb64wiki/index.php/DIM "DIM") Client [AS](/qb64wiki/index.php/AS "AS") ClientType RecordLEN = [LEN](/qb64wiki/index.php/LEN "LEN")(Client)       'find the size of each TYPE record  [OPEN](/qb64wiki/index.php/OPEN "OPEN") "ADDRESS.DAT" [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [AS](/qb64wiki/index.php/AS "AS") #1 [LEN](/qb64wiki/index.php/LEN "LEN") = RecordLEN [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") ClientData         'restore to start of DATA record = 0 [DO](/qb64wiki/index.php/DO "DO")    [READ](/qb64wiki/index.php/READ "READ") CName$, Address$, City$, State$, Zip$       'read DATA    [IF](/qb64wiki/index.php/IF "IF") CName$ = "END" [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")    record = record + 1               'increment record number    Client.CName = CName$    Client.Address = Address$    Client.City = City$    Client.State = State$    Client.Zip = Zip$    [PUT](/qb64wiki/index.php/PUT "PUT") #1, record, Client     'PUT by record number [LOOP](/qb64wiki/index.php/LOOP "LOOP") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1 [END](/qb64wiki/index.php/END "END")  ClientData:    [DATA](/qb64wiki/index.php/DATA "DATA") "Bob White","104 Birdland Rd.","Bellview","PA","15236"    [DATA](/qb64wiki/index.php/DATA "DATA") "Ward Cleaver","123 W. Beaver St.","Beaver","PA","15255"    [DATA](/qb64wiki/index.php/DATA "DATA") "Elmer Fudd","45 Wabbit St.","Bethel Park","PA","15022"    [DATA](/qb64wiki/index.php/DATA "DATA") "Wyley Coyote","33 Roadrunner Ave.","Clairton","PA","15122"    [DATA](/qb64wiki/index.php/DATA "DATA") "Jim Morrison","19 Doorway Dr.","Belleview","PA","15236"    [DATA](/qb64wiki/index.php/DATA "DATA") "END",0,0,0,0  ``` |
| --- |


Demo using the FIELD statement to read the file:





| ``` [CONST](/qb64wiki/index.php/CONST "CONST") NM = 30, AD = 30, CT = 15, ST = 2, ZC = 5  ' Define field and record lengths with constants. [CONST](/qb64wiki/index.php/CONST "CONST") RLEN = NM + AD + CY + ST + ZC ' [OPEN](/qb64wiki/index.php/OPEN "OPEN") "ADDRESS.DAT" [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") [AS](/qb64wiki/index.php/AS "AS") #1 [LEN](/qb64wiki/index.php/LEN "LEN") = RLEN FIELD #1, NM [AS](/qb64wiki/index.php/AS "AS") CName$, AD [AS](/qb64wiki/index.php/AS "AS") Address$, CY [AS](/qb64wiki/index.php/AS "AS") City$, ST [AS](/qb64wiki/index.php/AS "AS") State$, ZC [AS](/qb64wiki/index.php/AS "AS") Zip$ FIELD #1, RLEN [AS](/qb64wiki/index.php/AS "AS") Clist$         'define entire record  [GET](/qb64wiki/index.php/GET "GET") #1, 1                  'GET does not need a variable to read FIELD records!                                   'Read file for zip codes from 15230 to 15239 . [DO](/qb64wiki/index.php/DO "DO") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [NOT](/qb64wiki/index.php/NOT "NOT") [EOF](/qb64wiki/index.php/EOF "EOF")(1)    ZipCheck$ = Zip$                            'read zip codes    [IF](/qb64wiki/index.php/IF "IF") (ZipCheck$ >= "15230" [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") ZipCheck$ <= "15239") [THEN](/qb64wiki/index.php/THEN "THEN")       Info$ = Clist$       [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(Info$, 30)     'read name string       [PRINT](/qb64wiki/index.php/PRINT "PRINT") [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(Info$, 31, 30)  'read address string       [PRINT](/qb64wiki/index.php/PRINT "PRINT") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(Info$, 17)    'read city, state and zip code       [PRINT](/qb64wiki/index.php/PRINT "PRINT")    [END IF](/qb64wiki/index.php/END_IF "END IF")    [GET](/qb64wiki/index.php/GET "GET") #1                               'simply GET reads each FIELD record after first [LOOP](/qb64wiki/index.php/LOOP "LOOP") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1 [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [OPEN](/qb64wiki/index.php/OPEN "OPEN"), [TYPE](/qb64wiki/index.php/TYPE "TYPE")
* [GET](/qb64wiki/index.php/GET "GET"), [PUT](/qb64wiki/index.php/PUT "PUT")
* [LSET](/qb64wiki/index.php/LSET "LSET"), [RSET](/qb64wiki/index.php/RSET "RSET")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FIELD&oldid=8126>"




## Navigation menu








### Search





















