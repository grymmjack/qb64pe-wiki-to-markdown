


\_KEYHIT - QB64 Phoenix Edition Wiki








# \_KEYHIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_KEYHIT function returns [ASCII](/qb64wiki/index.php/ASCII "ASCII") one and two byte, OpenGL Virtual Key and Unicode keyboard key press codes.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*keycode&* = \_KEYHIT
  




## Description


* Return values range up to &H40000000 so use a [LONG](/qb64wiki/index.php/LONG "LONG") or [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") variable type. See the [\_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN") code list:


* 0-255: [ASCII](/qb64wiki/index.php/ASCII "ASCII") values (Refer to [CP437](https://en.wikipedia.org/wiki/Code_page_437 "wikipedia:Code page 437")).
* 256-65535: [2-byte](/qb64wiki/index.php/ASCII#Two_Byte_Codes "ASCII") character codes : code = [CVI](/qb64wiki/index.php/CVI "CVI")([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(scancode)) (unaffected by SHIFT/ALT/CTRL modifiers).
* 65536-&H40000000: [QB64-specific Virtual Key codes](/qb64wiki/index.php/KEYDOWN "KEYDOWN") (designated with + for 100000 on keyboard below)
* **Negative** [LONG](/qb64wiki/index.php/LONG "LONG") values returned indicate that a key was released or a lock function key has been turned off.

* **Note: \_KEYHIT can only return one value at a time so use the [\_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN") keyhit value to find key combinations.**
* To receive input from a [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") window, use [\_CINP](/qb64wiki/index.php/CINP "CINP").




| ``` '                                **_KEYHIT Keyboard Codes** ' ' **Esc  F1    F2    F3    F4    F5    F6    F7    F8    F9    F10   F11   F12   Sys  ScL Pause** '  27 15104 15360 15616 15872 16128 16384 16640 16896 17152 17408 34048 34304 +316 +302 +019 ' **`~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins   Hme   PUp   NumL   /     *    -** ' 126 33  64  35  36  37  94  38  42  40  41 95 43   8   20992 18176 18688 +300   47    42   45 '  *96 49  50  51  52  53  54  55  56  57  48 45 61* ' **Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del   End   PDn   7Hme  8/▲   9PU   +**  '  9  81  87  69  82  84  89  85  73  79  80 123 125 124 21248 20224 20736 18176 18432 18688 43 '  *113 119 101 114 116 121 117 105 111 112  91  93  92                    55    56    57*  ' **CapL   A   S   D   F   G   H   J   K   L   ;:  '" Enter                   4/◄-   5    6/-►** ' +301  65  83  68  70  71  72  74  75  76  58  34  13                     19200 19456 19712  **E** '  *97 115 100 102 103 104 106 107 108  59  39                          52    53    54*    **n** ' **Shift   Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲           1End  2/▼   3PD   t** ' +304   90  88  67  86  66  78  77  60  62  63    +303       18432        20224 20480 20736  **e** '  *122 120  99 118  98 110 109  44  46  47                             49    50    51*    **r** ' **Ctrl   Win  Alt     Spacebar      Alt  Win  Menu  Ctrl   ◄-   ▼   -►      0Ins        .Del**  ' +306  +311 +308       32         +307 +312 +319  +305 19200 20480 19712  20992       21248 13 '                                                                       *48          46* ' '      **Lower value = LCase/NumLock On __________________ + = add 100000**   ``` |
| --- |


NOTE: The above commented table can be copied and pasted directly into the QB64 IDE
  




* >= &H40000000: [Unicode](/qb64wiki/index.php/Unicode "Unicode").

* Font **cyberbit.ttf**, included with QB64 (**version 0.92 and up**), is required to facilitate the **IME**(in Chinese settings) only. The 12.7 MB font is free for **non-commercial** use and is not loaded unless the user switches to the **Input Mode Editor**. Set to "UNICODE".


**[Setting up the Unicode Input Method Editor in Windows](http://www.fileformat.info/tip/microsoft/enter_unicode.htm)**
If you need help with IME support in **Vista** see the following article: [Setting up IME in Vista](http://blogs.msdn.com/b/michkap/archive/2006/07/20/671835.aspx)
* QB64 can use several Windows fonts when **cyberbit** is not present so it is not necessary to include with program packages.
* An **important difference** between [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") and \_KEYHIT is how they work when **CTRL, ALT** or **SHIFT** are used. INKEY$ returns a different code if you hold down CTRL, ALT or SHIFT before pressing F1 (for example). \_KEYHIT will return the same code regardless of which modifiers were used but you can check [\_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN") to see which modifying keys are being used.
* **Keyboards with an Alt Gr key note:** \_KEYHIT may return both Alt (100307) and Ctrl (100306) codes when AltGr key is pressed or released.


  




## Examples


*Example:* This routine will return the codes for any keyboard presses.





| ``` [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG") A-Z [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 8) [CLS](/qb64wiki/index.php/CLS "CLS") , 1 font = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("cyberbit.ttf", 24) unifont = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("cyberbit.ttf", 24, "UNICODE") [_FONT](/qb64wiki/index.php/FONT "FONT") font  [DO](/qb64wiki/index.php/DO "DO")   x = _KEYHIT   [IF](/qb64wiki/index.php/IF "IF") x [THEN](/qb64wiki/index.php/THEN "THEN")     [IF](/qb64wiki/index.php/IF "IF") x < 0 [THEN](/qb64wiki/index.php/THEN "THEN")  'negative value means key released       [COLOR](/qb64wiki/index.php/COLOR "COLOR") 2       [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Released ";       x = -x     [ELSE](/qb64wiki/index.php/ELSE "ELSE")       [COLOR](/qb64wiki/index.php/COLOR "COLOR") 10       [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Pressed ";   'positive value means key pressed     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF "IF") x < 256 [THEN](/qb64wiki/index.php/THEN "THEN")    'ASCII code values       [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ASCII "; x;       [IF](/qb64wiki/index.php/IF "IF") x >= 32 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x <= 255 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[" + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(x) + "]" [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF "IF") x >= 256 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x < 65536 [THEN](/qb64wiki/index.php/THEN "THEN") '2 byte key codes       [PRINT](/qb64wiki/index.php/PRINT "PRINT") "2-BYTE-COMBO "; x [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") 255; x \ 256;       x2 = x \ 256       [IF](/qb64wiki/index.php/IF "IF") x2 >= 32 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x2 <= 255 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[" + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(x2) + "]" [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF "IF") x >= 100000 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x < 200000 [THEN](/qb64wiki/index.php/THEN "THEN")      'QB84 Virtual Key codes       [PRINT](/qb64wiki/index.php/PRINT "PRINT") "SDL VK"; x - 100000       [END IF](/qb64wiki/index.php/END_IF "END IF")       [IF](/qb64wiki/index.php/IF "IF") x >= 200000 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x < [&H](/qb64wiki/index.php/%26H "&H")40000000 [THEN](/qb64wiki/index.php/THEN "THEN")             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "QB64 VK"; x - 200000     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF "IF") x >= [&H](/qb64wiki/index.php/%26H "&H")40000000 [THEN](/qb64wiki/index.php/THEN "THEN")              'Unicode values (IME Input mode)       [PRINT](/qb64wiki/index.php/PRINT "PRINT") "UNICODE "; x - [&H](/qb64wiki/index.php/%26H "&H")40000000; "0x" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(x - [&H](/qb64wiki/index.php/%26H "&H")40000000) + " ...";       cx = [POS](/qb64wiki/index.php/POS "POS")(1): cy = [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN")       [_FONT](/qb64wiki/index.php/FONT "FONT") unifont       [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") cy, cx       [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15       z$ = [MKL$](/qb64wiki/index.php/MKL$ "MKL$")(x - [&H](/qb64wiki/index.php/%26H "&H")40000000) + [MKL$](/qb64wiki/index.php/MKL$ "MKL$")(0)       [PRINT](/qb64wiki/index.php/PRINT "PRINT") z$ + z$ + z$;       [_FONT](/qb64wiki/index.php/FONT "FONT") font       [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") cy, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT")     [END IF](/qb64wiki/index.php/END_IF "END IF")   [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


Code by Galleon
  




## See also


* [\_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN"), [\_CINP](/qb64wiki/index.php/CINP "CINP")
* [\_MAPUNICODE](/qb64wiki/index.php/MAPUNICODE "MAPUNICODE"), [\_MAPUNICODE (function)](/qb64wiki/index.php/MAPUNICODE_(function) "MAPUNICODE (function)")
* [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"), [ASCII](/qb64wiki/index.php/ASCII "ASCII") (code table),
* [Unicode](/qb64wiki/index.php/Unicode "Unicode"), [Code Pages](/qb64wiki/index.php/Code_Pages "Code Pages") (by region)
* [INP](/qb64wiki/index.php/INP "INP")([&H60](/qb64wiki/index.php/%26H "&H")), [Scancodes](/qb64wiki/index.php/Scancodes "Scancodes")
* [ON KEY(n)](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)"), [KEY(n)](/qb64wiki/index.php/KEY(n) "KEY(n)"), [KEY n](/qb64wiki/index.php/KEY_n "KEY n")
* [Windows hot keys](/qb64wiki/index.php/Windows_Libraries#Hot_Keys_(maximize) "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=KEYHIT&oldid=8988>"




## Navigation menu








### Search





















