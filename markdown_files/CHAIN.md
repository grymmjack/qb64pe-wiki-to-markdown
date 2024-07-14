


CHAIN - QB64 Phoenix Edition Wiki








# CHAIN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
CHAIN is used to change seamlessly from one module to another one in a program.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Legacy support](#Legacy_support) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


CHAIN *moduleName$*
### Legacy support


* The multi-modular technique goes back to when **QBasic** and **QuickBASIC** had module size constraints. In **QB64** the CHAIN statement has been implemented so that that older code can still be compiled, though it is advisable to use single modules for a single project (not counting [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") libraries), for ease of sharing and also because the module size constraints no longer exist.


  




## Parameters


* *moduleName$* is a variable or a literal [STRING](/qb64wiki/index.php/STRING "STRING") value in quotation marks with the optional EXE or BAS file name extension.


  




## Description


* CHAIN requires that both the invoking and called modules are of either .BAS or .EXE file types.
* In Windows, **QB64** will automatically compile a CHAIN referenced BAS file if there is no EXE file found.
* CHAIN looks for a file extension that is the same as the invoking module's extension.
* The module's filename extension is not required. To save editing at compile time just omit the extensions in the calls.
* To pass data from one module to the other use [COMMON SHARED](/qb64wiki/index.php/COMMON_SHARED "COMMON SHARED"). The COMMON list should match [types](/qb64wiki/index.php/Variable_Types "Variable Types") and names.
* **QB64 does not retain the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode like QBasic did.**
* Variable data can be passed in files instead of using [COMMON SHARED](/qb64wiki/index.php/COMMON_SHARED "COMMON SHARED") values. **QB64** uses files to pass [COMMON](/qb64wiki/index.php/COMMON "COMMON") lists.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  

*QBasic/QuickBASIC:*



* Compiled EXE files had to include BRUN45.EXE in QuickBASIC 4.5 when CHAIN was used with [COMMON SHARED](/qb64wiki/index.php/COMMON_SHARED "COMMON SHARED").


  




## Examples


*Example:* CHAIN looks for same file type extension as program module (BAS or EXE).





| ```  CHAIN "Level1"  ``` |
| --- |


*Explanation:* The file referred to is "Level1.BAS" if the program module using the call is a BAS file. If the program was compiled, it would look for "Level1.EXE".


  




## See also


* [RUN](/qb64wiki/index.php/RUN "RUN")
* [COMMON](/qb64wiki/index.php/COMMON "COMMON"), [COMMON SHARED](/qb64wiki/index.php/COMMON_SHARED "COMMON SHARED")
* [SHARED](/qb64wiki/index.php/SHARED "SHARED")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CHAIN&oldid=8701>"




## Navigation menu








### Search





















