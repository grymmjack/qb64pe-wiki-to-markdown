


\_ALLOWFULLSCREEN - QB64 Phoenix Edition Wiki








# \_ALLOWFULLSCREEN



From QB64 Phoenix Edition Wiki
(Redirected from [ALL](/qb64wiki/index.php?title=ALL&redirect=no "ALL"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ALLOWFULLSCREEN statement allows setting the behavior of the ALT+ENTER combo.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_ALLOWFULLSCREEN [{\_STRETCH|\_SQUAREPIXELS|OFF|\_ALL}][, {\_SMOOTH|OFF|\_ALL}]
  




## Description


* Calling the statement with no parameters enables all four possible full screen modes (and is the default state when a program is started): both [\_STRETCH](/qb64wiki/index.php/STRETCH "STRETCH") ([\_SMOOTH](/qb64wiki/index.php/SMOOTH "SMOOTH") and [\_OFF](/qb64wiki/index.php/OFF "OFF")) and [\_SQUAREPIXELS](/qb64wiki/index.php/SQUAREPIXELS "SQUAREPIXELS") ([\_SMOOTH](/qb64wiki/index.php/SMOOTH "SMOOTH") and [\_OFF](/qb64wiki/index.php/OFF "OFF")).
	+ Using \_ALLOWFULLSCREEN [\_ALL](/qb64wiki/index.php/ALL "ALL"), [\_ALL](/qb64wiki/index.php/ALL "ALL") has the same effect.
* \_ALLOWFULLSCREEN only affects the behavior of ALT+ENTER. The [\_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN") statement is not bound by \_ALLOWFULLSCREEN's settings so all modes can be accessed programmatically.
* To limit just the mode but allow both \_SMOOTH + \_OFF antialiasing modes, pass just the first parameter: *Example:* \_ALLOWFULLSCREEN \_SQUAREPIXELS
* To allow multiple modes with \_SMOOTH or \_OFF as default, pass just the second parameter. *Example:* \_ALLOWFULLSCREEN , \_SMOOTH
* Any possible permutation of the parameters is allowed.
* With \_ALLOWFULLSCREEN \_OFF you can trap Alt+Enter manually in your program and reassign it. See example 2 below.


  




## Availability


* **Version 1.3 and up**.


  




## Examples


*Example 1:* Allowing only one fullscreen mode with square pixels and no antialiasing:





| ``` _ALLOWFULLSCREEN [_SQUAREPIXELS](/qb64wiki/index.php/SQUAREPIXELS "SQUAREPIXELS") , [OFF](/qb64wiki/index.php/OFF "OFF")  ``` |
| --- |




---


*Example 2:* Disabling \_FULLSCREEN with Alt+ENTER so the combo can be manually trapped:





| ``` [DO](/qb64wiki/index.php/DO "DO")     [CLS](/qb64wiki/index.php/CLS "CLS")      [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 7     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "    - Press ALT+ENTER to test trapping the combo..."     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "    _ Press SPACEBAR to allow fullscreen again..."      k& = [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT")      [IF](/qb64wiki/index.php/IF "IF") k& = 13 [THEN](/qb64wiki/index.php/THEN "THEN")         [IF](/qb64wiki/index.php/IF "IF") [_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN")(100307) [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") [_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN")(100308) [THEN](/qb64wiki/index.php/THEN "THEN")             altEnter = altEnter + 1         [END IF](/qb64wiki/index.php/END_IF "END IF")     [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") k& = 32 [THEN](/qb64wiki/index.php/THEN "THEN")         fullscreenEnabled = [NOT](/qb64wiki/index.php/NOT "NOT") fullscreenEnabled     [END IF](/qb64wiki/index.php/END_IF "END IF")      [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 14     [IF](/qb64wiki/index.php/IF "IF") fullscreenEnabled [THEN](/qb64wiki/index.php/THEN "THEN")         _ALLOWFULLSCREEN [_ALL](/qb64wiki/index.php/ALL "ALL") , [_ALL](/qb64wiki/index.php/ALL "ALL")         altEnter = 0         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_ALLOWFULLSCREEN _ALL, _ALL"          [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 18         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ALT+ENTER will trigger all four fullscreen modes now."     [ELSE](/qb64wiki/index.php/ELSE "ELSE")         _ALLOWFULLSCREEN [OFF](/qb64wiki/index.php/OFF "OFF")         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "_ALLOWFULLSCREEN OFF"     [END IF](/qb64wiki/index.php/END_IF "END IF")      [IF](/qb64wiki/index.php/IF "IF") altEnter [THEN](/qb64wiki/index.php/THEN "THEN")         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 18         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ALT+ENTER manually trapped"; altEnter; "times."     [END IF](/qb64wiki/index.php/END_IF "END IF")      [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30 [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


  




## See also


* [\_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN"), [\_SMOOTH (function)](/qb64wiki/index.php/SMOOTH_(function) "SMOOTH (function)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ALLOWFULLSCREEN&oldid=8255>"




## Navigation menu








### Search





















