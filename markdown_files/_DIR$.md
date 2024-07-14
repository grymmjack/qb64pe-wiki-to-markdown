


\_DIR$ - QB64 Phoenix Edition Wiki








# \_DIR$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_DIR$** function returns common paths such as Documents, Pictures, Music, Desktop, etc.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*d$* = \_DIR$("*folderspecification*")
  




## Parameters


* *folderspecification* may be "desktop", "downloads", "documents", "music", "video", "pictures", "appdata", "common program data", "local data", "program files", "program files (x86)", "temp", "home", "fonts", "user fonts".
* Some variation is accepted for the folder specification:


MY DOCUMENTS, TEXT, DOCUMENT, DOCUMENTS, DOWNLOAD, DOWNLOADS
MY MUSIC, MUSIC, AUDIO, SOUND, SOUNDS
MY PICTURES, PICTURE, PICTURES, IMAGE, IMAGES, PHOTO, PHOTOS, DCIM, CAMERA, CAMERA ROLL
MY VIDEOS, VIDEO, VIDEOS, MOVIE, MOVIES,
DATA, APPDATA, APPLICATION DATA, PROGRAM DATA, LOCAL DATA, LOCALAPPDATA, LOCAL APPLICATION DATA, LOCAL PROGRAM DATA
PROGRAMFILES, PROGRAMFILESX86, PROGRAMFILES X86, PROGRAM FILES X86, PROGRAM FILES 86, PROGRAMFILES (X86), PROGRAM FILES(X86), PROGRAMFILES(X86)
FONT, USERFONT, USERFONTS, USER FONT
USER, PROFILE, USERPROFILE, USER PROFILE
  




## Description


* The path returned ends with a backslash on Windows and a forward-slash on Linux and macOS.
* A nonexistent folder specification usually defaults to the Desktop folder path.


  




## Availability


* [![v1.1](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v1.1")

**v1.1**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


* In **QB64-PE v3.11.0** support for "font" & "user font" and full Linux and macOS support was added.


  




## Examples


Example
Displaying default paths in Windows.


| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "DESKTOP=" + _DIR$("desktop") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "DOWNLOADS=" + _DIR$("download") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "DOCUMENTS=" + _DIR$("my documents") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "PICTURES=" + _DIR$("pictures") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "MUSIC=" + _DIR$("music") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "VIDEO=" + _DIR$("video") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "APPLICATION DATA=" + _DIR$("data") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "LOCAL APPLICATION DATA=" + _DIR$("local application data")  ``` |
| --- |




| ``` DESKTOP=C:\Documents and Settings\Administrator\Desktop\ DOWNLOADS=C:\Documents and Settings\Administrator\Downloads\ DOCUMENTS=C:\Documents and Settings\Administrator\My Documents\ PICTURES=C:\Documents and Settings\Administrator\My Documents\My Pictures\ MUSIC=C:\Documents and Settings\Administrator\My Documents\My Music\ VIDEO=C:\Documents and Settings\Administrator\My Documents\My Videos\ APPLICATION DATA=C:\Documents and Settings\Administrator\Application Data\ LOCAL APPLICATION DATA=C:\Documents and Settings\Administrator\Local Settings\Application Data\  ``` |
| --- |


  




## See also


* [\_CWD$](/qb64wiki/index.php/CWD$ "CWD$")
* [\_STARTDIR$](/qb64wiki/index.php/STARTDIR$ "STARTDIR$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DIR$&oldid=8624>"




## Navigation menu








### Search





















