


DO...LOOP - QB64 Phoenix Edition Wiki








# DO...LOOP



From QB64 Phoenix Edition Wiki
(Redirected from [DO](/qb64wiki/index.php?title=DO&redirect=no "DO"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**DO...LOOP** statements are used in programs to repeat code or return to the start of a procedure.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*Syntax 1:*



**[DO](/qb64wiki/index.php/DO "DO")** [{[WHILE](/qb64wiki/index.php/WHILE "WHILE")|[UNTIL](/qb64wiki/index.php/UNTIL "UNTIL")} condition]
*{code}*
⋮
**[LOOP](/qb64wiki/index.php/LOOP "LOOP")**
  

*Syntax 2:*



**[DO](/qb64wiki/index.php/DO "DO")**
*{code}*
⋮
**[LOOP](/qb64wiki/index.php/LOOP "LOOP")** [{[WHILE](/qb64wiki/index.php/WHILE "WHILE")|[UNTIL](/qb64wiki/index.php/UNTIL "UNTIL")} condition]
  




## Description


* **DO UNTIL or DO WHILE used with LOOP**: The condition is evaluated before running the loop code.


[UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") checks if the condition is false each time before running code.
[WHILE](/qb64wiki/index.php/WHILE "WHILE") checks if the condition is true each time before running code.
* **DO used with LOOP UNTIL or LOOP WHILE**: The code block will run at least once:


[UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") checks if the condition is false before running loop code again.
[WHILE](/qb64wiki/index.php/WHILE "WHILE") checks if the condition is true before running loop code again.
* NOTE: You cannot use a condition after both the DO and LOOP statements at the same time.
* Use **[EXIT](/qb64wiki/index.php/EXIT "EXIT") DO** to exit a loop block even before the condition is met.
	+ If you don't specify a condition, you must exit the loop block manually using **[EXIT](/qb64wiki/index.php/EXIT "EXIT") DO**.
* If a loop never meets an exit condition requirement, it will never stop.


  






| ```          Table 3: The relational operations for condition checking.   In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to compare. Both must represent  the same general type, i.e. they must result into either numerical values  or [STRING](/qb64wiki/index.php/STRING "STRING") values. If a test succeeds, then **true** (-1) is returned, **false** (0)      if it fails, which both can be used in further [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.  ┌─────────────────────────────────────────────────────────────────────────┐  │                          **[Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations")**                          │  ├────────────┬───────────────────────────────────────────┬────────────────┤  │ **Operation**  │                **Description**                │ **Example usage**  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [=](/qb64wiki/index.php/Equal "Equal") B    │ Tests if A is **equal** to B.                 │ [IF](/qb64wiki/index.php/IF "IF") A [=](/qb64wiki/index.php/Equal "Equal") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B   │ Tests if A is **not equal** to B.             │ [IF](/qb64wiki/index.php/IF "IF") A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<](/qb64wiki/index.php/Less_Than "Less Than") B    │ Tests if A is **less than** B.                │ [IF](/qb64wiki/index.php/IF "IF") A [<](/qb64wiki/index.php/Less_Than "Less Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B    │ Tests if A is **greater than** B.             │ [IF](/qb64wiki/index.php/IF "IF") A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B   │ Tests if A is **less than or equal** to B.    │ [IF](/qb64wiki/index.php/IF "IF") A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B   │ Tests if A is **greater than or equal** to B. │ [IF](/qb64wiki/index.php/IF "IF") A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  └────────────┴───────────────────────────────────────────┴────────────────┘    The operations should be very obvious for numerical values. For strings    be aware that all checks are done **case sensitive** (i.e. "Foo" <> "foo").    The **equal**/**not equal** check is pretty much straight forward, but for the    **less**/**greater** checks the [ASCII](/qb64wiki/index.php/ASCII "ASCII") value of the first different character is                           used for decision making:     **E.g.** "abc" is **less** than "abd", because in the first difference (the 3rd         character) the "c" has a lower [ASCII](/qb64wiki/index.php/ASCII "ASCII") value than the "d".     This behavior may give you some subtle results, if you are not aware of                    the [ASCII](/qb64wiki/index.php/ASCII "ASCII") values and the written case:     **E.g.** "abc" is **greater** than "abD", because the small letters have higher         [ASCII](/qb64wiki/index.php/ASCII "ASCII") values than the capital letters, hence "c" > "D". You may use         [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$") or [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$") to make sure both strings have the same case.  ``` |
| --- |


  




## Examples


*Example 1:* Using WHILE to clear the keyboard buffer.





| ```   DO WHILE [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "": LOOP ' checks evaluation before running loop code  DO: LOOP WHILE INKEY$ <> "" ' checks evaluation after one run of loop code   ``` |
| --- |


  

*Example 2:* Using UNTIL to clear the keyboard buffer.





| ```   DO UNTIL [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = "": LOOP ' checks evaluation before running loop code  DO: LOOP UNTIL [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = "" ' checks evaluation after one run of loop code   ``` |
| --- |


  

*Example 3:* Using a one time DO loop to exit ANY of several FOR LOOPs, without using [GOTO](/qb64wiki/index.php/GOTO "GOTO").



SUB reads header contents of a [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE") file that may include embedded RGB color settings before the image.


| ``` [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT") A-Z [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a BSAVE file name to read the file for screen mode:"', filenm$ CheckScreen filenm$  [END](/qb64wiki/index.php/END "END")  [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT") A-Z [SUB](/qb64wiki/index.php/SUB "SUB") CheckScreen (Filename$)        'find Screen mode (12 or 13) and image dimensions    DIM Bsv AS [STRING](/qb64wiki/index.php/STRING "STRING") * 1    DIM Header AS STRING * 6     Scr = 0: MaxColors = 0    [OPEN](/qb64wiki/index.php/OPEN "OPEN") Filename$ FOR [BINARY](/qb64wiki/index.php/BINARY "BINARY") AS #1     [GET](/qb64wiki/index.php/GET "GET") #1, , Bsv           '1 check for small 2 character    GET #1, , Header        '2 - 7 rest of file header     IF Bsv <> [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(253) THEN   ' small 2 character denotes a [BSAVE](/qb64wiki/index.php/BSAVE "BSAVE") file       COLOR 12: LOCATE 15, 33: PRINT "Not a BSAVE file!": SLEEP 3: [EXIT](/qb64wiki/index.php/EXIT "EXIT") SUB    END IF     GET #1, , widN           '8 no color info bmp sizes    GET #1, , depN           '9   "        "      "  DO   IF widN > 63 OR depN > 63 THEN [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")  ' width and depth already found    FOR i = 10 TO 55       'check for Screen 12 embedded colors     GET #1, , RGB     tot12& = tot12& + RGB     'PRINT i; RGB; : SOUND 300, 1         'test sound slows loop in QB     IF RGB > 63 OR RGB < 0 THEN [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")     IF i = 55 AND tot12& = 0 THEN [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")   NEXT    GET #1, , wid12          '56   GET #1, , dep12          '57   IF wid12 > 63 OR dep12 > 63 THEN [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")    FOR i = 58 TO 775      'check for Screen 13 embedded colors     GET #1, , RGB     tot13& = tot13& + RGB     'PRINT i; RGB; : SOUND 300, 1          'test     IF RGB > 63 OR RGB < 0 THEN [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")     IF i = 775 AND tot13& = 0 THEN [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")   NEXT   GET #1, , wid13          '776   GET #1, , dep13          '777 LOOP [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") 1 = 1    'TRUE statement exits one-time LOOP CLOSE #1  COLOR 14: LOCATE 10, 25 [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") i   [CASE IS](/qb64wiki/index.php/CASE_IS "CASE IS") < 56:    IF widN > 640 THEN        Scr = 13: MaxColors = 0        PRINT "Default Screen 13:"; widN \ 8; "X"; depN    ELSE     LOCATE 10, 15     PRINT "Screen 12 ("; widN; "X"; depN; ") OR 13 ("; widN \ 8; "X"; depN; ")"     DO: SOUND 600, 4        COLOR 13: LOCATE 12, 23  'ask if no data found. Prevents ERROR opening in wrong mode        [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a Screen mode 12 or 13 : ", Scrn$        Scr = VAL(Scrn$)     LOOP UNTIL Scr = 12 OR Scr = 13    END IF    IF Scr = 12 THEN MaxColors = 0: PWidth = widN: PDepth = depN    IF Scr = 13 THEN MaxColors = 0: PWidth = widN \ 8: PDepth = depN   [CASE](/qb64wiki/index.php/CASE "CASE") 56 TO 775      PRINT "Custom Screen 12:"; wid12; "X"; dep12      Scr = 12: MaxColors = 16: PWidth = wid12: PDepth = dep12   [CASE](/qb64wiki/index.php/CASE "CASE") 776: PRINT "Custom Screen 13:"; wid13 \ 8; "X"; dep13      Scr = 13: MaxColors = 256: PWidth = wid13 \ 8: PDepth = dep13 [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")  [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* The SUB procedure reads a file that was [BSAVEd](/qb64wiki/index.php/BSAVE "BSAVE") previously. If the RGB colors are stored before the image, the values can only be between 0 and 63. Higher values indicate that the image width and height are located there and that there are no stored color values to be read. SUB later displays the dimensions of the file image that [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") placed in the file array. The loop is set to only run once by creating **a TRUE [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") statement** such as 1 = 1. When a screen mode cannot be determined, the user must select one.
Dimensions and location of width and height information indicates the screen mode as [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 if it has 768 RGB values and dimensions of 320 X 200 max. If the file only holds 64 settings and/or is larger than 320 X 200, it uses SCREEN 12 or 9. The procedure [EXITs](/qb64wiki/index.php/EXIT "EXIT") the DO LOOP early when the image size is found with or without custom color settings.
Divide SCREEN 13 [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") widths by 8.
  




## See also


* [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")
* [WHILE...WEND](/qb64wiki/index.php/WHILE...WEND "WHILE...WEND")
* [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DO...LOOP&oldid=7865>"




## Navigation menu








### Search





















