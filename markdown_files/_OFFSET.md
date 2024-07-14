


\_OFFSET - QB64 Phoenix Edition Wiki








# \_OFFSET



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_OFFSET variable type stores the location of a value in memory. The byte size varies as required by the system.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[DIM](/qb64wiki/index.php/DIM "DIM") variable [AS](/qb64wiki/index.php/AS "AS") **\_OFFSET**
  




## Description


* \_OFFSET types can be created as signed or [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") at the programmer's discretion.
* The type suffix for \_OFFSET is **%&** which designates the integer value's flexible size.
* Offset values are only useful when used in conjunction with [\_MEM](/qb64wiki/index.php/MEM "MEM") or [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") procedures.
* OFFSET values are used as a part of the [\_MEM](/qb64wiki/index.php/MEM "MEM") variable [type](/qb64wiki/index.php/Variable_Types "Variable Types") in QB64. Variable.OFFSET returns or sets the current position in memory.
* API [LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") parameter or [type](/qb64wiki/index.php/TYPE "TYPE") names may include **lp, ptr** or **p** which designates them as a pointer type.
* **Warning: \_OFFSET values cannot be cast to other variable type values reliably.**
* **Warning: Variable length [STRING](/qb64wiki/index.php/STRING "STRING") values can move about in memory at any time.** If you get the \_OFFSET of a variable length sting on one code line and use it on the next it may not be there anymore. **To be safe, move variable length strings into fixed length strings first.**


  




## Examples


*Example:* The SHBrowseForFolder function receives information about the folder selected by the user in Windows XP and 7.





| ``` [DECLARE CUSTOMTYPE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")     [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") FindWindow& ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") ClassName AS _OFFSET, WindowName$) [END](/qb64wiki/index.php/END "END") [DECLARE](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")  [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "Super Window" hwnd& = FindWindow(0, "Super Window" + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0))  [TYPE](/qb64wiki/index.php/TYPE "TYPE") BROWSEINFO  'typedef struct _browseinfo '[Microsoft MSDN](http://msdn.microsoft.com/en-us/library/bb773205%28v=vs.85%29.aspx)   hwndOwner [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") '              '  HWND   pidlRoot [AS](/qb64wiki/index.php/AS "AS") _OFFSET '            '  PCIDLIST_ABSOLUTE   pszDisplayName [AS](/qb64wiki/index.php/AS "AS") _OFFSET '      '  LPTSTR   lpszTitle [AS](/qb64wiki/index.php/AS "AS") _OFFSET '           '  LPCTSTR   ulFlags [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")        '  UINT   lpfn [AS](/qb64wiki/index.php/AS "AS") _OFFSET '                '  BFFCALLBACK   lParam [AS](/qb64wiki/index.php/AS "AS") _OFFSET '              '  LPARAM   iImage [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") '                 '  int [END](/qb64wiki/index.php/END "END") [TYPE](/qb64wiki/index.php/TYPE "TYPE")  'BROWSEINFO, *PBROWSEINFO, *LPBROWSEINFO;  [DECLARE DYNAMIC LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") "shell32"   [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") SHBrowseForFolder%& (x [AS](/qb64wiki/index.php/AS "AS") BROWSEINFO) '[Microsoft MSDN](http://msdn.microsoft.com/en-us/library/bb762115%28v=vs.85%29.aspx)   [SUB](/qb64wiki/index.php/SUB "SUB") SHGetPathFromIDList ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") lpItem [AS](/qb64wiki/index.php/AS "AS") _OFFSET, [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") szDir [AS](/qb64wiki/index.php/AS "AS") _OFFSET) '[Microsoft MSDN](http://msdn.microsoft.com/en-us/library/bb762194%28VS.85%29.aspx) [END DECLARE](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")  [DIM](/qb64wiki/index.php/DIM "DIM") b [AS](/qb64wiki/index.php/AS "AS") BROWSEINFO b.hwndOwner = hwnd [DIM](/qb64wiki/index.php/DIM "DIM") s [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 1024 b.pszDisplayName = [_OFFSET](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)")(s$) a$ = "Choose a folder!!!" + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) b.lpszTitle = [_OFFSET](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)")(a$) [DIM](/qb64wiki/index.php/DIM "DIM") o [AS](/qb64wiki/index.php/AS "AS") _OFFSET o = SHBrowseForFolder(b) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") o [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(s$, [INSTR](/qb64wiki/index.php/INSTR "INSTR")(s$, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0)) - 1)     [DIM](/qb64wiki/index.php/DIM "DIM") s2 [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 1024     SHGetPathFromIDList o, [_OFFSET](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)")(s2$)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(s2$, [INSTR](/qb64wiki/index.php/INSTR "INSTR")(s2$, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0)) - 1) [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Cancel?" [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


Code by Galleon
  




## See also


* [\_WINDOWHANDLE](/qb64wiki/index.php/WINDOWHANDLE "WINDOWHANDLE")
* [Using \_OFFSET](/qb64wiki/index.php/Using_OFFSET "Using OFFSET")
* [\_OFFSET (function)](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)"), [\_MEM](/qb64wiki/index.php/MEM "MEM")
* [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")
* [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OFFSET&oldid=8800>"




## Navigation menu








### Search





















