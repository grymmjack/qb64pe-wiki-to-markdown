


KEY - QB64 Phoenix Edition Wiki








# KEY



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The [KEY n](/qb64wiki/index.php/KEY_n "KEY n") statement is used to assign a "soft key" string or a flag and scan code to a function key or display function soft key assignments.


  






| Contents * [1 Syntax](#Syntax) * [2 Function Soft Key Strings (1 to 10, 30 & 31)](#Function_Soft_Key_Strings_(1_to_10,_30_&_31)) * [3 Number Pad Arrow Keys (11 to 14)](#Number_Pad_Arrow_Keys_(11_to_14)) * [4 User Defined Keys (15 to 29)](#User_Defined_Keys_(15_to_29)) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


**KEY *n%*, *textString$***
**KEY *n%*, CHR$(*keyFlag%*) + CHR$(*scanCode*)**
  




## Function Soft Key Strings (1 to 10, 30 & 31)


**Assigning "Softkey" [STRING](/qb64wiki/index.php/STRING "STRING") values to function key press events**
* n% is the number 1 to 10 (F1 to F10), 30 or 31 (F11 or F12) of the function key to assign the soft key string.
* Instead of using an [ON KEY(n)](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)") [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") statement, Function keys F1 to F12 can be assigned a "soft key" string value to return.
* KEY n, text$ defines a literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") "soft key" function key return value.




| ```         **KEY 1, "Help"** 'returns the string "Help" to [INPUT](/qb64wiki/index.php/INPUT "INPUT") variable when F1 is pressed ``` |
| --- |


* [KEY LIST](/qb64wiki/index.php/KEY_LIST "KEY LIST") displays each of the 12 softkey **function key** (F1 to F12) string values going down left side of screen.
* [KEY {ON|OFF}](/qb64wiki/index.php/KEY_LIST "KEY LIST") displays or hides the softkey values of function keys F1 to F10 at the bottom of the screen.


  




## Number Pad Arrow Keys (11 to 14)


* Arrow keys on the Number Pad are predefined KEY numbers 11 to 14 and only work with Number Lock off.
* Soft Key [STRINGs](/qb64wiki/index.php/STRING "STRING") cannot be assigned to these key numbers!
* To use the extended arrow keys on a keyboard use the Extended Key Flag 128 with corresponding Scan code as User Defined Keys.


  




## User Defined Keys (15 to 29)


**Assigning user defined keys or combinations with: KEY n, CHR$(keyflag) + CHR$(scancode)**


| ```                    **Function Key Flag Combination Values**                    **0** = no function key combination flag(single key)                   **1** = Left Shift key flag                   **2** = Right Shift key flag                   **4** = Ctrl flag                   **8** = Alt flag                  **32** = Number Lock flag                  **64** = Caps Lock flag                 **128** = Extended keys (see trapping extended keys below)            Flag values can be added to monitor multiple function key combinations.  ``` |
| --- |


* After the keyflag code character the [scancode](/qb64wiki/index.php/Scancodes "Scancodes") character is added using one of the two **trapping methods** that follow:




| ``` '                           **Soft Key Scan Code Values** ' '      1  2  3  4  5  6  7  8  9  10   30  31                       Predefined Keys ' **Esc  F1 F2 F3 F4 F5 F6 F7 F8 F9 F10  F11 F12   SysReq ScrL Pause** '  1   59 60 61 62 63 64 65 66 67 68   87  88     --    70    29 ' **`~  1! 2@ 3# 4$ 5% 6^ 7& 8* 9( 0) -_ =+ BkSpc  Insert Home PgUp   NumL   /     *    -** '  41 2  3  4  5  6  7  8  9  10 11 12 13  14     82    71    73    32/69  53    55   74 ' **Tab  Q  W  E  R  T  Y  U  I  O  P  [{ ]} \|    Delete End  PgDn   7/Home 8/▲  9/PU  +**  '  15  16 17 18 19 20 21 22 23 24 25 26 27 43     83    79    81     71   11/72  73   78 ' **CapL  A  S  D  F  G  H  J  K  L  ;: '"  Enter                     4/◄-   5    6/-►  E** ' 64/58 30 31 32 33 34 35 36 37 38 39 40   28                       12/75  76   13/77 **n** ' **Shift  Z  X  C  V  B  N  M  ,< .> /?    Shift         ▲           1/End  2/▼  3/PD  t** ' 1/42   44 45 46 47 48 49 50 51 52 53    2/54          72           79   14/80  81   **e** ' **Ctrl Win Alt    Spacebar    Alt Win Menu Ctrl     ◄-  ▼   -►      0/Insert    ./Del r** ' 4/29  91 8/56      57       56  92   93  29       75  80  77       82          83   28 ' '  **Keyflag:** Function(0, 1, 2, 4, 8, 32, 64), Extended(128) **Scan Code:** 1-88, QB64 only(91-93) ' '        Reserved and function key combinations can be made using the scan code instead. '             Add function flag values to 128 for Extended key combinations.  ``` |
| --- |


NOTE: The above commented table can be copied and pasted directly into the QB64 IDE
  




**Trapping Ctrl, Alt and Shift key combinations**
Keyboard Flag values can be added to monitor more than one control key. For example, flag combination 12 would flag both the Ctrl and Alt key presses. Since the flag already determines the function key to monitor, you don't necessarily have to use it's scancode. You can look for a key combination such as Ctrl + by using the plus key's scancode which is 13 as shown below:


| ```       **KEY 15, CHR$(4) + CHR$(13)** 'enabled event when Ctrl and + key are pressed ``` |
| --- |


  




**Trapping Extended keys (Insert, Home, Page Up, Right Ctrl, R.Alt, and cursor arrow pad)**
* On a 101-key keyboard, you can trap any of the keys on the dedicated cursorpad by assigning the string to any of the keynumber values from 15 to 25 using the 128 keyboard flag. The cursor arrows are not the same as the pre-assigned number pad arrows:




| ```       **KEY n, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(128) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(scancode) ' where n = 15 to 29. See: [Scancodes](/qb64wiki/index.php/Scancodes "Scancodes")**                KEY 15, CHR$(128) + CHR$(75)  'left arrow cursor pad                KEY 16, CHR$(128) + CHR$(72)  'up arrow cursor pad                KEY 17, CHR$(128) + CHR$(77)  'right arrow cursor pad                KEY 18, CHR$(128) + CHR$(80)  'down arrow cursor pad  ``` |
| --- |


Use CHR$(0) for the first byte flag for non-function keys. You can substitute a literal [STRING](/qb64wiki/index.php/STRING "STRING") value to trap as shown in Example 2.
  




([Return to Table of Contents](#toc))


  




## Examples


*Example 1:* Shows a list of all the string assignments to the function keys F1-F12 (Prints help every time F1 is pressed in the input)





| ``` [KEY](/qb64wiki/index.php/KEY_n "KEY n") 1, "Help" [KEY LIST](/qb64wiki/index.php/KEY_LIST "KEY LIST") INPUT "Press F1 or to quit press ENTER: ", a$   ``` |
| --- |




| ``` F1 Help F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 Press F1 or to quit press ENTER: HelpHelpHelpHelp  ``` |
| --- |


  

*Example 2:* Trapping the Control + key combination. Use the Control Keyboard flag 4 and + key scancode 13.





| ``` [CLS](/qb64wiki/index.php/CLS "CLS") [KEY](/qb64wiki/index.php/KEY_n "KEY n") 15, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(4) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(13)     'scancode for "=" or "+" key is 13 [ON KEY](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")(15) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") control       'action of user defined key press [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(15) ON                     'turn ON event trapping for key combination [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press Ctrl and plus key combination, escape quits!" [DO](/qb64wiki/index.php/DO "DO"): [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") count = count + 1 [PRINT](/qb64wiki/index.php/PRINT "PRINT") count; [IF](/qb64wiki/index.php/IF "IF") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [THEN](/qb64wiki/index.php/THEN "THEN") [END](/qb64wiki/index.php/END "END")  'escape key exit [LOOP](/qb64wiki/index.php/LOOP "LOOP")  control:                             'NUMBER LOCK MUST BE OFF! [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Control and + keys pressed!"; [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


Code by Ted Weissgerber
  

*Example 3:* Differentiating the extended cursor keypad arrows from the predefined Number Pad arrow keys.





| ``` 'predefined keys 11 to 14 for number pad arrows only [ON KEY](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")(11) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") UpNum: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(11) ON 'up [ON KEY](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")(12) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") LNum: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(12) ON  'left [ON KEY](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")(13) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") RNum: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(13) ON  'right [ON KEY](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")(14) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") DnNum: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(14) ON 'down 'user defined keys use extended key flag 128 + scan code [ON KEY](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")(15) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") UpPad [KEY](/qb64wiki/index.php/KEY_n "KEY n") 15, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(128) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(72): [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(15) ON 'cursor up [ON KEY](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")(16) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") LPad [KEY](/qb64wiki/index.php/KEY_n "KEY n") 16, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(128) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(75): [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(16) ON 'cursor left [ON KEY](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")(17) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") RPad [KEY](/qb64wiki/index.php/KEY_n "KEY n") 17, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(128) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(77): [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(17) ON 'cursor right [ON KEY](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")(18) [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") DnPad [KEY](/qb64wiki/index.php/KEY_n "KEY n") 18, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(128) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(80): [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(18) ON 'cursor down  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = 0 DO   numL = [PEEK](/qb64wiki/index.php/PEEK "PEEK")(1047) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") 32 '32 if on   capL = [PEEK](/qb64wiki/index.php/PEEK "PEEK")(1047) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") 64 '64 on   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") numL [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") capL [THEN](/qb64wiki/index.php/THEN "THEN")     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 12: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 13, 50: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Turn Num or Cap Lock OFF!"   [ELSE](/qb64wiki/index.php/ELSE "ELSE") : [COLOR](/qb64wiki/index.php/COLOR "COLOR") 10: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 13, 50: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Number and Cap Lock OK!  "     [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")                  ' [KEY](/qb64wiki/index.php/KEY_n "KEY n") or [TIMER](/qb64wiki/index.php/TIMER "TIMER") event breaks a sleep   [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")  [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(15) OFF: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(16) OFF: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(17) OFF: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(18) OFF [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(11) OFF: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(12) OFF: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(13) OFF: [KEY](/qb64wiki/index.php/KEY(n) "KEY(n)")(14) OFF [END](/qb64wiki/index.php/END "END")  UpPad: COLOR 14: LOCATE 11, 26: PRINT " Up cursor pad  " [RETURN](/qb64wiki/index.php/RETURN "RETURN") LPad: COLOR 14: LOCATE 11, 26: PRINT "Left cursor pad " [RETURN](/qb64wiki/index.php/RETURN "RETURN") RPad: COLOR 14: LOCATE 11, 26: PRINT "Right cursor pad" [RETURN](/qb64wiki/index.php/RETURN "RETURN") DnPad: COLOR 14: LOCATE 11, 26: PRINT "Down cursor pad " [RETURN](/qb64wiki/index.php/RETURN "RETURN") UpNum: COLOR 11: LOCATE 11, 26: PRINT " Up number pad  " [RETURN](/qb64wiki/index.php/RETURN "RETURN") LNum: COLOR 11: LOCATE 11, 26: PRINT "Left number pad " [RETURN](/qb64wiki/index.php/RETURN "RETURN") RNum: COLOR 11: LOCATE 11, 26: PRINT "Right number pad" [RETURN](/qb64wiki/index.php/RETURN "RETURN") DnNum: COLOR 11: LOCATE 11, 26: PRINT "Down number pad " [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


*Explanation:* The Number Lock or Caps Lock keys ON may hinder extended key reads in QBasic but not QB64!
  




([Return to Table of Contents](#toc))


  




## See also


* [KEY LIST](/qb64wiki/index.php/KEY_LIST "KEY LIST"), [ON KEY(n)](/qb64wiki/index.php/ON_KEY(n) "ON KEY(n)")
* [KEY(n)](/qb64wiki/index.php/KEY(n) "KEY(n)"), [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")
* [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT"), [\_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN")
* [Keyboard scancodes](/qb64wiki/index.php/Keyboard_scancodes "Keyboard scancodes")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=KEY&oldid=8040>"




## Navigation menu








### Search





















