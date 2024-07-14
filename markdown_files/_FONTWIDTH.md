


\_FONTWIDTH - QB64 Phoenix Edition Wiki








# \_FONTWIDTH



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_FONTWIDTH function returns the font width of a MONOSPACE font handle created by [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT").


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


*pixelWidth%* = \_FONTWIDTH[(*fontHandle&*)]
  




* Returns the character width of the last font used if a handle is not specified.
* **Variable width fonts always return *pixelWidth%* = 0.** Even fixed width fonts return 0 unless the ["MONOSPACE"](/qb64wiki/index.php/LOADFONT "LOADFONT") style option is used.
* QB64 **version 1.000 and up** can load a variable width font as monospaced with the ["MONOSPACE"](/qb64wiki/index.php/LOADFONT "LOADFONT") style parameter.
* The font width is generally 3/4 of the [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT") specified when loading the font.
* In **graphics** [screen](/qb64wiki/index.php/SCREEN "SCREEN") modes, [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH") can return the total **pixel width** of a literal or variable [string](/qb64wiki/index.php/STRING "STRING") of text.


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1145)
* [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT")
* [\_FONT](/qb64wiki/index.php/FONT "FONT")
* [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")
* [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FONTWIDTH&oldid=8894>"




## Navigation menu








### Search





















