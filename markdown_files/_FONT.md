


\_FONT - QB64 Phoenix Edition Wiki








# \_FONT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_FONT statement sets the current [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT") function font handle to be used by [PRINT](/qb64wiki/index.php/PRINT "PRINT").


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_FONT *fontHandle&*[, *imageHandle&*]
  




## Parameters


* *fontHandle&* is the handle retrieved from [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT") function, the [\_FONT](/qb64wiki/index.php/FONT_(function) "FONT (function)") function, or a predefined handle.
* If the image handle is omitted the current image [\_DESTination](/qb64wiki/index.php/DEST "DEST") is used. Zero can designate the current program [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN").


  




## Description


* Predefined **QB64** font handle numbers can be used before freeing a font:
	+ **\_FONT 8**  - default font for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 1, 2, 7, 8 or 13
	+ **\_FONT 14** - default font for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 9 or 10
	+ **\_FONT 16** - default font for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 ([WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") 80, 25 text only), 11 or 12
	+ **\_FONT 9, 15** and **17** are the double width versions of 8, 14 and 16 respectively in text **SCREEN 0 only**.
* [Unicode](/qb64wiki/index.php/Unicode "Unicode") characters can be assigned to a monospace font that contains those unicode characters using the [\_MAPUNICODE](/qb64wiki/index.php/MAPUNICODE "MAPUNICODE") TO [ASCII](/qb64wiki/index.php/ASCII "ASCII") mapping statement. The optional **IME cyberbit.ttf** font included with QB64 can also be used.
* Can alpha blend a font with a background screen created by [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") in 32 bit color.
* **Check for valid handle values greater than 0 before using or freeing font handles.**
* Free **unused** font handles with [\_FREEFONT](/qb64wiki/index.php/FREEFONT "FREEFONT"). Freeing invalid handles will create an ["illegal function call"](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error.
* **NOTE: SCREEN 0 can only use one font type and style per viewed SCREEN page. Font size may also affect the window size.**


  




## Examples


*Example:* Previewing a font in SCREEN 0. A different true type font can be substituted below.





| ``` fontpath$ = [ENVIRON$](/qb64wiki/index.php/ENVIRON$ "ENVIRON$")("SYSTEMROOT") + "\fonts\lucon.ttf" 'Find Windows Folder Path. [DO](/qb64wiki/index.php/DO "DO"): [CLS](/qb64wiki/index.php/CLS "CLS")     [DO](/qb64wiki/index.php/DO "DO")         style$ = "MONOSPACE"         [PRINT](/qb64wiki/index.php/PRINT "PRINT")         [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter A FONT Size 8 TO 25: ", fontsize%     [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") fontsize% > 7 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") fontsize% < 26     [DO](/qb64wiki/index.php/DO "DO")         [PRINT](/qb64wiki/index.php/PRINT "PRINT")         [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter (0) for REGULAR OR (1) for ITALIC FONT: ", italic%     [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") italic% = 0 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") italic% = 1     [DO](/qb64wiki/index.php/DO "DO")         [PRINT](/qb64wiki/index.php/PRINT "PRINT")         [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter (0) for REGULAR OR (1) for BOLD FONT: ", bold%     [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") italic% = 0 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") italic% = 1     [IF](/qb64wiki/index.php/IF "IF") italic% = 1 [THEN](/qb64wiki/index.php/THEN "THEN") style$ = style$ + ", ITALIC"     [IF](/qb64wiki/index.php/IF "IF") bold% = 1 [THEN](/qb64wiki/index.php/THEN "THEN") style$ = style$ + ", BOLD"      [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") ClearFont     font& = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")(fontpath$, fontsize%, style$)     _FONT font&     [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This is your LUCON font! Want to try another STYLE?(Y/N): ";     [DO](/qb64wiki/index.php/DO "DO"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP"): K$ = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")([INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")): [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") K$ = "Y" [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") K$ = "N" [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") K$ = "N" [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") ClearFont  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This is the QB64 default _FONT 16!" [END](/qb64wiki/index.php/END "END")  ClearFont: [IF](/qb64wiki/index.php/IF "IF") font& > 0 [THEN](/qb64wiki/index.php/THEN "THEN")     _FONT 16 'select inbuilt 8x16 default font     [_FREEFONT](/qb64wiki/index.php/FREEFONT "FREEFONT") font& [END IF](/qb64wiki/index.php/END_IF "END IF") [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


**NOTE:** [ENVIRON$](/qb64wiki/index.php/ENVIRON$ "ENVIRON$")("SYSTEMROOT") returns a string value of: "C:\WINDOWS". Add the "\FONTS\" folder and the **.TTF** font file name.


  




## See also


* [\_FONT (function)](/qb64wiki/index.php/FONT_(function) "FONT (function)")
* [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT"), [\_FREEFONT](/qb64wiki/index.php/FREEFONT "FREEFONT")
* [Unicode](/qb64wiki/index.php/Unicode "Unicode"), [\_MAPUNICODE](/qb64wiki/index.php/MAPUNICODE "MAPUNICODE")
* [Windows Font Dialog Box](/qb64wiki/index.php/Windows_Libraries#Font_Dialog_Box "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FONT&oldid=8334>"




## Navigation menu








### Search





















