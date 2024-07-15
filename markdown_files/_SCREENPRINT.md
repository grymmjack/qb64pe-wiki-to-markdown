# _SCREENPRINT
> The _SCREENPRINT statement simulates typing text into a Windows focused program.

## SYNTAX
`_SCREENPRINT text$`

## DESCRIPTION
* Keyword not supported in Linux or macOS versions
* text$ is the text to be typed into a focused program's text entry area, one character at a time.
* Set the focus to a desktop program by using the [_SCREENIMAGE](_SCREENIMAGE.md) handle as the [_SOURCE](_SOURCE.md) . Use the image to map the desired area.
* [_SCREENCLICK](_SCREENCLICK.md) can also be used to set the focus to a program's text entry area on the desktop.
* Note: If the focus is not set correctly, the text may be printed to the QB64 IDE, if open, or not printed at all.
* Ctrl + letter key shortcuts can be simulated using the appropriate ASCII Control character codes 1 to 26 shown below:


## EXAMPLES
> Example: Printing text into a Windows text editor (Notepad) and copying to the clipboard. May not work on all systems.

```vb
CTRL + A = CHR$(1)   ☺  StartHeader (SOH)    CTRL + B = CHR$(2)   ☻  StartText         (STX)
CTRL + C = CHR$(3)   ♥  EndText     (ETX)    CTRL + D = CHR$(4)   ♦  EndOfTransmit     (EOT)
CTRL + E = CHR$(5)   ♣  Enquiry     (ENQ)    CTRL + F = CHR$(6)   ♠  Acknowledge       (ACK)
CTRL + G = CHR$(7)   •  BEEP        (BEL)    CTRL + H = CHR$(8)   ◘  [Backspace]       (BS)
CTRL + I = CHR$(9)   ○  Horiz.Tab   [Tab]    CTRL + J = CHR$(10)  ◙  LineFeed(printer) (LF)
CTRL + K = CHR$(11)  ♂  Vert. Tab   (VT)     CTRL + L = CHR$(12)  ♀  FormFeed(printer) (FF)
CTRL + M = CHR$(13)  ♪  [Enter]     (CR)     CTRL + N = CHR$(14)  ♫  ShiftOut          (SO)
CTRL + O = CHR$(15)  ☼  ShiftIn     (SI)     CTRL + P = CHR$(16)  ►  DataLinkEscape    (DLE)
CTRL + Q = CHR$(17)  ◄  DevControl1 (DC1)    CTRL + R = CHR$(18)  ↕  DeviceControl2    (DC2)
CTRL + S = CHR$(19)  ‼  DevControl3 (DC3)    CTRL + T = CHR$(20)  ¶  DeviceControl4    (DC4)
CTRL + U = CHR$(21)  §  NegativeACK (NAK)    CTRL + V = CHR$(22)  ▬  Synchronous Idle  (SYN)
CTRL + W = CHR$(23)  ↨  EndTXBlock  (ETB)    CTRL + X = CHR$(24)  ↑  Cancel            (CAN)
CTRL + Y = CHR$(25)  ↓  EndMedium   (EM)     CTRL + Z = CHR$(26)  →  End Of File(SUB)  (EOF)
```


```vb
CTRL + A = CHR$(1)   ☺  StartHeader (SOH)    CTRL + B = CHR$(2)   ☻  StartText         (STX)
CTRL + C = CHR$(3)   ♥  EndText     (ETX)    CTRL + D = CHR$(4)   ♦  EndOfTransmit     (EOT)
CTRL + E = CHR$(5)   ♣  Enquiry     (ENQ)    CTRL + F = CHR$(6)   ♠  Acknowledge       (ACK)
CTRL + G = CHR$(7)   •  BEEP        (BEL)    CTRL + H = CHR$(8)   ◘  [Backspace]       (BS)
CTRL + I = CHR$(9)   ○  Horiz.Tab   [Tab]    CTRL + J = CHR$(10)  ◙  LineFeed(printer) (LF)
CTRL + K = CHR$(11)  ♂  Vert. Tab   (VT)     CTRL + L = CHR$(12)  ♀  FormFeed(printer) (FF)
CTRL + M = CHR$(13)  ♪  [Enter]     (CR)     CTRL + N = CHR$(14)  ♫  ShiftOut          (SO)
CTRL + O = CHR$(15)  ☼  ShiftIn     (SI)     CTRL + P = CHR$(16)  ►  DataLinkEscape    (DLE)
CTRL + Q = CHR$(17)  ◄  DevControl1 (DC1)    CTRL + R = CHR$(18)  ↕  DeviceControl2    (DC2)
CTRL + S = CHR$(19)  ‼  DevControl3 (DC3)    CTRL + T = CHR$(20)  ¶  DeviceControl4    (DC4)
CTRL + U = CHR$(21)  §  NegativeACK (NAK)    CTRL + V = CHR$(22)  ▬  Synchronous Idle  (SYN)
CTRL + W = CHR$(23)  ↨  EndTXBlock  (ETB)    CTRL + X = CHR$(24)  ↑  Cancel            (CAN)
CTRL + Y = CHR$(25)  ↓  EndMedium   (EM)     CTRL + Z = CHR$(26)  →  End Of File(SUB)  (EOF)
```

* Featured in our "Keyword of the Day" series
* [_SCREENIMAGE](_SCREENIMAGE.md) , [_SCREENCLICK](_SCREENCLICK.md)
* [_SCREENMOVE](_SCREENMOVE.md) , [_SCREENX](_SCREENX.md) , [_SCREENY](_SCREENY.md)
* ASCII

```vb
CTRL + A = CHR$(1)   ☺  StartHeader (SOH)    CTRL + B = CHR$(2)   ☻  StartText         (STX)
CTRL + C = CHR$(3)   ♥  EndText     (ETX)    CTRL + D = CHR$(4)   ♦  EndOfTransmit     (EOT)
CTRL + E = CHR$(5)   ♣  Enquiry     (ENQ)    CTRL + F = CHR$(6)   ♠  Acknowledge       (ACK)
CTRL + G = CHR$(7)   •  BEEP        (BEL)    CTRL + H = CHR$(8)   ◘  [Backspace]       (BS)
CTRL + I = CHR$(9)   ○  Horiz.Tab   [Tab]    CTRL + J = CHR$(10)  ◙  LineFeed(printer) (LF)
CTRL + K = CHR$(11)  ♂  Vert. Tab   (VT)     CTRL + L = CHR$(12)  ♀  FormFeed(printer) (FF)
CTRL + M = CHR$(13)  ♪  [Enter]     (CR)     CTRL + N = CHR$(14)  ♫  ShiftOut          (SO)
CTRL + O = CHR$(15)  ☼  ShiftIn     (SI)     CTRL + P = CHR$(16)  ►  DataLinkEscape    (DLE)
CTRL + Q = CHR$(17)  ◄  DevControl1 (DC1)    CTRL + R = CHR$(18)  ↕  DeviceControl2    (DC2)
CTRL + S = CHR$(19)  ‼  DevControl3 (DC3)    CTRL + T = CHR$(20)  ¶  DeviceControl4    (DC4)
CTRL + U = CHR$(21)  §  NegativeACK (NAK)    CTRL + V = CHR$(22)  ▬  Synchronous Idle  (SYN)
CTRL + W = CHR$(23)  ↨  EndTXBlock  (ETB)    CTRL + X = CHR$(24)  ↑  Cancel            (CAN)
CTRL + Y = CHR$(25)  ↓  EndMedium   (EM)     CTRL + Z = CHR$(26)  →  End Of File(SUB)  (EOF)
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* [_SCREENIMAGE](_SCREENIMAGE.md) , [_SCREENCLICK](_SCREENCLICK.md)
* [_SCREENMOVE](_SCREENMOVE.md) , [_SCREENX](_SCREENX.md) , [_SCREENY](_SCREENY.md)
* ASCII

