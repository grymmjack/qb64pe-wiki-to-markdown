


COMMAND$ - QB64 Phoenix Edition Wiki








# COMMAND$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **COMMAND$** function returns the command line argument(s) passed when a program is run.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*commandLine$* = COMMAND$[(count%)]
  




## Description


* The [STRING](/qb64wiki/index.php/STRING "STRING") return value is anything typed after a program's executable file name in command line (or using the [RUN](/qb64wiki/index.php/RUN "RUN") statement).
* Unlike QuickBASIC, **QB64** does not return all [uppercase](/qb64wiki/index.php/UCASE$ "UCASE$") values so keep that in mind when checking parameters.
* In **QB64**, COMMAND$ works as an array to return specific elements passed to the command line. COMMAND$(2) would return the second parameter passed at the command line. Arguments can contain spaces if they are passed inside quotation marks. This can be used to properly retrieve file names and arguments which contain spaces.
* Use the [\_COMMANDCOUNT](/qb64wiki/index.php/COMMANDCOUNT "COMMANDCOUNT") function to find the number of parameters passed to a program via the command line. See *Example 2* below.


  




## Examples


*Example 1:* Compile both programs. ProgramA [RUNs](/qb64wiki/index.php/RUN "RUN") ProgramB with a parameter passed following the filename:





| ``` [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 12, 36: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ProgramA"  [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 23, 25: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press any key to run ProgramB" K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) [RUN](/qb64wiki/index.php/RUN "RUN") "ProgramB FS"  'pass FS parameter to ProgramB in QB64 or QB4.5  [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")  ``` |
| --- |


*ProgramB* checks for fullscreen parameter pass in QB64 and goes full screen.


| ``` [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 17, 36: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ProgramB" parameter$ = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(COMMAND$) 'UCASE$ is needed in QB64 only, as QB4.5 will always return upper case [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 33: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Parameter = " + parameter$ [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")(parameter$, 2) = "FS" [THEN](/qb64wiki/index.php/THEN "THEN") [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN") 'parameter changes to full screen  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ```                                     ProgramB                                     Parameter = FS.EXE  ``` |
| --- |


  

*Example 2:* Program gets the number of parameters passed to the program, and then prints those parameters to the screen one at a time.





| ``` count = [_COMMANDCOUNT](/qb64wiki/index.php/COMMANDCOUNT "COMMANDCOUNT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") c = 1 [TO](/qb64wiki/index.php/TO "TO") count     [PRINT](/qb64wiki/index.php/PRINT "PRINT") COMMAND$(c) 'or process commands sent [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |




| ``` -1 a data file  ``` |
| --- |


*Explanation: If we start* ThisProgram.exe *with the command line **ThisProgram -l "a data file"**, COMMAND$ will return a single string of "-1 a data file" which might be hard to process and interpret properly, but COMMAND$(1) would return "-l" and COMMAND$(2) would return the quoted "a data file" option as separate entries for easier parsing and processing.*
  

*Example 3:* As part of the command array syntax, you can also just read the array to see how many commands were sent (or simply check [\_COMMANDCOUNT](/qb64wiki/index.php/COMMANDCOUNT "COMMANDCOUNT")):





| ``` DO     count = count + 1     cmd$ = COMMAND$(count)     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") cmd$ = "" [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO") 'read until an empty return     [PRINT](/qb64wiki/index.php/PRINT "PRINT") cmd$ 'or process commands sent [LOOP](/qb64wiki/index.php/LOOP "LOOP") count = count - 1 'save the number of parameters sent to this program when run  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1271)
* [SHELL](/qb64wiki/index.php/SHELL "SHELL"), [RUN](/qb64wiki/index.php/RUN "RUN")
* [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$"), [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$")
* [\_COMMANDCOUNT](/qb64wiki/index.php/COMMANDCOUNT "COMMANDCOUNT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=COMMAND$&oldid=8921>"




## Navigation menu








### Search





















