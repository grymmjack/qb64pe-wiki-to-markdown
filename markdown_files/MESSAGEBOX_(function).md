## _MESSAGEBOX (function)
---

### The _MESSAGEBOX function displays a message dialog box, which presents a message and returns the button ID clicked by the user. The return value can be 0 for "cancel" / "no" , 1 for "ok" / "yes" , 2 for "no" in "yesnocancel" .

#### SYNTAX

`result& = _MESSAGEBOX ([ title$ ][, message$ ][, dialogType$ ][, iconType$ ][, defaultButton& ])`

#### PARAMETERS
* title$ is the dialog box title
* message$ is the dialog box message
* dialogType$ is the dialog box type and shows different buttons based on the value (this can be "ok" , "okcancel" , "yesno" , or "yesnocancel" )
* iconType$ is the icon type that is displayed inside the dialog box (this can be "info" , "warning" , "error" , or "question" )
* defaultButton& can be 0 for "cancel" / "no" , 1 for "ok" / "yes" , 2 for "no" in "yesnocancel"


#### DESCRIPTION
* "ok" , "okcancel" , "yesno" , or "yesnocancel" can be in any case
* "info" , "warning" , "error" , or "question" can be in any case
* All parameters accept nothing or an empty string ( "" ). In both cases system defaults are used
* The dialog box automatically becomes a modal window if the application window is visible


#### EXAMPLES
```vb
IF _MESSAGEBOX("My Cool App", "Do you want to hear a beep?", "yesno", "question") = 1 THEN
   BEEP
ELSE
   _MESSAGEBOX "My Cool App", "The sound of silence."
END IF
```
  


#### SEE ALSO
* [_NOTIFYPOPUP](./_NOTIFYPOPUP.md)
* [_MESSAGEBOX](./_MESSAGEBOX.md)
* _INPUTBOX$
* _SELECTFOLDERDIALOG$
* [_COLORCHOOSERDIALOG](./_COLORCHOOSERDIALOG.md)
* _OPENFILEDIALOG$
* _SAVEFILEDIALOG$
