# $INCLUDEONCE
> The $INCLUDEONCE metacommand, when placed in include files, prevents that the file's contents is injected multiple times into a program, even if the file is included multiple times directly or indirectly through other include files.

## SYNTAX
`$INCLUDEONCE`

## DESCRIPTION
* As QB64 metacommand it does not require a comment ' or [REM](REM.md) before it.
* It can be placed everywhere in an include file, but must be the only thing in the line, hence without additional whitespace or comments. Even if placed in the middle or the end of the file, it always designates the entire file contents.
	* Even if placed in the middle or the end of the file, it always designates the entire file contents.
* Even if placed in the middle or the end of the file, it always designates the entire file contents.
* If placed in the main program, $INCLUDEONCE does nothing and is simply ignored without error.
* $INCLUDEONCE will not work when placed inside pre-compiler $[IF](IF.md) .. $[ELSE](ELSE.md) ... $[END](END.md) [IF](IF.md) blocks.


## EXAMPLES

```vb
'included by test.bas and incl.bm

$INCLUDEONCE

PRINT
PRINT "This prints from file once.bm, and should appear only once on screen."
```

* Featured in our "Keyword of the Day" series
* $INCLUDE
* Metacommand

```vb
'included by test.bas and incl.bm

$INCLUDEONCE

PRINT
PRINT "This prints from file once.bm, and should appear only once on screen."
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* $INCLUDE
* Metacommand

