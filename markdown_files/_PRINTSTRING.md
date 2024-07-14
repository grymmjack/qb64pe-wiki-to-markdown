


\_PRINTSTRING - QB64 Phoenix Edition Wiki








# \_PRINTSTRING



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_PRINTSTRING statement prints text [strings](/qb64wiki/index.php/STRING "STRING") using graphic column and row coordinate positions.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


\_PRINTSTRING(*column*, *row*), *textExpression$*[, *imageHandle&*]
  




## Parameters


* *column* and *row* are [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [LONG](/qb64wiki/index.php/LONG "LONG") starting PIXEL (graphic) column and row coordinates to set text or custom fonts.
* *textExpression$* is any literal or variable [string](/qb64wiki/index.php/STRING "STRING") value of text to be displayed.
* *imageHandle&* is the optional image or destination to use. Zero designates current [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") page.


  




## Description


* The starting coordinate sets the top left corner of the text to be printed. Use [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT") to calculate that text or [font](/qb64wiki/index.php/FONT "FONT") position
* The [\_FONT](/qb64wiki/index.php/FONT "FONT") size can affect the [screen](/qb64wiki/index.php/SCREEN "SCREEN") and row heights.
	+ Custom fonts are not required. \_PRINTSTRING can print all [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters.
* [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH") can be used to determine how wide a text print will be so that the screen width is not exceeded.
* If the *imageHandle&* is omitted, the current image, page or screen destination is used.
* Can use the current font alpha blending with a designated image background. See the [\_RGBA](/qb64wiki/index.php/RGBA "RGBA") function example.
* Use the [\_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE") statement before printing to set how the background is rendered.
	+ Use the [\_PRINTMODE (function)](/qb64wiki/index.php/PRINTMODE_(function) "PRINTMODE (function)") to find the current \_PRINTMODE setting.
* In SCREEN 0 (text only), \_PRINTSTRING works as one-line replacement for **LOCATE x, y: PRINT text$**, without changing the current cursor position.


  




## Availability


* In versions of QB64 prior to 1.000 \_PRINTSTRING can only be used in graphic, 256 color or 32 bit screen modes, not SCREEN 0.


  




## Examples


*Example 1:* Printing those unprintable [ASCII](/qb64wiki/index.php/ASCII "ASCII") control characters is no longer a problem!





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 256)  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") code = 0 [TO](/qb64wiki/index.php/TO "TO") 31   chrstr$ = chrstr$ + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(code) + [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1) [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [_FONT](/qb64wiki/index.php/FONT "FONT") [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("C:\Windows\Fonts\Cour.ttf", 20, "MONOSPACE") 'select monospace font  _PRINTSTRING (0, 16), chrstr$  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ```   ☺ ☻ ♥ ♦ ♣ ♠ • ◘ ○ ◙ ♂ ♀ ♪ ♫ ☼ ► ◄ ↕ ‼ ¶ § ▬ ↨ ↑ ↓ → ← ∟ ↔ ▲ ▼  ``` |
| --- |


  

*Example 2:* Making any **QB64 program window** larger using a SUB that easily converts PRINT to \_PRINTSTRING.





| ``` Scr13& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(320, 200, 13)  'this is the old SCREEN 13 image page to set the image Big13& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 256) 'use 4 X 3 aspect ratio that QBasic used when full screen  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") Big13& [_DEST](/qb64wiki/index.php/DEST "DEST") Scr13& image1& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("Howie.BMP", 256) image2& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("Howie2.BMP", 256) [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (10, 20), image1&, Scr13& [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (160, 20), image2&, Scr13& [_COPYPALETTE](/qb64wiki/index.php/COPYPALETTE "COPYPALETTE") image1&, Scr13& [COLOR](/qb64wiki/index.php/COLOR "COLOR") 151: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 4: PRINTS "Screen 13 Height Reduction to 83%" [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 22, 22: PRINTS [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(24) + " 4 X 3 Proportion"  'use [concatenation](/qb64wiki/index.php/Concatenation "Concatenation") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 24, 21: PRINTS [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) + " Stretched at 100%" 'instead of a [semicolon](/qb64wiki/index.php/Semicolon "Semicolon")! [_COPYPALETTE](/qb64wiki/index.php/COPYPALETTE "COPYPALETTE") Scr13&, Big13&  'required when imported image colors are used [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , Scr13&, Big13&   'stretches the screen to double the size K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") PRINTS (Text$) row% = ([CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN") - 1) * [_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT")      'finds current screen page text or font row height col% = ([POS](/qb64wiki/index.php/POS "POS")(0) - 1) * [_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH")("W") 'finds current page text or font column width _PRINTSTRING (col%, row%), Text$ [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* The procedure above creates a larger version of a SCREEN 13 window by stretching it with [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE"). It cannot stretch PRINTed text so \_PRINTSTRING must be used instead. [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") sets the PRINT cursor position for [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN") and [POS](/qb64wiki/index.php/POS "POS")(0) to read. The SUB then converts the coordinates to graphical ones. Then **change** [PRINT](/qb64wiki/index.php/PRINT "PRINT") to PRINTS using the IDE **Search Menu**.
[Download of Example 2 Bitmap images](https://www.dropbox.com/s/tcdik1ajegbeiz4/HOWIE.zip?dl=0)
  

*Example 3:* Rotating a text string around a graphic object.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [DIM](/qb64wiki/index.php/DIM "DIM") row [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), cnt [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), cstart [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), cend [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") [DIM](/qb64wiki/index.php/DIM "DIM") xrot [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), yrot [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), scale [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") ' [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN")                       'full screen optional cstart = 0: cend = 8 * [ATN](/qb64wiki/index.php/ATN "ATN")(1) xrot = 6: yrot = 60: scale = 4 row = 1 [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (320, 240), 15, 9: [PAINT](/qb64wiki/index.php/PAINT "PAINT") [STEP](/qb64wiki/index.php/STEP "STEP")(0, 0), 9 [DO](/qb64wiki/index.php/DO "DO")   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = cstart [TO](/qb64wiki/index.php/TO "TO") cend [STEP](/qb64wiki/index.php/STEP "STEP") .04     x = 300 + (scale * 40 - (row * xrot)) * [COS](/qb64wiki/index.php/COS "COS")(i)     y = 200 + (scale * 40 - (row * yrot)) * [SIN](/qb64wiki/index.php/SIN "SIN")(i)     cnt = cnt + 1     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 7: _PRINTSTRING (x, y), "HELLO WORLD!", 0  'display     [IF](/qb64wiki/index.php/IF "IF") cnt = [LEN](/qb64wiki/index.php/LEN "LEN")(text$) * 8 [THEN](/qb64wiki/index.php/THEN "THEN") cnt = 0: [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0: _PRINTSTRING (x, y), "HELLO WORLD!", 0  'erase     [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.02   [NEXT](/qb64wiki/index.php/NEXT "NEXT") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) 'escape key exit [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15 [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Adapted from code by Unseen Machine
  




## See also


* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH"), [\_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE")
* [\_CONTROLCHR](/qb64wiki/index.php/CONTROLCHR "CONTROLCHR")
* [\_FONT](/qb64wiki/index.php/FONT "FONT"), [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT"), [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT"), [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE"), [\_SCREENPRINT](/qb64wiki/index.php/SCREENPRINT "SCREENPRINT")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PRINTSTRING&oldid=7931>"




## Navigation menu








### Search





















