


$LET - QB64 Phoenix Edition Wiki








# $LET



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
$LET is a precompiler command, which helps to include and/or exclude sections of code in a program based on OS/bit-size or other predefined conditions.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


$LET variable = expression
  




## Description


* Unlike [LET](/qb64wiki/index.php/LET "LET"), $LET is not optional.
* $LET a = 12 sets a precompiler variable "a" to the value of 12. This variable is only valid for the precompiler itself and does nothing to affect the values of any variable/constant which might also be called "a" in the program.
* Variable names must follow QB64's variable naming conventions.
* You can check a precompiler variable against special values **DEFINED** and **UNDEFINED**, in order to assess whether the variable has already been assigned a value. Useful for code in libraries which may be repeated.
* The precompiler comes with some preset values which can be used to help determine which code blocks to include/exclude. These are:
	+ **WIN** or **WINDOWS** if the user is running QB64 in a Windows environment.
	+ **LINUX** if the user is running QB64 in a Linux environment.
	+ **MAC** or **MACOSX** if the user is running QB64 in a macOS environment.
	+ **32BIT** if the user is running a 32-bit version of QB64.
	+ **64BIT** if the user is running a 64-bit version of QB64.
	+ **VERSION**, which is set to the version of the QB64 compiler.


  




## Examples


* See example 1 in [$IF](/qb64wiki/index.php/$IF "$IF").


  




## See also


* [$IF](/qb64wiki/index.php/$IF "$IF")
* [$ELSE](/qb64wiki/index.php/$ELSE "$ELSE")
* [$ELSEIF](/qb64wiki/index.php/$ELSEIF "$ELSEIF")
* [$END IF](/qb64wiki/index.php/$END_IF "$END IF")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$LET&oldid=4906>"




## Navigation menu








### Search





















