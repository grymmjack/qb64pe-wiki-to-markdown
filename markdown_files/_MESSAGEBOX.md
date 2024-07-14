


\_MESSAGEBOX - QB64 Phoenix Edition Wiki








# \_MESSAGEBOX



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_MESSAGEBOX** statement displays a message dialog box, which presents a message to the user.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


**\_MESSAGEBOX** [*title$*][, *message$*][, *iconType$*]
  




## Parameters


* *title$* is the dialog box title
* *message$* is the dialog box message
* *iconType$* is the icon type that is displayed inside the dialog box (this can be **"info"**, **"warning"**, or **"error"**)


  




## Description


* All parameters are optional
* Not using any parameters will show a blank dialog box with an OK button
* The dialog box automatically becomes a modal window if the application window is visible


  




## Availability


* **QB64-PE v3.4.0 and up**


  




## Examples


Example
Hello, world with common dialogs


| ``` username$ = [_INPUTBOX$](/qb64wiki/index.php/INPUTBOX$ "INPUTBOX$")("Hello App", "Enter your name:", "anonymous") [IF](/qb64wiki/index.php/IF "IF") username$ <> "" [THEN](/qb64wiki/index.php/THEN "THEN") _MESSAGEBOX "Hello App", "Hello " + username$, "info"  ``` |
| --- |


  




## See also


* [\_NOTIFYPOPUP](/qb64wiki/index.php/NOTIFYPOPUP "NOTIFYPOPUP")
* [\_MESSAGEBOX (function)](/qb64wiki/index.php/MESSAGEBOX_(function) "MESSAGEBOX (function)")
* [\_INPUTBOX$](/qb64wiki/index.php/INPUTBOX$ "INPUTBOX$")
* [\_SELECTFOLDERDIALOG$](/qb64wiki/index.php/SELECTFOLDERDIALOG$ "SELECTFOLDERDIALOG$")
* [\_COLORCHOOSERDIALOG](/qb64wiki/index.php/COLORCHOOSERDIALOG "COLORCHOOSERDIALOG")
* [\_OPENFILEDIALOG$](/qb64wiki/index.php/OPENFILEDIALOG$ "OPENFILEDIALOG$")
* [\_SAVEFILEDIALOG$](/qb64wiki/index.php/SAVEFILEDIALOG$ "SAVEFILEDIALOG$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MESSAGEBOX&oldid=9017>"




## Navigation menu








### Search





















