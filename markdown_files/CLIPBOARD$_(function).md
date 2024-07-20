## _CLIPBOARD$ (function)
---

### The _CLIPBOARD$ function returns the current Operating System's clipboard contents as a STRING .

#### SYNTAX

`result$ = _CLIPBOARD$`

#### DESCRIPTION
* Text returned can contain the entire contents of a copied file or web page or text from a previous _CLIPBOARD$ statement.
* The string returned can also contain formatting like CRLF ( CHR$ (13) + CHR$ (10)) end of line characters.
* The clipboard can be used to copy, paste and communicate between running programs.


#### EXAMPLES
```vb
'=================
'=== Program 1 ===
'=================

PRINT "Start Program2 to read your text entries! Empty entry quits!"
_CLIPBOARD$ = "Entry program started!" 'set clipboard initially

DO
   LINE INPUT "Enter some text to send to other program: ", text$
   IF text$ = "" THEN EXIT DO
   _CLIPBOARD$ = text$
LOOP

SYSTEM
```
  
```vb
'=================
'=== Program 2 ===
'=================

PRINT "Enter text in Program1 and this program will read it. Esc key quits!"

DO: _LIMIT 100
   text$ = CLIPBOARD$ 'function returns clipboard contents
   IF LEN(text$) THEN
       PRINT text$
       _CLIPBOARD$ = "" 'clear clipboard after a read
   END IF
LOOP UNTIL INKEY$ = CHR$(27)

END
```
  
```vb
'"ClippyBoard" program uses GetKeyState Win API to monitor a specific key combination.
'This demo will maximize the window and focus on program when Shift+A is pressed.

DECLARE DYNAMIC LIBRARY "user32"
   FUNCTION FindWindowA%& (BYVAL ClassName AS _OFFSET, WindowName$) 'find process handle by title
   FUNCTION GetKeyState% (BYVAL nVirtKey AS LONG) 'Windows virtual key presses
   FUNCTION ShowWindow& (BYVAL hwnd AS _OFFSET, BYVAL nCmdShow AS LONG) 'maximize process
   FUNCTION GetForegroundWindow%& 'find currently focused process handle
   FUNCTION SetForegroundWindow& (BYVAL hwnd AS _OFFSET) 'set foreground window process(focus)
END DECLARE

title$ = "Clippy Clipboard (Ctrl+Shift)" 'title of program window
_TITLE title$ 'set program title
hwnd%& = FindWindowA(0, title$ + CHR$(0)) 'find this program's process handle

SCREEN 13
_SCREENMOVE _MIDDLE

COLOR 10: PRINT
PRINT " Press Ctrl+Shift to see clipboard menu."

_DELAY 4
x& = ShowWindow&(hwnd%&, 2) 'minimize

DO: _LIMIT 30 'save CPU usage while waiting for key press

   IF GetKeyState(16) < 0 AND GetKeyState(17) < 0 THEN '<==== Shift+A
       FGwin%& = GetForegroundWindow%& 'get current process in focus
       y& = ShowWindow&(hwnd%&, 1) 'maximize minimized program

       IF FGwin%& <> hwnd%& THEN z& = SetForegroundWindow&(hwnd%&) 'set focus when necessary
       _DELAY 1
       GetKey
       x& = ShowWindow&(hwnd%&, 2) 'minimize after letter key entry
       COLOR 10: PRINT
       PRINT " Press Ctrl+Shift to see clipboard menu."
   END IF
LOOP


SUB GetKey
   CLS
   COLOR 12: PRINT: PRINT _CLIPBOARD$
   DO: LOOP UNTIL INKEY$ = ""
   _DELAY 1
   CLS
   COLOR 11: PRINT "Select a letter clipboard option:"
   PRINT
   PRINT "A = Address"
   PRINT "C = Cell phone"
   PRINT "E = Email"
   PRINT "F = First Name"
   PRINT "H = Home phone"
   PRINT "L = Last Name"
   PRINT "N = Name"
   PRINT "M = MAC address"
   PRINT "P = Password"
   PRINT "W = Work name"
   PRINT "X = QUIT!"
   PRINT "Z = Zip code"
   COLOR 14: PRINT
   PRINT "Another letter will skip or X = EXIT!"

   K$ = UCASE$(INPUT$(1))

   SELECT CASE K$ 'The following text should be your personal user info:
       CASE "A": _CLIPBOARD$ = "my address"
       CASE "C": _CLIPBOARD$ = "cell number"
       CASE "E": _CLIPBOARD$ = "myemail"
       CASE "F": _CLIPBOARD$ = "formal name"
       CASE "H": _CLIPBOARD$ = "home number"
       CASE "L": _CLIPBOARD$ = "lastname"
       CASE "M": _CLIPBOARD$ = "modempassword"
       CASE "N": _CLIPBOARD$ = "name"
       CASE "P": _CLIPBOARD$ = "password"
       CASE "X": END
       CASE "Z": _CLIPBOARD$ = "zipcode"
   END SELECT
   CLS
   PRINT
   PRINT
   COLOR 14: PRINT _CLIPBOARD$
   BEEP
   _DELAY 2
END SUB
```
  


#### SEE ALSO
* Featured in our "Keyword of the Day" series
* _CLIPBOARD$ (statement)
* [_CLIPBOARDIMAGE](./_CLIPBOARDIMAGE.md) (function) , [_CLIPBOARDIMAGE](./_CLIPBOARDIMAGE.md) (statement)
