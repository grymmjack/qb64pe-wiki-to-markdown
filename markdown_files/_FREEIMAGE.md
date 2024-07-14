


\_FREEIMAGE - QB64 Phoenix Edition Wiki








# \_FREEIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_FREEIMAGE** statement releases the designated file image created by the [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") or [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE") functions from memory when they are no longer needed.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_FREEIMAGE [*handle&*]
  




## Description


* If *handle&* is omitted, the current destination image is freed from memory.
* Freeing the destination image or source image will result in the display page being selected instead.
* **Invalid image handle values of -1 or 0 cannot be freed or an ["Illegal Function" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.** Check the handle value first.
* **[SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes in use cannot be freed or an ["Illegal Function" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.** Change SCREEN modes before freeing.
* Once a specific image handle is no longer used or referenced by your program, it can be freed with \_FREEIMAGE.
* **Images are not deallocated when the [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") they are created in ends. Free them with \_FREEIMAGE.**
* **It is important to free unused or unneeded images with \_FREEIMAGE to prevent memory overflow errors.**
* **Do not try to free image handles currently being used as the active [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"). Change screen modes first.**
* **Note that calling \_FREEIMAGE only frees the handle. It does NOT reset the variable used to store the handle back to 0. (This is because 0 is often used as a short cut value for the current display, such as with \_DEST 0.)**


## Examples


*Example:* Loading a program splash screen and freeing image when no longer necessary:





| ``` s& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("SPLASH.BMP", 32) 'load 32 bit(24 BPP) image [IF](/qb64wiki/index.php/IF "IF") s& < -1 [THEN](/qb64wiki/index.php/THEN "THEN") [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") s& 'use image as a 32 bit SCREEN [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 6 'display splash screen for 6 seconds [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 'MUST change screen mode before freeing a SCREEN image! [IF](/qb64wiki/index.php/IF "IF") s& < -1 [THEN](/qb64wiki/index.php/THEN "THEN") _FREEIMAGE s& 'handle value MUST be less than -1 or error! [CLS](/qb64wiki/index.php/CLS "CLS")  ``` |
| --- |


*Note:* A valid image file name must be used by [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") or the invalid handle memory value will not need to be freed.
  




## See also


* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")
* [\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")
* [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")
* [\_SAVEIMAGE](/qb64wiki/index.php/SAVEIMAGE "SAVEIMAGE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FREEIMAGE&oldid=8684>"




## Navigation menu








### Search





















