## KEY(n)
---

### KEY(n) assigns, enables, disables or suspends event trapping of a keypress by setting the flag ON , STOP or OFF .

#### SYNTAX

`KEY( number ) { ON | OFF | STOP }`

#### DESCRIPTION
* Predefined and user defined [KEY](./KEY.md) event number assignments to use with [KEY](./KEY.md)(n):


#### EXAMPLES
##### Example 1: How to trap the LEFT direction keys on both the dedicated cursor keypad and the numeric keypad.
```vb
KEY 15, CHR$(128) + CHR$(75) ' Assign trap for LEFT arrow key on the cursor keypad
ON KEY(15) GOSUB CursorPad
KEY(15) ON ' enable event trapping

ON KEY(12) GOSUB NumericPad ' Trap LEFT key on number pad
KEY(12) ON ' enable event trapping

DO
LOOP UNTIL UCASE$(INKEY$) = "Q" ' Idle loop for demo
SYSTEM

CursorPad:
PRINT "Pressed LEFT key on cursor keypad."
RETURN

NumericPad:
PRINT "Pressed LEFT key on numeric keypad."
RETURN
```
  
##### Example 2: Trapping the F5 keypress.
```vb
KEY(5) ON
ON KEY(5) GOSUB execute
PRINT "Press F5 (or ESC) to quit!)"
DO
LOOP UNTIL INKEY$ = CHR$(27) ' idle loop
SYSTEM
execute:
PRINT "You pressed the F5 key..."
SLEEP 1
PRINT "Press any key to continue..."
SLEEP
```
  


#### SEE ALSO
* [ON](./ON.md) [KEY](./KEY.md)(n) , [KEY](./KEY.md) n (softkeys)
* [_KEYHIT](./_KEYHIT.md) , [_KEYDOWN](./_KEYDOWN.md)
* Keyboard scancodes
