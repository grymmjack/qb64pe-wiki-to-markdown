


INKEY$ - QB64 Phoenix Edition Wiki








# INKEY$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The INKEY$ function returns user input as [ASCII](/qb64wiki/index.php/ASCII "ASCII") [STRING](/qb64wiki/index.php/STRING "STRING") character(s) from the keyboard buffer.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Two Byte Combinations](#Two_Byte_Combinations) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*keypress$* = INKEY$
  




## Description


* Returns [ASCII](/qb64wiki/index.php/ASCII "ASCII") character string values in upper or lower cases. See: [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$") and [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$")
* Returns "" if no key has been pressed since the last keyboard read.
* Some control keys cannot be read by INKEY$ or will return 2 byte [ASCII](/qb64wiki/index.php/ASCII "ASCII") codes.
* INKEY$ can also be used to clear a [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") key press or the keyboard buffer in a loop.
* Assign the INKEY$ return to a string variable to save the key entry.
* [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , , 1 displays the INKEY$ cursor. Use [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , , 0 to turn it off.
* To receive input from a [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") window, use [\_CINP](/qb64wiki/index.php/CINP "CINP").
* Returns can be evaluated as certain [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters or codes.




| ``` '                                **ASCII Keyboard Codes** ' '  **Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause** '   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    - '  **`~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -** '  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45 '  *96 49  50  51  52  53  54  55  56  57  48 45 61* '  **Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  +**  '   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43 '  *113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57*  '  **CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►** '    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  **E** '  *97 115 100 102 103 104 106 107 108  59  39                       52   53   54*  **n** '  **Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t** '    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  **e** '  *122 120  99 118  98 110 109  44  46  47                          49   50   51*  **r** '  **Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del**  '   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13 '                                                                     *48        46* ' '   ***Italics* = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)** '  ``` |
| --- |


  




## Two Byte Combinations


* INKEY$ 2 byte combinations always begin with [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0). [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)") will always read the first byte code as zero.
* Read the second byte code using: **code2 = ASC(press$, 2)**


  




**[Two Byte Ctrl, Alt and Shift + Function key combinations](/qb64wiki/index.php/ASCII#Two_Byte_Codes "ASCII")**


| ```                     **Two Byte Characters        Key                 CHR$(0) + "?"**                       CHR$(0) + CHR$(16-50)      [Alt] + letter                     CHR$(0) + CHR$(59)         [F1]                 ";"                     CHR$(0) + CHR$(60)         [F2]                 "<"                     CHR$(0) + CHR$(61)         [F3]                 "="                     CHR$(0) + CHR$(62)         [F4]                 ">"                     CHR$(0) + CHR$(63)         [F5]                 "?"                     CHR$(0) + CHR$(64)         [F6]                 "@"                     CHR$(0) + CHR$(65)         [F7]                 "A"                     CHR$(0) + CHR$(66)         [F8]                 "B"                     CHR$(0) + CHR$(67)         [F9]                 "C"                     CHR$(0) + CHR$(68)         [F10]                "D"                     CHR$(0) + CHR$(71)         [Home]               "G"                     CHR$(0) + CHR$(72)         [↑] Arrow            "H"                     CHR$(0) + CHR$(73)         [Page Up]            "I"                     CHR$(0) + CHR$(75)         [←] Arrow            "K"                     CHR$(0) + CHR$(76)         [5 NumberPad]        "L" (NumLock off in QB64)                     CHR$(0) + CHR$(77)         [→] Arrow            "M"                     CHR$(0) + CHR$(79)         [End]                "O"                     CHR$(0) + CHR$(80)         [↓] Arrow            "P"                     CHR$(0) + CHR$(81)         [Page Down]          "Q"                     CHR$(0) + CHR$(82)         [Insert]             "R"                     CHR$(0) + CHR$(83)         [Delete]             "S"                     CHR$(0) + CHR$(84-93)      [Shift] + F1-10                     CHR$(0) + CHR$(94-103)     [Ctrl] + F1-10                     CHR$(0) + CHR$(104-113)    [Alt] + F1-10                     CHR$(0) + CHR$(114-119)    [Ctrl] + keypad                     CHR$(0) + CHR$(120-129)    [Alt] + number                     CHR$(0) + CHR$(130 or 131) [Alt] + _/- or +/=   "é" or "â"                     CHR$(0) + CHR$(133)        [F11]                "à"                     CHR$(0) + CHR$(134)        [F12]                "å"                     CHR$(0) + CHR$(135)        [Shift] + [F11]      "ç"                     CHR$(0) + CHR$(136)        [Shift] + [F12]      "ê"                     CHR$(0) + CHR$(137)        [Ctrl] + [F11]       "ë"                     CHR$(0) + CHR$(138)        [Ctrl] + [F12]       "è"                     CHR$(0) + CHR$(139)        [Alt] + [F11]        "ï"                     CHR$(0) + CHR$(140)        [Alt] + [F12]        "î"  ``` |
| --- |


In **QB64**, [CVI](/qb64wiki/index.php/CVI "CVI") can be used to get the [\_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN") 2-byte code value. Example: **status = \_KEYDOWN(CVI(CHR$(0) + "P"))**
  




## Examples


*Example 1:* Clearing the keyboard buffer after [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") delays for later [INPUT](/qb64wiki/index.php/INPUT "INPUT").





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press any keyboard typing key to end SLEEP" [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") [DO](/qb64wiki/index.php/DO "DO"): K$ = INKEY$: [PRINT](/qb64wiki/index.php/PRINT "PRINT") K$: [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") K$ = ""  ``` |
| --- |


*Explanation:* [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") key presses will be kept in the keyboard buffer and may be added into an [INPUT](/qb64wiki/index.php/INPUT "INPUT") later.
  

*Example 2:* Entering a Ctrl + letter keypress combination will print [ASCII](/qb64wiki/index.php/ASCII "ASCII") Control characters 1 to 26. .





| ``` DO     K$ = INKEY$     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") K$ <> "" [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") K$; " "; [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") K$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) 'Esc key exit  ``` |
| --- |


*Note:* The above code will print Esc arrow, Backspace symbol, and 2 byte characters led by CHR$(0) in addition to normal keys.
  

*Example 3:* Use [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(INKEY$) in a keyboard read loop looking for uppercase "Y" or "N" user inputs to avoid multiple IF statements.





| ``` [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Do you want to continue? (Y/N): ";  'semicolon saves position for user entry   [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP"): K$ = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(INKEY$) 'change any user key press to uppercase   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") K$ = "Y" [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") K$ = "N"   [PRINT](/qb64wiki/index.php/PRINT "PRINT") K$  'print valid user entry   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") K$ = "N" [THEN](/qb64wiki/index.php/THEN "THEN") [END](/qb64wiki/index.php/END "END") [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


  

*Example 4:* Getting just number values entered by a user in an INKEY$ input loop.





| ``` [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Enter a number value: "; [DO](/qb64wiki/index.php/DO "DO"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")   K$ = INKEY$   [IF](/qb64wiki/index.php/IF "IF") K$ >= [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(48) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") K$ <= [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(57) [THEN](/qb64wiki/index.php/THEN "THEN") entry$ = entry$ + K$ ' numbers only   L = [LEN](/qb64wiki/index.php/LEN "LEN")(entry$) ' check entry length for possible backspace   [IF](/qb64wiki/index.php/IF "IF") K$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(46) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") flag = 0 [THEN](/qb64wiki/index.php/THEN "THEN") entry$ = entry$ + K$: flag = 1: mark = L ' decimal point   [IF](/qb64wiki/index.php/IF "IF") K$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(8) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") L > 0 [THEN](/qb64wiki/index.php/THEN "THEN") ' backspace pressed and entry has a length     entry$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(entry$, 1, L - 1) ' remove one character from entry$     [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")(entry$) < mark [THEN](/qb64wiki/index.php/THEN "THEN") flag = 0 ' allow decimal point entry if other was removed.     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN"), [POS](/qb64wiki/index.php/POS "POS")(0) - 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1); ' remove end character from screen   [END IF](/qb64wiki/index.php/END_IF "END IF")   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 32: [PRINT](/qb64wiki/index.php/PRINT "PRINT") entry$; ' display entry to user (semicolon required for correct [POS](/qb64wiki/index.php/POS "POS")) [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") K$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(13) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") L > 0 'assures something is entered  ``` |
| --- |


*Explanation:* [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") waits for a keypress. It also allows background programs to share the processor and it leaves the keypress in the buffer for INKEY$. Keyboard string number characters range from [ASCII](/qb64wiki/index.php/ASCII "ASCII") codes 48 to 57. Any other entry is ignored by the IF statement. A decimal point (code 46) entry is allowed once in the input. The flag value stops further decimal point additions. Backspacing (code 8) is also allowed if the entry has at least one character. The cursor column returned by [POS](/qb64wiki/index.php/POS "POS")(0) reverts too after the end of the entry when printed each loop. The loop exits when [Enter] (code 13) is pressed and the entry has a length.
  

*Example 5:* Using arrow keys to move a text character. A change from a previous position tells program when to PRINT:





| ``` movey = 1: movex = 1 'text coordinates can never be 0 at$ = "@"  'text sprite could be almost any ASCII character [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") movey, movex: [PRINT](/qb64wiki/index.php/PRINT "PRINT") at$; DO     px = movex: py = movey 'previous positions     B$ = INKEY$     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") B$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(72) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") movey > 1 [THEN](/qb64wiki/index.php/THEN "THEN") movey = movey - 1 'rows 1 to 23 only     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") B$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(80) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") movey < 23 [THEN](/qb64wiki/index.php/THEN "THEN") movey = movey + 1     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") B$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(75) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") movex > 1 [THEN](/qb64wiki/index.php/THEN "THEN") movex = movex - 1 'columns 1 to 80 only     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") B$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(0) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(77) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") movex < 80 [THEN](/qb64wiki/index.php/THEN "THEN") movex = movex + 1      [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") px <> movex [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") py <> movey [THEN](/qb64wiki/index.php/THEN "THEN") 'only changes when needed         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") py, px: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1); 'erase old sprite         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") movey, movex: [PRINT](/qb64wiki/index.php/PRINT "PRINT") at$; 'show new position     [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") B$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) 'ESCape key exit [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  

*Example 6:* Using INKEY$ with the arrow or WASD keys to move the QB64 bee image sprite with [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE"):





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") image [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") [DIM](/qb64wiki/index.php/DIM "DIM") x [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") y [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") Keypress [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING")  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32)  x = 0 y = 0 image = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("QB64bee.png") 'Here I actually used the QB64 icon  DO   [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (x, y), image   DO     Keypress = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(INKEY$)     ' ***** The following line detects the arrow keys *****     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LEN](/qb64wiki/index.php/LEN "LEN")(Keypress) > 1 [THEN](/qb64wiki/index.php/THEN "THEN") Keypress = [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(Keypress, 1)   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") Keypress > ""    [CLS](/qb64wiki/index.php/CLS "CLS") ' blank screen after valid key press to avoid smearing image on page    [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") Keypress     [CASE](/qb64wiki/index.php/CASE "CASE") "W", "H": y = y - 10 'Up     [CASE](/qb64wiki/index.php/CASE "CASE") "A", "K": x = x - 10 'Left     [CASE](/qb64wiki/index.php/CASE "CASE") "S", "P": y = y + 10 'Down     [CASE](/qb64wiki/index.php/CASE "CASE") "D", "M": x = x + 10 'Right     [CASE](/qb64wiki/index.php/CASE "CASE") "Q", [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27): [END](/qb64wiki/index.php/END "END") 'Q or Esc Ends prog.   [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")   [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (x, y), image [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


Adapted from code by Daniel
*Note:* The image can be placed off of the screen without error. The image moves 10 pixels to move faster. [CLS](/qb64wiki/index.php/CLS "CLS") eliminates any background.
  

*Example 7:* Creating upper [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters in a QB program using **Alt +** three number keys:





| ``` DO     A$ = "": [WHILE](/qb64wiki/index.php/WHILE "WHILE") A$ = "": A$ = INKEY$: [WEND](/qb64wiki/index.php/WEND "WEND")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LEN](/qb64wiki/index.php/LEN "LEN")(A$) = 2 [THEN](/qb64wiki/index.php/THEN "THEN") '2 byte INKEY$ return         B$ = [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(A$, 1)  'read second byte         b% = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(B$)        'read second byte code         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") b% > 119 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") b% < 130 [THEN](/qb64wiki/index.php/THEN "THEN") ' Alt + number codes only            C% = b% - 119  ' convert to actual number            [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") C% > 9 [THEN](/qb64wiki/index.php/THEN "THEN") C% = 0            num$ = num$ + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(C%))         [END IF](/qb64wiki/index.php/END_IF "END IF")     [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [LEN](/qb64wiki/index.php/LEN "LEN")(num$) = 3  ' 3 digit codes only  [PRINT](/qb64wiki/index.php/PRINT "PRINT") num$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([VAL](/qb64wiki/index.php/VAL "VAL")(num$)  ``` |
| --- |


Code by Ted Weissgerber


| ```  155 ¢  ``` |
| --- |


*Explanation:* Hold down Alt key and press 3 keyboard code number keys. **Number pad keys may not work.** Note that INKEY$ cannot read Alt, Ctrl or Shift key presses without a key combination and the return is CHR$(0) + CHR$(code).
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1229)
* [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT"), [\_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN"), [\_MAPUNICODE](/qb64wiki/index.php/MAPUNICODE "MAPUNICODE")
* [\_KEYCLEAR](/qb64wiki/index.php/KEYCLEAR "KEYCLEAR")
* [INPUT](/qb64wiki/index.php/INPUT "INPUT"), [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT")
* [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$"), [INP](/qb64wiki/index.php/INP "INP")
* [CHR$](/qb64wiki/index.php/CHR$ "CHR$"), [ASCII](/qb64wiki/index.php/ASCII "ASCII")
* [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)"), [Scancodes](/qb64wiki/index.php/Scancodes "Scancodes") (keyboard)
* [Windows hot keys](/qb64wiki/index.php/Windows_Libraries#Hot_Keys_(maximize) "Windows Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INKEY$&oldid=8905>"




## Navigation menu








### Search





















