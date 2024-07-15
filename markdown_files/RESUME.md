<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RESUME - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RESUME rootpage-RESUME skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RESUME</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>RESUME</b> statement is used with <b>NEXT</b> or a line number or label in an error handling routine.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">RESUME</a> {<b>NEXT</b>|<i>lineLabel</i>|<i>lineNumber</i>}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>NEXT</b> returns execution to the code immediately following the error.</li>
<li>A <i>lineLabel</i> or <i>lineNumber</i> is the code line to return to after an error.</li>
<li>If the line label or number is omitted or the line number = 0, the code execution resumes at the code that created the original error.</li>
<li><a class="mw-selflink selflink">RESUMEcan</a> only be used in ERROR handling routines. Use <a href="RETURN" title="RETURN">RETURN</a> in normal <a href="GOSUB" title="GOSUB">GOSUB</a> procedures.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ON_ERROR" title="ON ERROR">ON ERROR</a>, <a href="ERROR" title="ERROR">ERROR</a></li>
<li><a href="RETURN" title="RETURN">RETURN</a>, <a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a></li>
<li><a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034205
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.028 seconds
Preprocessor visited node count: 28/1000000
Post‐expand include size: 599/2097152 bytes
Template argument size: 38/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   12.242      1 -total
 21.74%    2.661      1 Template:PageSyntax
 20.44%    2.502      4 Template:Parameter
 18.97%    2.323      1 Template:PageNavigation
 16.80%    2.056      1 Template:PageDescription
 15.84%    1.939      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:253-0!canonical and timestamp 20240715034205 and revision id 7659.
 -->
</div>
</div>
</div>
</div>
</body>
</html>