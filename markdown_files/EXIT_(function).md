## _EXIT (function)
---

### The _EXIT function prevents the user from closing a program and indicates if a user has clicked the close button in the window title ( X button) or used CTRL + BREAK.

#### SYNTAX

`exitSignal% = _EXIT`

#### DESCRIPTION
* Once the [_EXIT](./_EXIT.md) function is used, the user can no longer manually exit the program until it is ended with [END](./END.md) or [SYSTEM](./SYSTEM.md) .
* [_EXIT](./_EXIT.md) returns any exit requests made after the initial call as:


#### EXAMPLES
##### Example 1: Using an ON TIMER check to read the _EXIT request return values.
```vb
q = _EXIT 'function read prevents any program exit at start of program
ON TIMER(5) GOSUB quit
TIMER ON
PRINT "  The Timer will check for exit request every 5 seconds."
PRINT "Click the X box and/or Ctrl - Break to see the _EXIT return!"
PRINT "                    Any Key Quits"
PRINT
DO: _LIMIT 30
   '                    ' simulated program loop
LOOP UNTIL INKEY$ <> ""
END

quit:
q = _EXIT
IF q THEN PRINT q;
SELECT CASE q
   CASE 1: PRINT "= X button was clicked"
   CASE 2: PRINT "= Ctrl + Break keypress"
   CASE 3: PRINT "= Both X and Ctrl + Break!"
END SELECT
RETURN
```
  
##### Example 2: Removing temporary files before closing a program upon a user's exit request.
```vb
x = _EXIT 'initial function call blocks a user exit
OPEN "t3mpdata.tmp" FOR APPEND AS #1
DO
   IF _EXIT THEN CLOSE: KILL "t3mpdata.tmp": _DELAY 1: SYSTEM
LOOP
```
  


#### SEE ALSO
* Featured in our "Keyword of the Day" series
* [SYSTEM](./SYSTEM.md)
* [END](./END.md)
* [EXIT](./EXIT.md)
