


\_READFILE$ - QB64 Phoenix Edition Wiki








# \_READFILE$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_READFILE$** function returns the complete contents of a file in a single string, but without the usual overhead. It does [OPEN](/qb64wiki/index.php/OPEN "OPEN"), [GET](/qb64wiki/index.php/GET "GET") and [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") the file in one run.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*contents$* = \_READFILE$(*fileSpec$*)
  




## Parameters


* *contents$* is the entire file contents returned as [STRING](/qb64wiki/index.php/STRING "STRING"). May return an empty string, if the specified file was empty, or if the program was continued from a file related [ERROR](/qb64wiki/index.php/ERROR_Codes "ERROR Codes").
* *fileSpec$* is the name of the file to read as literal or variable [STRING](/qb64wiki/index.php/STRING "STRING"), if required inclusive a full or relative path.
	+ To avoid errors you should use [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS") before calling this function to make sure the file exists.


  




## Description


* Sometimes it's required or at least useful to have the whole contents of a file in a single string for further processing, e.g. to pass it to hashing or compression functions which expect strings.
* In earlier versions of QB64(PE) you had to implement that loading process manually all the time or create a reusable custom [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") for it.
* Now **\_READFILE$** will simplify this, it's mainly a convenience function to wrap the following code sequence into one handy function:




| ``` fh = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") [OPEN](/qb64wiki/index.php/OPEN "OPEN") fileSpec$ [FOR](/qb64wiki/index.php/FOR "FOR") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") #fh contents$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")([LOF](/qb64wiki/index.php/LOF "LOF")(fh)) [GET](/qb64wiki/index.php/GET "GET") #fh, , contents$ [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #fh  ``` |
| --- |


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.12.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.12.0")

**v3.12.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


Example 1
Showing that this function's result is equal to the code sequence shown above.


| ``` [$COLOR](/qb64wiki/index.php/$COLOR "$COLOR"):0  fileSpec$ = "source\global\settings.bas"  fh = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") [OPEN](/qb64wiki/index.php/OPEN "OPEN") fileSpec$ [FOR](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [BINARY](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [AS](/qb64wiki/index.php/OPEN "OPEN") #fh content$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")([LOF](/qb64wiki/index.php/LOF "LOF")(fh)) [GET](/qb64wiki/index.php/GET "GET") #fh, , content$ [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #fh  [COLOR](/qb64wiki/index.php/COLOR "COLOR") LightGreen [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Using old manual load method..." [COLOR](/qb64wiki/index.php/COLOR "COLOR") White [PRINT](/qb64wiki/index.php/PRINT "PRINT") content$  [COLOR](/qb64wiki/index.php/COLOR "COLOR") LightGreen [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Using new direct load method..." [COLOR](/qb64wiki/index.php/COLOR "COLOR") White [PRINT](/qb64wiki/index.php/PRINT "PRINT") _READFILE$(fileSpec$)  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Example by RhoSigma


---


Example 2
Passing a whole file's contents to hashing functions.


| ``` [$COLOR](/qb64wiki/index.php/$COLOR "$COLOR"):0  fileSpec$ = "source\global\settings.bas"  [COLOR](/qb64wiki/index.php/COLOR "COLOR") LightGreen [PRINT](/qb64wiki/index.php/PRINT "PRINT") "CRC32 of the file..." [COLOR](/qb64wiki/index.php/COLOR "COLOR") White [PRINT](/qb64wiki/index.php/PRINT "PRINT") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")("00000000" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")([_CRC32](/qb64wiki/index.php/CRC32 "CRC32")(_READFILE$(fileSpec$))), 8) [PRINT](/qb64wiki/index.php/PRINT "PRINT")  [COLOR](/qb64wiki/index.php/COLOR "COLOR") LightGreen [PRINT](/qb64wiki/index.php/PRINT "PRINT") "MD5 of the file..." [COLOR](/qb64wiki/index.php/COLOR "COLOR") White [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_MD5$](/qb64wiki/index.php/MD5$ "MD5$")(_READFILE$(fileSpec$))  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Example by RhoSigma
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2699)
* [\_WRITEFILE](/qb64wiki/index.php/WRITEFILE "WRITEFILE"), [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD"), [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE")
* [\_DEFLATE$](/qb64wiki/index.php/DEFLATE$ "DEFLATE$"), [\_INFLATE$](/qb64wiki/index.php/INFLATE$ "INFLATE$")
* [\_ADLER32](/qb64wiki/index.php/ADLER32 "ADLER32"), [\_CRC32](/qb64wiki/index.php/CRC32 "CRC32"), [\_MD5$](/qb64wiki/index.php/MD5$ "MD5$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=READFILE$&oldid=8945>"




## Navigation menu








### Search





















