<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SLEEP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SLEEP rootpage-SLEEP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SLEEP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>SLEEP pauses the program indefinitely or for a specified number of seconds, program is unpaused when the user presses a key or when the specified number of seconds has passed.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>SLEEP [seconds]</dd></dl></dd></dl>
<p>
</p>
<ul><li>Seconds are an optional <a href="INTEGER" title="INTEGER">INTEGER</a> value. If there is no parameter, then it waits for a keypress.</li>
<li>Any user keypress will abort the SLEEP time.</li>
<li>SLEEP does NOT clear the keyboard buffer so it can affect <a href="INKEY$" title="INKEY$">INKEY$</a>, <a href="INPUT" title="INPUT">INPUT</a>, <a href="INPUT$" title="INPUT$">INPUT$</a> and <a href="LINE_INPUT" title="LINE INPUT">LINE INPUT</a> reads.</li>
<li>Use an <a href="INKEY$" title="INKEY$">INKEY$</a> keyboard buffer clearing loop when an empty keyboard buffer is necessary.</li>
<li>SLEEP allows other programs to share the processor time during the interval.</li></ul>
<p>
<i>Example:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press a key..."
<a class="mw-selflink selflink"><span style="color:#4593D8;">SLEEP</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "You pressed a key, now wait for 2 seconds."
<a class="mw-selflink selflink"><span style="color:#4593D8;">SLEEP</span></a> 2
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "You've waited for 2 seconds."
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "(or you pressed a key)"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Press a key...
You pressed a key, now wait for 2 seconds.
You've waited for 2 seconds.
(or you pressed a key)
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> SLEEP without any arguments waits until a key is pressed, next SLEEP statement uses the argument 2 which means that it will wait for 2 seconds, any number of seconds can be specified.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="TIMER_(function)" title="TIMER (function)">TIMER (function)</a>, <a href="INKEY$" title="INKEY$">INKEY$</a></li>
<li><a href="DELAY" title="DELAY">_DELAY</a>, <a href="LIMIT" title="LIMIT">_LIMIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714101304
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.054 seconds
Preprocessor visited node count: 68/1000000
Post‐expand include size: 997/2097152 bytes
Template argument size: 66/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   42.847      1 -total
 37.99%   16.277      1 Template:OutputStart
 11.70%    5.014      1 Template:CodeEnd
 11.49%    4.922      1 Template:CodeStart
 11.14%    4.774      1 Template:PageSyntax
  9.57%    4.102      7 Template:Cl
  5.58%    2.391      1 Template:OutputEnd
  4.84%    2.076      1 Template:PageSeeAlso
  4.78%    2.049      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:563-0!canonical and timestamp 20240714101304 and revision id 8062.
 -->
</div>
</div>
</div>
</div>
</body>
</html>