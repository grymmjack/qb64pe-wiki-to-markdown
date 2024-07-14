


\_ICON - QB64 Phoenix Edition Wiki








# \_ICON



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ICON statement uses an image handle from [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") for the program header and icon image in the OS.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) 	+ [3.1 Errors](#Errors) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_ICON [*mainImageHandle&*[, *smallImageHandle&*
  




## Parameters


* *mainImageHandle&* is the [LONG](/qb64wiki/index.php/LONG "LONG") handle value of the OS icon and title bar image pre-loaded with [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") when used alone.
* *smallImageHandle&* is the [LONG](/qb64wiki/index.php/LONG "LONG") handle value of a different title bar image pre-loaded with [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") when used.
* No image handle designates use of the default QB64 icon or the embedded icon set by [$EXEICON](/qb64wiki/index.php/$EXEICON "$EXEICON").


  




## Description


* If no image handle is passed, the default QB64 icon will be used (all versions). If the [$EXEICON](/qb64wiki/index.php/$EXEICON "$EXEICON") metacommand is used, \_ICON without an image handle uses the embedded icon from the binary (Windows only).
* Beginning with **version 1.000**, the following is considered:


*mainImageHandle&* creates the image as the icon in the OS and the image in the program header (title bar).
*smallImageHandle&* can be used for a different image in the program header bar.
* The header image will automatically be resized to fit the icon size of 16 X 16 if smaller or larger.
* Once the program's icon is set, the image handle can be discarded with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE").


### Errors


* **NOTE: Icon files are not supported with [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") and an error will occur. See Example 2.**
* Images used can be smaller or larger than 32 X 32 pixels, but image resolution may be affected.
* It is important to free unused or uneeded images with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") to prevent memory overflow errors.
* In **SCREEN 0** (default text mode) you need to specify 32-bit mode in [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") to load images.


  




## Examples


*Example 1:* Loading an image to a 32 bit palette in SCREEN 0 (the default screen mode).





| ``` i& =[_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("RDSWU16.BMP", 32) '<<<<<<< use your image file name here  [IF](/qb64wiki/index.php/IF "IF") i& < -1 THEN   _ICON i&   [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") i& ' release image handle after setting icon [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


*Note:* \_ICON images can be freed if the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode stays the same. Freed image handles can on longer be referenced.
  

*Example 2:* Function that converts an icon into a temporary bitmap for use in QB64. Function returns the available image count.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 256) [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "Icon Converter" icon$ = "daphne.ico"     '<<<<<<<<< change icon file name bitmap$ = "tempfile.bmp" indx% = 6  '1 minimum <<<<<<< higher values than count get highest entry image in icon file  [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Icon2BMP(icon$, bitmap$, indx%) [THEN](/qb64wiki/index.php/THEN "THEN")   img& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")(bitmap$) '  use 32 as color mode in SCREEN 0   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") img& < -1 [THEN](/qb64wiki/index.php/THEN "THEN") '           check that handle value is good before loading     _ICON img& '                place image in header     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (300, 250), img& 'place image on screen     [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") img& '           always free unused handles to save memory     [KILL](/qb64wiki/index.php/KILL "KILL") bitmap$ '              comment out and/or rename to save the bitmaps   [END IF](/qb64wiki/index.php/END_IF "END IF") [END IF](/qb64wiki/index.php/END_IF "END IF") [END](/qb64wiki/index.php/END "END") '                ----------------------------------------------------  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") Icon2BMP% (filein [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), fileout [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), index [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")) 'function creates a bitmap of the icon and returns the icon count [DIM](/qb64wiki/index.php/DIM "DIM") byte [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE"), word [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), dword [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") [DIM](/qb64wiki/index.php/DIM "DIM") wide [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), high [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), BM [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), bpp [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  rf = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$")([RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(filein, 4)) = ".ico" [THEN](/qb64wiki/index.php/THEN "THEN") 'check file extension is ICO only   [OPEN](/qb64wiki/index.php/OPEN "OPEN") filein [FOR](/qb64wiki/index.php/OPEN "OPEN") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [ACCESS](/qb64wiki/index.php/ACCESS "ACCESS") [READ](/qb64wiki/index.php/ACCESS "ACCESS") [AS](/qb64wiki/index.php/AS "AS") rf [ELSE](/qb64wiki/index.php/ELSE "ELSE") [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION") [END IF](/qb64wiki/index.php/END_IF "END IF") [GET](/qb64wiki/index.php/GET "GET") rf, , word [GET](/qb64wiki/index.php/GET "GET") rf, , word: icon = word [GET](/qb64wiki/index.php/GET "GET") rf, , word: count = word [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") icon <> 1 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") count = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") rf: [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION") '[PRINT](/qb64wiki/index.php/PRINT "PRINT") icon, count [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") index > 0 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") index <= count [THEN](/qb64wiki/index.php/THEN "THEN") entry = 16 * (index - 1) [ELSE](/qb64wiki/index.php/ELSE "ELSE") entry = 16 * (count - 1) [SEEK](/qb64wiki/index.php/SEEK "SEEK") rf, 1 + 6 + entry 'start of indexed Entry header [GET](/qb64wiki/index.php/GET "GET") rf, , byte: wide = byte ' use this unsigned for images over 127 [GET](/qb64wiki/index.php/GET "GET") rf, , byte: high = byte ' use this unsigned because it isn't doubled [GET](/qb64wiki/index.php/GET "GET") rf, , word 'number of 4 BPP colors(256 & 32 = 0) & reserved bytes [GET](/qb64wiki/index.php/GET "GET") rf, , dword '2 hot spots both normally 0 in icons, used for cursors [GET](/qb64wiki/index.php/GET "GET") rf, , dword: size = dword 'this could be used, doesn't seem to matter [GET](/qb64wiki/index.php/GET "GET") rf, , dword: offset = dword 'find where the specific index BMP header is '[PRINT](/qb64wiki/index.php/PRINT "PRINT") wide; "X"; high, size, offset  [SEEK](/qb64wiki/index.php/SEEK "SEEK") rf, 1 + offset + 14 'only read the BPP in BMP header [GET](/qb64wiki/index.php/GET "GET") rf, , word: bpp = word [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") bpp = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") rf: [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") bpp <= 24 [THEN](/qb64wiki/index.php/THEN "THEN") pixelbytes = bpp / 8 [ELSE](/qb64wiki/index.php/ELSE "ELSE") pixelbytes = 3 [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") bpp > 1 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") bpp <= 8 [THEN](/qb64wiki/index.php/THEN "THEN") palettebytes = 4 * (2 ^ bpp) [ELSE](/qb64wiki/index.php/ELSE "ELSE") palettebytes = 0 datasize& = (wide * high * pixelbytes) + palettebytes 'no padder should be necessary filesize& = datasize& + 14 + 40 '                      data and palette + header bmpoffset& = palettebytes + 54 '                       data offset from start of bitmap readbytes& = datasize& + 28 ' (40 - 12) bytes left to read in BMP header and [XOR](/qb64wiki/index.php/XOR "XOR") mask only '[PRINT](/qb64wiki/index.php/PRINT "PRINT") bpp, bmpoffset&, filesize&  BM = [CVI](/qb64wiki/index.php/CVI "CVI")("BM") 'this will create "BM" in file like [MKI$](/qb64wiki/index.php/MKI$ "MKI$") would wf = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") [OPEN](/qb64wiki/index.php/OPEN "OPEN") fileout [FOR](/qb64wiki/index.php/OPEN "OPEN") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") wf [PUT](/qb64wiki/index.php/PUT "PUT") wf, , BM [PUT](/qb64wiki/index.php/PUT "PUT") wf, , filesize& dword = 0 [PUT](/qb64wiki/index.php/PUT "PUT") wf, , dword [PUT](/qb64wiki/index.php/PUT "PUT") wf, , bmpoffset& 'byte location of end of palette or BMP header dword = 40 [PUT](/qb64wiki/index.php/PUT "PUT") wf, , dword '              start of 40 byte BMP header [PUT](/qb64wiki/index.php/PUT "PUT") wf, , wide [PUT](/qb64wiki/index.php/PUT "PUT") wf, , high [SEEK](/qb64wiki/index.php/SEEK "SEEK") rf, 1 + offset + 12 '     after 12 bytes start copy of BMP header starting at planes dat$ = [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(readbytes&, 0) 'create string to hold remaining bytes needed w/o [AND](/qb64wiki/index.php/AND "AND") mask data [GET](/qb64wiki/index.php/GET "GET") rf, , dat$ '               copy lower header, palette(if used) and [XOR](/qb64wiki/index.php/XOR "XOR") mask [PUT](/qb64wiki/index.php/PUT "PUT") wf, , dat$ '               put all of the string data in the bitmap all at once [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") rf, wf Icon2BMP = count '             return the number of icons available in the icon file [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Code by Ted Weissgerber
*Note:* Once the file has been loaded into memory, the image handle can still be used even after the file has been deleted.
  




## See also


* [\_TITLE](/qb64wiki/index.php/TITLE "TITLE")
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")
* [$EXEICON](/qb64wiki/index.php/$EXEICON "$EXEICON")
* [Creating Icon Bitmaps](/qb64wiki/index.php/Creating_Icon_Bitmaps "Creating Icon Bitmaps") (member-contributed program)
* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps"), [Icons and Cursors](/qb64wiki/index.php/Icons_and_Cursors "Icons and Cursors")
* [Icon Extraction](/qb64wiki/index.php/Resource_Table_extraction#Extract_Icon "Resource Table extraction")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ICON&oldid=7882>"




## Navigation menu








### Search





















