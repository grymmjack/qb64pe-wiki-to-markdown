


$INCLUDEONCE - QB64 Phoenix Edition Wiki








# $INCLUDEONCE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **$INCLUDEONCE** metacommand, when placed in include files, prevents that the file's contents is injected multiple times into a program, even if the file is [included](/qb64wiki/index.php/$INCLUDE "$INCLUDE") multiple times directly or indirectly through other include files.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


$INCLUDEONCE
  




## Description


* As QB64 [metacommand](/qb64wiki/index.php/Metacommand "Metacommand") it does not require a comment *['](/qb64wiki/index.php/Apostrophe "Apostrophe")* or [REM](/qb64wiki/index.php/REM "REM") before it.
* It can be placed everywhere in an include file, but must be the **only** thing in the line, hence without additional whitespace or comments.
	+ Even if placed in the middle or the end of the file, it always designates the **entire** file contents.
* If placed in the main program, **$INCLUDEONCE** does nothing and is simply ignored without error.
* **$INCLUDEONCE** will not work when placed inside pre-compiler [$IF](/qb64wiki/index.php/$IF "$IF")..[$ELSE](/qb64wiki/index.php/$ELSE "$ELSE")...[$END IF](/qb64wiki/index.php/$END_IF "$END IF") blocks.


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.12.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.12.0")

**v3.12.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


Example
* Show how the command prevents included code to be injected multiple times.
* First save the include files in your qb64pe folder, then take the main program.

**Save as "once.bm"**


| ``` 'included by test.bas and incl.bm  $INCLUDEONCE  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This prints from file once.bm, and should appear only once on screen."  ``` |
| --- |


**Save as "incl.bm"**


| ``` 'included 2 times by test.bas  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This prints from file incl.bm, it should appear 2 times on screen."  '[$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE"): 'once.bm'  ``` |
| --- |


**Save as "test.bas"**


| ``` 'this is a test for $INCLUDEONCE behavior  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This prints from the test.bas main program."  '[$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE"): 'incl.bm' '[$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE"): 'once.bm' '[$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE"): 'incl.bm'  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


**If it works, the output looks like this...**


| ``` This prints from the test.bas main program.  This prints from file incl.bm, it should appear 2 times on screen.  This prints from file once.bm, and should appear only once on screen.  This prints from file incl.bm, it should appear 2 times on screen.  ``` |
| --- |




| ``` **Explanation**  Even as the file *once.bm* is included 3 times into the *test.bas* program  (2 times indirectly through *incl.bm* and 1 time directly), the contained  PRINT statements are injected only once into the program due to the use  of the $INCLUDEONCE metacommand.  ``` |
| --- |


Examples by RhoSigma
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2685)
* [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE")
* [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$INCLUDEONCE&oldid=8947>"




## Navigation menu








### Search





















