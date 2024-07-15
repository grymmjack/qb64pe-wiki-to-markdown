# _MOUSEINPUT
> The _MOUSEINPUT function is used to monitor any new mouse positions, button presses or movements of the scroll wheel. Must be called before other mouse information becomes available.

## SYNTAX
`infoExists%% = _MOUSEINPUT`

## DESCRIPTION
* Returns -1 if new mouse information is available, otherwise it returns 0.
* Must be called before reading any of the other mouse functions. The function will not miss any mouse input even during an [INPUT](INPUT.md) entry.
* Use in a loop to monitor the mouse buttons, scroll wheel and coordinate positions.
* To clear all previous mouse data, use [_MOUSEINPUT](_MOUSEINPUT.md) in a loop until it returns 0.


## EXAMPLES
> Example 1: Mouse coordinate, click and scroll events are returned sequentially inside of a _MOUSEINPUT loop.

```vb
DO
 DO WHILE _MOUSEINPUT '      Check the mouse status
   PRINT _MOUSEX, _MOUSEY, _MOUSEBUTTON(1), _MOUSEWHEEL
 LOOP
LOOP UNTIL INKEY$ <> ""
```

> Example 2: How to use a _MOUSEINPUT loop to locate PSET positions on a screen using a right mouse button click.

```vb
DO
 DO WHILE _MOUSEINPUT '      Check the mouse status
   PRINT _MOUSEX, _MOUSEY, _MOUSEBUTTON(1), _MOUSEWHEEL
 LOOP
LOOP UNTIL INKEY$ <> ""
```

> Example 3: Clearing any mouse data read before or during an INPUT entry. Press "I" to enter input:

```vb
DO
 DO WHILE _MOUSEINPUT '      Check the mouse status
   PRINT _MOUSEX, _MOUSEY, _MOUSEBUTTON(1), _MOUSEWHEEL
 LOOP
LOOP UNTIL INKEY$ <> ""
```


```vb
DO
 DO WHILE _MOUSEINPUT '      Check the mouse status
   PRINT _MOUSEX, _MOUSEY, _MOUSEBUTTON(1), _MOUSEWHEEL
 LOOP
LOOP UNTIL INKEY$ <> ""
```

* Featured in our "Keyword of the Day" series
* [_MOUSEX](_MOUSEX.md) , [_MOUSEY](_MOUSEY.md) , [_MOUSEBUTTON](_MOUSEBUTTON.md) , [_MOUSEWHEEL](_MOUSEWHEEL.md)
* [_MOUSESHOW](_MOUSESHOW.md) , [_MOUSEHIDE](_MOUSEHIDE.md) , [_MOUSEMOVE](_MOUSEMOVE.md)
* Controller Devices

```vb
DO
 DO WHILE _MOUSEINPUT '      Check the mouse status
   PRINT _MOUSEX, _MOUSEY, _MOUSEBUTTON(1), _MOUSEWHEEL
 LOOP
LOOP UNTIL INKEY$ <> ""
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* [_MOUSEX](_MOUSEX.md) , [_MOUSEY](_MOUSEY.md) , [_MOUSEBUTTON](_MOUSEBUTTON.md) , [_MOUSEWHEEL](_MOUSEWHEEL.md)
* [_MOUSESHOW](_MOUSESHOW.md) , [_MOUSEHIDE](_MOUSEHIDE.md) , [_MOUSEMOVE](_MOUSEMOVE.md)
* Controller Devices

