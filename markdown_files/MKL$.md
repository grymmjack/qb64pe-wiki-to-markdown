<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>MKL$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MKL rootpage-MKL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">MKL$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">MKL$</a> function encodes a <a href="LONG" title="LONG">LONG</a> numerical value into a 4-byte <a href="ASCII" title="ASCII">ASCII</a> <a href="STRING" title="STRING">STRING</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">MKL$</a>(<i>longVariableOrLiteral&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>longVariableOrLiteral&amp;</i> is converted to four ASCII characters. To see this in action, try <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">PRINT MKL$(12345678)</span>.</li>
<li>The numerical data usually takes up less bytes than printing the <a href="LONG" title="LONG">LONG</a> number to a file.</li>
<li><a href="LONG" title="LONG">LONG</a> integer values can range from -2147483648 to 2147483647.</li>
<li>Since the representation of a long number can use up to 10 ASCII characters (ten bytes), writing to a file using <a class="mw-selflink selflink">MKL$</a> conversion, and then reading back with the <a href="CVL" title="CVL">CVL</a> conversion can save up to 6 bytes of storage space.</li>
<li><a href="CVL" title="CVL">CVL</a> can convert the value back to a <a href="LONG" title="LONG">LONG</a> numerical value.</li>
<li><a href="LONG" title="LONG">LONG</a> numerical variable values <a href="PUT" title="PUT">PUT</a> into a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> file are automatically placed as an MKL$ <a href="ASCII" title="ASCII">ASCII</a> string value.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p>See examples in:
</p>
<ul><li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a href="SaveIcon32" title="SaveIcon32">SaveIcon32</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MKI$" title="MKI$">MKI$</a>, <a href="MKS$" title="MKS$">MKS$</a>, <a href="MKD$" title="MKD$">MKD$</a></li>
<li><a href="CVD" title="CVD">CVD</a>, <a href="CVI" title="CVI">CVI</a>, <a href="CVS" title="CVS">CVS</a>, <a href="CVL" title="CVL">CVL</a></li>
<li><a href="MK$" title="MK$">_MK$</a>, <a href="CV" title="CV">_CV</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061343
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.021 seconds
Real time usage: 0.028 seconds
Preprocessor visited node count: 32/1000000
Post‐expand include size: 848/2097152 bytes
Template argument size: 51/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   15.131      1 -total
 15.10%    2.284      1 Template:PageSyntax
 13.36%    2.021      1 Template:PageNavigation
 12.44%    1.882      1 Template:PageSeeAlso
 11.26%    1.704      3 Template:Parameter
 11.15%    1.687      1 Template:InlineCode
 11.05%    1.672      1 Template:PageDescription
 10.42%    1.576      1 Template:PageExamples
 10.19%    1.541      1 Template:InlineCodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:537-0!canonical and timestamp 20240715061343 and revision id 8661.
 -->
</div>
</div>
</div>
</div>
</body>
</html>