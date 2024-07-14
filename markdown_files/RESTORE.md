


RESTORE - QB64 Phoenix Edition Wiki








# RESTORE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **RESTORE** statement is used to reset the DATA pointer to the beginning of the data.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


RESTORE [datafield]
  




* The datafield line label or number enables a labeled data field to be [READ](/qb64wiki/index.php/READ "READ") more than once as required.
* Datafield label names are not required when working with ONE or a progression of data fields in the main body of code.
* Label multiple data fields to restore them to use them again when necessary.
* If RESTORE is used with unlabeled data fields or no datafield is designated then the first data field is read.
* Use RESTORE to avoid an ["Out of Data" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") when reading a data field!
* See the [DATA](/qb64wiki/index.php/DATA "DATA") statement for [STRING](/qb64wiki/index.php/STRING "STRING") data value specifications.
* **Do not place [DATA](/qb64wiki/index.php/DATA "DATA") fields after [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures! QB64 will FAIL to RESTORE properly!**


QBasic allowed programmers to add DATA fields anywhere because the IDE separated the main code from other procedures.
  

*Example:* Restoring a labeled DATA field to avoid going past the end of DATA.





| ``` DO    [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a month number(1 to 12): ", monthnum%     RESTORE Months    FOR i = 1 TO monthnum%       [READ](/qb64wiki/index.php/READ "READ") month$, days%   'variables must match data field types    NEXT    [PRINT](/qb64wiki/index.php/PRINT "PRINT") "The month "; month$; " has"; days%; "days." LOOP UNTIL monthnum% < 1 OR monthnum% > 12   Months:  [DATA](/qb64wiki/index.php/DATA "DATA") January, 31, February, 28, March, 31, April, 30, May, 31, June, 30  [DATA](/qb64wiki/index.php/DATA "DATA") July, 31, August, 31, September, 30, October, 31, November, 30, December, 31  ``` |
| --- |




| ``` Enter a month number(1 to 12): 6 The month June has 30 days.  ``` |
| --- |


*Note:* String DATA values do not require quotes unless they have commas, end spaces or QBasic keywords in them.
  



*Example:* Using RESTORE to know the number of elements in the DATA in order to dimension and store the items in a array.





| ``` [DO](/qb64wiki/index.php/DO "DO") [READ](/qb64wiki/index.php/READ "READ") dummy$ 'we won't actually use this string for anything else than to know when there is no more DATA. count = count + 1 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") dummy$ = "stop" 'when dummy$ = "stop" then we know that it is the last entry so it only does the above loop until then.  count = count - 1 'since the last string is "stop" and we don't want to store it in the array.  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "The number of relevant entries are:"; count  [DIM](/qb64wiki/index.php/DIM "DIM") entry$(count) 'Now we know how many elements we need to make space for (DIM)  RESTORE 'We restore it so that it begins reading from the first DATA again.   [FOR](/qb64wiki/index.php/FOR "FOR") c = 1 [TO](/qb64wiki/index.php/TO "TO") count [READ](/qb64wiki/index.php/READ "READ") entry$(c) 'read the DATA and store it into the array. [NEXT](/qb64wiki/index.php/NEXT "NEXT")  'we can now print the contents of the array:  [FOR](/qb64wiki/index.php/FOR "FOR") c = 1 [TO](/qb64wiki/index.php/TO "TO") count [PRINT](/qb64wiki/index.php/PRINT "PRINT") entry$(c) [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [END](/qb64wiki/index.php/END "END")  [DATA](/qb64wiki/index.php/DATA "DATA") "entry1", "entry2", "entry3", "stop"  ``` |
| --- |


Code By: Cyperium


| ``` The number of relevant entries are: 3 entry1 entry2 entry3  ``` |
| --- |


*Note:* Now we can add any number of entries without further compensation to the code.


  




## See also


* [DATA](/qb64wiki/index.php/DATA "DATA"), [READ](/qb64wiki/index.php/READ "READ")
* [$EMBED](/qb64wiki/index.php/$EMBED "$EMBED"). [\_EMBEDDED$](/qb64wiki/index.php/EMBEDDED$ "EMBEDDED$")
* [line numbers](/qb64wiki/index.php/Line_numbers "Line numbers")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RESTORE&oldid=8697>"




## Navigation menu








### Search





















