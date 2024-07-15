<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>EXP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-EXP rootpage-EXP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">EXP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">EXP</a> math function calculates the exponential function (<b>e</b> raised to the power of a <i>numericExpression</i>).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">EXP</a>(<i>numericExpression</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>e</b> is defined as the base of natural logarithms or as the limit of (1 + 1 / n) ^ n, as n goes to infinity.</li>
<li>When passing <i>numericExpression</i> as a <a href="SINGLE" title="SINGLE">SINGLE</a> variable or as literal number without an explicit type suffix, then it must be less than or equal to <b>88.02969</b> or an <a href="ERROR_Codes" title="ERROR Codes">"overflow" error</a> will occur.</li>
<li>When passing <i>numericExpression</i> as a <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="FLOAT" title="FLOAT">_FLOAT</a> variable, then it must be less than or equal to <b>709.782712893</b> or an <a href="ERROR_Codes" title="ERROR Codes">"overflow" error</a> will occur. You may pass literal numbers as <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="FLOAT" title="FLOAT">_FLOAT</a> values by explicitly adding the <b>#</b> or <b>##</b> type suffix to it respectively, e.g. <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">result = <a class="mw-selflink selflink"><span style="color:#4593D8;">EXP</span></a>(678.9##)</span>.</li>
<li>The value returned is <b>e</b> to the exponent parameter (<b>e = 2.718282</b> approximately).</li>
<li>The precision of the returned values depends on the provided <i>result</i> variable type, but is usually not higher than that of the given <i>numericExpression</i>.</li>
<li>Positive exponent values indicate the number of times to multiply <b>e</b> by itself.</li>
<li>Negative exponent values indicate the number of times to divide by <b>e</b>. Example: <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">e ^ -3 = 1 / e ^ 3 = 1 / (e * e * e)</span></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LOG" title="LOG">LOG</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a href="Mathematical_Operations#Derived_Mathematical_Functions" title="Mathematical Operations">Derived Mathematical Functions</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061310
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.039 seconds
Preprocessor visited node count: 55/1000000
Post‐expand include size: 1123/2097152 bytes
Template argument size: 103/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   21.523      1 -total
 15.69%    3.378      7 Template:Parameter
 12.63%    2.718      1 Template:PageSyntax
 11.19%    2.409      1 Template:PageDescription
 11.00%    2.368      1 Template:PageSeeAlso
 10.94%    2.355      1 Template:PageNavigation
 10.88%    2.342      2 Template:InlineCode
 10.30%    2.217      1 Template:Cl
  9.79%    2.108      2 Template:InlineCodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:467-0!canonical and timestamp 20240715061310 and revision id 8015.
 -->
</div>
</div>
</div>
</div>
</body>
</html>