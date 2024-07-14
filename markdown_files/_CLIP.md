


\_CLIP - QB64 Phoenix Edition Wiki








# \_CLIP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CLIP option is used in a QB64 graphics [PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)") to allow placement of an image partially off of the screen.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[PUT](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)") PSET|AND|OR|PRESET}][, *omitcolor*]
  




## Description


* \_CLIP should be placed immediately before the PUT action if used. XOR is default when not used.
* The offscreen portions of the image will be the omit color.
* [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") can get portions of the images off screen in **QB64**.


  




## Examples


*Example:* Placing an image partially or fully offscreen.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") mypic(500) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13  [CLS](/qb64wiki/index.php/CLS "CLS") [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (10, 10), 10 [GET](/qb64wiki/index.php/GET_(general) "GET (general)") (0, 0)-(20, 20), mypic(0)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This program puts an image off screen." [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Select which option you'd like to try." [PRINT](/qb64wiki/index.php/PRINT "PRINT") "1 will produce an illegal function call." [PRINT](/qb64wiki/index.php/PRINT "PRINT") "1 is putting without _CLIP." [PRINT](/qb64wiki/index.php/PRINT "PRINT") "2 is putting with _CLIP PSET." [PRINT](/qb64wiki/index.php/PRINT "PRINT") "3 is putting with _CLIP XOR." [PRINT](/qb64wiki/index.php/PRINT "PRINT") "4 is putting with _CLIP PSET, 4."  [INPUT](/qb64wiki/index.php/INPUT "INPUT") sel [IF](/qb64wiki/index.php/IF "IF") sel = 1 [THEN](/qb64wiki/index.php/THEN "THEN") [PUT](/qb64wiki/index.php/PUT_(general) "PUT (general)") (-10, 10), mypic(0), [PSET](/qb64wiki/index.php/PSET "PSET") ' this causes an illegal function call [IF](/qb64wiki/index.php/IF "IF") sel = 2 [THEN](/qb64wiki/index.php/THEN "THEN") [PUT](/qb64wiki/index.php/PUT_(general) "PUT (general)") (-10, 10), mypic(0), _CLIP [PSET](/qb64wiki/index.php/PSET "PSET") ' allows graphic to be drawn off-screen [IF](/qb64wiki/index.php/IF "IF") sel = 3 [THEN](/qb64wiki/index.php/THEN "THEN") [PUT](/qb64wiki/index.php/PUT_(general) "PUT (general)") (-10, 10), mypic(0), _CLIP ' uses the default PUT XOR operation [IF](/qb64wiki/index.php/IF "IF") sel = 4 [THEN](/qb64wiki/index.php/THEN "THEN") [PUT](/qb64wiki/index.php/PUT_(general) "PUT (general)") (-10, 10), mypic(0), _CLIP [PSET](/qb64wiki/index.php/PSET "PSET"), 4 ' doesn't draw red pixels  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)")
* [STEP](/qb64wiki/index.php/STEP "STEP")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CLIP&oldid=8280>"




## Navigation menu








### Search





















