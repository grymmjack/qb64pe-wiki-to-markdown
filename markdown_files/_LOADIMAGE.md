


\_LOADIMAGE - QB64 Phoenix Edition Wiki








# \_LOADIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_LOADIMAGE** function loads an image into memory and returns valid [LONG](/qb64wiki/index.php/LONG "LONG") image handle values that are less than -1.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) 	+ [3.1 Errors](#Errors) * [4 Availability](#Availability) * [5 Examples](#Examples) 	+ [5.1 More examples](#More_examples) * [6 See also](#See_also) |
| --- |


## Syntax


*handle&* = \_LOADIMAGE(*fileName$*[, [*mode&*][, *requirements$*)
  




## Parameters


* *filename$* is literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") file name value.
* Optional *mode&* [LONG](/qb64wiki/index.php/LONG "LONG") values can be:
	+ 32 = 32-bit image.
	+ 33 = 32-bit hardware image.
	+ 256 = 8-bit (256 color) image using the QB64-PE master palette.
	+ 257 = 8-bit (256 color) image using an adaptive palette.
* Optional *requirements$* [STRING](/qb64wiki/index.php/STRING "STRING") values can be a combination of (**version 3.6.0 and up**):
	+ **HARDWARE**: Loads the image as a 32-bit hardware image. This can be used instead of mode **33** (above).
	+ **ADAPTIVE**: Loads the image as an 8-bit (256 color) image using an adaptive palette. This can be used instead of mode **257** (above).
	+ **MEMORY**: This will treat filename$ as a memory buffer containing the image file instead of a file name.
	+ **SXBR2**: Applies the Super-xBR 2x pixel scaler on the image.
	+ **MMPX2**: Applies the MMPX Style-Preserving 2x pixel scaler on the image.
	+ **HQ2XA**: Applies the High Quality Cartoon 2x pixel scaler on the image.
	+ **HQ2XB**: Applies the High Quality Complex 2x pixel scaler on the image.
	+ **HQ3XA**: Applies the High Quality Cartoon 3x pixel scaler on the image.
	+ **HQ3XB**: Applies the High Quality Complex 3x pixel scaler on the image.


  




## Description


* Image file formats **JPG, PNG, TGA, BMP, PSD, GIF, HDR, PIC, PNM, PCX, SVG and QOI** are supported. A path can also be given.
* The *mode&* parameter can be 32, 33,256 or 257. Omit to use the current graphic screen settings.
* Mode 33 images are **hardware** accelerated and are created using \_LOADIMAGE or [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE") (**version 1.000 and up**).
* Mode 256 images are loaded using the QB64-PE master VGA palette. This is the same palette that is used for 256 color screens like [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13.
* Mode 257 images are loaded using an adaptive palette making these images look better than mode 256 when used with 32-bit color screens (**version 3.1.0 and up**).
* Loaded images can be read invisibly using [POINT](/qb64wiki/index.php/POINT "POINT"). Image coordinates start at 0 up to the [\_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") - 1 and [\_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") - 1.
* Images can be made into a program [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") or page adopting the size and palette settings or placed using [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE").
* Returns -1 as an invalid handle if it can't load the image. Valid [LONG](/qb64wiki/index.php/LONG "LONG") handle returns are less than -1 (*handle&* < -1).
* Valid images only need to be loaded once. The handle can be used repeatedly until freed.
* **Images are not deallocated when the [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") they are created in ends. Free them with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE").**
* Use the various pixel scalers to scale and load extremely low resolution (retro) graphics without blurring.


### Errors


* Some picture file images may not load when a *mode&* value is designated. Try loading it without a *mode&* designation.
* **It is important to free unused or discarded images with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") to prevent CPU memory overflow errors.**
* **In text-only [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0, *mode&* 32 must be specified.** When loading an [\_ICON](/qb64wiki/index.php/ICON "ICON") image use 32 for the *mode&* too.


  




## Availability


* [![v0.800](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v0.800")

**v0.800**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


* Mode 33 was added in **QB64 v1.0**, which makes it also available in **all QB64-PE** versions.
* Mode 257 was added in **QB64-PE v3.1.0**, hence it's **not available** in the original **QB64** versions.
* In **QB64-PE v3.6.0** this function got a new optional parameter *requirements$* and the ability to load image files from memory.
* SVG and QOI support was added in **QB64-PE v3.9.0**.
* Pixel scaler support was added in **QB64-PE v3.9.0**.


  




## Examples


Example 1
To display an image in 32-bit color using its resolution as a program screen.


| ``` i& = _LOADIMAGE("mypic.jpg", 32) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") i&  ``` |
| --- |




---


Example 2
[DRAWing](/qb64wiki/index.php/DRAW "DRAW") and rotating an image 360 degrees using Turn Angle. [POINT](/qb64wiki/index.php/POINT "POINT") is used to read the invisible image source.


| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32) img& = _LOADIMAGE("QB64.PNG")                           'use any 24/32 bit image  wide% = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(img&): deep% = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(img&) TLC$ = "BL" + [STR$](/qb64wiki/index.php/STR$ "STR$")(wide% \ 2) + "BU" + [STR$](/qb64wiki/index.php/STR$ "STR$")(deep% \ 2)  'start draw at top left corner RET$ = "BD BL" + [STR$](/qb64wiki/index.php/STR$ "STR$")(wide%)                            'return to left side of image [_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") img& [_DEST](/qb64wiki/index.php/DEST "DEST") 0 DO   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") angle% = 0 [TO](/qb64wiki/index.php/TO "TO") 360 [STEP](/qb64wiki/index.php/STEP "STEP") 15     [CLS](/qb64wiki/index.php/CLS "CLS")     [DRAW](/qb64wiki/index.php/DRAW "DRAW") "BM400, 300" + "TA=" + [VARPTR$](/qb64wiki/index.php/VARPTR$ "VARPTR$")(angle%) + TLC$     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y = 0 [TO](/qb64wiki/index.php/TO "TO") deep% - 1       [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") x = 0 [TO](/qb64wiki/index.php/TO "TO") wide% - 1         [DRAW](/qb64wiki/index.php/DRAW "DRAW") "C" + [STR$](/qb64wiki/index.php/STR$ "STR$")([POINT](/qb64wiki/index.php/POINT "POINT")(x, y)) + "R1"            'color and DRAW each pixel       [NEXT](/qb64wiki/index.php/NEXT "NEXT")       [DRAW](/qb64wiki/index.php/DRAW "DRAW") RET$     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")                         'NOTE: CPU usage will be HIGH!   [NEXT](/qb64wiki/index.php/NEXT "NEXT") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") > ""  ``` |
| --- |


Code by Ted Weissgerber


---


Example 3
Load and scale an image from memory and display it on the screen.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [DIM](/qb64wiki/index.php/DIM "DIM") Bee& '                                               the image file [DIM](/qb64wiki/index.php/DIM "DIM") cx%, cy% '                                           center x,y coordinate for image  [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") Data_tbee0_png_2314 Bee& = _LOADIMAGE(LoadResource, 32, "memory, hq3xa") '   load image file from memory and scale it using a pixel scaler [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) '                         enter a graphics screen [CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(127, 127, 127) '                            clear the screen with gray [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 15 '                                           position text cursor [PRINT](/qb64wiki/index.php/PRINT "PRINT") "An image loaded into memory and placed on the screen." cx% = (640 - [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(Bee&)) \ 2 '                         calculate x center position cy% = (480 - [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(Bee&)) \ 2 '                        calculate y center position [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (cx%, cy%), Bee& '                             place image onto center of screen [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") '                                                  wait for key stroke [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") Bee& '                                        remove image from memory [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM") '                                                 return to OS   Data_tbee0_png_2314: [DATA](/qb64wiki/index.php/DATA "DATA") 2314,2988,-1 [DATA](/qb64wiki/index.php/DATA "DATA") eJx1VmdUU9kWDiihKDGEariKEKzUoV4FHWMgCYj0iVIVKeIocgNKiSCIkQuEZGBQRARxgCdNLNRQFYgE [DATA](/qb64wiki/index.php/DATA "DATA") pGMARYOSCCqiSAkgUia8f28t3zrfPvtb31lnn732+bF3oqM9SV4OK4dAIORtyFbOYg+vmwxSvFt+tF0/ [DATA](/qb64wiki/index.php/DATA "DATA") QJ4+SrJCrK2vew0FaWJFFiK7hSIQKM66SdzUQakjEDLFNlZ414jhr3wPO6XjAPJ7V4D6yajg4eHaeQx/ [DATA](/qb64wiki/index.php/DATA "DATA") 7iqd7Pt2sNckOvBk8pNWtXNM5hOOmguzyMk3YSFCVqEeaS25T0YyLjYpFk23flFcKIp3biLzZgI1jjUe [DATA](/qb64wiki/index.php/DATA "DATA") yriNaumc9Oye7DTKab9l/cprfEaYtZZ121hdEn1arRTCGXKa0NIEYDP1f0nLr0Qx+aVINfylyEl101GU [DATA](/qb64wiki/index.php/DATA "DATA") w9uirxhQ0dLryI+G/ZemdqAEO1Al7V1d1hcu6C/zPjBovyt8IQIc/DpY4Qlp2/JEw12huF5G4dIR3owi [DATA](/qb64wiki/index.php/DATA "DATA") CUu1ynOSlUDYLR7AMuNAyRAlDJOowCSObfNDwjM1trp4sFhhnrhQq0Ot/qKLPPCCWpe3uXr4aOp5PXxZ [DATA](/qb64wiki/index.php/DATA "DATA") 5UZfnM1b9kUlb0FK2MMQWOdqYZ7Isu6wlYBN/bynlfj3TFXDgHfSm23+7JeR2PC6boF3+E5L7jR7TXL7 [DATA](/qb64wiki/index.php/DATA "DATA") /IAAPxW5PBCNKoIqstpJwbM+2lhGLx9CD33Z1PtHOCLb9Of7+XjKpCvisINvav3sf3KKfPbEjLw8of10 [DATA](/qb64wiki/index.php/DATA "DATA") EIW26HjrVr7F65I01NCI4MtLpwbqHhGHEEdySBRecVDePneX29LobvntaWzFezUsm15QnWmYUS+TCh7o [DATA](/qb64wiki/index.php/DATA "DATA") nsJfHtBnX+KdohNKRI5rnShUnchaLF3MerchFUSmqU7PURTjkfp4kDV6+fhvJtDWMCrC8HpeaYi0u05V [DATA](/qb64wiki/index.php/DATA "DATA") kx5wkGkdwuPHY+BaC6en3fJAqfKbXkrNhgAI8ZgpnLI4bhg1tQ8QRqy+xxK/VTftRZXrwfS8MbtDD28E [DATA](/qb64wiki/index.php/DATA "DATA") WxczDVaOVireEMV5f/WhE3R21aIjXycPCm1/UMTJw8qAvTtKltu2YmYZA8lXQfURPNlHVE/9N3Hj/ccg [DATA](/qb64wiki/index.php/DATA "DATA") dZiCnzBjiSnbs0rKWxgxXaiYDiWjwpocwExbM4GgXR4yCrsHtwSi7bbAab8xGbvN7xX54Zbpvhcfb7oP [DATA](/qb64wiki/index.php/DATA "DATA") 1Uf1b+gDHwwCNBCbNJS3ujgFGbXlSx3ZFKuitPuap4gbQyJM0xKeaeaOOwojfuRLx4Pe8qJmeSBXnBSJ [DATA](/qb64wiki/index.php/DATA "DATA") /6Sy8GAZUgsi96xVhzwEGg5wUKxh3DnH8PN6VgIob2z9xqN42j+JQlH5IT8M64tIqnB/BXbgemQmuZOn [DATA](/qb64wiki/index.php/DATA "DATA") 5o67R4PZASPHE3NrDbeYwhQhLRpPHI1YebBFCCXLL+AUqTe+eSZPNFu6bvO8HiqlwySacJUf2kOFXAse [DATA](/qb64wiki/index.php/DATA "DATA") 2K38wGqg6Y9C/U7C5+7nWxN9z7PX+ONYdZvmICD3HKvW95zEKUlW0gYdKGwt5CU4Yn87qdrlvpaSXPvJ [DATA](/qb64wiki/index.php/DATA "DATA") krVgFe7rlQ4n6qnnGwEEXQiVjDsK1NRttPTA/oEQMmg/5RU/c/CoU9VlWdtw/dairwzHsiBN+w8Gh6cH [DATA](/qb64wiki/index.php/DATA "DATA") f8ywzK4RaBfEDEx9itj5RkXAm7few69R86+7dS+qxzlrpM5OlXS/Crja8s+AfEZi2U0ZJZZd6f7kWmUc [DATA](/qb64wiki/index.php/DATA "DATA") MKFP7H6zsNrDwW2p0XmS1MK8sDPIlHSARcniAbc6qmSC9lfEt7mMOqo8Fpf4LH/5RGggKzSZqR09FIIm [DATA](/qb64wiki/index.php/DATA "DATA") LbmznqRqO6NynmInsl35SRf9bxmlkjmuDQqJgd4ef9Z5nN3jPWUBTDQZuJzxJ0nXfTBv/xCnhMBEGnOt [DATA](/qb64wiki/index.php/DATA "DATA") y0W9beM1qbKPKuMI/JBFCXiO9Cjc/nm/CLCnkk1JuU/azPXgvqLIBpcf3tVAYquWpimp2EVUZaB4Q+64 [DATA](/qb64wiki/index.php/DATA "DATA") hR5MBigeLPGb21EF/KS2dEKzT+WYo2rm2Zpni+LPrb8y+FEWVQeX0aSKtqN0pM5e8hlhswdCMpo0v6qf [DATA](/qb64wiki/index.php/DATA "DATA") 9IzW10vW8EDhAJrq7KfswtmZwJ3KKIUdnjnVWnr5d0xhL2ACb2gMZm2Oq7lKcAtNQKYO2hxz7tAszRri [DATA](/qb64wiki/index.php/DATA "DATA") J71MwGpWMnB9J7SrgbTTrXfUwcm7EQxiXoKVVvphcs/CEucOhpufifqsCoxCr1xv5X5zbx59HAzZvagp [DATA](/qb64wiki/index.php/DATA "DATA") 874bkRZWhYFv0lt8fhyst5w2K9rtfLkv5NX+YzkTSo2qeqQdAa8ZHM2Vjvb2pqz9oSlpadcmJ8/7+ftr [DATA](/qb64wiki/index.php/DATA "DATA") qjCY6pPYgybqeXCAMBJvdlfVr+PRyplFB+2ZgNyYoM2J9bc/LYk2Vawtb3VX6To8u/y5cG3UlxdlHtT8 [DATA](/qb64wiki/index.php/DATA "DATA") /oSuCoFCUSkrLx97p/EXd2xBORHnWH0KbWqquf0v35H6yASuMB4c8fT6pEYaM9fIXS5ZcBGkpJN4PPqz [DATA](/qb64wiki/index.php/DATA "DATA") kZwWXZSO8esKOds+sFOlwr0jSEU6eESSngxlSPiYdHQFAZSAV0U5vvRr4fNOVTsqf9p1lZkzCH4Smfvs [DATA](/qb64wiki/index.php/DATA "DATA") 010OdjSWh2kslzkYCeYJlKli3NInTmcfQ/0LHogzL8a23inZxL20l8a3fZfpxq7Rj280LU9Z/Oo11D/d [DATA](/qb64wiki/index.php/DATA "DATA") 8THQa2bvw2WTDcdmC/JGuQ6OP1dMXGN+KuxrXH1mhBb8t5es47u5nI66V20ALhvkhZ4p1TWm5m+Fb59l [DATA](/qb64wiki/index.php/DATA "DATA") En83Ni5MnxBxRl2AiRL2jRj+C1Lp1NHwzSY018ZH2R4EBbjFw8GjhntrcLYBu7GcxvUtHYTBje8Na+/c [DATA](/qb64wiki/index.php/DATA "DATA") GwJvDGVjYOmM5LDYgbi58Vo15Opiv7NTMQwOlE371lseqhdhSLu2V2GkqXYXAErPiyUJ0n0tTZQgIwrs [DATA](/qb64wiki/index.php/DATA "DATA") vFIW9wa0MjCmgov0XSVDl05s+2xivHT24xKmYVpN8B0ND7YV0uiuP/YwY/dpVBJtS4H7GBgWXU/rcaMO [DATA](/qb64wiki/index.php/DATA "DATA") 0/JDoxNaFs+f25NGTThR8EyYcqjUjdMamtQsk5jgPzu72+WnCrEXWlQgt7JS7JGALjna/dWf0VHxfQtG [DATA](/qb64wiki/index.php/DATA "DATA") 0YcZIKBUQIE2+t+RQsI3O2SzPVdJgEQxPk4OlwLOxeYveaOrXXb8smk3/Z+JgAC8lUkOW93AGx2tePu3 [DATA](/qb64wiki/index.php/DATA "DATA") 9ax4lEHYWNtbPTxyKu5fF0s/3Q==  ' Convert a base64 string to a normal string [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") DecodeBase64$ (s [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"))     [CONST](/qb64wiki/index.php/CONST "CONST") BASE64_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"      [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") buffer, result     [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") i     [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") char1, char2, char3, char4      [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") [LEN](/qb64wiki/index.php/LEN "LEN")(s) [STEP](/qb64wiki/index.php/STEP "STEP") 4         char1 = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(BASE64_CHARACTERS, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(s, i))) - 1         char2 = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(BASE64_CHARACTERS, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(s, i + 1))) - 1         char3 = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(BASE64_CHARACTERS, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(s, i + 2))) - 1         char4 = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(BASE64_CHARACTERS, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")(s, i + 3))) - 1         buffer = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([_SHL](/qb64wiki/index.php/SHL "SHL")(char1, 2) [OR](/qb64wiki/index.php/OR "OR") [_SHR](/qb64wiki/index.php/SHR "SHR")(char2, 4)) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([_SHL](/qb64wiki/index.php/SHL "SHL")(char2 [AND](/qb64wiki/index.php/AND "AND") 15, 4) [OR](/qb64wiki/index.php/OR "OR") [_SHR](/qb64wiki/index.php/SHR "SHR")(char3, 2)) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")([_SHL](/qb64wiki/index.php/SHL "SHL")(char3 [AND](/qb64wiki/index.php/AND "AND") 3, 6) [OR](/qb64wiki/index.php/OR "OR") char4)          result = result + buffer     [NEXT](/qb64wiki/index.php/NEXT "NEXT")      ' Remove padding     [IF](/qb64wiki/index.php/IF "IF") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(s, 2) = "==" [THEN](/qb64wiki/index.php/THEN "THEN")         result = [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(result, [LEN](/qb64wiki/index.php/LEN "LEN")(result) - 2)     [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(s, 1) = "=" [THEN](/qb64wiki/index.php/THEN "THEN")         result = [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(result, [LEN](/qb64wiki/index.php/LEN "LEN")(result) - 1)     [END IF](/qb64wiki/index.php/END_IF "END IF")      DecodeBase64 = result [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")   ' Loads a binary file encoded with Bin2Data ' Usage: '   1. Encode the binary file with Bin2Data '   2. Include the file or it's contents '   3. Load the file like so: '       Restore label_generated_by_bin2data '       Dim buffer As String '       buffer = LoadResource   ' buffer will now hold the contents of the file [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") LoadResource$     [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") ogSize, resize     [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") isCompressed      [READ](/qb64wiki/index.php/READ "READ") ogSize, resize, isCompressed ' read the header      [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") buffer, result      ' Read the whole resource data     [DO WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [LEN](/qb64wiki/index.php/LEN "LEN")(result) < resize         [READ](/qb64wiki/index.php/READ "READ") buffer         result = result + buffer     [LOOP](/qb64wiki/index.php/LOOP "LOOP")      ' Decode the data     buffer = DecodeBase64(result)      ' Expand the data if needed     [IF](/qb64wiki/index.php/IF "IF") isCompressed [THEN](/qb64wiki/index.php/THEN "THEN")         result = [_INFLATE$](/qb64wiki/index.php/INFLATE$ "INFLATE$")(buffer, ogSize)     [ELSE](/qb64wiki/index.php/ELSE "ELSE")         result = buffer     [END IF](/qb64wiki/index.php/END_IF "END IF")      LoadResource = result [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Adapted from example code by Terry Ritchie


---


Example 4
Load SVG vector graphics data from memory and display it on the screen.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT") [$RESIZE](/qb64wiki/index.php/$RESIZE "$RESIZE"):[SMOOTH](/qb64wiki/index.php/SMOOTH "SMOOTH")  [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") svg_data  [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") svg, buffer  [DO](/qb64wiki/index.php/DO "DO")     [READ](/qb64wiki/index.php/READ "READ") buffer     svg = svg + buffer [LOOP WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [LEN](/qb64wiki/index.php/LEN "LEN")(buffer) > 0  [DIM](/qb64wiki/index.php/DIM "DIM") img [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): img = _LOADIMAGE(svg, 32, "memory")  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(img) \ 2, [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(img) \ 2, 32)  [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , img  [END](/qb64wiki/index.php/END "END")  svg_data: [DATA](/qb64wiki/index.php/DATA "DATA") "<svg xmlns='http://www.w3.org/2000/svg' width='1000pt' height='1000pt' viewBox='0 0 1000 1000'><g fill='#201701'" [DATA](/qb64wiki/index.php/DATA "DATA") "><path d='M107 94c-3-1 2-4 2-1l-2 1ZM96 672h35l24 168 220-43 4 21-255 42-28-188ZM521 768l41-8 5 25c0 2-3 3-4 3l-" [DATA](/qb64wiki/index.php/DATA "DATA") "36 6-6-26Z' opacity='.1'/></g><g fill='#020092'><path d='m107 94 2-1 683 134 76 328 2 7 23 101-176 35-3-5-24-104" [DATA](/qb64wiki/index.php/DATA "DATA") " 108-11 14 65 59-9-40-168h-60l17 78-84 7-18-82c0-1 0-3-2-2h-21l-17-71 169 7-12-54-26-1c-5-16-8-32-11-49 9 1 17 3" [DATA](/qb64wiki/index.php/DATA "DATA") " 26 3l-12-53-220-38 29 146c-25-3-50-9-74-14l-28-144-329-57 20 134c-15-1-30-5-46-8v-1L107 94Z'/><path d='m284 200" [DATA](/qb64wiki/index.php/DATA "DATA") " 140 22 6 33-25-2c4 23 9 46 12 70l-116-23h-1l-16-100ZM640 255l90 13 7 34-85-11c-2 0-5 0-5-3l-7-33ZM137 300l46 8 " [DATA](/qb64wiki/index.php/DATA "DATA") "10 69 31 1c3 28 9 56 13 85l80 5 8 2-120 1 3 22-43-2-28-191ZM305 330l77 13c2 0 4 2 4 4-26 0-53-3-79-4l-2-13ZM656 " [DATA](/qb64wiki/index.php/DATA "DATA") "330l89 8 9 39-89-5-9-42ZM519 368c8-1 16 2 24 3l50 8 4 15c11 1 23 0 35 2l7 33-22-2 9 40h-16l9 44c-20-1-41-1-61-3-" [DATA](/qb64wiki/index.php/DATA "DATA") "6 0-12 0-18-2l31-1-3-17 38 3c-1-11-4-21-7-31-24-2-48-6-72-7l3 15-60 1c-5-27-12-54-15-81l59 3 6 28 72 9-5-27-63-9" [DATA](/qb64wiki/index.php/DATA "DATA") "-5-24ZM325 425l77 1 8 43-77 1c-3-15-7-30-8-45Z'/></g><path fill='#00bbfd' d='m158 142 329 57 28 144 4 25 5 24-10" [DATA](/qb64wiki/index.php/DATA "DATA") "-1-59-3-27-1 7 39h-33l-77-1-7-43-94-4-31-1-10-69-5-32-20-134m126 58 16 100h1c0 10 3 20 4 30l2 13c26 1 53 4 79 4l" [DATA](/qb64wiki/index.php/DATA "DATA") "36 3-5-27c-3-24-8-47-12-70l25 2-6-33-140-22Z'/><path fill='#037efe' d='m560 211 220 38 12 53c-9 0-17-2-26-3 3 17" [DATA](/qb64wiki/index.php/DATA "DATA") " 6 33 11 49l26 1 12 54-169-7h-14c-12-2-24-1-35-2l-4-15-4-22-29-146m80 44 7 33c0 3 3 3 5 3l85 11-7-34-90-13m16 75" [DATA](/qb64wiki/index.php/DATA "DATA") " 9 42 89 5-9-39-89-8Z'/><g fill='#070636'><path d='m71 256 61 11v1c2 11 4 21 4 32l-23-4 29 195c8 1 16-2 23 3l11 " [DATA](/qb64wiki/index.php/DATA "DATA") "75h-24c7 38 12 76 17 114l16 106 22-4 2 13 446-88c5 2 10 0 14 0l35-6v-4l12-2c2 10 6 20 7 31a19145 19145 0 0 0-202" [DATA](/qb64wiki/index.php/DATA "DATA") " 39l-146 29-220 43-24-168-37-255-23-161ZM868 555c2 2 2 5 2 7l-2-7Z' opacity='.4'/></g><g fill='#030173'><path d=" [DATA](/qb64wiki/index.php/DATA "DATA") "'M132 268c16 3 31 7 46 8l5 32-46-8h-1c0-11-2-21-4-32ZM301 300l116 23 5 27-36-3c0-2-2-4-4-4l-77-13c-1-10-4-20-4-3" [DATA](/qb64wiki/index.php/DATA "DATA") "0ZM515 343c24 5 49 11 74 14l4 22-50-8c-8-1-16-4-24-3l-4-25ZM224 378l94 4 7 43c1 15 5 30 8 45h-8l-8-2-80-5c-4-29-" [DATA](/qb64wiki/index.php/DATA "DATA") "10-57-13-85ZM428 387l27 1c3 27 10 54 15 81h-60l-8-43h33l-7-39ZM514 391l10 1 63 9 5 27-72-9-6-28ZM632 396h14l17 7" [DATA](/qb64wiki/index.php/DATA "DATA") "1h-37l-9-40 22 2-7-33ZM527 453c24 1 48 5 72 7 3 10 6 20 7 31l-38-3-4-20h-34l-3-15ZM165 491l43 2 37 243 359-59-22" [DATA](/qb64wiki/index.php/DATA "DATA") "-115c-79 5-157 12-236 18l-11-67 205-7c6 2 12 2 18 2 20 2 41 2 61 3l17 84 54-6 24 104 3 5h-1l-12 2-49 10-446 88-2" [DATA](/qb64wiki/index.php/DATA "DATA") "-13-31-216-11-75v-3Z'/><path d='m491 609 6-1 8 44-143 19-8-47 137-15Z'/></g><path fill='#013f59' d='m113 296 23 " [DATA](/qb64wiki/index.php/DATA "DATA") "4h1l28 191v3c-7-5-15-2-23-3l-29-195Z' opacity='.4'/><path fill='#000314' d='M26 404c23 3 46 9 68 13l37 255H96l28" [DATA](/qb64wiki/index.php/DATA "DATA") " 188 255-42-4-21 146-29 6 26 36-6c1 0 4-1 4-3l-5-25 11-2 11 50-23 5-441 86c-7 2-14 4-22 4L26 404Z' opacity='.1'/" [DATA](/qb64wiki/index.php/DATA "DATA") "><path fill='#f87d03' d='M771 466h60l40 168-59 9-14-65-108 11-54 6-17-84-9-44h74c2-1 2 1 2 2l18 82 84-7-17-78Z'/" [DATA](/qb64wiki/index.php/DATA "DATA") "><path fill='#febd04' d='m470 469 60-1h34l4 20 3 17-31 1-205 7 11 67c79-6 157-13 236-18l22 115-359 59-37-243-3-2" [DATA](/qb64wiki/index.php/DATA "DATA") "2 120-1h8l77-1h60m21 140-137 15 8 47 143-19-8-44-6 1Z'/><g fill='#5d470f'><path d='M152 569h24l31 216-22 4-16-10" [DATA](/qb64wiki/index.php/DATA "DATA") "6c-5-38-10-76-17-114ZM655 710l49-10v4l-35 6c-4 0-9 2-14 0Z' opacity='.4'/></g></svg>" [DATA](/qb64wiki/index.php/DATA "DATA") ""  ``` |
| --- |


  




### More examples


* [Program ScreenShots](/qb64wiki/index.php/Program_ScreenShots "Program ScreenShots")
* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [ThirtyTwoBit SUB](/qb64wiki/index.php/ThirtyTwoBit_SUB "ThirtyTwoBit SUB")


  




## See also


* [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE"), [\_ICON](/qb64wiki/index.php/ICON "ICON")
* [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE"), [\_MAPTRIANGLE](/qb64wiki/index.php/MAPTRIANGLE "MAPTRIANGLE")
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE"), [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")
* [\_PRINTIMAGE](/qb64wiki/index.php/PRINTIMAGE "PRINTIMAGE") (printer)
* [\_PALETTECOLOR (function)](/qb64wiki/index.php/PALETTECOLOR_(function) "PALETTECOLOR (function)"), [\_COPYPALETTE](/qb64wiki/index.php/COPYPALETTE "COPYPALETTE"), [\_ICON](/qb64wiki/index.php/ICON "ICON")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")
* [\_SAVEIMAGE](/qb64wiki/index.php/SAVEIMAGE "SAVEIMAGE")
* [Hardware images](/qb64wiki/index.php/Hardware_images "Hardware images")
* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps"), [Icons and Cursors](/qb64wiki/index.php/Icons_and_Cursors "Icons and Cursors"), [GIF Images](/qb64wiki/index.php/GIF_Images "GIF Images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LOADIMAGE&oldid=8660>"




## Navigation menu








### Search





















