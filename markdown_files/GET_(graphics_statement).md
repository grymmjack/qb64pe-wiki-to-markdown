## GET (graphics statement)
---

### The GET statement is used in graphics to store a box area image of the screen into an INTEGER array.

#### SYNTAX

`GET [STEP] ( column1 , row1 )-[STEP]( column2 , row2 ), array ([ index ])[, offscreenColor ]`

#### PARAMETERS
* column and row [INTEGER](./INTEGER.md) coordinates for the box area must be on the screen except when using an offscreenColor .
* [INTEGER](./INTEGER.md) array sizes must be large enough (use width * height of the box area + 4) to hold the data or an error will occur.
* The array index offset is optional. If the offset is zero the brackets may be empty.
* The offscreenColor pixels will be returned as the designated color when part of an image is off screen.


#### DESCRIPTION
* The [STEP](./STEP.md) keyword can be used to for coordinates relative to the last graphic coordinates used.
* A graphic screen mode must be used. See the [SCREEN](./SCREEN.md) statement for graphic screen dimensions.
* QB64' [GET](./GET.md) statements can use coordinates off of the screen when an offscreenColor is designated. [STEP](./STEP.md) can be used for relative coordinates.
* The [GET](./GET.md) box coordinates are set just like a [LINE](./LINE.md) box statement is placed. You can use a box to find the correct [GET](./GET.md) area.
* Once [GET](./GET.md) has placed the pixel image data in the array, [PUT](./PUT.md) the image or [BSAVE](./BSAVE.md) it to a file.
* Once the image is stored in an array [PUT](./PUT.md) can be used to place the image on the screen.
* A [_SOURCE](./_SOURCE.md) handle can be set to [GET](./GET.md) image areas other than the ones on the current screen. Use [_DEST](./_DEST.md) to [PUT](./PUT.md) images there.
* To [GET](./GET.md) more than one image to the same array, designate an offset index that is not being used and is large enough to hold the data.
* The [INTEGER](./INTEGER.md) array size can be calculated as slightly larger than the box area width times the height. A closer estimate can be done by reading the array indices from [UBOUND](./UBOUND.md) to [LBOUND](./LBOUND.md) after a [GET](./GET.md) of a white box area. In QB64, a [LONG](./LONG.md) array can be used for large or full screen images.
* RGB color settings can be embedded at the beginning of the array for transferring custom colors. Specify an index for [GET](./GET.md) image data to be stored after any extra information added to the beginning of the array.
* In QB64, [_PUTIMAGE](./_PUTIMAGE.md) is recommended over [PUT](./PUT.md) as it can also do the [GET](./GET.md) operation directly from the image source without requiring an array.
* [PUT](./PUT.md) and [GET](./GET.md) file statements can also write and read image array data using [BINARY](./BINARY.md) files instead of using [BSAVE](./BSAVE.md) or [BLOAD](./BLOAD.md) .


#### EXAMPLES
##### Example 1: How to use GET and PUT to move a sprite with the arrow keys.
```vb
DEFINT A-Z
DIM BG(300), Box(300), SC(127) ' BG holds background images. Box holds the Box image.
SCREEN 13 ' graphic coordinate minimums are 0 to 319 column or 199 row maximums.
           ' set up screen background
 COLOR 4: LOCATE 10, 5: PRINT "Multikey Keyboard input routine"
 COLOR 10: LOCATE 12, 4: PRINT "Use the arrow keys to move the box."
 LOCATE 13, 4: PRINT "Note that you can press two or more"
 LOCATE 14, 4: PRINT "keys at once for diagonal movement!"
 COLOR 14: LOCATE 16, 4: PRINT " Also demonstrates how GET and PUT "
 LOCATE 17, 4: PRINT "are used to preserve the background."
 COLOR 11: LOCATE 20, 11: PRINT "Press [Esc] to quit"
 x = 150: y = 50: PX = x: PY = y ' actual box starting position

GET (x, y)-(x + 15, y + 15), BG  ' GET original BG at start box position
LINE (x, y)-(x + 15, y + 15), 9, BF ' the plain blue box to move
GET (x, y)-(x + 15, y + 15), Box   ' GET to Box Array

DO  'main loop
 t! = TIMER + .05
 DO         ' 1 Tick (1/18th second) keypress scancode read loop
   a$ = INKEY$ ' So the keyboard buffer won't get full
   code% = INP(&H60) ' Get keyboard scan code from port 96
   IF code% < 128 THEN SC(code%) = 1 ELSE SC(code% - 128) = 0 'true/false values to array
 LOOP UNTIL  TIMER > t!' loop until one tick has passed

 PX = x: PY = y  ' previous coordinates
 IF SC(75) = 1 THEN x = x - 5: IF x < 0 THEN x = 0
 IF SC(77) = 1 THEN x = x + 5: IF x > 304 THEN x = 304
 IF SC(72) = 1 THEN y = y - 5: IF y < 0 THEN y = 0
 IF SC(80) = 1 THEN y = y + 5: IF y > 184 THEN y = 184
 IF x <> PX OR y <> PY THEN             ' look for a changed coordinate value
   WAIT 936, 8: PUT(PX, PY), BG, PSET  ' replace previous BG first
   GET (x, y)-(x + 15, y + 15), BG      ' GET BG at new position before box is set
   PUT(x, y), Box, PSET                ' PUT box image at new position
 END IF
LOOP UNTIL SC(1) = 1 ' main loop until [Esc] key (scan code 1) is pressed
```
  
##### Example 2: How to GET graphics from an image other than the present screen using _SOURCE and _DESTination .
```vb
DIM img(20 * 20 + 4) AS INTEGER  'create img% array to hold 20 by 20 image data
a& = _NEWIMAGE(800, 600, 13)     'larger surface a& emulates screen 13 colors & resolution

SCREEN 13     'program screen 13

_DEST a&                         'set desination as the image page a&
CIRCLE (700, 300), 10, 10        'draw green circle on image page

_SOURCE a&                       'set source as image page a&
GET (690, 290)-(710, 310), img() 'GET a square screen area similar to a LINE Box.


_DEST 0                          'set destination as the program screen
PUT (100, 100), img()            'PUT the Top Left Corner of box area to pixel 100, 100
```
  


#### SEE ALSO
* [_PUTIMAGE](./_PUTIMAGE.md) , [_LOADIMAGE](./_LOADIMAGE.md) , [_SAVEIMAGE](./_SAVEIMAGE.md)
* [_MAPTRIANGLE](./_MAPTRIANGLE.md)
* [POINT](./POINT.md) , [PUT](./PUT.md) , [STEP](./STEP.md)
* [BSAVE](./BSAVE.md) , [BLOAD](./BLOAD.md)
* Scancodes , Creating Sprite Masks (for non-box shaped sprites)
* Bitmaps , [GET](./GET.md) and [PUT](./PUT.md) Demo
