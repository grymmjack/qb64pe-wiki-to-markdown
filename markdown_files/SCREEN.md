


SCREEN - QB64 Phoenix Edition Wiki








# SCREEN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The SCREEN statement sets the video display mode and size of the program window's workspace.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 QB64 Custom Screen Modes](#QB64_Custom_Screen_Modes) * [4 Legacy Screen Modes](#Legacy_Screen_Modes) * [5 Text and Graphics](#Text_and_Graphics) * [6 Examples](#Examples) 	+ [6.1 More Examples](#More_Examples) * [7 See also](#See_also) |
| --- |


## Syntax


SCREEN {*mode%*|*imagehandle&*} [, , active\_page, visual\_page]
  




## Parameters


* The SCREEN *mode* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values available today are 0 to 2 and 7 to 13 listed below.
* **QB64** can use a [LONG](/qb64wiki/index.php/LONG "LONG") [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") page or [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") file *image handle* value instead.
* The empty comma disables color when any value is used. **DO NOT USE!** Include the comma ONLY when using page flipping.
* If the SCREEN mode supports pages, the *active page* is the page to be worked on while *visual page* is the one displayed.


  

*Usage:*



* No SCREEN statement in a program defaults to SCREEN 0 text ONLY mode.
* A SCREEN statement that changes screen modes also clears the screen like [CLS](/qb64wiki/index.php/CLS "CLS"). Nothing on the screen is retained.
* Some screen mode text sizes are adjustable with [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") and all **QB64** screens support [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY") and page flipping.




| ```                        **LEGACY SCREEN MODES AT A GLANCE**   **Screen      Text           Graphics          Colors      Video    Text      Default**   **Mode   Rows   Columns   Width   Height  Attrib.   BPP   Pages    Block    QB64 Font**     0   25/43/50  80/40    No graphics     16/16 DAC  4     0-7     -----    _FONT 16    1      25      40      320     200     16/4 BG    4     none    8 X 8    _FONT 8    2      25      80      640     200      2/mono    1     none    8 X 8    _FONT 8    .................................................................................    7      25      40      320     200     16/16 DAC  4     0-7     8 X 8    _FONT 8    8      25      80      640     200     16/16      4     0-3     8 X 8    _FONT 8    9      25      80      640     350     16/64 DAC  4     0-1     8 X 14   _FONT 14   10      25      80      640     350     4/2 GScale 2     none    8 X 14   _FONT 14   11     30/60    80      640     480      2/mono    1     none    8 X 16   _FONT 16   12     30/60    80      640     480     16/262K    4     none    8 X 16   _FONT 16   13      25      40      320     200     256/65K    8     none    8 X 8    _FONT 8                **QB64 allows video paging and [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY") in ALL screen modes!**  ``` |
| --- |


  




## QB64 Custom Screen Modes


SCREEN *imagehandle&* [, , *active\_page*, *visual\_page*]
SCREEN [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(*wide&*, *high&*[, {*mode*|*256*|*32*}]) [, , *active\_page*, *visual\_page*]
SCREEN [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")(*file$*[, {*mode*|*256*|*32*}]) [, , *active\_page*, *visual\_page*]
  




* Custom screen modes can be created using a [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") or [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") function *imagehandle* return value.
* **QB64** screen modes 0 to 2 and 7 to 13 can be emulated with the same color depth and text block size and different dimensions.
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") screens can be any set size. A screen mode can be emulated or 256 or 32 bit colors can be designated.
* The [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") screen size will be the size of the image loaded. Can designate a *mode* or 256 or 32 bit colors.
* **QB64** allows page flipping or a [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY") in ANY SCREEN mode. [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") can also be used to reduce flickering in animations.
* All SCREEN modes are Windows in QB64. Use [\_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN") to set the window area to full screen.
* [\_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE") can position a window or the \_MIDDLE option can center it on the desktop.


([Return to Table of Contents](#toc))


  




## Legacy Screen Modes


* **SCREEN 0** (default mode) is a **text only** screen mode. 64 (VGA) colors with hi-intensity(blinking) colors 16 to 31. ([DAC](/qb64wiki/index.php/DAC "DAC") attrib 6, 8 to 15). 8 Background colors intensities only(0 - 7). No graphics are possible! Normally runs in a window. ALT-Enter switches from a window to fullscreen. To automatically run in **QBasic** fullscreen, use another Screen mode before using SCREEN 0. Can use [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY") with video pages 0 to 7. Text is 25, 43 or 50 rows by 40 or 80 columns. Default is 25 by 80. See [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH").


**Note:** Use [OUT](/qb64wiki/index.php/OUT "OUT") or [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR") to create higher intensity color backgrounds than [COLOR](/qb64wiki/index.php/COLOR "COLOR") , 7.
**All other available SCREEN modes can use text and graphics and are fullscreen in QBasic ONLY.**
* **SCREEN 1** has 4 background color attributes. 0 = black, 1 = blue, 2 = green, 3 = grey. White foreground only. Text is 25 by 40. White graphics is 320 by 200.


* **SCREEN 2** is **monochrome** with black background and white foreground. Text is 25 by 80. White graphics 640 by 200.          NO [COLOR](/qb64wiki/index.php/COLOR "COLOR") keyword allowed.


* **SCREEN 3 to 6 are no longer supported** on most computers! Using them will cause a video [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes")!


* **SCREEN 7** has 16 color attributes ([DAC](/qb64wiki/index.php/DAC "DAC") attrib. 8 to 15) with background colors. Text 25 rows by 40 columns. Graphics 320 columns by 200 rows. Video pages 0 to 7 for flipping or [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY").


* **SCREEN 8** has 16 color attributes with background. Text is 25 by 80. Graphics is 640 by 200. Video pages 0 to 3.


* **SCREEN 9** has 64 DAC color hues for ([DAC](/qb64wiki/index.php/DAC "DAC") attrib. 6, 8 to 15) with background colors. Text is 25 by 80. Graphics is 640 by 350. Video pages 0 and 1 for flipping or [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY").


* **SCREEN 10** has 4 gray scale color attributes with black background. 1 = normal white, 2 = blinking white and 3 = bright white. Text is 25 by 80. Graphics is 640 by 350.


* **SCREEN 11** is **monochrome** with black background and white foreground. Text is 30 or 60 by 80 columns(see [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH")). White graphics is 640 by 480. NO [COLOR](/qb64wiki/index.php/COLOR "COLOR") keyword allowed.


* **SCREEN 12** has 16 color attributes, black background. 256K possible color hues. Text is 30 or 60 by 80 columns(see [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH")). Graphics 640 by 480.


* **SCREEN 13** has 256 color attributes, black background. 256K possible color hues. Text is 25 by 40. Graphics is 320 by 200.


* **SCREEN [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")**(wide&, deep&, mode%) can imitate any size screen mode or use 32 bit or 256 color modes in **QB64**.


* **SCREEN [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")**(imagehandle&, colors) can load a program screen of an image file handle in **QB64** using 256 or 32 bit.


**QB64 can use page flipping with any number of pages in any screen mode!**
([Return to Table of Contents](#toc))


  




## Text and Graphics


**Text Coordinates:**
* Are a minimum of 1 and the values given above are the maximums. [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1 is the top left SCREEN text position.
* Text characters occupy a certain sized pixel box adjusted by [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") in some screen modes.
* Text [PRINT](/qb64wiki/index.php/PRINT "PRINT") cursor positions can be read by [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN") and [POS(0)](/qb64wiki/index.php/POS "POS") to [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") text [PRINTs](/qb64wiki/index.php/PRINT "PRINT").
* [VIEW PRINT](/qb64wiki/index.php/VIEW_PRINT "VIEW PRINT") can be used to designate a text view port area.
* In **QB64** the [\_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") and [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") functions will return the text dimensions in SCREEN 0 only.


  




**Graphic Coordinates:**
* The minimum on screen graphics pixel coordinates are 0 for columns and rows in the top left corner.
* Maximum pixel coordinates are one less than the maximum dimensions above because the pixel count starts at 0.
* Graphic objects such as [PSET](/qb64wiki/index.php/PSET "PSET"), [PRESET](/qb64wiki/index.php/PRESET "PRESET"), [LINE](/qb64wiki/index.php/LINE "LINE"), [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") and [DRAW](/qb64wiki/index.php/DRAW "DRAW") can be placed partially off of the screen.
* [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") and [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)") screen image operations MUST be located completely on the screen in QBasic!
* [VIEW](/qb64wiki/index.php/VIEW "VIEW") can be used to designate a graphic view port area of the screen.
* [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW") can be used to set the graphics SCREEN coordinates to almost any size needed. Use the SCREEN option for normal row coordinate values. Row coordinates are Cartesian(decrease in value going down the screen) otherwise.
* In **QB64** the [\_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") and [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") functions will return the graphic pixel dimensions in SCREENs other than 0.


  




**QB64 Screen Statements and Functions:**
* For file image screens that adopt the image dimensions and image color settings use: [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")
* To create custom sized screen modes or pages and 256 or 32 bit colors use: [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")
* [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") can stretch or reduce the size of images to fit the SCREEN size.
* [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)") can use [\_CLIP](/qb64wiki/index.php/CLIP "CLIP") to set objects partially off screen. [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") can read objects off screen as a color in QB64 ONLY.
* A [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") statement can be used to only display an image after changes instead of using page flipping or [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY").
* The current desktop screen resolution can be found using the [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE") handle value with [\_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") and [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT").
* **NOTE: Default 32 bit backgrounds are clear black or [\_RGBA](/qb64wiki/index.php/RGBA "RGBA")(0, 0, 0, 0)! Use [CLS](/qb64wiki/index.php/CLS "CLS") to make the black opaque!**


([Return to Table of Contents](#toc))


  




## Examples


*Example 1:* Shows an example of each legacy screen mode available to QBasic and QB64.


| ``` SCREEN 0 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This is SCREEN 0 - only text is allowed!" [FOR](/qb64wiki/index.php/FOR "FOR") S = 1 [TO](/qb64wiki/index.php/TO "TO") 13    [IF](/qb64wiki/index.php/IF "IF") S < 3 [OR](/qb64wiki/index.php/OR "OR") S > 6 [THEN](/qb64wiki/index.php/THEN "THEN")      [DO](/qb64wiki/index.php/DO "DO"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""      SCREEN S      [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This is SCREEN"; S; " - can use text and graphics!"        [IF](/qb64wiki/index.php/IF "IF") S = 2 [OR](/qb64wiki/index.php/OR "OR") S = 11 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Monochrome - no [COLOR](/qb64wiki/index.php/COLOR "COLOR") statements!"        [IF](/qb64wiki/index.php/IF "IF") S = 10 [THEN](/qb64wiki/index.php/THEN "THEN")          [COLOR](/qb64wiki/index.php/COLOR "COLOR") 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This SCREEN has only 4 colors. Black and 3 white: 2 blinks.          [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (100,100), 50, 2        [ELSE](/qb64wiki/index.php/ELSE "ELSE") : [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (100,100), 100, S        [END IF](/qb64wiki/index.php/END_IF "END IF")    [END IF](/qb64wiki/index.php/END_IF "END IF") [NEXT](/qb64wiki/index.php/NEXT "NEXT") [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")  ``` |
| --- |




| ``` This is SCREEN 0 - only text is allowed!  ``` |
| --- |


Displays each SCREEN mode one at a time with a [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (except for SCREEN 0)
([Return to Table of Contents](#toc))


### More Examples


* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [Program ScreenShots](/qb64wiki/index.php/Program_ScreenShots "Program ScreenShots")
* [ThirtyTwoBit SUB](/qb64wiki/index.php/ThirtyTwoBit_SUB "ThirtyTwoBit SUB")
* [SelectScreen](/qb64wiki/index.php/SelectScreen "SelectScreen")
* [ScreenMode](/qb64wiki/index.php/ScreenMode "ScreenMode")


  




## See also


* [COLOR](/qb64wiki/index.php/COLOR "COLOR"), [CLS](/qb64wiki/index.php/CLS "CLS"), [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH")
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_SAVEIMAGE](/qb64wiki/index.php/SAVEIMAGE "SAVEIMAGE")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")
* [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT"), [\_FONT](/qb64wiki/index.php/FONT "FONT")
* [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY"), [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE"), [\_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE")
* [\_SCREENHIDE](/qb64wiki/index.php/SCREENHIDE "SCREENHIDE"), [\_SCREENSHOW](/qb64wiki/index.php/SCREENSHOW "SCREENSHOW"), [\_SCREENICON](/qb64wiki/index.php/SCREENICON "SCREENICON")
* [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE"), [OUT](/qb64wiki/index.php/OUT "OUT"), [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY"),
* [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)"), [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [VIEW](/qb64wiki/index.php/VIEW "VIEW"), [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW"), [VIEW PRINT](/qb64wiki/index.php/VIEW_PRINT "VIEW PRINT")
* [SCREEN (function)](/qb64wiki/index.php/SCREEN_(function) "SCREEN (function)"), [POINT](/qb64wiki/index.php/POINT "POINT")
* [Screen Memory](/qb64wiki/index.php/Screen_Memory "Screen Memory"), [Screen Saver Programs](/qb64wiki/index.php/Screen_Saver_Programs "Screen Saver Programs")
* [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SCREEN&oldid=8691>"




## Navigation menu








### Search





















