


\_FREEFONT - QB64 Phoenix Edition Wiki








# \_FREEFONT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_FREEFONT statement frees a font handle that was created by [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_FREEFONT (*fontHandle&*)
  




## Description


* Unloads fonts that are no longer in use or needed in order to free program memory and resources.
* You cannot free a font which is in use. Change the font to a QB64 default font size before freeing the handle (see example below).
* Predefined **QB64** font handle numbers can be used before freeing a font:
	+ **\_FONT 8**  - default font for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 1, 2, 7, 8 or 13
	+ **\_FONT 14** - default font for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 9 or 10
	+ **\_FONT 16** - default font for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 ([WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") 80, 25 text only), 11 or 12
	+ **\_FONT 9, 15** and **17** are the double width versions of 8, 14 and 16 respectively in text **SCREEN 0**.
* If the font handle is invalid (equals -1 or 0), an [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur. **Check handle values before using or freeing them.**
* You cannot free inbuilt/default QB64 fonts nor do they ever need freed.


  




## Examples


*Example 1:* Previews and creates a file list of valid MONOSPACE TTF fonts by checking the [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT") handle values.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 path$ = "C:\WINDOWS\Fonts\" 'path to the font folder [SHELL](/qb64wiki/index.php/SHELL "SHELL") [_HIDE](/qb64wiki/index.php/HIDE "HIDE") "DIR /b " + path$ + "\*.ttf > TTFonts.INF" style$ = "monospace" 'set style to MONOSPACE [OPEN](/qb64wiki/index.php/OPEN "OPEN") "TTFonts.INF" [FOR](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [INPUT](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [AS](/qb64wiki/index.php/OPEN "OPEN") #1 'list of TTF fonts only [OPEN](/qb64wiki/index.php/OPEN "OPEN") "TTFMono.INF" [FOR](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [OUTPUT](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [AS](/qb64wiki/index.php/OPEN "OPEN") #2 'will hold list of valid MONOSPACE fonts  [DO UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [EOF](/qb64wiki/index.php/EOF "EOF")(1): found = found + 1     [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") #1, font$     f& = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")(path$ + font$, 30, style$)     [IF](/qb64wiki/index.php/IF "IF") f& > 0 [THEN](/qb64wiki/index.php/THEN "THEN") 'check for valid handle values > 0         OK = OK + 1         [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #2, font$         [_FONT](/qb64wiki/index.php/FONT "FONT") f& 'will create error if handle is invalid!         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello World!"         [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") font$; f&         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press any key."         K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1)         [_FONT](/qb64wiki/index.php/FONT "FONT") 16 'use QB64 default font to free tested font         _FREEFONT f& 'returns an error if handle <= 0!         [CLS](/qb64wiki/index.php/CLS "CLS")     [END IF](/qb64wiki/index.php/END_IF "END IF")     [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [IF](/qb64wiki/index.php/IF "IF") K$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Found"; found; "TTF files,"; OK; "can use Monospace," [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Ted Weissgerber


| ``` Found 106 TTF files, 13 can use Monospace.  ``` |
| --- |




---


*Example 2:* Using a \_FREEFONT sub-procedure.





| ``` fontpath$ = [ENVIRON$](/qb64wiki/index.php/ENVIRON$ "ENVIRON$")("SYSTEMROOT") + "\fonts\lucon.ttf" style$ = "MONOSPACE, ITALIC, BOLD" fontsize% = 20  [_FONT](/qb64wiki/index.php/FONT "FONT") 16 [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This is the QB64 default _FONT 16! To change, press any key!" [DO](/qb64wiki/index.php/DO "DO"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") ClearFont 'call will not free anything if font& = 0  font& = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")(fontpath$, fontsize%, style$) [IF](/qb64wiki/index.php/IF "IF") font > 0 [THEN](/qb64wiki/index.php/THEN "THEN") [_FONT](/qb64wiki/index.php/FONT "FONT") font& 'NEVER try to load a font value less than 1! [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "A NEW _FONT style. To change to default, press any key!" [DO](/qb64wiki/index.php/DO "DO"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") ClearFont 'call will free a valid font handle from memory  [END](/qb64wiki/index.php/END "END")  ClearFont: [IF](/qb64wiki/index.php/IF "IF") font& > 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [_FONT](/qb64wiki/index.php/FONT "FONT") 16 'change used font to the QB64 8x16 default font     _FREEFONT font&     [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "The previous font was freed with _FREEFONT!" [ELSE](/qb64wiki/index.php/ELSE "ELSE"): [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_FREEFONT was not used!" [END IF](/qb64wiki/index.php/END_IF "END IF") [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


  




## See also


* [\_FONT](/qb64wiki/index.php/FONT "FONT")
* [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FREEFONT&oldid=8336>"




## Navigation menu








### Search





















