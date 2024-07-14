


RND - QB64 Phoenix Edition Wiki








# RND



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **RND** function returns a random number with a value between 0 (inclusive) and 1 (exclusive).


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


result! = RND [(*n*)]
  




## Parameters


* *n* is a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") numeric value that defines the behavior of the RND function but is **NOT normally required**:


n parameter omitted: Returns next random number in the sequence.
n = 0: Return the last value returned.
n < 0: Always returns the same value for any given n
n > 0: the sequence of numbers generated will not change unless [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") is initiated.
  




## Description


* The random numbers generated range from 0 minimum to .9999999 maximum [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") values that never equal 1.
* To get values in a range larger than 1, multiply RND with a number to get returns up to but not including that numerical value.
* To get values starting at a certain number, add that number to the RND result as RND minimums can be 0.
* If you need an integer range of numbers, like a dice roll, round it down to an [INT](/qb64wiki/index.php/INT "INT"). Add 1 to the maximum number with [INT](/qb64wiki/index.php/INT "INT").
* The random sequence is 2 ^ 24 or 16,777,216 entries long, which can allow repeated patterns in some procedures.
* Formulas for the [Integer](/qb64wiki/index.php/INT "INT") or [Closest Integer](/qb64wiki/index.php/CINT "CINT") of ANY number range from *min%*(lowest value) to *max%*(greatest value):


* Using [INT](/qb64wiki/index.php/INT "INT"): randNum% = INT(RND \* (max% - min% + 1)) + min%
* Using [CINT](/qb64wiki/index.php/CINT "CINT"): randNum% = CINT(RND \* (max% - min%)) + min%

* Use [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") for different random number results each time a program is run.
* [RUN](/qb64wiki/index.php/RUN "RUN") should reset the [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") sequence to the starting RND function value.(Not yet in QB64)


  

*Example 1:* Generating a random integer value between 1 and 6 (inclusive) using INT.





| ``` dice% = [INT](/qb64wiki/index.php/INT "INT")(RND * 6) + 1 'add one as INT value never reaches 6  ``` |
| --- |


  

*Example 2:* Using uniform random numbers to create random numbers with a gaussian distribution ([Marsaglia's polar method](https://en.wikipedia.org/wiki/Marsaglia_polar_method "wikipedia:Marsaglia polar method")).





| ``` [DO](/qb64wiki/index.php/DO "DO")   u! = RND * 2 - 1   v! = RND * 2 - 1   s! = u! * u! + v! * v! [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") s! >= 1 [OR](/qb64wiki/index.php/OR "OR") s! = 0 s! = SQR(-2 * [LOG](/qb64wiki/index.php/LOG "LOG")(s!) / s!) * 0.5 u! = u! * s! v! = v! * s!  ``` |
| --- |


*Explanation:* Values *u!* and *v!* are now two independent random numbers with gaussian distribution, centered at 0.
  

*Example 3:* Random flashes from an explosion





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") BC = 120 ' BALL COUNT [DIM](/qb64wiki/index.php/DIM "DIM") ballx(1 [TO](/qb64wiki/index.php/TO "TO") BC) [DIM](/qb64wiki/index.php/DIM "DIM") bally(1 [TO](/qb64wiki/index.php/TO "TO") BC) [DIM](/qb64wiki/index.php/DIM "DIM") velx(1 [TO](/qb64wiki/index.php/TO "TO") BC) [DIM](/qb64wiki/index.php/DIM "DIM") vely(1 [TO](/qb64wiki/index.php/TO "TO") BC) [DIM](/qb64wiki/index.php/DIM "DIM") bsize(1 [TO](/qb64wiki/index.php/TO "TO") BC) Y = [INT](/qb64wiki/index.php/INT "INT")(RND * (400 - 100 + 1)) + 100 X0 = 325 Y0 = 300 Tmax = 150 DO     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") p = 1 [TO](/qb64wiki/index.php/TO "TO") BC         T = [INT](/qb64wiki/index.php/INT "INT")(RND * (Tmax - 50 + 1)) + 50         X = [INT](/qb64wiki/index.php/INT "INT")(RND * (1000 + 500 + 1)) - 500         velx(p) = (X - X0) / T '                       calculate velocity based on flight time         vely(p) = -1 * (Y - .05 * (T ^ 2 + 20 * Y0)) / (T) ' verticle velocity     [NEXT](/qb64wiki/index.php/NEXT "NEXT") p      [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") w = 1 [TO](/qb64wiki/index.php/TO "TO") BC         bsize(w) = [INT](/qb64wiki/index.php/INT "INT")(RND * (10 - 0 + 1)) + 0 'size     [NEXT](/qb64wiki/index.php/NEXT "NEXT") w      [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") J = 1 [TO](/qb64wiki/index.php/TO "TO") Tmax         [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60         [CLS](/qb64wiki/index.php/CLS "CLS")         '[FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 255 [STEP](/qb64wiki/index.php/STEP "STEP") .5         '[CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (X0, Y0), i, [_RGB](/qb64wiki/index.php/RGB "RGB")(255 - i, 0, 0), 0, 3.147         ' [NEXT](/qb64wiki/index.php/NEXT "NEXT") i          R = [INT](/qb64wiki/index.php/INT "INT")(RND * (25 - 20 + 1)) + 20 'random glimmer         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") z = 1 [TO](/qb64wiki/index.php/TO "TO") BC             ballx(z) = X0 + velx(z) * J             bally(z) = Y0 - vely(z) * J + .5 * .1 * J ^ 2         [NEXT](/qb64wiki/index.php/NEXT "NEXT") z          [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") d = 1 [TO](/qb64wiki/index.php/TO "TO") BC             RCOL = [INT](/qb64wiki/index.php/INT "INT")(RND * (255 - 0 + 1)) 'color             [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") bsize(d) + 1 [STEP](/qb64wiki/index.php/STEP "STEP") .4 'draw balls                 [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (ballx(d), bally(d)), i, [_RGBA](/qb64wiki/index.php/RGBA "RGBA")(255, RCOL - (R * i), RCOL - R * i, 255)             [NEXT](/qb64wiki/index.php/NEXT "NEXT") i         [NEXT](/qb64wiki/index.php/NEXT "NEXT") d          [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")      [NEXT](/qb64wiki/index.php/NEXT "NEXT") J  [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  ``` |
| --- |


Code by Falcon
  




## See also


* [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE"), [TIMER (function)](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")
* [INT](/qb64wiki/index.php/INT "INT"), [CINT](/qb64wiki/index.php/CINT "CINT"), [FIX](/qb64wiki/index.php/FIX "FIX")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RND&oldid=8993>"




## Navigation menu








### Search





















