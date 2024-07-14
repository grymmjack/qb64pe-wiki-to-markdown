


\_WINDOWHANDLE - QB64 Phoenix Edition Wiki








# \_WINDOWHANDLE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_WINDOWHANDLE function returns the window handle assigned to the current program by the OS. Windows-only.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*hwnd&&* = \_WINDOWHANDLE
  




## Description


* The result is an [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") number assigned by Windows to your running program.
* Use it to make [API calls](/qb64wiki/index.php/Windows_Libraries "Windows Libraries") that require a window handle to be passed.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Availability


* **Build 20170924/68**.


  




## Examples


*Example:* Showing the system-default message box in Windows.





| ``` 'Message Box Constant values as defined by Microsoft (MBType) [CONST](/qb64wiki/index.php/CONST "CONST") MB_OK& = 0                'OK button only [CONST](/qb64wiki/index.php/CONST "CONST") MB_OKCANCEL& = 1          'OK & Cancel [CONST](/qb64wiki/index.php/CONST "CONST") MB_ABORTRETRYIGNORE& = 2  'Abort, Retry & Ignore [CONST](/qb64wiki/index.php/CONST "CONST") MB_YESNOCANCEL& = 3       'Yes, No & Cancel [CONST](/qb64wiki/index.php/CONST "CONST") MB_YESNO& = 4             'Yes & No [CONST](/qb64wiki/index.php/CONST "CONST") MB_RETRYCANCEL& = 5       'Retry & Cancel [CONST](/qb64wiki/index.php/CONST "CONST") MB_CANCELTRYCONTINUE& = 6 'Cancel, Try Again & Continue [CONST](/qb64wiki/index.php/CONST "CONST") MB_ICONSTOP& = 16         'Error stop sign icon [CONST](/qb64wiki/index.php/CONST "CONST") MB_ICONQUESTION& = 32     'Question-mark icon [CONST](/qb64wiki/index.php/CONST "CONST") MB_ICONEXCLAMATION& = 48  'Exclamation-point icon [CONST](/qb64wiki/index.php/CONST "CONST") MB_ICONINFORMATION& = 64  'Letter i in a circle icon [CONST](/qb64wiki/index.php/CONST "CONST") MB_DEFBUTTON1& = 0        '1st button default(left) [CONST](/qb64wiki/index.php/CONST "CONST") MB_DEFBUTTON2& = 256      '2nd button default [CONST](/qb64wiki/index.php/CONST "CONST") MB_DEFBUTTON3& = 512      '3rd button default(right) [CONST](/qb64wiki/index.php/CONST "CONST") MB_APPLMODAL& = 0         'Message box applies to application only [CONST](/qb64wiki/index.php/CONST "CONST") MB_SYSTEMMODAL& = 4096    'Message box on top of all other windows [CONST](/qb64wiki/index.php/CONST "CONST") MB_SETFOCUS& = 65536      'Set message box as focus [CONST](/qb64wiki/index.php/CONST "CONST") IDOK& = 1                 'OK button pressed [CONST](/qb64wiki/index.php/CONST "CONST") IDCANCEL& = 2             'Cancel button pressed [CONST](/qb64wiki/index.php/CONST "CONST") IDABORT& = 3              'Abort button pressed [CONST](/qb64wiki/index.php/CONST "CONST") IDRETRY& = 4              'Retry button pressed [CONST](/qb64wiki/index.php/CONST "CONST") IDIGNORE& = 5             'Ignore button pressed [CONST](/qb64wiki/index.php/CONST "CONST") IDYES& = 6                'Yes button pressed [CONST](/qb64wiki/index.php/CONST "CONST") IDNO& = 7                 'No button pressed [CONST](/qb64wiki/index.php/CONST "CONST") IDTRYAGAIN& = 10          'Try again button pressed [CONST](/qb64wiki/index.php/CONST "CONST") IDCONTINUE& = 1           'Continue button pressed '----------------------------------------------------------------------------------------  [DECLARE DYNAMIC LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") "user32" [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") MessageBoxA& ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") hwnd [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Message [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), Title [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") MBType [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")) [END DECLARE](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")  DO   msg& = 0: icon& = 0: DB& = 0   [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter Message Box type(0 to 6 other Quits): ", BOX&   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") BOX& < 0 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") BOX& > 6 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")    [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter Icon&(0=none, 1=stop, 2=?, 3=!, 4=info): ", Icon&    [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") BOX& [THEN](/qb64wiki/index.php/THEN "THEN") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") "Enter Default Button(1st, 2nd or 3rd): ", DB&   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") DB& [THEN](/qb64wiki/index.php/THEN "THEN") DB& = DB& - 1     'adjust value to 0, 1, or 2   msg& = MsgBox&("Box Title", "Box text message", BOX&, Icon&, DB&, 4096) 'on top of all windows    [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Button ="; msg& [LOOP](/qb64wiki/index.php/LOOP "LOOP") [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") MsgBox& (Title$, Message$, BoxType&, Icon&, DBtn&, Mode&) [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") Icon&   [CASE](/qb64wiki/index.php/CASE "CASE") 1: Icon& = MB_ICONSTOP&          'warning X-sign icon   [CASE](/qb64wiki/index.php/CASE "CASE") 2: Icon& = MB_ICONQUESTION&      'question-mark icon   [CASE](/qb64wiki/index.php/CASE "CASE") 3: Icon& = MB_ICONEXCLAMATION&   'exclamation-point icon   [CASE](/qb64wiki/index.php/CASE "CASE") 4: Icon& = MB_ICONINFORMATION&   'lowercase letter i in circle   [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE"): Icon& = 0 'no icon [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") BoxType& > 0 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") DBtn& > 0 [THEN](/qb64wiki/index.php/THEN "THEN") 'set default button as 2nd(256) or 3rd(512)   [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") BoxType&     [CASE](/qb64wiki/index.php/CASE "CASE") 2, 3, 6      [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") DBtn& = 2 [THEN](/qb64wiki/index.php/THEN "THEN") Icon& = Icon& + MB_DEFBUTTON3& [ELSE](/qb64wiki/index.php/ELSE "ELSE") Icon& = Icon& + MB_DEFBUTTON2& '3 button     [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE"): Icon& = Icon& + MB_DEFBUTTON2& '2nd button default   [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT") [END IF](/qb64wiki/index.php/END_IF "END IF") Focus& = MB_SetFocus& MsgBox& = MessageBoxA&(_WINDOWHANDLE, Message$, Title$, BoxType& + Icon& + Mode& + Focus&) 'focus on button [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


*Explanation:* Notice how the call to the external dynamic library function MessageBoxA& passes \_WINDOWHANDLE to the API and how the message box shown is created as a child of your program's window, not allowing the main window to be manipulated while the message box is open.
  




## See also


* [\_WINDOWHASFOCUS](/qb64wiki/index.php/WINDOWHASFOCUS "WINDOWHASFOCUS")
* [\_SCREENEXISTS](/qb64wiki/index.php/SCREENEXISTS "SCREENEXISTS")
* [Windows Libraries](/qb64wiki/index.php/Windows_Libraries "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=WINDOWHANDLE&oldid=8492>"




## Navigation menu








### Search





















