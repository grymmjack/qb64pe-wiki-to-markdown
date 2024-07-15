# _FREEFONT
> The _FREEFONT statement frees a font handle that was created by _LOADFONT .

## SYNTAX
`_FREEFONT ( fontHandle& )`

## DESCRIPTION
* Unloads fonts that are no longer in use or needed in order to free program memory and resources.
* You cannot free a font which is in use. Change the font to a QB64 default font size before freeing the handle (see example below).
* Predefined QB64 font handle numbers can be used before freeing a font: [_FONT](_FONT.md) 8 - default font for [SCREEN](SCREEN.md) 1, 2, 7, 8 or 13 [_FONT](_FONT.md) 14 - default font for [SCREEN](SCREEN.md) 9 or 10 [_FONT](_FONT.md) 16 - default font for [SCREEN](SCREEN.md) 0 ( [WIDTH](WIDTH.md) 80, 25 text only), 11 or 12 [_FONT](_FONT.md) 9, 15 and 17 are the double width versions of 8, 14 and 16 respectively in text [SCREEN](SCREEN.md) 0 .
	* [_FONT](_FONT.md) 8 - default font for [SCREEN](SCREEN.md) 1, 2, 7, 8 or 13
	* [_FONT](_FONT.md) 14 - default font for [SCREEN](SCREEN.md) 9 or 10
	* [_FONT](_FONT.md) 16 - default font for [SCREEN](SCREEN.md) 0 ( [WIDTH](WIDTH.md) 80, 25 text only), 11 or 12
	* [_FONT](_FONT.md) 9, 15 and 17 are the double width versions of 8, 14 and 16 respectively in text [SCREEN](SCREEN.md) 0 .
* [_FONT](_FONT.md) 8 - default font for [SCREEN](SCREEN.md) 1, 2, 7, 8 or 13
* [_FONT](_FONT.md) 14 - default font for [SCREEN](SCREEN.md) 9 or 10
* [_FONT](_FONT.md) 16 - default font for [SCREEN](SCREEN.md) 0 ( [WIDTH](WIDTH.md) 80, 25 text only), 11 or 12
* [_FONT](_FONT.md) 9, 15 and 17 are the double width versions of 8, 14 and 16 respectively in text [SCREEN](SCREEN.md) 0 .
* If the font handle is invalid (equals -1 or 0), an error will occur. Check handle values before using or freeing them.
* You cannot free inbuilt/default QB64 fonts nor do they ever need freed.


## EXAMPLES
> Example 1: Previews and creates a file list of valid MONOSPACE TTF fonts by checking the _LOADFONT handle values.

```vb
SCREEN 12
path$ = "C:\WINDOWS\Fonts\" 'path to the font folder
SHELL _HIDE "DIR /b " + path$ + "\*.ttf > TTFonts.INF"
style$ = "monospace" 'set style to MONOSPACE
OPEN "TTFonts.INF" FOR INPUT AS #1 'list of TTF fonts only
OPEN "TTFMono.INF" FOR OUTPUT AS #2 'will hold list of valid MONOSPACE fonts

DO UNTIL EOF(1): found = found + 1
   LINE INPUT #1, font$
   f& = _LOADFONT(path$ + font$, 30, style$)
   IF f& > 0 THEN 'check for valid handle values > 0
       OK = OK + 1
       PRINT #2, font$
       _FONT f& 'will create error if handle is invalid!
       PRINT "Hello World!"
       PRINT: PRINT: PRINT font$; f&
       PRINT "Press any key."
       K$ = INPUT$(1)
       _FONT 16 'use QB64 default font to free tested font
       _FREEFONT f& 'returns an error if handle <= 0!
       CLS
   END IF
   PRINT
   IF K$ = CHR$(27) THEN EXIT DO
LOOP
CLOSE
PRINT: PRINT: PRINT "Found"; found; "TTF files,"; OK; "can use Monospace,"
END
```

> Example 2: Using a _FREEFONT sub-procedure.

```vb
SCREEN 12
path$ = "C:\WINDOWS\Fonts\" 'path to the font folder
SHELL _HIDE "DIR /b " + path$ + "\*.ttf > TTFonts.INF"
style$ = "monospace" 'set style to MONOSPACE
OPEN "TTFonts.INF" FOR INPUT AS #1 'list of TTF fonts only
OPEN "TTFMono.INF" FOR OUTPUT AS #2 'will hold list of valid MONOSPACE fonts

DO UNTIL EOF(1): found = found + 1
   LINE INPUT #1, font$
   f& = _LOADFONT(path$ + font$, 30, style$)
   IF f& > 0 THEN 'check for valid handle values > 0
       OK = OK + 1
       PRINT #2, font$
       _FONT f& 'will create error if handle is invalid!
       PRINT "Hello World!"
       PRINT: PRINT: PRINT font$; f&
       PRINT "Press any key."
       K$ = INPUT$(1)
       _FONT 16 'use QB64 default font to free tested font
       _FREEFONT f& 'returns an error if handle <= 0!
       CLS
   END IF
   PRINT
   IF K$ = CHR$(27) THEN EXIT DO
LOOP
CLOSE
PRINT: PRINT: PRINT "Found"; found; "TTF files,"; OK; "can use Monospace,"
END
```


```vb
SCREEN 12
path$ = "C:\WINDOWS\Fonts\" 'path to the font folder
SHELL _HIDE "DIR /b " + path$ + "\*.ttf > TTFonts.INF"
style$ = "monospace" 'set style to MONOSPACE
OPEN "TTFonts.INF" FOR INPUT AS #1 'list of TTF fonts only
OPEN "TTFMono.INF" FOR OUTPUT AS #2 'will hold list of valid MONOSPACE fonts

DO UNTIL EOF(1): found = found + 1
   LINE INPUT #1, font$
   f& = _LOADFONT(path$ + font$, 30, style$)
   IF f& > 0 THEN 'check for valid handle values > 0
       OK = OK + 1
       PRINT #2, font$
       _FONT f& 'will create error if handle is invalid!
       PRINT "Hello World!"
       PRINT: PRINT: PRINT font$; f&
       PRINT "Press any key."
       K$ = INPUT$(1)
       _FONT 16 'use QB64 default font to free tested font
       _FREEFONT f& 'returns an error if handle <= 0!
       CLS
   END IF
   PRINT
   IF K$ = CHR$(27) THEN EXIT DO
LOOP
CLOSE
PRINT: PRINT: PRINT "Found"; found; "TTF files,"; OK; "can use Monospace,"
END
```

* [_FONT](_FONT.md)
* [_LOADFONT](_LOADFONT.md)

```vb
SCREEN 12
path$ = "C:\WINDOWS\Fonts\" 'path to the font folder
SHELL _HIDE "DIR /b " + path$ + "\*.ttf > TTFonts.INF"
style$ = "monospace" 'set style to MONOSPACE
OPEN "TTFonts.INF" FOR INPUT AS #1 'list of TTF fonts only
OPEN "TTFMono.INF" FOR OUTPUT AS #2 'will hold list of valid MONOSPACE fonts

DO UNTIL EOF(1): found = found + 1
   LINE INPUT #1, font$
   f& = _LOADFONT(path$ + font$, 30, style$)
   IF f& > 0 THEN 'check for valid handle values > 0
       OK = OK + 1
       PRINT #2, font$
       _FONT f& 'will create error if handle is invalid!
       PRINT "Hello World!"
       PRINT: PRINT: PRINT font$; f&
       PRINT "Press any key."
       K$ = INPUT$(1)
       _FONT 16 'use QB64 default font to free tested font
       _FREEFONT f& 'returns an error if handle <= 0!
       CLS
   END IF
   PRINT
   IF K$ = CHR$(27) THEN EXIT DO
LOOP
CLOSE
PRINT: PRINT: PRINT "Found"; found; "TTF files,"; OK; "can use Monospace,"
END
```



# SEE ALSO
* [_FONT](_FONT.md)
* [_LOADFONT](_LOADFONT.md)

