


INPUT - QB64 Phoenix Edition Wiki








# INPUT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The INPUT statement requests a [STRING](/qb64wiki/index.php/STRING "STRING") or numerical keyboard entry from the user.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


INPUT [;] "[Question or statement text]"{,|;} *variable*[, ...]
INPUT ; *variable*[, ...]
  




## Parameters


* A [semicolon](/qb64wiki/index.php/Semicolon "Semicolon") after the INPUT keyword keeps the entry on the same row after enter is pressed and prevents the screen contents from rolling up.
* The optional prompt "Question or statement text" must be a literal predefined [string](/qb64wiki/index.php/STRING "STRING"). **The prompt cannot use a variable.**
* [Quotation marks](/qb64wiki/index.php/Quotation_mark "Quotation mark") are required except when a semicolon follows INPUT. A question mark will appear before the cursor.
* A [semicolon](/qb64wiki/index.php/Semicolon "Semicolon") immediately after the text statement will display a question mark with a space after it. Use a [comma](/qb64wiki/index.php/Comma "Comma") for input statements.


  




## Description


* **QB64** does not return *Redo from start* errors like QBasic did, as user input is limited to the scope of the variable [type](/qb64wiki/index.php/Data_types "Data types") used.
* Text entries (with a [STRING](/qb64wiki/index.php/STRING "STRING") variable can receive any characters, including numerical. **QB64 will ignore commas in single variable text entries.**
* The [type](/qb64wiki/index.php/Data_types "Data types") of the *variable* used to store user input determines the valid numerical range for value entries in QB64, with non-numerical characters limited to D, E, [&H](/qb64wiki/index.php/%26H "&H"), [&O](/qb64wiki/index.php/%26O "&O") or [&B](/qb64wiki/index.php/%26B "&B").
	+ For example, if you use an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") variable, as in INPUT "Initial value: ", myValue%, the valid range is -32768 to 32767.
	+ [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), and [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") entries will ignore decimal points entered and will use all numbers.
* INPUT can be used to get more than one *variable* value from the user. Do so by separating input variables with commas in the code.
	+ The program must inform the user that more than one variable is requested, in order to enter each value separated with a comma at runtime.
	+ [String](/qb64wiki/index.php/STRING "STRING") and numerical variables can both be used in multiple entry requests separated by commas.
	+ **QB64** allows comma separated entries to be skipped by the user without generating an error.
* **Use [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") for text input entries that may contain commas such as address or name entries.**
* The user must press enter for the INPUT procedure to end.
* INPUT accepts the [scientific notation](/qb64wiki/index.php/Scientific_notation "Scientific notation") letters D or E in [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") or [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") numerical values.
* Numerical values starting with [&H](/qb64wiki/index.php/%26H "&H"), [&O](/qb64wiki/index.php/%26O "&O") and [&B](/qb64wiki/index.php/%26B "&B") can also be entered.
* The statement halts a program until enter is pressed, which may not be desired in programs using mouse input (see [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") loops).
* Use [\_DEST](/qb64wiki/index.php/DEST "DEST") [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") before INPUT statements to receive input from a [console](/qb64wiki/index.php/$CONSOLE "$CONSOLE") window.


  




## Examples


*Example 1:* Using a variable in an input text message using PRINT. INPUT prompts cannot use variables.





| ``` INPUT "Enter your name: ", name$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") name$ + " please enter your age: ";: INPUT "", age% 'empty string with comma [PRINT](/qb64wiki/index.php/PRINT "PRINT") name$ + " how much do you weigh"; : INPUT weight%   'no text adds ?  ``` |
| --- |


*Explanation:* Use an empty string with a comma to eliminate the question mark that would appear without the string.
  

*Example 2:* How QB64 avoids a *Redo from start* multiple entry error. Use commas between values.





| ``` [DO](/qb64wiki/index.php/DO "DO")   INPUT "What is your name, age, and sex(M/F)"; name$, age%, sex$ [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") age%        'loop until age is not 0 [IF](/qb64wiki/index.php/IF "IF") age% >= 21 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "You can drink beer!" [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "You cannot drink beer yet!" [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ``` What is your name, age, and sex(M/F)? Tom,24,M You can drink beer!  ``` |
| --- |


*Explanation:* Try to enter text for the age value and it will not work. E or D should be allowed as decimal point numerical entries.
  

*Example 3:* Preventing screen roll after an input entry on the bottom 2 screen rows.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 29, 2 '          place cursor at beginning of prompt line [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Enter a name to search for... "; 'print prompt on screen with input to follow [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15: INPUT ; "", name$ '       get search name from user [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 29, 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [SPC](/qb64wiki/index.php/SPC "SPC")(78); '       erase previous prompt n$ = [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(name$) '                 convert search name to upper case [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14'                        change foreground color to yellow [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 29, 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Searching..."; 'print message [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")  ``` |
| --- |




| ``` Enter a name to search for... █  ``` |
| --- |


*Explanation:* The red [semicolon](/qb64wiki/index.php/Semicolon "Semicolon") after INPUT acts like a semicolon after a [PRINT](/qb64wiki/index.php/PRINT "PRINT"), which keeps the print cursor on the same row.
  




## See also


* [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$"), [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")
* [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT"), [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE")
* [INPUT #](/qb64wiki/index.php/INPUT_(file_statement) "INPUT (file statement)"), [LINE INPUT #](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") (file input)
* [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT"), [\_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN")
* [Scancodes](/qb64wiki/index.php/Scancodes "Scancodes")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INPUT&oldid=7886>"




## Navigation menu








### Search





















