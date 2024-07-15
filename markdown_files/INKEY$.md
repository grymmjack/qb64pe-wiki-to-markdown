<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>INKEY$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INKEY rootpage-INKEY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">INKEY$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">INKEY$</a> function returns user input as <a href="ASCII" title="ASCII">ASCII</a> <a href="STRING" title="STRING">STRING</a> character(s) from the keyboard buffer.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>keypress$</i> = <a class="mw-selflink selflink">INKEY$</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns <a href="ASCII" title="ASCII">ASCII</a> character string values in upper or lower cases. See: <a href="UCASE$" title="UCASE$">UCASE$</a> and <a href="LCASE$" title="LCASE$">LCASE$</a></li>
<li>Returns "" if no key has been pressed since the last keyboard read.</li>
<li>Some control keys cannot be read by INKEY$ or will return 2 byte <a href="ASCII" title="ASCII">ASCII</a> codes.</li>
<li>INKEY$ can also be used to clear a <a href="SLEEP" title="SLEEP">SLEEP</a> key press or the keyboard buffer in a loop.</li>
<li>Assign the INKEY$ return to a string variable to save the key entry.</li>
<li><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , , 1</span> displays the INKEY$ cursor. Use <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , , 0</span> to turn it off.</li>
<li>To receive input from a <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a> window, use <a href="CINP" title="CINP">_CINP</a>.</li>
<li>Returns can be evaluated as certain <a href="ASCII" title="ASCII">ASCII</a> characters or codes.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">'                                <b>ASCII Keyboard Codes</b>
'
' <b> Esc  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  Sys ScL Pause</b>
'   27 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68  +133 +134   -   -    -
' <b> `~  1!  2@  3#  4$  5%  6^  7&amp;  8*  9(  0) -_ =+ BkSp   Ins Hme PUp   NumL  /   *    -</b>
'  126 33  64  35  36  37  94  38  42  40  41 95 43   8    +82 +71 +73    -    47  42   45
' <i>  96 49  50  51  52  53  54  55  56  57  48 45 61</i>
' <b> Tab Q   W   E   R   T   Y   U   I   O   P  [{  ]}  \|   Del End PDn   7Hme 8/▲  9PU  + </b>
'   9  81  87  69  82  84  89  85  73  79  80 123 125 124  +83 +79 +81   +71  +72  +73  43
' <i>    113 119 101 114 116 121 117 105 111 112  91  93  92                 55   56   57 </i>
' <b> CapL  A   S   D   F   G   H   J   K   L   ;:  '" Enter                4/◄-  5   6/-►</b>
'    -   65  83  68  70  71  72  74  75  76  58  34  13                  +75  +76  +77  <b>E</b>
' <i>       97 115 100 102 103 104 106 107 108  59  39                       52   53   54 </i> <b>n</b>
' <b> Shift  Z   X   C   V   B   N   M   ,&lt;  .&gt;  /?    Shift       ▲        1End 2/▼  3PD  t</b>
'    *    90  88  67  86  66  78  77  60  62  63      *        +72       +79  +80  +81  <b>e</b>
' <i>       122 120  99 118  98 110 109  44  46  47                          49   50   51 </i> <b>r</b>
' <b> Ctrl Win Alt       Spacebar          Alt Win Menu Ctrl   ◄-  ▼   -►   0Ins     .Del </b>
'   *    -   *           32              *   -   -    *    +75 +80 +77   +82       +83  13
'                                                                    <i>     48        46</i>
'
'  <b>    <i>Italics</i> = LCase/NumLock On  * = 2 byte combo only,  + = 2 Byte: CHR$(0) + CHR$(code)</b>
'
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Two_Byte_Combinations">Two Byte Combinations</span></h2>
<ul><li>INKEY$ 2 byte combinations always begin with <a href="CHR$" title="CHR$">CHR$</a>(0). <a href="ASC_(function)" title="ASC (function)">ASC</a> will always read the first byte code as zero.</li>
<li>Read the second byte code using: <b><span style="color:green;">code2 = ASC(press$, 2)</span></b></li></ul>
<p>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">                    <b>Two Byte Characters        Key                 CHR$(0) + "?" </b>
                    CHR$(0) + CHR$(16-50)      [Alt] + letter
                    CHR$(0) + CHR$(59)         [F1]                 ";"
                    CHR$(0) + CHR$(60)         [F2]                 "&lt;"
                    CHR$(0) + CHR$(61)         [F3]                 "="
                    CHR$(0) + CHR$(62)         [F4]                 "&gt;"
                    CHR$(0) + CHR$(63)         [F5]                 "?"
                    CHR$(0) + CHR$(64)         [F6]                 "@"
                    CHR$(0) + CHR$(65)         [F7]                 "A"
                    CHR$(0) + CHR$(66)         [F8]                 "B"
                    CHR$(0) + CHR$(67)         [F9]                 "C"
                    CHR$(0) + CHR$(68)         [F10]                "D"
                    CHR$(0) + CHR$(71)         [Home]               "G"
                    CHR$(0) + CHR$(72)         [↑] Arrow            "H"
                    CHR$(0) + CHR$(73)         [Page Up]            "I"
                    CHR$(0) + CHR$(75)         [←] Arrow            "K"
                    CHR$(0) + CHR$(76)         [5 NumberPad]        "L" (NumLock off in QB64)
                    CHR$(0) + CHR$(77)         [→] Arrow            "M"
                    CHR$(0) + CHR$(79)         [End]                "O"
                    CHR$(0) + CHR$(80)         [↓] Arrow            "P"
                    CHR$(0) + CHR$(81)         [Page Down]          "Q"
                    CHR$(0) + CHR$(82)         [Insert]             "R"
                    CHR$(0) + CHR$(83)         [Delete]             "S"
                    CHR$(0) + CHR$(84-93)      [Shift] + F1-10
                    CHR$(0) + CHR$(94-103)     [Ctrl] + F1-10
                    CHR$(0) + CHR$(104-113)    [Alt] + F1-10
                    CHR$(0) + CHR$(114-119)    [Ctrl] + keypad
                    CHR$(0) + CHR$(120-129)    [Alt] + number
                    CHR$(0) + CHR$(130 or 131) [Alt] + _/- or +/=   "é" or "â"
                    CHR$(0) + CHR$(133)        [F11]                "à"
                    CHR$(0) + CHR$(134)        [F12]                "å"
                    CHR$(0) + CHR$(135)        [Shift] + [F11]      "ç"
                    CHR$(0) + CHR$(136)        [Shift] + [F12]      "ê"
                    CHR$(0) + CHR$(137)        [Ctrl] + [F11]       "ë"
                    CHR$(0) + CHR$(138)        [Ctrl] + [F12]       "è"
                    CHR$(0) + CHR$(139)        [Alt] + [F11]        "ï"
                    CHR$(0) + CHR$(140)        [Alt] + [F12]        "î"
</pre>
</td></tr></tbody></table>
<dl><dd>In <b>QB64</b>, <a href="CVI" title="CVI">CVI</a> can be used to get the <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a> 2-byte code value. Example: <b><span style="color:green;">status = _KEYDOWN(CVI(CHR$(0) + "P"))</span></b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Clearing the keyboard buffer after <a href="SLEEP" title="SLEEP">SLEEP</a> delays for later <a href="INPUT" title="INPUT">INPUT</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press any keyboard typing key to end SLEEP"
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: K$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">INKEY$</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> K$: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> K$ = ""
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> <a href="SLEEP" title="SLEEP">SLEEP</a> key presses will be kept in the keyboard buffer and may be added into an <a href="INPUT" title="INPUT">INPUT</a> later.</dd></dl>
<p>
<i>Example 2:</i> Entering a Ctrl + letter keypress combination will print <a href="ASCII" title="ASCII">ASCII</a> Control characters 1 to 26. .
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">DO
    K$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">INKEY$</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> K$ &lt;&gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> K$; " ";
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> K$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) 'Esc key exit
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The above code will print Esc arrow, Backspace symbol, and 2 byte characters led by CHR$(0) in addition to normal keys.</dd></dl>
<p>
<i>Example 3:</i> Use <a href="UCASE$" title="UCASE$">UCASE$</a>(INKEY$) in a keyboard read loop looking for uppercase "Y" or "N" user inputs to avoid multiple IF statements.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Do you want to continue? (Y/N): ";  'semicolon saves position for user entry
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>: K$ = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">INKEY$</span></a>) 'change any user key press to uppercase
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> K$ = "Y" <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> K$ = "N"
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> K$  'print valid user entry
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> K$ = "N" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 4:</i> Getting just number values entered by a user in an INKEY$ input loop.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Enter a number value: ";
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
  K$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">INKEY$</span></a>
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> K$ &gt;= <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(48) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> K$ &lt;= <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(57) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> entry$ = entry$ + K$ ' numbers only
  L = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(entry$) ' check entry length for possible backspace
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> K$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(46) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> flag = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> entry$ = entry$ + K$: flag = 1: mark = L ' decimal point
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> K$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(8) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> L &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ' backspace pressed and entry has a length
    entry$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(entry$, 1, L - 1) ' remove one character from entry$
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(entry$) &lt; mark <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> flag = 0 ' allow decimal point entry if other was removed.
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a>, <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(0) - 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(1); ' remove end character from screen
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 32: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> entry$; ' display entry to user (semicolon required for correct <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>)
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> K$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(13) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> L &gt; 0 'assures something is entered
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> <a href="SLEEP" title="SLEEP">SLEEP</a> waits for a keypress. It also allows background programs to share the processor and it leaves the keypress in the buffer for INKEY$. Keyboard string number characters range from <a href="ASCII" title="ASCII">ASCII</a> codes 48 to 57. Any other entry is ignored by the IF statement. A decimal point (code 46) entry is allowed once in the input. The flag value stops further decimal point additions. Backspacing (code 8) is also allowed if the entry has at least one character. The cursor column returned by <a href="POS" title="POS">POS</a>(0) reverts too after the end of the entry when printed each loop. The loop exits when [Enter] (code 13) is pressed and the entry has a length.</dd></dl>
<p>
<i>Example 5:</i> Using arrow keys to move a text character. A change from a previous position tells program when to PRINT:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">movey = 1: movex = 1 'text coordinates can never be 0
at$ = "@"  'text sprite could be almost any ASCII character
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> movey, movex: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> at$;
DO
    px = movex: py = movey 'previous positions
    B$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">INKEY$</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> B$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(72) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> movey &gt; 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> movey = movey - 1 'rows 1 to 23 only
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> B$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(80) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> movey &lt; 23 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> movey = movey + 1
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> B$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(75) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> movex &gt; 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> movex = movex - 1 'columns 1 to 80 only
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> B$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(77) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> movex &lt; 80 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> movex = movex + 1
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> px &lt;&gt; movex <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> py &lt;&gt; movey <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> 'only changes when needed
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> py, px: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(1); 'erase old sprite
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> movey, movex: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> at$; 'show new position
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> B$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) 'ESCape key exit
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 6:</i> Using INKEY$ with the arrow or WASD keys to move the QB64 bee image sprite with <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a>:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> image <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Keypress <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 32)
x = 0
y = 0
image = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("QB64bee.png") 'Here I actually used the QB64 icon
DO
  <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (x, y), image
  DO
    Keypress = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">INKEY$</span></a>)
    ' ***** The following line detects the arrow keys *****
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Keypress) &gt; 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> Keypress = <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(Keypress, 1)
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> Keypress &gt; ""
  <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> ' blank screen after valid key press to avoid smearing image on page
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> Keypress
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "W", "H": y = y - 10 'Up
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "A", "K": x = x - 10 'Left
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "S", "P": y = y + 10 'Down
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "D", "M": x = x + 10 'Right
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "Q", <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27): <a href="END" title="END"><span style="color:#4593D8;">END</span></a> 'Q or Esc Ends prog.
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (x, y), image
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The image can be placed off of the screen without error. The image moves 10 pixels to move faster. <a href="CLS" title="CLS">CLS</a> eliminates any background.</dd></dl>
<p>
<i>Example 7:</i> Creating upper <a href="ASCII" title="ASCII">ASCII</a> characters in a QB program using <b>Alt +</b> three number keys:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">DO
    A$ = "": <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> A$ = "": A$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">INKEY$</span></a>: <a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(A$) = 2 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> '2 byte INKEY$ return
        B$ = <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(A$, 1)  'read second byte
        b% = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(B$)        'read second byte code
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> b% &gt; 119 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> b% &lt; 130 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ' Alt + number codes only
           C% = b% - 119  ' convert to actual number
           <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> C% &gt; 9 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> C% = 0
           num$ = num$ + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(C%))
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(num$) = 3  ' 3 digit codes only
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> num$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(num$)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 155 ¢ </pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Hold down Alt key and press 3 keyboard code number keys. <b>Number pad keys may not work.</b> Note that <a class="mw-selflink selflink">INKEY$</a> cannot read Alt, Ctrl or Shift key presses without a key combination and the return is CHR$(0) + CHR$(code).</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1229" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="KEYHIT" title="KEYHIT">_KEYHIT</a>, <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a>, <a href="MAPUNICODE" title="MAPUNICODE">_MAPUNICODE</a></li>
<li><a href="KEYCLEAR" title="KEYCLEAR">_KEYCLEAR</a></li>
<li><a href="INPUT" title="INPUT">INPUT</a>, <a href="LINE_INPUT" title="LINE INPUT">LINE INPUT</a></li>
<li><a href="INPUT$" title="INPUT$">INPUT$</a>, <a href="INP" title="INP">INP</a></li>
<li><a href="CHR$" title="CHR$">CHR$</a>, <a href="ASCII" title="ASCII">ASCII</a></li>
<li><a href="ASC_(function)" title="ASC (function)">ASC (function)</a>, <a href="Scancodes" title="Scancodes">Scancodes</a> (keyboard)</li>
<li><a href="Windows_Libraries#Hot_Keys_(maximize)" title="Windows Libraries">Windows hot keys</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031613
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.078 seconds
Real time usage: 0.102 seconds
Preprocessor visited node count: 1254/1000000
Post‐expand include size: 10377/2097152 bytes
Template argument size: 1795/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   59.075      1 -total
 14.75%    8.712    161 Template:Cl
 11.71%    6.919      1 Template:OutputEnd
  6.54%    3.861      1 Template:PageExamples
  4.34%    2.565      2 Template:InlineCodeEnd
  4.08%    2.410      1 Template:PageSyntax
  4.00%    2.364      1 Template:PageDescription
  3.80%    2.245      7 Template:CodeEnd
  3.77%    2.225      7 Template:CodeStart
  3.67%    2.166      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:378-0!canonical and timestamp 20240715031613 and revision id 8905.
 -->
</div>
</div>
</div>
</div>
</body>
</html>