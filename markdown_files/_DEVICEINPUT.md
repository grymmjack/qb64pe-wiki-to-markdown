<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DEVICEINPUT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEVICEINPUT rootpage-DEVICEINPUT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DEVICEINPUT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_DEVICEINPUT</b> function returns the device number when a controller device button, wheel or axis event occurs.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>device%</i> = <a class="mw-selflink selflink">_DEVICEINPUT</a></dd>
<dd><i>device_active%</i> = <a class="mw-selflink selflink">_DEVICEINPUT</a>(<i>device_number%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Use the <i>device%</i> <a href="INTEGER" title="INTEGER">INTEGER</a> returned to find the number of the controller device being used.</li>
<li>A literal specific <i>device_number%</i> parameter can be used to return -1 if active or 0 if inactive, e.g. <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEVICEINPUT</span></a>(<span style="color:#F580B1;">2</span>)</span>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use <a href="DEVICES" title="DEVICES">_DEVICES</a> to find the number of controller devices available BEFORE using this function.</li>
<li><a href="DEVICE$" title="DEVICE$">_DEVICE$</a> can be used to list the device names and control types using valid <a href="DEVICES" title="DEVICES">_DEVICES</a> numbers.</li>
<li>When a device button is pressed or a scroll wheel or axis is moved, the device number will be returned.</li>
<li>Devices are numbered as 1 for keyboard and 2 for mouse. Other controller devices will be numbered 3 or higher if installed.</li>
<li><a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>, <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a>, or <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a> will indicate the number of functions available with the specified <i>device%</i> number.</li>
<li>User input events can be monitored reading valid numbered <a href="AXIS" title="AXIS">_AXIS</a>, <a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="BUTTONCHANGE" title="BUTTONCHANGE">_BUTTONCHANGE</a> or <a href="WHEEL" title="WHEEL">_WHEEL</a> functions.</li>
<li><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="ON...GOSUB" title="ON...GOSUB"><span style="color:#4593D8;">ON _DEVICEINPUT GOSUB</span></a> keyboard, mouse, gamecontrol</span> could be used to easily branch to device specific handler routines (see Example 3 below).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Checking device controller interfaces and finding out what devices are being used.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i% = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(i%) + <span style="color:#FFB100;">") "</span> + <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i%)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Button:"</span>; <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(i%); <span style="color:#FFB100;">",Axis:"</span>; <a href="LASTAXIS" title="LASTAXIS"><span style="color:#4593D8;">_LASTAXIS</span></a>(i%); <span style="color:#FFB100;">",Wheel:"</span>; <a href="LASTWHEEL" title="LASTWHEEL"><span style="color:#4593D8;">_LASTWHEEL</span></a>(i%)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i%
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    x% = <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEVICEINPUT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> x% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Device ="</span>; x%;
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">[KEYBOARD][BUTTON]
Buttons: 512 Axis: 0 Wheels: 0
[MOUSE][BUTTON][AXIS][WHEEL]
Buttons: 3 Axis: 2 Wheels: 3
[CONTROLLER][[NAME][Microsoft Sidewinder Precision Pro (USB)[BUTTON][AXIS]
Buttons: 9 Axis: 6 Wheels: 0
Device = 2 Device = 2
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputplain"><b>Note</b>
 Mouse events must be within the program screen area. Keyboard presses
 are registered only when program is in focus.
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Why does a mouse have 3 wheels? Relative x and y movements can be read using the first 2 <a href="WHEEL" title="WHEEL">_WHEEL</a> reads.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">ignore% = <a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX"><span style="color:#4593D8;">_MOUSEMOVEMENTX</span></a> <span style="color:#919191;">'dummy call to put mouse into relative movement mode</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Move your mouse and/or your mouse wheel (ESC to exit)"</span>
d% = <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a> <span style="color:#919191;">'always read number of devices to enable device input</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">30</span> <span style="color:#919191;">'main loop</span>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEVICEINPUT</span></a>(<span style="color:#F580B1;">2</span>) <span style="color:#919191;">'loop only runs during a device 2 mouse event</span>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="WHEEL" title="WHEEL"><span style="color:#4593D8;">_WHEEL</span></a>(<span style="color:#F580B1;">1</span>), <a href="WHEEL" title="WHEEL"><span style="color:#4593D8;">_WHEEL</span></a>(<span style="color:#F580B1;">2</span>), <a href="WHEEL" title="WHEEL"><span style="color:#4593D8;">_WHEEL</span></a>(<span style="color:#F580B1;">3</span>)
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputplain"><b>Explanation</b>
 Referencing the <a href="MOUSEMOVEMENTX" title="MOUSEMOVEMENTX">_MOUSEMOVEMENTX</a> function hides the mouse and sets
 the mouse to a relative movement mode which can be read by <a href="WHEEL" title="WHEEL">_WHEEL</a>.
 _DEVICEINPUT(2) returns -1 (true) only when the mouse is moved,
 scrolled or clicked.
</pre>
</td></tr></tbody></table>
<dl><dt>Example 3</dt>
<dd>Using <a href="ON...GOSUB" title="ON...GOSUB">ON...GOSUB</a> with the <a class="mw-selflink selflink">_DEVICEINPUT</a> number to add keyboard, mouse and game controller event procedures.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">n% = <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a> <span style="color:#919191;">'required when reading devices</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Number of devices found ="</span>; n%
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i% = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> n%
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i%; <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i%) <span style="color:#919191;">'1 = keyboard, 2 = mouse, 3 = other controller, etc.</span>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i%
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    device% = <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEVICEINPUT</span></a>
    <a href="ON" title="ON"><span style="color:#4593D8;">ON</span></a> device% <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> keyboard, mouse, controller <span style="color:#919191;">'must be inside program loop</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
keyboard:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> device%; <span style="color:#FFB100;">"Keyboard"</span>;
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
mouse:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> device%; <span style="color:#FFB100;">"Mouse "</span>;
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
controller:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> device%; <span style="color:#FFB100;">"Game control "</span>;
<a href="RETURN" title="RETURN"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputplain"><b>Note</b>
 <a href="ON...GOSUB" title="ON...GOSUB">ON...GOSUB</a> and <a href="ON...GOTO" title="ON...GOTO">ON...GOTO</a> events require numerical values to match
 the order of line labels listed in the event used inside loops.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICE$" title="DEVICE$">_DEVICE$</a></li>
<li><a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>, <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a>, <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a></li>
<li><a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="AXIS" title="AXIS">_AXIS</a>, <a href="WHEEL" title="WHEEL">_WHEEL</a></li>
<li><a href="STRIG" title="STRIG">STRIG</a>, <a href="STICK" title="STICK">STICK</a></li>
<li><a href="ON...GOSUB" title="ON...GOSUB">ON...GOSUB</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062321
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.054 seconds
Real time usage: 0.084 seconds
Preprocessor visited node count: 764/1000000
Post‐expand include size: 6645/2097152 bytes
Template argument size: 1628/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 425/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   58.890      1 -total
 19.78%   11.646      6 Template:Parameter
 10.94%    6.444     62 Template:Cl
  7.37%    4.339      1 Template:PageSyntax
  4.88%    2.874     28 Template:Text
  4.21%    2.480      3 Template:PreEnd
  3.97%    2.335      1 Template:PageParameters
  3.63%    2.135      3 Template:CodeEnd
  3.61%    2.127      2 Template:InlineCode
  3.60%    2.118      3 Template:PreStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:119-0!canonical and timestamp 20240715062320 and revision id 8576.
 -->
</div>
</div>
</div>
</div>
</body>
</html>