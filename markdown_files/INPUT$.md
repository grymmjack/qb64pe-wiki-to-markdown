# INPUT$
> The INPUT$ function is used to receive data from the user's keyboard, an open file or an open port.

## SYNTAX
`result$ = INPUT$ ( numberOfBytes% [, fileOrPortNumber])`

## DESCRIPTION
* Keyboard input is limited to the [INTEGER](INTEGER.md) numberOfBytes% (characters) designated by program.
* The keyboard is the default device when a file or port number is omitted. The numberOfBytes% is number of key presses to read.
* [INPUT](INPUT.md)$ will wait until the number of bytes are read from the keyboard or port. One byte per loop is recommended with ports.
* [RANDOM](RANDOM.md) opened file bytes can be up to the [LEN](LEN.md) = recordLength statement, or 128 if no statement is used.
* fileOrPortNumber is the number that was used in the [OPEN](OPEN.md) [AS](AS.md) statement.
* Returns [STRING](STRING.md) values including spaces or even extended ASCII characters.
* Backspace key results in the CHR$ (8) character being added to an entry.
* Use [LOCATE](LOCATE.md) , , 1 to view the cursor entry. Turn the cursor off using [LOCATE](LOCATE.md) , , 0 .
* Use [_DEST](_DEST.md) [_CONSOLE](_CONSOLE.md) before [INPUT](INPUT.md)$ is used  to receive input from a console window.


## EXAMPLES
> Example 1: A keyboard limited length entry can be made with a fixed blinking cursor. Entry must be completed before it can be shown.

```vb
LOCATE 10, 10, 1         'display fixed cursor at location
year$ = INPUT$(4)        'waits until all 4 digits are entered
PRINT year$              'display the text entry
```

> Example 2: Reading bytes from a text file for an 80 wide screen mode.

```vb
LOCATE 10, 10, 1         'display fixed cursor at location
year$ = INPUT$(4)        'waits until all 4 digits are entered
PRINT year$              'display the text entry
```

> Example 3: Getting the entire text file data as one string value.

```vb
LOCATE 10, 10, 1         'display fixed cursor at location
year$ = INPUT$(4)        'waits until all 4 digits are entered
PRINT year$              'display the text entry
```


```vb
LOCATE 10, 10, 1         'display fixed cursor at location
year$ = INPUT$(4)        'waits until all 4 digits are entered
PRINT year$              'display the text entry
```

* [INPUT](INPUT.md) , [LINE](LINE.md) [INPUT](INPUT.md) (keyboard input)
* [INPUT](INPUT.md) (file mode) , [INPUT](INPUT.md) # , [LINE](LINE.md) [INPUT](INPUT.md) # (file input)
* [OPEN](OPEN.md) , [LOC](LOC.md) (file)
* [LOCATE](LOCATE.md) (cursor on/off)

```vb
LOCATE 10, 10, 1         'display fixed cursor at location
year$ = INPUT$(4)        'waits until all 4 digits are entered
PRINT year$              'display the text entry
```



# SEE ALSO
* [INPUT](INPUT.md) , [LINE](LINE.md) [INPUT](INPUT.md) (keyboard input)
* [INPUT](INPUT.md) (file mode) , [INPUT](INPUT.md) # , [LINE](LINE.md) [INPUT](INPUT.md) # (file input)
* [OPEN](OPEN.md) , [LOC](LOC.md) (file)
* [LOCATE](LOCATE.md) (cursor on/off)

