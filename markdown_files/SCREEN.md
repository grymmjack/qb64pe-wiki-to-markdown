# SCREEN
> The SCREEN statement sets the video display mode and size of the program window's workspace.

## SYNTAX
`SCREEN { mode% | imagehandle& } [, , active_page, visual_page]`

## PARAMETERS
* The [SCREEN](SCREEN.md) mode [INTEGER](INTEGER.md) values available today are 0 to 2 and 7 to 13 listed below.
* QB64 can use a [LONG](LONG.md) [_NEWIMAGE](_NEWIMAGE.md) page or [_LOADIMAGE](_LOADIMAGE.md) file image handle value instead.
* The empty comma disables color when any value is used. [DO](DO.md) [NOT](NOT.md) USE! Include the comma [ONLY](ONLY.md) when using page flipping.
* If the [SCREEN](SCREEN.md) mode supports pages, the active page is the page to be worked on while visual page is the one displayed.


## EXAMPLES
> ( Return to Table of Contents )

```vb
LEGACY SCREEN MODES AT A GLANCE

Screen      Text           Graphics          Colors      Video    Text      Default
 Mode   Rows   Columns   Width   Height  Attrib.   BPP   Pages    Block    QB64 Font

  0   25/43/50  80/40    No graphics     16/16 DAC  4     0-7     -----    _FONT 16
  1      25      40      320     200     16/4 BG    4     none    8 X 8    _FONT 8
  2      25      80      640     200      2/mono    1     none    8 X 8    _FONT 8
  .................................................................................
  7      25      40      320     200     16/16 DAC  4     0-7     8 X 8    _FONT 8
  8      25      80      640     200     16/16      4     0-3     8 X 8    _FONT 8
  9      25      80      640     350     16/64 DAC  4     0-1     8 X 14   _FONT 14
 10      25      80      640     350     4/2 GScale 2     none    8 X 14   _FONT 14
 11     30/60    80      640     480      2/mono    1     none    8 X 16   _FONT 16
 12     30/60    80      640     480     16/262K    4     none    8 X 16   _FONT 16
 13      25      40      320     200     256/65K    8     none    8 X 8    _FONT 8

             QB64 allows video paging and PCOPY in ALL screen modes!
```

* SaveImage [SUB](SUB.md)
* Program ScreenShots
* ThirtyTwoBit [SUB](SUB.md)
* SelectScreen
* ScreenMode

```vb
LEGACY SCREEN MODES AT A GLANCE

Screen      Text           Graphics          Colors      Video    Text      Default
 Mode   Rows   Columns   Width   Height  Attrib.   BPP   Pages    Block    QB64 Font

  0   25/43/50  80/40    No graphics     16/16 DAC  4     0-7     -----    _FONT 16
  1      25      40      320     200     16/4 BG    4     none    8 X 8    _FONT 8
  2      25      80      640     200      2/mono    1     none    8 X 8    _FONT 8
  .................................................................................
  7      25      40      320     200     16/16 DAC  4     0-7     8 X 8    _FONT 8
  8      25      80      640     200     16/16      4     0-3     8 X 8    _FONT 8
  9      25      80      640     350     16/64 DAC  4     0-1     8 X 14   _FONT 14
 10      25      80      640     350     4/2 GScale 2     none    8 X 14   _FONT 14
 11     30/60    80      640     480      2/mono    1     none    8 X 16   _FONT 16
 12     30/60    80      640     480     16/262K    4     none    8 X 16   _FONT 16
 13      25      40      320     200     256/65K    8     none    8 X 8    _FONT 8

             QB64 allows video paging and PCOPY in ALL screen modes!
```

* [COLOR](COLOR.md) , [CLS](CLS.md) , [WIDTH](WIDTH.md)
* [_NEWIMAGE](_NEWIMAGE.md) , [_LOADIMAGE](_LOADIMAGE.md) , [_SAVEIMAGE](_SAVEIMAGE.md)
* [_SCREENIMAGE](_SCREENIMAGE.md)
* [_LOADFONT](_LOADFONT.md) , [_FONT](_FONT.md)
* [_DISPLAY](_DISPLAY.md) , [_COPYIMAGE](_COPYIMAGE.md) , [_SCREENMOVE](_SCREENMOVE.md)
* [_SCREENHIDE](_SCREENHIDE.md) , [_SCREENSHOW](_SCREENSHOW.md) , [_SCREENICON](_SCREENICON.md)
* [PALETTE](PALETTE.md) , [OUT](OUT.md) , [PCOPY](PCOPY.md) ,
* [GET](GET.md) , [PUT](PUT.md)
* [VIEW](VIEW.md) , [WINDOW](WINDOW.md) , [VIEW](VIEW.md) [PRINT](PRINT.md)
* [SCREEN](SCREEN.md) (function) , [POINT](POINT.md)
* Screen Memory , Screen Saver Programs
* [_CONSOLE](_CONSOLE.md)

```vb
LEGACY SCREEN MODES AT A GLANCE

Screen      Text           Graphics          Colors      Video    Text      Default
 Mode   Rows   Columns   Width   Height  Attrib.   BPP   Pages    Block    QB64 Font

  0   25/43/50  80/40    No graphics     16/16 DAC  4     0-7     -----    _FONT 16
  1      25      40      320     200     16/4 BG    4     none    8 X 8    _FONT 8
  2      25      80      640     200      2/mono    1     none    8 X 8    _FONT 8
  .................................................................................
  7      25      40      320     200     16/16 DAC  4     0-7     8 X 8    _FONT 8
  8      25      80      640     200     16/16      4     0-3     8 X 8    _FONT 8
  9      25      80      640     350     16/64 DAC  4     0-1     8 X 14   _FONT 14
 10      25      80      640     350     4/2 GScale 2     none    8 X 14   _FONT 14
 11     30/60    80      640     480      2/mono    1     none    8 X 16   _FONT 16
 12     30/60    80      640     480     16/262K    4     none    8 X 16   _FONT 16
 13      25      40      320     200     256/65K    8     none    8 X 8    _FONT 8

             QB64 allows video paging and PCOPY in ALL screen modes!
```



# SEE ALSO
* [COLOR](COLOR.md) , [CLS](CLS.md) , [WIDTH](WIDTH.md)
* [_NEWIMAGE](_NEWIMAGE.md) , [_LOADIMAGE](_LOADIMAGE.md) , [_SAVEIMAGE](_SAVEIMAGE.md)
* [_SCREENIMAGE](_SCREENIMAGE.md)
* [_LOADFONT](_LOADFONT.md) , [_FONT](_FONT.md)
* [_DISPLAY](_DISPLAY.md) , [_COPYIMAGE](_COPYIMAGE.md) , [_SCREENMOVE](_SCREENMOVE.md)
* [_SCREENHIDE](_SCREENHIDE.md) , [_SCREENSHOW](_SCREENSHOW.md) , [_SCREENICON](_SCREENICON.md)
* [PALETTE](PALETTE.md) , [OUT](OUT.md) , [PCOPY](PCOPY.md) ,
* [GET](GET.md) , [PUT](PUT.md)
* [VIEW](VIEW.md) , [WINDOW](WINDOW.md) , [VIEW](VIEW.md) [PRINT](PRINT.md)
* [SCREEN](SCREEN.md) (function) , [POINT](POINT.md)
* Screen Memory , Screen Saver Programs
* [_CONSOLE](_CONSOLE.md)

