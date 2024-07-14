


POINT - QB64 Phoenix Edition Wiki








# POINT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **POINT** function returns the pixel [COLOR](/qb64wiki/index.php/COLOR "COLOR") attribute at a specified graphics coordinate or the current graphic cursor position.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) 	+ [2.1 More Examples](#More_Examples) * [3 See also](#See_also) |
| --- |


## Syntax


Graphic Color
color\_attribute% = **POINT (***column%, row%***)**
Graphic cursor position
pointer\_coordinate% = **POINT(**{0|1|2|3}**)**
  




## Parameters


**Graphic Color syntax:**



* The [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") *column* and *row* coordinates designate the pixel position color on the screen to read.
* The return value is an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") palette attribute value or an [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") [\_RGBA](/qb64wiki/index.php/RGBA "RGBA") 32 bit value in QB64.


**Graphic cursor position syntax:**



* The [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") position number can be 0 to 3 depending on the cursor position desired:
	+ POINT(0) returns the current graphic cursor [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") column pixel coordinate.
	+ POINT(1) returns the current graphic cursor [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") row pixel coordinate.
	+ POINT(2) returns the current graphic cursor [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW") column position.
	+ POINT(3) returns the current graphic cursor [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW") row position.
* If a [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW") view port has not been established, the coordinate returned will be the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") cursor pixel position.
* The return value is the current graphic cursor *column* or *row* pixel position on the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") or [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW").
* Graphic cursor positions returned will be the last ones used in a graphic shape such as a [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") center point.


  

*Usage:*



* Use **[\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE")** first to set the image handle that POINT should read or QB64 will assume the current source image.


**\_SOURCE 0** 'sets POINT to read the current SCREEN image after reading a previous source image
* **POINT cannot be used in SCREEN 0!** Use the [SCREEN](/qb64wiki/index.php/SCREEN_(function) "SCREEN (function)") function to point text character codes and colors in SCREEN 0.


  




**POINT in QBasic Legacy Graphic SCREEN Modes:**
* The [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") color attributes returned are limited by the number of colors in the legacy SCREEN mode used.
* *Column* and *row* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") parameters denote the graphic pixel coordinate to read.
* In **QB64** the offscreen or off image value returned is -1. Use IF POINT(x, y) <> -1 THEN...
* In QBasic the coordinates MUST be on the screen or an [Illegal Function Call error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.


  




**POINT in QB64 32 Bit Graphic [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") or [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") Modes:**
* Returns [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") 32 bit color values. Use [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") values when you don't want negative values.
* **[\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") variables should be used when comparing POINT returns with [\_RGB](/qb64wiki/index.php/RGB "RGB") or [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") bit values**
* Convert 32 bit color values to RGB intensities(0 to 255) using the [\_RED32](/qb64wiki/index.php/RED32 "RED32"), [\_GREEN32](/qb64wiki/index.php/GREEN32 "GREEN32") and [\_BLUE32](/qb64wiki/index.php/BLUE32 "BLUE32") functions.
* To convert color intensities to OUT &H3C9 color port palette intensity values divide the values of 0 to 255 by 4.
* Use the [\_PALETTECOLOR (function)](/qb64wiki/index.php/PALETTECOLOR_(function) "PALETTECOLOR (function)") to convert color port palette intensities in 32 bit modes.


  

*Example 1:* How [\_RGB](/qb64wiki/index.php/RGB "RGB") 32 bit values return [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") or [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") values in QB64.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") clr [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") 'DO NOT use LONG in older versions of QB64 (V .936 down) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) [CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255)  'makes the background opaque white  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "POINT(100, 100) ="; POINT(100, 100) clr = POINT(100, 100) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Variable clr = ";  clr [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") clr = [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255) [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Long OK" [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") POINT(100, 100) = [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255) [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_RGB OK" [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") POINT(100, 100) = clr [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Type OK" 'will not print with a LONG variable type  ``` |
| --- |


**Note:** Change the [DIM](/qb64wiki/index.php/DIM "DIM") *clr* variable type to [LONG](/qb64wiki/index.php/LONG "LONG") to see how the last [IF](/qb64wiki/index.php/IF "IF") statement doesn't [PRINT](/qb64wiki/index.php/PRINT "PRINT") as shown in the output below:


| ``` POINT(100, 100) = 4294967295 Variable clr = -1 Long OK _RGB OK  ``` |
| --- |


  



*Example 2:* Using a POINT mouse routine to get the 32 bit color values of the image.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "Mouse POINTer 32"   '[LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") "Enter an image file: ", image$  'use quotes around file names with spaces image$ = "QB64bee.png" 'any 24/32 bit image up to 320 X 240 with current [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") settings i& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")(image$, 32) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") i& >= -1 [THEN](/qb64wiki/index.php/THEN "THEN") [BEEP](/qb64wiki/index.php/BEEP "BEEP"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Could [NOT](/qb64wiki/index.php/NOT "NOT") load image!": [END](/qb64wiki/index.php/END "END") w& = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(i&): h& = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(i&)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Make background transparent?(Y\N)"; BG$ = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")([INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1)) [PRINT](/qb64wiki/index.php/PRINT "PRINT") BG$ [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 1  '[CLS](/qb64wiki/index.php/CLS "CLS") 'commented to keep background alpha 0  [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") BG$ = "Y" [THEN](/qb64wiki/index.php/THEN "THEN") [_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(255, 255, 255), i& 'make white Background transparent [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (320 - w&, 240 - h&)-((2 * w&) + (320 - w&), (2 * h&) + (240 - h&)), i&, 0 [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") i&  [_MOUSEMOVE](/qb64wiki/index.php/MOUSEMOVE "MOUSEMOVE") 320, 240 'center mouse pointer on screen  [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 100   [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT")     mx = [_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX")     my = [_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY")     c& = POINT(mx, my)     r = [_RED32](/qb64wiki/index.php/RED32 "RED32")(c&)     g = [_GREEN32](/qb64wiki/index.php/GREEN32 "GREEN32")(c&)     b = [_BLUE32](/qb64wiki/index.php/BLUE32 "BLUE32")(c&)     a = [_ALPHA32](/qb64wiki/index.php/ALPHA32 "ALPHA32")(c&)     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") mx; my, "R:"; r, "G:"; g, "B:"; b, "A:"; a; "  "     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "HTML Color: [&H](/qb64wiki/index.php/%26H "&H")" + [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")([HEX$](/qb64wiki/index.php/HEX$ "HEX$")(c&), 6)   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") > "" [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* Use the mouse pointer to get the background RGB of the image to make it transparent with [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR").
  

*Snippet:* Creating an image mask to PUT an image over other colored backgrounds. See: [GET and PUT Demo](/qb64wiki/index.php/GET_and_PUT_Demo "GET and PUT Demo") to run code.





| ```  FOR c = 0 TO 59    '60 X 60 area from 0 pixel    FOR r = 0 TO 59     IF POINT(c, r) = 0 THEN [PSET](/qb64wiki/index.php/PSET "PSET") (c, r), 15 ELSE PSET (c, r), 0    NEXT r  NEXT c  [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)")(0, 0)-(60, 60), Image(1500) ' save mask in an array(indexed above original image).  ``` |
| --- |


*Explanation:* In the procedure all black areas(background) are changed to white for a PUT using AND over other colored objects. The other image colors are changed to black for a PUT of the original image using XOR. The array images can be [BSAVEd](/qb64wiki/index.php/BSAVE "BSAVE") for later use. **QB64 can also** [PUT](/qb64wiki/index.php/PUT "PUT") **a full screen 12 image from an array directly into a** [BINARY](/qb64wiki/index.php/BINARY "BINARY") **file.**
### More Examples


* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [Program ScreenShots](/qb64wiki/index.php/Program_ScreenShots "Program ScreenShots")
* [ThirtyTwoBit SUB](/qb64wiki/index.php/ThirtyTwoBit_SUB "ThirtyTwoBit SUB")
* [ThirtyTwoBit MEM SUB](/qb64wiki/index.php/ThirtyTwoBit_MEM_SUB "ThirtyTwoBit MEM SUB")


  




## See also


* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")
* [\_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE"), [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET")
* [PSET](/qb64wiki/index.php/PSET "PSET"), [PRESET](/qb64wiki/index.php/PRESET "PRESET")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [SCREEN (function)](/qb64wiki/index.php/SCREEN_(function) "SCREEN (function)")
* [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)"), [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps"), [Creating Sprite Masks](/qb64wiki/index.php/Creating_Sprite_Masks "Creating Sprite Masks"), [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=POINT&oldid=8665>"




## Navigation menu








### Search





















