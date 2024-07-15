<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>MKS$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MKS rootpage-MKS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">MKS$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">MKS$</a> function encodes a <a href="SINGLE" title="SINGLE">SINGLE</a> numerical value into a 4-byte <a href="ASCII" title="ASCII">ASCII</a> <a href="STRING" title="STRING">STRING</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">MKS$</a>(<i>singlePrecisionVariableOrLiteral#</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>singlePrecisionVariableOrLiteral#</i> is converted to four ASCII characters. To see this in action, try <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">PRINT MKS$(1345678)</span>.</li>
<li><a href="SINGLE" title="SINGLE">SINGLE</a> values can range up to 7 decimal point digits. Decimal point accuracy depends on whole value places taken.</li>
<li><a class="mw-selflink selflink">MKS$</a> string values can be converted back to SINGLE numerical values using the <a href="CVS" title="CVS">CVS</a> function.</li>
<li><a href="SINGLE" title="SINGLE">SINGLE</a> numerical variable values <a href="PUT" title="PUT">PUT</a> into a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> file are automatically placed as an <a class="mw-selflink selflink">MKS$</a> <a href="ASCII" title="ASCII">ASCII</a> string value.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MKI$" title="MKI$">MKI$</a>, <a href="MKD$" title="MKD$">MKD$</a>, <a href="MKL$" title="MKL$">MKL$</a></li>
<li><a href="CVD" title="CVD">CVD</a>, <a href="CVI" title="CVI">CVI</a>, <a href="CVS" title="CVS">CVS</a>, <a href="CVL" title="CVL">CVL</a></li>
<li><a href="MK$" title="MK$">_MK$</a>, <a href="CV" title="CV">_CV</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061344
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.020 seconds
Real time usage: 0.029 seconds
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
100.00%   18.789      1 -total
 23.44%    4.405      1 Template:PageSyntax
 12.64%    2.375      1 Template:InlineCodeEnd
 12.18%    2.289      1 Template:InlineCode
 12.10%    2.274      3 Template:Parameter
 11.92%    2.239      1 Template:PageSeeAlso
 11.71%    2.200      1 Template:PageDescription
 10.19%    1.915      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:538-0!canonical and timestamp 20240715061344 and revision id 632.
 -->
</div>
</div>
</div>
</div>
</body>
</html>