


\_COMMANDCOUNT - QB64 Phoenix Edition Wiki








# \_COMMANDCOUNT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_COMMANDCOUNT function returns the number or arguments passed from the command line to the [COMMAND$](/qb64wiki/index.php/COMMAND$ "COMMAND$") function.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result&* = \_COMMANDCOUNT
  




## Description


* The function returns the number of arguments passed from the command line to a program when it's executed.
* Arguments are spaced as separate numerical or text values. Spaced text inside of quotes is considered as one argument.
* In C, this function would generally be regarded as 'argc' when the main program is defined as the following: **int main(int argc, char \*argv[])**


  




## Examples


*Example:* The code below gets the number of parameters passed to our program from the command line with \_COMMANDCOUNT:





| ``` limit = _COMMANDCOUNT [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") limit     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [COMMAND$](/qb64wiki/index.php/COMMAND$ "COMMAND$")(i) [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |


*Explanation:* If we start *ThisProgram.exe* from the command window with **ThisProgram -l "loadfile.txt" -s "savefile.txt"**, the \_COMMANDCOUNT would be 4, "-l", "loadfile.txt", "-s", "savefile.txt" command arguments passed to the program, which we could then read separately with COMMAND$(n).
  




## See also


* [COMMAND$](/qb64wiki/index.php/COMMAND$ "COMMAND$")
* [SHELL](/qb64wiki/index.php/SHELL "SHELL")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=COMMANDCOUNT&oldid=8287>"




## Navigation menu








### Search





















