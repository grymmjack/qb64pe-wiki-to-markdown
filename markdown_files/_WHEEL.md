<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_WHEEL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-WHEEL rootpage-WHEEL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_WHEEL</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_WHEEL</a> function returns the relative position of a specified wheel number on a controller device.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>move</i> = <a class="mw-selflink selflink">_WHEEL</a>(<i>wheelNumber%</i>)</dd></dl>
<p>
</p>
<ul><li>Returns -1 when scrolling up and 1 when scrolling down with 0 indicating no movement since last read.</li>
<li>Add consecutive wheel values to determine a cumulative value over time for scrolling or moving objects.</li>
<li><i>wheelNumber%</i> must be a number which does not exceed the number of wheels found by the <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a> function.</li>
<li>When a mouse indicates it has 3 wheels, the first two are for relative movement reads. The third wheel is for scrolling.</li>
<li><b>The number of <a href="DEVICES" title="DEVICES">_DEVICES</a> must be read before using <a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a> or <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a>.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Reading multiple controller device buttons, axis and wheels.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a>
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(i) + ") " + <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i) + " Buttons:"; <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(i); ",Axis:"; <a href="LASTAXIS" title="LASTAXIS"><span style="color:#4593D8;">_LASTAXIS</span></a>(i); ",Wheel:"; <a href="LASTWHEEL" title="LASTWHEEL"><span style="color:#4593D8;">_LASTWHEEL</span></a>(i)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
  d&amp; = <a href="DEVICEINPUT" title="DEVICEINPUT"><span style="color:#4593D8;">_DEVICEINPUT</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> d&amp; <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> '             the device number cannot be zero!
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Found"; d&amp;;
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> b = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(d&amp;)
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="BUTTONCHANGE" title="BUTTONCHANGE"><span style="color:#4593D8;">_BUTTONCHANGE</span></a>(b); <a href="BUTTON" title="BUTTON"><span style="color:#4593D8;">_BUTTON</span></a>(b);
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> a = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LASTAXIS" title="LASTAXIS"><span style="color:#4593D8;">_LASTAXIS</span></a>(d&amp;)
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="AXIS" title="AXIS"><span style="color:#4593D8;">_AXIS</span></a>(a);
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> w = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LASTWHEEL" title="LASTWHEEL"><span style="color:#4593D8;">_LASTWHEEL</span></a>(d&amp;)
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_WHEEL</span></a>(w);
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) 'escape key exit
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> When there is no device control to read, a <a href="FOR...NEXT" title="FOR...NEXT">FOR</a> n = 1 TO 0 loop will not run thus avoiding a control function read error.</dd></dl>
<p>
<i>Example 2:</i> Why does a mouse have 3 wheels? Relative x and y movements can be read using the first 2 _WHEEL reads.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">ignore = <a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX"><span style="color:#4593D8;">_MOUSEMOVEMENTX</span></a> 'dummy call to put mouse into relative movement mode
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Move your mouse and/or your mouse wheel (ESC to exit)"
d = <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a> '  always read number of devices to enable device input
DO: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 30  'main loop
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="DEVICEINPUT" title="DEVICEINPUT"><span style="color:#4593D8;">_DEVICEINPUT</span></a>(2) 'loop only runs during a device 2 mouse event
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_WHEEL</span></a>(1), <a class="mw-selflink selflink"><span style="color:#4593D8;">_WHEEL</span></a>(2), <a class="mw-selflink selflink"><span style="color:#4593D8;">_WHEEL</span></a>(3)
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Referencing the <a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a> function hides the mouse and sets the mouse to a relative movement mode which can be read by <a class="mw-selflink selflink">_WHEEL</a>. <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a>(2) returns -1 (true) only when the mouse is moved, scrolled or clicked.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MOUSEWHEEL" title="MOUSEWHEEL">_MOUSEWHEEL</a></li>
<li><a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a>, <a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>, <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a></li>
<li><a href="AXIS" title="AXIS">_AXIS</a>, <a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="BUTTONCHANGE" title="BUTTONCHANGE">_BUTTONCHANGE</a></li>
<li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a></li>
<li><a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a>, <a href="MOUSEMOVEMENTY" title="MOUSEMOVEMENTY">_MOUSEMOVEMENTY</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062516
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.052 seconds
Real time usage: 0.066 seconds
Preprocessor visited node count: 432/1000000
Post‐expand include size: 3752/2097152 bytes
Template argument size: 725/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   32.604      1 -total
 17.27%    5.632     57 Template:Cl
 11.49%    3.747      1 Template:PageSyntax
 10.51%    3.426      3 Template:Parameter
  9.89%    3.224      1 Template:PageExamples
  9.50%    3.099      2 Template:CodeStart
  9.15%    2.982      1 Template:PageNavigation
  8.92%    2.909      2 Template:CodeEnd
  8.61%    2.808      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:363-0!canonical and timestamp 20240715062516 and revision id 6315.
 -->
</div>
</div>
</div>
</div>
</body>
</html>