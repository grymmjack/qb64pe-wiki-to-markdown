


ENVIRON$ - QB64 Phoenix Edition Wiki








# ENVIRON$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The ENVIRON$ function returns a [STRING](/qb64wiki/index.php/STRING "STRING") environmental value from **Windows'** environmental settings list.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*setting$* = ENVIRON$({*listIndex%*|*systemID$*})
  




## Description


* The function can use an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") *listIndex%* value or [STRING](/qb64wiki/index.php/STRING "STRING") *systemID$* parameter.
* *listIndex%* refers to the number order of the environmental list. Returns are not in any particular numerical order.
* *systemID$* is the specific [STRING](/qb64wiki/index.php/STRING "STRING") parameter requested. Returns only the specified environmental [STRING](/qb64wiki/index.php/STRING "STRING") setting:
	+ "BLASTER" = current Sound Blaster settings if installed.
	+ "COMPUTERNAME" or "USERDOMAIN" = OEM PC serial number or the computer name assigned by owner.
	+ "HOMEDRIVE" or "SystemDrive" = Windows root drive, normally C: on single partition drives.
	+ "HOMEPATH" = current user's Administrator or the single user's "OWNER" folder path.
	+ "OS" = Windows Operating System version. Often WindowsNT in modern computers.
	+ "PATH" = full path setting that Windows uses to look for file extensions in PATHEXT below.
	+ "PATHEXT = Windows extensions used: COM, EXE, BAT, CMD, VBS, VBE, JS, JSE, WSF, WSH, MSC
	+ "PROCESSOR\_ARCHITECTURE" = x86 for 32 or 64 bit.
	+ "PROGRAMFILES" = path to *Program files* folder, normally "C:\PROGRAM FILES"
	+ "PROMPT" = normally "$P$G" on Windows NT.
	+ "SYSTEMROOT" or "windir" = path to the Windows folder including the drive letter like "C:\WINDOWS"
	+ "TEMP" or "TMP" = path to TEMP folder. "C:\TEMP" or the user specific temp folder on later versions.
	+ "USERNAME" = current Administrator name or "OWNER".


*Note:* There are other possible system settings that are not listed or never used on older versions. Run *Example 1* below for a complete list in your system.
* *Note:* **QB64** may not return the same environment list as QBasic or SET did in DOS.


  




## Examples


*Example 1:* Viewing the list of environmental parameter settings using a counter loop like SET does in DOS.





| ``` [DO](/qb64wiki/index.php/DO "DO")   i = i + 1   setting$ = ENVIRON$(i) ' get a setting from the list   [PRINT](/qb64wiki/index.php/PRINT "PRINT") setting$   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") i [MOD](/qb64wiki/index.php/MOD "MOD") 20 = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press a key": [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): [CLS](/qb64wiki/index.php/CLS "CLS") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") setting$ = ""  ``` |
| --- |




| ``` ALLUSERSPROFILE=C:\ProgramData COMPUTERNAME=TED-LAPTOP ComSpec=C:\WINDOWS\system32\cmd.exe HOMEDRIVE=C: HOMEPATH=\Users\Ted LOCALAPPDATA=C:\Users\Ted\AppData\Local OS=Windows_NT Path=C:\PROGRAMDATA\ORACLE\JAVA\JAVAPATH;C:\WINDOWS\SYSTEM32;C:\WINDOWS; C:\WINDOWS\SYSTEM32\WBEM;C:\WINDOWS\SYSTEM32\WINDOWSPOWERSHELL\V1.0\;C:\ WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32 \WindowsPowerShell\v1.0\ PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC PROCESSOR_ARCHITECTURE=x86 PROCESSOR_IDENTIFIER=x86 Family 6 Model 14 Stepping 8, GenuineIntel ProgramFiles=C:\Program Files PROMPT=$P$G PSModulePath=C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules\ SystemRoot=C:\WINDOWS TEMP=C:\Users\TED\AppData\Local\Temp TMP=C:\Users\TED\AppData\Local\Temp USERDOMAIN=TED-LAPTOP USERNAME=Ted USERPROFILE=C:\Users\Ted  ``` |
| --- |


*Note:* Windows environmental settings are listed alphabetically, 20 at a time. **QB64 may not read all of them or may return an empty string.** The settings above were returned with SET in DOS. PROMPT returned nothing where SET returned $P$G.
  

*Example 2:* Creating a shortcut on a user's desktop for QB64.EXE using the program's icon. Must be run in program's folder to work!





| ``` '=== Enter the EXE file and ICON or BMP image for the shortcut.  Program$ = "QB64.EXE"  '<<<<<<<<<< Enter the **exact** program name for shortcut ICON$ = "QB64ICON.BMP" '<<<<<<<<<< Enter icon or bitmap to use from program's folder  DeskTopShortcut Program$, ICON$  [END](/qb64wiki/index.php/END "END")             '====== END DEMO CODE ======  [SUB](/qb64wiki/index.php/SUB "SUB") DeskTopShortcut (Program$, ICON$) f = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") [SHELL](/qb64wiki/index.php/SHELL "SHELL") [_HIDE](/qb64wiki/index.php/HIDE "HIDE") "CD > PRGMDIR.INF"  'get the current program path [OPEN](/qb64wiki/index.php/OPEN "OPEN") "PRGMDIR.INF" [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") [AS](/qb64wiki/index.php/AS "AS") #f [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") #f, PATH$ [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #f [KILL](/qb64wiki/index.php/KILL "KILL") "PRGMDIR.INF" PATH$ = PATH$ + "\": FILE$ = PATH + Program$ PRINT PATH$                         'DEMO print A$ = ENVIRON$("HOMEDRIVE")          '=== Get Current User setting from Environment. B$ = ENVIRON$("HOMEPATH") C$ = A$ + B$                        'shortcut to user's desktop if found  [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") C$ = "" [THEN](/qb64wiki/index.php/THEN "THEN") C$ = ENVIRON$("ALLUSERSPROFILE") 'try desktop for all users PRINT C$                            'DEMO print URLFILE$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(Program$, 1, [INSTR](/qb64wiki/index.php/INSTR "INSTR")(Program$, ".")) + "URL" 'change EXE to URL  [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") C$ > "" [THEN](/qb64wiki/index.php/THEN "THEN")      SHORTCUT$ = C$ + "\Desktop\" + URLFILE$ 'create filename for the desktop [ELSE](/qb64wiki/index.php/ELSE "ELSE") SHORTCUT$ = PATH$ + URLFILE$   'if all else fails put in program folder [END IF](/qb64wiki/index.php/END_IF "END IF") PRINT SHORTCUT                      'DEMO print [OPEN](/qb64wiki/index.php/OPEN "OPEN") SHORTCUT$ [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [APPEND](/qb64wiki/index.php/APPEND "APPEND") [AS](/qb64wiki/index.php/AS "AS") #f [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LOF](/qb64wiki/index.php/LOF "LOF")(f) [THEN](/qb64wiki/index.php/THEN "THEN") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #f: [EXIT SUB](/qb64wiki/index.php/EXIT_SUB "EXIT SUB")   '=== if filesize is NOT Zero don't overwrite!  Q$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34)                       '=== Write URL Shortcut file info. [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #f, "[InternetShortcut]"                    'URL type [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #f, "URL=" + Q$ + "file://" + FILE$ + Q$    'URL program file [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #f, "WorkingDirectory=" + Q$ + PATH$ + Q$   'Working path [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #f, "IconIndex = " + Q$ + "0" + Q$          '0 is first index [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #f, "IconFile = " + Q$ + PATH$ + ICON$ + Q$ 'Icon path in working folder [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #f [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Adapted from code by Dav
*Explanation:* The SUB program finds the current program's path and user's desktop path. It then creates the shortcut on the desktop with a program icon. The custom icon should be in the program's folder. If an environmental path is not found, the shortcut is placed in the program's folder. The SUB can be added to any program.
**NOTE:** A temorary file named PRGMDIR.INF is created and deleted in the example above.
  




## See also


* [ENVIRON](/qb64wiki/index.php/ENVIRON "ENVIRON") (statement)
* [\_DEVICES](/qb64wiki/index.php/DEVICES "DEVICES"), [\_DEVICE$](/qb64wiki/index.php/DEVICE$ "DEVICE$")
* [\_LASTBUTTON](/qb64wiki/index.php/LASTBUTTON "LASTBUTTON"), [\_OS$](/qb64wiki/index.php/OS$ "OS$")
* [Windows Environment](/qb64wiki/index.php/Windows_Environment "Windows Environment")
* [Windows User Paths Library](/qb64wiki/index.php/Windows_Libraries#Windows_User "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ENVIRON$&oldid=8125>"




## Navigation menu








### Search





















