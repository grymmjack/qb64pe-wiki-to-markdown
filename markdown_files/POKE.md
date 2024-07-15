# POKE
> The POKE statement sets the value of a specified memory address offset. QB64 currently has limited access!

## SYNTAX
`POKE segment_offset , offset_value`

## DESCRIPTION
* Writes a value to the segment_offset address in memory.
* [POKE](POKE.md) can only be used to set a value from 0 to 255 (one byte).
* A segment should be defined using [DEF](DEF.md) [SEG](SEG.md) , if you don't define a segment QBasic's ordinary segment will be used.
* [POKE](POKE.md) sends byte values to memory areas. It does not directly access registers.
* Important [SCREEN](SCREEN.md) segments using [PEEK](PEEK.md) and [POKE](POKE.md) include &HB800 (text segment) and &HA000 (graphics segment).
* [DEF](DEF.md) [SEG](SEG.md) should always be used to reset the default segment when access to other memory is no longer necessary.
* [POKE](POKE.md) is safer to use than [OUT](OUT.md) which could damage a PC register.
* Warning: [DEF](DEF.md) [SEG](SEG.md), [VARSEG](VARSEG.md) , [VARPTR](VARPTR.md), [PEEK](PEEK.md) or [POKE](POKE.md) access QB64's emulated 16 bit conventional memory block!


## EXAMPLES
> Example 2: A small PEEK and POKE fractal program.

```vb
DEF SEG = 0
oldsetting% = PEEK(1047)
POKE 1047,PEEK(1047) OR 16 ' ENABLES SCROLL LOCK
POKE 1047,PEEK(1047) OR 32 ' ENABLES NUMBER LOCK
POKE 1047,PEEK(1047) OR 64 ' ENABLES CAPS LOCK
POKE 1047,PEEK(1047) OR 128 ' ENABLES INSERT MODE
DEF SEG
```

> Example 3: Highlighting a row of text in Screen 0

```vb
DEF SEG = 0
oldsetting% = PEEK(1047)
POKE 1047,PEEK(1047) OR 16 ' ENABLES SCROLL LOCK
POKE 1047,PEEK(1047) OR 32 ' ENABLES NUMBER LOCK
POKE 1047,PEEK(1047) OR 64 ' ENABLES CAPS LOCK
POKE 1047,PEEK(1047) OR 128 ' ENABLES INSERT MODE
DEF SEG
```

* SelectScreen

```vb
DEF SEG = 0
oldsetting% = PEEK(1047)
POKE 1047,PEEK(1047) OR 16 ' ENABLES SCROLL LOCK
POKE 1047,PEEK(1047) OR 32 ' ENABLES NUMBER LOCK
POKE 1047,PEEK(1047) OR 64 ' ENABLES CAPS LOCK
POKE 1047,PEEK(1047) OR 128 ' ENABLES INSERT MODE
DEF SEG
```

* [DEF](DEF.md) [SEG](SEG.md) , [DEF](DEF.md) [SEG](SEG.md) = 0
* [PEEK](PEEK.md) , [OUT](OUT.md)
* [VARSEG](VARSEG.md) , [VARPTR](VARPTR.md)
* [_MEMGET](_MEMGET.md) (function) , [_MEMPUT](_MEMPUT.md)
* Scancodes , Screen Memory
* [PEEK](PEEK.md) and [POKE](POKE.md) Library

```vb
DEF SEG = 0
oldsetting% = PEEK(1047)
POKE 1047,PEEK(1047) OR 16 ' ENABLES SCROLL LOCK
POKE 1047,PEEK(1047) OR 32 ' ENABLES NUMBER LOCK
POKE 1047,PEEK(1047) OR 64 ' ENABLES CAPS LOCK
POKE 1047,PEEK(1047) OR 128 ' ENABLES INSERT MODE
DEF SEG
```



# SEE ALSO
* [DEF](DEF.md) [SEG](SEG.md) , [DEF](DEF.md) [SEG](SEG.md) = 0
* [PEEK](PEEK.md) , [OUT](OUT.md)
* [VARSEG](VARSEG.md) , [VARPTR](VARPTR.md)
* [_MEMGET](_MEMGET.md) (function) , [_MEMPUT](_MEMPUT.md)
* Scancodes , Screen Memory
* [PEEK](PEEK.md) and [POKE](POKE.md) Library

