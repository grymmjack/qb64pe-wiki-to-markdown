<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_LASTAXIS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LASTAXIS rootpage-LASTAXIS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_LASTAXIS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_LASTAXIS</a> function returns the number of axis a specified number INPUT device on your computer has.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>axisCount%</i> = <a class="mw-selflink selflink">_LASTAXIS</a>(<i>deviceNumber</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns the number of axis that can be read on a specified device number within the number of <a href="DEVICES" title="DEVICES">_DEVICES</a> found.</li>
<li>A valid number can be sent to the <a href="AXIS" title="AXIS">_AXIS</a> function to find any relative axis movements.</li>
<li>The devices are listed in a numerical order determined by the OS and can be read by the <a href="DEVICE$" title="DEVICE$">DEVICE$</a> function.</li>
<li><b>The <a href="DEVICES" title="DEVICES">_DEVICES</a> function must be read before using _LASTAXIS or an <a href="ERROR_Codes" title="ERROR Codes">"Illegal Function Call" error</a> will occur.</b></li>
<li>Devices include keyboard(1), mouse(2), joysticks, game pads and multiple stick game controllers.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Checking for the system's input devices and number of axis.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">devices = <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a>  'MUST be read in order for other 2 device functions to work!
PRINT "Number of input devices found ="; devices
FOR i = 1 TO devices
  PRINT <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i)
  IF <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(<a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i), "[AXIS]") THEN PRINT "Axis:"; <a class="mw-selflink selflink"><span style="color:#4593D8;">_LASTAXIS</span></a>(i)
NEXT
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Number of input devices found = 2
[KEYBOARD][BUTTON]
[MOUSE][BUTTON][AXIS][WHEEL]
Axis: 2
</pre>
</td></tr></tbody></table>
<dl><dd>Note: The <a href="STRIG" title="STRIG">STRIG</a>/<a href="STICK" title="STICK">STICK</a> commands won't read from the keyboard or mouse device the above example lists.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>, <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a></li>
<li><a href="AXIS" title="AXIS">_AXIS</a>, <a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="WHEEL" title="WHEEL">_WHEEL</a></li>
<li><a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICES" title="DEVICES">_DEVICES</a></li>
<li><a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a></li>
<li><a href="STRIG" title="STRIG">STRIG</a>, <a href="STICK" title="STICK">STICK</a></li>
<li><a href="ON_STRIG(n)" title="ON STRIG(n)">ON STRIG(n)</a>, <a href="STRIG(n)" title="STRIG(n)">STRIG(n)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062350
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 69/1000000
Post‐expand include size: 1032/2097152 bytes
Template argument size: 98/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.394      1 -total
 11.36%    2.545      1 Template:CodeStart
  9.27%    2.075      5 Template:Cl
  9.19%    2.057      1 Template:PageSyntax
  9.04%    2.024      1 Template:PageExamples
  8.51%    1.905      1 Template:PageSeeAlso
  8.46%    1.895      1 Template:PageNavigation
  8.20%    1.836      1 Template:PageDescription
  7.58%    1.697      1 Template:OutputEnd
  7.49%    1.677      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:165-0!canonical and timestamp 20240715062350 and revision id 6063.
 -->
</div>
</div>
</div>
</div>
</body>
</html>