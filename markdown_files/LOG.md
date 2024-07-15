<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LOG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LOG rootpage-LOG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LOG</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">LOG</a> math function returns the natural logarithm of a specified numerical value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>logarithm!</i> = <a class="mw-selflink selflink">LOG</a>(<i>value</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>value</i> MUST be greater than 0. <a href="ERROR_Codes" title="ERROR Codes">"Illegal function call" error</a> occurs if negative or zero values are used.</li>
<li>The natural logarithm is the logarithm to the base <b>e = 2.718282</b> (approximately).</li>
<li>The natural logarithm of <i>a</i> is defined as the integral from 1 to <i>a</i> of dx/x.</li>
<li>Returns are default <a href="SINGLE" title="SINGLE">SINGLE</a> precision unless the value parameter uses <a href="DOUBLE" title="DOUBLE">DOUBLE</a> precision.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> <a href="FUNCTION" title="FUNCTION">FUNCTION</a> to find the base ten logarithm of a numerical value.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> FUNCTION Log10#(value AS DOUBLE) <a href="STATIC" title="STATIC"><span style="color:#4593D8;">STATIC</span></a>
   Log10# = LOG(value) / LOG(10.#)
 END FUNCTION
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The natural logarithm of the value is divided by the base 10 logarithm. The LOG of ten is designated as a DOUBLE precision return by using # after the Log10 value. The return tells you the number of times 10 goes into a value.</dd></dl>
<p>
<i>Example 2:</i> A binary FUNCTION to convert <a href="INTEGER" title="INTEGER">INTEGER</a> values using LOG to find the number of digits the return will be.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">FUNCTION BinStr$ (n&amp;)
  IF n&amp; &lt; 0 THEN EXIT FUNCTION            'positive numbers only! negative error!
  FOR p% = 0 TO INT(<a class="mw-selflink selflink"><span style="color:#4593D8;">LOG</span></a>(n&amp; + .1) / <a class="mw-selflink selflink"><span style="color:#4593D8;">LOG</span></a>(2))     ' added +.1 to get 0 to work
    IF n&amp; <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> 2 ^ p% THEN s$ = "1" + s$ ELSE s$ = "0" + s$  'find bits on
  NEXT p%
  IF s$ = "" THEN BinStr$ = "&amp;B0" ELSE BinStr$ = "&amp;B" + s$       'check for zero return
END FUNCTION
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The LOG of a <b>positive</b> <a href="INTEGER" title="INTEGER">INTEGER</a> value is divided by the LOG of 2 to determine the number of binary digits that will be returned. The FOR loop compares the value with the exponents of two and determines if a bit is ON or OFF as "1" or "0".</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1114" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="EXP" title="EXP">EXP</a>, <a href="%26B" title="&amp;B">&amp;B</a> (binary number)</li>
<li><a href="Mathematical_Operations#Derived_Mathematical_Functions" title="Mathematical Operations">Derived Mathematical Functions</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192504
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.031 seconds
Preprocessor visited node count: 63/1000000
Post‐expand include size: 944/2097152 bytes
Template argument size: 50/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.984      1 -total
 13.85%    2.490      1 Template:PageSyntax
 11.97%    2.153      3 Template:Parameter
 11.13%    2.002      4 Template:Cl
 10.44%    1.878      2 Template:CodeStart
 10.33%    1.857      2 Template:CodeEnd
  9.29%    1.671      1 Template:PageExamples
  9.16%    1.647      1 Template:PageSeeAlso
  8.96%    1.611      1 Template:PageDescription
  8.19%    1.472      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:554-0!canonical and timestamp 20240714192504 and revision id 8895.
 -->
</div>
</div>
</div>
</div>
</body>
</html>