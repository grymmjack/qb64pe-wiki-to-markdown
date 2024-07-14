


\_GREEN - QB64 Phoenix Edition Wiki








# \_GREEN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_GREEN function returns the palette index or the green component intensity of a 32-bit image color.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*greenIntensity&* = \_GREEN(*rgbaColorIndex&*[, *imageHandle&*])
  




## Description


* *rgbaColorIndex&* is the *RGBA* color value or palette index of the color to retrieve the green component intensity from.
* The [LONG](/qb64wiki/index.php/LONG "LONG") intensity value returned ranges from 0 (no intensity, not present) to 255 (full intensity).
* If *imageHandle&* specifies a 32-bit color image, *rgbaColorIndex&* is interpreted as a 32-bit *RGBA* color value.
* If *imageHandle&* specifies an image that uses a palette, *rgbaColorIndex&* is interpreted as a palette index.
* If *imageHandle&* is not specified, it is assumed to be the current write page (See [\_DEST](/qb64wiki/index.php/DEST "DEST")).
* If *imageHandle&* is an invalid handle, an [invalid handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* If *rgbaColorIndex&* is outside the range of valid indexes for a given image mode, an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error occurs.
* Uses index parameters passed by the [\_RGB](/qb64wiki/index.php/RGB "RGB"), [\_RGBA](/qb64wiki/index.php/RGBA "RGBA"), [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") or [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32") functions.
* An image handle is optional.


  




## Examples


* See example in [POINT](/qb64wiki/index.php/POINT "POINT").


  




## See also


* [\_RED](/qb64wiki/index.php/RED "RED"), [\_BLUE](/qb64wiki/index.php/BLUE "BLUE")
* [\_RGB](/qb64wiki/index.php/RGB "RGB"), [RGB32](/qb64wiki/index.php/RGB32 "RGB32")
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=GREEN&oldid=6022>"




## Navigation menu








### Search





















