## _DISPLAY (function)
---

### The _DISPLAY function returns the handle of the current image that is displayed on the screen.

#### SYNTAX

`currentImage& = _DISPLAY`

#### DESCRIPTION
* Returns the current image handle value that is being displayed. Returns 0 if in the default screen image.
* Not to be confused with the [_DISPLAY](./_DISPLAY.md) statement that displays the screen when not using [_AUTODISPLAY](./_AUTODISPLAY.md) .


#### EXAMPLES
##### Example: Creating a mouse cursor using a page number that you create in memory without setting up page flipping.
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
   PCOPY _DISPLAY, 100 'any page number as desination with the _DISPLAY function as source
   PSET (_MOUSEX, _MOUSEY), _RGB(0, 255, 0)
   DRAW "ND10F10L3F5L4H5L3"
   _DISPLAY 'statement shows image
   PCOPY 100, _DISPLAY 'with the function return as destination page
END SUB
```
  
##### Note: Works with the _DISPLAY function return as the other page. If mouse reads are not crucial, put the _MOUSEINPUT loop inside of the UpdateCursor SUB.


#### SEE ALSO
* [SCREEN](./SCREEN.md)
* [PCOPY](./PCOPY.md)
* [_DISPLAY](./_DISPLAY.md) (statement)
* [_AUTODISPLAY](./_AUTODISPLAY.md) (default mode)
* [_DISPLAYORDER](./_DISPLAYORDER.md) (statement)
