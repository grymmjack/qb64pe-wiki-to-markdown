<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LOCATE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LOCATE rootpage-LOCATE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LOCATE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">LOCATE</a> statement locates the screen text row and column positions for a <a href="PRINT" title="PRINT">PRINT</a> or <a href="INPUT" title="INPUT">INPUT</a> procedure.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">LOCATE</a> [<i>row%</i>][, <i>column%</i>] [, <i>cursor%</i>][, <i>cursorStart%</i>, <i>cursorStop%</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>optional text <i>row%</i> <a href="INTEGER" title="INTEGER">INTEGER</a> values are from 1 to 25, 43 or 50 in <a href="SCREEN" title="SCREEN">SCREEN</a> 0 and  25 in most other legacy graphic screen modes, except screens 11 and 12 which can have 30 or 60 rows.</li>
<li>optional <i>column%</i> <a href="INTEGER" title="INTEGER">INTEGER</a> values are from 1 to 40 or 80 in <a href="SCREEN" title="SCREEN">SCREEN</a> 0 and 80 in all other legacy screen modes.</li>
<li>optional <i>cursor%</i> value can be 0 to turn displaying the cursor off or 1 to turn it on.</li>
<li>optional <i>cursorStart%</i> and <i>cursorStop%</i> values define the shape of the cursor by setting the start and stop scanline (values range from 0 to 31) for the cursor character.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a href="WIDTH" title="WIDTH">WIDTH</a> statement can be used to determine the text width and height in <a href="SCREEN" title="SCREEN">SCREEN</a> 0 and height of 30 or 60 in <a href="SCREEN" title="SCREEN">SCREEN</a> 11 or 12.</li>
<li>In <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> graphic screen the number of text <i>rows</i> are calculated as <a href="HEIGHT" title="HEIGHT">_HEIGHT</a> \ 16 except when a <a href="FONT" title="FONT">_FONT</a> is used. Use <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a> to calculate font rows.</li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> graphic screen text <i>columns</i> are calculated as <a href="WIDTH_(function)" title="WIDTH (function)">_WIDTH</a> \ 8 except when a <a href="FONT" title="FONT">_FONT</a> is used. Use <a href="PRINTWIDTH" title="PRINTWIDTH">_PRINTWIDTH</a> to measure a line of font text.
<ul><li>Additionally, when a variable width <a href="FONT" title="FONT">_FONT</a> is active, then the <i>columns</i> are not counted as char positions anymore but as pixel positions instead.</li></ul></li>
<li>The text <i>row</i> position is not required if the <a href="PRINT" title="PRINT">PRINT</a> is going to be on the next row. The <a href="Comma" title="Comma">comma</a> and a <i>column</i> value are required to set the column.</li>
<li>If only the <i>row</i> parameter is given, then the column position remains the same. <b>Neither <i>row</i> or <i>column</i> parameter can be 0.</b></li>
<li>When <a href="PRINT" title="PRINT">PRINTing</a> on the bottom 2 <i>rows</i>, use a <a href="Semicolon" title="Semicolon">semicolon</a> after the PRINT expression to avoid a screen roll.</li>
<li>If the <i>cursorStart%</i> line is given, the <i>cursorStop%</i> line must also be given. A wider range between them produces a taller cursor.</li>
<li>If you use LOCATE beyond the current number of rows in text mode, QB64 will try to adapt the screen instead of tossing an error.</li>
<li>When writing to the console, only the <i>row</i> and <i>column</i> arguments are used, all others are ignored. Furthermore, on non-Windows systems LOCATE statements that do not give both a <i>row</i> and <i>column</i> will be ignored entirely.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Moving the cursor around (now you can finally create a Commodore 64 emulator!). <b>Default SCREEN 0 only:</b>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">crx = <span style="color:#F580B1;">10</span>
cry = <span style="color:#F580B1;">10</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">LOCATE</span></a> cry, crx, <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">8</span>
    a$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
    <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> a$
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">0</span>) + <span style="color:#FFB100;">"H"</span>: <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> cry &gt; <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> cry = cry - <span style="color:#F580B1;">1</span> <span style="color:#919191;">'up</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">0</span>) + <span style="color:#FFB100;">"P"</span>: <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> cry &lt; <span style="color:#F580B1;">25</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> cry = cry + <span style="color:#F580B1;">1</span> <span style="color:#919191;">'down</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">0</span>) + <span style="color:#FFB100;">"K"</span>: <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> crx &gt; <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> crx = crx - <span style="color:#F580B1;">1</span> <span style="color:#919191;">'left</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">0</span>) + <span style="color:#FFB100;">"M"</span>: <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> crx &lt; <span style="color:#F580B1;">80</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> crx = crx + <span style="color:#F580B1;">1</span> <span style="color:#919191;">'right</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>): <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
    <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd>Explanation: The CHR$(0) + "H", "P", "K", "M" represents the cursor arrow keys. start = 0, stop = 8 is the tallest cursor, experiment with the start and stop values for different effects (start = 8, stop = 8 is the default producing a _ cursor).</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1218" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="CSRLIN" title="CSRLIN">CSRLIN</a>, <a href="POS" title="POS">POS</a> <span style="color:#777777;">(cursor position)</span></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="PRINT" title="PRINT">PRINT</a>, <a href="COLOR" title="COLOR">COLOR</a></li>
<li><a href="INPUT" title="INPUT">INPUT</a>, <a href="LINE_INPUT" title="LINE INPUT">LINE INPUT</a>, <a href="INPUT$" title="INPUT$">INPUT$</a> <span style="color:#777777;">(keyboard input)</span></li>
<li><a href="WIDTH" title="WIDTH">WIDTH</a>, <a href="INPUT$" title="INPUT$">INPUT$</a>, <a href="INKEY$" title="INKEY$">INKEY$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715025144
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.047 seconds
Real time usage: 0.071 seconds
Preprocessor visited node count: 464/1000000
Post‐expand include size: 3415/2097152 bytes
Template argument size: 827/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 31/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   36.114      1 -total
 10.81%    3.904     28 Template:Text
 10.10%    3.649     25 Template:Cl
  8.94%    3.229      1 Template:CodeStart
  8.57%    3.095      1 Template:PageSyntax
  8.33%    3.008      1 Template:PageExamples
  8.09%    2.921     12 Template:Parameter
  7.88%    2.846      1 Template:PageDescription
  6.78%    2.449      1 Template:PageParameters
  6.76%    2.441      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:430-0!canonical and timestamp 20240715025144 and revision id 8903.
 -->
</div>
</div>
</div>
</div>
</body>
</html>