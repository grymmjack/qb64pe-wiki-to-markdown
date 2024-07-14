


TYPE - QB64 Phoenix Edition Wiki








# TYPE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**TYPE** definitions are used to create variables that can hold more than one variable type of a fixed byte length.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


**TYPE** typename
.
. variable(s) [AS](/qb64wiki/index.php/AS "AS") type
.
**END TYPE**
  




* Typename is an undefined type name holder as it can hold any variable types.
* TYPE definitions should be placed in the main module before the start of the program code execution.
* TYPE definitions CAN be placed in [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures using QB64 only!
* TYPE definitions cannot contain Array variables! Arrays can be [DIMensioned](/qb64wiki/index.php/DIM "DIM") as a TYPE definition.
* TYPE definitions cannot be inside of another TYPE definition, but variables can be defined AS another type.(See Example 3)
* TYPE definitions must be ended with [END TYPE](/qb64wiki/index.php/END_TYPE "END TYPE").
* A TYPE variable MUST be assigned to the type after it is defined. Array variables are allowed.
* Type variables must be defined in every SUB or FUNCTION unless the type variable is [DIMensioned](/qb64wiki/index.php/DIM "DIM") as [SHARED](/qb64wiki/index.php/SHARED "SHARED").
* Type variables use DOT variable names to read or write specific values. They do not use type suffixes as they can hold ANY variable type values! The name before the dot is the one you defined after the type definition and the name after is the variable name used inside of the TYPE. The name of the dimensioned type variable alone can be used to [PUT](/qb64wiki/index.php/PUT "PUT") # or [GET](/qb64wiki/index.php/GET "GET") # all of the data at once!
* Once the TYPE variable is created you can find the record or byte size by using [LEN](/qb64wiki/index.php/LEN "LEN")(typevariable).
* TYPE definitions can also be placed in [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") .BI text files such as [QB.BI](/qb64wiki/index.php/QB.BI "QB.BI") is used by [INTERRUPT](/qb64wiki/index.php/INTERRUPT "INTERRUPT") and [INTERRUPTX](/qb64wiki/index.php/INTERRUPTX "INTERRUPTX").
* **[\_BIT](/qb64wiki/index.php/BIT "BIT") is not currently supported in User Defined TYPEs**.
* **NOTE: Many QBasic keyword variable names CAN be used with a [STRING](/qb64wiki/index.php/STRING "STRING") suffix($) ONLY! You CANNOT use them without the suffix, use a numerical suffix or use [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM"), [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") or TYPE variable [AS](/qb64wiki/index.php/AS "AS") statements!**




| ```          Table 1: The variable types supported by the QB64 language. ┌───────────────────────────────────────────────────────────────────────────┐ │                              **Numerical types**                              │ ├──────────────────────┬───────────┬────────────────────────────┬───────────┤ │      **Type Name**       │   **Type**    │       **Minimum value**        │  **Size in**  │ │                      │  **suffix**   │       **Maximum value**        │   **Bytes**   │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │         [_BIT](/qb64wiki/index.php/BIT "BIT")         │     `     │                         -1 │    1/8    │ │                      │           │                          0 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │       [_BIT * n](/qb64wiki/index.php/BIT "BIT")       │    `n     │                       -128 │    n/8    │ │                      │           │                        127 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │    [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BIT](/qb64wiki/index.php/BIT "BIT")    │    ~`     │                          0 │    1/8    │ │                      │           │                          1 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │        [_BYTE](/qb64wiki/index.php/BYTE "BYTE")         │    %%     │                       -128 │     1     │ │                      │           │                        127 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │   [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")    │    ~%%    │                          0 │     1     │ │                      │           │                        255 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │       [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")        │     %     │                    -32,768 │     2     │ │                      │           │                     32,767 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │  [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")   │    ~%     │                          0 │     2     │ │                      │           │                     65,535 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │         [LONG](/qb64wiki/index.php/LONG "LONG")         │     &     │             -2,147,483,648 │     4     │ │                      │           │              2,147,483,647 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │    [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")    │    ~&     │                          0 │     4     │ │                      │           │              4,294,967,295 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │      [_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")      │    &&     │ -9,223,372,036,854,775,808 │     8     │ │                      │           │  9,223,372,036,854,775,807 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") │    ~&&    │                          0 │     8     │ │                      │           │ 18,446,744,073,709,551,615 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │        [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")        │     !     │              -2.802597E-45 │     4     │ │                      │ (or none) │              +3.402823E+38 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │        [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")        │     #     │    -4.490656458412465E-324 │     8     │ │                      │           │    +1.797693134862310E+308 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │        [_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT")        │    ##     │                -1.18E-4932 │    32     │ │                      │           │                +1.18E+4932 │ (10 used) │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │       [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")        │    %&     │ -9,223,372,036,854,775,808 │  use [LEN](/qb64wiki/index.php/LEN "LEN")  │ │                      │           │  9,223,372,036,854,775,807 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │  [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")   │    ~%&    │                          0 │  use [LEN](/qb64wiki/index.php/LEN "LEN")  │ │                      │           │ 18,446,744,073,709,551,615 │           │ ├──────────────────────┼───────────┼────────────────────────────┴───────────┤ │         [_MEM](/qb64wiki/index.php/MEM "MEM")         │   none    │ **An internal TYPE like memory variable.** │ └──────────────────────┴───────────┴────────────────────────────────────────┘   For the floating-point numeric types [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") (default when not assigned),  [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") and [_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT"), the minimum values represent the smallest values closest   to zero, while the maximum values represent the largest values closest to     pos./neg. infinity. [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") dot values are used as a part of the [_MEM](/qb64wiki/index.php/MEM "MEM")        variable type in QB64 to return or set the position in memory.  ┌───────────────────────────────────────────────────────────────────────────┐ │                                **Text types**                                 │ ├──────────────────────┬───────────┬────────────────────────────┬───────────┤ │      **Type Name**       │   **Type**    │       **Minimum value**        │  **Size in**  │ │                      │  **suffix**   │       **Maximum value**        │   **Bytes**   │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │        [STRING](/qb64wiki/index.php/STRING "STRING")        │     $     │                          0 │  use [LEN](/qb64wiki/index.php/LEN "LEN")  │ │                      │           │              2,147,483,647 │           │ ├──────────────────────┼───────────┼────────────────────────────┼───────────┤ │      [STRING * n](/qb64wiki/index.php/STRING "STRING")      │    $n     │                          1 │     n     │ │                      │           │              2,147,483,647 │           │ └──────────────────────┴───────────┴────────────────────────────┴───────────┘   While a regular variable length [STRING](/qb64wiki/index.php/STRING "STRING") may have a minimum length of **zero**    (empty string), the fixed length string type [STRING * n](/qb64wiki/index.php/STRING "STRING"), where **n** is an  integer length value, must have a minimum length of at least **one** character.  ``` |
| --- |


  

*Example 1:* Creating a mouse [INTERRUPT](/qb64wiki/index.php/INTERRUPT "INTERRUPT") TYPE definition. Each [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value is 2 bytes.





| ```  TYPE RegType    AX [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    ' mouse function to use    BX [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    ' mouse button    CX [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    ' mouse graphic column position    DX [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    ' mouse graphic row position    BP [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    ' not used by mouse, but required *    SI [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    ' not used by mouse, but required *    DI [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    ' not used by mouse, but required *    Flags [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") ' not used by mouse but required *    DS [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    ' used by [INTERRUPTX](/qb64wiki/index.php/INTERRUPTX "INTERRUPTX") only    ES [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")    ' used by [INTERRUPTX](/qb64wiki/index.php/INTERRUPTX "INTERRUPTX") only  END TYPE   [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") InRegs [AS](/qb64wiki/index.php/AS "AS") RegType, OutRegs [AS](/qb64wiki/index.php/AS "AS") RegType ' create dot variables   InRegs.AX = 3 ' sets the mouse function to read the mouse buttons and position.   [CALL](/qb64wiki/index.php/CALL "CALL") [INTERRUPT](/qb64wiki/index.php/INTERRUPT "INTERRUPT")(&H33, InRegs, OutRegs)   column% = OutRegs.CX ' returns the current mouse column position  ``` |
| --- |


*Explanation:* InRegs and OutRegs become the DOT variable prefix name for the TYPE definition's variables.
Each TYPE variable is designated as the DOT variable's suffix.
**\* Note: Omitting variables in the RegType definition can change other program variable values!**


  



*Example 2:* Creating an addressbook database for a [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") file.





| ```  TYPE ContactInfo    First AS STRING * 10    Last AS STRING * 15    Address1 AS STRING * 30    Address2 AS STRING * 30    City AS STRING * 15    State AS STRING * 2    Zip AS LONG   ' (4 bytes)    Phone AS STRING * 12  END TYPE   DIM Contact AS ContactInfo 'create contact record variable for [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") file  RecordLEN% = [LEN](/qb64wiki/index.php/LEN "LEN")(Contact) ' 118 bytes   'define values  Contact.First = "Ted" ' the fixed string length value will contain 7 extra spaces  Contact.Zip = 15236 ' [LONG](/qb64wiki/index.php/LONG "LONG") value that can be used to search certain zip code numbers.   [PUT #](/qb64wiki/index.php/PUT "PUT")1, 5,Contact  'place contact info into fifth record position  ``` |
| --- |


*Explanation:* Use the assigned type variable to find the RANDOM record length which is 118 bytes.
The DOT variable names consist of Contact as the prefix:
  

*Example 3:* Defining a TYPE variable as another variable type from a previous TYPE definition in QB64.





| ``` TYPE bar   b [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 10 END TYPE  TYPE foo   a [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")   c [AS](/qb64wiki/index.php/AS "AS") bar          'define variable as a bar type END TYPE  [DIM](/qb64wiki/index.php/DIM "DIM") foobar [AS](/qb64wiki/index.php/AS "AS") foo   'create a variable to use the foo type foobar.a = 15.5 foobar.c.b = "this is me"  PRINT foobar.a, foobar.c.b [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  

*Example 4:* A bitmap header information TYPE [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") File.





| ``` ' ******** 'Bitmap.BI can be included at start of program   TYPE BMPHeaderType        ' Description                  Bytes      **QB64**    ID AS STRING * 2        ' File ID is "BM"                2    Size AS LONG            ' Size of the data file          4    Res1 AS INTEGER         ' Reserved 1 should be 0         2    Res2 AS INTEGER         ' Reserved 2 should be 0         2    Offset AS LONG          ' Start position of pixel data   4    Hsize AS LONG           ' Information header size        4    PWidth AS LONG          ' Image width                    4       [_WIDTH (function)](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")    PDepth AS LONG          ' Image height                   4       [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")    Planes AS INTEGER       ' Number of planes               2    BPP AS INTEGER          ' Bits per pixel(palette)        2       [_PIXELSIZE](/qb64wiki/index.php/PIXELSIZE "PIXELSIZE")    Compress AS LONG        ' Compression                    4    ImageBytes AS LONG      ' Width * Height = ImageSIZE     4    Xres AS LONG            ' Width in PELS per metre        4    Yres AS LONG            ' Depth in PELS per metre        4    NumColors AS LONG       ' Number of Colors               4    SigColors AS LONG       ' Significant Colors             4  END TYPE                  '          Total Header bytes = 54  ``` |
| --- |




| ``` '[$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE"): 'Bitmap.BI'  'use only when including a BI file  [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") BMPHead AS BMPHeaderType  [GET #](/qb64wiki/index.php/GET "GET")1, , BMPHead  'get the entire bitmap header information  ``` |
| --- |


*Explanation:* Use one [GET](/qb64wiki/index.php/GET "GET") to read all of the header information from the start of the bitmap file opened AS [BINARY](/qb64wiki/index.php/BINARY "BINARY"). It reads all 54 bytes as [STRING](/qb64wiki/index.php/STRING "STRING"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") and [LONG](/qb64wiki/index.php/LONG "LONG") type DOT variable values.
NOTE: BPP returns 4(16 colors), 8(256 colors) or 24(16 million colors) bits per pixel in QBasic. 24 bit can only be in greyscale.
Then use the DOT variable name values like this [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") after you load the bitmap image to the screen:


| ``` [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") (0, 0)-(BMPHead.PWidth - 1, BMPHead.PDepth - 1), Image(48) 'indexed for 4 BPP colors  ``` |
| --- |


The bitmap image is now stored in an [array](/qb64wiki/index.php/Arrays "Arrays") to [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE") to a file. The RGB color information follows the file header as [ASCII](/qb64wiki/index.php/ASCII "ASCII") character values read using [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)"). The color values could be indexed at the start of the Array with the image being offset to: index = NumberOfColors \* 3. As determined by the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode used. In SCREEN 13(256 colors) the index would be 768.
  




## See also


* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")
* [LONG](/qb64wiki/index.php/LONG "LONG"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64"), [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT")
* [STRING](/qb64wiki/index.php/STRING "STRING"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [\_BIT](/qb64wiki/index.php/BIT "BIT"), [\_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")
* [GET #](/qb64wiki/index.php/GET "GET"), [PUT #](/qb64wiki/index.php/PUT "PUT"), [BINARY](/qb64wiki/index.php/BINARY "BINARY")
* [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)"), [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [LEN](/qb64wiki/index.php/LEN "LEN"), [LOF](/qb64wiki/index.php/LOF "LOF"), [EOF](/qb64wiki/index.php/EOF "EOF")
* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps"), [Icon to Bitmap Conversion Function](/qb64wiki/index.php/Creating_Icon_Bitmaps#Icon_to_Bitmap_Conversion_Function "Creating Icon Bitmaps")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=TYPE&oldid=8738>"




## Navigation menu








### Search





















