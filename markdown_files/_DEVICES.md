<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DEVICES - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEVICES rootpage-DEVICES skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DEVICES</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_DEVICES</b> function returns the number of input devices on your computer including keyboard, mouse and game devices.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>device_count%</i> = <a class="mw-selflink selflink">_DEVICES</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns the number of devices that can be listed separately with the <a href="DEVICE$" title="DEVICE$">_DEVICE$</a> function by the device number.</li>
<li>Devices include keyboard, mouse, joysticks, game pads and multiple stick game controllers.</li></ul>
<dl><dt>Note</dt>
<dd>This function must be read before trying to use the <a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a> or any of the <b>_LASTxxx</b> control functions.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dd>Checking for the system's input devices.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">devices% = <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEVICES</span></a> <span style="color:#919191;">'MUST be read in order for other 2 device functions to work!</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Number of input devices found ="</span>; devices%
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i% = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> devices%
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i%)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Buttons:"</span>; <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(i%)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i%
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Number of input devices found = 2
[KEYBOARD][BUTTON]
Buttons: 512
[MOUSE][BUTTON][AXIS][WHEEL]
Buttons: 3
</pre>
</td></tr></tbody></table>
<dl><dt>Note</dt>
<dd>The <a href="STRIG" title="STRIG">STRIG</a> and <a href="STICK" title="STICK">STICK</a> commands won't read from the keyboard or mouse device the above example lists.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a></li>
<li><a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>, <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a>, <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a></li>
<li><a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="BUTTONCHANGE" title="BUTTONCHANGE">_BUTTONCHANGE</a></li>
<li><a href="AXIS" title="AXIS">_AXIS</a>, <a href="WHEEL" title="WHEEL">_WHEEL</a></li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a>, <a href="MOUSEX" title="MOUSEX">_MOUSEX</a>, <a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a></li>
<li><a href="STRIG" title="STRIG">STRIG</a>, <a href="STICK" title="STICK">STICK</a></li>
<li><a href="ON_STRIG(n)" title="ON STRIG(n)">ON STRIG(n)</a>, <a href="STRIG(n)" title="STRIG(n)">STRIG(n)</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062321
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 137/1000000
Post‐expand include size: 1503/2097152 bytes
Template argument size: 252/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 103/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.384      1 -total
 14.35%    4.074      1 Template:OutputStart
  9.69%    2.749     10 Template:Cl
  8.12%    2.305      1 Template:PageSyntax
  7.91%    2.244      4 Template:Text
  7.06%    2.003      1 Template:PageNavigation
  6.88%    1.954      1 Template:CodeEnd
  6.84%    1.943      1 Template:OutputEnd
  6.74%    1.914      1 Template:Parameter
  6.67%    1.892      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:120-0!canonical and timestamp 20240715062321 and revision id 8408.
 -->
</div>
</div>
</div>
</div>
</body>
</html>