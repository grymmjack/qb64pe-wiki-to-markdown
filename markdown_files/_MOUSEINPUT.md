<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MOUSEINPUT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MOUSEINPUT rootpage-MOUSEINPUT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MOUSEINPUT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MOUSEINPUT</a> function is used to monitor any new mouse positions, button presses or movements of the scroll wheel. Must be called before other mouse information becomes available.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>infoExists%%</i> = <a class="mw-selflink selflink">_MOUSEINPUT</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns -1 if new mouse information is available, otherwise it returns 0.</li>
<li>Must be called before reading any of the other mouse functions. The function will not miss any mouse input even during an <a href="INPUT" title="INPUT">INPUT</a> entry.</li>
<li>Use in a loop to monitor the mouse buttons, scroll wheel and coordinate positions.</li>
<li>To clear all previous mouse data, use <a class="mw-selflink selflink">_MOUSEINPUT</a> in a loop until it returns 0.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Mouse coordinate, click and scroll events are returned sequentially inside of a _MOUSEINPUT loop.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">DO
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEINPUT</span></a> '      Check the mouse status
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>, <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>, <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1), <a href="MOUSEWHEEL" title="MOUSEWHEEL"><span style="color:#4593D8;">_MOUSEWHEEL</span></a>
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The latest mouse function status can be read after the loop. <a href="LIMIT" title="LIMIT">_LIMIT</a> and <a href="DELAY" title="DELAY">_DELAY</a> loops will slow returns down.</dd></dl>
<p>
<i>Example 2:</i> How to use a _MOUSEINPUT loop to locate <a href="PSET" title="PSET">PSET</a> positions on a screen using a right mouse button click.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> ' main program loop
  ' your program code
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEINPUT</span></a>'mouse status changes only
    x = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
    y = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x &gt; 0 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> x &lt; 640 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y &gt; 0 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y &lt; 480 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(2) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (x, y), 15
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x, y
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
  ' your program code
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Clearing any mouse data read before or during an <a href="INPUT" title="INPUT">INPUT</a> entry. Press "I" to enter input:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press I to enter input! Press Q to quit"
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
  K$ = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(<a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>)
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1) = -1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "*"    'indicates a mouse click event
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> K$ = "Q" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> K$ = "I" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>                                          'press I to enter text
    <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Click the mouse and enter something: ", entry$   'enter some text
    <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> Clickcheck                                        'clear mouse data
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
Clickcheck:
count = 0
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
  count = count + 1
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> count        'returns the number of loops before mouse data is cleared
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Click the mouse a few times while entering <a href="INPUT" title="INPUT">INPUT</a> text. When Enter is pressed, the number of loops are displayed.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1165" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="MOUSEX" title="MOUSEX">_MOUSEX</a>, <a href="MOUSEY" title="MOUSEY">_MOUSEY</a>, <a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a>, <a href="MOUSEWHEEL" title="MOUSEWHEEL">_MOUSEWHEEL</a></li>
<li><a href="MOUSESHOW" title="MOUSESHOW">_MOUSESHOW</a>, <a href="MOUSEHIDE" title="MOUSEHIDE">_MOUSEHIDE</a>, <a href="MOUSEMOVE" title="MOUSEMOVE">_MOUSEMOVE</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062410
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.044 seconds
Real time usage: 0.052 seconds
Preprocessor visited node count: 486/1000000
Post‐expand include size: 4248/2097152 bytes
Template argument size: 793/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.135      1 -total
 17.40%    3.852     65 Template:Cl
 10.75%    2.379      1 Template:PageSyntax
  9.42%    2.085      1 Template:PageSeeAlso
  8.76%    1.939      1 Template:PageNavigation
  8.58%    1.900      3 Template:CodeEnd
  8.16%    1.807      1 Template:PageExamples
  7.85%    1.737      3 Template:CodeStart
  7.23%    1.600      1 Template:Parameter
  6.54%    1.448      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:190-0!canonical and timestamp 20240715062410 and revision id 8914.
 -->
</div>
</div>
</div>
</div>
</body>
</html>