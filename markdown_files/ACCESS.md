# OPEN
> The OPEN statement is used to open a file or COM serial communications port for program input or output.

## SYNTAX
`OPEN fileName$ [ FOR mode ] [{ ACCESS |{ LOCK |SHARED}} [{READ|WRITE}] AS [#] fileNumber& [LEN = recordLength ]`

## PARAMETERS
* The fileName$ is a [STRING](STRING.md) variable or literal file name (path optional) in quotes.
* [FOR](FOR.md) mode can be: [APPEND](APPEND.md) (write to end), [BINARY](BINARY.md) (read/write), [INPUT](INPUT.md) (read), [OUTPUT](OUTPUT.md) (write new) or [RANDOM](RANDOM.md) (read/write).
* GW-BASIC's modeLetter$ is a [STRING](STRING.md) variable or the letter "A", "B", "I", "O" or "R" designating the [OPEN](OPEN.md) modes above.
* fileNumber& can be any positive [INTEGER](INTEGER.md) or [LONG](LONG.md) whole number value or an unused value determined by the [FREEFILE](FREEFILE.md) function.
* [LEN](LEN.md) = or recordLength is optional to denote the [RANDOM](RANDOM.md) file record byte length (default = 128) or sequential (default = 512) load buffer.


## DESCRIPTION
* QB64 can open as many files as your computer memory can handle. QBasic could only open about 15 at a time.
* QB64 will allocate 4 bytes of memory for every possible file number up to the highest number used in a program.
* mode defaults to [RANDOM](RANDOM.md) if the mode or [FOR](FOR.md) access statement is omitted. (see open modes described below)
* Only the fileName$ , fileNumber& and [LEN](LEN.md) = recordLength values can use variable values in the QBasic syntax.
* If [LEN](LEN.md) = is ommitted, sequential file record sizes default to 512 and [RANDOM](RANDOM.md) to 128 bytes in QBasic.
* fileName$ can be up to 255 characters with no limit on file name extension length in QB64 .
* Once a file or port is opened, it can be used in any program procedure using the assigned file number.
* The "SCRN:" device is supported in version 1.000 and up (see Example 3).
* Devices such as "KYBD:", "CONS:", "COMn" and "LPTn:" are not supported in QB64. .


## EXAMPLES
> Example 1: Function that displays errors and the number of errors in QBasic filenames. Returns 0 when filename is OK.

```vb
file$ = "Hello,~1.mp3"      'example call below
LOCATE 20, 30: errors% = CheckName%(file$): COLOR 14: PRINT "  Total Errors ="; errors%

FUNCTION CheckName% (Filename$)
 'NOTE: Function also displays filename errors so LOCATE on screen before call!
 DIM L AS INTEGER, DP AS INTEGER, XL AS INTEGER
 L = LEN(Filename$): DP = INSTR(Filename$, "."): IF DP THEN XL = L - DP 'extension
 IF L = 0 OR L > 12 OR DP > 9 OR XL > 3 THEN
   CheckName% = -1: COLOR 12: PRINT "Illegal format!"; : EXIT FUNCTION
 END IF
 FOR i% = 1 TO L      'check each filename character"
    code% = ASC(MID$(Filename$, i%, 1)): COLOR 10      ' see ASCII codes
    SELECT CASE code%       'check for errors and highlight in red
       'CASE 34, 42 TO 44, 47, 58 TO 63, 91 TO 93, 124: E% = E% + 1: COLOR 12 ' QBasic errors
       CASE 34, 42, 47, 58, 60, 62, 92, 124: E% = E% + 1: COLOR 12 ' QB64 errors
       CASE 46: dot% = dot% + 1: IF dot% > 1 THEN E% = E% + 1: COLOR 12
    END SELECT
    PRINT CHR$(code%);  'use LOCATE before FUNCTION call to place print
 NEXT
 CheckName% = E%
END FUNCTION
```

> Note: The QBasic character error list is commented out and the function will return invalid filenames under QB64.

```vb
file$ = "Hello,~1.mp3"      'example call below
LOCATE 20, 30: errors% = CheckName%(file$): COLOR 14: PRINT "  Total Errors ="; errors%

FUNCTION CheckName% (Filename$)
 'NOTE: Function also displays filename errors so LOCATE on screen before call!
 DIM L AS INTEGER, DP AS INTEGER, XL AS INTEGER
 L = LEN(Filename$): DP = INSTR(Filename$, "."): IF DP THEN XL = L - DP 'extension
 IF L = 0 OR L > 12 OR DP > 9 OR XL > 3 THEN
   CheckName% = -1: COLOR 12: PRINT "Illegal format!"; : EXIT FUNCTION
 END IF
 FOR i% = 1 TO L      'check each filename character"
    code% = ASC(MID$(Filename$, i%, 1)): COLOR 10      ' see ASCII codes
    SELECT CASE code%       'check for errors and highlight in red
       'CASE 34, 42 TO 44, 47, 58 TO 63, 91 TO 93, 124: E% = E% + 1: COLOR 12 ' QBasic errors
       CASE 34, 42, 47, 58, 60, 62, 92, 124: E% = E% + 1: COLOR 12 ' QB64 errors
       CASE 46: dot% = dot% + 1: IF dot% > 1 THEN E% = E% + 1: COLOR 12
    END SELECT
    PRINT CHR$(code%);  'use LOCATE before FUNCTION call to place print
 NEXT
 CheckName% = E%
END FUNCTION
```

> Example 2: When OPEN "SCRN:" FOR OUTPUT AS #f is used, PRINT #f will print the text to the screen instead of to a file:

```vb
file$ = "Hello,~1.mp3"      'example call below
LOCATE 20, 30: errors% = CheckName%(file$): COLOR 14: PRINT "  Total Errors ="; errors%

FUNCTION CheckName% (Filename$)
 'NOTE: Function also displays filename errors so LOCATE on screen before call!
 DIM L AS INTEGER, DP AS INTEGER, XL AS INTEGER
 L = LEN(Filename$): DP = INSTR(Filename$, "."): IF DP THEN XL = L - DP 'extension
 IF L = 0 OR L > 12 OR DP > 9 OR XL > 3 THEN
   CheckName% = -1: COLOR 12: PRINT "Illegal format!"; : EXIT FUNCTION
 END IF
 FOR i% = 1 TO L      'check each filename character"
    code% = ASC(MID$(Filename$, i%, 1)): COLOR 10      ' see ASCII codes
    SELECT CASE code%       'check for errors and highlight in red
       'CASE 34, 42 TO 44, 47, 58 TO 63, 91 TO 93, 124: E% = E% + 1: COLOR 12 ' QBasic errors
       CASE 34, 42, 47, 58, 60, 62, 92, 124: E% = E% + 1: COLOR 12 ' QB64 errors
       CASE 46: dot% = dot% + 1: IF dot% > 1 THEN E% = E% + 1: COLOR 12
    END SELECT
    PRINT CHR$(code%);  'use LOCATE before FUNCTION call to place print
 NEXT
 CheckName% = E%
END FUNCTION
```

> Example 3: Showcasing different file modes.

```vb
file$ = "Hello,~1.mp3"      'example call below
LOCATE 20, 30: errors% = CheckName%(file$): COLOR 14: PRINT "  Total Errors ="; errors%

FUNCTION CheckName% (Filename$)
 'NOTE: Function also displays filename errors so LOCATE on screen before call!
 DIM L AS INTEGER, DP AS INTEGER, XL AS INTEGER
 L = LEN(Filename$): DP = INSTR(Filename$, "."): IF DP THEN XL = L - DP 'extension
 IF L = 0 OR L > 12 OR DP > 9 OR XL > 3 THEN
   CheckName% = -1: COLOR 12: PRINT "Illegal format!"; : EXIT FUNCTION
 END IF
 FOR i% = 1 TO L      'check each filename character"
    code% = ASC(MID$(Filename$, i%, 1)): COLOR 10      ' see ASCII codes
    SELECT CASE code%       'check for errors and highlight in red
       'CASE 34, 42 TO 44, 47, 58 TO 63, 91 TO 93, 124: E% = E% + 1: COLOR 12 ' QBasic errors
       CASE 34, 42, 47, 58, 60, 62, 92, 124: E% = E% + 1: COLOR 12 ' QB64 errors
       CASE 46: dot% = dot% + 1: IF dot% > 1 THEN E% = E% + 1: COLOR 12
    END SELECT
    PRINT CHR$(code%);  'use LOCATE before FUNCTION call to place print
 NEXT
 CheckName% = E%
END FUNCTION
```


```vb
file$ = "Hello,~1.mp3"      'example call below
LOCATE 20, 30: errors% = CheckName%(file$): COLOR 14: PRINT "  Total Errors ="; errors%

FUNCTION CheckName% (Filename$)
 'NOTE: Function also displays filename errors so LOCATE on screen before call!
 DIM L AS INTEGER, DP AS INTEGER, XL AS INTEGER
 L = LEN(Filename$): DP = INSTR(Filename$, "."): IF DP THEN XL = L - DP 'extension
 IF L = 0 OR L > 12 OR DP > 9 OR XL > 3 THEN
   CheckName% = -1: COLOR 12: PRINT "Illegal format!"; : EXIT FUNCTION
 END IF
 FOR i% = 1 TO L      'check each filename character"
    code% = ASC(MID$(Filename$, i%, 1)): COLOR 10      ' see ASCII codes
    SELECT CASE code%       'check for errors and highlight in red
       'CASE 34, 42 TO 44, 47, 58 TO 63, 91 TO 93, 124: E% = E% + 1: COLOR 12 ' QBasic errors
       CASE 34, 42, 47, 58, 60, 62, 92, 124: E% = E% + 1: COLOR 12 ' QB64 errors
       CASE 46: dot% = dot% + 1: IF dot% > 1 THEN E% = E% + 1: COLOR 12
    END SELECT
    PRINT CHR$(code%);  'use LOCATE before FUNCTION call to place print
 NEXT
 CheckName% = E%
END FUNCTION
```

* [PRINT](PRINT.md) (file statement) , [INPUT](INPUT.md) (file statement)
* [GET](GET.md) , [PUT](PUT.md) , [WRITE](WRITE.md) (file statement)
* [INPUT](INPUT.md)$ , [LINE](LINE.md) [INPUT](INPUT.md) (file statement)
* [CLOSE](CLOSE.md) , [LOF](LOF.md) , [EOF](EOF.md) , [LOC](LOC.md)
* [SEEK](SEEK.md) , [SEEK](SEEK.md) (function)
* [OPEN](OPEN.md) [COM](COM.md) , [LEN](LEN.md) , [RESET](RESET.md)
* [FIELD](FIELD.md) , [TYPE](TYPE.md)
* [_FILEEXISTS](_FILEEXISTS.md) , [_DIREXISTS](_DIREXISTS.md)
* [_OPENCLIENT](_OPENCLIENT.md) , [_OPENHOST](_OPENHOST.md) , [_OPENCONNECTION](_OPENCONNECTION.md)
* [_SNDOPEN](_SNDOPEN.md) , [_LOADIMAGE](_LOADIMAGE.md)

```vb
file$ = "Hello,~1.mp3"      'example call below
LOCATE 20, 30: errors% = CheckName%(file$): COLOR 14: PRINT "  Total Errors ="; errors%

FUNCTION CheckName% (Filename$)
 'NOTE: Function also displays filename errors so LOCATE on screen before call!
 DIM L AS INTEGER, DP AS INTEGER, XL AS INTEGER
 L = LEN(Filename$): DP = INSTR(Filename$, "."): IF DP THEN XL = L - DP 'extension
 IF L = 0 OR L > 12 OR DP > 9 OR XL > 3 THEN
   CheckName% = -1: COLOR 12: PRINT "Illegal format!"; : EXIT FUNCTION
 END IF
 FOR i% = 1 TO L      'check each filename character"
    code% = ASC(MID$(Filename$, i%, 1)): COLOR 10      ' see ASCII codes
    SELECT CASE code%       'check for errors and highlight in red
       'CASE 34, 42 TO 44, 47, 58 TO 63, 91 TO 93, 124: E% = E% + 1: COLOR 12 ' QBasic errors
       CASE 34, 42, 47, 58, 60, 62, 92, 124: E% = E% + 1: COLOR 12 ' QB64 errors
       CASE 46: dot% = dot% + 1: IF dot% > 1 THEN E% = E% + 1: COLOR 12
    END SELECT
    PRINT CHR$(code%);  'use LOCATE before FUNCTION call to place print
 NEXT
 CheckName% = E%
END FUNCTION
```



# SEE ALSO
* [PRINT](PRINT.md) (file statement) , [INPUT](INPUT.md) (file statement)
* [GET](GET.md) , [PUT](PUT.md) , [WRITE](WRITE.md) (file statement)
* [INPUT](INPUT.md)$ , [LINE](LINE.md) [INPUT](INPUT.md) (file statement)
* [CLOSE](CLOSE.md) , [LOF](LOF.md) , [EOF](EOF.md) , [LOC](LOC.md)
* [SEEK](SEEK.md) , [SEEK](SEEK.md) (function)
* [OPEN](OPEN.md) [COM](COM.md) , [LEN](LEN.md) , [RESET](RESET.md)
* [FIELD](FIELD.md) , [TYPE](TYPE.md)
* [_FILEEXISTS](_FILEEXISTS.md) , [_DIREXISTS](_DIREXISTS.md)
* [_OPENCLIENT](_OPENCLIENT.md) , [_OPENHOST](_OPENHOST.md) , [_OPENCONNECTION](_OPENCONNECTION.md)
* [_SNDOPEN](_SNDOPEN.md) , [_LOADIMAGE](_LOADIMAGE.md)

