# TIME$
> The TIME$ Function returns a STRING representation of the current computer time in a 24 hour format.

## SYNTAX
`PRINT "Present time = "; TIME$`

## DESCRIPTION
* Returns the present computer time in hh:mm:ss 24 hour format: "19:20:33"
* Uses 2 colon (:) separators between hours, minutes and seconds
* Hour values range from "00" to "23" starting from midnite.
* Minutes and seconds range from "00" to "59"
* Continuous TIME$ calls may lag if a QBasic program is minimized to the taskbar!


## EXAMPLES
> Example 1: A simple clock using DRAW with Turn Angle.

```vb
SCREEN 12
DO
   CLS
   t$ = TIME$: h = VAL(t$): m = VAL(MID$(t$, 4, 2)): s = VAL(MID$(t$, 7, 2))
   PRINT t$
   CIRCLE STEP(0, 0), 200, 8
   DRAW "c12ta" + STR$((h MOD 12) * -30) + "nu133"
   DRAW "c14ta" + STR$(m * -6) + "nu200"
   DRAW "c9ta" + STR$(s * -6) + "nu200"
   _DISPLAY
   _LIMIT 1
LOOP UNTIL INKEY$ = CHR$(27)
```

> Example 2: The following Function converts TIME$ to normal 12 hour AM-PM digital clock  format.

```vb
SCREEN 12
DO
   CLS
   t$ = TIME$: h = VAL(t$): m = VAL(MID$(t$, 4, 2)): s = VAL(MID$(t$, 7, 2))
   PRINT t$
   CIRCLE STEP(0, 0), 200, 8
   DRAW "c12ta" + STR$((h MOD 12) * -30) + "nu133"
   DRAW "c14ta" + STR$(m * -6) + "nu200"
   DRAW "c9ta" + STR$(s * -6) + "nu200"
   _DISPLAY
   _LIMIT 1
LOOP UNTIL INKEY$ = CHR$(27)
```


```vb
SCREEN 12
DO
   CLS
   t$ = TIME$: h = VAL(t$): m = VAL(MID$(t$, 4, 2)): s = VAL(MID$(t$, 7, 2))
   PRINT t$
   CIRCLE STEP(0, 0), 200, 8
   DRAW "c12ta" + STR$((h MOD 12) * -30) + "nu133"
   DRAW "c14ta" + STR$(m * -6) + "nu200"
   DRAW "c9ta" + STR$(s * -6) + "nu200"
   _DISPLAY
   _LIMIT 1
LOOP UNTIL INKEY$ = CHR$(27)
```

* [TIMER](TIMER.md) (function)
* DATE$ , [IF](IF.md)...[THEN](THEN.md)
* [VAL](VAL.md) , STR$ , MID$ (function)
* LEFT$ , RIGHT$

```vb
SCREEN 12
DO
   CLS
   t$ = TIME$: h = VAL(t$): m = VAL(MID$(t$, 4, 2)): s = VAL(MID$(t$, 7, 2))
   PRINT t$
   CIRCLE STEP(0, 0), 200, 8
   DRAW "c12ta" + STR$((h MOD 12) * -30) + "nu133"
   DRAW "c14ta" + STR$(m * -6) + "nu200"
   DRAW "c9ta" + STR$(s * -6) + "nu200"
   _DISPLAY
   _LIMIT 1
LOOP UNTIL INKEY$ = CHR$(27)
```



# SEE ALSO
* [TIMER](TIMER.md) (function)
* DATE$ , [IF](IF.md)...[THEN](THEN.md)
* [VAL](VAL.md) , STR$ , MID$ (function)
* LEFT$ , RIGHT$

