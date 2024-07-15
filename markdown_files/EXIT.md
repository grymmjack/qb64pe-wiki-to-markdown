<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>EXIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-EXIT rootpage-EXIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">EXIT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">EXIT</a> statement is used to exit certain QBasic procedures.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">EXIT</a> {DO|WHILE|FOR|SUB|FUNCTION|SELECT|CASE}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">EXIT</a> leaves any of the following procedures immediately.
<ul><li><a class="mw-selflink selflink">EXIT</a> DO exits a <a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a>.</li>
<li><a class="mw-selflink selflink">EXIT</a> WHILE exits a <a href="WHILE...WEND" title="WHILE...WEND">WHILE...WEND</a> loop.</li>
<li><a class="mw-selflink selflink">EXIT</a> FOR exits a <a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a> counter loop.</li>
<li><a class="mw-selflink selflink">EXIT</a> SUB exits a <a href="SUB" title="SUB">SUB</a> procedure before it ends. Use before any <a href="GOSUB" title="GOSUB">GOSUB</a> procedures using <a href="RETURN" title="RETURN">RETURN</a>.</li>
<li><a class="mw-selflink selflink">EXIT</a> FUNCTION exits a <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedure before it ends. The value passed by the function's name should be defined.</li>
<li><a class="mw-selflink selflink">EXIT</a> SELECT exits a <a href="SELECT_CASE" title="SELECT CASE">SELECT CASE</a> block.</li>
<li><a class="mw-selflink selflink">EXIT</a> CASE does the same as EXIT SELECT unless when used in a <b>SELECT EVERYCASE</b> block; in such case, execution proceeds to the next CASE evaluation.</li></ul></li>
<li>EXIT statements normally use an <a href="IF...THEN" title="IF...THEN">IF...THEN</a> statement to evaluate a program condition that would require the EXIT.</li>
<li>To exit a program and allow the last program screen to be displayed with the message "Press any key to continue...", use <a href="END" title="END">END</a>.</li>
<li>To exit the program immediately, use <a href="SYSTEM" title="SYSTEM">SYSTEM</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>EXIT SELECT/CASE</b> available in:
<ul><li><b>QB64 v1.5 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul></li>
<li>All other variants available in all versions of QB64</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="EXIT_(function)" title="EXIT (function)">_EXIT (function)</a></li>
<li><a href="END" title="END">END</a>, <a href="SYSTEM" title="SYSTEM">SYSTEM</a></li>
<li><a href="STOP" title="STOP">STOP</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192432
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 15/1000000
Post‐expand include size: 586/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.978      1 -total
 44.55%    8.454      1 Template:PageSyntax
 13.95%    2.647      1 Template:PageDescription
 13.10%    2.487      1 Template:PageAvailability
 12.85%    2.439      1 Template:PageNavigation
 11.92%    2.262      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:311-0!canonical and timestamp 20240714192432 and revision id 5549.
 -->
</div>
</div>
</div>
</div>
</body>
</html>