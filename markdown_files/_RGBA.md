


\_RGBA - QB64 Phoenix Edition Wiki








# \_RGBA



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_RGBA function returns the closest palette index (legacy SCREEN modes) OR the 32-bit [LONG](/qb64wiki/index.php/LONG "LONG") color value (32-bit screens).


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


*colorIndex~&* = \_RGBA(*red&*, *green&*, *blue&*, *alpha&*[, *imageHandle&*]**)**
  




* The value returned is either the closest color attribute number or a 32-bit [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") color value.
* **Return variable types must be [LONG](/qb64wiki/index.php/LONG "LONG") or the resulting color may lose the [\_BLUE](/qb64wiki/index.php/BLUE "BLUE") value.**
* *red&* specifies the red component intensity from 0 to 255.
* *green&* specifies the green component intensity from 0 to 255.
* *blue&* specifies the blue component intensity from 0 to 255.
* The [*alpha&*](/qb64wiki/index.php/ALPHA "ALPHA") value can be set to make the color transparent (0), opaque (255) or somewhere in between.
* Parameter values outside of the 0 to 255 range are clipped.
* Returns [LONG](/qb64wiki/index.php/LONG "LONG") 32-bit hexadecimal values from **&H00000000** to **&HFFFFFFFF** with varying [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") transparency.
* When [LONG](/qb64wiki/index.php/LONG "LONG") values are [PUT](/qb64wiki/index.php/PUT "PUT") to file, the ARGB values become BGRA. Use [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")([MKL$](/qb64wiki/index.php/MKL$ "MKL$")(*colorIndex~&*), 3) to place 3 colors.
* If *imageHandle&* is omitted, the image is assumed to be the current [destination](/qb64wiki/index.php/DEST "DEST") or [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") page.
* Allows the blending of pixel colors red, green and blue to create any of 16 million colors.
* **NOTE: Default 32-bit backgrounds are clear black or \_RGBA(0, 0, 0, 0). Use [CLS](/qb64wiki/index.php/CLS "CLS") to make the black opaque.**


  




## Examples


*Example:* Setting a font's background color alpha to clear to overlay a second text color.





| ``` scrn& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(400, 400, 32) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") scrn& fnt& = [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("C:\WINDOWS\FONTS\ARIAL.TTF", 26) [_FONT](/qb64wiki/index.php/FONT "FONT") fnt& X% = 20 Y% = 20 [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255), [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 0, 0) 'Foreground set to WHITE background to BLACK [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (X%, Y%), "Hello World" [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 0, 0), _RGBA(0, 0, 0, 0) 'Foreground set to RED background to TRANSPARENT BLACK [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (X% + 2, Y% + 2), "Hello World" [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Unseen Machine
*Explanation:* [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") allows text or font colors to be alpha blended in 32 bit screens.


  




## See also


* [\_RGB](/qb64wiki/index.php/RGB "RGB"), [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32"), [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")
* [\_RED](/qb64wiki/index.php/RED "RED"), [\_GREEN](/qb64wiki/index.php/GREEN "GREEN"), [\_BLUE](/qb64wiki/index.php/BLUE "BLUE")
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")
* [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING")
* [HEX$ 32 Bit Values](/qb64wiki/index.php/HEX$_32_Bit_Values "HEX$ 32 Bit Values"), [POINT](/qb64wiki/index.php/POINT "POINT")
* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [Hexadecimal Color Values](http://www.w3schools.com/html/html_colornames.asp)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RGBA&oldid=8670>"




## Navigation menu








### Search





















