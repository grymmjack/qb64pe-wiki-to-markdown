


\_PRESERVE - QB64 Phoenix Edition Wiki








# \_PRESERVE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_PRESERVE [REDIM](/qb64wiki/index.php/REDIM "REDIM") action preserves the current contents of [dynamic](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") [arrays](/qb64wiki/index.php/Arrays "Arrays"), when resizing or changing indices.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 Errors](#Errors) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[REDIM](/qb64wiki/index.php/REDIM "REDIM") \_PRESERVE array(*newLowerIndex&* [TO *newUpperIndex&*]) [AS variabletype]
  




## Description


* [REDIM](/qb64wiki/index.php/REDIM "REDIM") or the [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") metacommand must be used when the array is first created to be able to resize and preserve.
* If \_PRESERVE is not used, the current contents of the array are cleared by [REDIM](/qb64wiki/index.php/REDIM "REDIM").
	+ All element values of an array are preserved if the array size is increased.
	+ The remaining elements of the array are preserved if the array size is decreased.
	+ If the new index range is different from the original, all values will be moved to the new corresponding indices.
* **REDIM \_PRESERVE cannot change the number of array dimensions, but can change the number of elements.**
* **Always use the same array [TYPE](/qb64wiki/index.php/TYPE "TYPE") suffix ([AS](/qb64wiki/index.php/AS "AS") type) or a new array type with the same name may be created.**


### Errors


* [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") arrays created using [REDIM](/qb64wiki/index.php/REDIM "REDIM") require that they be recreated to be used after arrays are [ERASEd](/qb64wiki/index.php/ERASE "ERASE").
* **Warning:** Do not use negative upper array index values as an "Out of Memory" [error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") (or global Operating System errors) will occur.
* Use \_PRESERVE before [SHARED](/qb64wiki/index.php/SHARED "SHARED") or an "invalid variable name" error will occur.


  




## Examples


*Example 1:* Changing the upper and lower array bounds





| ``` [REDIM](/qb64wiki/index.php/REDIM "REDIM") a(5 [TO](/qb64wiki/index.php/TO "TO") 10) ' create array as dynamic using REDIM a(5) = 123 [REDIM](/qb64wiki/index.php/REDIM "REDIM") _PRESERVE a(20 [TO](/qb64wiki/index.php/TO "TO") 40) [PRINT](/qb64wiki/index.php/PRINT "PRINT") a(20)  ``` |
| --- |


*Explanation:* a(20) is now the 123 value a(5) was. The upper or lower bounds of arrays can be changed, but the type cannot. New array indices like a(40) are null(0) or empty strings. If the array element count is not reduced, all of the data will be preserved.
  

*Example 2:* Sizing an array while storing file data.





| ``` [REDIM](/qb64wiki/index.php/REDIM "REDIM") Array$(1)                'create a dynamic string array filename$ = "Readme.txt"       'QB64 information text file [OPEN](/qb64wiki/index.php/OPEN "OPEN") filename$ [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") [AS](/qb64wiki/index.php/AS "AS") #1 [DO](/qb64wiki/index.php/DO "DO") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [EOF](/qb64wiki/index.php/EOF "EOF")(1)   count = count + 1   [IF](/qb64wiki/index.php/IF "IF") count > [UBOUND](/qb64wiki/index.php/UBOUND "UBOUND")(Array$) [THEN](/qb64wiki/index.php/THEN "THEN")     [REDIM](/qb64wiki/index.php/REDIM "REDIM") _PRESERVE Array$(count * 3 / 2)'increase array's size by 50% without losing data   [END IF](/qb64wiki/index.php/END_IF "END IF")    [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") #1, textline$   Array$(count) = textline$ [LOOP](/qb64wiki/index.php/LOOP "LOOP") [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") c = 1 [TO](/qb64wiki/index.php/TO "TO") count [PRINT](/qb64wiki/index.php/PRINT "PRINT") Array$(c) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") c [MOD](/qb64wiki/index.php/MOD "MOD") 20 = 0 [THEN](/qb64wiki/index.php/THEN "THEN") k$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1111)
* [REDIM](/qb64wiki/index.php/REDIM "REDIM")
* [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC")
* [Arrays](/qb64wiki/index.php/Arrays "Arrays")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PRESERVE&oldid=8887>"




## Navigation menu








### Search





















