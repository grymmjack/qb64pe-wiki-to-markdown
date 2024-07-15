<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DISPLAY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DISPLAY rootpage-DISPLAY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DISPLAY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_DISPLAY</a> statement turns off the automatic display while only displaying the screen changes when called.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_DISPLAY</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>_DISPLAY</b> turns off the auto refresh screen default <a href="AUTODISPLAY" title="AUTODISPLAY">_AUTODISPLAY</a> behavior. Prevents screen flickering.</li>
<li>Call _DISPLAY each time the screen graphics are to be displayed. Place call after the image has been changed.</li>
<li>Re-enable automatic display refreshing by calling <a href="AUTODISPLAY" title="AUTODISPLAY">_AUTODISPLAY</a>. If it isn't re-enabled, things may not be displayed later.</li>
<li>_DISPLAY tells <b>QB64</b> to render all of the hardware <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a> commands loaded into the buffer previously.</li>
<li>The <a href="AUTODISPLAY_(function)" title="AUTODISPLAY (function)">_AUTODISPLAY (function)</a> can be used to detect the current display behavior.</li>
<li><b>QB64</b> can set the graphic rendering order of _SOFTWARE, _HARDWARE, and _GLRENDER with <a href="DISPLAYORDER" title="DISPLAYORDER">_DISPLAYORDER</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Displaying a circle bouncing around the screen.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">12</span>
x = <span style="color:#F580B1;">21</span>: y = <span style="color:#F580B1;">31</span> <span style="color:#919191;">'start position</span>
dx = <span style="color:#F580B1;">3</span>: dy = <span style="color:#F580B1;">3</span> <span style="color:#919191;">'number of pixel moves per loop</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">100</span> <span style="color:#919191;">' set to 100 frames per second</span>
    x = x + dx: y = y + dy
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x &lt; <span style="color:#F580B1;">0</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> x &gt; <span style="color:#F580B1;">640</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dx = -dx <span style="color:#919191;">'limit columns and reverse column direction each side</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> y &lt; <span style="color:#F580B1;">0</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> y &gt; <span style="color:#F580B1;">480</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dy = -dy <span style="color:#919191;">'limit rows and reverse row direction top or bottom</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> px &lt;&gt; x <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> py &lt;&gt; y <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> d = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">20</span>: <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (px, py), d, <span style="color:#F580B1;">0</span>: <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> <span style="color:#919191;">'erase</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> c = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">20</span>: <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (x, y), c, <span style="color:#F580B1;">6</span>: <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> <span style="color:#919191;">'draw new circle at new position</span>
    px = x: py = y <span style="color:#919191;">'save older coordinates to erase older circle next loop</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_DISPLAY</span></a> <span style="color:#919191;">'after new circle is set, show it</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>)
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The loop is set with <a href="LIMIT" title="LIMIT">_LIMIT</a> to 100 frames per second to limit CPU usage and the speed of the ball. Each loop a circle is drawn while the previous one is erased when the coordinates change. _DISPLAY only shows the new circle position once each loop. The <b>_DISPLAY</b> routine eliminates the need for setting <a href="SCREEN" title="SCREEN">SCREEN</a> swap pages, <a href="CLS" title="CLS">CLS</a> and <a href="PCOPY" title="PCOPY">PCOPY</a>. _DISPLAY keeps the image off of the screen until the changes have all completed. Drawing 40 circles every loop helps slow down the ball.</dd></dl>
<p><i>Example 2:</i> <a class="mw-selflink selflink">_DISPLAY</a> must be used to render hardware images placed with <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a> (<b>version 1.000 and up</b>).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> MenuHeight = <span style="color:#F580B1;">200</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>)
<span style="color:#919191;">'SLEEP 1</span>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">20</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">30</span>
    <span style="color:#55FF55;">DisplayMenu</span>
    k = <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> k &lt;&gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> k,
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> k = <span style="color:#F580B1;">32</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> k = <span style="color:#F580B1;">27</span>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">DisplayMenu</span>
    <a href="STATIC" title="STATIC"><span style="color:#4593D8;">STATIC</span></a> init, MS_HW <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> init <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        init = <span style="color:#F580B1;">-1</span>
        MS = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, MenuHeight, <span style="color:#F580B1;">32</span>) <span style="color:#919191;">'MenuScreen image</span>
        D = <a href="DEST_(function)" title="DEST (function)"><span style="color:#4593D8;">_DEST</span></a>: <a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> MS
        <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <span style="color:#F580B1;">&amp;HFFAAAAAA</span> <span style="color:#919191;">'background color gray</span>
        <a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (<span style="color:#F580B1;">20</span>, <span style="color:#F580B1;">2</span>), <span style="color:#FFB100;">"Menu Test"</span> <span style="color:#919191;">'image text</span>
        MS_HW = <a href="COPYIMAGE" title="COPYIMAGE"><span style="color:#4593D8;">_COPYIMAGE</span></a>(MS, <span style="color:#F580B1;">33</span>) <span style="color:#919191;">'create the MenuScreen_HardWare image</span>
        <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> MS
        <a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> D
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)-(<span style="color:#F580B1;">640</span>, MenuHeight), MS_HW
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Notes:</i> When _DISPLAY is commented out, the hardware Menu Test screen portion will blink and key codes may be seen underneath.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DISPLAY_(function)" title="DISPLAY (function)">_DISPLAY (function)</a></li>
<li><a href="DISPLAYORDER" title="DISPLAYORDER">_DISPLAYORDER</a></li>
<li><a href="AUTODISPLAY" title="AUTODISPLAY">_AUTODISPLAY</a>, <a href="AUTODISPLAY_(function)" title="AUTODISPLAY (function)">_AUTODISPLAY (function)</a></li>
<li><a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a></li>
<li><a href="PCOPY" title="PCOPY">PCOPY</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715053753
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.071 seconds
Real time usage: 0.101 seconds
Preprocessor visited node count: 830/1000000
Post‐expand include size: 6228/2097152 bytes
Template argument size: 1597/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 412/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   55.693      1 -total
 15.99%    8.906     53 Template:Text
 11.56%    6.437     55 Template:Cl
  9.63%    5.361      1 Template:PageDescription
  8.86%    4.936      2 Template:CodeStart
  7.09%    3.949      2 Template:CodeEnd
  7.06%    3.934      1 Template:PageExamples
  7.01%    3.903      1 Template:Small
  6.41%    3.567      1 Template:PageNavigation
  5.05%    2.814      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:123-0!canonical and timestamp 20240715053753 and revision id 8313.
 -->
</div>
</div>
</div>
</div>
</body>
</html>