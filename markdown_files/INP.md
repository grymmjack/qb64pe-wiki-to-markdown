<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>INP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INP rootpage-INP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">INP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">INP</a> returns a value from a computer register or port values at a specified physical address.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>i</i> = <a class="mw-selflink selflink">INP</a>(<i>address</i>)</dd></dl>
<p>
</p>
<ul><li><b>QB64 has limited access to registers. VGA memory and registers are emulated.</b></li>
<li>Address can be a decimal or hexadecimal <a href="INTEGER" title="INTEGER">INTEGER</a> value.</li>
<li><a class="mw-selflink selflink">INP</a> reads directly from a register or port address.</li>
<li>It does not require a <a href="DEF_SEG" title="DEF SEG">DEF SEG</a> memory segment address like <a href="PEEK" title="PEEK">PEEK</a> or <a href="POKE" title="POKE">POKE</a> do.</li>
<li>Reads color port intensity settings after <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="OUT" title="OUT">OUT</a> &amp;H3C7, attribute</span> sets the starting attribute read mode.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Reading the current RGB color settings used in a bitmap to an array.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> SCREEN 12
 <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Colors%(47)
 <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> &amp;H3C7, 0 ' set color port for INP reads at attribute 0 to start
 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 47
 Colors%(i) = <a class="mw-selflink selflink"><span style="color:#4593D8;">INP</span></a>(&amp;H3C9) ' moves to next color attribute every 3 loops
 <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Reading the keyboard Scan Codes as an alternative to <a href="INKEY$" title="INKEY$">INKEY$</a>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
    scancode% = <a class="mw-selflink selflink"><span style="color:#4593D8;">INP</span></a>(&amp;H60)
    a$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> ' clears keyboard buffer
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> scancode%;
 <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> scancode% = 1 ' [ESC] keypress exit
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> A simple ping pong game using an array function to read multiple keys for two players.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DEFINT" title="DEFINT"><span style="color:#4593D8;">DEFINT</span></a> A-Z
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> ball%(100)        ' Set aside enough space to hold the ball sprite
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (4, 3), 4, 4
<a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> (4, 3), 12, 4   ' Draw a filled circle and fill for ball
<a href="GET_(graphics_statement)" title="GET (graphics statement)"><span style="color:#4593D8;">GET</span></a> (0, 0)-(8, 7), ball%(0) ' Get the sprite into the Ball% array
begin:
xmin = 10: ymin = 10
xmax = 630: ymax = 470
x = 25: y = 25
dx = 1: dy = 1
LTpos = 50: RTpos = 50
DO: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 100 'adjust higher for faster
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ScanKey%(17) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> LTpos = LTpos - 1
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ScanKey%(31) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> LTpos = LTpos + 1
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ScanKey%(72) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> RTpos = RTpos - 1
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ScanKey%(80) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> RTpos = RTpos + 1
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Player 1 : "; ponescore; " Player 2 : "; ptwoscore
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x &gt; xmax - 15 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y &gt;= RTpos <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y &lt;= RTpos + 100 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
dx = -1
<a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> x &gt; xmax <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
ponescore = ponescore + 1
<a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> begin
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x &lt; xmin + 15 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y &gt;= LTpos <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y &lt;= LTpos + 100 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
dx = 1
<a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> x &lt; xmin <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
ptwoscore = ptwoscore + 1
<a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> begin
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y &gt; ymax - 5 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dy = -1
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y &lt; ymin + 5 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dy = 1
' Display the sprite elsewhere on the screen
x = x + dx
y = y + dy
<a href="PUT_(graphics_statement)" title="PUT (graphics statement)"><span style="color:#4593D8;">PUT</span></a>(x, y), ball%(0)
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (20, LTpos)-(20, LTpos + 100)
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (620, RTpos)-(620, RTpos + 100)
<a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a> 'shows completed screen every call
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> ScanKey%(1)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> ScanKey% (scancode%)
<a href="STATIC" title="STATIC"><span style="color:#4593D8;">STATIC</span></a> Ready%, keyflags%()
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> Ready% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> keyflags%(0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 127): Ready% = -1
i% = <a class="mw-selflink selflink"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>60) 'read keyboard states
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> (i% <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> 128) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> keyflags%(i% <a href="XOR_(boolean)" title="XOR (boolean)"><span style="color:#4593D8;">XOR</span></a> 128) = 0
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> (i% <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> 128) = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> keyflags%(i%) = -1
K$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
ScanKey% = keyflags%(scancode%)
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a> can be used to read multiple keys simultaneously and is the <b>recommended practice</b>.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OUT" title="OUT">OUT</a> <span style="color:#777777;">(write to register)</span>,  <a href="PEEK" title="PEEK">PEEK</a> <span style="color:#777777;">(read memory)</span></li>
<li><a href="INKEY$" title="INKEY$">INKEY$</a>, <a href="KEYHIT" title="KEYHIT">_KEYHIT</a>, <a href="KEYDOWN" title="KEYDOWN">_KEYDOWN</a></li>
<li><a href="Bitmaps" title="Bitmaps">Bitmaps</a>, <a href="Scancodes" title="Scancodes">Scancodes</a> <span style="color:#777777;">(keyboard)</span></li>
<li><a href="Port_Access_Libraries" title="Port Access Libraries">Port Access Libraries</a> <span style="color:#777777;">(COM or LPT registers)</span></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714133211
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.054 seconds
Preprocessor visited node count: 585/1000000
Post‐expand include size: 5040/2097152 bytes
Template argument size: 864/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.962      1 -total
 15.20%    4.404     75 Template:Cl
  8.88%    2.572      4 Template:Text
  8.23%    2.383      1 Template:PageSyntax
  7.14%    2.068      2 Template:Parameter
  7.12%    2.061      1 Template:PageSeeAlso
  6.91%    2.002      1 Template:PageNavigation
  6.70%    1.940      1 Template:InlineCode
  6.43%    1.863      3 Template:CodeStart
  6.32%    1.830      3 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:474-0!canonical and timestamp 20240714133211 and revision id 8986.
 -->
</div>
</div>
</div>
</div>
</body>
</html>