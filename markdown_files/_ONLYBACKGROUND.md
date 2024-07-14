


\_PRINTMODE - QB64 Phoenix Edition Wiki








# \_PRINTMODE



From QB64 Phoenix Edition Wiki
(Redirected from [ONLYBACKGROUND](/qb64wiki/index.php?title=ONLYBACKGROUND&redirect=no "ONLYBACKGROUND"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_PRINTMODE statement sets the text or [\_FONT](/qb64wiki/index.php/FONT "FONT") printing mode on an image when using [PRINT](/qb64wiki/index.php/PRINT "PRINT") or [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING").


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_PRINTMODE {*\_KEEPBACKGROUND*|*\_ONLYBACKGROUND*|*\_FILLBACKGROUND*}[, *imageHandle&*]
  




## Parameters


* One of 3 mode keywords is mandatory when using this statement to deal with the text background.
	+ *\_KEEPBACKGROUND* (mode 1): Text background transparent. Only the text is displayed over anything behind it.
	+ *\_ONLYBACKGROUND* (mode 2): Text background only is displayed. Text is transparent to anything behind it.
	+ *\_FILLBACKGROUND* (mode 3): Text and background block anything behind them like a normal [PRINT](/qb64wiki/index.php/PRINT "PRINT"). **Default setting.**
* If the optional *imageHandle&* is omitted or is 0 then the setting will be applied to the current [destination](/qb64wiki/index.php/DEST "DEST") image.


  




## Description


* Use the [\_PRINTMODE (function)](/qb64wiki/index.php/PRINTMODE_(function) "PRINTMODE (function)") to find the current \_PRINTMODE setting mode number for an image.
* **The \_PRINTMODE statement and function can only be used on graphic images, not text-based ones such as SCREEN 0**


  




## Examples


*Example:* Using \_PRINTMODE with [PRINT](/qb64wiki/index.php/PRINT "PRINT") in a graphic screen mode. The background used is CHR$(219) = █





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 8: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(3, 219) 'background _PRINTMODE _KEEPBACKGROUND [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") _PRINTMODE [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [\_PRINTMODE (function)](/qb64wiki/index.php/PRINTMODE_(function) "PRINTMODE (function)")
* [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING")
* [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")
* [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [\_PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PRINTMODE&oldid=6688>"




## Navigation menu








### Search





















