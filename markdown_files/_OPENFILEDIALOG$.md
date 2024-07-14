


\_OPENFILEDIALOG$ - QB64 Phoenix Edition Wiki








# \_OPENFILEDIALOG$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_OPENFILEDIALOG$** function displays a standard dialog box that prompts the user to open a file. The returned string is an empty string (**""**) if the user cancelled. The returned string will contain file paths delimited using **"|"** if allowMultipleSelects& is passed as **-1** (true) and multiple files are selected by the user.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*result$* = \_OPENFILEDIALOG$([*title$*][, *defaultPathAndFile$*][, *filterPatterns$*][, *singleFilterDescription$*][, *allowMultipleSelects&*])
  




## Parameters


* *title$* is the dialog box title
* *defaultPathAndFile$* is the default path that will be used by the dialog box if not changed by the user
* *filterPatterns$* are the file filters separated using **"|"** (e.g., "\*.png|\*.jpg|\*.gif")
* *singleFilterDescription$* is the single filter description (e.g., "Image files")
* *allowMultipleSelects&* can be **0** (false) or **-1** (true) if multiple file selection is to be allowed. If omitted, then this defaults to **0** (false)


  




## Description


* All parameters accept an empty string (**""**) in which case system defaults are used
* If *singleFilterDescription$* is an empty string (**""**), then *filterPatterns$* will be shown in it's place
* The dialog box automatically becomes a modal window if the application window is visible


  




## Availability


* **QB64-PE v3.4.0 and up**


  




## Examples


Example
Simple open file dialog example


| ``` audiofiles$ = _OPENFILEDIALOG$("Open File", "", "*.mp3|*.ogg|*.wav|*.flac", "Audio files", -1) [IF](/qb64wiki/index.php/IF "IF") audiofiles$ <> "" [THEN](/qb64wiki/index.php/THEN "THEN") [_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX") "Information", "You selected " + audiofiles$  ``` |
| --- |


  




## See also


* [\_NOTIFYPOPUP](/qb64wiki/index.php/NOTIFYPOPUP "NOTIFYPOPUP")
* [\_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX")
* [\_MESSAGEBOX (function)](/qb64wiki/index.php/MESSAGEBOX_(function) "MESSAGEBOX (function)")
* [\_INPUTBOX$](/qb64wiki/index.php/INPUTBOX$ "INPUTBOX$")
* [\_SELECTFOLDERDIALOG$](/qb64wiki/index.php/SELECTFOLDERDIALOG$ "SELECTFOLDERDIALOG$")
* [\_COLORCHOOSERDIALOG](/qb64wiki/index.php/COLORCHOOSERDIALOG "COLORCHOOSERDIALOG")
* [\_SAVEFILEDIALOG$](/qb64wiki/index.php/SAVEFILEDIALOG$ "SAVEFILEDIALOG$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OPENFILEDIALOG$&oldid=8452>"




## Navigation menu








### Search





















