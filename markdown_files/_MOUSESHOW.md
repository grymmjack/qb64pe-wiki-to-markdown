<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MOUSESHOW - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MOUSESHOW rootpage-MOUSESHOW skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MOUSESHOW</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MOUSESHOW</a> statement displays the mouse cursor and can change its shape.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_MOUSESHOW</a> [<i>cursorShape$</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Simply use the statement whenever <a href="MOUSEHIDE" title="MOUSEHIDE">_MOUSEHIDE</a> has been used previously.</li>
<li>In <b>version 1.000 and up</b> the following <i>cursorShape$</i> can be displayed:</li></ul>
<dl><dd>_MOUSESHOW "LINK" will display an upward pointing hand cursor used to denote hypertext</dd>
<dd>_MOUSESHOW "TEXT" will display the I cursor often used in text entry areas</dd>
<dd>_MOUSESHOW "CROSSHAIR" will display a crosshair cursor</dd>
<dd>_MOUSESHOW "VERTICAL" will display vertical arrow cursor for movement</dd>
<dd>_MOUSESHOW "HORIZONTAL" will display horizontal arrow cursor for movement</dd>
<dd>_MOUSESHOW "TOPLEFT_BOTTOMRIGHT" will display bottom diagonal arrow cursor for movement</dd>
<dd>_MOUSESHOW "TOPRIGHT_BOTTOMLEFT" will display bottom diagonal arrow cursor for movement</dd>
<dd>_MOUSESHOW "DEFAULT" can be used after a mouse cursor statement above was previously used.</dd></dl>
<ul><li>This statement will also disable <a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a> or <a href="MOUSEMOVEMENTY" title="MOUSEMOVEMENTY">_MOUSEMOVEMENTY</a> relative mouse movement reads.</li>
<li>The mouse cursor will not interfere with any print or graphic screen changes in <b>QB64</b>.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>_MOUSEHIDE statements do not accumulate like they did with <a href="CALL_ABSOLUTE" title="CALL ABSOLUTE">ABSOLUTE</a> or <a href="INTERRUPT" title="INTERRUPT">INTERRUPT</a> in QBasic.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> <b>QB64 1.000 and up</b> allow special cursors to be displayed by using special string parameters:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSESHOW</span></a> "default": <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.5
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSESHOW</span></a> "link": <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.5 'a hand, typically used in web browsers
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSESHOW</span></a> "text": <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.5
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSESHOW</span></a> "crosshair": <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.5
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSESHOW</span></a> "vertical": <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.5
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSESHOW</span></a> "horizontal": <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.5
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSESHOW</span></a> "topleft_bottomright": <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.5
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MOUSESHOW</span></a> "topright_bottomleft": <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 0.5
</pre>
</td></tr></tbody></table>
<dl><dd><b>Note:</b> There is no hourglass, stopwatch or spinning colorful wheel in the list. The fact is that these typically only appear in a program when something has gone terribly wrong and the program has crashed or frozen.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MOUSEHIDE" title="MOUSEHIDE">_MOUSEHIDE</a></li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a></li>
<li><a href="MOUSEMOVE" title="MOUSEMOVE">_MOUSEMOVE</a></li>
<li><a href="MOUSEX" title="MOUSEX">_MOUSEX</a>, <a href="MOUSEY" title="MOUSEY">_MOUSEY</a></li>
<li><a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a></li>
<li><a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a>, <a href="MOUSEMOVEMENTY" title="MOUSEMOVEMENTY">_MOUSEMOVEMENTY</a></li>
<li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICE$" title="DEVICE$">_DEVICE$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062414
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 157/1000000
Post‐expand include size: 1594/2097152 bytes
Template argument size: 280/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.343      1 -total
 14.15%    3.162      1 Template:PageSyntax
 12.31%    2.750     16 Template:Cl
 10.65%    2.380      2 Template:Parameter
  9.62%    2.149      1 Template:CodeStart
  9.46%    2.114      1 Template:PageSeeAlso
  9.43%    2.107      1 Template:PageDescription
  9.32%    2.083      1 Template:CodeEnd
  9.01%    2.013      1 Template:PageExamples
  7.91%    1.768      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:195-0!canonical and timestamp 20240715062414 and revision id 7144.
 -->
</div>
</div>
</div>
</div>
</body>
</html>