


\_SCREENPRINT - QB64 Phoenix Edition Wiki








# \_SCREENPRINT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SCREENPRINT statement simulates typing text into a Windows focused program.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_SCREENPRINT *text$*
  




## Description


* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**
* *text$* is the text to be typed into a focused program's text entry area, one character at a time.
* Set the focus to a desktop program by using the [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE") handle as the [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE"). Use the image to map the desired area.
* [\_SCREENCLICK](/qb64wiki/index.php/SCREENCLICK "SCREENCLICK") can also be used to set the focus to a program's text entry area on the desktop.
* **Note: If the focus is not set correctly, the text may be printed to the QB64 IDE, if open, or not printed at all.**
* Ctrl + letter key shortcuts can be simulated using the appropriate [ASCII](/qb64wiki/index.php/ASCII "ASCII") Control character codes 1 to 26 shown below:




| ```  CTRL + A = CHR$(1)   ☺  StartHeader (SOH)    CTRL + B = CHR$(2)   ☻  StartText         (STX)  CTRL + C = CHR$(3)   ♥  EndText     (ETX)    CTRL + D = CHR$(4)   ♦  EndOfTransmit     (EOT)  CTRL + E = CHR$(5)   ♣  Enquiry     (ENQ)    CTRL + F = CHR$(6)   ♠  Acknowledge       (ACK)  CTRL + G = CHR$(7)   •  [BEEP](/qb64wiki/index.php/BEEP "BEEP")        (BEL)    CTRL + H = CHR$(8)   ◘  **[Backspace]**       (BS)  CTRL + I = CHR$(9)   ○  Horiz.Tab   **[Tab]**    CTRL + J = CHR$(10)  ◙  LineFeed(printer) (LF)  CTRL + K = CHR$(11)  ♂  Vert. Tab   (VT)     CTRL + L = CHR$(12)  ♀  FormFeed(printer) (FF)  CTRL + M = CHR$(13)  ♪  **[Enter]**     (CR)     CTRL + N = CHR$(14)  ♫  ShiftOut          (SO)  CTRL + O = CHR$(15)  ☼  ShiftIn     (SI)     CTRL + P = CHR$(16)  ►  DataLinkEscape    (DLE)  CTRL + Q = CHR$(17)  ◄  DevControl1 (DC1)    CTRL + R = CHR$(18)  ↕  DeviceControl2    (DC2)  CTRL + S = CHR$(19)  ‼  DevControl3 (DC3)    CTRL + T = CHR$(20)  ¶  DeviceControl4    (DC4)  CTRL + U = CHR$(21)  §  NegativeACK (NAK)    CTRL + V = CHR$(22)  ▬  Synchronous Idle  (SYN)  CTRL + W = CHR$(23)  ↨  EndTXBlock  (ETB)    CTRL + X = CHR$(24)  ↑  Cancel            (CAN)  CTRL + Y = CHR$(25)  ↓  EndMedium   (EM)     CTRL + Z = CHR$(26)  →  End Of File(SUB)  (EOF)  ``` |
| --- |


  




## Examples


*Example:* Printing text into a Windows text editor (Notepad) and copying to the clipboard. May not work on all systems.





| ``` [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG") A-Z [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "OPENing and MAXIMIZING Notepad in 5 seconds..."; : [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 5 [SHELL](/qb64wiki/index.php/SHELL "SHELL") [_DONTWAIT](/qb64wiki/index.php/DONTWAIT "DONTWAIT") "START /MAX NotePad.exe"  'opens Notepad file "untitled.txt" 'detect notepad open and maximized 'condition: 80% or more of the screen is white [DO](/qb64wiki/index.php/DO "DO")                     'read the desktop screen image for maximized window   s = [_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")   [_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") s   z = 0   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y = 0 [TO](/qb64wiki/index.php/TO "TO") [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(s) - 1   'scan for large white area     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") x = 0 [TO](/qb64wiki/index.php/TO "TO") _[WIDTH](/qb64wiki/index.php/WIDTH "WIDTH")(s) - 1        c = [POINT](/qb64wiki/index.php/POINT "POINT")(x, y)        [IF](/qb64wiki/index.php/IF "IF") c = [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(255, 255, 255) [THEN](/qb64wiki/index.php/THEN "THEN") z = z + 1     [NEXT](/qb64wiki/index.php/NEXT "NEXT")   [NEXT](/qb64wiki/index.php/NEXT "NEXT")   [IF](/qb64wiki/index.php/IF "IF") z / ([_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(s) * _[WIDTH](/qb64wiki/index.php/WIDTH "WIDTH")(s)) > 0.8 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO") 'when 80% of screen is white   [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") s   'free desktop image   [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 1       'scans 1 loop per second [PRINT](/qb64wiki/index.php/PRINT "PRINT") "."; [LOOP](/qb64wiki/index.php/LOOP "LOOP") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "NOTEPAD detected as OPEN and MAXIMIZED"   _SCREENPRINT "HELLO WORLD" [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 2 _SCREENPRINT [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(8) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(8) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(8) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(8) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(8) 'backspace 5 characters [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 3 _SCREENPRINT "QB64!" [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 2 _SCREENPRINT [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(1) 'CTRL + A select all [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 2 _SCREENPRINT [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(3) 'CTRL + C copy to clipboard [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 2 [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CLIPBOARD$](/qb64wiki/index.php/CLIPBOARD$_(function) "CLIPBOARD$ (function)") [_CLIPBOARD$](/qb64wiki/index.php/CLIPBOARD$ "CLIPBOARD$") = "QB64 ROCKS!" [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 2 _SCREENPRINT [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(22) 'CTRL + V paste from clipboard [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Galleon
*Explanation:* If the Windows shortcuts are set up properly, printing ASCII Control characters acts like the user selected the control + letter combinations to *Select all* (CHR$(1)), *Copy* (CHR$(3)) and *Paste* (CHR$(22)) the text with the Windows Clipboard. If the editor program's CTRL key combinations are different, use the matching letter [ASCII](/qb64wiki/index.php/ASCII "ASCII") code from A = 1 to Z = 26 in the text editor.
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1252)
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE"), [\_SCREENCLICK](/qb64wiki/index.php/SCREENCLICK "SCREENCLICK")
* [\_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE"), [\_SCREENX](/qb64wiki/index.php/SCREENX "SCREENX"), [\_SCREENY](/qb64wiki/index.php/SCREENY "SCREENY")
* [ASCII](/qb64wiki/index.php/ASCII "ASCII")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SCREENPRINT&oldid=8913>"




## Navigation menu








### Search





















