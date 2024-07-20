## ON STRIG(n)
---

### The ON STRIG(n) statement is an event procedure that directs program flow upon the press of a specified joystick button.

#### SYNTAX

`ON STRIG ( buttonFunction ) GOSUB { lineNumber | lineLabel }`

#### EXAMPLES
##### Example 1: Reading a STRIG event to do something in a GOSUB procedure.
```vb
ON STRIG(0) GOSUB 10
STRIG(0)ON

DO
   PRINT ".";
   _LIMIT 30
LOOP UNTIL INKEY$ <> ""
END

10
a$ = "[STRIG 0 EVENT]"
FOR x = 1 TO LEN(a$)
   PRINT MID$(a$, x, 1);
   _DELAY 0.02
NEXT
RETURN
```
  
##### Example 2: Displays any number of game pad or joystick device button presses.
```vb
FOR j = 1 TO 256
   FOR b = 1 TO 256
       ON STRIG((b - 1) * 4, j) JoyButton (j - 1) * 256 + b - 1
   NEXT
NEXT
STRIG ON

DO
   PRINT ".";
   _LIMIT 30
LOOP UNTIL INKEY$ <> ""
END

SUB JoyButton (js AS LONG)
PRINT "Joystick #"; js \ 256 + 1; "button #"; (js AND 255) + 1; "pressed!"
END SUB
```
  


#### SEE ALSO
* [STRIG](./STRIG.md) , [STICK](./STICK.md)
* [STRIG](./STRIG.md)(n)
* [_DEVICES](./_DEVICES.md) , _DEVICE$ , [_LASTBUTTON](./_LASTBUTTON.md)
* Single and Dual Stick Controllers
