


\_MEM - QB64 Phoenix Edition Wiki








# \_MEM



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEM variable type can be used when working with memory blocks. It has no variable [type](/qb64wiki/index.php/Variable_Types "Variable Types") suffix.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 Usage](#Usage) * [3 .TYPE values (version 1.000 and up incl. all QB64-PE releases)](#.TYPE_values_(version_1.000_and_up_incl._all_QB64-PE_releases)) 	+ [3.1 Versions prior to 1.000 (never use with QB64-PE releases)](#Versions_prior_to_1.000_(never_use_with_QB64-PE_releases)) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


[DIM](/qb64wiki/index.php/DIM "DIM") m [AS](/qb64wiki/index.php/AS "AS") \_MEM
  




## Description


*Variable TYPE:*



* Memory DOT values are actually part of the built in memory variable [type](/qb64wiki/index.php/Variable_Types "Variable Types") in QB64. The following [TYPE](/qb64wiki/index.php/TYPE "TYPE") is built in:




| ``` TYPE memory_type   OFFSET AS _OFFSET       'start location of block(changes with byte position)   SIZE AS _OFFSET         'size of block remaining at offset(changes with position)   TYPE AS _OFFSET         'type description of variable used(never changes)   ELEMENTSIZE AS _OFFSET  'byte size of values inside the block(never changes)   IMAGE AS LONG           'the image handle used when _MEMIMAGE(handle) is used   SOUND AS LONG           'the sound handle used when _MEMSOUND(handle) is used END TYPE  The above [TYPE](/qb64wiki/index.php/TYPE "TYPE") is for clarification purposes only. It **doesn't need** to be pasted ina program to use _MEM.  **IMPORTANT NOTE:** *As of Build 20170802/57 onward (early v1.2 development), mem.TYPE hasbeen changed to be an _OFFSET, just as mem.SIZE and mem.ELEMENTSIZE.*  ``` |
| --- |


### Usage


* The \_MEM type contains the following **read-only** elements where *name* is the \_MEM variable name:


*name***.OFFSET** is the current start position in the memory block AS [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET"). Add bytes to change position.
*name***.SIZE** is the remaining size of the block at current position in bytes AS [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")
*name***.TYPE** is the type (represented as bits combined to form a value) AS [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET"):
  




## .TYPE values (version 1.000 and up incl. all QB64-PE releases)


* [bit 0] 1\* byte types (\_BYTE)
* [bit 1] 2\* byte types (INTEGER)
* [bit 2] 4\* byte types (LONG or SINGLE)
* [bit 3] 8\* byte types (DOUBLE or \_INTEGER64)
* [bit 4] 16\* byte types (reserved for future use)
* [bit 5] 32\* byte types (\_FLOAT)
* [bit 6] 64\* byte types (reserved for future use)
* [bit 7] 128 = integer types (\_BYTE, INTEGER, LONG, \_INTEGER64) (added to \*)
* [bit 8] 256 = floating point types (SINGLE, DOUBLE, \_FLOAT) (added to \*)
* [bit 9] 512 = STRING types (fixed length or variable length)
* [bit 10] 1024 = \_UNSIGNED types (added to \*+128)
* [bit 11] 2048 = pixel data usually from \_MEMIMAGE (added to 1+128+1024 for 256 color screens, or 2+128+1024 for text screens, or 4+128+1024 for 32-bit color screens)
* [bit 12] 4096 = \_MEM TYPE structure (NOT added to 32768)
* [bit 13] 8192 = \_OFFSET type (added to 4+128+[1024] or 8+128+[1024] or future\_size+128+[1024])
* [bit 14] 16384 = data created/defined by \_MEMNEW(size) or \_MEMNEW(offset,size)
* [bit 15] 32768 = a custom, user defined type (ie. created with TYPE name ... END TYPE)
* [bit 16] 65536 = an array of data (added to other type values defining the array's data type)

*Note: If a future integer, float or other type doesn't have a size that is 1,2,4,8,16,32,64,128 or 256 it won't have a size-bit set.*



### Versions prior to 1.000 (never use with QB64-PE releases)


* 1 = Integer types such as [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") or [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")
* 2 = [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") variable types. Value must be added to the variable type value.(2 cannot be used by itself)
* 3 = ALL [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") type values.(add 1 + 2)
* 4 = Floating point types such as [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") or [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT")
* 8 = [STRING](/qb64wiki/index.php/STRING "STRING")
* 0 = unknown(eg. created with [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")) or [user-defined-types](/qb64wiki/index.php/TYPE "TYPE")

* **Note: [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") values cannot be cast to other variable [types](/qb64wiki/index.php/Variable_Types "Variable Types") reliably. \_MEM is a reserved custom variable [type](/qb64wiki/index.php/Variable_Types "Variable Types").**
* **[\_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)") cannot reference variable length [STRING](/qb64wiki/index.php/STRING "STRING") variable values. String values must be designated as a fixed-[length](/qb64wiki/index.php/LEN "LEN") string.**


  




## Examples


*Example 1:* Demonstration of .IMAGE to determine an image's dimensions, .TYPE to verify the type and [\_MEMEXISTS](/qb64wiki/index.php/MEMEXISTS "MEMEXISTS") to check image has not been freed





| ``` 'The $UNSTABLE command may not be necessary if HTTP integration has been fully accepted into QB64PE. 'Feel free to remark it out if the IDE flags the following line with an ERROR message. 'And kindly report the issue on our forums or Discord so that we can update this page to keep it as 100% relevant, as possible.  [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE"):HTTP  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(500, 500, 32)  Image$ = Download$("https://qb64phoenix.com/qb64wiki/resources/assets/peWikiLogo.png", statusCode&) 'Let's try and download the QB64PE Logo from the web [IF](/qb64wiki/index.php/IF "IF") statusCode& = 200 [THEN](/qb64wiki/index.php/THEN "THEN") '                                      200 says a proper connection was made to the web page in question     i = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")(Image$, 32, "memory") '                       and then we load it for use as a registered imange [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "HTTP ERROR"; statusCode '                             can't get a proper connection to our webpage, so we don't have an image to work with.     [END](/qb64wiki/index.php/END "END") '                                                        end and go report the issue on the forums, if you'd be so kind, dear user. [END IF](/qb64wiki/index.php/END_IF "END IF")  [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 0)-(500, 500), i '                                 put the image on the screen so we can view it [DIM](/qb64wiki/index.php/DIM "DIM") m [AS](/qb64wiki/index.php/AS "AS") _MEM: m = [_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE")(i) '                                make a memblock and point it towards our image   '                                                           **** try uncommenting the following line and see what happens **** '_MEMFREE m   [IF](/qb64wiki/index.php/IF "IF") m.TYPE [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") 2048 [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "this is/was an image"     [IF](/qb64wiki/index.php/IF "IF") [_MEMEXISTS](/qb64wiki/index.php/MEMEXISTS "MEMEXISTS")(m) [THEN](/qb64wiki/index.php/THEN "THEN") '                                      check if memory m is still available         [PRINT](/qb64wiki/index.php/PRINT "PRINT") t [AND](/qb64wiki/index.php/AND "AND") 7; "bytes per pixel"         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "image handle "; m.IMAGE         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "image width"; [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(m.IMAGE)         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "image height"; [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(m.IMAGE)     [ELSE](/qb64wiki/index.php/ELSE "ELSE") '                                                       if we removed the remark from the _MEMFREE above, we'll see the following message         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Memory already freed!"     [END IF](/qb64wiki/index.php/END_IF "END IF") [END IF](/qb64wiki/index.php/END_IF "END IF")   ' Content of the HTTP response is returned. ' The statusCode is also assigned. [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") Download$ (url [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), statusCode [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [DIM](/qb64wiki/index.php/DIM "DIM") h [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), content [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), s [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING")     h = [_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")("HTTP:" + url)      statusCode = [_STATUSCODE](/qb64wiki/index.php/STATUSCODE "STATUSCODE")(h)      [WHILE](/qb64wiki/index.php/WHILE "WHILE") [NOT](/qb64wiki/index.php/NOT "NOT") [EOF](/qb64wiki/index.php/EOF "EOF")(h)         [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60         [GET](/qb64wiki/index.php/GET "GET") #h, , s         content = content + s     [WEND](/qb64wiki/index.php/WEND "WEND")     [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #h      Download$ = content [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


  



*Example 2:* Converts the current [destination](/qb64wiki/index.php/DEST "DEST") [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 image memory altered by [PSET](/qb64wiki/index.php/PSET "PSET") to a [STRING](/qb64wiki/index.php/STRING "STRING") value. SCREEN 13 only.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 [PSET](/qb64wiki/index.php/PSET "PSET") (0, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("H") 'put the ASCII value of "H" into the top left corner of screen, which is the first byte of screen image memory [PSET](/qb64wiki/index.php/PSET "PSET") (1, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("E") 'put the ASCII value of "E" into the 2nd byte of screen image memory [PSET](/qb64wiki/index.php/PSET "PSET") (2, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("L") 'put the ASCII value of "L" into the 3nd byte of screen image memory [PSET](/qb64wiki/index.php/PSET "PSET") (3, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("L") 'put the ASCII value of "L" into the 4th byte of screen image memory [PSET](/qb64wiki/index.php/PSET "PSET") (4, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("O") 'put the ASCII value of "O" into the 5th byte of screen image memory                                                                                                                                                                                                            'put the ASCII value of "E" into the 2nd byte of screen image memory  [DIM](/qb64wiki/index.php/DIM "DIM") m [AS](/qb64wiki/index.php/AS "AS") _MEM '                         define m as a mem block m = [_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE")(0) '                      point m to where our screen exists in memory  x1$ = [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(m, m.OFFSET, [STRING](/qb64wiki/index.php/STRING "STRING") * 5) 'm is the mem block that we're wanting to get information from '                                       m.OFFSET is the mem block m starting position '                                       STRING * 5 is the size and type of information that we want to get from that position in memory.  [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 1 [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LEN](/qb64wiki/index.php/LEN "LEN")(x1$) '                        prints 5 bytes as we deliberately fetched STRING * 5 bytes with our _MEMGET above. [PRINT](/qb64wiki/index.php/PRINT "PRINT") x1$ '                             prints the contents of that 5-byte string which we got above -- which is "HELLO" as CHR$() string character values [_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") m  ``` |
| --- |




| ```  5 HELLO   ``` |
| --- |


  

*Example 3:* Using \_MEM to convert \_OFFSET to \_INTEGER64.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") x [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") m [AS](/qb64wiki/index.php/AS "AS") _MEM m = [_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)")(x) [PRINT](/qb64wiki/index.php/PRINT "PRINT") m.OFFSET [PRINT](/qb64wiki/index.php/PRINT "PRINT") ConvertOffset(m.OFFSET)   [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") ConvertOffset&& (value [AS](/qb64wiki/index.php/AS "AS") [_OFFSET](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)"))     [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING"):[OFF](/qb64wiki/index.php/OFF "OFF")     [DIM](/qb64wiki/index.php/DIM "DIM") m [AS](/qb64wiki/index.php/AS "AS") _MEM 'Define a memblock     m = [_MEM](/qb64wiki/index.php/MEM_(function) "MEM (function)")(value) 'Point it to use value     [$IF](/qb64wiki/index.php/$IF "$IF") 64BIT [THEN](/qb64wiki/index.php/THEN "THEN")         [DIM](/qb64wiki/index.php/DIM "DIM") temp [AS](/qb64wiki/index.php/AS "AS") [_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") 'On 64 bit OSes, an OFFSET is 8 bytes in size.     [$ELSE](/qb64wiki/index.php/$ELSE "$ELSE")         [DIM](/qb64wiki/index.php/DIM "DIM") temp [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") '      However, on 32 bit OSes, an OFFSET is only 4 bytes.     [$END IF](/qb64wiki/index.php/$END_IF "$END IF")      [_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET") m, m.OFFSET, temp 'Once we've sized our variable correctly, let's get it     ConvertOffset&& = temp '   And then assign that long value to ConvertOffset&&     [_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") m '               Free the memblock     [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING"):[ON](/qb64wiki/index.php/ON "ON") [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


  

*Explanation:* The above will print two numbers which should match. These numbers will vary, as they're representations of where X is stored in memory, and that position is going to vary every time the program is run. What it should illustrate, however, is a way to convert \_OFFSET to \_INTEGER64 values, which can sometimes be useful when trying to run calculations involving mem.SIZE, mem.TYPE, or mem.ELEMENTSIZE.


  




## See also


* [\_MEM (function)](/qb64wiki/index.php/MEM_(function) "MEM (function)"), [\_MEMELEMENT](/qb64wiki/index.php/MEMELEMENT "MEMELEMENT")
* [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW"), [\_MEMCOPY](/qb64wiki/index.php/MEMCOPY "MEMCOPY"), [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE")
* [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT"), [\_MEMFILL](/qb64wiki/index.php/MEMFILL "MEMFILL")
* [\_MEMIMAGE](/qb64wiki/index.php/MEMIMAGE "MEMIMAGE"), [\_MEMSOUND](/qb64wiki/index.php/MEMSOUND "MEMSOUND")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEM&oldid=8528>"




## Navigation menu








### Search





















