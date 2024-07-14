


DECLARE LIBRARY - QB64 Phoenix Edition Wiki








# DECLARE LIBRARY



From QB64 Phoenix Edition Wiki
(Redirected from [BYVAL](/qb64wiki/index.php?title=BYVAL&redirect=no "BYVAL"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **DECLARE LIBRARY** declaration allows for the utilization of external library [SUB](/qb64wiki/index.php/SUB "SUB") and [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Parameters](#Parameters) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


**DECLARE [DYNAMIC|CUSTOMTYPE|STATIC] LIBRARY** [*"Library\_name"*][, *"Library\_name2"*][, ...]
{[SUB](/qb64wiki/index.php/SUB "SUB")|[FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")} *Procedure\_name* [**ALIAS** *Library\_procedure*] ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") *Parameter*[{suffix| [AS](/qb64wiki/index.php/AS "AS") [type](/qb64wiki/index.php/Variable_Types "Variable Types")[, *Parameter2*...][, ...)
.
. ' Other SUBs or FUNCTIONs as required
.
**END DECLARE**
  




## Description


* The declaration can be used with:
	+ C/C++ sub-procedures files (*.h* and *.hpp*)
	+ Dynamically linked libraries and shared object files (*.dll*, *.so* and *.dylib*)
	+ Static libraries (*.a*)
	+ Object files (*.o*)
* *Library file names* can be listed to combine more than one supported file name or path into one DECLARE LIBRARY block (**except for dynamically linked libraries and shared object files**). Do not include any file extension (*.h*, *.dll*, *.a* etc.).
* The dynamically linked library or shared object file can be in a relative/absolute path specified along with the library name, in the operating system's directory (e.g., C:\Windows\System32), or in the QB64 directory (alongside your program's executable).
* Specify *""* as the library file name to inform QB64 that the function exists in a library that is already linked and that it must define the C function before calling it, as well as allowing QB64 code to call it.
* It's a good idea to try declaring Operating System API libraries without a library file name first, as most common Operating System headers are already included in QB64 source.
* When using a procedure from a dynamically linked library or shared object (*.dll*, *.so* and *.dylib* files) use **DECLARE DYNAMIC LIBRARY**.
* When using a procedure from a static library (*.a* files) use **DECLARE STATIC LIBRARY**.
* *Procedure\_name* can be any desired procedure name designated by using [ALIAS](/qb64wiki/index.php/ALIAS "ALIAS") with the *Library\_procedure* name following. Enclose *Library\_procedure* in *""* when using a C++ function with the scope operator (e.g., "std::clamp").
* *Parameters* used by the library procedure can be passed by value ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL")) when needed, except for [STRING](/qb64wiki/index.php/STRING "STRING") values.
* QB64 [STRINGs](/qb64wiki/index.php/STRING "STRING") are passed to external libraries as pointers to first character. Many external library procedures expect strings to be NULL terminated. Terminate [STRINGs](/qb64wiki/index.php/STRING "STRING") using [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) wherever it is needed.
* Declarations can be made inside of [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures. Declarations do not need to be at program start.
* C/C++ procedures can use a header file name and the file code must be included with program code.
* C/C++ header files cannot be used with **DECLARE DYNAMIC LIBRARY**. Existence of any *.h* or *.hpp* file of the same name as the dynamically linked library or shared object file will cause DECLARE DYNAMIC LIBRARY to fail.
* The [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") in memory can be used in **CUSTOMTYPE**, **STATIC** and **DYNAMIC LIBRARY** declarations.
* **DECLARE DYNAMIC LIBRARY** let's you specify any [SUB](/qb64wiki/index.php/SUB "SUB")/[FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") calling format you wish, but if the size of the parameters does not match, the size expected within the library, your code will probably cause a GPF (General Protection Fault). It is important to understand that pointers (if required) will be 32-bits in size (the equivalent of a [LONG](/qb64wiki/index.php/LONG "LONG")) when creating a 32-bit program (even under 64-bit Windows).
* **STATIC** is the same as **DYNAMIC** except that it prioritizes linking to static libraries (*.a* and *.o* files) over dynamically linked libraries and shared object files, if both exist.
* **CUSTOMTYPE** is already implied when using **DECLARE DYNAMIC LIBRARY**. This type of library just allows the same flexibility to apply when referencing STATIC libraries that are used to refer to dynamic libraries.
* [SUB](/qb64wiki/index.php/SUB "SUB") procedures using **DECLARE CUSTOMTYPE LIBRARY** API procedures **may error**. Try **DYNAMIC** with the dynamically linked library or shared object file name.
* It is up to the user to document and determine the suitability of all libraries and procedures they choose to use. QB64 cannot guarantee that any procedure will work and cannot guarantee any troubleshooting help.
* QB64 version 1.000 and up produce standalone executables. External dynamically linked libraries or shared object files must be distributed with your program.
* What libraries are or aren't automatically used in the linking process is not formally defined, nor is it guaranteed to stay that way in future versions of QB64.


  




## Parameters


* The *Library\_name* is needed if a library is not already loaded by QB64. Do not include the file extension. Begin the *Library\_name* with **./** or **.\** to make it relative to the path where your source file is saved, so you can keep all your project files together.
* *Procedure\_name* is any program procedure name you want to designate by using [ALIAS](/qb64wiki/index.php/ALIAS "ALIAS") with the *Library\_procedure* name.
* *Library procedure* is the actual procedure name used inside of the library or header file.


  




## Availability


* [![v0.923](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v0.923")

**v0.923**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


* Available for *Linux* and *macOS* since **QB64 v0.940**


  




## Examples


Example 1
Using GLUT library procedure as a program SUB procedure to set the mouse pointer style.


| ``` [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_NORMAL = 1 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_HAND = 2 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_HELP = 4 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_CYCLE = 7 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_TEXT = 8 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_CROSSHAIR = 3 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_UP_DOWN = 10 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_LEFT_RIGHT = 11 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_LEFT_RIGHT_CORNER = 16 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_RIGHT_LEFT_CORNER = 17 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_MOVE = 5 [CONST](/qb64wiki/index.php/CONST "CONST") CURSOR_NONE = 23  DECLARE LIBRARY     [SUB](/qb64wiki/index.php/SUB "SUB") glutSetCursor ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") style&) [END DECLARE](/qb64wiki/index.php/END_DECLARE "END DECLARE")  glutSetCursor CURSOR_CROSSHAIR  ``` |
| --- |


  




Example 2
Using [ALIAS](/qb64wiki/index.php/ALIAS "ALIAS") to create a program SUB or FUNCTION**.**


| ``` DECLARE LIBRARY     [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") GetMilliseconds~&& [ALIAS](/qb64wiki/index.php/ALIAS "ALIAS") GetTicks [END DECLARE](/qb64wiki/index.php/END_DECLARE "END DECLARE")  [DO](/qb64wiki/index.php/DO "DO")     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Seconds since program start:"; GetMilliseconds \ 1000; [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") = 27  ``` |
| --- |


*Explanation:* When a library procedure is used to represent another procedure name use [ALIAS](/qb64wiki/index.php/ALIAS "ALIAS") instead. Saves creating a SUB!
  




Example 3
Don't know if a C function is defined by C++ or QB64? Try using empty quotes.


| ``` DECLARE LIBRARY ""     [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") addone& ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") value&) [END DECLARE](/qb64wiki/index.php/END_DECLARE "END DECLARE")  ``` |
| --- |


*Explanation:* The C function 'addone' exists in a library QB64 already links to, but it hasn't been defined as a C function or a QB64 function. By using "" we are telling QB64 the function exists in a library which is already linked to and that it must define the C function before calling it, as well as allowing QB64 code to call it. Trying the above code without the "" will fail.
  




Example 4
This example plays MIDI files using the *playmidi32.dll* documented here: [Liberty Basic University](http://libertybasicuniversity.com/lbnews/nl110/midi3.htm). Download the following DLL file to your main QB64 directory: [PlayMidi32.dll](https://www.qb64.org/resources/Playmidi32.dll)


| ``` [DECLARE](/qb64wiki/index.php/DECLARE "DECLARE") [DYNAMIC](/qb64wiki/index.php/DYNAMIC "DYNAMIC") [LIBRARY](/qb64wiki/index.php/LIBRARY "LIBRARY") "playmidi32"     [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") PlayMIDI& (filename [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING")) [END DECLARE](/qb64wiki/index.php/END_DECLARE "END DECLARE") result = PlayMIDI(".\samples\qb64\original\ps2battl.mid" + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0)) [PRINT](/qb64wiki/index.php/PRINT "PRINT") result  ``` |
| --- |


  




Example 5
Using a CUSTOMTYPE LIBRARY to return the [Unicode](/qb64wiki/index.php/Unicode "Unicode") version of the current running program's name.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  [DECLARE](/qb64wiki/index.php/DECLARE "DECLARE") [CUSTOMTYPE](/qb64wiki/index.php/CUSTOMTYPE "CUSTOMTYPE") [LIBRARY](/qb64wiki/index.php/LIBRARY "LIBRARY") 'Directory Information using KERNEL32 provided by Dav     [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") GetModuleFileNameA& ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") hModule [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), lpFileName [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") nSize [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") GetModuleFileNameW& ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") hModule [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), lpFileName [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") nSize [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")) [END DECLARE](/qb64wiki/index.php/END_DECLARE "END DECLARE")  '=== SHOW CURRENT PROGRAM FileName$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(512)  Result = GetModuleFileNameA(0, FileName$, [LEN](/qb64wiki/index.php/LEN "LEN")(FileName$)) [IF](/qb64wiki/index.php/IF "IF") Result [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "CURRENT PROGRAM (ASCII): "; [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(FileName$, Result)  'load a unicode font f = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("cyberbit.ttf", 24, "UNICODE") [_FONT](/qb64wiki/index.php/FONT "FONT") f Result = GetModuleFileNameW(0, FileName$, [LEN](/qb64wiki/index.php/LEN "LEN")(FileName$) \ 2) [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 1 [PRINT](/qb64wiki/index.php/PRINT "PRINT") QuickCP437toUTF32$("CURRENT PROGRAM (UTF): ") + QuickUTF16toUTF32$([LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(FileName$, Result * 2)) [_FONT](/qb64wiki/index.php/FONT "FONT") 16 'restore CP437 font  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") QuickCP437toUTF32$ (a$)     b$ = [STRING$](/qb64wiki/index.php/STRING$ "STRING$")([LEN](/qb64wiki/index.php/LEN "LEN")(a$) * 4, 0)     [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(a$)         [ASC](/qb64wiki/index.php/ASC "ASC")(b$, i * 4 - 3) = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(a$, i)     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     QuickCP437toUTF32$ = b$ [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") QuickUTF16toUTF32$ (a$)     b$ = [STRING$](/qb64wiki/index.php/STRING$ "STRING$")([LEN](/qb64wiki/index.php/LEN "LEN")(a$) * 2, 0)     [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(a$) \ 2         [ASC](/qb64wiki/index.php/ASC "ASC")(b$, i * 4 - 3) = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(a$, i * 2 - 1)         [ASC](/qb64wiki/index.php/ASC "ASC")(b$, i * 4 - 2) = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(a$, i * 2)     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     QuickUTF16toUTF32$ = b$ [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Code by Galleon
  




## See also


* [SUB](/qb64wiki/index.php/SUB "SUB"), [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")
* [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL"), [ALIAS](/qb64wiki/index.php/ALIAS "ALIAS")
* [\_OFFSET (function)](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)"), [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") (variable type)
* [C Libraries](/qb64wiki/index.php/C_Libraries "C Libraries"), [DLL Libraries](/qb64wiki/index.php/DLL_Libraries "DLL Libraries"), [Windows Libraries](/qb64wiki/index.php/Windows_Libraries "Windows Libraries")
* [Port Access Libraries](/qb64wiki/index.php/Port_Access_Libraries "Port Access Libraries")
* [SQL Client](/qb64wiki/index.php/SQL_Client "SQL Client")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DECLARE_LIBRARY&oldid=8832>"




## Navigation menu








### Search





















