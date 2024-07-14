


BLOAD - QB64 Phoenix Edition Wiki








# BLOAD



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
BLOAD loads a binary graphics file created by [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE") to an array.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Legacy support](#Legacy_support) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


BLOAD *fileName$*, [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")(*imageArray%(*index*)*)
### Legacy support


* **QB64** can load larger arrays directly from binary files using [PUT](/qb64wiki/index.php/PUT "PUT") # and [GET](/qb64wiki/index.php/GET "GET") # without **BLOAD**. For that reason, **BLOAD** isn't recommended practice anymore and is supported to maintain compatibility with legacy code.


  




## Parameters


* *fileName$* is the name of the file that the image should be [BSAVEd](/qb64wiki/index.php/BSAVE "BSAVE") to.
* *imageArray%(index)* is the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [array](/qb64wiki/index.php/Arrays "Arrays") start index to store the image loaded.


  




## Description


* There must be an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") array of adequate size (up to 26K) to hold the graphic data.
* A [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") pointing to the array is required. [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG")(imageArray%(index))
* *index* is the starting image element of the Array. Can also include RGB color settings at the start index.
* Fullscreen images in [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 require 3 file BLOADs. A 26K array can hold 1/3 of screen.
* Custom RGB color settings can be embedded(indexed) at the start of the image array.
* BLOAD can be used to load any array that was saved with [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE"), not just graphics.
* Array sizes are limited to 32767 Integer elements due to use of [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR") in QBasic and **QB64'**s emulated conventional memory.


  




## Examples


*Example 1:* Loading data to an array from a BSAVED file.





| ```  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG")(Array(0))    BLOAD filename$, [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")(Array([LBOUND](/qb64wiki/index.php/LBOUND "LBOUND")(Array))) ' changeable index  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")  ``` |
| --- |


*Explanation:* Referance any type of array that matches the data saved. Can work with Integer, Single, Double, Long, fixed length Strings or [TYPE](/qb64wiki/index.php/TYPE "TYPE") arrays. [LBOUND](/qb64wiki/index.php/LBOUND "LBOUND") determines the starting offset of the array or another index could be used.
  

*Example 2:* Using a QB default colored image.





| ```  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG")(Image%(0)) ' pointer to first image element of an array    BLOAD FileName$, [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")(Image%(0)) ' place data into array at index position 0    [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")(Col, Row), Image%(0), PSET ' Put the image on the screen from index 0  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")  ``` |
| --- |


*Note:* [PSET](/qb64wiki/index.php/PSET "PSET") is used as a [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)") action that places the image over any background objects.
  




## See also


* [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE"), [OPEN](/qb64wiki/index.php/OPEN "OPEN"), [BINARY](/qb64wiki/index.php/BINARY "BINARY")
* [PUT](/qb64wiki/index.php/PUT "PUT"), [GET](/qb64wiki/index.php/GET "GET") (file statement)
* [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)"), [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG"), [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")
* [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=BLOAD&oldid=7824>"




## Navigation menu








### Search





















