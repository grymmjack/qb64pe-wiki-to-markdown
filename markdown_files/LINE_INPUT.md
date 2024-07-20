## LINE INPUT
---

### The LINE INPUT statement requests a STRING keyboard entry from a program user.

#### SYNTAX

`LINE INPUT [;] "[text prompt or question]"{,|;} stringVariable$`

#### PARAMETERS
* A semicolon immediately after [LINE](./LINE.md) [INPUT](./INPUT.md) stops the cursor after the entry and prevents screen roll on the lowest two screen rows.
* text prompt or question is optional, but quotes are necessary unless just a semicolon is used before the stringVariable$ .
* Requires only one string variable to hold the entire text entry.


#### DESCRIPTION
* Cannot use numerical type variables or comma separated variable lists for multiple entries.
* Allows commas and quotation marks in the user input, unlike [INPUT](./INPUT.md) where commas denote extra input values and quotes delimit strings.
* The statement halts the program until an entry is made. Pressing Enter ends the entry and code execution resumes.
* [LINE](./LINE.md) [INPUT](./INPUT.md) does not trim off leading or trailing spaces in the string entry like [INPUT](./INPUT.md) string returns.
* Use [VAL](./VAL.md) to convert string numbers and &O (octal), &H (hexadecimal) or &B (binary) prefixed entries into numerical values.
* Use [_DEST](./_DEST.md) [_CONSOLE](./_CONSOLE.md) before [LINE](./LINE.md) [INPUT](./INPUT.md) statements to receive input from a console window.
* Note: QB64 will not remove CHR$(0) from the end of [LINE](./LINE.md) [INPUT](./INPUT.md) string return values like QBasic did.


#### EXAMPLES
##### Example: Preventing screen roll after an input entry on the bottom 2 screen rows.
```vb
SCREEN 12

COLOR 14: LOCATE 29, 2 '          place dursor at beginning of prompt liine
PRINT "Enter a name to search for... "; 'print prompt on screen
COLOR 15: LINE INPUT ; "", name$ '       get search name from user
LOCATE 29, 2: PRINT SPC(78); '       erase previous prompt
n$ = UCASE$(name$) '                 convert search name to upper case
COLOR 14'                        change foreground color to yellow
LOCATE 29, 2: PRINT "Searching..."; 'print message
SLEEP
```
  
```vb
Enter a name to search for... █
```
  


#### SEE ALSO
* [INPUT](./INPUT.md) (file mode) , [INPUT](./INPUT.md) # , [LINE](./LINE.md) [INPUT](./INPUT.md) #
* [INPUT](./INPUT.md) , [INPUT](./INPUT.md)$ (keyboard input)
* [COLOR](./COLOR.md) , [LOCATE](./LOCATE.md)
* INKEY$
* [_KEYHIT](./_KEYHIT.md) , [_KEYDOWN](./_KEYDOWN.md)
