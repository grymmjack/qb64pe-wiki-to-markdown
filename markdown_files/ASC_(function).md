## ASC (function)
---

### The ASC function returns the ASCII code number of a certain STRING text character.

#### SYNTAX

`code% = ASC ( text$ [, position% ])`

#### DESCRIPTION
* The text$ parameter must have a length of at least 1 byte or an error occurs.
* In QB64 only the optional position% parameter specifies the character in a string to be returned. Must be greater than 0.
* If the optional position% parameter is omitted, [ASC](./ASC.md) will return the ASCII code of the first character.
* ASCII code  values returned range from 0 to 255.
* In QB64 , the [ASC](./ASC.md) function reads string byte positions about 5 times faster than MID$ when parsing strings character wise. See MID$ Example 2 .


#### EXAMPLES
```vb
PRINT ASC("A")
PRINT ASC("Be a rockstar")
PRINT ASC("QB64 is not only COMPATIBLE, it can find any part of the string!", 18)
```
  
```vb
65
66
67
```
  
```vb
Explanation
The ASCII code for "A" is 65 and the ASCII code for "B" is 66,
ASCII code for "C" is 67 and the "C" is at position 18 in the string.
```
  
```vb
Q$ = CHR$(34) ' quote character
COLOR 10: LOCATE 5, 22: PRINT "Press some keys or combinations!"
COLOR 13: LOCATE 23, 30: PRINT "Escape key Quits"
DO
  DO: key$ = INKEY$: LOOP UNTIL key$ <> "" ' prevent ASC empty string read error
  code% = ASC(key$): COLOR 11: LOCATE 10, 10
  IF code% THEN    ' ASC returns any value greater than 0
   PRINT "CHR$(" + LTRIM$(STR$(code%)) + ")" + SPACE$(13):
   IF code% > 8 AND code% < 14 THEN code% = 32    ' unprintable control codes
   COLOR 14: LOCATE 10, 50: PRINT CHR$(code%) + SPACE$(13)
  ELSE: PRINT "CHR$(0) + CHR$(" + LTRIM$(STR$(ASC(key$, 2))) + ")"
   COLOR 14: LOCATE 10, 50: PRINT "CHR$(0) + " + Q$ + CHR$(ASC(key$, 2)) + Q$
  END IF
LOOP UNTIL code% = 27  '
```
  
```vb
Explanation
The keypress read loop checks that ASC will not read an empty
string. That would create a program error. Normal byte codes returned
are indicated by the IF statement when ASC returns a value.
Otherwise the routine will return the two byte ASCII code. The
extended keyboard keys (Home pad, Arrow pad and Number pad), Function
keys or Ctrl, Alt or Shift key combinations will return two byte codes.
Ctrl + letter combinations will return control character codes 1 to 26.
```
  


#### SEE ALSO
* Featured in our "Keyword of the Day" series
* [ASC](./ASC.md)
* [_KEYHIT](./_KEYHIT.md) , [_KEYDOWN](./_KEYDOWN.md)
* MID$ , MID$ (function)
* CHR$ , INKEY$
* [VAL](./VAL.md) , [STRING](./STRING.md)$
* ASCII , [_MAPUNICODE](./_MAPUNICODE.md)
* Scancodes
