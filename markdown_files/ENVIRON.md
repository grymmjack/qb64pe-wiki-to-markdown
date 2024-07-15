<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ENVIRON - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ENVIRON rootpage-ENVIRON skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ENVIRON</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">ENVIRON</a> statement is used to temporarily set or change an environmental string value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">ENVIRON</a> <i>stringExpression$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>stringExpression$</i> must include the environmental parameter ID and the setting:
<ul><li>Using an <b>=</b> sign: <a class="mw-selflink selflink">ENVIRON</a> "parameterID=setting"</li>
<li>Using a space: <a class="mw-selflink selflink">ENVIRON</a> "parameterID setting"</li></ul></li>
<li>If the parameter ID did not previously exist in the environmental string table, it is appended to the end of the table.</li>
<li>If a parameter ID did exist, it is deleted and the new value is appended to end of the list.</li>
<li>Any changes made at runtime are discarded when your program ends.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ENVIRON$" title="ENVIRON$">ENVIRON$</a></li>
<li><a href="Windows_Environment" title="Windows Environment">Windows Environment</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192425
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.015 seconds
Real time usage: 0.019 seconds
Preprocessor visited node count: 20/1000000
Post‐expand include size: 587/2097152 bytes
Template argument size: 34/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    9.205      1 -total
 22.39%    2.061      1 Template:PageSyntax
 18.93%    1.743      2 Template:Parameter
 18.77%    1.728      1 Template:PageNavigation
 17.76%    1.635      1 Template:PageDescription
 17.51%    1.612      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:462-0!canonical and timestamp 20240714192425 and revision id 553.
 -->
</div>
</div>
</div>
</div>
</body>
</html>