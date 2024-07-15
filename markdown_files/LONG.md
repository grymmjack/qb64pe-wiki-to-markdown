<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LONG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LONG rootpage-LONG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LONG</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">LONG</a> defines a variable as a 4 byte number type definition for larger <a href="INTEGER" title="INTEGER">INTEGER</a> values.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="DIM" title="DIM">DIM</a> <i>variable</i> AS <a class="mw-selflink selflink">LONG</a></dd></dl>
<p>
</p>
<ul><li><a class="mw-selflink selflink">LONG</a> integer values range from -2147483648 to 2147483647.</li>
<li><b>QB64'</b>s <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a class="mw-selflink selflink">LONG</a> integer values range from 0 to 4294967295.</li>
<li><b>QB64</b> <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> values range from 0 to 18446744073709551615.</li>
<li>Decimal point values assigned to a <a class="mw-selflink selflink">LONG</a> variable will be rounded to the nearest whole number.</li>
<li>The LONG variable type suffix is &amp; or ~&amp; for <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>. Suffix can also be placed after a literal or hexadecimal numerical value.</li>
<li><a href="INTEGER64" title="INTEGER64">_INTEGER64</a> uses the <b>&amp;&amp;</b> or <b>~&amp;&amp;</b> <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> suffix.</li>
<li>Values can be converted to 4 byte <a href="ASCII" title="ASCII">ASCII</a> string values using <a href="MKL$" title="MKL$">MKL$</a> and back with <a href="CVL" title="CVL">CVL</a>.</li>
<li><b>When a variable has not been assigned or has no type suffix, the type defaults to <a href="SINGLE" title="SINGLE">SINGLE</a>.</b></li>
<li><b>Warning: QBasic keyword names cannot be used as numerical variable names with or without the type suffix.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DIM" title="DIM">DIM</a>, <a href="DEFLNG" title="DEFLNG">DEFLNG</a></li>
<li><a href="LEN" title="LEN">LEN</a>, <a href="CLNG" title="CLNG">CLNG</a></li>
<li><a href="MKL$" title="MKL$">MKL$</a>, <a href="CVL" title="CVL">CVL</a></li>
<li><a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a></li>
<li><a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a></li>
<li><a href="DEFINE" title="DEFINE">_DEFINE</a>, <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031630
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.012 seconds
Real time usage: 0.016 seconds
Preprocessor visited node count: 13/1000000
Post‐expand include size: 517/2097152 bytes
Template argument size: 8/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    7.559      1 -total
 27.45%    2.075      1 Template:PageSyntax
 24.16%    1.826      1 Template:PageNavigation
 22.18%    1.677      1 Template:PageSeeAlso
 21.52%    1.627      1 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:231-0!canonical and timestamp 20240715031630 and revision id 6080.
 -->
</div>
</div>
</div>
</div>
</body>
</html>