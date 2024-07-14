


RANDOMIZE - QB64 Phoenix Edition Wiki








# RANDOMIZE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**RANDOMIZE** is used with a seed value to generate different random number sequences using the [RND](/qb64wiki/index.php/RND "RND") function.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


**RANDOMIZE** [USING] **{*seednumber*|TIMER}**
  




* The *seed number* can be ANY positive or negative numerical type value. The [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") value is often used to change [RND](/qb64wiki/index.php/RND "RND") output each run.
* If the *seed number* is omitted, the program will display: **Random-number seed (-32768 to 32767)?** request on screen.
* **USING** resets a *seed number* sequence to the start of the sequence as if the program just started using that seed in **QB64 only**.
* **Note:** The RANDOMIZE USING *seed number* MUST be designated or a Name already in use status error will occur!
* If the same initial seed number is used, the sequence of random numbers returned will be identical every program run.
* The fact that random numbers would always be the same has been used for simple data encryption and decryption.
* Using a [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") starting value ensures that the initial return sequence values are different almost every time the program is run!
* [RUN](/qb64wiki/index.php/RUN "RUN") should reset the RANDOMIZE sequence to the starting [RND](/qb64wiki/index.php/RND "RND") function value.(Not yet in QB64)


  

*Example 1:* Using RANDOMIZE **TIMER** to set a different starting sequence of [random](/qb64wiki/index.php/RND "RND") numbers every run.





| ``` RANDOMIZE [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP") randnum% = INT([RND](/qb64wiki/index.php/RND "RND") * 11) + 2  'add one to multiplier as INT rounds down and never equals 10 PRINT randnum% K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(K$) = "Q"  'q = quit [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Explanation:* Procedure generates random integer values from 2 to 12 like a pair of dice.
  

*Example 2:* Repeating a random number sequence with RANDOMIZE **USING** and a specific seed value in **QB64** only.





| ``` seed = 10 RANDOMIZE seed Print7 RANDOMIZE seed Print7 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press a key to start sequence over!" K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) RANDOMIZE **USING** seed Print7  [SUB](/qb64wiki/index.php/SUB "SUB") Print7 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") r = 1 TO 7   [PRINT](/qb64wiki/index.php/PRINT "PRINT") [RND](/qb64wiki/index.php/RND "RND"); [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


*Explanation:* The second RANDOMIZE statement just continues the sequence where USING in the third restarts the sequence.
  

*Example 3:* Random fireworks explosions:





| ``` RANDOMIZE [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT") A-Z  [TYPE](/qb64wiki/index.php/TYPE "TYPE") ftype     vx [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")     vy [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") [END](/qb64wiki/index.php/END "END") [TYPE](/qb64wiki/index.php/TYPE "TYPE") [DIM](/qb64wiki/index.php/DIM "DIM") frag(500) [AS](/qb64wiki/index.php/AS "AS") ftype 'fragments  [DIM](/qb64wiki/index.php/DIM "DIM") pi [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") pi = 3.141593  [DIM](/qb64wiki/index.php/DIM "DIM") x [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), y [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") [DIM](/qb64wiki/index.php/DIM "DIM") t [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), g [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), p [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") t = 0 g = 0.4 'gravity p = 15 'explosion power  sw = 800 sh = 600  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(sw, sh, 32)  DO     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")(frag)         frag(i).vx = [RND](/qb64wiki/index.php/RND "RND") * [COS](/qb64wiki/index.php/COS "COS")(2 * pi * [RND](/qb64wiki/index.php/RND "RND"))         frag(i).vy = [RND](/qb64wiki/index.php/RND "RND") * [SIN](/qb64wiki/index.php/SIN "SIN")(2 * pi * [RND](/qb64wiki/index.php/RND "RND"))     [NEXT](/qb64wiki/index.php/NEXT "NEXT")      x = sw * [RND](/qb64wiki/index.php/RND "RND")     y = sh * [RND](/qb64wiki/index.php/RND "RND")      [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") t = 0 [TO](/qb64wiki/index.php/TO "TO") 25 [STEP](/qb64wiki/index.php/STEP "STEP") 0.1         [LINE](/qb64wiki/index.php/LINE "LINE") (0, 0)-(sw, sh), [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 0, 0), BF         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")(frag)             [PSET](/qb64wiki/index.php/PSET "PSET") (x + t * p * frag(i).vx, y + t * p * frag(i).vy + g * t * t), [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 0)         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")         [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 150          [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") = -27 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")  ``` |
| --- |


Code by Ben
  




## See also


* [RND](/qb64wiki/index.php/RND "RND"), [INT](/qb64wiki/index.php/INT "INT"), [CINT](/qb64wiki/index.php/CINT "CINT")
* [TIMER (function)](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RANDOMIZE&oldid=8060>"




## Navigation menu








### Search





















