


\_WRITEFILE - QB64 Phoenix Edition Wiki








# \_WRITEFILE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_WRITEFILE** statement writes a string into a new file, overwriting an existing file of the same name. It does [OPEN](/qb64wiki/index.php/OPEN "OPEN"), [PUT](/qb64wiki/index.php/PUT "PUT") and [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") the file in one run. It's the counterpart to the [\_READFILE$](/qb64wiki/index.php/READFILE$ "READFILE$") function.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


\_WRITEFILE *fileSpec$*, *contents$*
  




## Parameters


* *fileSpec$* is the name of the file to write as literal or variable [STRING](/qb64wiki/index.php/STRING "STRING"), if required inclusive a full or relative path.
	+ To avoid errors you should use [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS") before using this statement to make sure a desired path exists.
* *contents$* is the literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") which its contents shall be written into the file.


  




## Description


* Sometimes you may be in need to quickly dump a huge amount of data into a file without much fuss, e.g. the results of the pack/unpack functions [\_DEFLATE$](/qb64wiki/index.php/DEFLATE$ "DEFLATE$") and [\_INFLATE$](/qb64wiki/index.php/INFLATE$ "INFLATE$") or when copying a file in conjunction with the [\_READFILE$](/qb64wiki/index.php/READFILE$ "READFILE$") function.
* In earlier versions of QB64(PE) you had to implement that saving process manually all the time or create a reusable custom [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") for it.
* Now **\_WRITEFILE** will simplify this, it's mainly for convenience to wrap the following code sequence into one handy statement:




| ``` fh = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") [OPEN](/qb64wiki/index.php/OPEN "OPEN") fileSpec$ [FOR](/qb64wiki/index.php/FOR "FOR") [OUTPUT](/qb64wiki/index.php/OUTPUT "OUTPUT") [AS](/qb64wiki/index.php/AS "AS") #fh: [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #fh [OPEN](/qb64wiki/index.php/OPEN "OPEN") fileSpec$ [FOR](/qb64wiki/index.php/FOR "FOR") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") #fh [PUT](/qb64wiki/index.php/PUT "PUT") #fh, , contents$ [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #fh  ``` |
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


Example
Implementing a simple file copy routine using **\_READFILE$** and **\_WRITEFILE**.


| ``` s$ = "Makefile" d$ = "Makefile - Copy"  r$ = CopyFile$(s$, d$)  [IF](/qb64wiki/index.php/IF "IF") r$ = "" [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Sucessfully copied '"; s$; "' to '"; d$; "'." [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") r$ [END IF](/qb64wiki/index.php/END_IF "END IF")  [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") CopyFile$ (src$, dst$)     CopyFile$ = "" 'empty = success, otherwise error message     buffer$ = [_READFILE$](/qb64wiki/index.php/READFILE$ "READFILE$")(src$)     [IF](/qb64wiki/index.php/IF "IF") buffer$ = "" [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS")(src$) = 0 [THEN](/qb64wiki/index.php/THEN "THEN")         CopyFile$ = "ERROR: Source file not found."     [ELSE](/qb64wiki/index.php/ELSE "ELSE")         slp% = [_INSTRREV](/qb64wiki/index.php/INSTRREV "INSTRREV")(dst$, "\")         [IF](/qb64wiki/index.php/IF "IF") slp% = 0 [THEN](/qb64wiki/index.php/THEN "THEN") slp% = [_INSTRREV](/qb64wiki/index.php/INSTRREV "INSTRREV")(dst$, "/")         [IF](/qb64wiki/index.php/IF "IF") slp% > 0 [THEN](/qb64wiki/index.php/THEN "THEN")             [IF](/qb64wiki/index.php/IF "IF") [NOT](/qb64wiki/index.php/NOT "NOT") [_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")([LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(dst$, slp% - 1)) [THEN](/qb64wiki/index.php/THEN "THEN")                 CopyFile$ = "ERROR: Destination path not found."                 [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION")             [END IF](/qb64wiki/index.php/END_IF "END IF")         [END IF](/qb64wiki/index.php/END_IF "END IF")         _WRITEFILE dst$, buffer$     [END IF](/qb64wiki/index.php/END_IF "END IF") [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Example by RhoSigma
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2713)
* [\_READFILE$](/qb64wiki/index.php/READFILE$ "READFILE$"), [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD"), [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE")
* [\_DEFLATE$](/qb64wiki/index.php/DEFLATE$ "DEFLATE$"), [\_INFLATE$](/qb64wiki/index.php/INFLATE$ "INFLATE$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=WRITEFILE&oldid=8946>"




## Navigation menu








### Search





















