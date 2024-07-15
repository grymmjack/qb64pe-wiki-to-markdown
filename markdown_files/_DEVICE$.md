<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DEVICE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEVICE rootpage-DEVICE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DEVICE$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_DEVICE$</b> function returns a <a href="STRING" title="STRING">STRING</a> value holding the controller type, name and input types of the input devices on a computer.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>device$</i> = _DEVICE$(<i>device_number</i>)</dd></dl>
<p>
</p>
<ul><li>The <b><a href="DEVICES" title="DEVICES">_DEVICES</a> function must be read first to get the number of devices and to enable <a class="mw-selflink selflink">_DEVICE$</a> and <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a>.</b></li>
<li>The <i>device_number</i> parameter indicates the number of the controller device to be read.</li>
<li>Returns the <a href="STRING" title="STRING">STRING</a> control type, name of the device and input types each can use included in brackets:</li></ul>
<dl><dd><dl><dd><ul><li>Control type:</li></ul>
<dl><dd>[KEYBOARD] always listed as first device when keyboard(s) available. Only one keyboard will show.</dd>
<dd>[MOUSE always listed as second device when keyboard(s) and mouse(mice) are available. Only one mouse will show.</dd>
<dd>[CONTROLLER] subsequent devices are listed as controllers which include joysticks and game pads.</dd></dl>
<ul><li>When [CONTROLLER] is returned it may also give the <a href="STRING" title="STRING">STRING</a> [[NAME] [device description of the controller.</li>
<li>When [DISCONNECTED] is returned, then the device was unplugged after device init.</li>
<li>Returns the type of input after the device name as one or more of the following types:</li></ul>
<dl><dd>[[[BUTTON] indicates there are button types of input. <a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a> can return the number of buttons available.</dd>
<dd>[[[AXIS] indicates there are stick types of input. <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a> can return the number of axis available.</dd>
<dd>[[[WHEEL] indicates that a scrolling input can be read. <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a> can return the number of wheels available.</dd></dl></dd></dl></dd></dl>
<ul><li><b>Device numbers above the number of <a href="DEVICES" title="DEVICES">devices</a> found will return an OS error.</b></li>
<li>Devices found include keyboard, mouse, joysticks, game pads and multiple stick game controllers.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Checking for the system's input devices and the number of buttons available.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">devices = <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a> <span style="color:#919191;">'MUST be read in order for other 2 device functions to work!</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Number of input devices found ="</span>; devices
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> devices
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEVICE$</span></a>(i)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Buttons:"</span>; <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(i); <span style="color:#FFB100;">"Axis:"</span>; <a href="LASTAXIS" title="LASTAXIS"><span style="color:#4593D8;">_LASTAXIS</span></a>(i); <span style="color:#FFB100;">"Wheels:"</span>; <a href="LASTWHEEL" title="LASTWHEEL"><span style="color:#4593D8;">_LASTWHEEL</span></a>(i)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Number of input devices found = 3
[KEYBOARD][BUTTON]
Buttons: 512 Axis: 0 Wheels: 0
[MOUSE][BUTTON][AXIS][WHEEL]
Buttons: 3 Axis: 2 Wheels: 3
[CONTROLLER][[NAME][Microsoft Sidewinder Precision Pro (USB)[BUTTON][AXIS]
Buttons: 9 Axis: 6 Wheels: 0
</pre>
</td></tr></tbody></table>
<dl><dd>Note: The <a href="STRIG" title="STRIG">STRIG</a>/<a href="STICK" title="STICK">STICK</a> commands won't read from the keyboard or mouse device the above example lists. They will only work on controllers.</dd></dl>
<p><i>Example 2:</i> Finding the number of mouse buttons available in QB64. This could also be used for other devices.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> d = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a> <span style="color:#919191;">'number of input devices found</span>
    dev$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEVICE$</span></a>(d)
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(dev$, <span style="color:#FFB100;">"[MOUSE]"</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> buttons = <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(d): <a href="EXIT_FOR" title="EXIT FOR"><span style="color:#4593D8;">EXIT FOR</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> buttons; <span style="color:#FFB100;">"mouse buttons available"</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a></li>
<li><a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>, <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a>, <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a></li>
<li><a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="BUTTONCHANGE" title="BUTTONCHANGE">_BUTTONCHANGE</a></li>
<li><a href="AXIS" title="AXIS">_AXIS</a>, <a href="WHEEL" title="WHEEL">_WHEEL</a></li>
<li><a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a></li>
<li><a href="STRIG" title="STRIG">STRIG</a>, <a href="STICK" title="STICK">STICK</a></li>
<li><a href="ON_STRIG(n)" title="ON STRIG(n)">ON STRIG(n)</a>, <a href="STRIG(n)" title="STRIG(n)">STRIG(n)</a></li>
<li><a href="Controller_Devices" title="Controller Devices">Controller Devices</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062319
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 286/1000000
Post‐expand include size: 2590/2097152 bytes
Template argument size: 637/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 183/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.042      1 -total
 14.11%    4.238      1 Template:PageSyntax
 13.78%    4.139      3 Template:Parameter
 10.05%    3.019     22 Template:Cl
  9.09%    2.732      1 Template:PageNavigation
  7.84%    2.354     10 Template:Text
  6.77%    2.035      1 Template:PageExamples
  6.41%    1.925      2 Template:CodeStart
  6.06%    1.821      1 Template:PageSeeAlso
  5.73%    1.721      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:118-0!canonical and timestamp 20240715062319 and revision id 8447.
 -->
</div>
</div>
</div>
</div>
</body>
</html>