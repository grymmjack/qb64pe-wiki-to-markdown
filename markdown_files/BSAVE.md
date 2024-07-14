


BSAVE - QB64 Phoenix Edition Wiki








# BSAVE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
BSAVE saves the contents of an image array to a [BINARY](/qb64wiki/index.php/BINARY "BINARY") file.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Legacy support](#Legacy_support) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


BSAVE *saveFile$*, [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")(*array(index)*), *fileSize&*
### Legacy support


* **QB64** can save larger arrays directly to binary files using [PUT](/qb64wiki/index.php/PUT "PUT") # and [GET](/qb64wiki/index.php/GET "GET") # without **BSAVE**. For that reason, **BSAVE** isn't recommended practice anymore and is supported to maintain compatibility with legacy code.


  




## Parameters


* *saveFile$* is the STRING file name of the file designated to be created.
* *array(index)* is the image [array](/qb64wiki/index.php/Arrays "Arrays") that already holds the [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") image data.
* *fileSize&* must be a bit over twice the size of the elements used in an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [array](/qb64wiki/index.php/Arrays "Arrays").


  




## Description


* To place image data into the array, use [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") to store a box area image of the screen.
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 can only GET 1/3 of the screen image at one time using a 26K array.
* Image arrays are [DIMensioned](/qb64wiki/index.php/DIM "DIM") as [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"). Use [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT") when working with large graphic arrays.
* Any arrays can be saved, but image arrays are most common.
* [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG") must be used to designate the array segment position in memory.
* [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR") returns the array index offset of the memory segment. Array sizes are limited to 32767 Integer elements due to the use of [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR") in QBasic and **QB64'**s emulated conventional memory.
* BSAVE files can later be opened with [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD").


  




## Examples


*Example 1:* Saving array data to a file quickly.





| ```  LB% = [LBOUND](/qb64wiki/index.php/LBOUND "LBOUND")(Array)  bytes% = [LEN](/qb64wiki/index.php/LEN "LEN")(Array(LB%))  filesize& = (([UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")(Array) - LB%) + 1) * bytes%  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG")(Array(0))   BSAVE filename$, [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")(Array(LB%)), filesize&  ' changeable index  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")  ``` |
| --- |


*Explanation:* Procedure determines the filesize from the array size automatically. [LBOUND](/qb64wiki/index.php/LBOUND "LBOUND") is used with [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND") to determine array size and byte size. Works with any type of array except variable-length strings. Used for saving program data fast.
  

*Example 2:* BSAVEing a bitmap and calculating the file size





| ```  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG")(Image(0))  [PSET](/qb64wiki/index.php/PSET "PSET")(BMPHead.PWidth - 1, BMPHead.PDepth - 1)  'color lower right corner if black  [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") (0, 0)-(BMPHead.PWidth - 1, BMPHead.PDepth - 1), Image(NColors * 3) ' for 16 or 256 colors  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") a& = 26000 [TO](/qb64wiki/index.php/TO "TO") 0 [STEP](/qb64wiki/index.php/STEP "STEP") -1    [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Image(a&) [THEN](/qb64wiki/index.php/THEN "THEN") ArraySize& = a&: [EXIT FOR](/qb64wiki/index.php/EXIT_FOR "EXIT FOR")  [NEXT](/qb64wiki/index.php/NEXT "NEXT")  BSAVE SaveName$, [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")(Image(0)), (2 * ArraySize&) + 200 'file size  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")  ``` |
| --- |


*Explanation:* The [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") loop reads backwards through the image array until it finds a value not 0. The [LONG](/qb64wiki/index.php/LONG "LONG") *ArraySize&* value is doubled and 200 is added. *BMPhead.PWidth* and *BMPhead.PDepth* are found by reading the bitmap's information header using a [TYPE](/qb64wiki/index.php/TYPE "TYPE") definition. See [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps").
  

*Example 3:* Using [PUT](/qb64wiki/index.php/PUT "PUT") and [GET](/qb64wiki/index.php/GET "GET") to write and read array data from a file without using BSAVE or [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD"):





| ``` [KILL](/qb64wiki/index.php/KILL "KILL") "example2.BIN" 'removes old image file!  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 [OPTION BASE](/qb64wiki/index.php/OPTION_BASE "OPTION BASE") 0 [REDIM](/qb64wiki/index.php/REDIM "REDIM") Graphic%(1001) 'REDIM makes array resize-able later  [LINE](/qb64wiki/index.php/LINE "LINE") (0, 0)-(10, 10), 12, B 'create image [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)")(0, 0)-[STEP](/qb64wiki/index.php/STEP "STEP")(10, 10), Graphic%() 'get image to array  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i% = 1000 [TO](/qb64wiki/index.php/TO "TO") 0 [STEP](/qb64wiki/index.php/STEP "STEP") -1 'reverse read array for size needed     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Graphic%(i%) <> 0 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT](/qb64wiki/index.php/EXIT "EXIT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") 'find image color not black [NEXT](/qb64wiki/index.php/NEXT "NEXT") size% = i% + 4 'size plus 2 integers(4  bytes) for dimensions [REDIM](/qb64wiki/index.php/REDIM "REDIM") [_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE") Graphic%(size%) 'resize existing array in QB64 only!  [OPEN](/qb64wiki/index.php/OPEN "OPEN") "example2.BIN" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") #1 ' [PUT](/qb64wiki/index.php/PUT "PUT") to a file [PUT](/qb64wiki/index.php/PUT "PUT") #1, , Graphic%() [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE")  [OPEN](/qb64wiki/index.php/OPEN "OPEN") "example2.BIN" [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") [BINARY](/qb64wiki/index.php/BINARY "BINARY") [AS](/qb64wiki/index.php/AS "AS") #2 'GET array and [PUT](/qb64wiki/index.php/PUT "PUT") to screen [DIM](/qb64wiki/index.php/DIM "DIM") CopyBin%([LOF](/qb64wiki/index.php/LOF "LOF")(2) \ 2) 'create new array sized by half of file size [GET](/qb64wiki/index.php/GET "GET") #2, , CopyBin%() [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")(100, 100), CopyBin%(), [PSET](/qb64wiki/index.php/PSET "PSET") fsize% = [LOF](/qb64wiki/index.php/LOF "LOF")(2) [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE")  K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) 'Press any key [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 20 'read all 3 arrays     [PRINT](/qb64wiki/index.php/PRINT "PRINT") Graphic%(i); CopyBin%(i) [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Array:"; size%, "File:"; fsize%  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* A 10 by 10 pixel box is saved to an array using the [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") and written to a BINARY file using [PUT](/qb64wiki/index.php/PUT "PUT") #1. Then [GET](/qb64wiki/index.php/GET "GET") #1 places the file contents into another INTEGER array and places it on the screen with the [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)").
The array contents: 88 is the width in the GET array for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 which needs divided by 8 in that mode only. The area is actually 11 X 11. The array size needed can be found by looping backwards through the array until a color value is found. **IF array(i) <> 0 THEN EXIT FOR** (66 integers) or by dividing the created BINARY file size in half (134 bytes) when known to be array sized already.
  




## See also


* [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)"), [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [BLOAD](/qb64wiki/index.php/BLOAD "BLOAD"), [OPEN](/qb64wiki/index.php/OPEN "OPEN"), [BINARY](/qb64wiki/index.php/BINARY "BINARY")
* [GET](/qb64wiki/index.php/GET "GET"), [PUT](/qb64wiki/index.php/PUT "PUT") (file statements)
* [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG"), [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")
* [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG"), [TYPE](/qb64wiki/index.php/TYPE "TYPE")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=BSAVE&oldid=7825>"




## Navigation menu








### Search





















