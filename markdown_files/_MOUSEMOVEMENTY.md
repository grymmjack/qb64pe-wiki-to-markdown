<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MOUSEMOVEMENTY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MOUSEMOVEMENTY rootpage-MOUSEMOVEMENTY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MOUSEMOVEMENTY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MOUSEMOVEMENTY</a> function returns the relative vertical position of the mouse cursor as positive or negative values.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>verticalMove</i> = <a class="mw-selflink selflink">_MOUSEMOVEMENTY</a></dd></dl>
<p>
</p>
<ul><li>Returns the relative vertical cursor pixel position compared to the previous cursor position. Negative values are up moves.</li>
<li><b>Note:</b> A <a href="MOUSESHOW" title="MOUSESHOW">_MOUSESHOW</a> statement will disable <a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a> or <a class="mw-selflink selflink">_MOUSEMOVEMENTY</a> relative mouse movement reads.</li>
<li>Can also be used to check for any mouse movements to enable a program or close <a href="Screen_Saver_Programs" title="Screen Saver Programs">Screen Saver Programs</a>.</li>
<li>Sets the mouse to a relative movement mode which can be read by <a href="WHEEL" title="WHEEL">_WHEEL</a> instead of <a href="AXIS" title="AXIS">_AXIS</a> as mouse <a href="DEVICES" title="DEVICES">device</a> 2.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Since values returned are relative to the last position, the returns can be positive or negative.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">12</span>
PX = <span style="color:#F580B1;">320</span>: PY = <span style="color:#F580B1;">240</span> <span style="color:#919191;">'center position</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">200</span>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
        PX = PX + <a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX"><span style="color:#4593D8;">_MOUSEMOVEMENTX</span></a>
        PY = PY + <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEMOVEMENTY</span></a>
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (PX, PY), <span style="color:#F580B1;">10</span>, <span style="color:#F580B1;">10</span>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">1</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> PX, PY
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>) <span style="color:#919191;">'escape key exit</span>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>MOD is used to keep horizontal movement of the circle and cursor inside of the SCREEN 13 window(320).</dd>
<dd>Note when using the function this way, then give the user a keypress exit option. Make sure the user has some way to exit that is not dependent on clicking the X button.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">13</span>, , <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">0</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">200</span>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
        x = x + <a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX"><span style="color:#4593D8;">_MOUSEMOVEMENTX</span></a>
        y = y + <a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSEMOVEMENTY</span></a>
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
    x = (x + <span style="color:#F580B1;">320</span>) <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> <span style="color:#F580B1;">320</span> <span style="color:#919191;">'keeps object on screen</span>
    y = (y + <span style="color:#F580B1;">200</span>) <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> <span style="color:#F580B1;">200</span> <span style="color:#919191;">'remove if off screen moves are desired</span>
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (x, y), <span style="color:#F580B1;">20</span>
    <a href="PCOPY" title="PCOPY"><span style="color:#4593D8;">PCOPY</span></a> <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">0</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span> <span style="color:#919191;">'press any key to exit</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a></li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>, <a href="MOUSEX" title="MOUSEX">_MOUSEX</a></li>
<li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a></li>
<li><a href="WHEEL" title="WHEEL">_WHEEL</a>, <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a></li>
<li><a href="AXIS" title="AXIS">_AXIS</a>, <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a></li>
<li><a href="MOUSESHOW" title="MOUSESHOW">_MOUSESHOW</a>, <a href="MOUSEHIDE" title="MOUSEHIDE">_MOUSEHIDE</a></li>
<li><a href="Screen_Saver_Programs" title="Screen Saver Programs">Screen Saver Programs</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062413
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.059 seconds
Preprocessor visited node count: 435/1000000
Post‐expand include size: 3526/2097152 bytes
Template argument size: 860/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 118/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   37.173      1 -total
 27.07%   10.064      1 Template:Parameter
 17.57%    6.530     26 Template:Text
 11.26%    4.186      2 Template:CodeEnd
  8.53%    3.172      1 Template:PageExamples
  7.54%    2.804     30 Template:Cl
  5.85%    2.175      1 Template:PageSyntax
  4.79%    1.782      1 Template:PageNavigation
  4.57%    1.697      2 Template:CodeStart
  4.49%    1.668      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:193-0!canonical and timestamp 20240715062413 and revision id 8839.
 -->
</div>
</div>
</div>
</div>
</body>
</html>