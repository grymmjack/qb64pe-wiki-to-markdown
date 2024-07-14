


\_CINP - QB64 Phoenix Edition Wiki








# \_CINP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CINP function returns keyboard key press codes from a [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") window. Windows-only.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*keycode&* = \_CINP
  




## Description


* Return values are the same as the ones for [INP](/qb64wiki/index.php/INP "INP") when used to read keyboard input. See table below.
* Negative values returned indicate that a key was released or a lock function key has been turned off.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**




| ``` '                            **Extended Keyboard Press Scancodes** ' ' **Esc  F1 F2 F3 F4 F5 F6 F7 F8 F9 F10  F11 F12   SysReq ScrL Pause** '  1   59 60 61 62 63 64 65 66 67 68   87  88     0     70    29 ' **`~  1! 2@ 3# 4$ 5% 6^ 7& 8* 9( 0) -_ =+ BkSpc  Insert Home PgUp   NumL   /     *    -** '  41 2  3  4  5  6  7  8  9  10 11 12 13  14     82    71    73     69    53    55   74 ' **Tab  Q  W  E  R  T  Y  U  I  O  P  [{ ]} \|    Delete End  PgDn   7/Home 8/▲  9/PU  +**  '  15  16 17 18 19 20 21 22 23 24 25 26 27 43     83    79    81     71    72    73   78 ' **CapL  A  S  D  F  G  H  J  K  L  ;: '"  Enter                     4/◄-   5    6/-►  E** '  58   30 31 32 33 34 35 36 37 38 39 40   28                        75    76    77   **n** ' **Shift  Z  X  C  V  B  N  M  ,< .> /?    Shift         ▲           1/End  2/▼  3/PD  t** '  42    44 45 46 47 48 49 50 51 52 53     54           72           79    80    81   **e** ' **Ctrl Win Alt    Spacebar    Alt Win Menu Ctrl     ◄-  ▼   -►      0/Insert    ./Del r** '  29  91  56        57       56  92   93  29       75  80  77       82          83   28 '  ``` |
| --- |


  




## Examples


*Example 1:* Reading individual key strokes from a console window (Windows).





| ``` [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"):[ONLY](/qb64wiki/index.php/ONLY "ONLY") [_DEST](/qb64wiki/index.php/DEST "DEST") [_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE"): [_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") [_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press any key, and I'll give you the scan code for it.  <ESC> quits the demo." [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [DO](/qb64wiki/index.php/DO "DO")     x = [_CONSOLEINPUT](/qb64wiki/index.php/CONSOLEINPUT "CONSOLEINPUT")     [IF](/qb64wiki/index.php/IF "IF") x = 1 [THEN](/qb64wiki/index.php/THEN "THEN") 'read only keyboard input ( = 1)         c = _CINP         [PRINT](/qb64wiki/index.php/PRINT "PRINT") c;     [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") c = 1 [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE"), [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")
* [\_CONSOLEINPUT](/qb64wiki/index.php/CONSOLEINPUT "CONSOLEINPUT")
* [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"), [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY"), [\_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON"), [\_MOUSEWHEEL](/qb64wiki/index.php/MOUSEWHEEL "MOUSEWHEEL")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CINP&oldid=8277>"




## Navigation menu








### Search





















