# _MOUSEWHEEL
> The _MOUSEWHEEL function returns a positive or negative INTEGER value indicating mouse scroll events since the last read of _MOUSEINPUT .

## SYNTAX
`scrollAmount% = _MOUSEWHEEL`

## DESCRIPTION
* Returns -1 when scrolling up and 1 when scrolling down with 0 indicating no movement since last read.
* After an event has been read, the value resets to 0 automatically so cumulative position values must be added.
* If no movement on the wheel has occurred since the last [_MOUSEINPUT](_MOUSEINPUT.md) read, [_MOUSEWHEEL](_MOUSEWHEEL.md) returns 0.


## EXAMPLES

```vb
DO
   _LIMIT 50
   DO WHILE _MOUSEINPUT
       Scroll = Scroll + _MOUSEWHEEL
       LOCATE 10, 20: PRINT Scroll
   LOOP
LOOP UNTIL INKEY$ = CHR$(13) ' press Enter to quit
```

* Featured in our "Keyword of the Day" series
* [_MOUSEX](_MOUSEX.md) , [_MOUSEY](_MOUSEY.md) , [_MOUSEBUTTON](_MOUSEBUTTON.md)
* [_MOUSEINPUT](_MOUSEINPUT.md) , [_MOUSEMOVE](_MOUSEMOVE.md)
* [_MOUSESHOW](_MOUSESHOW.md) , [_MOUSEHIDE](_MOUSEHIDE.md)
* Controller Devices

```vb
DO
   _LIMIT 50
   DO WHILE _MOUSEINPUT
       Scroll = Scroll + _MOUSEWHEEL
       LOCATE 10, 20: PRINT Scroll
   LOOP
LOOP UNTIL INKEY$ = CHR$(13) ' press Enter to quit
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* [_MOUSEX](_MOUSEX.md) , [_MOUSEY](_MOUSEY.md) , [_MOUSEBUTTON](_MOUSEBUTTON.md)
* [_MOUSEINPUT](_MOUSEINPUT.md) , [_MOUSEMOVE](_MOUSEMOVE.md)
* [_MOUSESHOW](_MOUSESHOW.md) , [_MOUSEHIDE](_MOUSEHIDE.md)
* Controller Devices

