


\_LOADFONT - QB64 Phoenix Edition Wiki








# \_LOADFONT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_LOADFONT function loads a FreeType supported font file in a specific size and style and returns a [LONG](/qb64wiki/index.php/LONG "LONG") font handle.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*handle&* = \_LOADFONT(*fontFileName$*, *size&*[, "{MONOSPACE|, BOLD|, ITALIC|, UNDERLINE|, UNICODE|, DONTBLEND|, MEMORY|, AUTOMONO}"][, *fontIndex&*])
  




## Description


* The assigned [LONG](/qb64wiki/index.php/LONG "LONG") font *handle&* variable return value designates a font style to be used somewhere in a program. Valid handle values are greater than 0 (***handle&* > 0**).
* *fontFileName$* is the filename of a font. It can include the path to the font file. **TTF, TTC, OTF, FNT, FON, PCF and BDF** font file formats are supported. Best practice is to include font files with a program.
* If no path is specified for *fontFileName$* and the font file isn't in the same folder as the resulting binary, QB64 attempts to load from the default *%SystemRoot%\Fonts* path. Similar known locations are searched in other operating systems.
* *size&* is the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") height of the font. If the size is too large or small an [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.
* Optional comma separated *style* parameter(s) used are literal [STRINGs](/qb64wiki/index.php/STRING "STRING") (in quotes) or can be contained in variable(s).
	+ **"MONOSPACE"** loads a font with all characters occupying the same width. Results may be too spaced out for fonts that aren't designed for monospace use.
	+ **"BOLD", "ITALIC"** or **"UNDERLINE"** create bold, italic or underlined fonts when available in font.
		- (valid for QB64 versions prior to 1.000).
		- For **QB64 1.000 or later**, you must specify the proper file name according to the desired attributes. For example, Courier New is in font **cour.ttf** while Courier New Bold is in font **courbd.ttf**, as shipped with Windows.
	+ **"UNICODE"** loads Unicode fonts such as *cyberbit.ttf* which is included in the QB64 downloads.
	+ **"DONTBLEND"** turns off [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") blending of fonts. This can also be done with the [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") statement.
	+ **"MEMORY"** will treat *fontFileName$* as a memory buffer containing the font file instead of a file name.
	+ **"AUTOMONO"** will automatically detect monospace fonts and set the **"MONOSPACE"** flag if *fontFileName$* is monospaced.


* You can pass different font styles using different predefined [STRING](/qb64wiki/index.php/STRING "STRING") variable lists. You **can** include an empty style string.

* *fontIndex&* is the index of a font in a font collection (usually **.ttc** files). When this is negative the first font from the collection is loaded.
* **Always check that font handle values are greater than 0 (***handle&* > 0**) before using them or [illegal function errors](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") may occur.**
* **NOTE: SCREEN 0 can only use ONE font on a screen page. Thus a style like underline would affect the entire page.**
* Font sizes can be found using the [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT") function. Font *size*s can also affect [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") sizes.
* [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH") can only measure monospaced fonts. **"MONOSPACE" can be used to load a variable width font as a monospace font.**
* [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH") can measure the width of a string of text in **graphics modes only**. Use one character to get the font's width.


  




**Font Handles**
* Multiple fonts will require multiple font variable handles unless used and freed consecutively.
* Font handles with values greater than 0 that are **no longer used** should be freed using [\_FREEFONT](/qb64wiki/index.php/FREEFONT "FREEFONT").
* **Predefined QB64** font handle numbers can be substituted before freeing a font handle:
	+ **\_FONT 8**  - default font for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 1, 2, 7, 8 or 13
	+ **\_FONT 14** - default font for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 9 or 10
	+ **\_FONT 16** - default font for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 ([WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") 80, 25 text only), 11 or 12
	+ **\_FONT 9, 15** and **17** are the double width versions of 8, 14 and 16 respectively in text **SCREEN 0 only**.
* Once the font is changed to a predefined value, the font handle value can be freed using [\_FREEFONT](/qb64wiki/index.php/FREEFONT "FREEFONT") for another font type.
* Font handle values of -1 (load failure) **do not** need to be freed. **An [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur if you try to free invalid handles.**


  




**Font File Specs**
* Windows users should find **TTF** font files in the C:\WINDOWS\FONTS folder, but don't depend on unusual ones being there.
* **Check the font file name. The name in the "viewer" is not necessarily the file's name. Use the name in properties (right click a font listed and choose Properties in the contextual menu)**
* If a program is on a different drive than Windows, [ENVIRON$](/qb64wiki/index.php/ENVIRON$ "ENVIRON$")("SYSTEMROOT") will return the path to the "WINDOWS" folder. Normally "C:\WINDOWS". Then add the "\FONTS\" folder and the font **.TTF** filename to the path [STRING](/qb64wiki/index.php/STRING "STRING").


## Availability


* [![v1.3](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v1.3")

**v1.3**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


* The capability to load from *memory* and loading a font from a *font collection* was introduced in **QB64-PE** *v3.7.0*.
* The capability to auto-detect monospaced fonts was introduced in **QB64-PE** *v3.13.1*.


## Examples


Example 1
You need to know that if you are in a text mode (such as SCREEN 0 - the default) then you will only be able to use mono-spaced (fixed width) fonts.


| ``` rootpath$ = [ENVIRON$](/qb64wiki/index.php/ENVIRON$ "ENVIRON$")("SYSTEMROOT") 'normally "C:\WINDOWS" fontfile$ = rootpath$ + "\Fonts\cour.ttf" 'TTF file in Windows style$ = "monospace" 'font style is not case sensitive f& = _LOADFONT(fontfile$, 30, style$) [_FONT](/qb64wiki/index.php/FONT "FONT") f& [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello!"  ``` |
| --- |




| ``` Hello!  ``` |
| --- |


*Note:* 30 means each row of text (including vertical spacing) will be exactly 30 pixels high. This may make some program screens larger. If you don't want a style listed just use style$ = "" if using a [STRING](/qb64wiki/index.php/STRING "STRING") variable for different calls.





---


Example 2
In a 32-bit graphics mode you can alpha blend onto the background.


| ``` i& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") i& [COLOR](/qb64wiki/index.php/COLOR "COLOR") &HC0FFFF00, &H200000FF f& = _LOADFONT("C:\Windows\Fonts\times.ttf", 25) 'normal style [_FONT](/qb64wiki/index.php/FONT "FONT") f& [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello!"  ``` |
| --- |




| ``` Hello!  ``` |
| --- |


*Note:* You can load a fixed width font file without using the "monospace" option and it will be treated as variable width. This can be useful because LOCATE treats the horizontal position as an offset in pixels for variable width fonts.


---


Example 3
Loading a [Unicode](/qb64wiki/index.php/Unicode "Unicode") font, *cyberbit.ttf*, which was downloaded with QB64.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  [DECLARE](/qb64wiki/index.php/DECLARE "DECLARE") [CUSTOMTYPE](/qb64wiki/index.php/CUSTOMTYPE "CUSTOMTYPE") [LIBRARY](/qb64wiki/index.php/LIBRARY "LIBRARY") 'Directory Information using KERNEL32 provided by Dav     [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") GetModuleFileNameA& ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") hModule [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), lpFileName [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") nSize [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") GetModuleFileNameW& ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") hModule [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), lpFileName [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") nSize [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")) [END DECLARE](/qb64wiki/index.php/END_DECLARE "END DECLARE")  '=== SHOW CURRENT PROGRAM FileName$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(512)  Result = GetModuleFileNameA(0, FileName$, [LEN](/qb64wiki/index.php/LEN "LEN")(FileName$)) [IF](/qb64wiki/index.php/IF "IF") Result [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "CURRENT PROGRAM (ASCII): "; [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(FileName$, Result)  'load a unicode font f = _LOADFONT("cyberbit.ttf", 24, "UNICODE") [_FONT](/qb64wiki/index.php/FONT "FONT") f Result = GetModuleFileNameW(0, FileName$, [LEN](/qb64wiki/index.php/LEN "LEN")(FileName$) \ 2) [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 1 [PRINT](/qb64wiki/index.php/PRINT "PRINT") QuickCP437toUTF32$("CURRENT PROGRAM (UTF): ") + QuickUTF16toUTF32$([LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(FileName$, Result * 2)) [_FONT](/qb64wiki/index.php/FONT "FONT") 16 'restore CP437 font  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") QuickCP437toUTF32$ (a$)     b$ = [STRING$](/qb64wiki/index.php/STRING$ "STRING$")([LEN](/qb64wiki/index.php/LEN "LEN")(a$) * 4, 0)     [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(a$)         [ASC](/qb64wiki/index.php/ASC "ASC")(b$, i * 4 - 3) = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(a$, i)     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     QuickCP437toUTF32$ = b$ [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") QuickUTF16toUTF32$ (a$)     b$ = [STRING$](/qb64wiki/index.php/STRING$ "STRING$")([LEN](/qb64wiki/index.php/LEN "LEN")(a$) * 2, 0)     [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(a$) \ 2         [ASC](/qb64wiki/index.php/ASC "ASC")(b$, i * 4 - 3) = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(a$, i * 2 - 1)         [ASC](/qb64wiki/index.php/ASC "ASC")(b$, i * 4 - 2) = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(a$, i * 2)     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     QuickUTF16toUTF32$ = b$ [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


  




## See also


* [\_FONT](/qb64wiki/index.php/FONT "FONT"), [\_FONT (function)](/qb64wiki/index.php/FONT_(function) "FONT (function)")
* [\_FREEFONT](/qb64wiki/index.php/FREEFONT "FREEFONT")
* [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING"), [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH")
* [\_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE"), [\_PRINTMODE (function)](/qb64wiki/index.php/PRINTMODE_(function) "PRINTMODE (function)")
* [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT"), [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics") (Demo)
* [Windows Font Dialog Box](/qb64wiki/index.php/Windows_Libraries#Font_Dialog_Box "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LOADFONT&oldid=8869>"




## Navigation menu








### Search





















