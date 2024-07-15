<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CONTINUE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CONTINUE rootpage-CONTINUE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CONTINUE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>
The <a class="mw-selflink selflink">_CONTINUE</a> statement is used in a <a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a>, <a href="WHILE...WEND" title="WHILE...WEND">WHILE...WEND</a> or <a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a> block to skip the remaining lines of code in a block (without exiting it) and start the next iteration. It works as a shortcut to a <a href="GOTO" title="GOTO">GOTO</a>, but without the need for a <a href="Line_numbers" title="Line numbers">line label</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_CONTINUE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.2 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">10</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> i = <span style="color:#F580B1;">5</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_CONTINUE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i;
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 1  2  3  4  6  7  8  9  10
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a></li>
<li><a href="WHILE...WEND" title="WHILE...WEND">WHILE...WEND</a></li>
<li><a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a></li>
<li><a href="GOTO" title="GOTO">GOTO</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062305
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.069 seconds
Preprocessor visited node count: 96/1000000
Post‐expand include size: 1179/2097152 bytes
Template argument size: 83/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   51.999      1 -total
 15.08%    7.841      3 Template:Text
 15.00%    7.800      1 Template:PageSyntax
 12.65%    6.580      1 Template:CodeEnd
  9.84%    5.117      1 Template:OutputStart
  9.35%    4.860      1 Template:PageSeeAlso
  7.59%    3.949      1 Template:PageNavigation
  6.21%    3.231      1 Template:PageAvailability
  5.48%    2.852      7 Template:Cl
  4.99%    2.594      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:100-0!canonical and timestamp 20240715062304 and revision id 8293.
 -->
</div>
</div>
</div>
</div>
</body>
</html>