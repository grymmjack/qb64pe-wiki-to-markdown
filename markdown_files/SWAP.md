


SWAP - QB64 Phoenix Edition Wiki








# SWAP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The SWAP statement is used to exchange two variable or array element values.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


SWAP *variable1*, *variable2*
  




## Description


* *variable1* and *variable2* are any type variables whose values will be exchanged.
* If either *variable1* or *variable2* is an array, then an element in the array must be designated.
* SWAP can be used with string or number variable values. Both must be of the same type.
* SWAP is often used to sort array elements into greater or lesser numerical or cumulative [ASCII](/qb64wiki/index.php/ASCII "ASCII") [STRING](/qb64wiki/index.php/STRING "STRING") values.
* SWAP can be used in page flipping to change between source and destination pages.


  

*Example 1:* A simple SWAP of [string](/qb64wiki/index.php/STRING "STRING") values.





| ``` a$ = "one" b$ = "two"  SWAP a$, b$  [PRINT](/qb64wiki/index.php/PRINT "PRINT") a$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") b$  ``` |
| --- |




| ``` two one  ``` |
| --- |


  

*Example 2:* Creating Cryptograms by scrambling EVERY capital letter in the alphabet.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") Letter$(65 [TO](/qb64wiki/index.php/TO "TO") 90) [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") [CLS](/qb64wiki/index.php/CLS "CLS") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") a = 65 [TO](/qb64wiki/index.php/TO "TO") 90                    'set ASCII codes and letters in order   Letter$(a) = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(a)              'create capitalized characters [NEXT](/qb64wiki/index.php/NEXT "NEXT") a  [COLOR](/qb64wiki/index.php/COLOR "COLOR") 11: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 10 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 65 [TO](/qb64wiki/index.php/TO "TO") 90   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Letter$(i) = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(i) [THEN](/qb64wiki/index.php/THEN "THEN")      'find characters the same as the [ASCII](/qb64wiki/index.php/ASCII "ASCII") code index     [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP"): j = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 26) + 65: [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") j = i    'loop until j <> i     SWAP Letter$(i), Letter$(j)     'swap corresponding letter characters   [END IF](/qb64wiki/index.php/END_IF "END IF")   [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(i); " ";               'print normal alphabetical order [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 12, 10 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") a = 65 [TO](/qb64wiki/index.php/TO "TO") 90                    'display new alphabetical order   [PRINT](/qb64wiki/index.php/PRINT "PRINT") Letter$(a); " "; [NEXT](/qb64wiki/index.php/NEXT "NEXT")  text$ = "This is how a normal sentence would look before being encrypted." [COLOR](/qb64wiki/index.php/COLOR "COLOR") 11: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 5: [PRINT](/qb64wiki/index.php/PRINT "PRINT") text$ L = [LEN](/qb64wiki/index.php/LEN "LEN")(text$) [DIM](/qb64wiki/index.php/DIM "DIM") Code(L)                         'place ASCII code solution into an array [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 22, 5 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") L   Code(i) = [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")([UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")(text$), i)   'in QB64, ASC can read by character position   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Code(i) >= 65 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") Code(i) <= 90 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") Letter$(Code(i)); [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(Code(i)); [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Ted Weissgerber
 *Explanation:* The Letter$ [STRING](/qb64wiki/index.php/STRING "STRING") [array](/qb64wiki/index.php/Arrays "Arrays") is first created with the letters matching the [ASCII](/qb64wiki/index.php/ASCII "ASCII") code index value. Every index is **swap**ped when the letter matches it's index code until every letter is different. The Code array holds the text code solution.
  

*Example 3:* A very quick array sorting SUB procedure using recursion sorts 10 thousand numbers in milliseconds.





| ``` [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT") A-Z [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") swap2 [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")  'Demo only [DIM](/qb64wiki/index.php/DIM "DIM") array(10000) [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") 'array can hold any type of value [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 10000   array(i) = [RND](/qb64wiki/index.php/RND "RND") * 1000 'populate array with random values to sort [NEXT](/qb64wiki/index.php/NEXT "NEXT") start = [LBOUND](/qb64wiki/index.php/LBOUND "LBOUND")(array)  'lowest element finish = [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")(array) 'highest element swap2 = 0                     'count swaps for demo only start! = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")(.001) [CALL](/qb64wiki/index.php/CALL "CALL") QuickSort(start, finish, array()) ending! = [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")(.001) tmp$ = " array(0)= ##.#####     array(5000)= ###.####   array(10000)= ###.####" [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") tmp$; array(0); array(5000); array(10000) [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") " Elapsed time: #.###### seconds with #######, swaps"; ending! - start!; swap2& [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") n = 0 [TO](/qb64wiki/index.php/TO "TO") 10000             'check array sort order   [IF](/qb64wiki/index.php/IF "IF") array(n) >= max! [THEN](/qb64wiki/index.php/THEN "THEN")     'max should match the array type     max! = array(n)   [ELSE](/qb64wiki/index.php/ELSE "ELSE") [BEEP](/qb64wiki/index.php/BEEP "BEEP")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Bad sort order!"     [EXIT](/qb64wiki/index.php/EXIT "EXIT") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")   [END IF](/qb64wiki/index.php/END_IF "END IF") [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") QuickSort (start [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), finish [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), array() [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")) [DIM](/qb64wiki/index.php/DIM "DIM") Hi [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), Lo [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), Middle [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") Hi = finish: Lo = start Middle = array((Lo + Hi) / 2) 'find middle of array [DO](/qb64wiki/index.php/DO "DO")   [DO](/qb64wiki/index.php/DO "DO") [WHILE](/qb64wiki/index.php/WHILE "WHILE") array(Lo) < Middle: Lo = Lo + 1: [LOOP](/qb64wiki/index.php/LOOP "LOOP")   [DO](/qb64wiki/index.php/DO "DO") [WHILE](/qb64wiki/index.php/WHILE "WHILE") array(Hi) > Middle: Hi = Hi - 1: [LOOP](/qb64wiki/index.php/LOOP "LOOP")   [IF](/qb64wiki/index.php/IF "IF") Lo <= Hi [THEN](/qb64wiki/index.php/THEN "THEN")     SWAP array(Lo), array(Hi)     swap2 = swap2 + 1                  'count swaps for demo only     Lo = Lo + 1: Hi = Hi - 1   [END IF](/qb64wiki/index.php/END_IF "END IF")                               'If homework, you will fail [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") Lo > Hi [IF](/qb64wiki/index.php/IF "IF") Hi > start [THEN](/qb64wiki/index.php/THEN "THEN") [CALL](/qb64wiki/index.php/CALL "CALL") QuickSort(start, Hi, array()) [IF](/qb64wiki/index.php/IF "IF") Lo < finish [THEN](/qb64wiki/index.php/THEN "THEN") [CALL](/qb64wiki/index.php/CALL "CALL") QuickSort(Lo, finish, array()) [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |




| ```  array(0)= 0.20200    array(5000)= 525.8505   array(10000)= 999.6196  Elapsed time: 0.023438 seconds with 33,759 swaps  ``` |
| --- |


**NOTE:** The *swap2* shared value is used to count the swaps for the demo and can be removed from the SUB procedure for speed.
  




## See also


* [RND](/qb64wiki/index.php/RND "RND"), [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE")
* [CHR$](/qb64wiki/index.php/CHR$ "CHR$"), [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)")
* [ASCII](/qb64wiki/index.php/ASCII "ASCII"), [Arrays](/qb64wiki/index.php/Arrays "Arrays")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SWAP&oldid=8171>"




## Navigation menu








### Search





















