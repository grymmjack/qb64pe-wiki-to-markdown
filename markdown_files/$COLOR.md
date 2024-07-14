


$COLOR - QB64 Phoenix Edition Wiki








# $COLOR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**$COLOR** is a metacommand that adds named color constants into a program, which then can be used instead of hardcoded literal color values.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


$COLOR**:**{0|32}
  




## Parameters


* The one and only parameter is a literal number designating either to include [SCREEN 0](/qb64wiki/index.php/SCREEN "SCREEN") based color indexes, or full [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") color values with full (opaque) alpha.


  




## Description


* **$COLOR:0** adds constants for the colors 0-15 available in **SCREEN 0**, these do also match for the first 16 colors on 8-Bit (256 colors) graphic screens as long as they are not changed using [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE") or [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR"). For the actual constant names see [$COLOR:0 Name Table](https://qb64phoenix.com/qb64wiki/resources/Color0.html).
* **$COLOR:32** adds constants for full 32-Bit color values as used on 32-Bit screens created via [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), similar to HTML color names. For the actual constant names see [$COLOR:32 Name Table](https://qb64phoenix.com/qb64wiki/resources/Color32.html).
* Prior to QB64-PE v0.5.0, **$COLOR** was not compatible with [$NOPREFIX](/qb64wiki/index.php/$NOPREFIX "$NOPREFIX").
* Since QB64-PE v0.5.0, **$COLOR** can now be used with [$NOPREFIX](/qb64wiki/index.php/$NOPREFIX "$NOPREFIX"), with a few notable differences to three conflicting colors -- Red, Green, Blue.


Red would conflict with [\_RED](/qb64wiki/index.php/RED "RED"), Green would conflict with [\_GREEN](/qb64wiki/index.php/GREEN "GREEN"), and Blue would conflict with [\_BLUE](/qb64wiki/index.php/BLUE "BLUE"), once the underscore was removed from those commands with [$NOPREFIX](/qb64wiki/index.php/$NOPREFIX "$NOPREFIX").

To prevent these conflicts, the [COLOR](/qb64wiki/index.php/COLOR "COLOR") values have had **NP\_** prepended to the front of them, to distinguish them from the non-prefixed command names. All other color names remain the same, with only the three colors in conflict having to use **NP\_** (for **N**o **P**refix) in front of them.
  




## Examples


Example 1
Adding named color constants for SCREEN 0.


| ``` $COLOR:0  [COLOR](/qb64wiki/index.php/COLOR "COLOR") BrightWhite, Red [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Bright white on red."  ``` |
| --- |




| ``` Bright white on red.  ``` |
| --- |




---


Example 2
Adding named color constants for 32-bit modes.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 400, 32) $COLOR:32  [COLOR](/qb64wiki/index.php/COLOR "COLOR") CrayolaGold, DarkCyan [PRINT](/qb64wiki/index.php/PRINT "PRINT") "CrayolaGold on DarkCyan."  ``` |
| --- |




| ``` CrayolaGold on DarkCyan.  ``` |
| --- |




---


Example 3
Adding named color constants for 32-bit modes (with $NOPREFIX in effect).


| ``` [$NOPREFIX](/qb64wiki/index.php/$NOPREFIX "$NOPREFIX")  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 400, 32) $COLOR:32  [COLOR](/qb64wiki/index.php/COLOR "COLOR") NP_Red, White 'notice the NP_ in front of Red? 'This is to distinguish the color from the command with $NOPREFIX. [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Red on White."  ``` |
| --- |




| ``` Red on White.  ``` |
| --- |


  




## See also


* [COLOR](/qb64wiki/index.php/COLOR "COLOR")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")
* [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand")
* [$COLOR:0 Name Table](https://qb64phoenix.com/qb64wiki/resources/Color0.html)
* [$COLOR:32 Name Table](https://qb64phoenix.com/qb64wiki/resources/Color32.html)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$COLOR&oldid=8975>"




## Navigation menu








### Search





















