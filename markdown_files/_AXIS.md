<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_AXIS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-AXIS rootpage-AXIS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_AXIS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_AXIS</a> function returns the relative position of a specified axis number on a controller device.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>move!</i> = <a class="mw-selflink selflink">_AXIS</a>(<i>axis_number%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a href="SINGLE" title="SINGLE">SINGLE</a> values returned range between -1 and 1 as maximums and 0 indicating minimum or axis center.</li>
<li>When the mouse is moved on the program screen, moves left or above center are negative while below or right are positive.</li>
<li>The <i>axis_number</i> must be a number which does not exceed the number of axis found by the <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a> function.</li>
<li><b>The number of <a href="DEVICES" title="DEVICES">_DEVICES</a> must be read before using <a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a> or <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a>.</b></li></ul>
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
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="BUTTONCHANGE" title="BUTTONCHANGE"><span style="color:#4593D8;">_BUTTONCHANGE</span></a>(b); <a href="BUTTON" title="BUTTON"><span style="color:#4593D8;">_BUTTON</span></a>(b);
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> a = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LASTAXIS" title="LASTAXIS"><span style="color:#4593D8;">_LASTAXIS</span></a>(d&amp;)
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_AXIS</span></a>(a);
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
<li><a href="WHEEL" title="WHEEL">_WHEEL</a>, <a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="BUTTONCHANGE" title="BUTTONCHANGE">_BUTTONCHANGE</a></li>
<li><a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICES" title="DEVICES">_DEVICES</a></li>
<li><a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a>, <a href="MOUSEMOVEMENTY" title="MOUSEMOVEMENTY">_MOUSEMOVEMENTY</a> <span style="color:#777777;">(relative movement)</span></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062245
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.054 seconds
Real time usage: 0.086 seconds
Preprocessor visited node count: 420/1000000
Post‐expand include size: 3497/2097152 bytes
Template argument size: 815/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 102/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   47.512      1 -total
 13.13%    6.240      1 Template:CodeEnd
 12.47%    5.924     40 Template:Cl
  8.95%    4.252      1 Template:PageSyntax
  8.39%    3.988      1 Template:PageSeeAlso
  8.35%    3.967      1 Template:CodeStart
  8.09%    3.843      1 Template:PageDescription
  7.86%    3.735      2 Template:Parameter
  7.06%    3.357     13 Template:Text
  7.04%    3.347      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:51-0!canonical and timestamp 20240715062245 and revision id 8263.
 -->
</div>
</div>
</div>
</div>
</body>
</html>