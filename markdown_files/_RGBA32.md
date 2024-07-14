


\_RGBA32 - QB64 Phoenix Edition Wiki








# \_RGBA32



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_RGBA32 function returns the 32-bit *RGBA* color value with the specified red, green, blue and alpha component intensities.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*color32value~&* = \_RGBA32(*red&*, *green&*, *blue&*, *alpha&*)
  




## Description


* The value returned is a 32-bit [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") color value.
* **Return variable types must be [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") or resulting color may lose the [\_BLUE](/qb64wiki/index.php/BLUE "BLUE") value.**
* *red&* specifies the red component intensity from 0 to 255.
* *green&* specifies the green component intensity from 0 to 255.
* *blue&* specifies the blue component intensity from 0 to 255.
* *alpha&* specifies the [*alpha*](/qb64wiki/index.php/ALPHA "ALPHA") component transparency value from 0 (fully transparent) to 255 (opaque).
* Alpha or intensity values outside of the valid range of 0 to 255 are clipped.
* Returns [LONG](/qb64wiki/index.php/LONG "LONG") 32-bit hexadecimal values from **&H00000000** to **&HFFFFFFFF** with varying [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") transparency.
* When [LONG](/qb64wiki/index.php/LONG "LONG") values are [PUT](/qb64wiki/index.php/PUT "PUT") to file, the ARGB values become BGRA. Use [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")([MKL$](/qb64wiki/index.php/MKL$ "MKL$")(*color32value~&*), 3) to place 3 colors.
* **NOTE: Default 32-bit backgrounds are clear black or [\_RGBA](/qb64wiki/index.php/RGBA "RGBA")(0, 0, 0, 0). Use [CLS](/qb64wiki/index.php/CLS "CLS") to make the black opaque.**


  




## Examples


*Example:* Changing the [ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") value to fade an image in and out using a 32 bit PNG image.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(600, 400, 32)  img& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("qb64_trans.png")  'use any 24/32 bit image 'Turn off auto display [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")  ' Fade in [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i% = 255 [TO](/qb64wiki/index.php/TO "TO") 0 [STEP](/qb64wiki/index.php/STEP "STEP") -5   [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 20                          'control fade speed   [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 0)-(600, 400), img&   [LINE](/qb64wiki/index.php/LINE "LINE") (0, 0)-(600, 400), [_RGBA](/qb64wiki/index.php/RGBA "RGBA")(0, 0, 0, i%), BF 'decrease black box transparency   [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ' Fade out [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i% = 0 [TO](/qb64wiki/index.php/TO "TO") 255 [STEP](/qb64wiki/index.php/STEP "STEP") 5   [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 20                          'control fade speed   [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 0)-(600, 400), img&   [LINE](/qb64wiki/index.php/LINE "LINE") (0, 0)-(600, 400), [_RGBA](/qb64wiki/index.php/RGBA "RGBA")(0, 0, 0, i%), BF 'increase black box transparency   [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Unseen Machine
  




## See also


* [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32"), [\_RGBA](/qb64wiki/index.php/RGBA "RGBA"), [\_RGB](/qb64wiki/index.php/RGB "RGB")
* [\_RED32](/qb64wiki/index.php/RED32 "RED32"), [\_GREEN32](/qb64wiki/index.php/GREEN32 "GREEN32"), [\_BLUE32](/qb64wiki/index.php/BLUE32 "BLUE32")
* [HEX$ 32 Bit Values](/qb64wiki/index.php/HEX$_32_Bit_Values "HEX$ 32 Bit Values"), [POINT](/qb64wiki/index.php/POINT "POINT")
* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [Hexadecimal Color Values](http://www.w3schools.com/html/html_colornames.asp)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RGBA32&oldid=8671>"




## Navigation menu








### Search





















