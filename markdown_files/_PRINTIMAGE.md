<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_PRINTIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PRINTIMAGE rootpage-PRINTIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_PRINTIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_PRINTIMAGE</a> statement prints a colored image on the printer, stretching it to full paper size first.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_PRINTIMAGE</a> <i>imageHandle&amp;</i></dd></dl>
<p>
</p>
<ul><li><i>imageHandle&amp;</i> is created by the <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> or <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a> functions.</li>
<li>Use a white background to save ink. <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255)</span> can be used to set the white background in any <a href="SCREEN" title="SCREEN">SCREEN</a> mode.</li>
<li>The image may be stretched disproportionately using normal screen sizes. To compensate, use a <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> screen that is proportional to the paper size. <i>e.g.</i> A 640 X 900 SCREEN page is roughly the same as 3 times a 210mm X 297mm paper size.</li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> or graphic screen pages can use <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a> to print different sized text <a href="FONT" title="FONT">_FONTs</a>.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Shows how to transfer custom font text on screen pages to the printer in Windows. Change the font path for other OS's.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">PageScale = 10
PageHeight = 297 * PageScale 'A4 paper size is 210 X 297 mm
PageWidth = 210 * PageScale
Page&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(PageWidth, PageHeight, 32)
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> Page&amp;: <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255): <a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> 0  'make background white to save ink!
CursorPosY = 0
'example text to print
PointSize = 12
text$ = "The rain in Spain falls mainly on the plain."
<a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> PrintText
PointSize = 50
text$ = "BUT!"
<a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> PrintText
PointSize = 12
text$ = "In Hartford, Hereford, and Hampshire, hurricanes hardly happen."
<a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> PrintText
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Preview (Y/N)?", i$                      'print preview of screen (optional)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(i$) = "Y" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  Prev&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(600, 900, 32)               'print preview smaller image
  <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , Page&amp;, Prev&amp;
  <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> Prev&amp;
  DO: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
  <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 0
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Print on printer (Y/N)?", i$             'print screen page on printer
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(i$) = "Y" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  <a class="mw-selflink selflink"><span style="color:#4593D8;">_PRINTIMAGE</span></a> Page&amp;
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
PrintText:
FontHeight = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(PointSize * 0.3527 * PageScale)
FontHandle = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>("c:\windows\fonts\times.ttf", FontHeight)
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> Page&amp;
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> FontHandle
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 0, 0), <a href="RGBA" title="RGBA"><span style="color:#4593D8;">_RGBA</span></a>(0, 0, 0, 0)        'RED text on clear black background
<a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (0, CursorPosY), text$
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> 16                               'change to the QB64 default font to free it
<a href="FREEFONT" title="FREEFONT"><span style="color:#4593D8;">_FREEFONT</span></a> FontHandle
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> 0
CursorPosY = CursorPosY + FontHeight            'adjust print position down
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> CLS with the color white makes sure that the background is not printed a color. The PrintText <a href="GOSUB" title="GOSUB">GOSUB</a> sets the <a href="COLOR" title="COLOR">COLOR</a> of the text to red with a transparent background using <a href="RGBA" title="RGBA">_RGBA</a> to set the <a href="ALPHA" title="ALPHA">_ALPHA</a> transparency to zero or clear black.</dd></dl>
<p>
<i>Example 2:</i> Printing an old SCREEN 12 <a href="ASCII" title="ASCII">ASCII</a> table using a deeper sized page to prevent stretching by <a class="mw-selflink selflink">_PRINTIMAGE</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> "Print Preview ASCII Table"
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 900, 256)  'size is proportional to 210mm X 297mm(8-1/2 X 11) paper
<a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C8, 0: <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, 63: <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, 63: <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9, 63 'white background saves ink!
Align 8, 2, "ASCII and Extended Character Code Table using <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(n%)"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(80, 223)
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 40
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> " ";
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i% = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 13
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i%;: SetCHR <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a>, <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(0), 40, i%
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a>, <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(0) + 1
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i%
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i% = 14 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 16
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i%; <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(i%);
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a> + 1, 2
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 17 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 27
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i; <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(i);
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i% = 28 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 31
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i%;: SetCHR <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a>, <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(0), 40, i%
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a>, <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(0) + 1
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i%
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a> + 1, 2
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 2: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> 32; <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(32);
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i% = 33 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 255
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> i%
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 45, 58, 71, 84: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a> + 1, 1
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a class="mw-redirect" href="IS" title="IS"><span style="color:#4593D8;">IS</span></a> &gt; 96: <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> (i% - 97) <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 11 = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <a href="CSRLIN" title="CSRLIN"><span style="color:#4593D8;">CSRLIN</span></a> + 1, 1
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> i%
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 48 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 57: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 9 'denotes number keys 48 to 57
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 65 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 90: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 5 ' A to Z keys 65 to 90
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 97 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 122: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 36 'a to z keys 97 to 122
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 127 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 175: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 42
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 176 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 223: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 6 'drawing characters 176 to 223
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a class="mw-redirect" href="IS" title="IS"><span style="color:#4593D8;">IS</span></a> &gt; 223: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 42
    <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 2
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> i% = 98 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> i% = 99 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> i% = 100 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(1);
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> " "; i%; <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(i%);
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i%
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 3: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "= NBSP(Non-Breaking Space)"
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 8: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(80, <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(220))
Border 8
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 4: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 27, 4: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "7) BELL, 8) Backspace, 9) Tab, 10) LineFeed(printer), 12) FormFeed(printer)"
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 28, 4: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "  13) Return, 26) End Of File, 27) Escape  30) Line up, 31) Line down "
Align 13, 29, "Press Ctrl + P to PRINT!"
DO: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: K$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> K$ &lt;&gt; ""
Align 13, 29, <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(50)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> K$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(16) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  <a class="mw-selflink selflink"><span style="color:#4593D8;">_PRINTIMAGE</span></a> 0              '&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; to PRINTER
  Align 11, 29, "Use the ASCII Table for a reference of the codes!"
  <a href="SOUND" title="SOUND"><span style="color:#4593D8;">SOUND</span></a> 700, 4
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> Align (Tclr, Trow, txt$)
Tcol = 41 - (<a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(txt$) \ 2)
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> Tclr: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> Trow, Tcol: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> txt$;
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> Border (clr%)
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> clr%
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> row = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 30
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> row, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(179);
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> row, 80: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(179);
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> row
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(80, 196);
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 30, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(80, 196);
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(218);
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 80: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(191);
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 30, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(192);
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 30, 80: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(217);
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> SetCHR (Trow, Tcol, FG, ASCode)
Srow = 16 * (Trow - 1): Scol = 8 * (Tcol - 1) 'convert text to graphic coordinates
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> FG: <a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (Scol, Srow), <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(ASCode)
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <a href="ASCII" title="ASCII">ASCII</a> character table was originally made in <a href="SCREEN" title="SCREEN">SCREEN</a> 12 (640 X 480) and was adapted to 256 colors.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a></li>
<li><a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a>, <a href="SAVEIMAGE" title="SAVEIMAGE">_SAVEIMAGE</a></li>
<li><a href="LPRINT" title="LPRINT">LPRINT</a></li>
<li><a href="Windows_Printer_Settings" title="Windows Printer Settings">Windows Printer Settings</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192832
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.096 seconds
Real time usage: 0.108 seconds
Preprocessor visited node count: 1458/1000000
Post‐expand include size: 11542/2097152 bytes
Template argument size: 2129/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   52.611      1 -total
 25.94%   13.648    202 Template:Cl
  5.57%    2.928      1 Template:PageSyntax
  5.44%    2.863      1 Template:PageSeeAlso
  5.16%    2.714      2 Template:CodeEnd
  4.78%    2.514      1 Template:PageNavigation
  4.62%    2.432      2 Template:Small
  4.57%    2.403      1 Template:PageExamples
  4.53%    2.381      1 Template:InlineCodeEnd
  4.47%    2.353      2 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:249-0!canonical and timestamp 20240714192832 and revision id 8687.
 -->
</div>
</div>
</div>
</div>
</body>
</html>