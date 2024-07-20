## Boolean
---

### Boolean statements are evaluations that return true (-1) or false (0) values. This are for instance the Relational Operations , but also functions such as _FILEEXISTS , EOF , _SCREENEXISTS etc. return those values when checking for certain conditions. The results of those evaluations or function calls can be used in other mathematical or logical operations.

#### EXAMPLES
```vb
INPUT "Enter a year greater than 1583: ", annum$
Y = VAL(annum$)
leap1 = (Y MOD 4 = 0 AND Y MOD 100 <> 0) OR (Y MOD 400 = 0)
leap2 = (Y MOD 4 = 0) - (Y MOD 100 = 0) + (Y MOD 400 = 0)
PRINT "Year = "; annum$, "Leap1 = "; leap1, "Leap2 = "; leap2
```
  
```vb
Evaluation for year 2000
leap1 = (-1 AND 0) OR -1 = -1 'the AND evaluation is false(0), so the OR value is used
leap2 = (-1) - (-1) + (-1) = -1 + 1 + -1 = -1
Evaluation for year 1900
leap1 = (-1 AND 0) OR 0 = 0 OR 0 = 0
leap2 = (-1) - (-1) + (0) = -1 + 1 + 0 = 0
```
  
```vb
SCREEN 12
COLOR 7
LOCATE 11, 20: PRINT "Using Screen 12 here to be in 80 X 30 coordinates mode"
LOCATE 13, 6: PRINT "Simple Example of Alternative programming without IF-THEN-ELSE Statements"
LOCATE 15, 1: PRINT "Use the four Cursor keys to move the yellow cursor, text will not be disturbed"
LOCATE 17, 12: PRINT "When you END the program with the ESC key, cursor will disappear"

cordx% = 40
cordy% = 15

DO
   oldcordx% = cordx%
   oldcordy% = cordy%
   p% = SCREEN(cordy%, cordx%) 'get ASCII character code at present position
   COLOR 14: LOCATE cordy%, cordx%: PRINT CHR$(178); 'print cursor character to position

   WHILE cordx% = oldcordx% AND cordy% = oldcordy% AND k$ <> CHR$(27)
       k$ = INKEY$
       cordx% = cordx% + (k$ = (CHR$(0) + "K") AND cordx% > 1) + ABS(k$ = (CHR$(0) + "M") AND cordx% < 80)
       cordy% = cordy% + (k$ = (CHR$(0) + "H") AND cordy% > 1) + ABS(k$ = (CHR$(0) + "P") AND cordy% < 30)
   WEND

   COLOR 7: LOCATE oldcordy%, oldcordx%: PRINT CHR$(p%); 'replace overwritten screen characters

LOOP UNTIL k$ = CHR$(27)
```
  


#### SEE ALSO
* [IF](./IF.md)...[THEN](./THEN.md) , [SELECT](./SELECT.md) [CASE](./CASE.md)
* Binary , [ABS](./ABS.md) , [SGN](./SGN.md)
* [AND](./AND.md) , [OR](./OR.md) , [XOR](./XOR.md)
* Bitwise Operations
