## Keyboard scancodes
---

### 

#### EXAMPLES
##### Example 1: An INP Function that retrieves multiple scancodes (allows 2 players and diagonal moves). Function includes it's own array.
```vb
CLS
x = 40: px = x
y = 20: py = y
xx = 41: pxx = xx
yy = 21: pyy = yy

DO ' program or game loop
 _LIMIT 20  ' Delay .05 'in QBasic
 COLOR 15
 LOCATE 8, 14: PRINT "W A S D": LOCATE 8, 52: PRINT "ARROW PAD"
 IF ScanKey%(17) THEN 'W key
   LOCATE 2, 15: PRINT " UP "
   IF y > 1 THEN y = y - 1
 ELSE LOCATE 2, 15: PRINT "----"
 END IF
 IF ScanKey%(31) THEN 'S key
   LOCATE 6, 15: PRINT "DOWN"
   IF y < 25 THEN y = y + 1
 ELSE LOCATE 6, 15: PRINT "----"
 END IF
 IF ScanKey%(30) THEN 'A key
   LOCATE 4, 12: PRINT "LEFT"
   IF x > 1 THEN x = x - 1
 ELSE LOCATE 4, 12: PRINT "----"
 END IF
 IF ScanKey%(32) THEN 'D key
   LOCATE 4, 18: PRINT "RIGHT"
   IF x < 80 THEN x = x + 1
 ELSE LOCATE 4, 18: PRINT "---- "
 END IF
 IF ScanKey%(72) THEN 'up arrow
   LOCATE 2, 55: PRINT " UP "
   IF yy > 1 THEN yy = yy - 1
 ELSE LOCATE 2, 55: PRINT "----"
 END IF
 IF ScanKey%(80) THEN 'down arrow
   LOCATE 6, 55: PRINT "DOWN"
   IF yy < 25 THEN yy = yy + 1
 ELSE LOCATE 6, 55: PRINT "----"
 END IF
 IF ScanKey%(75) THEN 'left arrow
   LOCATE 4, 52: PRINT "LEFT"
   IF xx > 1 THEN xx = xx - 1
 ELSE LOCATE 4, 52: PRINT "----"
 END IF
 IF ScanKey%(77) THEN 'right arrow
   LOCATE 4, 58: PRINT "RIGHT"
   IF xx < 80 THEN xx = xx + 1
 ELSE LOCATE 4, 58: PRINT "---- "
 END IF
 LOCATE py, px: PRINT SPACE$(1);  'erase sprite at previous position
 LOCATE pyy, pxx: PRINT SPACE$(1);
 COLOR 10: LOCATE y, x: PRINT CHR$(1); 'place sprite at new position
 COLOR 12: LOCATE yy, xx: PRINT CHR$(2);
 px = x: py = y: pxx = xx: pyy = yy
LOOP UNTIL ScanKey%(1)
zerocodes% = ScanKey%(0) 'reset all array values to zero for next part of program
END

FUNCTION ScanKey% (scancode%)
STATIC Ready%, keyflags%() 'retain values on procedure exit
IF NOT Ready% THEN REDIM keyflags%(0 TO 127): Ready% = -1 'create array on first use
i% = INP(&H60) 'read keyboard states
IF (i% AND 128) THEN keyflags%(i% XOR 128) = 0
IF (i% AND 128) = 0 THEN keyflags%(i%) = -1
K$ = INKEY$ 'clears the key from buffer to prevent beeps
ScanKey% = keyflags%(scancode%)
IF scancode% = 0 THEN Ready% = 0 'a zero scancode value clears all previous key presses with a REDIM
END FUNCTION

SUB Delay (dlay!) 'optional QBasic delay
start! = TIMER
DO WHILE start! + dlay! >= TIMER
 IF start! > TIMER THEN start! = start! - 86400
LOOP
END SUB
```
  
```vb
UP                                      UP

           ----  RIGHT                             LEFT  ----

              ----                                    ----

            W A S D                                ARROW PAD





                                     ☺
                                      ☻
```
  
##### Example 2: How to get Control, Alt and shift key entries from a user using PEEK in QB64 or QBasic:
```vb
DO
   _LIMIT 50
   DEF SEG = &H40  'set memory segment to read
   ShiftFlag = PEEK(&H17)  'read keyboard function keys
   DEF SEG
   IF ShiftFlag <> x THEN  'find key not previously read
       x = ShiftFlag  'read a new keypress
       IF (ShiftFlag AND 1) = 1 THEN PRINT "rightshift"
       IF (ShiftFlag AND 2) = 2 THEN PRINT "leftshift"
       IF (ShiftFlag AND 4) = 4 THEN PRINT "ctrl"
       IF (ShiftFlag AND 8) = 8 THEN PRINT "alt"
   END IF
   x$ = INKEY$ 'clear keyboard buffer to prevent beeping
   IF x$ <> "" THEN PRINT ASC(x$)  'read other keypress ASCII codes
LOOP UNTIL x$ = CHR$(27) 'Escape key exit
```
  
##### ( Return to Table of Contents )


#### SEE ALSO
* INKEY$ , ASCII , [ASC](./ASC.md) (function)
* [_KEYHIT](./_KEYHIT.md) , [_KEYDOWN](./_KEYDOWN.md) , [_KEYCLEAR](./_KEYCLEAR.md)
* [ON](./ON.md) [KEY](./KEY.md)(n) , [KEY](./KEY.md)(n) , [KEY](./KEY.md) ,
* [INP](./INP.md) , Scancodes (examples)
* Windows hot keys
* Mac keyboard Symbols
