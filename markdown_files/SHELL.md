


SHELL - QB64 Phoenix Edition Wiki








# SHELL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The SHELL statement allows a program to run external programs or command line statements in Windows, macOS and Linux.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) 	+ [3.1 More examples](#More_examples) * [4 See also](#See_also) |
| --- |


## Syntax


SHELL [*DOSCommand$*]
SHELL [**\_DONTWAIT**] [**\_HIDE**] [*DOSCommand$*]
  




## Description


* If the *DOSCommand$* [STRING](/qb64wiki/index.php/STRING "STRING") parameter isn't used, the "command console" is opened and execution is halted until the user closes it manually.
* If [\_DONTWAIT](/qb64wiki/index.php/DONTWAIT "DONTWAIT") is used, the **QB64** program doesn't wait for the SHELLed program/command to end.
* When the [\_HIDE](/qb64wiki/index.php/HIDE "HIDE") action is used, the [console](/qb64wiki/index.php/CONSOLE "CONSOLE") window is hidden and screen info can be "redirected" (using redirection characters like >) to a file (recommended).
* Commands are external commands, according to the user's operating system, passed as [strings](/qb64wiki/index.php/STRING "STRING") enclosed in quotes or string variables.
* Commands can be a mixture of [strings](/qb64wiki/index.php/STRING "STRING") and string variables added together using the + [concatenation](/qb64wiki/index.php/Concatenation "Concatenation") operator.
* Command text can be in upper or lower case. Use single spacing between items and options.
* **QB64** automatically uses CMD /C when using SHELL, but it is allowed in a command string. Note: CMD alone may lock up program.
	+ **Note: Some commands may not work without adding CMD /C to the start of the command line.**
* **QB64** program screens will not get distorted, minimized or freeze the program like QBasic fullscreen modes would.
* **QB64** can use long path folder names and file names and SHELL command lines can be longer than 124 characters.
* In Windows, use additional [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) quotation marks around folder or file names that contain spaces.
* For other operating systems, both the quotation mark character and the apostrophe can be used to enclose a file name that contains spaces.
* **NOTE: Use [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR") instead of CD as SHELL commands cannot affect the current program path.**


### QBasic/QuickBASIC


* **QBasic BAS files could be run like compiled programs without returning to the IDE when [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM") was used to [end](/qb64wiki/index.php/END "END") them.**
* A user would invoke it with SHELL "QB.EXE /L /RUN program.BAS"


  




## Examples


*Example 1:* When working with file or folder names with spaces, add quotation marks around the path and/or file name with [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34).





| ``` SHELL [_HIDE](/qb64wiki/index.php/HIDE "HIDE") "dir " + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) + "free cell.ico" + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) + " /b > temp.dir" SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window  ``` |
| --- |




| ``` Free Cell.ico  ``` |
| --- |


Contents of the temp.dir text file
  

*Example 2:* Opening a Windows program (Notepad) to read or print a Basic created text file.





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a file name to read in Notepad: ", filename$ SHELL "CMD /C start /max notepad " + filename$  ' display in Notepad full screen in XP or NT  'SHELL "start /min notepad /p " + filename$ ' taskbar print using QB64 CMD /C not necessary  ``` |
| --- |


*Explanation:* Notepad is an easy program to open in Windows as no path is needed. Windows NT computers, including XP, use CMD /C where older versions of DOS don't require any command reference. The top command opens Notepad in a normal window for a user to view the file. They can use Notepad to print it. The second command places Notepad file in the taskbar and prints it automatically. The filename variable is added by the program using proper spacing.
* **Start** is used to allow a Basic program to run without waiting for Notepad to be closed.
* **/min** places the window into the taskbar. **/max** is fullscreen and no option is a normal window.
* Notepad's **/p** option prints the file contents, even with USB printers.

  



*Example 3:* Function that returns the program's current working path.





| ```  currentpath$ = Path$ ' function call saves a path for later program use  PRINT currentpath$   [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") Path$    SHELL [_HIDE](/qb64wiki/index.php/HIDE "HIDE") "CD > D0S-DATA.INF"   'code to hide window in **QB64**    [OPEN](/qb64wiki/index.php/OPEN "OPEN") "D0S-DATA.INF" FOR [APPEND](/qb64wiki/index.php/APPEND "APPEND") AS #1  'this may create the file         L% = [LOF](/qb64wiki/index.php/LOF "LOF")(1)          'verify that file and data exist    [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1    [IF](/qb64wiki/index.php/IF "IF") L% [THEN](/qb64wiki/index.php/THEN "THEN")                       'read file if it has data      [OPEN](/qb64wiki/index.php/OPEN "OPEN") "D0S-DATA.INF" FOR [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") AS #1      [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") #1, line$           'read only line in file      Path$ = line$ + "\"            'add slash to path so only a filename needs added later      [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1    [ELSE](/qb64wiki/index.php/ELSE "ELSE") : Path = ""                 'returns zero length string if path not found    END IF    [KILL](/qb64wiki/index.php/KILL "KILL") "D0S-DATA.INF"              'deleting the file is optional  [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* The **SHELL "CD"** statement requests the current working path. This info is normally printed to the screen, but the **>** pipe character sends the information to the DOS-DATA.INF file instead(**QB64** can use [\_HIDE](/qb64wiki/index.php/HIDE "HIDE") to not display the DOS window). The function uses the [OPEN](/qb64wiki/index.php/OPEN "OPEN") FOR [APPEND](/qb64wiki/index.php/APPEND "APPEND") mode to check for the file and the data([INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") would create an error if file does not exist). The current path is listed on one line of the file. The file is opened and [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") returns one line of the file text. The function adds a "\" so that the Path$ returned can be used in another file statement by just adding a file name. Save the Path$ to another variable for later use when the program has moved to another directory.
In **QB64** you can simply use the [\_CWD$](/qb64wiki/index.php/CWD$ "CWD$") statement for the same purpose of the example above.
  

*Example 4:* Determining if a drive or path exists. Cannot use with a file name specification.





| ``` [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") "Enter a drive or path (no file name): ", DirPath$ [IF](/qb64wiki/index.php/IF "IF") PathExist%(DirPath$) [THEN](/qb64wiki/index.php/THEN "THEN") PRINT "Drive Path exists!" [ELSE](/qb64wiki/index.php/ELSE "ELSE") PRINT "Drive Path does not exist!" [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") PathExist% (Path$) PathExist% = 0 [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")(Path$) = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION") 'no entry [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")([ENVIRON$](/qb64wiki/index.php/ENVIRON$ "ENVIRON$")("OS")) [THEN](/qb64wiki/index.php/THEN "THEN") CMD$ = "CMD /C " [ELSE](/qb64wiki/index.php/ELSE "ELSE") CMD$ = "COMMAND /C " SHELL [_HIDE](/qb64wiki/index.php/HIDE "HIDE") CMD$ + "If Exist " + Path$ + "\nul echo yes > D0S-DATA.INF" [OPEN](/qb64wiki/index.php/OPEN "OPEN") "D0S-DATA.INF" [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [APPEND](/qb64wiki/index.php/APPEND "APPEND") [AS](/qb64wiki/index.php/AS "AS") #1 [IF](/qb64wiki/index.php/IF "IF") [LOF](/qb64wiki/index.php/LOF "LOF")(1) [THEN](/qb64wiki/index.php/THEN "THEN") PathExist% = -1             'yes will be in file if path exists [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1 [KILL](/qb64wiki/index.php/KILL "KILL") "D0S-DATA.INF"               'delete data file optional [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Code by Ted Weissgerber
*Explanation: IF Exist* checks for the drive path. *\Nul* allows an emply folder at end of path. *Echo* prints **yes** in the file if it exists.
In **QB64** you can simply use the [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS") statement for the same purpose of the example above.
  

*Snippet 1:* When looking for **printers** this command gives you a file list with the default printer marked as **TRUE**:





| ``` SHELL [_HIDE](/qb64wiki/index.php/HIDE "HIDE") "CMD /C" + "wmic printer get name,default > default.txt"  ``` |
| --- |


**Created file's text:**





| ``` Default  Name   FALSE    Microsoft XPS Document Writer   TRUE     HP Photosmart C7200 series   FALSE    HP Officejet Pro 8600   FALSE    Fax  ``` |
| --- |


*Explanation:* [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") could be used to find the printer names as [STRING](/qb64wiki/index.php/STRING "STRING") variables.
  

*Snippet 2:* Here is the code to set the default printer to the "HP Officejet Pro 8600":





| ``` SHELL _HIDE "CMD /C" + "wmic printer where name='HP Officejet Pro 8600' call setdefaultprinter"  ``` |
| --- |


After executing this program, and then running the first snippet again, we see the following **contents of the text file:**


| ``` Default  Name   FALSE    Microsoft XPS Document Writer   FALSE    HP Photosmart C7200 series   TRUE     HP Officejet Pro 8600   FALSE    Fax  ``` |
| --- |


### More examples


* [FILELIST$ (function)](/qb64wiki/index.php/FILELIST$_(function) "FILELIST$ (function)")
* [FileExist Library Function](/qb64wiki/index.php/Windows_Libraries#File_Exist "Windows Libraries")


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1282)
* [SHELL (function)](/qb64wiki/index.php/SHELL_(function) "SHELL (function)"), [\_SHELLHIDE](/qb64wiki/index.php/SHELLHIDE "SHELLHIDE")
* [FILES](/qb64wiki/index.php/FILES "FILES"), [CHDIR](/qb64wiki/index.php/CHDIR "CHDIR"), [MKDIR](/qb64wiki/index.php/MKDIR "MKDIR")
* [\_CWD$](/qb64wiki/index.php/CWD$ "CWD$"), [\_STARTDIR$](/qb64wiki/index.php/STARTDIR$ "STARTDIR$")
* [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS"), [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")
* [RMDIR](/qb64wiki/index.php/RMDIR "RMDIR"), [NAME](/qb64wiki/index.php/NAME "NAME"), [KILL](/qb64wiki/index.php/KILL "KILL"), [RUN](/qb64wiki/index.php/RUN "RUN")
* [\_HIDE](/qb64wiki/index.php/HIDE "HIDE"), [\_DONTWAIT](/qb64wiki/index.php/DONTWAIT "DONTWAIT")
* [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE"), [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE")
* [$SCREENHIDE](/qb64wiki/index.php/$SCREENHIDE "$SCREENHIDE"), [$SCREENSHOW](/qb64wiki/index.php/$SCREENSHOW "$SCREENSHOW")
* [\_SCREENHIDE](/qb64wiki/index.php/SCREENHIDE "SCREENHIDE"), [\_SCREENSHOW](/qb64wiki/index.php/SCREENSHOW "SCREENSHOW")
* [FILELIST$](/qb64wiki/index.php/FILELIST$ "FILELIST$"), [DIR$](/qb64wiki/index.php/PDS(7.1)_Procedures#DIR$ "PDS(7.1) Procedures")
* [Windows Open and Save Dialog Boxes](/qb64wiki/index.php/Windows_Libraries#File_Dialog_Boxes "Windows Libraries")
* [C Console Library](/qb64wiki/index.php/C_Libraries#Console_Window "C Libraries")
* [Windows Printer Settings](/qb64wiki/index.php/Windows_Printer_Settings "Windows Printer Settings")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SHELL&oldid=8924>"




## Navigation menu








### Search





















