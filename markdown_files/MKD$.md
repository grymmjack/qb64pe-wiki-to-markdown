<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>MKD$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MKD rootpage-MKD skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">MKD$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">MKD$</a> function encodes a <a href="DOUBLE" title="DOUBLE">DOUBLE</a> numerical value into an 8-byte <a href="ASCII" title="ASCII">ASCII</a> <a href="STRING" title="STRING">STRING</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">MKD$</a>(<i>doublePrecisionVariableOrLiteral#</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>doublePrecisionVariableOrLiteral#</i> is converted to eight ASCII characters. To see this in action, try <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">PRINT MKD$(12345678)</span>.</li>
<li><a href="DOUBLE" title="DOUBLE">DOUBLE</a> values can range up to 15 decimal point digits. Decimal point accuracy depends on whole value places taken.</li>
<li>The string value can be converted back to a DOUBLE numerical value using <a href="CVD" title="CVD">CVD</a>.</li>
<li><a href="DOUBLE" title="DOUBLE">DOUBLE</a> numerical variable values <a href="PUT" title="PUT">PUT</a> into a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> file are automatically placed as an MKD$ <a href="ASCII" title="ASCII">ASCII</a> string value.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MKI$" title="MKI$">MKI$</a>, <a href="MKS$" title="MKS$">MKS$</a>, <a href="MKL$" title="MKL$">MKL$</a></li>
<li><a href="CVD" title="CVD">CVD</a>, <a href="CVI" title="CVI">CVI</a>, <a href="CVS" title="CVS">CVS</a>, <a href="CVL" title="CVL">CVL</a></li>
<li><a href="MK$" title="MK$">_MK$</a>, <a href="CV" title="CV">_CV</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192509
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.024 seconds
Real time usage: 0.034 seconds
Preprocessor visited node count: 29/1000000
Post‐expand include size: 833/2097152 bytes
Template argument size: 73/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.081      1 -total
 16.93%    3.231      3 Template:Parameter
 15.14%    2.889      1 Template:InlineCode
 14.20%    2.710      1 Template:PageSyntax
 14.08%    2.687      1 Template:PageDescription
 11.83%    2.257      1 Template:PageSeeAlso
 11.34%    2.164      1 Template:PageNavigation
 11.10%    2.118      1 Template:InlineCodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:534-0!canonical and timestamp 20240714192509 and revision id 7344.
 -->
</div>
</div>
</div>
</div>
</body>
</html>