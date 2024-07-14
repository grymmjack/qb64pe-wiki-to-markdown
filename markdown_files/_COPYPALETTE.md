


\_COPYPALETTE - QB64 Phoenix Edition Wiki








# \_COPYPALETTE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_COPYPALETTE statement copies the color palette intensities from one 4 or 8 BPP image to another image or a [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") screen page using 256 or less colors.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_COPYPALETTE [*sourceImageHandle&*[, *destinationImageHandle&*
  




## Description


* Palette Intensity settings are **not** used by 24/32 bit images. Use only with 4 or 8 BPP images.
* [\_PIXELSIZE](/qb64wiki/index.php/PIXELSIZE "PIXELSIZE") function returns 1 to indicate that \_COPYPALETTE can be used. 4 indicates 24/32 bit images.
* If *sourceImageHandle&* is omitted, it is assumed to be the current read page.
* If *destinationImageHandle&* is omitted, it is assumed to be the current write page.
* If either of the images specified by *sourceImageHandle&* or *destinationImageHandle&* do not use a palette, an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error is returned.
* If either *sourceImageHandle&* or *destinationImageHandle&* is an invalid handle, an [invalid handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error is returned.
* When loading 4 or 8 BPP image files, it is necessary to adopt the color palette of the image or it may not have the correct colors!


  




## Examples


* See the example in [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB").


  




## See also


* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")
* [\_PIXELSIZE](/qb64wiki/index.php/PIXELSIZE "PIXELSIZE")
* [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR"), [\_PALETTECOLOR (function)](/qb64wiki/index.php/PALETTECOLOR_(function) "PALETTECOLOR (function)")
* [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE"), [Images](/qb64wiki/index.php/Images "Images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=COPYPALETTE&oldid=8657>"




## Navigation menu








### Search





















