


\_OS$ - QB64 Phoenix Edition Wiki








# \_OS$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_OS$ function returns the operating system and QB64 compiler bit version **used to compile** a QB64 program.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*compilerVersion$* = \_OS$
  




## Description


* Returns a [STRING](/qb64wiki/index.php/STRING "STRING") listing the OS as [WINDOWS], [LINUX] or [MACOSX] and the compiler bit format of [32BIT] or [64BIT]. Example: [WINDOWS][32BIT]
* Allows a BAS program to be compiled with QB64 in Windows, Linux or macOS using different OS or language specifications.
* Use the return *compilerVersion$* to specify the current OS code to use when a BAS program is compiled using another version of the QB64 compiler.
* Windows can use either a 32 (default) or 64 bit compiler. Linux and macOS use 64 bit by default.


Important Note
* Even if you're on a 64-bit Windows system, the \_OS$ function may return [32BIT].
* That is, if your program was compiled with the 32-bit version of QB64, hence it's a 32-bit executable running on 64-bit Windows.
* This is by design and not a bug, as your program gets the information it needs to run (e.g. to use 32-bit or 64-bit DLL using DECLARE DYNAMIC LIBRARY) and not what you as user would expect to see according to your system.
* That's why the "**used to compile**" phrase was printed bold in the first line above.

  




## See also


* [ENVIRON$](/qb64wiki/index.php/ENVIRON$ "ENVIRON$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OS$&oldid=7920>"




## Navigation menu








### Search





















