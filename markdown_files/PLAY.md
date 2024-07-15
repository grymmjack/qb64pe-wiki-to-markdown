# PLAY
> PLAY is a statement that plays notes of sound through the sound card in QB64 using a command STRING .

## SYNTAX
`PLAY commandstring$`

## PARAMETERS
* The commandstring$ can be any literal or variable [STRING](STRING.md) consisting of the following commands: Command string values are not case sensitive and spacing is ignored. Use upper or lower case as desired.
	* Command string values are not case sensitive and spacing is ignored. Use upper or lower case as desired.
* Command string values are not case sensitive and spacing is ignored. Use upper or lower case as desired.


## EXAMPLES

```vb
PLAY "q0mll64"
DO
   FOR x = 1 TO 50
       a$ = a$ + "v" + LTRIM$(STR$(x)) + "n" + LTRIM$(STR$(x))
   NEXT
   FOR x = 50 TO 1 STEP -1
       a$ = a$ + "v" + LTRIM$(STR$(x)) + "n" + LTRIM$(STR$(x))
   NEXT
   PLAY a$
   a$ = ""
LOOP UNTIL INKEY$ <> ""
PLAY "v10l1c,l4egl2o5c,o4l4eg"
```

* [PLAY](PLAY.md) (function)
* [SOUND](SOUND.md) , [DRAW](DRAW.md)
* [_SNDRAW](_SNDRAW.md)
* [_SNDOPEN](_SNDOPEN.md)

```vb
PLAY "q0mll64"
DO
   FOR x = 1 TO 50
       a$ = a$ + "v" + LTRIM$(STR$(x)) + "n" + LTRIM$(STR$(x))
   NEXT
   FOR x = 50 TO 1 STEP -1
       a$ = a$ + "v" + LTRIM$(STR$(x)) + "n" + LTRIM$(STR$(x))
   NEXT
   PLAY a$
   a$ = ""
LOOP UNTIL INKEY$ <> ""
PLAY "v10l1c,l4egl2o5c,o4l4eg"
```



# SEE ALSO
* [PLAY](PLAY.md) (function)
* [SOUND](SOUND.md) , [DRAW](DRAW.md)
* [_SNDRAW](_SNDRAW.md)
* [_SNDOPEN](_SNDOPEN.md)

