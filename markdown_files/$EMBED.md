


$EMBED - QB64 Phoenix Edition Wiki








# $EMBED



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **$EMBED** metacommand can embed any designated file (e.g. images, sounds, fonts and all other file types) into the compiled EXE file. You can roughly compare this to converting and placing a file's contents into [DATA](/qb64wiki/index.php/DATA "DATA") lines, but **$EMBED** obviously is much more convenient.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


$EMBED**:**'*filename*'**,**'*handle*'
  




## Parameters


IMPORTANT

* Both parameters must be enclosed in single quotes and given as literal strings, variables cannot be used here.
* Your inputs are checked while typing to ensure its validity, warnings (if any) will be displayed immediately in the IDE status area.

* The *filename* is the name of the file to embed, if required inclusive a full or relative path.
* The *handle* is a unique case sensitive identifier beginning with a letter and only containing lower/upper case letters and/or numbers, it's used later in the [\_EMBEDDED$](/qb64wiki/index.php/EMBEDDED$ "EMBEDDED$") call to recall the embedded data.
	+ You can compare this identifier to the line label in front of a [DATA](/qb64wiki/index.php/DATA "DATA") block, which is later used in a [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") call to set the [READ](/qb64wiki/index.php/READ "READ") pointer to exactly that [DATA](/qb64wiki/index.php/DATA "DATA") block.


  




## Description


* All files will be embedded in a compressed form, if a 20% least ratio is reached.
	+ This low ratio was chosen, cause it will be reached by most files, except those which are already highly compressed such as PNG, JPG, MP3/4, ZIP, 7z etc. and are not worth the additional effort for just a few bytes less.
* To recall the embedded file data use the [\_EMBEDDED$](/qb64wiki/index.php/EMBEDDED$ "EMBEDDED$") call with the very same *handle* identifier which was used in the respective file's **$EMBED** line. That call also does the decompression, if required.
* Embedding files can be useful to deliver a program inclusive all required assets in just one EXE file.
* No more worries whether a user installs your program correctly and retains the required folder structure.
* If required, you can easily write the files back to disk using the [\_WRITEFILE](/qb64wiki/index.php/WRITEFILE "WRITEFILE") command, i.e. you could create your own simple installer or package manager.
* Embedded images, sounds or fonts can be passed directly to [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") or [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT") respectively when using the *memory load* capabilities of these functions.
* The **$EMBED** metacommand can be used everywhere in a program. You may even place it inside pre-compiler [$IF](/qb64wiki/index.php/$IF "$IF")..[$ELSE](/qb64wiki/index.php/$ELSE "$ELSE")...[$END IF](/qb64wiki/index.php/$END_IF "$END IF") blocks and only the files designated in the true block are embedded then.
* How many or how big files you can embed depends on your system achitecture (x86/x64) as well as your installed memory. However, it should work just fine for all the normally expected working cases like embedding a font, a spritesheet and some level graphics as well a couple sound effects.
* To avoid useless bloat of the compiled EXE file, the embedding process is smart enough to only embed those files, which are recalled by the [\_EMBEDDED$](/qb64wiki/index.php/EMBEDDED$ "EMBEDDED$") call at least once. I.e. you may **$EMBED** a dozen files, but if you recall only one of it in your program, then only that one file will be really embedded, while the other files are simply ignored.


  




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


| ``` $EMBED:'source\peLogo.png','bigImg' $EMBED:'source\qb64pe.png','smallImg'  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32)  bi& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")([_EMBEDDED$](/qb64wiki/index.php/EMBEDDED$ "EMBEDDED$")("bigImg"), 32, "memory") si& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")([_EMBEDDED$](/qb64wiki/index.php/EMBEDDED$ "EMBEDDED$")("smallImg"), 32, "memory")  [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (140, 180), bi& [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (410, 230), si&  [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") si& [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") bi&  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Example by RhoSigma
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2740)
* [\_EMBEDDED$](/qb64wiki/index.php/EMBEDDED$ "EMBEDDED$")
* [DATA](/qb64wiki/index.php/DATA "DATA"), [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE"), [READ](/qb64wiki/index.php/READ "READ")
* [\_LOADFONT](/qb64wiki/index.php/LOADFONT "LOADFONT"), [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$EMBED&oldid=9018>"




## Navigation menu








### Search





















