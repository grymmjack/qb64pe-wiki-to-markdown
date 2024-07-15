# _LOADFONT
> The _LOADFONT function loads a FreeType supported font file in a specific size and style and returns a LONG font handle.

## SYNTAX
`handle& = _LOADFONT ( fontFileName$ , size& [, "{MONOSPACE|, BOLD|, ITALIC|, UNDERLINE|, UNICODE|, DONTBLEND|, MEMORY|, AUTOMONO}"][, fontIndex& ])`

## DESCRIPTION
* The assigned [LONG](LONG.md) font handle& variable return value designates a font style to be used somewhere in a program. Valid handle values are greater than 0 ( handle& > 0 ).
* fontFileName$ is the filename of a font. It can include the path to the font file. TTF, TTC, OTF, FNT, FON, PCF and BDF font file formats are supported. Best practice is to include font files with a program.
* If no path is specified for fontFileName$ and the font file isn't in the same folder as the resulting binary, QB64 attempts to load from the default %SystemRoot%\Fonts path. Similar known locations are searched in other operating systems.
* size& is the [INTEGER](INTEGER.md) height of the font. If the size is too large or small an error will occur.
* Optional comma separated style parameter(s) used are literal STRINGs (in quotes) or can be contained in variable(s). "MONOSPACE" loads a font with all characters occupying the same width. Results may be too spaced out for fonts that aren't designed for monospace use. "BOLD", "ITALIC" or "UNDERLINE" create bold, italic or underlined fonts when available in font. (valid for QB64 versions prior to 1.000). For QB64 1.000 or later , you must specify the proper file name according to the desired attributes. For example, Courier New is in font cour.ttf while Courier New Bold is in font courbd.ttf , as shipped with Windows. "UNICODE" loads Unicode fonts such as cyberbit.ttf which is included in the QB64 downloads. "DONTBLEND" turns off [_ALPHA](_ALPHA.md) blending of fonts. This can also be done with the [_DONTBLEND](_DONTBLEND.md) statement. "MEMORY" will treat fontFileName$ as a memory buffer containing the font file instead of a file name. "AUTOMONO" will automatically detect monospace fonts and set the "MONOSPACE" flag if fontFileName$ is monospaced.
	* "MONOSPACE" loads a font with all characters occupying the same width. Results may be too spaced out for fonts that aren't designed for monospace use.
	* "BOLD", "ITALIC" or "UNDERLINE" create bold, italic or underlined fonts when available in font. (valid for QB64 versions prior to 1.000). For QB64 1.000 or later , you must specify the proper file name according to the desired attributes. For example, Courier New is in font cour.ttf while Courier New Bold is in font courbd.ttf , as shipped with Windows.
		* (valid for QB64 versions prior to 1.000).
		* For QB64 1.000 or later , you must specify the proper file name according to the desired attributes. For example, Courier New is in font cour.ttf while Courier New Bold is in font courbd.ttf , as shipped with Windows.
	* "UNICODE" loads Unicode fonts such as cyberbit.ttf which is included in the QB64 downloads.
	* "DONTBLEND" turns off [_ALPHA](_ALPHA.md) blending of fonts. This can also be done with the [_DONTBLEND](_DONTBLEND.md) statement.
	* "MEMORY" will treat fontFileName$ as a memory buffer containing the font file instead of a file name.
	* "AUTOMONO" will automatically detect monospace fonts and set the "MONOSPACE" flag if fontFileName$ is monospaced.
* "MONOSPACE" loads a font with all characters occupying the same width. Results may be too spaced out for fonts that aren't designed for monospace use.
* "BOLD", "ITALIC" or "UNDERLINE" create bold, italic or underlined fonts when available in font. (valid for QB64 versions prior to 1.000). For QB64 1.000 or later , you must specify the proper file name according to the desired attributes. For example, Courier New is in font cour.ttf while Courier New Bold is in font courbd.ttf , as shipped with Windows.
	* (valid for QB64 versions prior to 1.000).
	* For QB64 1.000 or later , you must specify the proper file name according to the desired attributes. For example, Courier New is in font cour.ttf while Courier New Bold is in font courbd.ttf , as shipped with Windows.
* (valid for QB64 versions prior to 1.000).
* For QB64 1.000 or later , you must specify the proper file name according to the desired attributes. For example, Courier New is in font cour.ttf while Courier New Bold is in font courbd.ttf , as shipped with Windows.
* "UNICODE" loads Unicode fonts such as cyberbit.ttf which is included in the QB64 downloads.
* "DONTBLEND" turns off [_ALPHA](_ALPHA.md) blending of fonts. This can also be done with the [_DONTBLEND](_DONTBLEND.md) statement.
* "MEMORY" will treat fontFileName$ as a memory buffer containing the font file instead of a file name.
* "AUTOMONO" will automatically detect monospace fonts and set the "MONOSPACE" flag if fontFileName$ is monospaced.


## EXAMPLES
> Note: 30 means each row of text (including vertical spacing) will be exactly 30 pixels high. This may make some program screens larger. If you don't want a style listed just use style$ = "" if using a STRING variable for different calls.

```vb
rootpath$ = ENVIRON$("SYSTEMROOT") 'normally "C:\WINDOWS"
fontfile$ = rootpath$ + "\Fonts\cour.ttf" 'TTF file in Windows
style$ = "monospace" 'font style is not case sensitive
f& = _LOADFONT(fontfile$, 30, style$)
_FONT f&
PRINT "Hello!"
```


```vb
rootpath$ = ENVIRON$("SYSTEMROOT") 'normally "C:\WINDOWS"
fontfile$ = rootpath$ + "\Fonts\cour.ttf" 'TTF file in Windows
style$ = "monospace" 'font style is not case sensitive
f& = _LOADFONT(fontfile$, 30, style$)
_FONT f&
PRINT "Hello!"
```

* [_FONT](_FONT.md) , [_FONT](_FONT.md) (function)
* [_FREEFONT](_FREEFONT.md)
* [_PRINTSTRING](_PRINTSTRING.md) , [_PRINTWIDTH](_PRINTWIDTH.md)
* [_PRINTMODE](_PRINTMODE.md) , [_PRINTMODE](_PRINTMODE.md) (function)
* [_FONTHEIGHT](_FONTHEIGHT.md) , [_FONTWIDTH](_FONTWIDTH.md)
* Text Using Graphics (Demo)
* Windows Font Dialog Box

```vb
rootpath$ = ENVIRON$("SYSTEMROOT") 'normally "C:\WINDOWS"
fontfile$ = rootpath$ + "\Fonts\cour.ttf" 'TTF file in Windows
style$ = "monospace" 'font style is not case sensitive
f& = _LOADFONT(fontfile$, 30, style$)
_FONT f&
PRINT "Hello!"
```



# SEE ALSO
* [_FONT](_FONT.md) , [_FONT](_FONT.md) (function)
* [_FREEFONT](_FREEFONT.md)
* [_PRINTSTRING](_PRINTSTRING.md) , [_PRINTWIDTH](_PRINTWIDTH.md)
* [_PRINTMODE](_PRINTMODE.md) , [_PRINTMODE](_PRINTMODE.md) (function)
* [_FONTHEIGHT](_FONTHEIGHT.md) , [_FONTWIDTH](_FONTWIDTH.md)
* Text Using Graphics (Demo)
* Windows Font Dialog Box

