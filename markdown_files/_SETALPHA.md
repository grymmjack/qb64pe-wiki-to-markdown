


\_SETALPHA - QB64 Phoenix Edition Wiki








# \_SETALPHA



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SETALPHA statement sets the alpha channel transparency level of some or all of the pixels of an image.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_SETALPHA *alpha&*[, *color1&*][ [TO](/qb64wiki/index.php/TO "TO") *colour2&*] [, *imageHandle&*]
  




## Parameters


* *alpha&* is the new alpha level to set, ranging from 0 (transparent) to 255 (opaque).
* *color1&* designates the 32-bit [LONG](/qb64wiki/index.php/LONG "LONG") color value or range of color values *color1&* TO *colour2&* to set the transparency.
* If no color value or range of colors is given, the entire image's alpha is changed, including any [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") settings.
* If *imageHandle&* is omitted, it is assumed to be the current write page or [destination](/qb64wiki/index.php/DEST "DEST") image.


  




## Description


* In the first syntax, the alpha level of all pixels is set to *alpha&*.
* In the second syntax, the alpha level of all pixels matching the color *color1&* is set to *alpha&*.
* In the third syntax, the alpha level of all pixels with red, green, blue and alpha channels in the range [*color1&* TO *color2&*] are set.
* The [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") setting makes a 32-bit color transparent, opaque or something in between. Zero is clear and 255 totally blocks underlying images. Use it to see through backgrounds or image colors.
* If *alpha&* is outside that range, an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* If the image specified by *imageHandle&* uses a palette, an [invalid handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* If *imageHandle&* is an invalid handle, an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* **NOTE: 32-bit [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") screen page backgrounds are transparent black or [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") 0. Use [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") or [CLS](/qb64wiki/index.php/CLS "CLS") for opaque.**


  




## Examples


*Example:* Using a \_SETALPHA color range to fade an image in and out while not affecting the transparent white background.





| ``` main = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") main [_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE") [_MIDDLE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE")  Image1& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("qb64_trans.png") '<<< PNG file with white background to hide [_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") Image1& clr~& = [POINT](/qb64wiki/index.php/POINT "POINT")(0, 0) 'find background color of image [_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") clr~&, Image1& 'set background color as transparent  topclr~& = clr~& - [_RGBA](/qb64wiki/index.php/RGBA "RGBA")(1, 1, 1, 0)  'get topmost color range just below full white [_DEST](/qb64wiki/index.php/DEST "DEST") main  a& = 0 d = 1 DO   [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 10 'regulate speed of fade in and out   [CLS](/qb64wiki/index.php/CLS "CLS") ', [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 0, 0)   a& = a& + d   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") a& = 255 [THEN](/qb64wiki/index.php/THEN "THEN") d = -d   _SETALPHA a&, 0 [TO](/qb64wiki/index.php/TO "TO") topclr~&, Image1& 'affects all colors below bright white   [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 342), Image1&   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Alpha: "; a&   [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") a& = 0  ``` |
| --- |


*Explanation:* The [POINT](/qb64wiki/index.php/POINT "POINT") value minus [\_RGBA](/qb64wiki/index.php/RGBA "RGBA")(1, 1, 1, 0) subtracts a small amount from the bright white color value so that the top \_SETALPHA color range will not affect the [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") transparency of the bright white PNG background.
  




## See also


* [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA"), [\_ALPHA32](/qb64wiki/index.php/ALPHA32 "ALPHA32")
* [\_RGBA](/qb64wiki/index.php/RGBA "RGBA"), [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")
* [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR")
* [\_CLEARCOLOR (function)](/qb64wiki/index.php/CLEARCOLOR_(function) "CLEARCOLOR (function)")
* [\_BLEND](/qb64wiki/index.php/BLEND "BLEND"), [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND")
* [COLOR](/qb64wiki/index.php/COLOR "COLOR"), [Images](/qb64wiki/index.php/Images "Images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SETALPHA&oldid=6531>"




## Navigation menu








### Search





















