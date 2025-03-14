<style type="text/css">
body {
    background: #00a !important;
    color: #ccc !important;
}
li {
    list-style-type: square !important;
    color: #ccc !important;
}
li::marker {
    color: #77f !important;
}    
hr {
    border-color: #55f !important;
    border-width: 2px !important;
}
h2 {
    color: #fff !important;
    border: 0 !important;
}
h3 {
    color: #cfc !important;
    border: 0 !important;
}
h4 {
    color: #ccc !important;
    border: 0 !important;
}
h5 {
    margin: 0 0 0.5em 0  !important;
    color: #88f !important;
    border: 0 !important;
    font-style: italic !important;
    font-weight: normal !important;
}
code {
    background: #000 !important;
    margin: 0 !important;
    padding: 8px !important;
    border-radius: 4px !important; 
    border: 1px solid #333 !important;
}
pre > code {
    background: transparent !important;
    margin: 0 !important;
    padding: 0 !important;
    border-radius: inherit !important; 
    border: 0 !important;
}
blockquote {
    border: 0 !important;
    background: transparent !important;
    margin: 0 !important;
    padding: 0 1em !important;
}
pre {
    border-radius: 4px !important;
    background: #000 !important;
    border: 1px solid #333 !important;
    margin: 0 !important;
}
a:link, a:visited, a:hover, a:active {
    color: #ff0 !important;
}
br + pre {
    border-radius: 0 !important;
    border-style: inset !important;
    border-width: 5px !important;
    border-color: #999 !important;
    background-color: #000 !important;
    box-shadow: 0px 10px 3px rgba(0, 0, 0, 0.25) !important;
    margin-top: -1em !important;
}
br + pre::before {
    content: "OUTPUT \A" !important;
    color: #555 !important;
    border-bottom: 1px solid #333;
    font-size: x-small;
    display: block !important;
    padding: 0 3px !important;
    margin: -1em -1em 1em -1em !important;
    -webkit-user-select: none; /* Safari */
    -ms-user-select: none; /* IE 10 and IE 11 */
    user-select: none; /* Standard syntax */    
}
br ~ h5 {
    margin-top: 2em !important;
}
.explanation {
    color: #995 !important;
    /* background-color: rgba(150, 150, 100) !important; */
    border-radius: 10em !important;
    border: 2px #441 dashed !important;
    padding: 8px 32px !important;
    margin-bottom: 4em !important;
    font-size: x-small !important;
}
</style>


## [LOCATE](LOCATE.md) [📖](https://qb64phoenix.com/qb64wiki/index.php/LOCATE)
---
<blockquote>

### The LOCATE statement locates the screen text row and column positions for a PRINT or INPUT procedure.

</blockquote>

#### SYNTAX

<blockquote>

`LOCATE [ row% ][, column% ] [, cursor% ][, cursorStart% , cursorStop% ]`

</blockquote>

#### PARAMETERS

<blockquote>


* optional text row% [INTEGER](INTEGER.md) values are from 1 to 25, 43 or 50 in [SCREEN](SCREEN.md) 0 and  25 in most other legacy graphic screen modes, except screens 11 and 12 which can have 30 or 60 rows.
* optional column% [INTEGER](INTEGER.md) values are from 1 to 40 or 80 in [SCREEN](SCREEN.md) 0 and 80 in all other legacy screen modes.
* optional cursor% value can be 0 to turn displaying the cursor off or 1 to turn it on.
* optional cursorStart% and cursorStop% values define the shape of the cursor by setting the start and stop scanline (values range from 0 to 31) for the cursor character.
</blockquote>

#### DESCRIPTION

<blockquote>


* [WIDTH](WIDTH.md) statement can be used to determine the text width and height in [SCREEN](SCREEN.md) 0 and height of 30 or 60 in [SCREEN](SCREEN.md) 11 or 12.
* In _NEWIMAGE graphic screen the number of text rows are calculated as _HEIGHT \ 16 except when a _FONT is used. Use _FONTHEIGHT to calculate font rows.
* _NEWIMAGE graphic screen text columns are calculated as _WIDTH \ 8 except when a _FONT is used. Use _PRINTWIDTH to measure a line of font text.
* Additionally, when a variable width _FONT is active, then the columns are not counted as char positions anymore but as pixel positions instead.
* The text row position is not required if the [PRINT](PRINT.md) is going to be on the next row. The comma and a column value are required to set the column.
* If only the row parameter is given, then the column position remains the same. Neither row or column parameter can be 0.
* When PRINTing on the bottom 2 rows , use a semicolon after the [PRINT](PRINT.md) expression to avoid a screen roll.
* If the cursorStart% line is given, the cursorStop% line must also be given. A wider range between them produces a taller cursor.
* If you use [LOCATE](LOCATE.md) beyond the current number of rows in text mode, QB64 will try to adapt the screen instead of tossing an error.
* When writing to the console, only the row and column arguments are used, all others are ignored. Furthermore, on non-Windows systems [LOCATE](LOCATE.md) statements that do not give both a row and column will be ignored entirely.

</blockquote>

#### EXAMPLES

<blockquote>



##### Example: Moving the cursor around (now you can finally create a Commodore 64 emulator!). Default SCREEN 0 only:
```vb
crx = 10
cry = 10
DO
   LOCATE cry, crx, 1, 0, 8
   a$ = INKEY$
   SELECT CASE a$
       CASE CHR$(0) + "H": IF cry > 1 THEN cry = cry - 1 'up
       CASE CHR$(0) + "P": IF cry < 25 THEN cry = cry + 1 'down
       CASE CHR$(0) + "K": IF crx > 1 THEN crx = crx - 1 'left
       CASE CHR$(0) + "M": IF crx < 80 THEN crx = crx + 1 'right
       CASE CHR$(27): END
   END SELECT
LOOP
```
  
<br>


</blockquote>

#### SEE ALSO

<blockquote>


* Featured in our "Keyword of the Day" series
* [CSRLIN](CSRLIN.md) , [POS](POS.md) (cursor position)
* [SCREEN](SCREEN.md) , [PRINT](PRINT.md) , [COLOR](COLOR.md)
* [INPUT](INPUT.md) , [LINE](LINE.md) [INPUT](INPUT.md) , [INPUT\$](INPUT\$.md) (keyboard input)
* [WIDTH](WIDTH.md) , [INPUT\$](INPUT\$.md) , [INKEY\$](INKEY\$.md)
</blockquote>
