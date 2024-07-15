<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_D2G - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-D2G rootpage-D2G skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_D2G</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_D2G</a> function converts a <b>degree</b> value into a <b>gradient</b> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_D2G</a>(<i>num</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.0 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Coverting Degrees into Gradient.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Give me an angle in Degrees "</span>, D
G = <a class="mw-selflink selflink"><span style="color:#4593D8;">_D2G</span></a>(D)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"That angle in Gradient is "</span>; G
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Give me an angle in Degrees 60
That angle in Gradient is  66.66666
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="D2R" title="D2R">_D2R</a></li>
<li><a href="G2D" title="G2D">_G2D</a>, <a href="G2R" title="G2R">_G2R</a></li>
<li><a href="R2D" title="R2D">_R2D</a>, <a href="R2G" title="R2G">_R2G</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192656
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.039 seconds
Preprocessor visited node count: 75/1000000
Post‐expand include size: 1030/2097152 bytes
Template argument size: 119/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 58/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.455      1 -total
  8.91%    2.445      1 Template:PageSeeAlso
  8.61%    2.364      2 Template:Text
  8.30%    2.280      3 Template:Cl
  8.20%    2.251      1 Template:PageSyntax
  7.93%    2.178      1 Template:CodeEnd
  7.69%    2.112      1 Template:PageNavigation
  7.64%    2.097      1 Template:PageExamples
  7.59%    2.085      2 Template:Parameter
  7.52%    2.065      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:75-0!canonical and timestamp 20240714192656 and revision id 8342.
 -->
</div>
</div>
</div>
</div>
</body>
</html>