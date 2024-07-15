# PCOPY
> The PCOPY statement copies one source screen page to a destination page in memory.

## SYNTAX
`PCOPY sourcePage% , destinationPage%`

## DESCRIPTION
* sourcePage% is an image page in video memory.
* destinationPage% is the video memory location to copy the source image to.
* The working page is set as 0. All drawing occurs there.
* The visible page is set as any page number that the [SCREEN](SCREEN.md) mode allows.
* The [_DISPLAY](_DISPLAY.md) (function) return can be used a page number reference in QB64 (See Example 1).
* The QB64 [_DISPLAY](_DISPLAY.md) statement can also be used to stop screen flicker without page flipping or [CLS](CLS.md) and is the recommended practice .


## EXAMPLES
> Example 1: Creating a mouse cursor using a page number that you create in memory without setting up page flipping.

```vb
SCREEN _NEWIMAGE(640, 480, 32) 'any graphics mode should work without setting up pages
_MOUSEHIDE
SetupCursor
PRINT "Hello World!"
DO: _LIMIT 30
 DO WHILE _MOUSEINPUT: LOOP 'main loop must contain _MOUSEINPUT
'       other program code
LOOP

SUB SetupCursor
ON TIMER(0.02) UpdateCursor
TIMER ON
END SUB

SUB UpdateCursor
PCOPY _DISPLAY, 100  'any page number as desination with the _DISPLAY function as source
PSET (_MOUSEX, _MOUSEY), _RGB(0, 255, 0)
DRAW "ND10F10L3F5L4H5L3"
_DISPLAY                  'statement shows image
PCOPY 100, _DISPLAY 'function return as destination page
END SUB
```

> Example 2: Bouncing balls

```vb
SCREEN _NEWIMAGE(640, 480, 32) 'any graphics mode should work without setting up pages
_MOUSEHIDE
SetupCursor
PRINT "Hello World!"
DO: _LIMIT 30
 DO WHILE _MOUSEINPUT: LOOP 'main loop must contain _MOUSEINPUT
'       other program code
LOOP

SUB SetupCursor
ON TIMER(0.02) UpdateCursor
TIMER ON
END SUB

SUB UpdateCursor
PCOPY _DISPLAY, 100  'any page number as desination with the _DISPLAY function as source
PSET (_MOUSEX, _MOUSEY), _RGB(0, 255, 0)
DRAW "ND10F10L3F5L4H5L3"
_DISPLAY                  'statement shows image
PCOPY 100, _DISPLAY 'function return as destination page
END SUB
```


```vb
SCREEN _NEWIMAGE(640, 480, 32) 'any graphics mode should work without setting up pages
_MOUSEHIDE
SetupCursor
PRINT "Hello World!"
DO: _LIMIT 30
 DO WHILE _MOUSEINPUT: LOOP 'main loop must contain _MOUSEINPUT
'       other program code
LOOP

SUB SetupCursor
ON TIMER(0.02) UpdateCursor
TIMER ON
END SUB

SUB UpdateCursor
PCOPY _DISPLAY, 100  'any page number as desination with the _DISPLAY function as source
PSET (_MOUSEX, _MOUSEY), _RGB(0, 255, 0)
DRAW "ND10F10L3F5L4H5L3"
_DISPLAY                  'statement shows image
PCOPY 100, _DISPLAY 'function return as destination page
END SUB
```

* [_DISPLAY](_DISPLAY.md)
* [SCREEN](SCREEN.md)

```vb
SCREEN _NEWIMAGE(640, 480, 32) 'any graphics mode should work without setting up pages
_MOUSEHIDE
SetupCursor
PRINT "Hello World!"
DO: _LIMIT 30
 DO WHILE _MOUSEINPUT: LOOP 'main loop must contain _MOUSEINPUT
'       other program code
LOOP

SUB SetupCursor
ON TIMER(0.02) UpdateCursor
TIMER ON
END SUB

SUB UpdateCursor
PCOPY _DISPLAY, 100  'any page number as desination with the _DISPLAY function as source
PSET (_MOUSEX, _MOUSEY), _RGB(0, 255, 0)
DRAW "ND10F10L3F5L4H5L3"
_DISPLAY                  'statement shows image
PCOPY 100, _DISPLAY 'function return as destination page
END SUB
```



# SEE ALSO
* [_DISPLAY](_DISPLAY.md)
* [SCREEN](SCREEN.md)

