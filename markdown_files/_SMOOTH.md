# _FULLSCREEN
> The _FULLSCREEN statement attempts to make the program window fullscreen.

## SYNTAX
`_FULLSCREEN [ _STRETCH | _SQUAREPIXELS| _OFF ][, _SMOOTH ]`

## PARAMETERS
* [_STRETCH](_STRETCH.md) default first choice attempts to mimic QBasic's full screens if possible. [_FULLSCREEN](_FULLSCREEN.md) (function) returns 1.
* [_SQUAREPIXELS](_SQUAREPIXELS.md) alternate choice enlarges the pixels into squares on some monitors. [_FULLSCREEN](_FULLSCREEN.md) returns 2
* [_OFF](_OFF.md) turns [_FULLSCREEN](_FULLSCREEN.md) off after full screen has been enabled. [_FULLSCREEN](_FULLSCREEN.md) (function) returns 0.
* Second optional parameter [_SMOOTH](_SMOOTH.md) applies antialiasing to the stretched screen.


## DESCRIPTION
* Set the [SCREEN](SCREEN.md) mode and text [WIDTH](WIDTH.md) when necessary first. Otherwise there may be desktop view issues.
* [_FULLSCREEN](_FULLSCREEN.md) with no parameters chooses [_STRETCH](_STRETCH.md) or [_SQUAREPIXELS](_SQUAREPIXELS.md) (prioritizes [_STRETCH](_STRETCH.md) to mimic QBasic if possible)
* Check the fullscreen mode with the [_FULLSCREEN](_FULLSCREEN.md) function in your programs when a method is required.
* It is advisable to get input from the user to confirm that fullscreen was completed or there were possible monitor incompatibilities.
* If fullscreen is not confirmed with a [_FULLSCREEN](_FULLSCREEN.md) (function) return greater than 0 , then disable with [_FULLSCREEN](_FULLSCREEN.md) [_OFF](_OFF.md) .
* NOTE: [_FULLSCREEN](_FULLSCREEN.md) can also be affected by custom [_FONT](_FONT.md) size settings and make program screens too large.


## EXAMPLES
> Example 1: Setting the screen mode first prevents enlargement of the desktop before the program window is set:

```vb
SCREEN 12
_FULLSCREEN
IF _FULLSCREEN = 0 THEN _FULLSCREEN _OFF 'check that a full screen mode initialized

LINE (100, 100)-(500, 400), 13, BF
```

> Example 2: How fonts and _FULLSCREEN affect the program's window size.

```vb
SCREEN 12
_FULLSCREEN
IF _FULLSCREEN = 0 THEN _FULLSCREEN _OFF 'check that a full screen mode initialized

LINE (100, 100)-(500, 400), 13, BF
```

> Example 3: Testing all fullscreen methods.

```vb
SCREEN 12
_FULLSCREEN
IF _FULLSCREEN = 0 THEN _FULLSCREEN _OFF 'check that a full screen mode initialized

LINE (100, 100)-(500, 400), 13, BF
```


```vb
SCREEN 12
_FULLSCREEN
IF _FULLSCREEN = 0 THEN _FULLSCREEN _OFF 'check that a full screen mode initialized

LINE (100, 100)-(500, 400), 13, BF
```

* [_FULLSCREEN](_FULLSCREEN.md) (function)
* [_SMOOTH](_SMOOTH.md) (function)
* [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md)
* [_FONT](_FONT.md) , [SCREEN](SCREEN.md)
* [_SCREENIMAGE](_SCREENIMAGE.md)
* [_SCREENMOVE](_SCREENMOVE.md) , [_SCREENX](_SCREENX.md) , [_SCREENY](_SCREENY.md)

```vb
SCREEN 12
_FULLSCREEN
IF _FULLSCREEN = 0 THEN _FULLSCREEN _OFF 'check that a full screen mode initialized

LINE (100, 100)-(500, 400), 13, BF
```



# SEE ALSO
* [_FULLSCREEN](_FULLSCREEN.md) (function)
* [_SMOOTH](_SMOOTH.md) (function)
* [_ALLOWFULLSCREEN](_ALLOWFULLSCREEN.md)
* [_FONT](_FONT.md) , [SCREEN](SCREEN.md)
* [_SCREENIMAGE](_SCREENIMAGE.md)
* [_SCREENMOVE](_SCREENMOVE.md) , [_SCREENX](_SCREENX.md) , [_SCREENY](_SCREENY.md)

