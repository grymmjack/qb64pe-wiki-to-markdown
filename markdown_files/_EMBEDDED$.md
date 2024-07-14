


\_EMBEDDED$ - QB64 Phoenix Edition Wiki








# \_EMBEDDED$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_EMBEDDED$** function is used to recall the data of a file which was earlier embedded into the EXE file using the [$EMBED](/qb64wiki/index.php/$EMBED "$EMBED") metacommand. You can roughly compare this to a [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") to any [DATA](/qb64wiki/index.php/DATA "DATA") block and then using [READ](/qb64wiki/index.php/READ "READ") to retrieve the data.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*filedata$* = \_EMBEDDED$("*handle*")
  




## Parameters


IMPORTANT

* The parameter *handle* must be given as a single literal string enclosed in quotes, variables cannot be used here.
* Your inputs are checked while typing to ensure its validity, warnings (if any) will be displayed immediately in the IDE status area.

* The *filedata$* will receive the embedded file data as a single contiguous string, just as you would regularly [OPEN](/qb64wiki/index.php/OPEN "OPEN") the file and read its entire contents into that string.
* The *handle* is a unique case sensitive identifier beginning with a letter and only containing lower/upper case letters and/or numbers. It must exactly match the *handle* value used to [$EMBED](/qb64wiki/index.php/$EMBED "$EMBED") the respective file.
	+ You can compare this identifier to the line label in front of a [DATA](/qb64wiki/index.php/DATA "DATA") block, which is later used in a [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") call to set the [READ](/qb64wiki/index.php/READ "READ") pointer to exactly that [DATA](/qb64wiki/index.php/DATA "DATA") block.


  




## Description


* All embedded files can be recalled individually by using its respective *handle* identifier.
	+ If required, decompression is done internally, hence you always get back the original file contents.
* Recalling a file multiple times is possible, but in regard for the needed decompression time considered inefficient. Rather recall the file once and store the result in a [STRING](/qb64wiki/index.php/STRING "STRING") variable, if you know you need it multiple times in your program.
* To easily embed a file into your compiled EXE file use the [$EMBED](/qb64wiki/index.php/$EMBED "$EMBED") metacommand.
* Embedding files can be useful to deliver a program inclusive all required assets in just one EXE file.
* No more worries whether a user installs your program correctly and retains the required folder structure.
* If required, you can easily write the files back to disk using the [\_WRITEFILE](/qb64wiki/index.php/WRITEFILE "WRITEFILE") command, i.e. you could create your own simple installer or package manager.
* Embedded images, sounds or fonts can be passed directly to [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") or [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT") respectively when using the *memory load* capabilities of these functions.


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.10.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.10.0")

**v3.10.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


Example
Embeds two image files into the compiled EXE, then memory loads and displays it.


| ``` [$EMBED](/qb64wiki/index.php/$EMBED "$EMBED"):'source\peLogo.png','bigImg' [$EMBED](/qb64wiki/index.php/$EMBED "$EMBED"):'source\qb64pe.png','smallImg'  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32)  bi& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")(_EMBEDDED$("bigImg"), 32, "memory") si& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")(_EMBEDDED$("smallImg"), 32, "memory")  [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (140, 180), bi& [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (410, 230), si&  [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") si& [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") bi&  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Example by RhoSigma
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2740)
* [$EMBED](/qb64wiki/index.php/$EMBED "$EMBED")
* [DATA](/qb64wiki/index.php/DATA "DATA"), [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE"), [READ](/qb64wiki/index.php/READ "READ")
* [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT"), [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=EMBEDDED$&oldid=9019>"




## Navigation menu








### Search





















