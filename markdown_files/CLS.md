


CLS - QB64 Phoenix Edition Wiki








# CLS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **CLS** statement clears the [current write page](/qb64wiki/index.php/DEST "DEST") or the designated image.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


CLS [*method%*] [, *bgColor&*] [, *imageHandle&*]
  




## Parameters


* *method%* specifies which parts of the page to clear, and can have one of the following values:
	+ **CLS** - clears the active graphics or text viewport or the entire text screen and refreshes bottom function [KEY ON](/qb64wiki/index.php/KEY_LIST "KEY LIST") line.
	+ **CLS** 0 - Clears the entire page of text and graphics. Print cursor is moved to row 1 at column 1.
	+ **CLS** 1 - Clears only the graphics view port. Has no effect for text mode.
	+ **CLS** 2 - Clears only the text view port. The print cursor is moved to the top row of the text view port at column 1.
* The *bgColor&* specifies the color attribute or palette index to use when clearing the screen in **QB64**.
* *imageHandle&* specifies an image handle to clear. If it is not specified, then **CLS** clears the [current write page](/qb64wiki/index.php/DEST "DEST").


  




## Description


* In legacy [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes *bgColor&* specifies the color attribute of the background.
* For 32-bit graphics mode, *bgColor&* specifies the [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") or [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32") color to use.
* **32-bit screen surface backgrounds (black) have zero [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") so that they are transparent when placed over other surfaces.**
	+ Use **CLS** or [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") to make a new surface background [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") 255 or opaque.
* If not specified, *bgColor&* is assumed to be the current background color. 32-bit backgrounds will change to opaque.
* If *bgColor&* is not a valid attribute, an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* Use [\_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE") to allow the background colors to be visible through the text or the text background.


  




## Availability


* [![v0.610](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v0.610")

**v0.610**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


* In **QB64-PE v3.10.0** support for clearing images was added.


  




## Examples


*Example 1:* Printing black text on a white background in QB64.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 CLS , 15 [_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE")  _KEEPBACKGROUND        'keeps the text background visible [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This is black text on a white background!" K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1  ``` |
| --- |


*Explanation:* [\_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE") can be used with [PRINT](/qb64wiki/index.php/PRINT "PRINT") or [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") to make the text or the text background transparent.
  

*Example 2:* You don't need to do anything special to use a .PNG image with alpha/transparency. Here's a simple example:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) CLS , [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 255, 0) i = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")(**"qb64_trans.png"**) 'see note below examples to get the image [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 0), i 'places image at upper left corner of window w/o stretching it   ``` |
| --- |


*Explanation:* When QB64 loads a .PNG file containing a transparent color, that color will be properly treated as transparent when \_PUTIMAGE is used to put it onto another image. You can use a .PNG file containing transparency information in a 256-color screen mode in QB64. CLS sets the [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") setting using [\_RGB](/qb64wiki/index.php/RGB "RGB").
  




## See also


* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")
* [\_RGB](/qb64wiki/index.php/RGB "RGB"), [\_RGBA](/qb64wiki/index.php/RGBA "RGBA"), [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32"), [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")
* [VIEW PRINT](/qb64wiki/index.php/VIEW_PRINT "VIEW PRINT"), [VIEW](/qb64wiki/index.php/VIEW "VIEW")
* [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CLS&oldid=8603>"




## Navigation menu








### Search





















