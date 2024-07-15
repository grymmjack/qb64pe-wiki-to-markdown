<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_LASTBUTTON - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LASTBUTTON rootpage-LASTBUTTON skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_LASTBUTTON</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_LASTBUTTON</a> function returns the number of buttons a specified INPUT device on your computer has.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>buttonCount%</i> = _<a class="mw-selflink selflink">_LASTBUTTON</a>(<i>deviceNumber</i>)</dd></dl>
<p>
</p>
<ul><li>Returns the number of buttons that can be read on a specified device number within the number of <a href="DEVICES" title="DEVICES">_DEVICES</a> found.</li>
<li>A valid number can be sent to the <a href="BUTTON" title="BUTTON">_BUTTON</a> or <a href="BUTTONCHANGE" title="BUTTONCHANGE">_BUTTONCHANGE</a> function to find any button events.</li>
<li>The specific device name and functions can be found by the <a href="DEVICE$" title="DEVICE$">_DEVICE$</a> function <a href="STRING" title="STRING">string</a>.</li>
<li>The devices are listed in a numerical order determined by the OS and can be read by the <a href="DEVICE$" title="DEVICE$">DEVICE$</a> function.</li>
<li><b>The <a href="DEVICES" title="DEVICES">_DEVICES</a> function must be read before using _LASTBUTTON or an <a href="ERROR_Codes" title="ERROR Codes">"Illegal Function Call" error</a> will occur.</b></li>
<li>Devices include keyboard (reported as 1), mouse (reported as 2), joysticks, game pads and multiple stick game controllers.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Checking for the system's input devices.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">devices = <a href="DEVICES" title="DEVICES"><span style="color:#4593D8;">_DEVICES</span></a>  'MUST be read in order for other 2 device functions to work!
PRINT "Number of input devices found ="; devices
FOR i = 1 TO devices
  PRINT <a href="DEVICE$" title="DEVICE$"><span style="color:#4593D8;">_DEVICE$</span></a>(i)
  PRINT "Buttons:"; <a class="mw-selflink selflink"><span style="color:#4593D8;">_LASTBUTTON</span></a>(i)
NEXT
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
<dl><dd>Note: The <a href="STRIG" title="STRIG">STRIG</a>/<a href="STICK" title="STICK">STICK</a> commands won't read from the keyboard or mouse device the above example lists.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LASTAXIS" title="LASTAXIS">_LASTAXIS</a>, <a href="LASTWHEEL" title="LASTWHEEL">_LASTWHEEL</a></li>
<li><a href="AXIS" title="AXIS">_AXIS</a>, <a href="BUTTON" title="BUTTON">_BUTTON</a>, <a href="WHEEL" title="WHEEL">_WHEEL</a></li>
<li><a href="DEVICES" title="DEVICES">_DEVICES</a>, <a href="DEVICE$" title="DEVICE$">_DEVICE$</a></li>
<li><a href="DEVICEINPUT" title="DEVICEINPUT">_DEVICEINPUT</a></li>
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
CPU time usage: 0.027 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 52/1000000
Post‐expand include size: 890/2097152 bytes
Template argument size: 78/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.200      1 -total
 10.41%    2.416      1 Template:PageExamples
 10.13%    2.350      2 Template:Parameter
 10.12%    2.347      1 Template:PageSyntax
  9.72%    2.255      3 Template:Cl
  9.27%    2.150      1 Template:PageNavigation
  9.26%    2.149      1 Template:CodeStart
  9.08%    2.106      1 Template:PageSeeAlso
  9.00%    2.089      1 Template:OutputEnd
  8.67%    2.011      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:166-0!canonical and timestamp 20240715062350 and revision id 6064.
 -->
</div>
</div>
</div>
</div>
</body>
</html>