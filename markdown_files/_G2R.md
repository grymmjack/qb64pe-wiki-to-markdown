<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_G2R - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-G2R rootpage-G2R skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_G2R</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_G2R</a> function converts a <b>gradient</b> value into a <b>radian</b> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_G2R</a>(<i>num</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.0 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Coverting Gradient into Radians.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <span style="color:#FFB100;">"Give me an angle in Gradient "</span>, G
R = <a class="mw-selflink selflink"><span style="color:#4593D8;">_G2R</span></a>(G)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"That angle in Radians is "</span>; R
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Give me an angle in Gradient 60
That angle in Radians is  .9424778
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="D2G" title="D2G">_D2G</a>, <a href="D2R" title="D2R">_D2R</a></li>
<li><a href="G2D" title="G2D">_G2D</a>, <a class="mw-selflink selflink">_G2R</a></li>
<li><a href="R2D" title="R2D">_R2D</a>, <a href="R2G" title="R2G">_R2G</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062339
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.062 seconds
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
100.00%   44.695      1 -total
 21.25%    9.496      3 Template:Cl
 11.38%    5.086      1 Template:CodeEnd
 10.17%    4.544      2 Template:Text
  9.78%    4.373      1 Template:CodeStart
  5.84%    2.611      1 Template:PageSyntax
  5.71%    2.554      1 Template:OutputStart
  5.65%    2.526      2 Template:Parameter
  5.52%    2.467      1 Template:PageExamples
  5.37%    2.401      1 Template:PageAvailability
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:79-0!canonical and timestamp 20240715062339 and revision id 8345.
 -->
</div>
</div>
</div>
</div>
</body>
</html>