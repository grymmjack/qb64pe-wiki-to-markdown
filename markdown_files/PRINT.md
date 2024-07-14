


PRINT - QB64 Phoenix Edition Wiki








# PRINT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The PRINT statement prints numeric or string expressions to the program screen. Typing shortcut **?** will convert to PRINT.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 See also](#See_also) |
| --- |


## Syntax


**PRINT** [*expression*] [{;|,}] [*expression*...]
  




## Parameters


* *expression* is a numeric or string expression or list of expressions to be written to the screen. End quotes will not be displayed in strings.
* The print statement can be followed by a [semicolon](/qb64wiki/index.php/Semicolon "Semicolon") to stop the print cursor or a [comma](/qb64wiki/index.php/Comma "Comma") to tab space the next print.


  

*Usage:*



* [STRING](/qb64wiki/index.php/STRING "STRING") values will eliminate leading and trailing quotation marks when printed to the screen. Use [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) to add quotes to the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN").
* PRINT with no parameters moves the print cursor to the next print row at column 1.
* *expression* is a numeric or string expression to be printed.
	+ [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(*n%*) or [SPC](/qb64wiki/index.php/SPC "SPC")(*n%*) - specifies that *n%* space characters will be printed.
	+ [TAB](/qb64wiki/index.php/TAB "TAB")(*column%*) - specifies that the print cursor is to move to column number *column%*. If the print cursor is already beyond that column, it is moved to the designated column on the next row.
* A *separator* is used to separate multiple expressions and specifies how the print cursor is to be moved:
	+ [Semicolon](/qb64wiki/index.php/Semicolon "Semicolon")(;) - specifies that the print cursor stops at the end of the printed *expression* and may append later *expressions* or prints. PRINT ; or PRINT ""; will stop cursor movement and append later prints. Ending [semicolons](/qb64wiki/index.php/Semicolon "Semicolon") can also stop screen roll.
	+ [Comma](/qb64wiki/index.php/Comma "Comma")(,) - specifies that the print cursor is to move to the next 14-column tab-stop. If the print cursor is at column 56 or greater, it is moved to the next row at column 1. When used after an *expression* it may Tab-stop append later prints.
	+ [Plus](/qb64wiki/index.php/%2B "+")(+) uses [concatenation](/qb64wiki/index.php/Concatenation "Concatenation") to add [STRING](/qb64wiki/index.php/STRING "STRING") expressions ONLY with no spacing. **Cannot combine numerical *expression*s!**
	+ If a *separator* is not used at the end of the expression list, the print cursor moves to the next row at column 1.
* When **printing numerical** *expressions* values, the following rules are used:
	+ If the value is positive, the number is prefixed with a space character, otherwise, the number is prefixed with a negative sign (-).
	+ If the value is an integer (whole number), no decimal point or fractional part will be printed.
	+ If the value is not an [integer](/qb64wiki/index.php/INTEGER "INTEGER")(whole number) and has zero for a coefficient, no leading zero is printed. EX: -0.123 prints "-.123 "
	+ If the expression is in [scientific notation](/qb64wiki/index.php/Scientific_notation "Scientific notation"), the number is also printed in scientific notation.
	+ The number is printed with a space after it unless [STR$](/qb64wiki/index.php/STR$ "STR$")(number) is used to convert it to string text.
	+ Numerical values MUST be added to a PRINT statement string using [commas](/qb64wiki/index.php/Comma "Comma") or [semicolons](/qb64wiki/index.php/Semicolon "Semicolon") on each side of the value or by using [STR$](/qb64wiki/index.php/STR$ "STR$") to convert the value to a string to use [concatenation](/qb64wiki/index.php/Concatenation "Concatenation") (+ string addition).
* [VIEW PRINT](/qb64wiki/index.php/VIEW_PRINT "VIEW PRINT") can set up a viewport area for PRINTs. Text printed on the bottom view port row will scroll the text upward.
* Text to be printed can be a [STRING](/qb64wiki/index.php/STRING "STRING") variable or a literal value inside of quotation marks.
* Use [semicolon](/qb64wiki/index.php/Semicolon "Semicolon") ends on bottom 2 rows of the SCREEN mode used or the PRINT will roll the screen up.
* **Quotes cannot be inside of a literal STRING! Use [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) [concatenation](/qb64wiki/index.php/Concatenation "Concatenation") to insert [quotation marks](/qb64wiki/index.php/Quotation_mark "Quotation mark") into a literal string.**
* To better format number and text data placement use [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING").
* Instead of typing PRINT you can just type a [question mark](/qb64wiki/index.php/Question_mark "Question mark") (?). It will change to PRINT when enter is pressed in the IDE.
* Use the [\_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE") statement before a print to deal with the text background in **QB64**:


* **1** \_KEEPBACKGROUND: Text background transparent. Only the text is displayed over anything behind it.
* **2** \_ONLYBACKGROUND: Text background is only displayed. Text is transparent to anything behind it.
* **3** \_FILLBACKGROUND: Text and background block anything behind them. Default setting.
* Use the [\_PRINTMODE (function)](/qb64wiki/index.php/PRINTMODE_(function) "PRINTMODE (function)") to find the current \_PRINTMODE setting number.

* [WRITE](/qb64wiki/index.php/WRITE "WRITE") can be used to print a list of comma separated data values to the screen with [commas](/qb64wiki/index.php/Comma "Comma") between each value.
* Use [\_DEST](/qb64wiki/index.php/DEST "DEST") [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") before PRINT statements to be used in a [console](/qb64wiki/index.php/$CONSOLE "$CONSOLE") window.
* Use [\_CONTROLCHR](/qb64wiki/index.php/CONTROLCHR "CONTROLCHR") **OFF** to PRINT the unprintable lower [ASCII](/qb64wiki/index.php/ASCII "ASCII") control characters in QB64.


  

*Example 1:* Using semicolons, comma tabs or concatenation to insert [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters and numbers in a PRINT:





| ``` PRINT CHR$(34); "Hello world!"; CHR$(34) ' adding quotation marks PRINT 123 'demonstrates the positive leading space a$ = "Hello country!": a = 321: b = -321 PRINT a$, a ' demonstrates comma in statement PRINT a$; a ' demonstrates semicolon in statement PRINT a$ + [STR$](/qb64wiki/index.php/STR$ "STR$")(b) ' concatenation of string numerical values only ? "Hello city!" ' a ? changes to PRINT after moving cursor from the code line in IDE  ``` |
| --- |




| ``` "Hello world!"  123 Hello country!      321 Hello country! 321 Hello country!-321 Hello city!  ``` |
| --- |


First PRINT prints the text between two quotation marks, then it prints the value 123, notice that there are no quotation marks when printing the value, quotation marks mean that it will be treated like a literal string of text. a$ is set to "Hello country" and 'a' is set to the value 321, the dollar sign is used when a variable holds the text string. The contents of a$ is then printed and the "," means that the value of 'a' is printed separated by a tab and ";" means that there is no separation from the other text except for the leading positive value space.
  

*Example 2:* Changing colors in a line of text using semicolons with colon separators between PRINTs on the same code line.





| ``` [COLOR](/qb64wiki/index.php/COLOR "COLOR") 12: PRINT "Start red "; : [COLOR](/qb64wiki/index.php/COLOR "COLOR") 10: PRINT "and end green." [COLOR](/qb64wiki/index.php/COLOR "COLOR") 11: PRINT "Start aqua "; [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: PRINT "and end blue."  ``` |
| --- |




| ``` Start red and end green. Start aqua and end blue.  ``` |
| --- |


  




## See also


* [\_PRINTMODE](/qb64wiki/index.php/PRINTMODE "PRINTMODE"), [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING"), [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING")
* [SPC](/qb64wiki/index.php/SPC "SPC"), [TAB](/qb64wiki/index.php/TAB "TAB"), [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$"), [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")
* [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN"), [POS](/qb64wiki/index.php/POS "POS"), [SCREEN (function)](/qb64wiki/index.php/SCREEN_(function) "SCREEN (function)")
* [COLOR](/qb64wiki/index.php/COLOR "COLOR"), [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE"), [VIEW PRINT](/qb64wiki/index.php/VIEW_PRINT "VIEW PRINT")
* [INPUT](/qb64wiki/index.php/INPUT "INPUT"), [STR$](/qb64wiki/index.php/STR$ "STR$"), [CHR$](/qb64wiki/index.php/CHR$ "CHR$")
* [ASCII](/qb64wiki/index.php/ASCII "ASCII"), [\_CONTROLCHR](/qb64wiki/index.php/CONTROLCHR "CONTROLCHR")
* [Text Using Graphics](/qb64wiki/index.php/Text_Using_Graphics "Text Using Graphics")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PRINT&oldid=8853>"




## Navigation menu








### Search





















