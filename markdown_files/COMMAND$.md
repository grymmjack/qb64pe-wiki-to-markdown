# COMMAND$
> The COMMAND$ function returns the command line argument(s) passed when a program is run.

## SYNTAX
`commandLine$ = COMMAND$ [(count%)]`

## DESCRIPTION
* The [STRING](STRING.md) return value is anything typed after a program's executable file name in command line (or using the [RUN](RUN.md) statement).
* Unlike QuickBASIC, QB64 does not return all uppercase values so keep that in mind when checking parameters.
* In QB64 , COMMAND$ works as an array to return specific elements passed to the command line. COMMAND$(2) would return the second parameter passed at the command line. Arguments can contain spaces if they are passed inside quotation marks. This can be used to properly retrieve file names and arguments which contain spaces.
* Use the [_COMMANDCOUNT](_COMMANDCOUNT.md) function to find the number of parameters passed to a program via the command line. See Example 2 below.


## EXAMPLES
> Example 1: Compile both programs. ProgramA RUNs ProgramB with a parameter passed following the filename:

```vb
LOCATE 12, 36: PRINT "ProgramA"

LOCATE 23, 25: PRINT "Press any key to run ProgramB"
K$ = INPUT$(1)
RUN "ProgramB FS"  'pass FS parameter to ProgramB in QB64 or QB4.5

SYSTEM
```

> Example 2: Program gets the number of parameters passed to the program, and then prints those parameters to the screen one at a time.

```vb
LOCATE 12, 36: PRINT "ProgramA"

LOCATE 23, 25: PRINT "Press any key to run ProgramB"
K$ = INPUT$(1)
RUN "ProgramB FS"  'pass FS parameter to ProgramB in QB64 or QB4.5

SYSTEM
```

> Example 3: As part of the command array syntax, you can also just read the array to see how many commands were sent (or simply check _COMMANDCOUNT ):

```vb
LOCATE 12, 36: PRINT "ProgramA"

LOCATE 23, 25: PRINT "Press any key to run ProgramB"
K$ = INPUT$(1)
RUN "ProgramB FS"  'pass FS parameter to ProgramB in QB64 or QB4.5

SYSTEM
```


```vb
LOCATE 12, 36: PRINT "ProgramA"

LOCATE 23, 25: PRINT "Press any key to run ProgramB"
K$ = INPUT$(1)
RUN "ProgramB FS"  'pass FS parameter to ProgramB in QB64 or QB4.5

SYSTEM
```

* Featured in our "Keyword of the Day" series
* [SHELL](SHELL.md) , [RUN](RUN.md)
* UCASE$ , LCASE$
* [_COMMANDCOUNT](_COMMANDCOUNT.md)

```vb
LOCATE 12, 36: PRINT "ProgramA"

LOCATE 23, 25: PRINT "Press any key to run ProgramB"
K$ = INPUT$(1)
RUN "ProgramB FS"  'pass FS parameter to ProgramB in QB64 or QB4.5

SYSTEM
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* [SHELL](SHELL.md) , [RUN](RUN.md)
* UCASE$ , LCASE$
* [_COMMANDCOUNT](_COMMANDCOUNT.md)

