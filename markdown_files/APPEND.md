


OPEN - QB64 Phoenix Edition Wiki








# OPEN



From QB64 Phoenix Edition Wiki
(Redirected from [APPEND](/qb64wiki/index.php?title=APPEND&redirect=no "APPEND"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The OPEN statement is used to open a file or [COM](/qb64wiki/index.php/OPEN_COM "OPEN COM") serial communications port for program input or output.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Legacy GW-BASIC syntax](#Legacy_GW-BASIC_syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) 	+ [3.1 Errors](#Errors) * [4 Details](#Details) 	+ [4.1 File ACCESS and LOCK Permissions](#File_ACCESS_and_LOCK_Permissions) 	+ [4.2 File Access Modes](#File_Access_Modes) 	+ [4.3 GW-BASIC modes](#GW-BASIC_modes) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


OPEN *fileName$* [**FOR** *mode*] [{[ACCESS](/qb64wiki/index.php/ACCESS "ACCESS")|{[LOCK](/qb64wiki/index.php/LOCK "LOCK")|SHARED}} [{READ|WRITE}] [AS](/qb64wiki/index.php/AS "AS") [#]*fileNumber&* [LEN = *recordLength*]
### Legacy GW-BASIC syntax


OPEN *modeLetter$*, [#]*fileNumber&*, *fileName$*[, *recordLength*]
  




## Parameters


* The *fileName$* is a [STRING](/qb64wiki/index.php/STRING "STRING") variable or literal file name (path optional) in quotes.
* FOR mode can be: [APPEND](/qb64wiki/index.php/APPEND "APPEND") (write to end), [BINARY](/qb64wiki/index.php/BINARY "BINARY") (read/write), [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") (read), [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT") (write new) or [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") (read/write).
* GW-BASIC's *modeLetter$* is a [STRING](/qb64wiki/index.php/STRING "STRING") variable or the letter "A", "B", "I", "O" or "R" designating the OPEN modes above.
* *fileNumber&* can be any **positive** [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [LONG](/qb64wiki/index.php/LONG "LONG") whole number value or an unused value determined by the [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") function.
* [LEN](/qb64wiki/index.php/LEN "LEN") = or *recordLength* is optional to denote the RANDOM file record byte length (default = 128) or sequential (default = 512) load buffer.


  




## Description


* **QB64** can open as many files as your computer memory can handle. QBasic could only open about 15 at a time.
* **QB64 will allocate 4 bytes of memory for every possible file number up to the highest number used in a program.**
* *mode* defaults to RANDOM if the *mode* or FOR access statement is omitted. (see open modes described below)
* **Only the *fileName$*, *fileNumber&* and LEN = *recordLength* values can use variable values in the QBasic syntax.**
* If [LEN](/qb64wiki/index.php/LEN "LEN") = is ommitted, sequential file record sizes default to 512 and [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") to 128 bytes in QBasic.
* *fileName$* can be up to 255 characters with no limit on file name extension length in **QB64**.
* Once a file or port is opened, it can be used in any program procedure using the assigned file number.
* The **"SCRN:"** device is supported in **version 1.000 and up** (see Example 3).
* **Devices such as "KYBD:", "CONS:", "COMn" and "LPTn:" are [not supported in QB64.](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64 "Keywords currently not supported by QB64")**.


**Note:** OPEN "LPTn" is not supported by QB64, but may be supported directly by your operating system.
* [OPEN COM](/qb64wiki/index.php/OPEN_COM "OPEN COM") can also be used for serial port access in **QB64**.


### Errors


* Illegal **QB64** Windows filename characters are  **" \* / \ | ? : < >** . Multiple dots (periods) are allowed.
* Possible OPEN [errors](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") include "Bad file name or number", "Bad File Mode", "File Not Found" or "Path Not Found".
	+ An OPEN file not found error may occur if [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) to (31) are used in a Windows file name.
* **QB64** does not have DOS file name limitations.


  




## Details


### File ACCESS and LOCK Permissions


* [ACCESS](/qb64wiki/index.php/ACCESS "ACCESS") clause limits file access to READ, WRITE or READ WRITE on a network.
* [LOCK](/qb64wiki/index.php/LOCK_(access) "LOCK (access)") clause can specify SHARED or a LOCK READ or LOCK WRITE file lock in an OPEN statement working on a network.
* A separate [LOCK](/qb64wiki/index.php/LOCK "LOCK") statement can lock or [UNLOCK](/qb64wiki/index.php/UNLOCK "UNLOCK") file access on a network using a format that can lock specific records.
* If another process already has access to a specified file, program access is denied for that file OPEN access. A "Permission Denied" error 70 will be returned. A network program must be able to handle a denial of access error.


### File Access Modes


* FOR mode can be:
	+ **OUTPUT**: Sequential mode creates a new file or erases an existing file for new program output. Use [WRITE #](/qb64wiki/index.php/WRITE_(file_statement) "WRITE (file statement)") to write numerical or text data or [PRINT #](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") for text. **OUTPUT clears files of all data** and clears the receive buffer on other devices such as [COM](/qb64wiki/index.php/OPEN_COM "OPEN COM").
	+ **APPEND**: Sequential mode creates a new file if it doesn't exist or appends program output to the end of an existing file. Use [WRITE #](/qb64wiki/index.php/WRITE_(file_statement) "WRITE (file statement)") for numerical or text data or [PRINT #](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") for text as in the OUTPUT mode. **APPEND does not remove previous data.**
	+ **INPUT** : Sequential mode **only reads input** from an existing file. **[File error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") if file does not exist.** Use [INPUT #](/qb64wiki/index.php/INPUT_(file_statement) "INPUT (file statement)") for comma separated numerical or text data and [LINE INPUT #](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") or [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$") to only read text data. **Use [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS") or [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS") to avoid errors.**
	+ **BINARY**: Creates a new file when it doesn't exist or reads and writes to an existing binary file. Use [GET #](/qb64wiki/index.php/GET "GET") to read or [PUT #](/qb64wiki/index.php/PUT "PUT") to write byte positions simultaneously. [LEN](/qb64wiki/index.php/LEN "LEN") = statements are ignored in this mode.
	+ **RANDOM**: Creates a new file when it doesn't exist or reads or writes to an existing random file record. Use [GET #](/qb64wiki/index.php/GET "GET") or [PUT #](/qb64wiki/index.php/PUT "PUT") to read or write to file records. A [LEN](/qb64wiki/index.php/LEN "LEN") = statement can define the byte size of a record (no LEN statement defaults to 128 bytes)
	+ Modes **INPUT**, **BINARY** and **RANDOM** allow a file to be concurrently opened in a different mode and number.


### GW-BASIC modes


* *Mode letter* is a variable or literal [STRING](/qb64wiki/index.php/STRING "STRING") letter value as one of the following:
	+ "A" = **APPEND**.
	+ "B" = **BINARY**.
	+ "I" = **INPUT**.
	+ "O" = **OUTPUT**.
	+ "R" = **RANDOM**.


  




## Examples


*Example 1:* Function that displays errors and the number of errors in QBasic filenames. Returns 0 when filename is OK.





| ```  file$ = "Hello,~1.mp3"      'example call below  [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 30: errors% = CheckName%(file$): [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "  Total Errors ="; errors%  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") CheckName% (Filename$)   '[NOT](/qb64wiki/index.php/NOT "NOT")E: Function also displays filename errors so [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") on screen before call!   [DIM](/qb64wiki/index.php/DIM "DIM") L [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), DP [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), XL [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")   L = [LEN](/qb64wiki/index.php/LEN "LEN")(Filename$): DP = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(Filename$, "."): [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") DP [THEN](/qb64wiki/index.php/THEN "THEN") XL = L - DP 'extension   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") L = 0 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") L > 12 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") DP > 9 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") XL > 3 [THEN](/qb64wiki/index.php/THEN "THEN")     CheckName% = -1: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 12: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Illegal format!"; : [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION")   [END IF](/qb64wiki/index.php/END_IF "END IF")   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i% = 1 [TO](/qb64wiki/index.php/TO "TO") L      'check each filename character"      code% = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")([MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(Filename$, i%, 1)): [COLOR](/qb64wiki/index.php/COLOR "COLOR") 10      ' see ASCII codes      [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") code%       'check for errors and highlight in red         '[CASE](/qb64wiki/index.php/CASE "CASE") 34, 42 [TO](/qb64wiki/index.php/TO "TO") 44, 47, 58 [TO](/qb64wiki/index.php/TO "TO") 63, 91 [TO](/qb64wiki/index.php/TO "TO") 93, 124: E% = E% + 1: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 12 ' **QBasic errors**         [CASE](/qb64wiki/index.php/CASE "CASE") 34, 42, 47, 58, 60, 62, 92, 124: E% = E% + 1: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 12 ' **QB64 errors**         [CASE](/qb64wiki/index.php/CASE "CASE") 46: dot% = dot% + 1: [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") dot% > 1 [THEN](/qb64wiki/index.php/THEN "THEN") E% = E% + 1: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 12      [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")      [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(code%);  'use [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") before [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") call to place print   [NEXT](/qb64wiki/index.php/NEXT "NEXT")   CheckName% = E% [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


*Note: The QBasic character error list is commented out and the function will return invalid filenames under QB64.*





| ```                          Hello,~1.mp3  Total Errors = 1  ``` |
| --- |


*Note:* The screen output displays filename characters in green except for red comma QBasic error.
  

*Example 2:* When **OPEN "SCRN:" FOR OUTPUT AS #f** is used, **PRINT #f** will print the text to the screen instead of to a file:





| ``` f% = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") 'should always be 1 at program start OPEN "SCRN:" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT") [AS](/qb64wiki/index.php/AS "AS") #f% g% = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") 'should always be 2 after 1 OPEN "temp.txt" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT") [AS](/qb64wiki/index.php/AS "AS") #g%  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 2     [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #i, "Hello World, Screen and File version" NEXT  ``` |
| --- |


code by Steve McNeill
*Note:* Linux or macOS file names can use a path destination such as ".\SCRN:" to use SCRN: as an actual file name.
  

*Example 3:* Showcasing different file modes.





| ``` [CLS](/qb64wiki/index.php/CLS "CLS")  OPEN "test.tst" [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT") [AS](/qb64wiki/index.php/AS "AS") #1 [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #1, "If test.tst didn't exist:" [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #1, "A new file was created named test.tst and then deleted." [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #1, "If test.tst did exist:" [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #1, "It was overwritten with this and deleted." [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  OPEN "test.tst" [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") [AS](/qb64wiki/index.php/AS "AS") #1 [DO](/qb64wiki/index.php/DO "DO") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [EOF](/qb64wiki/index.php/EOF "EOF")(1) [INPUT](/qb64wiki/index.php/INPUT_(file_statement) "INPUT (file statement)") #1, a$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") a$ [LOOP](/qb64wiki/index.php/LOOP "LOOP") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1  [KILL](/qb64wiki/index.php/KILL "KILL") "test.tst"  [END](/qb64wiki/index.php/END "END")   ``` |
| --- |




| ``` If test.tst didn't exist: A new file was created named test.tst and then deleted. If test.tst did exist: It was overwritten with this and deleted.  ``` |
| --- |


**Warning:** Make sure you don't have a file named test.tst before you run this or it will be overwritten.
  




## See also


* [PRINT (file statement)](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)"), [INPUT (file statement)](/qb64wiki/index.php/INPUT_(file_statement) "INPUT (file statement)")
* [GET](/qb64wiki/index.php/GET "GET"), [PUT](/qb64wiki/index.php/PUT "PUT"), [WRITE (file statement)](/qb64wiki/index.php/WRITE_(file_statement) "WRITE (file statement)")
* [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$"), [LINE INPUT (file statement)](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)")
* [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE"), [LOF](/qb64wiki/index.php/LOF "LOF"), [EOF](/qb64wiki/index.php/EOF "EOF"), [LOC](/qb64wiki/index.php/LOC "LOC")
* [SEEK](/qb64wiki/index.php/SEEK "SEEK"), [SEEK (function)](/qb64wiki/index.php/SEEK_(function) "SEEK (function)")
* [OPEN COM](/qb64wiki/index.php/OPEN_COM "OPEN COM"), [LEN](/qb64wiki/index.php/LEN "LEN"), [RESET](/qb64wiki/index.php/RESET "RESET")
* [FIELD](/qb64wiki/index.php/FIELD "FIELD"), [TYPE](/qb64wiki/index.php/TYPE "TYPE")
* [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS"), [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")
* [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT"), [\_OPENHOST](/qb64wiki/index.php/OPENHOST "OPENHOST"), [\_OPENCONNECTION](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OPEN&oldid=8156#File_Access_Modes>"




## Navigation menu








### Search





















