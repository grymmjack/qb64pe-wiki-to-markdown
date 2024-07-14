


\_NOTIFYPOPUP - QB64 Phoenix Edition Wiki








# \_NOTIFYPOPUP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_NOTIFYPOPUP** statement shows a system notification.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


**\_NOTIFYPOPUP** [*title$*][, *message$*][, *iconType$*]
  




## Parameters


* *title$* is the notification title (usually appears above message and in bold)
* *message$* is the notification message
* *iconType$* is the notification icon type (this can be **"info"**, **"warning"**, or **"error"**)


  




## Description


* All parameters are optional
* Not using any parameters will show a blank notification
* The notification popup will show where OS notifications are expected / configured by the system


  




## Availability


* **QB64-PE v3.4.0 and up**


  




## Examples


Example
Show a system notification after completing a lengthy task


| ``` _NOTIFYPOPUP "My Cool App", "Conversion complete!", "info"  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2843)
* [\_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX")
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





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=NOTIFYPOPUP&oldid=9022>"




## Navigation menu








### Search





















