# CIRCLE
> The CIRCLE statement is used in graphic SCREEN modes to create circles, arcs or ellipses.

## SYNTAX
`CIRCLE [[[STEP]]] ( column , row ), radius% , [ drawColor% ][, startRadian! , stopRadian! ] [, aspect! ]`

## PARAMETERS
* Can use [STEP](STEP.md) for relative coordinate moves from the previous graphic coordinates.
* Coordinates designate the center position of the circle. Can be partially drawn offscreen.
* radius% is an [INTEGER](INTEGER.md) value for half of the total circle diameter.
* drawColor% is any available color attribute in the [SCREEN](SCREEN.md) mode used.
* startRadian! and stopRadian! can be any [SINGLE](SINGLE.md) value from 0 to 2 * π to create partial circles or ellipses.
* aspect! [SINGLE](SINGLE.md) values of 0 to 1 affect the vertical height and values over 1 affect the horizontal width of an ellipse. Aspect = 1 is a normal circle.


## DESCRIPTION
* When using aspect! the startRadian! and stopRadian! commas must be included even if not used.
* Radians move in a counter clockwise direction from 0 to 2 * π. Zero and 2 * π are the same circle radian at 3 o'clock.
* Negative radian values can be used to draw lines from the end of an arc or partial ellipse to the circle center.
* Commas after the drawColor% parameter are not required when creating a normal circle. drawColor% can also be omitted to use the last color used in a draw statement.
* The graphic cursor is set to the center of the program window on program start for [STEP](STEP.md) relative coordinates.
* [CIRCLE](CIRCLE.md) can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only.


## EXAMPLES
> Example 1: Finding when the mouse is inside of a circular area:

```vb
SCREEN 12

r& = 200 'radius    change circle size and position here
cx& = 320 'center x horizontal
cy& = 240 'center y vertical

DO
 i = _MOUSEINPUT
 x& = _MOUSEX
 y& = _MOUSEY
 xy& = ((x& - cx&) ^ 2) + ((y& - cy&) ^ 2) 'Pythagorean theorem
 IF r& ^ 2 >= xy& THEN CIRCLE (cx&, cy&), r&, 10 ELSE CIRCLE (cx&, cy&), r&, 12
LOOP UNTIL INKEY$ = CHR$(27) 'escape key exit
```

> Example 2: Program illustrates how the CIRCLE command using a negative radian value can be used to create the hands of a clock.

```vb
SCREEN 12

r& = 200 'radius    change circle size and position here
cx& = 320 'center x horizontal
cy& = 240 'center y vertical

DO
 i = _MOUSEINPUT
 x& = _MOUSEX
 y& = _MOUSEY
 xy& = ((x& - cx&) ^ 2) + ((y& - cy&) ^ 2) 'Pythagorean theorem
 IF r& ^ 2 >= xy& THEN CIRCLE (cx&, cy&), r&, 10 ELSE CIRCLE (cx&, cy&), r&, 12
LOOP UNTIL INKEY$ = CHR$(27) 'escape key exit
```


```vb
SCREEN 12

r& = 200 'radius    change circle size and position here
cx& = 320 'center x horizontal
cy& = 240 'center y vertical

DO
 i = _MOUSEINPUT
 x& = _MOUSEX
 y& = _MOUSEY
 xy& = ((x& - cx&) ^ 2) + ((y& - cy&) ^ 2) 'Pythagorean theorem
 IF r& ^ 2 >= xy& THEN CIRCLE (cx&, cy&), r&, 10 ELSE CIRCLE (cx&, cy&), r&, 12
LOOP UNTIL INKEY$ = CHR$(27) 'escape key exit
```

* [STEP](STEP.md) , [DRAW](DRAW.md)
* [LINE](LINE.md) , [PSET](PSET.md) , [PRESET](PRESET.md)
* [SCREEN](SCREEN.md) , [SCREEN](SCREEN.md) (function)
* Alternative circle routine (member-contributed program)

```vb
SCREEN 12

r& = 200 'radius    change circle size and position here
cx& = 320 'center x horizontal
cy& = 240 'center y vertical

DO
 i = _MOUSEINPUT
 x& = _MOUSEX
 y& = _MOUSEY
 xy& = ((x& - cx&) ^ 2) + ((y& - cy&) ^ 2) 'Pythagorean theorem
 IF r& ^ 2 >= xy& THEN CIRCLE (cx&, cy&), r&, 10 ELSE CIRCLE (cx&, cy&), r&, 12
LOOP UNTIL INKEY$ = CHR$(27) 'escape key exit
```



# SEE ALSO
* [STEP](STEP.md) , [DRAW](DRAW.md)
* [LINE](LINE.md) , [PSET](PSET.md) , [PRESET](PRESET.md)
* [SCREEN](SCREEN.md) , [SCREEN](SCREEN.md) (function)
* Alternative circle routine (member-contributed program)

