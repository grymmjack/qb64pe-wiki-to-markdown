<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>STICK - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STICK rootpage-STICK skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">STICK</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>STICK</b> function returns the directional axis coordinate move of game port (&amp;H201) joystick or USB controller devices.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dt>QuickBASIC</dt>
<dd>coordinate_move% = <a class="mw-selflink selflink">STICK</a><i>(direction%)</i></dd>
<dt>QB64</dt>
<dd>coordinate_move% = <a class="mw-selflink selflink">STICK</a><i>(direction%[, axis_number%])</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>QB64</b> allows any number of coordinate pairs for more than two game device controllers. STICK will not read a mouse axis.</li>
<li><i>axis_number</i> can be used as the next axis parameter for controllers with multiple axis using the SAME <i>directional</i> parameters.</li>
<li>The <i>axis_number</i> 1 can be omitted for the main stick column and row parameter reads.</li>
<li>Point of view "hats" also have 2 axis. Slide, turn or twist controls have one. The device determines the order of the axis.</li>
<li>Returns coordinate values from 1 to 254. QBasic only returned values from 1 to 200.</li>
<li>STICK(0) is required to get values from the other STICK functions. Always read it first!</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed"><b>STICK(0) returns the column coordinate of device 1. Enables reads of the other STICK values.</b>
<b>STICK(1) returns row coordinate of device 1.</b>
STICK(2) returns column coordinate of device 2. (second joystick if used)
STICK(3) returns row coordinate of device 2 if used. (QBasic maximum was 2 controllers)
<b>STICK(4) returns column coordinate of device 3. (other joysticks if used in QB64 only!)</b>
<b>STICK(5) returns row coordinate of device 3 if used.</b>
</pre>
</td></tr></tbody></table>
<ul><li><b>QB64</b> allows more joysticks by extending the numbers in pairs like device 3 above. EX: STICK(6): STICK(7) 'device 4</li>
<li><b>QB64</b> allows a dual stick to be read using the same first parameters and 2 as the second parameter. EX: STICK(0, 2)</li>
<li><b>There will not be an error if you try to read too many device axis or buttons!</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Displays the input from 3 joysticks, all with dual sticks and 3 buttons.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 10
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "JOY1: <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>"; <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(0); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(1); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(0, 2); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(1, 2);_
  "STRIG"; <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(0); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(1); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(4); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(5); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(8); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(9)
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "JOY2: <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>"; <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(2); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(3); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(2, 2); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(3, 2);_
  "STRIG"; <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(2); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(3); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(6); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(7); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(10); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(11)
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "JOY3: <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>"; <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(4); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(5); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(4, 2); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(5, 2);_
  "STRIG"; <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(0, 3); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(1, 3); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(4, 3); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(5, 3); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(8, 3); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(9, 3)
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &gt; ""
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Notice the extra <b>QB64 only</b> parameters used to cater for the 2nd stick and the buttons of the 3rd joystick.</dd></dl>
<p>
<i>Example 2:</i> Displays the Sidewinder Precision Pro Stick, Slider, Z Axis, and Hat Point of View.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
d = <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Number of input devices found ="; d
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> d
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i)
  buttons = <a href="LASTBUTTON" title="LASTBUTTON"><span style="color:#4593D8;">_LASTBUTTON</span></a>(i)
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Buttons:"; buttons
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
DO: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 50
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 1
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "   X    Main    Y          Slider         Z-axis           POV"
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(0, 1), <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(1, 1), <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(0, 2), <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(1, 2), <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(0, 3); <a class="mw-selflink selflink"><span style="color:#4593D8;">STICK</span></a>(1, 3); "   "
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "                   Buttons"
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 4 * buttons - 1 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> 4
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(i); <a href="STRIG" title="STRIG"><span style="color:#4593D8;">STRIG</span></a>(i + 1); <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(219);
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Each axis on the first controller found is either STICK(0, n) or STICK(1, n) with n increasing when necessary.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Number of input devices found = 3
[KEYBOARD][BUTTON
Buttons: 512
[MOUSE][BUTTON][AXIS][WHEEL]
Buttons: 3
[CONTROLLER][[NAME][Microsoft Sidewinder Precision Pro (USB)[BUTTON][AXIS]
Buttons: 9
  X    Main     Y          Slider         Z-axis           POV
 127           127           254           127           127  127
                      Buttons
-0 -1 █ 0  0 █ 0  0 █ 0  0 █ 0  0 █ 0  0 █ 0  0 █ 0  0 █ 0  0 █
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> A Sidewinder Precision Pro requires that pins 2 and 7(blue and purple) be connected together for digital USB recognition.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="STRIG" title="STRIG">STRIG</a></li>
<li><a href="ON_STRIG(n)" title="ON STRIG(n)">ON STRIG(n)</a></li>
<li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a></li>
<li><a class="extiw" href="https://en.wikipedia.org/wiki/Analog_stick" title="wikipedia:Analog stick">Single and Dual Stick Controllers</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061025
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.079 seconds
Real time usage: 0.159 seconds
Preprocessor visited node count: 566/1000000
Post‐expand include size: 4747/2097152 bytes
Template argument size: 804/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   87.160      1 -total
 18.88%   16.460      1 Template:PageSyntax
 11.22%    9.775     75 Template:Cl
  8.89%    7.749      1 Template:PageDescription
  7.22%    6.293      1 Template:FixedEnd
  6.77%    5.900      1 Template:FixedStart
  6.75%    5.886      2 Template:Parameter
  5.54%    4.828      1 Template:PageExamples
  5.40%    4.704      2 Template:CodeStart
  4.74%    4.135      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:568-0!canonical and timestamp 20240715061024 and revision id 8996.
 -->
</div>
</div>
</div>
</div>
</body>
</html>