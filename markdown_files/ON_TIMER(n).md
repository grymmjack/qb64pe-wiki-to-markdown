## ON TIMER(n)
---

### The ON TIMER statement sets up a timed event to be repeated at specified intervals throughout a program when enabled.

#### SYNTAX

`ON TIMER ( seconds% ) GOSUB { lineLabel | lineNumber }`

#### DESCRIPTION


#### EXAMPLES
##### Example: Using a numbered TIMER to check the mouse button press status in QB64 .
```vb
DIM SHARED Button AS LONG    'share variable value with Sub

t1 = _FREETIMER              'get a timer number from _FREETIMER ONLY!
ON TIMER(t1, .05) MouseClick
TIMER(t1) ON

DO
 LOCATE 1, 1
 IF Button THEN
   PRINT "Mouse button"; Button; "is pressed.";
 ELSE PRINT SPACE$(70)
 END IF
 _DISPLAY
LOOP UNTIL INKEY$ = CHR$(27)
TIMER(t1) OFF
TIMER(t1) FREE 'release timer
END

SUB MouseClick
DO WHILE _MOUSEINPUT
 IF _MOUSEBUTTON(1) THEN
   COLOR 10: Button = 1
 ELSEIF _MOUSEBUTTON(2) THEN
   COLOR 12: Button = 2
 ELSE Button = 0
 END IF
LOOP
END SUB
```
  


#### SEE ALSO
* [_FREETIMER](./_FREETIMER.md) , [TIMER](./TIMER.md)
* [_DELAY](./_DELAY.md) , [_LIMIT](./_LIMIT.md)
* $CHECKING
