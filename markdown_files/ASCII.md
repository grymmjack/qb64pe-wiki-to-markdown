## ASCII
---

### 

#### EXAMPLES
##### Example 1: Using arrow keys to move a text character. A change from a previous position tells program when to PRINT:
```vb
movey = 1: movex = 1 'text coordinates can never be 0
at$ = "@" 'text sprite could be almost any ASCII character
LOCATE movey, movex: PRINT at$;
DO
   px = movex: py = movey 'previous positions
   B$ = INKEY$
   IF B$ = CHR$(0) + CHR$(72) AND movey > 1 THEN movey = movey - 1 'rows 1 to 23 only
   IF B$ = CHR$(0) + CHR$(80) AND movey < 23 THEN movey = movey + 1
   IF B$ = CHR$(0) + CHR$(75) AND movex > 1 THEN movex = movex - 1 'columns 1 to 80 only
   IF B$ = CHR$(0) + CHR$(77) AND movex < 80 THEN movex = movex + 1

   IF px <> movex OR py <> movey THEN 'only changes when needed
       LOCATE py, px: PRINT SPACE$(1); 'erase old sprite
       LOCATE movey, movex: PRINT at$; 'show new position
   END IF
LOOP UNTIL B$ = CHR$(27) 'ESCape key exit
END
```
  
##### Example 2: Routine displays all keypress codes including Ctrl, Alt and Shift combinations. Ctrl + letter = control codes 1 to 26.
```vb
SCREEN 13
tmp$ = "   CHR$(###),\\,\          \       "
tmp2$ = "  CHR$(0) + CHR$(###) \           \"
COLOR 14: LOCATE 3, 3: PRINT "The code can tell what key is pressed"
COLOR 12: LOCATE 5, 14: PRINT CHR$(3); SPACE$(3);
COLOR 13: PRINT CHR$(5); SPACE$(3);
COLOR 12: PRINT CHR$(4); SPACE$(3);
COLOR 13: PRINT CHR$(6)
COLOR 10: LOCATE 7, 4: PRINT " Hit a key to find the ASCII Code"
COLOR 5: LOCATE 13, 1: PRINT " Codes below 33 are called control keys"
LOCATE 14, 1: PRINT " CHR$(0) + are 2 byte Extended key codes"
COLOR 13: LOCATE 16, 1: PRINT " Extended: Press Alt + numberpad: Enter"
LOCATE 18, 1: PRINT "  Try some Ctrl, Alt, or Shift Combo's"
COLOR 5: LOCATE 20, 1: PRINT " INKEY$ is used to detect the key entry"
COLOR 2: LOCATE 22, 15: PRINT CHR$(1); "       "; CHR$(2)
COLOR 4: LOCATE 24, 10: PRINT "To Quit hit the TAB key";

COLOR 9
DO
   DO: SLEEP: A$ = INKEY$: LOOP UNTIL A$ <> "" 'legal ASC read keys
   IF ASC(A$) > 0 THEN ' normal key codes
       code% = ASC(A$)
       SELECT CASE code%
           CASE 7: Key$ = "Beep"
           CASE 8: Key$ = "Backspace"
           CASE 9: Key$ = "Tab Key"
           CASE 10: Key$ = "Line Feed"
           CASE 12: Key$ = "Form Feed"
           CASE 13: Key$ = "Enter"
           CASE 27: Key$ = "Escape"
           CASE 32: Key$ = "Space Bar"
           CASE 48 TO 57: Key$ = "Number"
           CASE 65 TO 90: Key$ = "Uppercase"
           CASE 97 TO 122: Key$ = "Lowercase"
           CASE ELSE: Key$ = ""
       END SELECT
       SELECT CASE code% 'check for unprintable control combo characters
           CASE 10 TO 13: Kcode% = 32
           CASE ELSE: Kcode% = code%
       END SELECT
       COLOR 9: LOCATE 10, 5: PRINT USING tmp$; code%; CHR$(Kcode%); Key$;
   END IF
   IF ASC(A$) = 0 THEN 'two byte key codes
       code% = ASC(RIGHT$(A$, 1)) 'QBasic code
       'code% = ASC(A$, 2)        'QB64 code alternative
       SELECT CASE code%
           CASE 16 TO 50: Key$ = "Alt+ letter"
           CASE 72: Key$ = CHR$(24) + " Arrow"
           CASE 75: Key$ = CHR$(27) + " Arrow"
           CASE 77: Key$ = CHR$(26) + " Arrow"
           CASE 80: Key$ = CHR$(25) + " Arrow"
           CASE 83: Key$ = "Delete"
           CASE 59: Key$ = "F1"
           CASE 60: Key$ = "F2"
           CASE 61: Key$ = "F3"
           CASE 62: Key$ = "F4"
           CASE 63: Key$ = "F5"
           CASE 64: Key$ = "F6"
           CASE 65: Key$ = "F7"
           CASE 66: Key$ = "F8"
           CASE 67: Key$ = "F9"
           CASE 68: Key$ = "F10"
           CASE 71: Key$ = "Home"
           CASE 73: Key$ = "Page " + CHR$(24)
           CASE 79: Key$ = "End"
           CASE 81: Key$ = "Page " + CHR$(25)
           CASE 82: Key$ = "Insert"
           CASE 83: Key$ = "Delete"
           CASE 84 TO 93: Key$ = "Shift+ F"
           CASE 94 TO 103: Key$ = "Ctrl+ F"
           CASE 104 TO 113: Key$ = "Alt+ F"
           CASE 114 TO 119: Key$ = "Ctrl + pad"
           CASE 120 TO 129: Key$ = "Alt+ number"
           CASE 132: Key$ = "Ctrl + pad"
           CASE 133: Key$ = "F11"
           CASE 134: Key$ = "F12"
           CASE 135: Key$ = "Shift+ F11"
           CASE 136: Key$ = "Shift+ F12"
           CASE 137: Key$ = "Ctrl+ F11"
           CASE 138: Key$ = "Ctrl+ F12"
           CASE 139: Key$ = "Alt+ F11"
           CASE 140: Key$ = "Alt+ F12"
           CASE ELSE: Key$ = ""
       END SELECT
       LOCATE 10, 5: PRINT USING tmp2$; code%; Key$
   END IF
LOOP UNTIL A$ = CHR$(9)
SOUND 400, 4
SLEEP 3
SYSTEM
```
  
##### Explanation: The routine checks for a keypress and SLEEP guarantees that ASC will never read an empty string from INKEY$. When the keypress is determined to be two bytes ( ASC (A$) = 0) the second SELECT CASE routine is used. You can even display non-keyboard extended characters. Just press Alt + numberpad code, release and press enter.
##### ( Return to Table of Contents )


#### SEE ALSO
* [_KEYHIT](./_KEYHIT.md) , [_KEYDOWN](./_KEYDOWN.md)
* [_MAPUNICODE](./_MAPUNICODE.md) , [_MAPUNICODE](./_MAPUNICODE.md) (function)
* Code Pages
* [ASC](./ASC.md) , [ASC](./ASC.md) (function)
* MID$ , MID$ (function)
* [INSTR](./INSTR.md) , CHR$ , INKEY$
* LEFT$ , RIGHT$
* [PRINT](./PRINT.md) , [SCREEN](./SCREEN.md)
* MKI$ , MKL$ , MKS$ , MKD$ , _MK$
* [_PRINTSTRING](./_PRINTSTRING.md) , [_SCREENPRINT](./_SCREENPRINT.md)
* [_CONTROLCHR](./_CONTROLCHR.md)
* Scancodes , Unicode
* Text Using Graphics
