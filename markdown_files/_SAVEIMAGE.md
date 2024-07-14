


\_SAVEIMAGE - QB64 Phoenix Edition Wiki








# \_SAVEIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**\_SAVEIMAGE** saves the contents of an image or screen page to an image file.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


\_SAVEIMAGE *fileName$*[, *imageHandle&*][, *requirements$*]
  




## Parameters


* *fileName$* is literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") file name value.
* Optional *imageHandle&* is a [LONG](/qb64wiki/index.php/LONG "LONG") image handle or a valid screen page number.
* Optional *requirements$* [STRING](/qb64wiki/index.php/STRING "STRING") values can be:
	+ **PNG**: Saves the image as Portable Network Graphics format if no file extension is specified.
	+ **QOI**: Saves the image as Quite OK Image format if no file extension is specified.
	+ **BMP**: Saves the image as Windows Bitmap format if no file extension is specified.
	+ **TGA**: Saves the image as Truevision TARGA format if no file extension is specified.
	+ **JPG**: Saves the image as Joint Photographic Experts Group format if no file extension is specified.
	+ **HDR**: Saves the image as Radiance HDR format if no file extension is specified.


  




## Description


* *fileName$* extension name takes precedence over *requirements$*
* If no file extension is specified in *fileName$* and no format is specified in *requirements$*, then the PNG format is used by default.
* If *imageHandle&* is omitted then the image handle returned by [\_DISPLAY (function)](/qb64wiki/index.php/DISPLAY_(function) "DISPLAY (function)") is used.
* All attempts are made to ensure the image is saved in the best possible quality in 32-bit RGBA format. Alpha channel information is preserved wherever the format allows.
* SCREEN 0 (text mode) screen and "images" can also be saved. Text surfaces are internally rendered using the master QB64-PE VGA fonts before saving.


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.9.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.9.0")

**v3.9.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


Example 1
It's possible to use **\_SAVEIMAGE** with text screens.
This demo draws a Mandelbrot in [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 and then saves the screen as a .jpg image.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [CONST](/qb64wiki/index.php/CONST "CONST") X_MIN = -2! [CONST](/qb64wiki/index.php/CONST "CONST") X_MAX = 1! [CONST](/qb64wiki/index.php/CONST "CONST") Y_MIN = -1! [CONST](/qb64wiki/index.php/CONST "CONST") Y_MAX = 1! [CONST](/qb64wiki/index.php/CONST "CONST") MAX_ITER = 100 [CONST](/qb64wiki/index.php/CONST "CONST") PIX_CHAR = 48  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") 160, 100 [_FONT](/qb64wiki/index.php/FONT "FONT") 8  [DIM](/qb64wiki/index.php/DIM "DIM") w [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): w = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") [DIM](/qb64wiki/index.php/DIM "DIM") h [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): h = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") [DIM](/qb64wiki/index.php/DIM "DIM") maxX [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): maxX = w - 1 [DIM](/qb64wiki/index.php/DIM "DIM") maxY [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): maxY = h - 1  [DIM](/qb64wiki/index.php/DIM "DIM") y [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): [FOR](/qb64wiki/index.php/FOR "FOR") y = 0 [TO](/qb64wiki/index.php/TO "TO") maxY     [DIM](/qb64wiki/index.php/DIM "DIM") x [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") maxX         [DIM](/qb64wiki/index.php/DIM "DIM") cx [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): cx = X_MIN + (x / w) * (X_MAX - X_MIN)         [DIM](/qb64wiki/index.php/DIM "DIM") cy [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): cy = Y_MIN + (y / h) * (Y_MAX - Y_MIN)          [DIM](/qb64wiki/index.php/DIM "DIM") zx [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): zx = 0         [DIM](/qb64wiki/index.php/DIM "DIM") zy [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): zy = 0         [DIM](/qb64wiki/index.php/DIM "DIM") i [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): i = 0          [DO UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") zx * zx + zy * zy >= 4 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") i >= MAX_ITER             [DIM](/qb64wiki/index.php/DIM "DIM") temp [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): temp = zx * zx - zy * zy + cx             zy = 2 * zx * zy + cy             zx = temp             i = i + 1         [LOOP](/qb64wiki/index.php/LOOP "LOOP")          [COLOR](/qb64wiki/index.php/COLOR "COLOR") i [MOD](/qb64wiki/index.php/MOD "MOD") 16          [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (x + 1, y + 1), [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(PIX_CHAR)     [NEXT](/qb64wiki/index.php/NEXT "NEXT") x [NEXT](/qb64wiki/index.php/NEXT "NEXT") y  _SAVEIMAGE "TextMandelbrot!.jpg"  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




---


Example 2
Saving a graphics image to a .png file. This is much like example one. However, it renders the graphics to an 8-bit offscreen image and then passes the image handle to **\_SAVEIMAGE**.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [CONST](/qb64wiki/index.php/CONST "CONST") X_MIN = -2! [CONST](/qb64wiki/index.php/CONST "CONST") X_MAX = 1! [CONST](/qb64wiki/index.php/CONST "CONST") Y_MIN = -1! [CONST](/qb64wiki/index.php/CONST "CONST") Y_MAX = 1! [CONST](/qb64wiki/index.php/CONST "CONST") MAX_ITER = 100  [DIM](/qb64wiki/index.php/DIM "DIM") img [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): img = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640 * 2, 400 * 2, 256) [_DEST](/qb64wiki/index.php/DEST "DEST") img  [DIM](/qb64wiki/index.php/DIM "DIM") w [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): w = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") [DIM](/qb64wiki/index.php/DIM "DIM") h [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): h = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") [DIM](/qb64wiki/index.php/DIM "DIM") maxX [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): maxX = w - 1 [DIM](/qb64wiki/index.php/DIM "DIM") maxY [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): maxY = h - 1  [DIM](/qb64wiki/index.php/DIM "DIM") y [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): [FOR](/qb64wiki/index.php/FOR "FOR") y = 0 [TO](/qb64wiki/index.php/TO "TO") maxY     [DIM](/qb64wiki/index.php/DIM "DIM") x [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") maxX         [DIM](/qb64wiki/index.php/DIM "DIM") cx [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): cx = X_MIN + (x / maxX) * (X_MAX - X_MIN)         [DIM](/qb64wiki/index.php/DIM "DIM") cy [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): cy = Y_MIN + (y / maxY) * (Y_MAX - Y_MIN)          [DIM](/qb64wiki/index.php/DIM "DIM") zx [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): zx = 0         [DIM](/qb64wiki/index.php/DIM "DIM") zy [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): zy = 0         [DIM](/qb64wiki/index.php/DIM "DIM") i [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): i = 0          [DO UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") zx * zx + zy * zy >= 4 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") i >= MAX_ITER             [DIM](/qb64wiki/index.php/DIM "DIM") temp [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): temp = zx * zx - zy * zy + cx             zy = 2 * zx * zy + cy             zx = temp             i = i + 1         [LOOP](/qb64wiki/index.php/LOOP "LOOP")          [PSET](/qb64wiki/index.php/PSET "PSET") (x, y), (i [MOD](/qb64wiki/index.php/MOD "MOD") 16) * 16 + (i [MOD](/qb64wiki/index.php/MOD "MOD") 8)     [NEXT](/qb64wiki/index.php/NEXT "NEXT") x [NEXT](/qb64wiki/index.php/NEXT "NEXT") y  _SAVEIMAGE "Mandelbrot", img  [_DEST](/qb64wiki/index.php/DEST "DEST") 0 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Saved image."  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2749)
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_ICON](/qb64wiki/index.php/ICON "ICON"), [$EXEICON](/qb64wiki/index.php/$EXEICON "$EXEICON")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")
* [TYPE](/qb64wiki/index.php/TYPE "TYPE"), [MKI$](/qb64wiki/index.php/MKI$ "MKI$"), [MKL$](/qb64wiki/index.php/MKL$ "MKL$")
* [Program ScreenShots](/qb64wiki/index.php/Program_ScreenShots "Program ScreenShots")
* [ThirtyTwoBit SUB](/qb64wiki/index.php/ThirtyTwoBit_SUB "ThirtyTwoBit SUB")
* [ThirtyTwoBit MEM SUB](/qb64wiki/index.php/ThirtyTwoBit_MEM_SUB "ThirtyTwoBit MEM SUB")
* [SaveIcon32](/qb64wiki/index.php/SaveIcon32 "SaveIcon32")
* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps"), [Icons and Cursors](/qb64wiki/index.php/Icons_and_Cursors "Icons and Cursors")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")






Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SAVEIMAGE&oldid=8953>"




## Navigation menu








### Search





















