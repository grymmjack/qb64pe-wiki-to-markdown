


\_PUTIMAGE - QB64 Phoenix Edition Wiki








# \_PUTIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
\_PUTIMAGE puts an area of a source image to an area of a destination image in one operation, like [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") and [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)").


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Sample usage](#Sample_usage) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) 	+ [4.1 More examples](#More_examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_PUTIMAGE [STEP] [(*dx1*, *dy1*)-[STEP][(*dx2*, *dy2*)[, *sourceHandle&*][, *destHandle&*][, ][STEP][(*sx1*, *sy1*)[-STEP][(*sx2*, *sy2*)[, *\_SMOOTH*]
### Sample usage


\_PUTIMAGE 'full source image to fit full destination area after [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") and [\_DEST](/qb64wiki/index.php/DEST "DEST") are set
\_PUTIMAGE , *sourceHandle&*, *destHandle&* 'size full source to fit full destination area
\_PUTIMAGE (*dx1*, *dy1*), *sourceHandle&*, *destHandle&* 'full source to top-left corner destination position
\_PUTIMAGE (*dx1*, *dy1*)-(*dx2*, *dy2*), *sourceHandle&*, *destHandle&* 'size full source to destination coordinate area
\_PUTIMAGE (*dx1*, *dy1*), *sourceHandle&*, *destHandle&*, (*sx1*, *sy1*)-(*sx2*, *sy2*) 'portion of source to the top-left corner of the destination page
\_PUTIMAGE , *sourceHandle&*, *destHandle&*, (*sx1*, *sy1*)-(*sx2*, *sy2*) 'portion of source to full destination area
\_PUTIMAGE (*dx1*, *dy1*)-(*dx2*, *dy2*), *sourceHandle&*, *destHandle&*,(*sx1*, *sy1*) 'right side of source from top-left corner to destination
  




Note: The top-left corner position designates the leftmost and topmost portion of the image to use.
  




## Parameters


* Relative coordinates to a previous graphical object can be designated using [STEP](/qb64wiki/index.php/STEP "STEP") as opposed to literal surface coordinates (version **1.000** and up).
* Coordinates *dx* and *dy* map the box area of the [destination](/qb64wiki/index.php/DEST "DEST") area to use. When omitted the entire desination area is used. If only one coordinate is used, the source is placed with its original dimensions. Coordinates can be set to flip or resize the image.
	+ *dx1* = the column coordinate at which the insertion of the source will begin (leftmost); when larger than *dx2*, reverses image.
	+ *dy1* = the row coordinate at which the insertion of the source will begin (topmost); when larger than *dy2*, inverts image.
	+ *dx2* = the column coordinate at which the insertion of the source will end (rightmost); further apart, widens image.
	+ *dy2* = the row coordinate at which the insertion of the source will end (bottommost); closer together, shrinks image
* *sourceHandle&* = the [LONG](/qb64wiki/index.php/LONG "LONG") handle of the [source](/qb64wiki/index.php/SOURCE "SOURCE") image created with [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") or [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE").
* *destHandle&* = the [LONG](/qb64wiki/index.php/LONG "LONG") handle of the [destination](/qb64wiki/index.php/DEST "DEST") image may be created with [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") or [destination](/qb64wiki/index.php/DEST "DEST") 0.
* Coordinates *sx* and *sy* [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") the box area of the [source](/qb64wiki/index.php/SOURCE "SOURCE") image to transfer to the [destination](/qb64wiki/index.php/DEST "DEST") image, page or [screen](/qb64wiki/index.php/SCREEN "SCREEN"):
	+ *sx1* = the column coordinate of the left-most pixel to include of the source. When omitted, the entire image is used
	+ *sy1* = the row coordinate of the upper-most pixel to include of the source. When omitted, the entire image is used
	+ *sx2* = the column coordinate of the right-most pixel to include of the source. Can be omitted to get rest of image.
	+ *sy2* = the row coordinate of the bottom-most pixel to include of the source. Can be omitted to get rest of image.
* *\_SMOOTH* applies linear filtering (**version 1.000 and up**).


**Note: The [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)") options PSET, PRESET, AND, OR and XOR are not available with \_PUTIMAGE. QB64 can use [transparency](/qb64wiki/index.php/ALPHA "ALPHA") of colors to achieve the same results.**
  




## Description


* \_PUTIMAGE can be used without any handle parameters if the [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") and/or [\_DEST](/qb64wiki/index.php/DEST "DEST") are already defined.
* If the area of the source is bigger or smaller than the area of the destination then the image is adjusted to fit that area.
* Supports 32 bit alpha blending, color key transparency, true type fonts, stretching, mirroring/flipping, and a variety of graphics file formats including gif, png, bmp & jpg. **32 bit screen surface backgrounds (black) have zero [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") and are transparent when placed over other surfaces.** Use [CLS](/qb64wiki/index.php/CLS "CLS") or [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") to make a new surface background [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") 255 or opaque.
* All graphical surfaces, including screen pages, can be acted upon in the same manner, and are referred to as "images".
* **Hardware images** (created using mode **33** via [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") or [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")) can be used as the source or destination.
* [Handles](/qb64wiki/index.php/Handle "Handle") are used to identify graphical surfaces. Positive values are used to refer to screen pages. -1 (negative one) indicates an invalid surface. It is recommended to store image handles in [LONG](/qb64wiki/index.php/LONG "LONG") variables. Passing an invalid handle generates an ["Invalid handle"](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error.
* When handles are not passed (or cannot be passed) to subs/functions then the default destination image or source image is referenced. These are set to the active page when the SCREEN statement is called, but can be changed to any image. So it is possible to read from one image using [POINT](/qb64wiki/index.php/POINT "POINT") and write to a different one with [PSET](/qb64wiki/index.php/PSET "PSET").
* **[PRINTed](/qb64wiki/index.php/PRINT "PRINT") text cannot be transferred and positioned accurately.** Use [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") for graphical text or font placement.
* **Images are not deallocated when the [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") they are created in ends. Free them with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE").**
* **It is important to free discarded or unused images with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") to prevent CPU memory overflow errors.**


  




## Examples


*Example 1:*





| ```  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13  a& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 200, 13) ' creates a 640 * 200 image with the [LONG](/qb64wiki/index.php/LONG "LONG") handle a&  [_DEST](/qb64wiki/index.php/DEST "DEST") a& ' makes image a& the default drawing output.  [LINE](/qb64wiki/index.php/LINE "LINE") (10, 10)-(100, 100), 12, BF ' draws a filled box (BF) into destination  _PUTIMAGE (0, 0)-(320, 200), a&, 0, (0, 0)-(320, 200)  ``` |
| --- |


*Explanation:*
1) A graphics mode is set by using [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 which can use up to 256 colors.
2) A new image is created that is 640 X 200 and uses the palette compatible with SCREEN 13 (256 colors).
3) [\_DEST](/qb64wiki/index.php/DEST "DEST") a& makes the image with handle 'a&' the default image to draw on instead of the screen (which is [\_DEST](/qb64wiki/index.php/DEST "DEST") 0).
4) Next a filled box (BF) is drawn from 10, 10 to 100, 100 with red color (12) to the destination image (set by [\_DEST](/qb64wiki/index.php/DEST "DEST") a&)
5) Now we put the image from 0, 0 to 320, 200 from the image with the handle 'a&' to the screen (always handle 0) and puts this image into the coordinates 0, 0 to 320, 200. If we want to stretch the image we can alter these coordinates.
**Note:** All arguments are optional. If you want to simply put the whole image of the source to the whole image of the destination then you omit the area (x, y)-(x2, y2) on both sides, the last line of the example can be replaced by \_PUTIMAGE , a&, 0 which indeed will stretch the image since image a& is bigger than the screen (the screen is 320 \* 200 and a& is 640 \* 200)
  

*Example 2:* You don't need to do anything special to use a .PNG image with alpha/transparency. Here's a simple example:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) [CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 255, 0) i = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")(**"QB64.PNG"**) 'any 32 bit image (ie. with alpha channel) _PUTIMAGE (0, 0), i ' places image at upper left corner of window w/o stretching it   ``` |
| --- |


*Explanation:* When QB64 loads a 256 color .PNG file containing a transparent color, that color will be treated as transparent when \_PUTIMAGE is used to put it onto another image. So actually, you can use a 256-color .PNG file containing transparency information in a 256 color screen mode in QB64.
  

*Example 3:* Flipping and enlarging an image with \_PUTIMAGE by swapping or increasing the desination coordinates.





| ``` [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG") A-Z dest_handle = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") dest_handle  '32 bit Screen 12 dimensions source_handle = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")(**"QB64.PNG"**, 32) 'any 32 bit image (ie. with alpha channel) dx1 = 0: dy1 = 0 dx2 = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(source_handle) - 1: dy2 = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(source_handle) - 1 'image dimensions - 1 [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 29, 33: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press any Key!"; 'normal image coordinate values based on the dimensions of the image: _PUTIMAGE (dx1, dy1)-(dx2, dy2), source_handle, dest_handle [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 34: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Normal layout" [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 24, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_PUTIMAGE (dx1, dy1)-(dx2, dy2), source_handle, dest_handle" K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) 'to flip the image on the x axis, swap the dx coordinate values: _PUTIMAGE (dx2, dy1)-(dx1, dy2), source_handle, dest_handle [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 34: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Flip by X axis" [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 24, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_PUTIMAGE (dx2, dy1)-(dx1, dy2), source_handle, dest_handle" K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) 'to flip image on y axis, swap the dy coordinate values: _PUTIMAGE (dx1, dy2)-(dx2, dy1), source_handle, dest_handle [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 34: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Flip by Y axis" [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 24, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_PUTIMAGE (dx1, dy2)-(dx2, dy1), source_handle, dest_handle " K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) 'to flip both, swap both the dx and dy coordinate values: _PUTIMAGE (dx2, dy2)-(dx1, dy1), source_handle, dest_handle [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 34: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Flip on both axis" [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 24, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_PUTIMAGE (dx2, dy2)-(dx1, dy1), source_handle, dest_handle" K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) 'to enlarge, double the second set of values plus any offset of the first coordinates: _PUTIMAGE (dx1, dy1)-((2 * dx2) + dx1, (2 * dy2) + dy1), source_handle, dest_handle [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 34: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Double image size" [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 24, 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_PUTIMAGE (dx1, dy1)-((2 * dx2) + dx1, (2 * dy2) + dy1), s_handle, d_handle [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Adapted from code by Darth Who
  

*Example 4:* Using \_PUTIMAGE to scroll a larger image created on a separate [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") screen page with QB64.





| ``` [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") ws& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(2560, 1440, 32) 'large image page s& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(1280, 720, 32)' program screen  [_DEST](/qb64wiki/index.php/DEST "DEST") ws& 'create large image of random filled circles [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 50     x = [RND](/qb64wiki/index.php/RND "RND")(1) * 2560     y = [RND](/qb64wiki/index.php/RND "RND")(1) * 1440     clr& = [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")([RND](/qb64wiki/index.php/RND "RND")(1) * 255, [RND](/qb64wiki/index.php/RND "RND")(1) * 255, [RND](/qb64wiki/index.php/RND "RND")(1) * 255)     [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (x, y), [RND](/qb64wiki/index.php/RND "RND")(1) * 300, clr&     [PAINT](/qb64wiki/index.php/PAINT "PAINT") (x, y), clr& [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This is a demo of some screen scrolling.   Use the number pad keys to scroll.  4 goes left, 6 goes right.  8 up, 2 down. ESC key will close this program." x = 0: y = 0 [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") s&  DO     [CLS](/qb64wiki/index.php/CLS "CLS")     _PUTIMAGE (0, 0), ws&, 0, (x, y)-(x + 1279, y + 719)     a$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")     [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") a$         [CASE](/qb64wiki/index.php/CASE "CASE") "4": x = x - 10: [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x < 0 [THEN](/qb64wiki/index.php/THEN "THEN") x = 0         [CASE](/qb64wiki/index.php/CASE "CASE") "6": x = x + 10: [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x > 1280 [THEN](/qb64wiki/index.php/THEN "THEN") x = 1280         [CASE](/qb64wiki/index.php/CASE "CASE") "8": y = y - 10: [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y < 0 [THEN](/qb64wiki/index.php/THEN "THEN") y = 0         [CASE](/qb64wiki/index.php/CASE "CASE") "2": y = y + 10: [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y > 720 [THEN](/qb64wiki/index.php/THEN "THEN") y = 720         [CASE](/qb64wiki/index.php/CASE "CASE") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(32): [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")     [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


Code example by SMcNeill
  

*Example 5:* \_PUTIMAGE can be used with no parameters at all if the [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") and [\_DEST](/qb64wiki/index.php/DEST "DEST") are already set.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 h& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 256) [_DEST](/qb64wiki/index.php/DEST "DEST") h& [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (10, 10), "This _PUTIMAGE used no parameters!" [_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") h& [_DEST](/qb64wiki/index.php/DEST "DEST") 0 _PUTIMAGE [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


### More examples


* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps")
* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1119)
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")
* [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE"), [\_SAVEIMAGE](/qb64wiki/index.php/SAVEIMAGE "SAVEIMAGE")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")
* [\_MAPTRIANGLE](/qb64wiki/index.php/MAPTRIANGLE "MAPTRIANGLE"), [STEP](/qb64wiki/index.php/STEP "STEP")
* [\_DEST](/qb64wiki/index.php/DEST "DEST"), [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE"), [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE")
* [Hardware images](/qb64wiki/index.php/Hardware_images "Hardware images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PUTIMAGE&oldid=8888>"




## Navigation menu








### Search





















