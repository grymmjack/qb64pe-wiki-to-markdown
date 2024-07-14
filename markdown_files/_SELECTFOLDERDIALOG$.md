


\_SELECTFOLDERDIALOG$ - QB64 Phoenix Edition Wiki








# \_SELECTFOLDERDIALOG$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_SELECTFOLDERDIALOG$** function displays a dialog box that enables the user to select a folder (directory). The returned string is a folder path or an empty string (**""**) if the user cancelled.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*folder$* = \_SELECTFOLDERDIALOG$([*title$*][, *defaultPath$*])
  




## Parameters


* *title$* is a string that is displayed above the folder tree view in the dialog box
* *defaultPath$* is the default folder that is pre-selected (if the folder exists)


  




## Description


* All parameters accept an empty string (**""**) in which case system defaults are used
* Use the title$ to specify instructions to the user
* The dialog box automatically becomes a modal window if the application window is visible
* The folder selected must exist in the filesystem else an empty string is returned


  




## Availability


* **QB64-PE v3.4.0 and up**


  




## Examples


Example
Folder selection


| ``` folder$ = _SELECTFOLDERDIALOG$("Select a folder to scan:") [IF](/qb64wiki/index.php/IF "IF") folder$ <> "" [THEN](/qb64wiki/index.php/THEN "THEN") [_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX") "Information", "You selected " + folder$  ``` |
| --- |


  




## See also


* [\_NOTIFYPOPUP](/qb64wiki/index.php/NOTIFYPOPUP "NOTIFYPOPUP")
* [\_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX")
* [\_MESSAGEBOX (function)](/qb64wiki/index.php/MESSAGEBOX_(function) "MESSAGEBOX (function)")
* [\_INPUTBOX$](/qb64wiki/index.php/INPUTBOX$ "INPUTBOX$")
* [\_COLORCHOOSERDIALOG](/qb64wiki/index.php/COLORCHOOSERDIALOG "COLORCHOOSERDIALOG")
* [\_OPENFILEDIALOG$](/qb64wiki/index.php/OPENFILEDIALOG$ "OPENFILEDIALOG$")
* [\_SAVEFILEDIALOG$](/qb64wiki/index.php/SAVEFILEDIALOG$ "SAVEFILEDIALOG$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SELECTFOLDERDIALOG$&oldid=8448>"




## Navigation menu








### Search





















