


\_SAVEFILEDIALOG$ - QB64 Phoenix Edition Wiki








# \_SAVEFILEDIALOG$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_SAVEFILEDIALOG$** function displays a standard dialog box that prompts the user to save a file. The returned string is an empty string (**""**) if the user cancelled.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*result$* = \_SAVEFILEDIALOG$([*title$*][, *defaultPathAndFile$*][, *filterPatterns$*][, *singleFilterDescription$*])
  




## Parameters


* *title$* is the dialog box title
* *defaultPathAndFile$* is the default path that will be used by the dialog box if not changed by the user
* *filterPatterns$* are the file filters separated using **"|"** (e.g., "\*.png|\*.jpg|\*.gif")
* *singleFilterDescription$* is the single filter description (e.g., "Image files")


  




## Description


* All parameters accept an empty string (**""**) in which case system defaults are used
* If *singleFilterDescription$* is an empty string (**""**), then *filterPatterns$* will be shown in it's place
* The dialog box automatically becomes a modal window if the application window is visible


  




## Availability


* **QB64-PE v3.4.0 and up**


  




## Examples


Example
Simple save file dialog example


| ``` [IF](/qb64wiki/index.php/IF "IF") [NOT](/qb64wiki/index.php/NOT "NOT") filesaved& [THEN](/qb64wiki/index.php/THEN "THEN")     textfile$ = _SAVEFILEDIALOG$("Save File", "", "*.txt|*.doc", "Text files")     [IF](/qb64wiki/index.php/IF "IF") textfile$ <> "" [THEN](/qb64wiki/index.php/THEN "THEN")         filesaved& = -1         [_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX") "Information", "File will be saved to " + textfile$     [END IF](/qb64wiki/index.php/END_IF "END IF") [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


  




## See also


* [\_NOTIFYPOPUP](/qb64wiki/index.php/NOTIFYPOPUP "NOTIFYPOPUP")
* [\_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX")
* [\_MESSAGEBOX (function)](/qb64wiki/index.php/MESSAGEBOX_(function) "MESSAGEBOX (function)")
* [\_INPUTBOX$](/qb64wiki/index.php/INPUTBOX$ "INPUTBOX$")
* [\_SELECTFOLDERDIALOG$](/qb64wiki/index.php/SELECTFOLDERDIALOG$ "SELECTFOLDERDIALOG$")
* [\_COLORCHOOSERDIALOG](/qb64wiki/index.php/COLORCHOOSERDIALOG "COLORCHOOSERDIALOG")
* [\_OPENFILEDIALOG$](/qb64wiki/index.php/OPENFILEDIALOG$ "OPENFILEDIALOG$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SAVEFILEDIALOG$&oldid=8453>"




## Navigation menu








### Search





















