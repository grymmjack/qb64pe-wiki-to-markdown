<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_BUTTONCHANGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BUTTONCHANGE rootpage-BUTTONCHANGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_BUTTONCHANGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_BUTTONCHANGE</a> function returns -1 or 1 when a specified button number on a controller device has been pressed or released.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>press%</i> = <a class="mw-selflink selflink">_BUTTONCHANGE</a>(<i>button_number%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Values returned are -1 for a press and 1 when a button is released. No press or release event returns zero.</li>
<li>The <i>button_number%</i> must be a number which does not exceed the number of buttons found by the <a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a> function.</li>
<li><b>The number of <a href="DEVICES" title="DEVICES">_DEVICES</a> must be read before using <a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a> or <a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>.</b></li>
<li><b>Note:</b> The center mouse button is button number 2. Center can also be read using  <a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a>(3).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Reading multiple controller device buttons, axis and wheels.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(i) + <span style="color:#FFB100;">") "</span> + <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i) + <span style="color:#FFB100;">" Buttons:"</span>; <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(i); <span style="color:#FFB100;">",Axis:"</span>; <a href="LASTAXIS" title="LASTAXIS"><span style="color:#4593D8;">_LASTAXIS</span></a>(i); <span style="color:#FFB100;">",Wheel:"</span>; <a href="LASTWHEEL" title="LASTWHEEL"><span style="color:#4593D8;">_LASTWHEEL</span></a>(i)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    d&amp; = <a href="DEVICEINPUT" title="DEVICEINPUT"><span style="color:#4593D8;">_DEVICEINPUT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> d&amp; <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">'             the device number cannot be zero!</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Found"</span>; d&amp;;
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> b = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(d&amp;)
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_BUTTONCHANGE</span></a>(b); <a href="BUTTON" title="BUTTON"><span style="color:#4593D8;">_BUTTON</span></a>(b);
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> a = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LASTAXIS" title="LASTAXIS"><span style="color:#4593D8;">_LASTAXIS</span></a>(d&amp;)
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="AXIS" title="AXIS"><span style="color:#4593D8;">_AXIS</span></a>(a);
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> w = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LASTWHEEL" title="LASTWHEEL"><span style="color:#4593D8;">_LASTWHEEL</span></a>(d&amp;)
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="WHEEL" title="WHEEL"><span style="color:#4593D8;">_WHEEL</span></a>(w);
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>) <span style="color:#919191;">'escape key exit</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> When there is no device control to read, a <a href="FOR...NEXT" title="FOR...NEXT">FOR</a> n = 1 TO 0 loop will not run thus avoiding a control function read error.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a>, <a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>, <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a></li>
<li><a href="AXIS" title="AXIS">_AXIS</a>, <a href="WHEEL" title="WHEEL">_WHEEL</a>, <a href="BUTTON" title="BUTTON">_BUTTON</a></li>
<li><a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICES" title="DEVICES">_DEVICES</a></li>
<li><a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062252
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.052 seconds
Real time usage: 0.062 seconds
Preprocessor visited node count: 418/1000000
Post‐expand include size: 3463/2097152 bytes
Template argument size: 813/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 102/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   32.361      1 -total
 14.97%    4.845     40 Template:Cl
  9.69%    3.136     12 Template:Text
  8.48%    2.744      1 Template:CodeEnd
  8.12%    2.626      1 Template:CodeStart
  7.88%    2.550      1 Template:PageSyntax
  7.66%    2.478      3 Template:Parameter
  7.35%    2.380      1 Template:PageDescription
  7.31%    2.365      1 Template:PageSeeAlso
  7.25%    2.346      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:61-0!canonical and timestamp 20240715062252 and revision id 8274.
 -->
</div>
</div>
</div>
</div>
</body>
</html>