<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_LASTWHEEL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LASTWHEEL rootpage-LASTWHEEL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_LASTWHEEL</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_LASTWHEEL</a> function returns the number of wheels a specified number INPUT device on your computer has.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>wheelCount%</i> = <a class="mw-selflink selflink">_LASTWHEEL</a>(<i>deviceNumber</i>)</dd></dl>
<p>
</p>
<ul><li>Returns the number of wheels that can be used on a specified device number within the number of <a href="DEVICES" title="DEVICES">_DEVICES</a> found.</li>
<li>A valid number can be sent to the <a href="WHEEL" title="WHEEL">_WHEEL</a> function to find any relative positive or negative wheel movements.</li>
<li>The devices are listed in a numerical order determined by the OS and can be read by the <a href="DEVICE$" title="DEVICE$">_DEVICE$</a> function.</li>
<li><b>The <a href="DEVICES" title="DEVICES">_DEVICES</a> function must be read before using _LASTWHEEL or an <a href="ERROR_Codes" title="ERROR Codes">"Illegal Function Call" error</a> may occur.</b></li>
<li>Devices include keyboard (reported as 1), mouse (reported as 2), joysticks, game pads and multiple stick game controllers.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Checking for the system's input devices and number of wheels available.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">devices = <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a>  'MUST be read in order for other 2 device functions to work!
PRINT "Number of input devices found ="; devices
FOR i = 1 TO devices
  PRINT <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i)
  IF <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(<a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i), "[WHEEL]") THEN PRINT "Wheels:"; <a class="mw-selflink selflink"><span style="color:#4593D8;">_LASTWHEEL</span></a>(i)
NEXT
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Number of input devices found = 2
[KEYBOARD][BUTTON]
[MOUSE][BUTTON][AXIS][WHEEL]
Wheels: 3
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> A mouse may have 3 wheels listed when there is only one scroll wheel.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LASTBUTTON" title="LASTBUTTON">_LASTBUTTON</a>, <a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a></li>
<li><a href="AXIS" title="AXIS">_AXIS</a>, <a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="WHEEL" title="WHEEL">_WHEEL</a></li>
<li><a href="DEVICE$" title="DEVICE$">_DEVICE$</a>, <a href="DEVICES" title="DEVICES">_DEVICES</a></li>
<li><a href="MOUSEBUTTON" title="MOUSEBUTTON">_MOUSEBUTTON</a></li>
<li><a href="STRIG" title="STRIG">STRIG</a>, <a href="STICK" title="STICK">STICK</a></li>
<li><a href="ON_STRIG(n)" title="ON STRIG(n)">ON STRIG(n)</a>, <a href="STRIG(n)" title="STRIG(n)">STRIG(n)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062351
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.020 seconds
Real time usage: 0.026 seconds
Preprocessor visited node count: 66/1000000
Post‐expand include size: 995/2097152 bytes
Template argument size: 101/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   16.828      1 -total
 12.82%    2.158      1 Template:PageSyntax
 10.93%    1.839      2 Template:Parameter
  9.91%    1.668      1 Template:PageExamples
  9.90%    1.665      5 Template:Cl
  8.73%    1.469      1 Template:OutputEnd
  8.51%    1.432      1 Template:CodeEnd
  8.44%    1.421      1 Template:CodeStart
  8.44%    1.420      1 Template:OutputStart
  8.28%    1.393      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:167-0!canonical and timestamp 20240715062351 and revision id 6065.
 -->
</div>
</div>
</div>
</div>
</body>
</html>