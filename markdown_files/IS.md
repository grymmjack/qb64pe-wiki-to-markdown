


SELECT CASE - QB64 Phoenix Edition Wiki








# SELECT CASE



From QB64 Phoenix Edition Wiki
(Redirected from [IS](/qb64wiki/index.php?title=IS&redirect=no "IS"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
SELECT CASE is used to determine the program flow by comparing the value of a variable to specific CASE values.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


**SELECT** [EVERY]**CASE** *testExpression*
**CASE** *expressionList1*
[statement-block1]
[**CASE** *expressionList2*
[statement-block2...
[**CASE ELSE**
[statementblock-n
**END SELECT**
  




* **SELECT CASE** evaluates *testExpression* and executes the first matching [CASE](/qb64wiki/index.php/CASE "CASE") or [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE") block and exits.
* **SELECT EVERYCASE** allows the execution of all matching [CASE](/qb64wiki/index.php/CASE "CASE") blocks from top to bottom or the [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE") block.
* The literal, variable or expression *testExpression* comparison can result in any string or numerical type.
* **Note:** A *testExpression* variable value can be changed inside of true CASE evaluations in SELECT EVERYCASE.
* A *testExpression* derived from an expression or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") will only be determined once at the start of the block execution.
* Supports individual CASE values and ranges or lists of literal values as below:
	+ **CASE** casevalue: code '**case compares one numerical or text value**
	+ **CASE** casevalue1 [TO](/qb64wiki/index.php/TO "TO") casevalue2: code '**case compares a range of values**
	+ **CASE** casevalue1, casevalue2, casevalue3: code '**case compares a list of values separated by commas**
	+ **CASE IS** > casevalue: code '**case compares a value as =, <>, < or >**
	+ **CASE ELSE**: code '**bottom case statement executes only when no other CASE is executed.**
* The CASE values should cover the normal ranges of the comparison *testExpression* values.
* Use **CASE ELSE** before **END SELECT** if an alternative is necessary when no other case matches.
* CASEs should be listed in an ascending or descending values for best and fastest results.
* [STRING](/qb64wiki/index.php/STRING "STRING") comparisons will be based on their respective [ASCII](/qb64wiki/index.php/ASCII "ASCII") code values where capital letters are valued less than lower case.
* Use **SELECT CASE** when [IF...THEN](/qb64wiki/index.php/IF...THEN "IF...THEN") statements get too long or complicated.
* **SELECT CASE** and **EVERYCASE** statement blocks must **always** be ended with [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT").
* Use **[colons](/qb64wiki/index.php/Colon "Colon")** to execute multiple statements in one line.
* An **[underscore](/qb64wiki/index.php/Underscore "Underscore")** can be used anywhere after the code on one line to continue it to the next line in **QB64**.


  




## Examples


*Example 1:* SELECT CASE can use literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") or numerical values in CASE comparisons:





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a whole number value from 1 to 40: ", value value1 = 10 value2 = 20 value3 = 30  SELECT CASE value   [CASE](/qb64wiki/index.php/CASE "CASE") value1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Ten only"   [CASE](/qb64wiki/index.php/CASE "CASE") value1 [TO](/qb64wiki/index.php/TO "TO") value2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "11 to 20 only" '10 is already evaluated   [CASE](/qb64wiki/index.php/CASE "CASE") value1, value2, value3: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "30 only" '10 and 20 are already evaluated   [CASE IS](/qb64wiki/index.php/CASE_IS "CASE IS") > value2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "greater than 20 but not 30" '30 is already evaluated   [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Other value" 'values less than 10 [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")  ``` |
| --- |


*Explanation:* The first true CASE is executed and SELECT CASE is exited. "Other value" is printed for values less than 10.
  

*Example 2:* SELECT CASE will execute the first CASE statement that is true and ignore all CASE evaluations after that:





| ``` a = 100 SELECT CASE a          'designate the value to compare   [CASE](/qb64wiki/index.php/CASE "CASE") 1, 3, 5, 7, 9     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown."   [CASE](/qb64wiki/index.php/CASE "CASE") 10     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown."   [CASE](/qb64wiki/index.php/CASE "CASE") 50     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown."   [CASE](/qb64wiki/index.php/CASE "CASE") 100     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will be displayed when a equals 100"     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "(and no other case will be checked)"   [CASE](/qb64wiki/index.php/CASE "CASE") 150     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown."   [CASE IS](/qb64wiki/index.php/CASE_IS "CASE IS") < 150     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown as a previous case was true"   [CASE](/qb64wiki/index.php/CASE "CASE") 50 [TO](/qb64wiki/index.php/TO "TO") 150     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown as a previous case was true"   [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE")    [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will only print if it gets this far!" [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")  ``` |
| --- |




| ``` This will be displayed when a equals 100 (and no other case will be checked)  ``` |
| --- |


*Explanation:* The first case where a value is true is shown, the remainder are skipped. Try changing the value of *a*.
  

*Example 3:* Same as Example 2 but, SELECT EVERYCASE will execute every CASE statement that is true.





| ``` a = 100 SELECT EVERYCASE a          'designate the value to compare   [CASE](/qb64wiki/index.php/CASE "CASE") 1, 3, 5, 7, 9     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown."   [CASE](/qb64wiki/index.php/CASE "CASE") 10     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown."   [CASE](/qb64wiki/index.php/CASE "CASE") 50     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown."   [CASE](/qb64wiki/index.php/CASE "CASE") 100     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will be displayed when a equals 100"     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "(and other cases will be checked)"   [CASE](/qb64wiki/index.php/CASE "CASE") 150     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will not be shown."   [CASE IS](/qb64wiki/index.php/CASE_IS "CASE IS") < 150     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will be shown as 100 is less than 150"   [CASE](/qb64wiki/index.php/CASE "CASE") 50 [TO](/qb64wiki/index.php/TO "TO") 150     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will be shown as 100 is between 50 and 150"   [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE")    [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This will only print if no other CASE is true!" [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")  ``` |
| --- |




| ``` This will be displayed when a equals 100 (and other cases will be checked) This will be shown as 100 is less than 150 This will be shown as 100 is between 50 and 150  ``` |
| --- |


*Explanation:* [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE") will only execute if no other CASE was true. See Example 5 for more usages.
  

*Example 4:* SELECT CASE evaluates string values by the [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)") code value according to [ASCII](/qb64wiki/index.php/ASCII "ASCII").





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Enter a letter, number or punctuation mark from the keyboard: "; value$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) [PRINT](/qb64wiki/index.php/PRINT "PRINT") value$ value1$ = "A" value2$ = "m" value3$ = "z"  SELECT CASE value$   [CASE](/qb64wiki/index.php/CASE "CASE") value1$: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "A only"   [CASE](/qb64wiki/index.php/CASE "CASE") value1$ [TO](/qb64wiki/index.php/TO "TO") value2$: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "B to m" 'A is already evaluated   [CASE](/qb64wiki/index.php/CASE "CASE") value1$, value2$, value3$: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "z only" 'A and m are already evaluated   [CASE IS](/qb64wiki/index.php/CASE_IS "CASE IS") > value2$: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "greater than m but not z" 'z is already evaluated   [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "other value" 'key entry below A including all numbers [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")  ``` |
| --- |


*Notes:* [STRING](/qb64wiki/index.php/STRING "STRING") values using multiple characters will be compared by the [ASCII](/qb64wiki/index.php/ASCII "ASCII") code values sequentially from left to right. Once the equivalent code value of one string is larger than the other the evaluation stops. This allows string values to be compared and sorted alphabetically using [>](/qb64wiki/index.php/Greater_Than "Greater Than") or [<](/qb64wiki/index.php/Less_Than "Less Than") and to [SWAP](/qb64wiki/index.php/SWAP "SWAP") values in [arrays](/qb64wiki/index.php/Arrays "Arrays") regardless of the string lengths.
  

*Example 5:* EVERYCASE is used to draw sections of digital numbers in a simulated LED readout using numbers from 0 to 9:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 DO   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a number 0 to 9: ", num   [CLS](/qb64wiki/index.php/CLS "CLS")   SELECT EVERYCASE num     [CASE](/qb64wiki/index.php/CASE "CASE") 0, 2, 3, 5 [TO](/qb64wiki/index.php/TO "TO") 9: [PSET](/qb64wiki/index.php/PSET "PSET") (20, 20), 12       [DRAW](/qb64wiki/index.php/DRAW "DRAW") "E2R30F2G2L30H2BR5P12,12" 'top horiz     [CASE](/qb64wiki/index.php/CASE "CASE") 0, 4 [TO](/qb64wiki/index.php/TO "TO") 6, 8, 9: [PSET](/qb64wiki/index.php/PSET "PSET") (20, 20), 12       [DRAW](/qb64wiki/index.php/DRAW "DRAW") "F2D30G2H2U30E2BD5P12,12" 'left top vert     [CASE](/qb64wiki/index.php/CASE "CASE") 0, 2, 6, 8: [PSET](/qb64wiki/index.php/PSET "PSET") (20, 54), 12       [DRAW](/qb64wiki/index.php/DRAW "DRAW") "F2D30G2H2U30E2BD5P12, 12" 'left bot vert     [CASE](/qb64wiki/index.php/CASE "CASE") 2 [TO](/qb64wiki/index.php/TO "TO") 6, 8, 9: [PSET](/qb64wiki/index.php/PSET "PSET") (20, 54), 12       [DRAW](/qb64wiki/index.php/DRAW "DRAW") "E2R30F2G2L30H2BR5P12, 12" 'middle horiz     [CASE](/qb64wiki/index.php/CASE "CASE") 0 [TO](/qb64wiki/index.php/TO "TO") 4, 7 [TO](/qb64wiki/index.php/TO "TO") 9: [PSET](/qb64wiki/index.php/PSET "PSET") (54, 20), 12       [DRAW](/qb64wiki/index.php/DRAW "DRAW") "F2D30G2H2U30E2BD5P12,12" 'top right vert     [CASE](/qb64wiki/index.php/CASE "CASE") 0, 1, 3 [TO](/qb64wiki/index.php/TO "TO") 9: [PSET](/qb64wiki/index.php/PSET "PSET") (54, 54), 12       [DRAW](/qb64wiki/index.php/DRAW "DRAW") "F2D30G2H2U30E2BD5P12,12" 'bottom right vert     [CASE](/qb64wiki/index.php/CASE "CASE") 0, 2, 3, 5, 6, 8: [PSET](/qb64wiki/index.php/PSET "PSET") (20, 88), 12       [DRAW](/qb64wiki/index.php/DRAW "DRAW") "E2R30F2G2L30H2BR5P12,12" 'bottom horiz     [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE")       [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 20: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Goodbye!"; num   [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") num > 9  ``` |
| --- |


**Note:** [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE") will only execute if no other CASE is true! Changing the comparison value in a CASE may affect later CASE evaluations. **Beware of duplicate variables inside of cases affecting the comparison values and remaining cases.**
  




## See also


* [IF...THEN](/qb64wiki/index.php/IF...THEN "IF...THEN"), [Boolean](/qb64wiki/index.php/Boolean "Boolean")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SELECT_CASE&oldid=8591>"




## Navigation menu








### Search





















