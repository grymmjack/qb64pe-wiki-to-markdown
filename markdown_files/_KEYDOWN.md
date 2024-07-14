


\_KEYDOWN - QB64 Phoenix Edition Wiki








# \_KEYDOWN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_KEYDOWN** function returns whether modifying keys like CTRL, ALT, SHIFT, and any other keys are pressed.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


return% = **\_KEYDOWN(***code&***)**
  




* The *return* value is -1 if a specified key is pressed or 0 if it was not pressed. It can be used to monitor key combinations.
* The POSITIVE [LONG](/qb64wiki/index.php/LONG "LONG") *code* value can be from any function key that needs to be monitored in a key press combination.
* Unicode references:


* 1) What is the glyph represented by that UNICODE value: [Unicode Format Info](http://www.fileformat.info/info/unicode/char/search.htm)
* 2) Which fonts support the characters I want to use: [Unicode Fonts](https://en.wikipedia.org/wiki/Unicode_typefaces#Comparison_of_fonts "wikipedia:Unicode typefaces")
* 3) What was the format again?: [Unicode Formats](http://www.birds-eye.net/definition/u/unicode.shtml)
* A UTF32 value is usually(but by no means always!) the same as a UTF16 value just with the top 2 bytes set to 0.

* An important difference between [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") and [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") is how they work when **CTRL, ALT** or **SHIFT** are used. [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") returns a different code if you hold down CTRL, ALT or SHIFT before pressing F1 (for example). [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") will return the same code regardless of which modifiers were used but you can check \_KEYDOWN to see which modifying keys are being used.
* **Keyboards with Alt Gr key:** [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") may return both Alt(100307) and Ctrl(100306) codes when key is pressed or released.
* **Linux with foreign keyboards:** [SHELL](/qb64wiki/index.php/SHELL "SHELL") [\_HIDE](/qb64wiki/index.php/HIDE "HIDE") "setxkbmap us" will setup a keyboard to read US [Scancodes](/qb64wiki/index.php/Scancodes "Scancodes").


  






| ```                        **The QB64 Virtual Key constant values used:**            **0-255**: [ASCII and Extended code](/qb64wiki/index.php/ASCII "ASCII") values (Refer to [CP437](https://en.wikipedia.org/wiki/Code_page_437 "wikipedia:Code page 437"))           **256-65535**: [ASCII 2-byte](/qb64wiki/index.php/ASCII#Two_Byte_Codes "ASCII") character codes (unaffected by SHIFT/ALT/CTRL modifiers)                   Use [CVI](/qb64wiki/index.php/CVI "CVI") to convert ASCII 2-byte codes to _KEYDOWN values.  '                                **_KEYDOWN Keyboard Values** ' ' **Esc  F1    F2    F3    F4    F5    F6    F7    F8    F9    F10   F11   F12   Sys  ScL Pause** '  27 15104 15360 15616 15872 16128 16384 16640 16896 17152 17408 34048 34304 +316 +302 +019 ' **`~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins   Hme   PUp   NumL   /     *    -** ' 126 33  64  35  36  37  94  38  42  40  41 95 43   8   20992 18176 18688 +300   47    42   45 '  *96 49  50  51  52  53  54  55  56  57  48 45 61* ' **Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del   End   PDn   7Hme  8/▲   9PU   +**  '  9  81  87  69  82  84  89  85  73  79  80 123 125 124 21248 20224 20736 18176 18432 18688 43 '  *113 119 101 114 116 121 117 105 111 112  91  93  92                    55    56    57*  ' **CapL   A   S   D   F   G   H   J   K   L   ;:  '" Enter                   4/◄-   5    6/-►** ' +301  65  83  68  70  71  72  74  75  76  58  34  13                     19200 19456 19712  **E** '  *97 115 100 102 103 104 106 107 108  59  39                          52    53    54*    **n** ' **Shift   Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲           1End  2/▼   3PD   t** ' +304   90  88  67  86  66  78  77  60  62  63    +303       18432        20224 20480 20736  **e** '  *122 120  99 118  98 110 109  44  46  47                             49    50    51*    **r** ' **Ctrl   Win  Alt     Spacebar      Alt  Win  Menu  Ctrl   ◄-   ▼   -►      0Ins        .Del**  ' +306  +311 +308       32         +307 +312 +319  +305 19200 20480 19712  20992       21248 13 '                                                                       *48          46* ' '       **Lower value = LCase/NumLock On __________________ + = add 100000**   ``` |
| --- |


NOTE: The above commented table can be copied and pasted directly into the QB64 IDE
  






| ```          **65536-&H40000000: QB64-specific Virtual Key codes:**                          CONST KEY_PAUSE& = 100019                         CONST KEY_NUMLOCK& = 100300                         CONST KEY_CAPSLOCK& = 100301                         CONST KEY_SCROLLOCK& = 100302                         CONST KEY_RSHIFT& = 100303                         CONST KEY_LSHIFT& = 100304                         CONST KEY_RCTRL& = 100305                         CONST KEY_LCTRL& = 100306                         CONST KEY_RALT& = 100307                         CONST KEY_LALT& = 100308                         CONST KEY_RMETA& = 100309 'Left 'Apple' key (macOS)                         CONST KEY_LMETA& = 100310 'Right 'Apple' key (macOS)                         CONST KEY_LSUPER& = 100311 'Left "Windows" key                         CONST KEY_RSUPER& = 100312 'Right "Windows"key                         CONST KEY_MODE& = 100313 '"AltGr" key                         CONST KEY_COMPOSE& = 100314                         CONST KEY_HELP& = 100315                         CONST KEY_PRINT& = 100316                         CONST KEY_SYSREQ& = 100317                         CONST KEY_BREAK& = 100318                         CONST KEY_MENU& = 100319                         CONST KEY_POWER& = 100320                         CONST KEY_EURO& = 100321                         CONST KEY_UNDO& = 100322                         CONST KEY_KP0& = 100256                         CONST KEY_KP1& = 100257                         CONST KEY_KP2& = 100258                         CONST KEY_KP3& = 100259                         CONST KEY_KP4& = 100260                         CONST KEY_KP5& = 100261                         CONST KEY_KP6& = 100262                         CONST KEY_KP7& = 100263                         CONST KEY_KP8& = 100264                         CONST KEY_KP9& = 100265                         CONST KEY_KP_PERIOD& = 100266                         CONST KEY_KP_DIVIDE& = 100267                         CONST KEY_KP_MULTIPLY& = 100268                         CONST KEY_KP_MINUS& = 100269                         CONST KEY_KP_PLUS& = 100270                         CONST KEY_KP_ENTER& = 100271                         CONST KEY_KP_INSERT& = 200000                         CONST KEY_KP_END& = 200001                         CONST KEY_KP_DOWN& = 200002                         CONST KEY_KP_PAGE_DOWN& = 200003                         CONST KEY_KP_LEFT& = 200004                         CONST KEY_KP_MIDDLE& = 200005                         CONST KEY_KP_RIGHT& = 200006                         CONST KEY_KP_HOME& = 200007                         CONST KEY_KP_UP& = 200008                         CONST KEY_KP_PAGE_UP& = 200009                         CONST KEY_KP_DELETE& = 200010                         CONST KEY_SCROLL_LOCK_MODE& = 200011                         CONST KEY_INSERT_MODE& = 200012           **&H40000000 up**: [Unicode](/qb64wiki/index.php/Unicode "Unicode") using the **cyberbit.ttf** font when available.                **Use [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") to find the key codes to be monitored by _KEYDOWN!**    ``` |
| --- |


*Example 1:* Comparing the \_KEYDOWN returns using [constant](/qb64wiki/index.php/CONST "CONST") values with 2 byte [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") returns.





| ``` [CONST](/qb64wiki/index.php/CONST "CONST") RSHIFT& = 100303 [CONST](/qb64wiki/index.php/CONST "CONST") LSHIFT& = 100304 [DO](/qb64wiki/index.php/DO "DO")     x = [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT")     [IF](/qb64wiki/index.php/IF "IF") x = [CVI](/qb64wiki/index.php/CVI "CVI")([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(59)) [THEN](/qb64wiki/index.php/THEN "THEN")         [IF](/qb64wiki/index.php/IF "IF") _KEYDOWN(LSHIFT&) [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") _KEYDOWN(RSHIFT&) [THEN](/qb64wiki/index.php/THEN "THEN")             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "KEYHIT: SHIFT + F1"         [ELSE](/qb64wiki/index.php/ELSE "ELSE")             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "KEYHIT: F1"         [END IF](/qb64wiki/index.php/END_IF "END IF")     [END IF](/qb64wiki/index.php/END_IF "END IF")     k$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")         'compare key press return values     [IF](/qb64wiki/index.php/IF "IF") k$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(59) [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "INKEY$: F1"     [IF](/qb64wiki/index.php/IF "IF") k$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(84) [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "INKEY$: SHIFT+F1" [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") k$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27)     'escape key exit  ``` |
| --- |


Code by Galleon
  

*Example 2:* How to calculate the \_KEYDOWN codes of the 2 byte INKEY$ arrow key codes using [CVI](/qb64wiki/index.php/CVI "CVI").





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  x = 320: y = 240 col = [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 0, 0) radius = 20  DO     [CLS](/qb64wiki/index.php/CLS "CLS")     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Use the arrow keys to move the circle."     [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (x, y), radius, col     [PAINT](/qb64wiki/index.php/PAINT "PAINT") (x, y), col      [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") _KEYDOWN([CVI](/qb64wiki/index.php/CVI "CVI")([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "P")) [THEN](/qb64wiki/index.php/THEN "THEN") y = y + 1   '_KEYDOWN(20480)     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") _KEYDOWN([CVI](/qb64wiki/index.php/CVI "CVI")([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "H")) [THEN](/qb64wiki/index.php/THEN "THEN") y = y - 1   '_KEYDOWN(18432)     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") _KEYDOWN([CVI](/qb64wiki/index.php/CVI "CVI")([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "K")) [THEN](/qb64wiki/index.php/THEN "THEN") x = x - 1   '_KEYDOWN(19200)     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") _KEYDOWN([CVI](/qb64wiki/index.php/CVI "CVI")([CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + "M")) [THEN](/qb64wiki/index.php/THEN "THEN") x = x + 1   '_KEYDOWN(19712)      [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 100 'limit to 100 frames per second [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


Code by Galleon
*Explanation:* When [CVI](/qb64wiki/index.php/CVI "CVI") is used with a 2 byte code, the code of the first character(0) is added to the second character code which is multiplied by 256. In the example, code zero is added to the [ASCII](/qb64wiki/index.php/ASCII "ASCII") code of "P" which is 80. CVI multiplies 80 \* 256 = 20480.
  




## See also


* [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT"), [Unicode](/qb64wiki/index.php/Unicode "Unicode"), [Code Pages](/qb64wiki/index.php/Code_Pages "Code Pages") (by region)
* [\_MAPUNICODE](/qb64wiki/index.php/MAPUNICODE "MAPUNICODE"), [\_MAPUNICODE (function)](/qb64wiki/index.php/MAPUNICODE_(function) "MAPUNICODE (function)")
* [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"), [ASCII](/qb64wiki/index.php/ASCII "ASCII"), [CVI](/qb64wiki/index.php/CVI "CVI")
* [INP](/qb64wiki/index.php/INP "INP")(&H60), [Scancodes](/qb64wiki/index.php/Scancodes "Scancodes")
* [ON KEY(n)](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)"), [KEY(n)](/qb64wiki/index.php/KEY(n) "KEY(n)"), [KEY n](/qb64wiki/index.php/KEY_n "KEY n")
* [Windows hot keys](/qb64wiki/index.php/Windows_Libraries#Hot_Keys_(maximize) "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=KEYDOWN&oldid=8987>"




## Navigation menu








### Search





















