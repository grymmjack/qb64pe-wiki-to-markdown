<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>STRIG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STRIG rootpage-STRIG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">STRIG</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>STRIG</b> function returns button press True or False status of game port (&amp;H201) or USB joystick control device(s).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dt>QuickBASIC</dt>
<dd>IF STRIG(button_function%) THEN ...</dd>
<dt>QB64</dt>
<dd>IF STRIG(<i>button_function%</i>[, <i>device_number%</i>]) THEN ...</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Function returns -1 when a button event(even functions) has occurred or a button is pressed(odd functions).</li>
<li>STRIG will not read keyboard or mouse buttons detected by <a href="DEVICES" title="DEVICES">_DEVICES</a>.</li>
<li>The <i>device number</i> must be used with more than 2 devices. Use device 1 function numbers for just one joystick.</li>
<li><b>QB64</b> can read many buttons from many devices and allows the use of devices with more than 2 buttons.</li>
<li>Returns True(-1) or False(0) button press values for 2 devices. Each leading STRIG checks for missed button press events:</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">  <b>STRIG(0) = -1  'lower button 1 on device 1 pressed since last STRIG(0) read</b>
  <b>STRIG(1) = -1  'lower button 1 on device 1 currently pressed</b>
  STRIG(2) = -1  'lower button 1 on device 2 pressed since last STRIG(2) read
  STRIG(3) = -1  'lower button 1 on device 2 currently pressed
  <b>STRIG(4) = -1  'upper button 2 on device 1 pressed since last STRIG(4) read</b>
  <b>STRIG(5) = -1  'upper button 2 on device 1 currently pressed</b>
  STRIG(6) = -1  'upper button 2 on device 2 pressed since last STRIG(6) read
  STRIG(7) = -1  'upper button 2 on device 2 currently pressed (maximum in QBasic)
  <b>STRIG(8) = -1  'button 3 on device 1 pressed since last STRIG(8) read</b>  'QB64 only
  <b>STRIG(9) = -1  'button 3 on device 1 currently pressed</b>
  STRIG(10) = -1 'button 3 on device 2 pressed since last STRIG(10) read 'QB64 only
  STRIG(11) = -1 'button 3 on device 2 currently pressed
</pre>
</td></tr></tbody></table>
<ul><li>STRIG(0), STRIG(2), STRIG(4), STRIG(6), STRIG(8), STRIG(10) are used to monitor any presses that might have been missed.</li>
<li><b>QB64</b> allows more than two controllers by using the second parameter as the stick number and the odd or even STRIG values:</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed"><b>STRIG(0, 3): STRIG(1, 3): STRIG(4, 3): STRIG(5, 3): STRIG(8, 3): STRIG(9, 3) 'device 3 {odd)</b>
STRIG(2, 4): STRIG(3, 4): STRIG(6, 4): STRIG(7, 4): STRIG(10, 4): STRIG(11, 4) 'device 4 (even)
</pre>
</td></tr></tbody></table>
<dl><dd>Odd devices use 0, 1, 4, 5, 8 and 9 and Even devices use 2, 3, 6, 7, 10 and 11 as first parameters with device number following.</dd></dl>
<ul><li><b>There will not be an error if you try to read too many device axis or buttons!</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Displays the input from 3 joysticks, all with dual sticks and 3 buttons.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 10
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "JOY1: <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>"; <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(0); <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(1); <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(0, 2); <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(1, 2);_
  "STRIG"; <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(0); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(1); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(4); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(5); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(8); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(9)
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "JOY2: <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>"; <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(2); <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(3); <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(2, 2); <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(3, 2);_
  "STRIG"; <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(2); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(3); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(6); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(7); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(10); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(11)
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "JOY3: <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>"; <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(4); <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(5); <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(4, 2); <a href="STICK" title="STICK"><span style="color:#4593D8;">STICK</span></a>(5, 2);_
  "STRIG"; <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(0, 3); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(1, 3); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(4, 3); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(5, 3); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(8, 3); <a class="mw-selflink selflink"><span style="color:#4593D8;">STRIG</span></a>(9, 3)
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &gt; ""
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Notice the extra <b>QB64 only</b> parameters used to cater for the 2nd stick and the buttons of the 3rd joystick.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="STRIG(n)" title="STRIG(n)">STRIG(n)</a></li>
<li><a href="ON_STRIG(n)" title="ON STRIG(n)">ON STRIG(n)</a>, <a href="STICK" title="STICK">STICK</a></li>
<li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a></li>
<li><a class="extiw" href="https://en.wikipedia.org/wiki/Analog_stick" title="wikipedia:Analog stick">Single and Dual Stick Controllers</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061426
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.038 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 322/1000000
Post‐expand include size: 2932/2097152 bytes
Template argument size: 418/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   29.515      1 -total
 15.84%    4.675     42 Template:Cl
  9.98%    2.947      1 Template:PageSyntax
  8.84%    2.608      1 Template:PageDescription
  8.04%    2.373      1 Template:CodeEnd
  7.78%    2.295      2 Template:FixedEnd
  7.47%    2.205      1 Template:PageExamples
  7.43%    2.193      1 Template:CodeStart
  7.38%    2.177      2 Template:FixedStart
  6.45%    1.903      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:569-0!canonical and timestamp 20240715061426 and revision id 8997.
 -->
</div>
</div>
</div>
</div>
</body>
</html>