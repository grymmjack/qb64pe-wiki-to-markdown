


WIDTH - QB64 Phoenix Edition Wiki








# WIDTH



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **WIDTH** statement changes the text dimensions of certain **SCREEN** modes or devices.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


For SCREEN
* **WIDTH** [*columns%*] [,*rows%*]

For CONSOLE (Windows Console Only)
* **WIDTH** [*columns%*] [,*rows%*] [,*buffer\_columns%*] [,*buffer\_rows%*]

For Files
* **WIDTH** *file\_number | device*, *columnwidth%*

  




## Parameters


* When parameters are not specified, columns defaults to 80 with 25 (30 in [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 11 or 12) rows.


  




## Description


* **WIDTH** should be used after a program [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") statement. It does not affect screen graphics or graphic coordinates.
* Affects SCREEN 0 Window size and alters the text block size of each screen mode listed in QBasic:


* SCREEN 0 can use 80 or 40 columns and 25, 43 or 50 rows. Default is **WIDTH** 80, 25.
* SCREEN 9 can use 80 columns and 25 or 43(not supported on many monitors) rows. Default **WIDTH** 80, 25 fullscreen.
* SCREEN 10 can use 80 columns and 25 or 43 rows. Default is **WIDTH** 80, 25 fullscreen.
* SCREEN 11 and 12 can use 80 columns and 30 or 60 rows. Default is **WIDTH** 80, 30 fullscreen.

* **QB64** can alter all [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode widths and heights which may also affect text or [\_FONT](/qb64wiki/index.php/FONT "FONT") block sizes.
* If a [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") window is active and you set [\_DEST](/qb64wiki/index.php/DEST "DEST") [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE"), **WIDTH** will affect the console output window size (Windows only), with the last two optional parameters setting the buffer size for the console. (For example, you can set a console to be 80 characters x 25 lines for the display, with a buffer size of 300 characters and 100 lines, which allows you to display that much information and navigate the visible display with the scroll bars.)


Note
* **WIDTH** changes may change screen color settings in QBasic. Use [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE") to reset to default colors.
* **WIDTH LPRINT** is not supported in QB64.

  




## Examples


Example 1
* Showing the use of the buffer parameters for [$CONSOLE](/qb64wiki/index.php/$CONSOLE "$CONSOLE") usage.
* The program creates more output than fits to the display, but the buffer preserves the output and you can scroll back and forth.



| ``` [$CONSOLE:ONLY](/qb64wiki/index.php/$CONSOLE "$CONSOLE") WIDTH 80, 25, 300, 100 [CLS](/qb64wiki/index.php/CLS "CLS") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") 97     [PRINT](/qb64wiki/index.php/PRINT "PRINT") i [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(100, "0") + [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(100, "1") + [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(100, "2") 'print the 100's placeholders [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") j = 1 [TO](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") 3     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") 9         [PRINT](/qb64wiki/index.php/PRINT "PRINT") [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(10, [_TRIM$](/qb64wiki/index.php/TRIM$ "TRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(i))); 'print the 10's placeholders     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") j = 1 [TO](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") 30     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") 9         [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_TRIM$](/qb64wiki/index.php/TRIM$ "TRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(i)); 'print the 1's placeholders.     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1276)
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [COLOR](/qb64wiki/index.php/COLOR "COLOR"), [OUT](/qb64wiki/index.php/OUT "OUT")
* [\_PRINTWIDTH](/qb64wiki/index.php/PRINTWIDTH "PRINTWIDTH")
* [\_WIDTH (function)](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)"), [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")
* [\_FONT](/qb64wiki/index.php/FONT "FONT"), [\_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH"), [\_FONTHEIGHT](/qb64wiki/index.php/FONTHEIGHT "FONTHEIGHT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=WIDTH&oldid=8922>"




## Navigation menu








### Search





















