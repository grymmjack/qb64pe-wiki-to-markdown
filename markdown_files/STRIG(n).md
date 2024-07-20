## STRIG(n)
---

### The STRIG(n) statement controls event trapping for a particular joystick or game pad device button.

#### DESCRIPTION
* button function specifies the device's button function. Even functions record events while odd ones read the actual presses.
* QB64 can designate a button function and controller device number from 0 to 256.
* When no parameters are used QB64 enables, disables or suspends the reading of ALL button events.
* [ON](./ON.md) specifies that event trapping is turned on for the specified button.
* [OFF](./OFF.md) specifies that event trapping is turned off for the specified button.
* If [STOP](./STOP.md) is specified, event trapping is suspended for the specified button. Further joystick button events are remembered and trapped, in order, after the next [STRIG](./STRIG.md)(n) [ON](./ON.md) statement is used.


#### EXAMPLES
##### Example:
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
  


#### SEE ALSO
* [ON](./ON.md) [STRIG](./STRIG.md)(n)
* [STRIG](./STRIG.md) , [STICK](./STICK.md)
* Single and Dual Stick Controllers
