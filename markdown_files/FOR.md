


FOR - QB64 Phoenix Edition Wiki








# FOR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The FOR statement creates a counter loop using specified start and stop numerical boundaries. The default increment is + 1.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


FOR *counterVariable* = *startValue* [TO](/qb64wiki/index.php/TO "TO") *stopValue* [[[STEP *increment*]
*{code}*
⋮
[NEXT](/qb64wiki/index.php/NEXT "NEXT") [*counterVariable*]
  




## Parameters


* The FOR *counterVariable* name is required to define the counter span and may also be used after the NEXT keyword.
* The *startValue* [TO](/qb64wiki/index.php/TO "TO") *stopValue* can be any literal or variable numerical type. Both values are required.
* [STEP](/qb64wiki/index.php/STEP "STEP") can be used for a loop *increment* other than the default *plus 1 and can be any positive or negative literal or variable numerical value as long as the STEP value corresponds to the loop's* startValue *and* stopValue*.*
* [NEXT](/qb64wiki/index.php/NEXT "NEXT") ends the FOR loop code block and increments the counter to the next value even when it exceeds the stop limit.


  




## Description


* [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") counter loops must be within the proper start, stop and increment values or the entire loop code block will not be executed.
* Avoid changing the FOR *counterVariable'*s value inside of the loop. This obfuscates code and is a poor programming practice.
* Once the loop has been started, changing the variables holding the *startValue*, *stopValue* or *increment* value will not affect loop execution.
* **If the [STEP](/qb64wiki/index.php/STEP "STEP") *increment* value does not match the *startValue* [TO](/qb64wiki/index.php/TO "TO") *stopValue* the FOR loop block will be ignored.**
	+ If *startValue* is less than *stopValue*, use the default increment or positive [STEP](/qb64wiki/index.php/STEP "STEP") value or the loop will not be executed.
	+ If *startValue* is more than *stopValue*, use a negative [STEP](/qb64wiki/index.php/STEP "STEP") interval or the loop will not be executed.
	+ The [STEP](/qb64wiki/index.php/STEP "STEP") *increment* value cannot be changed inside of the loop.
* Use **[EXIT](/qb64wiki/index.php/EXIT "EXIT") FOR** to leave a FOR loop early when a certain condition is met inside of the loop.
* The [NEXT](/qb64wiki/index.php/NEXT "NEXT") counter variable name is not required. NEXT loop increments can be separated by colons in nested FOR loops.
* **NOTE: When the FOR loop is exited after the *stopValue* is reached, the *counterVariable****s value will be* stopValue *+ 1 (or* stopValue *+* increment*)*
* **Beware of FOR loop counts that exceed the *counterVariable* type limits and may repeat without error in QB64.**
	+ For example, if *counterVariable* is of type [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") and the stop limit exceeds 32767, the *counterVariable* will reset back to -32768 and loop endlessly.


  




## Examples


*Example 1:* Adding all of the even numbers from 10 to 0.





| ``` FOR i = 10 TO 0 [STEP](/qb64wiki/index.php/STEP "STEP") -2   totaleven% = i + totaleven%   PRINT totaleven%; NEXT PRINT "After loop, i ="; i  ``` |
| --- |




| ``` 10 18 24 28 30 30 After loop, i = -2  ``` |
| --- |


*Explanation:* The loop counts down from 10 to every even value below it. The counter keeps stepping down until the FOR stop limit is reached or exceeded. Note that the value of i is -2 after the loop is exited. [NEXT](/qb64wiki/index.php/NEXT "NEXT") always increments the counter one last time.
  

*Example 2:* How an entire FOR loop block is ignored when the start and stop limits do not match the default or [STEP](/qb64wiki/index.php/STEP "STEP") increment.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "hi"  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 10 [TO](/qb64wiki/index.php/TO "TO") 1 'requires a negative [STEP](/qb64wiki/index.php/STEP "STEP") value   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "lo" [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "bye"  ``` |
| --- |




| ``` hi bye  ``` |
| --- |


  




## See also


* [STEP](/qb64wiki/index.php/STEP "STEP")
* [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP"), [WHILE...WEND](/qb64wiki/index.php/WHILE...WEND "WHILE...WEND")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FOR&oldid=7289>"




## Navigation menu








### Search





















