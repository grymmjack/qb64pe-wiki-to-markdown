


\_MEMSOUND - QB64 Phoenix Edition Wiki








# \_MEMSOUND



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_MEMSOUND** function returns a [\_MEM](/qb64wiki/index.php/MEM "MEM") value referring to a sound's raw data in memory using a designated sound handle created by the [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") or [\_SNDNEW](/qb64wiki/index.php/SNDNEW "SNDNEW") function.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*soundBlock* = \_MEMSOUND(*soundHandle&*[, *channel&*])
  




## Parameters


* The *soundBlock* [\_MEM](/qb64wiki/index.php/MEM "MEM") type variable holds the read-only elements .OFFSET, .SIZE, .ELEMENTSIZE, .TYPE and .SOUND.
	+ **.OFFSET** is the starting memory address of the sound sample data.
	+ **.SIZE** is the size of the sample data in **bytes**
	+ **.ELEMENTSIZE** will contain the number of **bytes-per-sample** the audio contains.
		- Can return 1 (8-bit mono), 2 (8-bit stereo), 2 (16-bit mono), 4 (16-bit stereo), 4 (32-bit mono) or 8 (32-bit stereo).
		- Use **.TYPE** to determine the data type of the sample data.
	+ **.TYPE** will contain the data type of the sample data. See [\_MEM](/qb64wiki/index.php/MEM "MEM") for details.
	+ **.SOUND** will contain the same handle value as returned by the [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") function.
* The second parameter *channel&* is optional and deprecated. This was used to specify the sound channel. In **QB64-PE v3.1.0** and above stereo data is always interleaved. You must use **.ELEMENTSIZE** and **.TYPE** to determine the type of audio data you are dealing with.


  




## Description


* Use this function to obtain a pointer to the raw sound data in memory for direct access.
* Even if the memory pointer obtained by this fuction was already freed again using [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE"), the respective Sound handle itself must still be freed using [\_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") when no longer required.
* If .SIZE returns 0, that means the data could not be accessed. It may happen if you try to access the right channel in a mono file or the format simply does not support accessing raw PCM samples.
* *channel&* - 1 (left channel/mono) or 2 (right channel; for stereo files) was supported on the old OpenAL backend. For the new miniaudio backend, this must be 0.


  




## Availability


* **QB64 v1.5 and up**
* **QB64-PE all versions**


  




## Examples


Example 1
Checking that a sound file is stereo.


| ``` [OPTION _EXPLICIT](/qb64wiki/index.php/OPTION_EXPLICIT "OPTION EXPLICIT")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Loading..."; [DIM](/qb64wiki/index.php/DIM "DIM") Song [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") Song = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("onward_ride1.flac") ' Replace file name with your sound file [IF](/qb64wiki/index.php/IF "IF") Song < 1 [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to load sound!"     [END](/qb64wiki/index.php/END "END") [END IF](/qb64wiki/index.php/END_IF "END IF") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Done!"  [DIM](/qb64wiki/index.php/DIM "DIM") Channels [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") Channels = SndChannels(Song)  [IF](/qb64wiki/index.php/IF "IF") Channels = 2 [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This file is STEREO" [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") Channels = 1 [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This file is MONO" [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "An error occurred." [END IF](/qb64wiki/index.php/END_IF "END IF")  [_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") Song 'closing the sound releases the mem blocks  [END](/qb64wiki/index.php/END "END")   ' This function returns the number of sound channels for a valid sound "handle" ' 2 = stereo, 1 = mono, 0 = error [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") SndChannels~%% (handle [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [DIM](/qb64wiki/index.php/DIM "DIM") SampleData [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM")      SndChannels = 0 ' Assume failure      ' Check if the sound is valid     SampleData = _MEMSOUND(handle, 0)     [IF](/qb64wiki/index.php/IF "IF") SampleData.SIZE = 0 [THEN](/qb64wiki/index.php/THEN "THEN")         [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION")     [END IF](/qb64wiki/index.php/END_IF "END IF")      ' Check the data type and then decide if the sound is stereo or mono     [IF](/qb64wiki/index.php/IF "IF") SampleData.TYPE = 260 [THEN](/qb64wiki/index.php/THEN "THEN") ' 32-bit floating point         [IF](/qb64wiki/index.php/IF "IF") SampleData.ELEMENTSIZE = 4 [THEN](/qb64wiki/index.php/THEN "THEN")             SndChannels = 1         [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.ELEMENTSIZE = 8 [THEN](/qb64wiki/index.php/THEN "THEN")             SndChannels = 2         [END IF](/qb64wiki/index.php/END_IF "END IF")     [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.TYPE = 132 [THEN](/qb64wiki/index.php/THEN "THEN") ' 32-bit integer         [IF](/qb64wiki/index.php/IF "IF") SampleData.ELEMENTSIZE = 4 [THEN](/qb64wiki/index.php/THEN "THEN")             SndChannels = 1         [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.ELEMENTSIZE = 8 [THEN](/qb64wiki/index.php/THEN "THEN")             SndChannels = 2         [END IF](/qb64wiki/index.php/END_IF "END IF")     [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.TYPE = 130 [THEN](/qb64wiki/index.php/THEN "THEN") ' 16-bit integer         [IF](/qb64wiki/index.php/IF "IF") SampleData.ELEMENTSIZE = 2 [THEN](/qb64wiki/index.php/THEN "THEN")             SndChannels = 1         [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.ELEMENTSIZE = 4 [THEN](/qb64wiki/index.php/THEN "THEN")             SndChannels = 2         [END IF](/qb64wiki/index.php/END_IF "END IF")     [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.TYPE = 1153 [THEN](/qb64wiki/index.php/THEN "THEN") ' 8-bit unsigned integer         [IF](/qb64wiki/index.php/IF "IF") SampleData.ELEMENTSIZE = 1 [THEN](/qb64wiki/index.php/THEN "THEN")             SndChannels = 1         [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.ELEMENTSIZE = 2 [THEN](/qb64wiki/index.php/THEN "THEN")             SndChannels = 2         [END IF](/qb64wiki/index.php/END_IF "END IF")     [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.TYPE = 0 [THEN](/qb64wiki/index.php/THEN "THEN") ' This means this is an OpenAL sound handle         [DIM](/qb64wiki/index.php/DIM "DIM") RightChannel [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM")         RightChannel = _MEMSOUND(handle, 2)         [IF](/qb64wiki/index.php/IF "IF") RightChannel.SIZE > 0 [THEN](/qb64wiki/index.php/THEN "THEN")             SndChannels = 2         [ELSE](/qb64wiki/index.php/ELSE "ELSE")             SndChannels = 1         [END IF](/qb64wiki/index.php/END_IF "END IF")     [END IF](/qb64wiki/index.php/END_IF "END IF") [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |




---


Example 2
Plotting a sound's waves.


| ``` [OPTION](/qb64wiki/index.php/OPTION "OPTION") [_EXPLICIT](/qb64wiki/index.php/EXPLICIT "EXPLICIT")  [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")     [$IF](/qb64wiki/index.php/$IF "$IF") 32BIT [THEN](/qb64wiki/index.php/THEN "THEN")         [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") ConvertOffset~& [ALIAS](/qb64wiki/index.php/ALIAS "ALIAS") "uintptr_t" ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") o [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_OFFSET](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)"))     [$ELSE](/qb64wiki/index.php/$ELSE "$ELSE")         [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") ConvertOffset~&& [ALIAS](/qb64wiki/index.php/ALIAS "ALIAS") "uintptr_t" ([BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") o [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_OFFSET](/qb64wiki/index.php/OFFSET_(function) "OFFSET (function)"))     [$END IF](/qb64wiki/index.php/$END_IF "$END IF")  [END DECLARE](/qb64wiki/index.php/END_DECLARE "END DECLARE")  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 327, 32)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Loading..."; [DIM](/qb64wiki/index.php/DIM "DIM") Song [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): Song = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("OPL3 Groove.rad") ' replace this with your (WAV, AIFF, AIFC, FLAC, OGG, MP3, MID, IT, XM, S3M, MOD, RAD, AHX, HVL, QOA) sound file [IF](/qb64wiki/index.php/IF "IF") Song < 1 [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to load song!"     [END](/qb64wiki/index.php/END "END") [END IF](/qb64wiki/index.php/END_IF "END IF") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Done!"  [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") Song  [DIM](/qb64wiki/index.php/DIM "DIM") SampleData [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM"): SampleData = _MEMSOUND(Song, 0) [IF](/qb64wiki/index.php/IF "IF") SampleData.SIZE = 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to access sound sample data."     [END](/qb64wiki/index.php/END "END") [END IF](/qb64wiki/index.php/END_IF "END IF")  [DIM](/qb64wiki/index.php/DIM "DIM") sz [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64"): sz = ConvertOffset(SampleData.ELEMENTSIZE) ' sz is the total size of the sound in bytes [DIM](/qb64wiki/index.php/DIM "DIM") x [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), i [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")  [DO UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") = 27 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") [NOT](/qb64wiki/index.php/NOT "NOT") [_SNDPLAYING](/qb64wiki/index.php/SNDPLAYING "SNDPLAYING")(Song) [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") i + ([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") * sz) > SampleData.SIZE     [CLS](/qb64wiki/index.php/CLS "CLS")     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") i; "/"; SampleData.SIZE, "Frame Size ="; sz, "Data Type ="; SampleData.TYPE      [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING"):[OFF](/qb64wiki/index.php/OFF "OFF")     [IF](/qb64wiki/index.php/IF "IF") SampleData.TYPE = 130 [THEN](/qb64wiki/index.php/THEN "THEN") ' 128 OR 2: integer stereo or mono         [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") - 1             [DIM](/qb64wiki/index.php/DIM "DIM") si [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"): si = [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(SampleData, SampleData.OFFSET + i + x * sz, [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")) ' get sound data             [LINE](/qb64wiki/index.php/LINE "LINE") (x, [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") / 2)-[STEP](/qb64wiki/index.php/STEP "STEP")(0, 300 * si / 32768), [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(0, 111, 0) 'plot wave         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.TYPE = 260 [THEN](/qb64wiki/index.php/THEN "THEN") ' 256 OR 4: floating point stereo or mono         [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") - 1             [DIM](/qb64wiki/index.php/DIM "DIM") sf [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): sf = [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(SampleData, SampleData.OFFSET + i + x * sz, [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")) ' get sound data             [LINE](/qb64wiki/index.php/LINE "LINE") (x, [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") / 2)-[STEP](/qb64wiki/index.php/STEP "STEP")(0, sf * 300), [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(0, 111, 0) 'plot wave         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") SampleData.TYPE = 1153 [THEN](/qb64wiki/index.php/THEN "THEN") ' 128 OR 1 OR 1024: unsigned byte stereo or mono         [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") - 1             [DIM](/qb64wiki/index.php/DIM "DIM") sb [AS](/qb64wiki/index.php/AS "AS") [_BYTE](/qb64wiki/index.php/BYTE "BYTE"): sb = [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(SampleData, SampleData.OFFSET + i + x * sz, [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")) [XOR](/qb64wiki/index.php/XOR "XOR") &H80 ' get sound data and convert to signed             [LINE](/qb64wiki/index.php/LINE "LINE") (x, [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") / 2)-[STEP](/qb64wiki/index.php/STEP "STEP")(0, 300 * sb / 128), [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(0, 111, 0) ' plot wave         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [END IF](/qb64wiki/index.php/END_IF "END IF")     [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING"):[ON](/qb64wiki/index.php/ON "ON")      [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60      i = [FIX](/qb64wiki/index.php/FIX "FIX")([_SNDGETPOS](/qb64wiki/index.php/SNDGETPOS "SNDGETPOS")(Song) * [_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE")) * sz ' calculate the new sample frame position [LOOP](/qb64wiki/index.php/LOOP "LOOP")  [_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") Song ' closing the sound releases the mem blocks [_AUTODISPLAY](/qb64wiki/index.php/AUTODISPLAY "AUTODISPLAY") [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [\_MEM](/qb64wiki/index.php/MEM "MEM"), [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE")
* [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT"), [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMGET (function)](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), [\_SNDNEW](/qb64wiki/index.php/SNDNEW "SNDNEW"), [\_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE"), [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW")
* [\_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMSOUND&oldid=8569>"




## Navigation menu








### Search





















