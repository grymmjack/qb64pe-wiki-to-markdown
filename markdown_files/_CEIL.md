<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CEIL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CEIL rootpage-CEIL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CEIL</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CEIL</a> function rounds a numeric value up to the next whole number or <a href="INTEGER" title="INTEGER">INTEGER</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_CEIL</a>(<i>expression</i>)</dd></dl>
<p>
</p>
<ul><li><a class="mw-selflink selflink">_CEIL</a> returns he smallest integral value that is greater than the numerical <i>expression</i> (as a floating-point value).</li>
<li>This means that <a class="mw-selflink selflink">_CEIL</a> rounds up for both positive and negative numbers.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.0 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Displaying the rounding behavior of <a href="INT" title="INT">INT</a>, <a href="CINT" title="CINT">CINT</a> and <a href="FIX" title="FIX">FIX</a> vs <a class="mw-selflink selflink">_CEIL</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<span style="color:#F580B1;">2.5</span>), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(<span style="color:#F580B1;">2.5</span>), <a href="FIX" title="FIX"><span style="color:#4593D8;">FIX</span></a>(<span style="color:#F580B1;">2.5</span>), <a class="mw-selflink selflink"><span style="color:#4593D8;">_CEIL</span></a>(<span style="color:#F580B1;">2.5</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<span style="color:#F580B1;">-2.5</span>), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(<span style="color:#F580B1;">-2.5</span>), <a href="FIX" title="FIX"><span style="color:#4593D8;">FIX</span></a>(<span style="color:#F580B1;">-2.5</span>), <a class="mw-selflink selflink"><span style="color:#4593D8;">_CEIL</span></a>(<span style="color:#F580B1;">-2.5</span>)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 2        2         2         3
-3       -2        -2        -2
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="INT" title="INT">INT</a>, <a href="FIX" title="FIX">FIX</a></li>
<li><a href="CINT" title="CINT">CINT</a>, <a href="CLNG" title="CLNG">CLNG</a>,</li>
<li><a href="CSNG" title="CSNG">CSNG</a>, <a href="CDBL" title="CDBL">CDBL</a></li>
<li><a href="ROUND" title="ROUND">_ROUND</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211309
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.046 seconds
Preprocessor visited node count: 164/1000000
Post‐expand include size: 1566/2097152 bytes
Template argument size: 190/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   32.464      1 -total
 16.42%    5.331      1 Template:PageAvailability
 11.71%    3.802      1 Template:CodeEnd
  7.05%    2.289      1 Template:PageSyntax
  7.04%    2.285     10 Template:Cl
  6.79%    2.206      1 Template:CodeStart
  6.72%    2.182      1 Template:OutputEnd
  6.70%    2.176      1 Template:OutputStart
  6.68%    2.168      1 Template:PageNavigation
  6.61%    2.147      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:83-0!canonical and timestamp 20240714211309 and revision id 8276.
 -->
</div>
</div>
</div>
</div>
</body>
</html>