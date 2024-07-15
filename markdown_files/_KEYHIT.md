# _KEYHIT
> The _KEYHIT function returns ASCII one and two byte, OpenGL Virtual Key and Unicode keyboard key press codes.

## SYNTAX
`keycode& = _KEYHIT`

## DESCRIPTION
* Return values range up to &H40000000 so use a [LONG](LONG.md) or [_INTEGER64](_INTEGER64.md) variable type. See the [_KEYDOWN](_KEYDOWN.md) code list:


## EXAMPLES
> Example: This routine will return the codes for any keyboard presses.

```vb
'                                _KEYHIT Keyboard Codes
'
' Esc  F1    F2    F3    F4    F5    F6    F7    F8    F9    F10   F11   F12   Sys  ScL Pause
'  27 15104 15360 15616 15872 16128 16384 16640 16896 17152 17408 34048 34304 +316 +302 +019
' `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins   Hme   PUp   NumL   /     *    -
' 126 33  64  35  36  37  94  38  42  40  41 95 43   8   20992 18176 18688 +300   47    42   45
'  96 49  50  51  52  53  54  55  56  57  48 45 61
' Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del   End   PDn   7Hme  8/▲   9PU   + 
'  9  81  87  69  82  84  89  85  73  79  80 123 125 124 21248 20224 20736 18176 18432 18688 43
'    113 119 101 114 116 121 117 105 111 112  91  93  92                    55    56    57 
' CapL   A   S   D   F   G   H   J   K   L   ;:  '" Enter                   4/◄-   5    6/-►
' +301  65  83  68  70  71  72  74  75  76  58  34  13                     19200 19456 19712  E
'       97 115 100 102 103 104 106 107 108  59  39                          52    53    54    n
' Shift   Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲           1End  2/▼   3PD   t
' +304   90  88  67  86  66  78  77  60  62  63    +303       18432        20224 20480 20736  e
'       122 120  99 118  98 110 109  44  46  47                             49    50    51    r
' Ctrl   Win  Alt     Spacebar      Alt  Win  Menu  Ctrl   ◄-   ▼   -►      0Ins        .Del 
' +306  +311 +308       32         +307 +312 +319  +305 19200 20480 19712  20992       21248 13
'                                                                           48          46
'
'         Lower value = LCase/NumLock On __________________ + = add 100000
```


```vb
'                                _KEYHIT Keyboard Codes
'
' Esc  F1    F2    F3    F4    F5    F6    F7    F8    F9    F10   F11   F12   Sys  ScL Pause
'  27 15104 15360 15616 15872 16128 16384 16640 16896 17152 17408 34048 34304 +316 +302 +019
' `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins   Hme   PUp   NumL   /     *    -
' 126 33  64  35  36  37  94  38  42  40  41 95 43   8   20992 18176 18688 +300   47    42   45
'  96 49  50  51  52  53  54  55  56  57  48 45 61
' Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del   End   PDn   7Hme  8/▲   9PU   + 
'  9  81  87  69  82  84  89  85  73  79  80 123 125 124 21248 20224 20736 18176 18432 18688 43
'    113 119 101 114 116 121 117 105 111 112  91  93  92                    55    56    57 
' CapL   A   S   D   F   G   H   J   K   L   ;:  '" Enter                   4/◄-   5    6/-►
' +301  65  83  68  70  71  72  74  75  76  58  34  13                     19200 19456 19712  E
'       97 115 100 102 103 104 106 107 108  59  39                          52    53    54    n
' Shift   Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲           1End  2/▼   3PD   t
' +304   90  88  67  86  66  78  77  60  62  63    +303       18432        20224 20480 20736  e
'       122 120  99 118  98 110 109  44  46  47                             49    50    51    r
' Ctrl   Win  Alt     Spacebar      Alt  Win  Menu  Ctrl   ◄-   ▼   -►      0Ins        .Del 
' +306  +311 +308       32         +307 +312 +319  +305 19200 20480 19712  20992       21248 13
'                                                                           48          46
'
'         Lower value = LCase/NumLock On __________________ + = add 100000
```

* [_KEYDOWN](_KEYDOWN.md) , [_CINP](_CINP.md)
* [_MAPUNICODE](_MAPUNICODE.md) , [_MAPUNICODE](_MAPUNICODE.md) (function)
* INKEY$ , ASCII (code table) ,
* Unicode , Code Pages (by region)
* [INP](INP.md) ( &H60 ), Scancodes
* [ON](ON.md) [KEY](KEY.md)(n) , [KEY](KEY.md)(n) , [KEY](KEY.md) n
* Windows hot keys

```vb
'                                _KEYHIT Keyboard Codes
'
' Esc  F1    F2    F3    F4    F5    F6    F7    F8    F9    F10   F11   F12   Sys  ScL Pause
'  27 15104 15360 15616 15872 16128 16384 16640 16896 17152 17408 34048 34304 +316 +302 +019
' `~  1!  2@  3#  4$  5%  6^  7&  8*  9(  0) -_ =+ BkSp   Ins   Hme   PUp   NumL   /     *    -
' 126 33  64  35  36  37  94  38  42  40  41 95 43   8   20992 18176 18688 +300   47    42   45
'  96 49  50  51  52  53  54  55  56  57  48 45 61
' Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del   End   PDn   7Hme  8/▲   9PU   + 
'  9  81  87  69  82  84  89  85  73  79  80 123 125 124 21248 20224 20736 18176 18432 18688 43
'    113 119 101 114 116 121 117 105 111 112  91  93  92                    55    56    57 
' CapL   A   S   D   F   G   H   J   K   L   ;:  '" Enter                   4/◄-   5    6/-►
' +301  65  83  68  70  71  72  74  75  76  58  34  13                     19200 19456 19712  E
'       97 115 100 102 103 104 106 107 108  59  39                          52    53    54    n
' Shift   Z   X   C   V   B   N   M   ,<  .>  /?    Shift       ▲           1End  2/▼   3PD   t
' +304   90  88  67  86  66  78  77  60  62  63    +303       18432        20224 20480 20736  e
'       122 120  99 118  98 110 109  44  46  47                             49    50    51    r
' Ctrl   Win  Alt     Spacebar      Alt  Win  Menu  Ctrl   ◄-   ▼   -►      0Ins        .Del 
' +306  +311 +308       32         +307 +312 +319  +305 19200 20480 19712  20992       21248 13
'                                                                           48          46
'
'         Lower value = LCase/NumLock On __________________ + = add 100000
```



# SEE ALSO
* [_KEYDOWN](_KEYDOWN.md) , [_CINP](_CINP.md)
* [_MAPUNICODE](_MAPUNICODE.md) , [_MAPUNICODE](_MAPUNICODE.md) (function)
* INKEY$ , ASCII (code table) ,
* Unicode , Code Pages (by region)
* [INP](INP.md) ( &H60 ), Scancodes
* [ON](ON.md) [KEY](KEY.md)(n) , [KEY](KEY.md)(n) , [KEY](KEY.md) n
* Windows hot keys

