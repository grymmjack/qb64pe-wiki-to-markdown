# INKEY$
> The INKEY$ function returns user input as ASCII STRING character(s) from the keyboard buffer.

## SYNTAX
`keypress$ = INKEY$`

## DESCRIPTION
* Returns ASCII character string values in upper or lower cases. See: UCASE$ and LCASE$
* Returns "" if no key has been pressed since the last keyboard read.
* Some control keys cannot be read by INKEY$ or will return 2 byte ASCII codes.
* INKEY$ can also be used to clear a [SLEEP](SLEEP.md) key press or the keyboard buffer in a loop.
* Assign the INKEY$ return to a string variable to save the key entry.
* [LOCATE](LOCATE.md) , , 1 displays the INKEY$ cursor. Use [LOCATE](LOCATE.md) , , 0 to turn it off.
* To receive input from a $[CONSOLE](CONSOLE.md) window, use [_CINP](_CINP.md) .
* Returns can be evaluated as certain ASCII characters or codes.


## EXAMPLES
> Example 1: Clearing the keyboard buffer after SLEEP delays for later INPUT .

```vb
'                                ASCII Keyboard Codes
'
'  Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
'  `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
'   96 49  50  51  52  53  54  55  56  57  48 45 61
'  Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + 
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
'     113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 
'  CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  E
'        97 115 100 102 103 104 106 107 108  59  39                       52   53   54  n
'  Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  e
'        122 120  99 118  98 110 109  44  46  47                          49   50   51  r
'  Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del 
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                         48        46
'
'      Italics = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)
'
```

> Example 2: Entering a Ctrl + letter keypress combination will print ASCII Control characters 1 to 26. .

```vb
'                                ASCII Keyboard Codes
'
'  Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
'  `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
'   96 49  50  51  52  53  54  55  56  57  48 45 61
'  Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + 
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
'     113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 
'  CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  E
'        97 115 100 102 103 104 106 107 108  59  39                       52   53   54  n
'  Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  e
'        122 120  99 118  98 110 109  44  46  47                          49   50   51  r
'  Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del 
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                         48        46
'
'      Italics = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)
'
```

> Example 3: Use UCASE$ (INKEY$) in a keyboard read loop looking for uppercase "Y" or "N" user inputs to avoid multiple IF statements.

```vb
'                                ASCII Keyboard Codes
'
'  Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
'  `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
'   96 49  50  51  52  53  54  55  56  57  48 45 61
'  Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + 
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
'     113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 
'  CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  E
'        97 115 100 102 103 104 106 107 108  59  39                       52   53   54  n
'  Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  e
'        122 120  99 118  98 110 109  44  46  47                          49   50   51  r
'  Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del 
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                         48        46
'
'      Italics = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)
'
```

> Example 4: Getting just number values entered by a user in an INKEY$ input loop.

```vb
'                                ASCII Keyboard Codes
'
'  Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
'  `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
'   96 49  50  51  52  53  54  55  56  57  48 45 61
'  Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + 
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
'     113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 
'  CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  E
'        97 115 100 102 103 104 106 107 108  59  39                       52   53   54  n
'  Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  e
'        122 120  99 118  98 110 109  44  46  47                          49   50   51  r
'  Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del 
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                         48        46
'
'      Italics = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)
'
```

> Example 5: Using arrow keys to move a text character. A change from a previous position tells program when to PRINT:

```vb
'                                ASCII Keyboard Codes
'
'  Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
'  `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
'   96 49  50  51  52  53  54  55  56  57  48 45 61
'  Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + 
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
'     113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 
'  CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  E
'        97 115 100 102 103 104 106 107 108  59  39                       52   53   54  n
'  Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  e
'        122 120  99 118  98 110 109  44  46  47                          49   50   51  r
'  Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del 
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                         48        46
'
'      Italics = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)
'
```

> Example 6: Using INKEY$ with the arrow or WASD keys to move the QB64 bee image sprite with _PUTIMAGE :

```vb
'                                ASCII Keyboard Codes
'
'  Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
'  `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
'   96 49  50  51  52  53  54  55  56  57  48 45 61
'  Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + 
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
'     113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 
'  CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  E
'        97 115 100 102 103 104 106 107 108  59  39                       52   53   54  n
'  Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  e
'        122 120  99 118  98 110 109  44  46  47                          49   50   51  r
'  Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del 
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                         48        46
'
'      Italics = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)
'
```

> Example 7: Creating upper ASCII characters in a QB program using Alt + three number keys:

```vb
'                                ASCII Keyboard Codes
'
'  Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
'  `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
'   96 49  50  51  52  53  54  55  56  57  48 45 61
'  Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + 
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
'     113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 
'  CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  E
'        97 115 100 102 103 104 106 107 108  59  39                       52   53   54  n
'  Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  e
'        122 120  99 118  98 110 109  44  46  47                          49   50   51  r
'  Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del 
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                         48        46
'
'      Italics = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)
'
```


```vb
'                                ASCII Keyboard Codes
'
'  Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
'  `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
'   96 49  50  51  52  53  54  55  56  57  48 45 61
'  Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + 
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
'     113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 
'  CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  E
'        97 115 100 102 103 104 106 107 108  59  39                       52   53   54  n
'  Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  e
'        122 120  99 118  98 110 109  44  46  47                          49   50   51  r
'  Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del 
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                         48        46
'
'      Italics = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)
'
```

* Featured in our "Keyword of the Day" series
* [_KEYHIT](_KEYHIT.md) , [_KEYDOWN](_KEYDOWN.md) , [_MAPUNICODE](_MAPUNICODE.md)
* [_KEYCLEAR](_KEYCLEAR.md)
* [INPUT](INPUT.md) , [LINE](LINE.md) [INPUT](INPUT.md)
* [INPUT](INPUT.md)$ , [INP](INP.md)
* CHR$ , ASCII
* [ASC](ASC.md) (function) , Scancodes (keyboard)
* Windows hot keys

```vb
'                                ASCII Keyboard Codes
'
'  Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
'  `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
'   96 49  50  51  52  53  54  55  56  57  48 45 61
'  Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + 
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
'     113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 
'  CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  E
'        97 115 100 102 103 104 106 107 108  59  39                       52   53   54  n
'  Shift  Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲        1End 2/▼  3PD  t
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  e
'        122 120  99 118  98 110 109  44  46  47                          49   50   51  r
'  Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del 
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                         48        46
'
'      Italics = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)
'
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* [_KEYHIT](_KEYHIT.md) , [_KEYDOWN](_KEYDOWN.md) , [_MAPUNICODE](_MAPUNICODE.md)
* [_KEYCLEAR](_KEYCLEAR.md)
* [INPUT](INPUT.md) , [LINE](LINE.md) [INPUT](INPUT.md)
* [INPUT](INPUT.md)$ , [INP](INP.md)
* CHR$ , ASCII
* [ASC](ASC.md) (function) , Scancodes (keyboard)
* Windows hot keys

