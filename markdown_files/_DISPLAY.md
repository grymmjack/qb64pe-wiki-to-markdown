# _DISPLAY
> The _DISPLAY statement turns off the automatic display while only displaying the screen changes when called.

## SYNTAX
`_DISPLAY`

## DESCRIPTION
* [_DISPLAY](_DISPLAY.md) turns off the auto refresh screen default [_AUTODISPLAY](_AUTODISPLAY.md) behavior. Prevents screen flickering.
* Call [_DISPLAY](_DISPLAY.md) each time the screen graphics are to be displayed. Place call after the image has been changed.
* Re-enable automatic display refreshing by calling [_AUTODISPLAY](_AUTODISPLAY.md) . If it isn't re-enabled, things may not be displayed later.
* [_DISPLAY](_DISPLAY.md) tells QB64 to render all of the hardware [_PUTIMAGE](_PUTIMAGE.md) commands loaded into the buffer previously.
* The [_AUTODISPLAY](_AUTODISPLAY.md) (function) can be used to detect the current display behavior.
* QB64 can set the graphic rendering order of [_SOFTWARE](_SOFTWARE.md), [_HARDWARE](_HARDWARE.md), and [_GLRENDER](_GLRENDER.md) with [_DISPLAYORDER](_DISPLAYORDER.md) .


## EXAMPLES
> Example 1: Displaying a circle bouncing around the screen.

```vb
SCREEN 12
x = 21: y = 31 'start position
dx = 3: dy = 3 'number of pixel moves per loop
DO
   _LIMIT 100 ' set to 100 frames per second
   x = x + dx: y = y + dy
   IF x < 0 OR x > 640 THEN dx = -dx 'limit columns and reverse column direction each side
   IF y < 0 OR y > 480 THEN dy = -dy 'limit rows and reverse row direction top or bottom
   IF px <> x OR py <> y THEN FOR d = 1 TO 20: CIRCLE (px, py), d, 0: NEXT 'erase
   FOR c = 1 TO 20: CIRCLE (x, y), c, 6: NEXT 'draw new circle at new position
   px = x: py = y 'save older coordinates to erase older circle next loop
   _DISPLAY 'after new circle is set, show it
LOOP UNTIL INKEY$ = CHR$(27)
```

> Example 2: _DISPLAY must be used to render hardware images placed with _PUTIMAGE ( version 1.000 and up ).

```vb
SCREEN 12
x = 21: y = 31 'start position
dx = 3: dy = 3 'number of pixel moves per loop
DO
   _LIMIT 100 ' set to 100 frames per second
   x = x + dx: y = y + dy
   IF x < 0 OR x > 640 THEN dx = -dx 'limit columns and reverse column direction each side
   IF y < 0 OR y > 480 THEN dy = -dy 'limit rows and reverse row direction top or bottom
   IF px <> x OR py <> y THEN FOR d = 1 TO 20: CIRCLE (px, py), d, 0: NEXT 'erase
   FOR c = 1 TO 20: CIRCLE (x, y), c, 6: NEXT 'draw new circle at new position
   px = x: py = y 'save older coordinates to erase older circle next loop
   _DISPLAY 'after new circle is set, show it
LOOP UNTIL INKEY$ = CHR$(27)
```


```vb
SCREEN 12
x = 21: y = 31 'start position
dx = 3: dy = 3 'number of pixel moves per loop
DO
   _LIMIT 100 ' set to 100 frames per second
   x = x + dx: y = y + dy
   IF x < 0 OR x > 640 THEN dx = -dx 'limit columns and reverse column direction each side
   IF y < 0 OR y > 480 THEN dy = -dy 'limit rows and reverse row direction top or bottom
   IF px <> x OR py <> y THEN FOR d = 1 TO 20: CIRCLE (px, py), d, 0: NEXT 'erase
   FOR c = 1 TO 20: CIRCLE (x, y), c, 6: NEXT 'draw new circle at new position
   px = x: py = y 'save older coordinates to erase older circle next loop
   _DISPLAY 'after new circle is set, show it
LOOP UNTIL INKEY$ = CHR$(27)
```

* [_DISPLAY](_DISPLAY.md) (function)
* [_DISPLAYORDER](_DISPLAYORDER.md)
* [_AUTODISPLAY](_AUTODISPLAY.md) , [_AUTODISPLAY](_AUTODISPLAY.md) (function)
* [_PUTIMAGE](_PUTIMAGE.md)
* [PCOPY](PCOPY.md)

```vb
SCREEN 12
x = 21: y = 31 'start position
dx = 3: dy = 3 'number of pixel moves per loop
DO
   _LIMIT 100 ' set to 100 frames per second
   x = x + dx: y = y + dy
   IF x < 0 OR x > 640 THEN dx = -dx 'limit columns and reverse column direction each side
   IF y < 0 OR y > 480 THEN dy = -dy 'limit rows and reverse row direction top or bottom
   IF px <> x OR py <> y THEN FOR d = 1 TO 20: CIRCLE (px, py), d, 0: NEXT 'erase
   FOR c = 1 TO 20: CIRCLE (x, y), c, 6: NEXT 'draw new circle at new position
   px = x: py = y 'save older coordinates to erase older circle next loop
   _DISPLAY 'after new circle is set, show it
LOOP UNTIL INKEY$ = CHR$(27)
```



# SEE ALSO
* [_DISPLAY](_DISPLAY.md) (function)
* [_DISPLAYORDER](_DISPLAYORDER.md)
* [_AUTODISPLAY](_AUTODISPLAY.md) , [_AUTODISPLAY](_AUTODISPLAY.md) (function)
* [_PUTIMAGE](_PUTIMAGE.md)
* [PCOPY](PCOPY.md)

