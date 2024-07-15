<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LOOP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LOOP rootpage-LOOP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LOOP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>LOOP</b> statement denotes the end of a <a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a> where the program jumps to the beginning of the loop if the optional condition is true.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>DO</dd>
<dd>.</dd>
<dd>.</dd>
<dd>.</dd>
<dd>LOOP [{UNTIL|WHILE} <i>condition</i>]</dd></dl></dd></dl>
<p>
</p>
<ul><li>LOOP indicates the bottom or end of a <a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a> block of code.</li>
<li>Either the <a href="DO...LOOP" title="DO...LOOP">DO</a> statement or LOOP statement can set a condition to end the loop.</li>
<li>When a loop uses a LOOP condition, the code inside of it will run at least ONCE.</li></ul>
<dl><dd>* A <a class="mw-redirect" href="WHILE" title="WHILE">WHILE</a> condition continues the loop until the condition is false.</dd>
<dd>* An <a href="UNTIL" title="UNTIL">UNTIL</a> condition continues the loop until the condition is true.</dd>
<dd>* If only DO and LOOP are used the loop will never end! <b>Ctrl-Break</b> can be used to stop an endless loop!</dd></dl>
<ul><li>DO LOOPs can also be exited using <a href="EXIT_DO" title="EXIT DO">EXIT DO</a> or <a href="GOTO" title="GOTO">GOTO</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a> {counter loop)</li>
<li><a href="WHILE...WEND" title="WHILE...WEND">WHILE...WEND</a> (loop)</li>
<li><a href="UNTIL" title="UNTIL">UNTIL</a>, <a class="mw-redirect" href="WHILE" title="WHILE">WHILE</a> {conditions)</li>
<li><a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a>, <a href="EXIT_DO" title="EXIT DO">EXIT DO</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714160122
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.013 seconds
Real time usage: 0.016 seconds
Preprocessor visited node count: 9/1000000
Post‐expand include size: 505/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    5.375      1 -total
 35.87%    1.928      1 Template:PageSyntax
 32.76%    1.761      1 Template:PageNavigation
 27.89%    1.499      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:614-0!canonical and timestamp 20240714160122 and revision id 7332.
 -->
</div>
</div>
</div>
</div>
</body>
</html>