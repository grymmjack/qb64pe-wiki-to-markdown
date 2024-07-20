## ON KEY(n)
---

### The ON KEY(n) statement defines a line number or label to go to (or a SUB to run) when a specified key is pressed.

#### SYNTAX

`ON KEY(n) GOSUB linelabel | linenumber`

#### DESCRIPTION
* Predefined and user defined [KEY](./KEY.md) event number assignments to use with [ON](./ON.md) [KEY](./KEY.md)(n):


#### EXAMPLES
##### Example 1: Using ON KEY with GOSUB to execute code.
```vb
KEY(1) ON
ON KEY(1) GOSUB trap
PRINT "Press F1 to quit!"
DO:LOOP          'never ending loop

trap:
PRINT "You pressed F1 like I told you to :)"
END
RETURN
```
  
##### Example 2: Setting multiple ON KEY statements to send different values to a SUB procedure.
```vb
FOR n = 1 TO 10
 KEY n, STR$(n)  '   assigns soft key as a numerical string
 ON KEY(n) Funct n  'designate SUB procedure and parameter value passed
 KEY(n) ON '         turns each key event monitor on
NEXT
KEY ON  'displays F1 to F10 soft key assignments at bottom of screen

DO
LOOP UNTIL INKEY$ = CHR$(27)
END

SUB Funct (num%)
CLS'                  clears the screen and refreshes bottom soft key list
PRINT "You pressed F"; LTRIM$(STR$(num%))
END SUB
```
  


#### SEE ALSO
* [KEY](./KEY.md)(n) , [KEY](./KEY.md) n
* [ON](./ON.md)...[GOSUB](./GOSUB.md) , Scancodes
* [_KEYHIT](./_KEYHIT.md) , [_KEYDOWN](./_KEYDOWN.md)
