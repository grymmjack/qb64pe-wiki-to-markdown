


\_INPUTBOX$ - QB64 Phoenix Edition Wiki








# \_INPUTBOX$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_INPUTBOX$** function displays a prompt in a dialog box, waits for the user to input text or click a button, and returns a string containing the contents of the text box.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*result$* = \_INPUTBOX$([*title$*][, *message$*][, *defaultInput$*])
  




## Parameters


* *title$* is an optional dialog box title.
* *message$* is an optional message or prompt that will be displayed in the dialog box.
* *defaultInput$* is an optional string that is displayed in the text box as the default response if no other input is provided.


  




## Description


* Use *message$* to specify instructions to the user.
* All parameters are optional, hence omitting *defaultInput$* will display a empty text box.
	+ However, if *defaultInput$* is provided, but is an empty string (**""**), then a password box is shown, and the text input will be masked.
* The *result$* may be an empty string (**""**), if the user simply cancelled the dialog.
* The dialog box automatically becomes a modal window, if the application window is visible.


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.4.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.4.0")

**v3.4.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


Example 1
Hello world, with common dialogs.


| ``` username$ = _INPUTBOX$("Hello App", "Enter your name:", "anonymous")  [_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX") "Hello App", "Hello " + username$, "info"  ``` |
| --- |




---


Example 2
Checking whether the user cancelled the input dialog.


| ``` age$ = [_TRIM$](/qb64wiki/index.php/TRIM$ "TRIM$")(_INPUTBOX$(, "Enter your age:"))  [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")(age$) = 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX") , "Cancelled." [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX") , "Age = " + age$ [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |




---


Example 3
Getting passwords.


| ``` password$ = _INPUTBOX$("Login", "Enter password:", "")  [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")(password$) = 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX") , "Cancelled." [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX") , "You entered = " + password$ [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


  




## See also


* [\_MESSAGEBOX](/qb64wiki/index.php/MESSAGEBOX "MESSAGEBOX"), [\_MESSAGEBOX (function)](/qb64wiki/index.php/MESSAGEBOX_(function) "MESSAGEBOX (function)")
* [\_NOTIFYPOPUP](/qb64wiki/index.php/NOTIFYPOPUP "NOTIFYPOPUP"), [\_COLORCHOOSERDIALOG](/qb64wiki/index.php/COLORCHOOSERDIALOG "COLORCHOOSERDIALOG")
* [\_SELECTFOLDERDIALOG$](/qb64wiki/index.php/SELECTFOLDERDIALOG$ "SELECTFOLDERDIALOG$"), [\_OPENFILEDIALOG$](/qb64wiki/index.php/OPENFILEDIALOG$ "OPENFILEDIALOG$"), [\_SAVEFILEDIALOG$](/qb64wiki/index.php/SAVEFILEDIALOG$ "SAVEFILEDIALOG$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INPUTBOX$&oldid=8602>"




## Navigation menu








### Search





















