## SaveImage SUB
---

### 

#### EXAMPLES
```vb
'load a 32 bit .PNG file image
i& = _LOADIMAGE("source\peLogo.png", 32)
IF i& < -1 THEN
   'load success: get image's width/height
   w& = _WIDTH(i&): h& = _HEIGHT(i&)
   'TEST-1: directly save the loaded image as .BMP file "logo.bmp"
   SaveImage i&, "logo"
   'TEST-2: make a new 4:3 program SCREEN of the loaded image's width/height
   SCREEN _NEWIMAGE((4 * w&), (3 * h&), 32)
   'now tile-fill the screen with the loaded image
   FOR x& = 0 TO (4 * w&) STEP w&
       FOR y& = 0 TO (3 * h&) STEP h&
           _PUTIMAGE (x&, y&), i&
       NEXT y&
   NEXT x&
   'and then save the entire program screen as "screenshot.bmp"
   SaveImage 0, "screenshot"
ELSE
   'load failure: print error
   PRINT "Cannot find/load the given image."
END IF
END

SUB SaveImage (image AS LONG, filename AS STRING)
bytesperpixel& = _PIXELSIZE(image&)
IF bytesperpixel& = 0 THEN PRINT "Text modes unsupported!": END
IF bytesperpixel& = 1 THEN bpp& = 8 ELSE bpp& = 24
x& = _WIDTH(image&)
y& = _HEIGHT(image&)
b$ = "BM????QB64????" + MKL$(40) + MKL$(x&) + MKL$(y&) + MKI$(1) + MKI$(bpp&) + MKL$(0) + "????" + STRING$(16, 0) 'partial BMP header info(???? to be filled later)
IF bytesperpixel& = 1 THEN
   FOR c& = 0 TO 255 ' read BGR color settings from JPG image + 1 byte spacer(CHR$(0))
       cv& = _PALETTECOLOR(c&, image&) ' color attribute to read.
       b$ = b$ + CHR$(_BLUE32(cv&)) + CHR$(_GREEN32(cv&)) + CHR$(_RED32(cv&)) + CHR$(0) 'spacer byte
   NEXT
END IF
MID$(b$, 11, 4) = MKL$(LEN(b$)) ' image pixel data offset(BMP header)
lastsource& = _SOURCE
_SOURCE image&
IF ((x& * 3) MOD 4) THEN padder$ = STRING$(4 - ((x& * 3) MOD 4), 0)
FOR py& = y& - 1 TO 0 STEP -1 ' read JPG image pixel color data
   r$ = ""
   FOR px& = 0 TO x& - 1
       c& = POINT(px&, py&) 'POINT 32 bit values are large LONG values
       IF bytesperpixel& = 1 THEN r$ = r$ + CHR$(c&) ELSE r$ = r$ + LEFT$(MKL$(c&), 3)
   NEXT px&
   d$ = d$ + r$ + padder$
NEXT py&
_SOURCE lastsource&
MID$(b$, 35, 4) = MKL$(LEN(d$)) ' image size(BMP header)
b$ = b$ + d$ ' total file data bytes to create file
MID$(b$, 3, 4) = MKL$(LEN(b$)) ' size of data file(BMP header)
IF LCASE$(RIGHT$(filename$, 4)) <> ".bmp" THEN ext$ = ".bmp"
f& = FREEFILE
OPEN filename$ + ext$ FOR OUTPUT AS #f&: CLOSE #f& ' erases an existing file
OPEN filename$ + ext$ FOR BINARY AS #f&
PUT #f&, , b$
CLOSE #f&
END SUB
```
  
##### SUB Explanation: b$ and d$ assemble the entire string of data to create a bitmap file. Some of the bitmap header info is placed later using a MID$ to add final header numerical data converted to ASCII characters by MKI$ or MKL$ .
##### After the header, the RGB color settings are created using ASCII characters read backwards as Blue, Green, Red and CHR$(0) as a spacer. MKL$ places the byte values in reverse order too. Bitmaps and icons require that format. LEFT$ trims off the _ALPHA byte.
##### The actual image is read as pixel attributes from the image bottom to the top for proper formatting with zero padding when necessary.
##### Note: 32-bit images will be saved as 24-bit BMP files. All palette indexed images/modes will be saved as 256 color BMP files. Text modes cannot be saved.


#### SEE ALSO
* [_LOADIMAGE](./_LOADIMAGE.md) , [_ICON](./_ICON.md) , $EXEICON
* [SCREEN](./SCREEN.md)
* [TYPE](./TYPE.md) , MKI$ , MKL$
* Program ScreenShots (member [SUB](./SUB.md) program)
* ThirtyTwoBit [SUB](./SUB.md) (member [SUB](./SUB.md) captures selected area)
* ThirtyTwoBit MEM [SUB](./SUB.md) (Fast [SUB](./SUB.md) uses memory instead of [POINT](./POINT.md))
* SaveIcon32 (converts any image to icon)
* Bitmaps , Icons and Cursors
