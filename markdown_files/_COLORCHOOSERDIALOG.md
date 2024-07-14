


\_COLORCHOOSERDIALOG - QB64 Phoenix Edition Wiki








# \_COLORCHOOSERDIALOG



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_COLORCHOOSERDIALOG** function displays a standard color picker dialog box. It returns a 32-bit RGBA color with the alpha channel set to &HFF (255). A zero is returned if the user cancelled.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*color32bpp~&* = \_COLORCHOOSERDIALOG([*title$*][, *defaultRGB~&*])
  




## Parameters


* *title$* is the dialog box title
* *defaultRGB~&* is the default 32-bit RGB color that is pre-selected


  




## Description


* *title$* accepts an empty string (**""**) in which case system defaults are used
* The dialog box automatically becomes a modal window if the application window is visible
* *defaultRGB~&* may be ignored on some platforms


  




## Availability


* **QB64-PE v3.4.0 and up**


  




## Examples


Example
Color selection


| ``` mycolor~& = _COLORCHOOSERDIALOG("Select a color", [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(0, 255, 255)) [IF](/qb64wiki/index.php/IF "IF") mycolor~& <> 0 [THEN](/qb64wiki/index.php/THEN "THEN") [_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX") "Information", "You selected " + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(mycolor~&)  ``` |
| --- |


  




## See also


* [\_NOTIFYPOPUP](/qb64wiki/index.php/NOTIFYPOPUP "NOTIFYPOPUP")
* [\_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX")
* [\_MESSAGEBOX (function)](/qb64wiki/index.php/MESSAGEBOX_(function) "MESSAGEBOX (function)")
* [\_INPUTBOX$](/qb64wiki/index.php/INPUTBOX$ "INPUTBOX$")
* [\_SELECTFOLDERDIALOG$](/qb64wiki/index.php/SELECTFOLDERDIALOG$ "SELECTFOLDERDIALOG$")
* [\_OPENFILEDIALOG$](/qb64wiki/index.php/OPENFILEDIALOG$ "OPENFILEDIALOG$")
* [\_SAVEFILEDIALOG$](/qb64wiki/index.php/SAVEFILEDIALOG$ "SAVEFILEDIALOG$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=COLORCHOOSERDIALOG&oldid=8449>"




## Navigation menu








### Search





















