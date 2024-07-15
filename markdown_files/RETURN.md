<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RETURN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RETURN rootpage-RETURN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RETURN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>RETURN</b> is used in <a href="GOSUB" title="GOSUB">GOSUB</a> procedures to return to the original call code line or a specified line label.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><b>RETURN</b> [{<i>linelabel</i>|<i>linenumber</i>}]</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>RETURN without parameters returns to the code immediately following the original <a href="GOSUB" title="GOSUB">GOSUB</a> call.</li>
<li><i>line number</i> or <i>linelabel</i> after the RETURN statement returns code execution to that label.</li></ul>
<p>
<i>Usage:</i>
</p>
<ul><li>Normally required at the end of a <a href="GOSUB" title="GOSUB">GOSUB</a> procedure unless the procedure returns using a loop.</li>
<li>RETURN is not used in error handling procedures. Error procedures use <a href="RESUME" title="RESUME">RESUME</a> <i>line number</i> or <a href="RESUME" title="RESUME">RESUME NEXT</a>.</li>
<li>GOSUB procedures use line numbers or line labels designated with a colon after the number or label.</li>
<li>If RETURN is encountered without a previous <a href="GOSUB" title="GOSUB">GOSUB</a> call a <a href="ERROR_Codes" title="ERROR Codes">"RETURN without GOSUB" error</a> is produced.</li>
<li>To avoid errors, place <a href="GOSUB" title="GOSUB">GOSUB</a> procedures AFTER the main program code <a href="END" title="END">END</a> or after an <a href="EXIT_SUB" title="EXIT SUB">EXIT SUB</a> or <a href="EXIT_FUNCTION" title="EXIT FUNCTION">EXIT FUNCTION</a> call.</li></ul>
<p>
<i>Example 1:</i> Returns after a Gosub.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> a = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> a = 5 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> five
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>       'END or SYSTEM stop the program before the execution of a sub procedure
five:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Aha! Five!"
<a class="mw-selflink selflink"><span style="color:#4593D8;">RETURN</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 1
 2
 3
 4
 5
Aha! Five!
 6
 7
 8
 9
 10
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Returns to a specific line label.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="GOSUB" title="GOSUB"><span style="color:#4593D8;">GOSUB</span></a> hey
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "it didn't go here."
hoho:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "it went here."
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
hey:
<a class="mw-selflink selflink"><span style="color:#4593D8;">RETURN</span></a> hoho
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">it went here.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GOSUB" title="GOSUB">GOSUB</a>, <a href="GOTO" title="GOTO">GOTO</a></li>
<li><a href="RESUME" title="RESUME">RESUME</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192536
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.045 seconds
Preprocessor visited node count: 138/1000000
Post‐expand include size: 1714/2097152 bytes
Template argument size: 156/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.832      1 -total
 25.01%    7.210     15 Template:Cl
  9.13%    2.632      1 Template:PageNavigation
  8.84%    2.548      1 Template:Small
  8.32%    2.398      2 Template:CodeEnd
  8.13%    2.343      2 Template:OutputStart
  7.53%    2.171      2 Template:OutputEnd
  7.48%    2.156      1 Template:PageSeeAlso
  6.72%    1.938      1 Template:PageSyntax
  5.70%    1.642      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:255-0!canonical and timestamp 20240714192536 and revision id 7943.
 -->
</div>
</div>
</div>
</div>
</body>
</html>