


\_PRINTIMAGE - QB64 Phoenix Edition Wiki








# \_PRINTIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_PRINTIMAGE statement prints a colored image on the printer, stretching it to full paper size first.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


\_PRINTIMAGE *imageHandle&*
  




* *imageHandle&* is created by the [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") or [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE") functions.
* Use a white background to save ink. [CLS](/qb64wiki/index.php/CLS "CLS") , [\_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255) can be used to set the white background in any [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode.
* The image may be stretched disproportionately using normal screen sizes. To compensate, use a [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") screen that is proportional to the paper size. *e.g.* A 640 X 900 SCREEN page is roughly the same as 3 times a 210mm X 297mm paper size.
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") or graphic screen pages can use [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") to print different sized text [\_FONTs](/qb64wiki/index.php/FONT "FONT").
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Examples


*Example 1:* Shows how to transfer custom font text on screen pages to the printer in Windows. Change the font path for other OS's.





| ``` PageScale = 10 PageHeight = 297 * PageScale 'A4 paper size is 210 X 297 mm PageWidth = 210 * PageScale Page& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(PageWidth, PageHeight, 32) [_DEST](/qb64wiki/index.php/DEST "DEST") Page&: [CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255): [_DEST](/qb64wiki/index.php/DEST "DEST") 0  'make background white to save ink! CursorPosY = 0  'example text to print PointSize = 12 text$ = "The rain in Spain falls mainly on the plain." [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") PrintText  PointSize = 50 text$ = "BUT!" [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") PrintText  PointSize = 12 text$ = "In Hartford, Hereford, and Hampshire, hurricanes hardly happen." [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") PrintText  [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Preview (Y/N)?", i$                      'print preview of screen (optional) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(i$) = "Y" [THEN](/qb64wiki/index.php/THEN "THEN")   Prev& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(600, 900, 32)               'print preview smaller image   [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , Page&, Prev&   [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") Prev&   DO: [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""   [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 [END IF](/qb64wiki/index.php/END_IF "END IF")  [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Print on printer (Y/N)?", i$             'print screen page on printer [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(i$) = "Y" [THEN](/qb64wiki/index.php/THEN "THEN")   _PRINTIMAGE Page& [END IF](/qb64wiki/index.php/END_IF "END IF")  [END](/qb64wiki/index.php/END "END")  PrintText: FontHeight = [INT](/qb64wiki/index.php/INT "INT")(PointSize * 0.3527 * PageScale) FontHandle = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("c:\windows\fonts\times.ttf", FontHeight) [_DEST](/qb64wiki/index.php/DEST "DEST") Page& [_FONT](/qb64wiki/index.php/FONT "FONT") FontHandle [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 0, 0), [_RGBA](/qb64wiki/index.php/RGBA "RGBA")(0, 0, 0, 0)        'RED text on clear black background [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (0, CursorPosY), text$ [_FONT](/qb64wiki/index.php/FONT "FONT") 16                               'change to the QB64 default font to free it [_FREEFONT](/qb64wiki/index.php/FREEFONT "FREEFONT") FontHandle [_DEST](/qb64wiki/index.php/DEST "DEST") 0 CursorPosY = CursorPosY + FontHeight            'adjust print position down [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


Code by Galleon
*Explanation:* CLS with the color white makes sure that the background is not printed a color. The PrintText [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") sets the [COLOR](/qb64wiki/index.php/COLOR "COLOR") of the text to red with a transparent background using [\_RGBA](/qb64wiki/index.php/RGBA "RGBA") to set the [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") transparency to zero or clear black.
  

*Example 2:* Printing an old SCREEN 12 [ASCII](/qb64wiki/index.php/ASCII "ASCII") table using a deeper sized page to prevent stretching by \_PRINTIMAGE.





| ``` [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "Print Preview ASCII Table" [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 900, 256)  'size is proportional to 210mm X 297mm(8-1/2 X 11) paper  [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C8, 0: [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C9, 63: [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C9, 63: [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C9, 63 'white background saves ink!  Align 8, 2, "ASCII and Extended Character Code Table using [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(n%)" [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(80, 223) [COLOR](/qb64wiki/index.php/COLOR "COLOR") 40 [PRINT](/qb64wiki/index.php/PRINT "PRINT") " "; [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i% = 0 [TO](/qb64wiki/index.php/TO "TO") 13   [PRINT](/qb64wiki/index.php/PRINT "PRINT") i%;: SetCHR [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN"), [POS](/qb64wiki/index.php/POS "POS")(0), 40, i%   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN"), [POS](/qb64wiki/index.php/POS "POS")(0) + 1 [NEXT](/qb64wiki/index.php/NEXT "NEXT") i% [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i% = 14 [TO](/qb64wiki/index.php/TO "TO") 16   [PRINT](/qb64wiki/index.php/PRINT "PRINT") i%; [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(i%); [NEXT](/qb64wiki/index.php/NEXT "NEXT") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN") + 1, 2 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 17 [TO](/qb64wiki/index.php/TO "TO") 27   [PRINT](/qb64wiki/index.php/PRINT "PRINT") i; [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(i); [NEXT](/qb64wiki/index.php/NEXT "NEXT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i% = 28 [TO](/qb64wiki/index.php/TO "TO") 31   [PRINT](/qb64wiki/index.php/PRINT "PRINT") i%;: SetCHR [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN"), [POS](/qb64wiki/index.php/POS "POS")(0), 40, i%   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN"), [POS](/qb64wiki/index.php/POS "POS")(0) + 1 [NEXT](/qb64wiki/index.php/NEXT "NEXT") i% [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN") + 1, 2 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") 32; [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(32); [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i% = 33 [TO](/qb64wiki/index.php/TO "TO") 255   [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") i%     [CASE](/qb64wiki/index.php/CASE "CASE") 45, 58, 71, 84: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN") + 1, 1     [CASE](/qb64wiki/index.php/CASE "CASE") [IS](/qb64wiki/index.php/IS "IS") > 96: [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") (i% - 97) [MOD](/qb64wiki/index.php/MOD "MOD") 11 = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN") + 1, 1   [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")   [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") i%     [CASE](/qb64wiki/index.php/CASE "CASE") 48 [TO](/qb64wiki/index.php/TO "TO") 57: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 9 'denotes number keys 48 to 57     [CASE](/qb64wiki/index.php/CASE "CASE") 65 [TO](/qb64wiki/index.php/TO "TO") 90: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 5 ' A to Z keys 65 to 90     [CASE](/qb64wiki/index.php/CASE "CASE") 97 [TO](/qb64wiki/index.php/TO "TO") 122: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 36 'a to z keys 97 to 122     [CASE](/qb64wiki/index.php/CASE "CASE") 127 [TO](/qb64wiki/index.php/TO "TO") 175: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 42     [CASE](/qb64wiki/index.php/CASE "CASE") 176 [TO](/qb64wiki/index.php/TO "TO") 223: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 6 'drawing characters 176 to 223     [CASE](/qb64wiki/index.php/CASE "CASE") [IS](/qb64wiki/index.php/IS "IS") > 223: [COLOR](/qb64wiki/index.php/COLOR "COLOR") 42     [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE"): [COLOR](/qb64wiki/index.php/COLOR "COLOR") 2   [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") i% = 98 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") i% = 99 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") i% = 100 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1);   [PRINT](/qb64wiki/index.php/PRINT "PRINT") " "; i%; [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(i%); [NEXT](/qb64wiki/index.php/NEXT "NEXT") i% [COLOR](/qb64wiki/index.php/COLOR "COLOR") 3: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "= NBSP(Non-Breaking Space)" [COLOR](/qb64wiki/index.php/COLOR "COLOR") 8: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(80, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(220)) Border 8 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 4: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 27, 4: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "7) BELL, 8) Backspace, 9) Tab, 10) LineFeed(printer), 12) FormFeed(printer)" [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 28, 4: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "  13) Return, 26) End Of File, 27) Escape  30) Line up, 31) Line down "  Align 13, 29, "Press Ctrl + P to PRINT!"  DO: [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): K$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"): [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") K$ <> "" Align 13, 29, [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(50) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") K$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(16) [THEN](/qb64wiki/index.php/THEN "THEN")   _PRINTIMAGE 0              '<<<<<<<<<<<< to PRINTER   Align 11, 29, "Use the ASCII Table for a reference of the codes!"   [SOUND](/qb64wiki/index.php/SOUND "SOUND") 700, 4 [END IF](/qb64wiki/index.php/END_IF "END IF") K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")  [SUB](/qb64wiki/index.php/SUB "SUB") Align (Tclr, Trow, txt$) Tcol = 41 - ([LEN](/qb64wiki/index.php/LEN "LEN")(txt$) \ 2) [COLOR](/qb64wiki/index.php/COLOR "COLOR") Tclr: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") Trow, Tcol: [PRINT](/qb64wiki/index.php/PRINT "PRINT") txt$; [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") Border (clr%) [COLOR](/qb64wiki/index.php/COLOR "COLOR") clr% [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") row = 1 [TO](/qb64wiki/index.php/TO "TO") 30   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") row, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(179);   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") row, 80: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(179); [NEXT](/qb64wiki/index.php/NEXT "NEXT") row [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(80, 196); [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 30, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(80, 196); [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(218); [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 80: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(191); [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 30, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(192); [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 30, 80: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(217); [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") SetCHR (Trow, Tcol, FG, ASCode) Srow = 16 * (Trow - 1): Scol = 8 * (Tcol - 1) 'convert text to graphic coordinates [COLOR](/qb64wiki/index.php/COLOR "COLOR") FG: [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (Scol, Srow), [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(ASCode) [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* The [ASCII](/qb64wiki/index.php/ASCII "ASCII") character table was originally made in [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 (640 X 480) and was adapted to 256 colors.
  




## See also


* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")
* [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE"), [\_SAVEIMAGE](/qb64wiki/index.php/SAVEIMAGE "SAVEIMAGE")
* [LPRINT](/qb64wiki/index.php/LPRINT "LPRINT")
* [Windows Printer Settings](/qb64wiki/index.php/Windows_Printer_Settings "Windows Printer Settings")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PRINTIMAGE&oldid=8687>"




## Navigation menu








### Search





















