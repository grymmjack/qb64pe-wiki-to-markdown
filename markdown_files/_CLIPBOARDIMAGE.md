


\_CLIPBOARDIMAGE - QB64 Phoenix Edition Wiki








# \_CLIPBOARDIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CLIPBOARDIMAGE statement copies a valid QB64 image to the clipboard.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_CLIPBOARDIMAGE = *existingImageHandle&*
  




## Description


* *existingImageHandle&* is a valid handle to a graphic QB64 image in memory, created with [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") or [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE").
* You can pass [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE"), [\_DEST](/qb64wiki/index.php/DEST "DEST") or [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") to copy the current source, destination or active display pages, as long as they are valid graphic images.
* SCREEN 0 handles (created either with [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") or passed using \_DEST while in a text screen) are not valid and will create an [Illegal Function Call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") or [Invalid Handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error.


  




## Availability


* [![v1.2](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v1.2")

**v1.2**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


* Available for *macOS* and *Linux* since **QB64-PE v3.13.0**


  




## Examples


Example
Create a sample image and copy it to the clipboard:


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32)  'Create image in memory: canvas& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(300, 200, 32) [_DEST](/qb64wiki/index.php/DEST "DEST") canvas&  'Draw some random rectangles: [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") 100     [LINE](/qb64wiki/index.php/LINE "LINE") (-100 + [RND](/qb64wiki/index.php/RND "RND") * [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)"), -100 + [RND](/qb64wiki/index.php/RND "RND") * [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT"))-[STEP](/qb64wiki/index.php/STEP "STEP")([RND](/qb64wiki/index.php/RND "RND") * 150, [RND](/qb64wiki/index.php/RND "RND") * 150), [_RGB](/qb64wiki/index.php/RGB "RGB")([RND](/qb64wiki/index.php/RND "RND") * 255, [RND](/qb64wiki/index.php/RND "RND") * 255, [RND](/qb64wiki/index.php/RND "RND") * 255), BF [NEXT](/qb64wiki/index.php/NEXT "NEXT") [LINE](/qb64wiki/index.php/LINE "LINE") (0, 0)-([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") - 1, [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") - 1), [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255), B [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 0, 0), [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255) m$ = " Hello, world! " [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") ([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") / 2 - [_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH")(m$) / 2, [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") / 2 - [_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT") / 2), m$  'Show the image: [_DEST](/qb64wiki/index.php/DEST "DEST") 0 [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") ([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") / 2 - [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(canvas&) / 2, [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") / 2 - [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(canvas&) / 2), canvas& [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Image generated."  'Copy to the clipboard: _CLIPBOARDIMAGE = canvas&  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Image copied to clipboard."  ``` |
| --- |


Example by Fellippe Heitor
  




## See also


* [\_CLIPBOARDIMAGE](/qb64wiki/index.php/CLIPBOARDIMAGE_(function) "CLIPBOARDIMAGE (function)") (function - used to paste an image from the clipboard)
* [\_CLIPBOARD$](/qb64wiki/index.php/CLIPBOARD$ "CLIPBOARD$"), [\_CLIPBOARD$ (function)](/qb64wiki/index.php/CLIPBOARD$_(function) "CLIPBOARD$ (function)") (used to copy/paste text)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CLIPBOARDIMAGE&oldid=8844>"




## Navigation menu








### Search





















