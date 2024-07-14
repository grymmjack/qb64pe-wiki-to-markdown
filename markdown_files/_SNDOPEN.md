


\_SNDOPEN - QB64 Phoenix Edition Wiki








# \_SNDOPEN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDOPEN function loads a sound file into memory and returns a [LONG](/qb64wiki/index.php/LONG "LONG") handle value above 0.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*soundHandle&* = \_SNDOPEN(*fileName$*[, *capabilities$*])
  




## Description


* Returns a [LONG](/qb64wiki/index.php/LONG "LONG") *soundHandle&* value to the sound file in memory. **A value of zero means the sound could not be loaded.**
* The literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") sound *fileName$* can be **WAV, AIFF, AIFC, FLAC, OGG, MP3, MID, IT, XM, S3M, MOD, RAD (v1 & v2), AHX, HVL & QOA** file types.
	+ **MID** support is enabled via the [$MIDISOUNDFONT](/qb64wiki/index.php/$MIDISOUNDFONT "$MIDISOUNDFONT") metacommand.
* The literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") *capabilities$* is optional but can be one of the following. Anything else is ignored. Multiple capability strings can be specified separated by a comma.
	+ **STREAM**: This will "stream" the sound into memory rather than fully decoding it.
	+ **MEMORY**: This will treat *fileName$* as a memory buffer containing the sound file instead of a file name.
* Short sounds should not be loaded using **STREAM**. Use **STREAM** when you want to play long sounds as background music and want to avoid loading delays.
* [\_MEMSOUND](/qb64wiki/index.php/MEMSOUND "MEMSOUND") will not work for sounds loaded using **STREAM** or **MEMORY**.
* **Always check the handle value returned is greater than zero before attempting to play the sound.**
* The handle can be used by most of the \_SND sound playing functions and statements in QB64 except [\_SNDPLAYFILE](/qb64wiki/index.php/SNDPLAYFILE "SNDPLAYFILE") which plays a sound file directly from the disk and does not use a handle value.
* Handles can be closed with [\_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") when the sound is no longer necessary.
* If a WAV sound file won't play, try it using the Windows [Play WAV sounds library](/qb64wiki/index.php/Windows_Libraries#Play_WAV_Sounds "Windows Libraries") to check it or convert the sound file to FLAC, OGG or MP3.


  




## Availability


* [![v0.610](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v0.610")

**v0.610**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


* Available for *Linux* since **QB64 v0.800** and for *macOS* since **QB64 v0.900**
* Until **QB64 v0.954** various formats and capabilities are supported via the SDL audio backend.
	+ See the historic page [\_SNDOPEN-v0.954](/qb64wiki/index.php/SNDOPEN-v0.954 "SNDOPEN-v0.954") for reference.
* In **QB64 v0.960** the underlying SDL library was exchanged by OpenGL (graphics) and OpenAL (sound) and as a result only the WAV, OGG, and MP3 formats are supported until today's current versions without any special capabilities.
	+ See historic page [\_SNDOPEN-v0.960](/qb64wiki/index.php/SNDOPEN-v0.960 "SNDOPEN-v0.960") for reference.
	+ This limitation also applies up to **QB64-PE v3.0.0** of the Phoenix Edition.
* Since **QB64-PE v3.1.0** the new formats FLAC, MOD, S3M, XM, IT and RAD were added to that very limited list, in the move away from OpenAL to the Miniaudio library in combination with separate and extensible player libraries.
	+ In this version also the new capability to STREAM the sound was added.
* With **QB64-PE v3.2.0** the MID format was added, but needs explicitly to be enabled via the [$MIDISOUNDFONT](/qb64wiki/index.php/$MIDISOUNDFONT "$MIDISOUNDFONT") metacommand.
* In **QB64-PE v3.5.0** the Amiga AHX and HVL formats were added to the list.
	+ In this version also the new capability to load sounds from MEMORY was added.
* In **QB64-PE v3.8.0** support for Apple's AIFF and AIFC formats was added.
* In **QB64-PE v3.9.0** support for Quite OK Audio (QOA) format was added.
* In **QB64-PE v3.9.0** the old OpenAL audio backend was finally removed.


  




## Examples


*Snippet 1:* Loading a sound file to use in the program later. Only load it once and use the handle any time you want.





| ``` h& = _SNDOPEN("dog.wav") IF h& <= 0 THEN BEEP ELSE [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") h&      'check for valid handle before using!  ``` |
| --- |


  

*Snippet 2:* Playing a sound from 2 different speakers based on program results.





| ``` ' This examples load, plays and then bounces the sound between the left and right channels Laff& = _SNDOPEN("KONGlaff.ogg", "stream") 'load sound file and get LONG handle value [IF](/qb64wiki/index.php/IF "IF") Laff& > 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") Laff& 'play sound [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to load sound file."     [END](/qb64wiki/index.php/END "END") [END](/qb64wiki/index.php/END "END") [IF](/qb64wiki/index.php/IF "IF")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press ESC to stop." dir = 0.01 [DO](/qb64wiki/index.php/DO "DO")     [IF](/qb64wiki/index.php/IF "IF") laffx! <= -1 [THEN](/qb64wiki/index.php/THEN "THEN") dir = 0.01     [IF](/qb64wiki/index.php/IF "IF") laffx! >= 1 [THEN](/qb64wiki/index.php/THEN "THEN") dir = -0.01     laffx! = laffx! + dir      [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , 1: [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") "Balance = ##.##"; laffx!;     [_SNDBAL](/qb64wiki/index.php/SNDBAL "SNDBAL") Laff&, laffx! 'balance sound to left or right speaker      [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_SNDPLAYING](/qb64wiki/index.php/SNDPLAYING "SNDPLAYING")(Laff&) [AND](/qb64wiki/index.php/AND "AND") [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") <> 27  ``` |
| --- |


  

*Snippet 3:* Loading a sound file from memory and then playing it.





| ``` [OPTION _EXPLICIT](/qb64wiki/index.php/OPTION_EXPLICIT "OPTION EXPLICIT")  [DIM](/qb64wiki/index.php/DIM "DIM") buffer [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"): buffer = LoadSlidingAwayData [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Size ="; [LEN](/qb64wiki/index.php/LEN "LEN")(buffer)  [DIM](/qb64wiki/index.php/DIM "DIM") h [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): h = _SNDOPEN(buffer, "memory") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Handle ="; h [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Length ="; [_SNDLEN](/qb64wiki/index.php/SNDLEN "SNDLEN")(h)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Looping audio..." [_SNDLOOP](/qb64wiki/index.php/SNDLOOP "SNDLOOP") h  [END](/qb64wiki/index.php/END "END")  ' This function reads the file directly from data and then returns the decompressed data [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") LoadSlidingAwayData$     [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") numL, numb, stroffs, i, dat     [DIM](/qb64wiki/index.php/DIM "DIM") rawdata [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING")      [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") Sliding_Away     [READ](/qb64wiki/index.php/READ "READ") numL, numb     rawdata = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")((numL * 4) + numb)     stroffs = 1      [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") numL         [READ](/qb64wiki/index.php/READ "READ") dat         [MID$](/qb64wiki/index.php/MID$ "MID$")(rawdata, stroffs, 4) = [MKL$](/qb64wiki/index.php/MKL$ "MKL$")(dat)         stroffs = stroffs + 4     [NEXT](/qb64wiki/index.php/NEXT "NEXT")      [IF](/qb64wiki/index.php/IF "IF") numb > 0 [THEN](/qb64wiki/index.php/THEN "THEN")         [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") numb             [READ](/qb64wiki/index.php/READ "READ") dat             [MID$](/qb64wiki/index.php/MID$ "MID$")(rawdata, stroffs, 1) = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(dat)             stroffs = stroffs + 1         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [END IF](/qb64wiki/index.php/END_IF "END IF")      LoadSlidingAwayData = [_INFLATE$](/qb64wiki/index.php/INFLATE$ "INFLATE$")(rawdata)      '--- DATAs representing the contents of file sliding_away.hvl     '---------------------------------------------------------------------     Sliding_Away:     [DATA](/qb64wiki/index.php/DATA "DATA") 192,10     [DATA](/qb64wiki/index.php/DATA "DATA") &H56A59C78,&H51134F5B,&H7766FE10,&HE96D0B6B,&HC5258202,&H5BAED8BA,&H840A956B,&HFBB240F8     [DATA](/qb64wiki/index.php/DATA "DATA") &H3E2483E0,&H4B3E24A0,&H018928C4,&H6217892F,&H9F813FA2,&H47E14FC0,&H3D1356F1,&HED9D9EB7     [DATA](/qb64wiki/index.php/DATA "DATA") &H9A78DA05,&HFB3399CE,&HCCE677CD,&HB3CE6ECC,&H7451CF57,&HDF05877E,&H02F0F2DF,&H0F297204     [DATA](/qb64wiki/index.php/DATA "DATA") &HA39E8435,&HF47BD182,&H9ED67297,&H95727A62,&HC2AD1C62,&HF6E174BD,&HFC52E2CC,&HCDF31E7B     [DATA](/qb64wiki/index.php/DATA "DATA") &H8C1BFE31,&H0530CF3F,&HFC639FC6,&H767F8C33,&H3E117F0C,&H12FE196E,&HFC3551E6,&HC5602C65     [DATA](/qb64wiki/index.php/DATA "DATA") &H88B0E660,&H622FE19A,&HBF86AB19,&H6DB89B82,&H42588BF8,&HFF9CEADD,&HFE69F88E,&HFE8E0AA2     [DATA](/qb64wiki/index.php/DATA "DATA") &HB4151E28,&HB77813DB,&HC0F00F98,&HB1D0D7E2,&H6878BBF8,&HB23C0DF1,&H2DD626F8,&HE2D7443E     [DATA](/qb64wiki/index.php/DATA "DATA") &HC5B1E1EF,&HF8B0D847,&H35213616,&H7DC6DF37,&HBF4CA16C,&H51D38F90,&H988C1126,&H6396662B     [DATA](/qb64wiki/index.php/DATA "DATA") &H92BEE941,&H82D4AECA,&HAE19975A,&H84D3803F,&H78C59C84,&H2FDA3819,&H91FEB274,&HBD99B759     [DATA](/qb64wiki/index.php/DATA "DATA") &H696D74A3,&H9EC47B19,&HD31127F3,&H7BFBB907,&H55F2AF36,&H07F1906A,&H48D709CE,&H28535583     [DATA](/qb64wiki/index.php/DATA "DATA") &H14E43B7B,&H26A6E166,&HC5B6BE73,&H9987436B,&H4B9F9E0D,&H711ECA4F,&H1F8A569A,&H4C4C7F8E     [DATA](/qb64wiki/index.php/DATA "DATA") &HD687B61D,&H169A5E4D,&H2C214CDF,&H606A9A4F,&H39E3E02F,&H19D3C0E2,&HBB2BA06B,&H44260BBA     [DATA](/qb64wiki/index.php/DATA "DATA") &H36837A77,&HD7E5755B,&H8B6D5EB2,&HE2BD64E8,&H5DAFD7B6,&H511EC46B,&H28D99976,&HB2229E54     [DATA](/qb64wiki/index.php/DATA "DATA") &H119E361B,&H7F0D34A1,&H3F556E80,&H54E38DA8,&HB2C43EA2,&H4A6A18AA,&H6D68D8AE,&HDD4B1A0F     [DATA](/qb64wiki/index.php/DATA "DATA") &HB08FCF44,&H9F93723A,&H9BF305C9,&H0940B334,&H77655317,&HCFA7E047,&H1FABC0EE,&HB2C99E6B     [DATA](/qb64wiki/index.php/DATA "DATA") &H6938C69D,&HD2B70456,&H3A4AA7FE,&H9A5571BE,&H72E75DE4,&HC6436D54,&H63C88D17,&H3B1E4C6B     [DATA](/qb64wiki/index.php/DATA "DATA") &H7D6DAFC6,&H2D781D78,&H551D6B43,&H6D631693,&H0CA258D9,&HC2AD8353,&HDBED2EA1,&HE7D494D6     [DATA](/qb64wiki/index.php/DATA "DATA") &HDB5D33AA,&HD774C635,&HB7B60E08,&HEA3C14D4,&HAE70F1F7,&H15274254,&H20DB7E57,&HDF3624DB     [DATA](/qb64wiki/index.php/DATA "DATA") &HD967DE36,&H34FB694A,&H5CF3EAD5,&H3714A95D,&HDFB4B55D,&H8E1B15F5,&HD4C09FBB,&HB2E5593E     [DATA](/qb64wiki/index.php/DATA "DATA") &HAE7965FB,&H1C50DEAF,&H4AADD413,&HCCF2D114,&H3C053CBE,&H2131FA2A,&HA86FB8EF,&H8B5EE49A     [DATA](/qb64wiki/index.php/DATA "DATA") &H8E4EC59B,&H4A212712,&HE24DEF20,&H5CD1131F,&H8F7D3BC9,&HBACE8D52,&H48140715,&HF214BADF     [DATA](/qb64wiki/index.php/DATA "DATA") &H2F5717E5,&HF0A5E631,&H5148A8A5,&HF4DD4296,&HDD4AEDD4,&HA3C4BD17,&HB991EF24,&H2C4E0200     [DATA](/qb64wiki/index.php/DATA "DATA") &HE1EE4B6F,&H5A527069,&H07B674FC,&HDA9EC13F,&H70AF9D0A,&HA12937B6,&H196D4427,&H8BD50886     [DATA](/qb64wiki/index.php/DATA "DATA") &H3422259D,&HE5FA7FC8,&HD1E1D1C3,&HE0E0BBF1,&H7C0FC1DB,&HE4F9FB7F,&H760F5838,&H63EEEE5F     [DATA](/qb64wiki/index.php/DATA "DATA") &HA3,&HDB,&HDD,&H16,&HF8,&H7F,&HEE,&H68,&H18,&HB9 [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


  




## See also


* [\_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE"), [\_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY"), [\_SNDSTOP](/qb64wiki/index.php/SNDSTOP "SNDSTOP")
* [\_SNDPAUSE](/qb64wiki/index.php/SNDPAUSE "SNDPAUSE"), [\_SNDLOOP](/qb64wiki/index.php/SNDLOOP "SNDLOOP"), [\_SNDLIMIT](/qb64wiki/index.php/SNDLIMIT "SNDLIMIT")
* [\_SNDSETPOS](/qb64wiki/index.php/SNDSETPOS "SNDSETPOS"), [\_SNDGETPOS](/qb64wiki/index.php/SNDGETPOS "SNDGETPOS")
* [\_SNDPLAYING](/qb64wiki/index.php/SNDPLAYING "SNDPLAYING"), [\_SNDPAUSED](/qb64wiki/index.php/SNDPAUSED "SNDPAUSED")
* [\_SNDCOPY](/qb64wiki/index.php/SNDCOPY "SNDCOPY"), [\_SNDPLAYCOPY](/qb64wiki/index.php/SNDPLAYCOPY "SNDPLAYCOPY")
* [\_SNDBAL](/qb64wiki/index.php/SNDBAL "SNDBAL"), [\_SNDLEN](/qb64wiki/index.php/SNDLEN "SNDLEN"), [\_SNDVOL](/qb64wiki/index.php/SNDVOL "SNDVOL")
* [\_SNDPLAYFILE](/qb64wiki/index.php/SNDPLAYFILE "SNDPLAYFILE")
* [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW"), [\_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE"), [\_SNDRAWLEN](/qb64wiki/index.php/SNDRAWLEN "SNDRAWLEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDOPEN&oldid=8900>"




## Navigation menu








### Search





















