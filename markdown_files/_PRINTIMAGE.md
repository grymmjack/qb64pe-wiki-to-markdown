# _PRINTIMAGE
> The _PRINTIMAGE statement prints a colored image on the printer, stretching it to full paper size first.

## SYNTAX
`_PRINTIMAGE imageHandle&`

## EXAMPLES
> Example 1: Shows how to transfer custom font text on screen pages to the printer in Windows. Change the font path for other OS's.

```vb
PageScale = 10
PageHeight = 297 * PageScale 'A4 paper size is 210 X 297 mm
PageWidth = 210 * PageScale
Page& = _NEWIMAGE(PageWidth, PageHeight, 32)
_DEST Page&: CLS , _RGB(255, 255, 255): _DEST 0  'make background white to save ink!
CursorPosY = 0

'example text to print
PointSize = 12
text$ = "The rain in Spain falls mainly on the plain."
GOSUB PrintText

PointSize = 50
text$ = "BUT!"
GOSUB PrintText

PointSize = 12
text$ = "In Hartford, Hereford, and Hampshire, hurricanes hardly happen."
GOSUB PrintText

INPUT "Preview (Y/N)?", i$                      'print preview of screen (optional)
IF UCASE$(i$) = "Y" THEN
 Prev& = _NEWIMAGE(600, 900, 32)               'print preview smaller image
 _PUTIMAGE , Page&, Prev&
 SCREEN Prev&
 DO: LOOP UNTIL INKEY$ <> ""
 SCREEN 0
END IF

INPUT "Print on printer (Y/N)?", i$             'print screen page on printer
IF UCASE$(i$) = "Y" THEN
 _PRINTIMAGE Page&
END IF

END

PrintText:
FontHeight = INT(PointSize * 0.3527 * PageScale)
FontHandle = _LOADFONT("c:\windows\fonts\times.ttf", FontHeight)
_DEST Page&
_FONT FontHandle
COLOR _RGB(255, 0, 0), _RGBA(0, 0, 0, 0)        'RED text on clear black background
_PRINTSTRING (0, CursorPosY), text$
_FONT 16                               'change to the QB64 default font to free it
_FREEFONT FontHandle
_DEST 0
CursorPosY = CursorPosY + FontHeight            'adjust print position down
RETURN
```

> Example 2: Printing an old SCREEN 12 ASCII table using a deeper sized page to prevent stretching by _PRINTIMAGE .

```vb
PageScale = 10
PageHeight = 297 * PageScale 'A4 paper size is 210 X 297 mm
PageWidth = 210 * PageScale
Page& = _NEWIMAGE(PageWidth, PageHeight, 32)
_DEST Page&: CLS , _RGB(255, 255, 255): _DEST 0  'make background white to save ink!
CursorPosY = 0

'example text to print
PointSize = 12
text$ = "The rain in Spain falls mainly on the plain."
GOSUB PrintText

PointSize = 50
text$ = "BUT!"
GOSUB PrintText

PointSize = 12
text$ = "In Hartford, Hereford, and Hampshire, hurricanes hardly happen."
GOSUB PrintText

INPUT "Preview (Y/N)?", i$                      'print preview of screen (optional)
IF UCASE$(i$) = "Y" THEN
 Prev& = _NEWIMAGE(600, 900, 32)               'print preview smaller image
 _PUTIMAGE , Page&, Prev&
 SCREEN Prev&
 DO: LOOP UNTIL INKEY$ <> ""
 SCREEN 0
END IF

INPUT "Print on printer (Y/N)?", i$             'print screen page on printer
IF UCASE$(i$) = "Y" THEN
 _PRINTIMAGE Page&
END IF

END

PrintText:
FontHeight = INT(PointSize * 0.3527 * PageScale)
FontHandle = _LOADFONT("c:\windows\fonts\times.ttf", FontHeight)
_DEST Page&
_FONT FontHandle
COLOR _RGB(255, 0, 0), _RGBA(0, 0, 0, 0)        'RED text on clear black background
_PRINTSTRING (0, CursorPosY), text$
_FONT 16                               'change to the QB64 default font to free it
_FREEFONT FontHandle
_DEST 0
CursorPosY = CursorPosY + FontHeight            'adjust print position down
RETURN
```


```vb
PageScale = 10
PageHeight = 297 * PageScale 'A4 paper size is 210 X 297 mm
PageWidth = 210 * PageScale
Page& = _NEWIMAGE(PageWidth, PageHeight, 32)
_DEST Page&: CLS , _RGB(255, 255, 255): _DEST 0  'make background white to save ink!
CursorPosY = 0

'example text to print
PointSize = 12
text$ = "The rain in Spain falls mainly on the plain."
GOSUB PrintText

PointSize = 50
text$ = "BUT!"
GOSUB PrintText

PointSize = 12
text$ = "In Hartford, Hereford, and Hampshire, hurricanes hardly happen."
GOSUB PrintText

INPUT "Preview (Y/N)?", i$                      'print preview of screen (optional)
IF UCASE$(i$) = "Y" THEN
 Prev& = _NEWIMAGE(600, 900, 32)               'print preview smaller image
 _PUTIMAGE , Page&, Prev&
 SCREEN Prev&
 DO: LOOP UNTIL INKEY$ <> ""
 SCREEN 0
END IF

INPUT "Print on printer (Y/N)?", i$             'print screen page on printer
IF UCASE$(i$) = "Y" THEN
 _PRINTIMAGE Page&
END IF

END

PrintText:
FontHeight = INT(PointSize * 0.3527 * PageScale)
FontHandle = _LOADFONT("c:\windows\fonts\times.ttf", FontHeight)
_DEST Page&
_FONT FontHandle
COLOR _RGB(255, 0, 0), _RGBA(0, 0, 0, 0)        'RED text on clear black background
_PRINTSTRING (0, CursorPosY), text$
_FONT 16                               'change to the QB64 default font to free it
_FREEFONT FontHandle
_DEST 0
CursorPosY = CursorPosY + FontHeight            'adjust print position down
RETURN
```

* [_LOADIMAGE](_LOADIMAGE.md) , [_NEWIMAGE](_NEWIMAGE.md)
* [_COPYIMAGE](_COPYIMAGE.md) , [_SAVEIMAGE](_SAVEIMAGE.md)
* [LPRINT](LPRINT.md)
* Windows Printer Settings

```vb
PageScale = 10
PageHeight = 297 * PageScale 'A4 paper size is 210 X 297 mm
PageWidth = 210 * PageScale
Page& = _NEWIMAGE(PageWidth, PageHeight, 32)
_DEST Page&: CLS , _RGB(255, 255, 255): _DEST 0  'make background white to save ink!
CursorPosY = 0

'example text to print
PointSize = 12
text$ = "The rain in Spain falls mainly on the plain."
GOSUB PrintText

PointSize = 50
text$ = "BUT!"
GOSUB PrintText

PointSize = 12
text$ = "In Hartford, Hereford, and Hampshire, hurricanes hardly happen."
GOSUB PrintText

INPUT "Preview (Y/N)?", i$                      'print preview of screen (optional)
IF UCASE$(i$) = "Y" THEN
 Prev& = _NEWIMAGE(600, 900, 32)               'print preview smaller image
 _PUTIMAGE , Page&, Prev&
 SCREEN Prev&
 DO: LOOP UNTIL INKEY$ <> ""
 SCREEN 0
END IF

INPUT "Print on printer (Y/N)?", i$             'print screen page on printer
IF UCASE$(i$) = "Y" THEN
 _PRINTIMAGE Page&
END IF

END

PrintText:
FontHeight = INT(PointSize * 0.3527 * PageScale)
FontHandle = _LOADFONT("c:\windows\fonts\times.ttf", FontHeight)
_DEST Page&
_FONT FontHandle
COLOR _RGB(255, 0, 0), _RGBA(0, 0, 0, 0)        'RED text on clear black background
_PRINTSTRING (0, CursorPosY), text$
_FONT 16                               'change to the QB64 default font to free it
_FREEFONT FontHandle
_DEST 0
CursorPosY = CursorPosY + FontHeight            'adjust print position down
RETURN
```



# SEE ALSO
* [_LOADIMAGE](_LOADIMAGE.md) , [_NEWIMAGE](_NEWIMAGE.md)
* [_COPYIMAGE](_COPYIMAGE.md) , [_SAVEIMAGE](_SAVEIMAGE.md)
* [LPRINT](LPRINT.md)
* Windows Printer Settings

