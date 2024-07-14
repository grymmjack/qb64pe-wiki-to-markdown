


\_MAPUNICODE - QB64 Phoenix Edition Wiki








# \_MAPUNICODE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MAPUNICODE statement maps a [Unicode](/qb64wiki/index.php/Unicode "Unicode") value to an [ASCII](/qb64wiki/index.php/ASCII "ASCII") character code value.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


\_MAPUNICODE *unicode&* **TO** *asciiCode%*
  




* The [LONG](/qb64wiki/index.php/LONG "LONG") *unicode&* value is a [hexadecimal](/qb64wiki/index.php/HEX$ "HEX$") or decimal code value from a [Unicode](/qb64wiki/index.php/Unicode "Unicode") [Code Page](/qb64wiki/index.php/Code_Pages "Code Pages").
* The *asciiCode%* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") parameter is any [ASCII](/qb64wiki/index.php/ASCII "ASCII") or Extended code value from 0 to 255.
* Use the Unicode Page Table values listed here: [DOS Code Pages](https://en.wikipedia.org/wiki/Category:DOS_code_pages "wikipedia:Category:DOS code pages") or [Windows Mapping](http://unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/)
* Once the codes are mapped, key entries will display the unicode character in the **monospace**  [font](/qb64wiki/index.php/FONT "FONT") selected.
* The [\_MAPUNICODE](/qb64wiki/index.php/MAPUNICODE_(function) "MAPUNICODE (function)") function can be used to verify or read the present [Unicode](/qb64wiki/index.php/Unicode "Unicode") UTF32 code point settings.
* **\_MAPUNICODE can place the Unicode characters TO any [ASCII](/qb64wiki/index.php/ASCII "ASCII") code space you desire (0 to 255)**.


  




## Examples


*Example:* Converting the extended [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters to other characters using DATA from the Unicode [Code Pages](/qb64wiki/index.php/Code_Pages "Code Pages").





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 [_FONT](/qb64wiki/index.php/FONT "FONT") [_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT")("C:\windows\fonts\cour.ttf", 20, "MONOSPACE")  [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") Microsoft_pc_cpMIK [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") ASCIIcode = 128 [TO](/qb64wiki/index.php/TO "TO") 255   [READ](/qb64wiki/index.php/READ "READ") unicode   _MAPUNICODE Unicode [TO](/qb64wiki/index.php/TO "TO") ASCIIcode [NEXT](/qb64wiki/index.php/NEXT "NEXT")   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 128 [TO](/qb64wiki/index.php/TO "TO") 255   [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(i) + " ";   cnt = cnt + 1   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") cnt [MOD](/qb64wiki/index.php/MOD "MOD") 16 = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")  Microsoft_pc_cpMIK: [DATA](/qb64wiki/index.php/DATA "DATA") 1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055 [DATA](/qb64wiki/index.php/DATA "DATA") 1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071 [DATA](/qb64wiki/index.php/DATA "DATA") 1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087 [DATA](/qb64wiki/index.php/DATA "DATA") 1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103 [DATA](/qb64wiki/index.php/DATA "DATA") 9492,9524,9516,9500,9472,9532,9571,9553,9562,9566,9577,9574,9568,9552,9580,9488 [DATA](/qb64wiki/index.php/DATA "DATA") 9617,9618,9619,9474,9508,8470,167,9559,9565,9496,9484,9608,9604,9612,9616,9600 [DATA](/qb64wiki/index.php/DATA "DATA") 945,223,915,960,931,963,181,964,934,920,937,948,8734,966,949,8745 [DATA](/qb64wiki/index.php/DATA "DATA") 8801,177,8805,8804,8992,8993,247,8776,176,8729,183,8730,8319,178,9632,160  ``` |
| --- |


*Note:* The Unicode data field is created by adding DATA before each line listed for the appropriate [Code Page](/qb64wiki/index.php/Code_Pages "Code Pages").
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1169)
* [\_MAPUNICODE (function)](/qb64wiki/index.php/MAPUNICODE_(function) "MAPUNICODE (function)")
* [ASCII](/qb64wiki/index.php/ASCII "ASCII"), [Unicode](/qb64wiki/index.php/Unicode "Unicode"), [\_FONT](/qb64wiki/index.php/FONT "FONT")
* [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT"), [\_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN")
* [ASC](/qb64wiki/index.php/ASC "ASC"), [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"), [CHR$](/qb64wiki/index.php/CHR$ "CHR$")
* [Code Pages](/qb64wiki/index.php/Code_Pages "Code Pages")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MAPUNICODE&oldid=8989>"




## Navigation menu








### Search





















