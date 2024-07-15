<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>FIX - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FIX rootpage-FIX skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">FIX</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">FIX</a> function rounds a numerical value to the next whole number closest to zero.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">FIX</a>(<i>expression</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>expression</i> is any <a href="Data_types" title="Data types">type</a> of literal or variable numerical value or mathematical calculation.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">FIX</a> effectively truncates (removes) the fractional part of <i>expression</i>, returning the integer part.
<ul><li>This means that <a class="mw-selflink selflink">FIX</a> rounds down for positive values and up for negative values.</li></ul></li>
<li>Use <a href="INT" title="INT">INT</a> to round down negative values. Positive values are rounded down by both.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Showing the behavior of <a class="mw-selflink selflink">FIX</a> with positive and negative decimal point values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> PRINT FIX(2.5)
 PRINT FIX(-2.5)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">2
-2
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> The NORMAL arithmetic method (round half up) can be achieved using the function in the example code below:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> MATHROUND(0.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> MATHROUND(1.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> MATHROUND(2.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> MATHROUND(3.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> MATHROUND(4.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> MATHROUND(5.5)
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> MATHROUND(n)
    MATHROUND = <a class="mw-selflink selflink"><span style="color:#4593D8;">FIX</span></a>(n + 0.5 * <a href="SGN" title="SGN"><span style="color:#4593D8;">SGN</span></a>(n))
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">1
2
3
4
5
6
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CEIL" title="CEIL">_CEIL</a></li>
<li><a href="INT" title="INT">INT</a>, <a href="CINT" title="CINT">CINT</a></li>
<li><a href="CLNG" title="CLNG">CLNG</a>, <a href="ROUND" title="ROUND">_ROUND</a></li>
<li><a href="MOD" title="MOD">MOD</a>, <a href="%5C" title="\">Integer Division</a></li>
<li><a href="/" title="/">Normal division</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714200706
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 120/1000000
Post‐expand include size: 1473/2097152 bytes
Template argument size: 148/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.799      1 -total
 10.32%    2.353     10 Template:Cl
  9.10%    2.075      1 Template:PageSyntax
  8.42%    1.920      4 Template:Parameter
  7.67%    1.748      1 Template:PageSeeAlso
  7.53%    1.717      2 Template:OutputEnd
  7.50%    1.710      2 Template:CodeStart
  7.14%    1.629      2 Template:CodeEnd
  7.13%    1.625      1 Template:PageNavigation
  6.97%    1.589      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:540-0!canonical and timestamp 20240714200706 and revision id 6413.
 -->
</div>
</div>
</div>
</div>
</body>
</html>