<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_PI - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PI rootpage-PI skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_PI</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_PI</a> function returns <b>π</b> as a <a href="FLOAT" title="FLOAT">_FLOAT</a> value with an optional multiplier parameter.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>circumference</i> = <a class="mw-selflink selflink">_PI</a>[(<i>multiplier</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Optional <i>multiplier</i> (<i>2 * radius</i> in above syntax) allows multiplication of the π value.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Function can be used in to supply π or multiples in a program.</li>
<li>Accuracy is determined by the return variable type <a href="AS" title="AS">AS</a> <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="FLOAT" title="FLOAT">_FLOAT</a>.</li>
<li>The π value can also be derived using 4 * <a href="ATN" title="ATN">ATN</a>(1) for a <a href="SINGLE" title="SINGLE">SINGLE</a> value.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Calculating the area of a circle using a <a href="SINGLE" title="SINGLE">SINGLE</a> variable in this case.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">radius = 5
circlearea = <a class="mw-selflink selflink"><span style="color:#4593D8;">_PI</span></a>(radius ^ 2)
PRINT circlearea
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 78.53982
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ATAN2" title="ATAN2">_ATAN2</a>, <a href="TAN" title="TAN">TAN</a></li>
<li><a href="ATN" title="ATN">ATN</a></li>
<li><a href="SIN" title="SIN">SIN</a>, <a href="COS" title="COS">COS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192829
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.059 seconds
Preprocessor visited node count: 48/1000000
Post‐expand include size: 852/2097152 bytes
Template argument size: 39/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   41.876      1 -total
 23.68%    9.917      1 Template:OutputEnd
  9.16%    3.835      1 Template:PageSyntax
  7.78%    3.258      1 Template:PageParameters
  7.42%    3.105      1 Template:PageDescription
  7.13%    2.986      3 Template:Parameter
  6.25%    2.618      1 Template:PageSeeAlso
  6.16%    2.578      1 Template:Cl
  6.02%    2.523      1 Template:PageNavigation
  5.89%    2.467      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:245-0!canonical and timestamp 20240714192829 and revision id 7644.
 -->
</div>
</div>
</div>
</div>
</body>
</html>