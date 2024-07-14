


\_NEWIMAGE - QB64 Phoenix Edition Wiki








# \_NEWIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_NEWIMAGE function prepares a window image surface and returns the [LONG](/qb64wiki/index.php/LONG "LONG") [handle](/qb64wiki/index.php/Handle "Handle") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) 	+ [4.1 More examples](#More_examples) * [5 See also](#See_also) |
| --- |


## Syntax


*handle&* = \_NEWIMAGE(*width&*, *height&*[, {*0*|*1*|*2*|*7*|*8*|*9*|*10*|*11*|*12*|*13*|*256*|*32*}])
  




## Parameters


* Minimum [LONG](/qb64wiki/index.php/LONG "LONG") screen dimensions are *width&* >= 1, *height&* >= 1 measured in pixels as [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [LONG](/qb64wiki/index.php/LONG "LONG") values.
	+ For mode 0 (text), *width&* and *height&* are measured in character blocks, not pixels.
* Mode is either a QBasic type [screen](/qb64wiki/index.php/SCREEN "SCREEN") mode (0 to 2 or 7 to 13), 256 colors or 32 bit (16 million colors) compatible.


  




## Description


* If the mode is omitted, an image will be created with the same BPP mode, font (which may block freeing of that font), palette, selected colors, transparent color, blend state and print method settings as the current [\_DESTination](/qb64wiki/index.php/DEST "DEST") image/[screen](/qb64wiki/index.php/SCREEN "SCREEN") page.
* Valid [LONG](/qb64wiki/index.php/LONG "LONG") [handle](/qb64wiki/index.php/Handle "Handle") returns are less than -1. Invalid handles equal -1 and a zero or positive value is also invalid.
* You can create any sized window (limited by the OS) in any emulated [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode or 32 bit using this function.
* Default text block size in emulated [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes 1, 2, 7, 8 and 13 is 8 X 8; 9 and 10 is 8 X 14; 11, 12, 256 and 32 bit is 8 X 16. The text block pixel size will allow you to calculate the available text rows and columns in a custom sized screen.
* To view the image page, just use [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") *handle&*. Even if another procedure changes the screen mode and clears the screen, the image can be restored later by using the same SCREEN handle mode.
* Use the [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE") function to preserve a SCREEN handle value when changing to another screen mode to restore it later.
* **32 bit screen surface backgrounds (black) have zero [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") so that they are transparent when placed over other surfaces.**


Use [CLS](/qb64wiki/index.php/CLS "CLS") or [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") to make a new surface background [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") 255 or opague.
* **Images are not deallocated when the [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") they are created in ends. Free them with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE").**
* **It is important to free unused or uneeded images with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") to prevent CPU [memory overflow errors](/qb64wiki/index.php/ERROR_Codes#Other_Errors "ERROR Codes").**
* **Do not try to free image handles currently being used as the active [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"). Change screen modes first.**


  




## Examples


*Example 1:* Shrinking a SCREEN 0 text window's size:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") _NEWIMAGE(28, 25, 0)  ``` |
| --- |


  

*Example 2:* Creating an 800 by 600 window version of SCREEN 12 with 256 colors (text 37 X 100):





| ``` handle& = _NEWIMAGE(800, 600, 256) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") handle&  ``` |
| --- |


  

*Example 3:* Setting up a 32 bit SCREEN with \_NEWIMAGE for page flipping in QB64.





| ``` SCREEN _NEWIMAGE(640, 480, 32), , 1, 0  ``` |
| --- |


*Note:* [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") may be used as a substitute for page flipping or [PCOPY](/qb64wiki/index.php/PCOPY "PCOPY").
  

*Example 4:* Switching between two different SCREEN modes





| ``` [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "Switching [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes" [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") _NEWIMAGE (800, 600, 256) mode1& = [_DEST](/qb64wiki/index.php/DEST "DEST")               'get current screen mode handle mode2& = _NEWIMAGE (300, 200, 13)  [_DEST](/qb64wiki/index.php/DEST "DEST") mode2&                  'prepare small window [COLOR](/qb64wiki/index.php/COLOR "COLOR") 10: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 13: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "mode2& = "; mode2& [COLOR](/qb64wiki/index.php/COLOR "COLOR") 13: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 16, 16: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "First"  [_DEST](/qb64wiki/index.php/DEST "DEST") mode1&  'work in main window [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 5 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") c = 1 [TO](/qb64wiki/index.php/TO "TO") 248    Color c: [PRINT](/qb64wiki/index.php/PRINT "PRINT") c; [NEXT](/qb64wiki/index.php/NEXT "NEXT") [COLOR](/qb64wiki/index.php/COLOR "COLOR") 12: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 44: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "mode1& = "; mode1& [COLOR](/qb64wiki/index.php/COLOR "COLOR") 11: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 30, 34: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press a key to goto Pop-up Window" [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode2&  'switch to small window [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode1&  'back to main window [COLOR](/qb64wiki/index.php/COLOR "COLOR") 12: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 37, 43: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "One more time!" [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode2&  'back to small window [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 16, 16: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "LAST "  ``` |
| --- |


*Explanation:* The [\_DEST](/qb64wiki/index.php/DEST_(function) "DEST (function)") function can determine the present screen mode destination handle. The second \_NEWIMAGE handle is created using a SCREEN 13 palette(256 colors also). Each SCREEN is worked on after changing the destination with [\_DEST](/qb64wiki/index.php/DEST "DEST") *handle&* statement. Images can be created before viewing them. When a key is pressed the second SCREEN created is displayed and so on.
**Legacy SCREEN modes can also return a \_DEST value, but the value will create a handle error.** To restore legacy screens get the[\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE") function value before changing screens. Then restore it using SCREEN oldmode&.
### More examples


* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [\_PIXELSIZE](/qb64wiki/index.php/PIXELSIZE "PIXELSIZE")


  




## See also


* [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")
* [\_SAVEIMAGE](/qb64wiki/index.php/SAVEIMAGE "SAVEIMAGE")
* [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE")
* [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")
* [\_CLIPBOARDIMAGE (function)](/qb64wiki/index.php/CLIPBOARDIMAGE_(function) "CLIPBOARDIMAGE (function)")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=NEWIMAGE&oldid=8724>"




## Navigation menu








### Search





















