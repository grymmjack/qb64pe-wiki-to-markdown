<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_BLINK - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BLINK rootpage-BLINK skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_BLINK</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_BLINK</a> statement toggles blinking colors in text mode (SCREEN 0). Default state is ON.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_BLINK</a> {ON|OFF}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>SCREEN 0 emulates the VGA palette with regular colors from 0 to 15 and blinking colors from 16-31 (these are the same colors as 0-15, except their blink attribute is set to on). <a class="mw-selflink selflink">_BLINK</a> OFF emulates writing to the video memory and disabling blinking for colors 16-31.</li>
<li>Using colors 16-31 for the foreground with <a class="mw-selflink selflink">_BLINK</a> set to OFF will produce high intensity background colors.</li>
<li><a class="mw-selflink selflink">_BLINK</a> is only effective in SCREEN 0. It's ignored in graphic modes.</li>
<li>IF <a href="DISPLAY" title="DISPLAY">_DISPLAY</a> is used, blinking is disabled, even if _BLINK is ON, but high intensity backgrounds aren't enabled in this case.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li>Build 20170816/61 up (August 16, 2017).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">16</span>, <span style="color:#F580B1;">7</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"This is printed in black over gray background. Black letters are blinking."</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Hit a key..."</span>
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_BLINK</span></a> <a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Now the same text is printed in black over bright white, because blinking was disabled."</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1319" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="BLINK_(function)" title="BLINK (function)">_BLINK (function)</a></li>
<li><a href="OUT" title="OUT">OUT</a></li>
<li><a href="DISPLAY" title="DISPLAY">_DISPLAY</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714200850
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 117/1000000
Post‐expand include size: 1331/2097152 bytes
Template argument size: 208/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 179/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.092      1 -total
 10.61%    2.026      5 Template:Text
 10.30%    1.966      1 Template:PageSyntax
  9.99%    1.907      7 Template:Cl
  9.40%    1.794      1 Template:PageAvailability
  9.01%    1.720      1 Template:PageDescription
  8.81%    1.682      1 Template:CodeEnd
  8.73%    1.667      1 Template:CodeStart
  8.65%    1.651      1 Template:PageNavigation
  8.41%    1.606      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:56-0!canonical and timestamp 20240714200850 and revision id 8931.
 -->
</div>
</div>
</div>
</div>
</body>
</html>