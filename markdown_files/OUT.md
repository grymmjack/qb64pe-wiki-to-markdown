


OUT - QB64 Phoenix Edition Wiki








# OUT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
OUT writes values to register and port hardware addresses.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Color Port Palette access using OUT](#Color_Port_Palette_access_using_OUT) 	+ [4.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


OUT *registerAddress%*, *value%*
  




## Parameters


* *registerAddress%* is a value expressed as a decimal [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [hexadecimal](/qb64wiki/index.php/%26H "&H").
* The [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") *value%* sent is normally only 0 to 255 per byte register (8 bit) address.


  




## Description


* **QB64 has limited access to registers. VGA memory and registers are emulated.**
* OUT can be used to change color port and a limited number of other port settings in QB64.
* Some settings may be set in a specific order to gain access to settings and [INP](/qb64wiki/index.php/INP "INP") reads.
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes determine the number of available color palette attributes from 2 to 256 in SCREEN 13.
* Windows NT may block access to Parallel printer and Serial ports. See [Port Access Libraries](/qb64wiki/index.php/Port_Access_Libraries "Port Access Libraries") or other DLLs.
* [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR") can also be used to set RGB intensity values using [32 bit color](/qb64wiki/index.php/RGB32 "RGB32") values.
* OUT can toggle the blinking attribute of SCREEN 0 color 16-31 for legacy code. [\_BLINK](/qb64wiki/index.php/BLINK "BLINK") is the preferred method. (starting with build 20170816/61).


  




## Color Port Palette access using OUT


OUT &H3C7, attribute : Set port to read RGB settings for start attribute
[INP](/qb64wiki/index.php/INP "INP") &H3C9, colorIntensity : Reads RGB color intensity settings in order
OUT &H3C8, attribute : Set port to write RGB settings for start attribute
OUT &H3C9, colorIntensity : Writes RGB color intensity settings in order
* Every 3 reads or writes, changes to next color attribute without a set
* Color setting is Red, Green and Blue attribute intensities in order.
* Color attribute intensity values range from 0 to 63.
* Some [DAC](/qb64wiki/index.php/DAC "DAC") color attribute intensities cannot be changed using OUT.

### QBasic/QuickBASIC


* In DOS, OUT accesses memory and hardware directly, unlike [POKE](/qb64wiki/index.php/POKE "POKE"), and could cause PC damage.


  




## Examples


*Example 1:* Reading the default RGB color settings of color attribute 15.





| ``` OUT &H3C7, 15      'set color port attribute 15 for a read red% = [INP](/qb64wiki/index.php/INP "INP")(&H3C9) green% = INP(&H3C9) blue% = INP(&H3C9) PRINT red%, green%, blue%  ``` |
| --- |




| ```  63       63       63  ``` |
| --- |


  

*Example 2:* Changing the color intensity settings of the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") background [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0 to bright white.





| ``` OUT &H3C8, 0  'attribute number. 0 for black screen background OUT &H3C9, 63 'red OUT &H3C9, 63 'green OUT &H3C9, 63 'blue  ``` |
| --- |


*Explanation:* In [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 this is one way to make high intensity background colors. [COLOR](/qb64wiki/index.php/COLOR "COLOR") ,15 is actually grey (7).
  

*Example 3:* Toggling blinking colors in SCREEN beginning with build 20170816/61





| ``` OUT &H3C0, &H10  'disables blinking and enables high intensity backgrounds (colors 16-31) OUT &H3C0, 2 ^ 3 'reenables blinking and disables high intensity backgrounds  (colors 16-31)  ``` |
| --- |


Note: In QB64, the recommended practice is to use the [\_BLINK](/qb64wiki/index.php/BLINK "BLINK") {ON|OFF} statement.
  

*Example 4:* Restoring colors to a bitmap from the Red, Green and Blue [BSAVEd](/qb64wiki/index.php/BSAVE "BSAVE") indexed array of color values.





| ```  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  OUT [&H](/qb64wiki/index.php/%26H "&H")3C8, 0 ' set color port for output at attribute 0  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 47 ' 48 RGB values is (3 * 16) -1 color attributes from 0 in screen 12    OUT [&H](/qb64wiki/index.php/%26H "&H")3C9, Image%(i) ' changes to next attribute after 3 RGB loops  [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")(clm, row), Image(48) PSET  ``` |
| --- |


*Explanation:* The color RGB intensity settings were imported from a file to the Image array using [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD"). The color attribute advances to the next one every 3 writes using OUT. The color information was indexed to the start of the array. The image is after the color settings at index 48. Index 48 is the [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") image width and 49 is the height.
  




## See also


* [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE"), [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR")
* [INP](/qb64wiki/index.php/INP "INP")
* [PEEK](/qb64wiki/index.php/PEEK "PEEK")
* [POKE](/qb64wiki/index.php/POKE "POKE")
* [COLOR](/qb64wiki/index.php/COLOR "COLOR"), [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")
* [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE"), [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD")
* [\_BLINK](/qb64wiki/index.php/BLINK "BLINK"), [\_BLINK (function)](/qb64wiki/index.php/BLINK_(function) "BLINK (function)")
* [Port Access Libraries](/qb64wiki/index.php/Port_Access_Libraries "Port Access Libraries")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OUT&oldid=8991>"




## Navigation menu








### Search





















