


\_PIXELSIZE - QB64 Phoenix Edition Wiki








# \_PIXELSIZE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_PIXELSIZE function returns the color depth (Bits Per Pixel) of an image as 0 for text, 1 for 1 to 8 BPP or 4 for 32 bit.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) 	+ [3.1 More examples](#More_examples) * [4 See also](#See_also) |
| --- |


## Syntax


*pixelSize%* = \_PIXELSIZE[(*imageHandle&*)]
  




## Description


* If *imageHandle&* is omitted, it is assumed to be the current write page.
* Returns:
	+ 0 if the image or screen page specified by *imageHandle&* is in text mode.
	+ 1 if the image specified by *imageHandle&* is in 1 (B & W), 4 (16 colors) or 8 (256 colors) BPP mode.
	+ 4 if the image specified is a 24/32-bit compatible mode. Pixels use three bytes, one per red, green and blue color intensity.
* The [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") or [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") or [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") color mode (256 or 32) can influence the pixel sizes that can be returned.
* If *imageHandle&* is an invalid handle, then an [invalid handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error occurs.


  




## Examples


*Snippet:* Saving Images for later program use. Handle values could be saved to an array.





| ```   handle1& = _Getimage(sx1, sy1, sx2, sy2, sourcehandle&) ' function call  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") GetImage& (sx1, sy1, sx2, sy2, sourcehandle&) bytespp = _PIXELSIZE(sourcehandle&) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") bytespp = 4 [THEN](/qb64wiki/index.php/THEN "THEN") Pal = 32 [ELSE](/qb64wiki/index.php/ELSE "ELSE") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") bytespp = 1 [THEN](/qb64wiki/index.php/THEN "THEN") Pal = 256 [ELSE](/qb64wiki/index.php/ELSE "ELSE") [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION") h& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")([ABS](/qb64wiki/index.php/ABS "ABS")(sx2 - sx1) + 1, [ABS](/qb64wiki/index.php/ABS "ABS")(sy2 - sy1) + 1, Pal) [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 0), sourcehandle&, h&, (sx1, sy1)-(sx2, sy2) 'image is not displayed GetImage& = h& [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Adapted from code by Galleon
### More examples


* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [SaveIcon32](/qb64wiki/index.php/SaveIcon32 "SaveIcon32")
* [ThirtyTwoBit SUB](/qb64wiki/index.php/ThirtyTwoBit_SUB "ThirtyTwoBit SUB")
* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps")


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1362)
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_SAVEIMAGE](/qb64wiki/index.php/SAVEIMAGE "SAVEIMAGE")
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE")
* [\_COPYPALETTE](/qb64wiki/index.php/COPYPALETTE "COPYPALETTE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PIXELSIZE&oldid=8935>"




## Navigation menu








### Search





















